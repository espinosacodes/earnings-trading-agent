"""Fetch market data and compute pre-earnings quantitative metrics.

Writes a JSON payload to stdout that is consumed by analyze.py.
"""
import json
import os
import sys

import numpy as np
import pandas as pd
import yfinance as yf
from scipy import stats

DEFAULT_PEERS = ["MSFT", "ORCL", "CRM", "SNOW", "NOW", "DDOG"]
DRIFT_WINDOWS = (1, 3, 5, 7, 10, 15, 20, 30)


def _naive(s: pd.Series) -> pd.Series:
    if s.index.tz is not None:
        s.index = s.index.tz_convert(None)
    return s


def earnings_events(t: yf.Ticker, hist: pd.DataFrame) -> pd.DataFrame:
    """One row per past earnings date: price reaction + EPS surprise."""
    closes = _naive(hist["Close"].copy())
    try:
        ed = t.earnings_dates
    except Exception:
        ed = None
    if ed is None or ed.empty:
        return pd.DataFrame(columns=["date", "return", "surprise_pct", "estimated", "actual"])

    rows = []
    for date, row in ed.iterrows():
        d = pd.Timestamp(date)
        d = d.tz_convert(None) if d.tzinfo is not None else d
        pos = closes.index.searchsorted(d)
        if pos == 0 or pos >= len(closes):
            continue
        prev, nxt = closes.iloc[pos - 1], closes.iloc[pos]
        rows.append(
            {
                "date": d,
                "return": (nxt - prev) / prev * 100,
                "surprise_pct": None if pd.isna(row.get("Surprise(%)")) else float(row["Surprise(%)"]),
                "estimated": None if pd.isna(row.get("EPS Estimate")) else float(row["EPS Estimate"]),
                "actual": None if pd.isna(row.get("Reported EPS")) else float(row["Reported EPS"]),
            }
        )
    return pd.DataFrame(rows).sort_values("date").reset_index(drop=True)


def pre_earnings_drift(closes: pd.Series, dates: pd.Series) -> dict:
    """Mean return and win rate of buying N days before earnings, selling the
    session before the release. This is the pre-announcement drift edge."""
    closes = _naive(closes.copy())
    dates = pd.to_datetime(dates)
    out = {w: [] for w in DRIFT_WINDOWS}
    for d in dates:
        d = d.tz_convert(None) if d.tzinfo is not None else d
        pos = closes.index.searchsorted(d)
        for w in DRIFT_WINDOWS:
            if pos - 1 - w < 0 or pos - 1 >= len(closes):
                continue
            entry, exit_ = closes.iloc[pos - 1 - w], closes.iloc[pos - 1]
            if entry > 0:
                out[w].append((exit_ - entry) / entry * 100)
    return {
        str(w): {
            "mean_pct": round(float(np.mean(v)), 2),
            "median_pct": round(float(np.median(v)), 2),
            "win_rate_pct": round(float(np.mean([x > 0 for x in v]) * 100), 1),
            "count": len(v),
        }
        for w, v in out.items()
        if v
    }


def drift_signal(drift: dict) -> dict:
    """Pick the pre-earnings window with the best risk-adjusted drift."""
    best = None
    for w, m in drift.items():
        score = m["mean_pct"] * m["win_rate_pct"] / 100
        if best is None or score > best["score"]:
            best = {"window_days": int(w), "score": round(score, 2), **m}
    return best


def surprise_vs_move(events: pd.DataFrame) -> dict | None:
    df = events.dropna(subset=["return", "surprise_pct"])
    if len(df) < 4:
        return None
    r = float(np.corrcoef(df["surprise_pct"], df["return"])[0, 1])
    slope, intercept = np.polyfit(df["surprise_pct"], df["return"], 1)
    return {
        "pearson_r": round(r, 3),
        "slope_pct_per_surprise": round(float(slope), 3),
        "n": int(len(df)),
    }


def surprise_momentum(events: pd.DataFrame) -> str | None:
    s = events["surprise_pct"].dropna().tail(4)
    if len(s) < 2:
        return None
    slope = np.polyfit(range(len(s)), s.astype(float), 1)[0]
    return "expanding" if slope > 0 else "decelerating"


def options_iv(t: yf.Ticker, spot: float, earnings_date: str | None = None) -> dict | None:
    try:
        exps = t.options
    except Exception:
        return None
    if not exps:
        return None
    exp = None
    if earnings_date:
        edate = pd.Timestamp(earnings_date)
        for e in exps:
            if pd.Timestamp(e) >= edate:
                exp = e
                break
    if exp is None:
        for e in exps:
            if (pd.Timestamp(e) - pd.Timestamp.now()).days >= 14:
                exp = e
                break
    if exp is None:
        exp = exps[0]
    try:
        chain = t.option_chain(exp)
    except Exception:
        return None
    calls, puts = chain.calls, chain.puts
    if calls.empty or puts.empty:
        return None
    strike = min(calls["strike"], key=lambda s: abs(s - spot))
    call = calls[calls["strike"] == strike].iloc[0]
    put = puts[puts["strike"] == strike].iloc[0]
    straddle = float(call["lastPrice"] + put["lastPrice"])
    return {
        "expiration": exp,
        "atm_strike": float(strike),
        "atm_call_iv_pct": round(float(call["impliedVolatility"]) * 100, 2),
        "atm_put_iv_pct": round(float(put["impliedVolatility"]) * 100, 2),
        "straddle_price": round(straddle, 2),
        "implied_move_pct": round(straddle / spot * 100, 2) if spot else None,
    }


def peer_premium(ticker: str, info: dict, peers: list[str]) -> dict:
    rows = []
    for p in peers:
        if p == ticker:
            continue
        try:
            pi = yf.Ticker(p).info or {}
            rows.append((p, pi.get("trailingPE"), pi.get("priceToSalesTrailing12Months")))
        except Exception:
            continue
    if not rows:
        return {}
    pes = [r[1] for r in rows if r[1] and r[1] > 0]
    pss = [r[2] for r in rows if r[2] and r[2] > 0]
    avg_pe = float(np.mean(pes)) if pes else None
    avg_ps = float(np.mean(pss)) if pss else None
    own_pe, own_ps = info.get("trailingPE"), info.get("priceToSalesTrailing12Months")
    return {
        "peers": [r[0] for r in rows],
        "peer_avg_trailing_pe": round(avg_pe, 2) if avg_pe else None,
        "peer_avg_price_to_sales": round(avg_ps, 2) if avg_ps else None,
        "pe_premium_pct": round((own_pe / avg_pe - 1) * 100, 1) if own_pe and avg_pe else None,
        "ps_premium_pct": round((own_ps / avg_ps - 1) * 100, 1) if own_ps and avg_ps else None,
    }


def rsi(close: pd.Series, period: int = 14) -> float:
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / period, min_periods=period).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / period, min_periods=period).mean()
    rs = gain / loss.replace(0, np.nan)
    return float(100 - 100 / (1 + rs).iloc[-1])


def volume_profile(hist: pd.DataFrame, bins: int = 50, top: int = 3):
    price = (hist["High"] + hist["Low"]) / 2
    edges = np.linspace(price.min(), price.max(), bins + 1)
    centers = (edges[:-1] + edges[1:]) / 2
    vol = np.histogram(price, bins=edges, weights=hist["Volume"])[0]
    idx = np.argsort(vol)[::-1][:top]
    return [{"price": round(float(centers[i]), 2), "volume": int(vol[i])} for i in idx]


def fetch(ticker: str, peers: list[str]) -> dict:
    t = yf.Ticker(ticker)
    hist = t.history(period="5y", auto_adjust=True)
    info = t.info or {}

    if hist.empty:
        sys.exit(f"no price data for {ticker}")

    close = hist["Close"]
    logret = np.log(close / close.shift(1)).dropna()
    hv30 = float(logret.tail(30).std() * np.sqrt(252) * 100)

    def dist_to_ema(span: int) -> float:
        ema = close.ewm(span=span, adjust=False).mean().iloc[-1]
        return float((close.iloc[-1] - ema) / ema * 100)

    events = earnings_events(t, hist)
    moves = events["return"]
    moves8 = moves.tail(8)

    drift = pre_earnings_drift(close, events["date"])
    drift_best = drift_signal(drift)

    next_earnings = None
    try:
        now = pd.Timestamp.now()
        future = []
        for d in t.earnings_dates.index:
            dd = pd.Timestamp(d)
            dd = dd.tz_convert(None) if dd.tzinfo is not None else dd
            if dd > now:
                future.append(dd)
        next_earnings = str(future[0].date()) if future else None
    except Exception:
        pass

    dist = moves if len(moves) else pd.Series(dtype=float)
    dist_stats = {
        "count": int(len(dist)),
        "mean_pct": round(float(dist.mean()), 2),
        "std_pct": round(float(dist.std()), 2),
        "min_pct": round(float(dist.min()), 2),
        "max_pct": round(float(dist.max()), 2),
        "skew": round(float(stats.skew(dist)), 2) if len(dist) > 2 else None,
        "kurtosis": round(float(stats.kurtosis(dist)), 2) if len(dist) > 3 else None,
        "prob_abs_move_gt_10pct": round(float(np.mean(dist.abs() > 10) * 100), 1),
        "prob_abs_move_gt_15pct": round(float(np.mean(dist.abs() > 15) * 100), 1),
    }

    return {
        "ticker": ticker,
        "last_close": round(float(close.iloc[-1]), 2),
        "next_earnings_date": next_earnings,
        "days_to_earnings": (pd.Timestamp(next_earnings) - pd.Timestamp.now()).days if next_earnings else None,
        "earnings_distribution": dist_stats,
        "earnings_day_returns_8q": [round(x, 2) for x in moves8.tolist()],
        "mean_abs_earnings_move_pct": round(float(moves8.abs().mean()), 2) if len(moves8) else None,
        "max_earnings_drawdown_pct": round(float(moves8.min()), 2) if len(moves8) else None,
        "max_earnings_gain_pct": round(float(moves8.max()), 2) if len(moves8) else None,
        "hv_30d_pct": round(hv30, 2),
        "pre_earnings_drift": drift,
        "best_entry_window": drift_best,
        "surprise_vs_move_corr": surprise_vs_move(events),
        "surprise_momentum": surprise_momentum(events),
        "rsi_14": round(rsi(close), 2),
        "dist_to_ema21_pct": round(dist_to_ema(21), 2),
        "dist_to_ema50_pct": round(dist_to_ema(50), 2),
        "dist_to_ema200_pct": round(dist_to_ema(200), 2),
        "volume_profile_top3": volume_profile(hist.tail(180)),
        "trailing_pe": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),
        "price_to_sales": info.get("priceToSalesTrailing12Months"),
        "market_cap": info.get("marketCap"),
        "revenue_growth": info.get("revenueGrowth"),
        "profit_margins": info.get("profitMargins"),
        "sector": info.get("sector"),
        "peer_premium": peer_premium(ticker, info, peers),
        "options": options_iv(t, float(close.iloc[-1]), next_earnings),
        "eps_surprise_history": _eps_surprises(events),
    }


def _eps_surprises(events: pd.DataFrame) -> list:
    out = []
    for _, row in events.tail(8).iterrows():
        out.append(
            {
                "date": str(row["date"].date()),
                "estimated": round(row["estimated"], 4) if row["estimated"] is not None else None,
                "actual": round(row["actual"], 4) if row["actual"] is not None else None,
                "surprise_pct": row["surprise_pct"],
            }
        )
    return out


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    ticker = (os.getenv("TICKER") or "PLTR").upper()
    peers = [p.strip().upper() for p in (os.getenv("PEERS") or ",".join(DEFAULT_PEERS)).split(",") if p.strip()]
    print(json.dumps(fetch(ticker, peers), indent=2))
