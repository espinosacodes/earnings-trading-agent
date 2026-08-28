"""Fetch market data and compute pre-earnings quantitative metrics.

Writes a JSON payload to stdout that is consumed by analyze.py.
"""
import json
import sys

import numpy as np
import pandas as pd
import yfinance as yf


def earnings_day_returns(ticker: yf.Ticker, hist: pd.DataFrame):
    """Return DataFrame of earnings-day % returns using reported EPS dates."""
    try:
        ed = ticker.earnings_dates
    except Exception:
        ed = None
    if ed is None or ed.empty:
        return pd.DataFrame(columns=["return"])

    closes = hist["Close"].copy()
    if closes.index.tz is not None:
        closes.index = closes.index.tz_convert(None)
    rows = []
    for date in ed.index:
        date = pd.Timestamp(date)
        date = date.tz_convert(None) if date.tzinfo is not None else date
        prior = closes[closes.index <= date]
        after = closes[closes.index >= date]
        if prior.empty or after.empty:
            continue
        prev_close = prior.iloc[-1]
        next_close = after.iloc[0]
        rows.append((date, (next_close - prev_close) / prev_close * 100))
    return pd.DataFrame(rows, columns=["date", "return"]).set_index("date").sort_index()


def rsi(close: pd.Series, period: int = 14) -> float:
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / period, min_periods=period).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / period, min_periods=period).mean()
    rs = gain / loss.replace(0, np.nan)
    return float(100 - 100 / (1 + rs).iloc[-1])


def volume_profile(hist: pd.DataFrame, bins: int = 50, top: int = 3):
    price = (hist["High"] + hist["Low"]) / 2
    lo, hi = price.min(), price.max()
    edges = np.linspace(lo, hi, bins + 1)
    centers = (edges[:-1] + edges[1:]) / 2
    vol = np.histogram(price, bins=edges, weights=hist["Volume"])[0]
    idx = np.argsort(vol)[::-1][:top]
    return [{"price": round(float(centers[i]), 2), "volume": int(vol[i])} for i in idx]


def fetch(ticker: str) -> dict:
    t = yf.Ticker(ticker)
    hist = t.history(period="2y", auto_adjust=True)
    info = t.info or {}

    if hist.empty:
        sys.exit(f"no price data for {ticker}")

    close = hist["Close"]
    logret = np.log(close / close.shift(1)).dropna()
    hv30 = float(logret.tail(30).std() * np.sqrt(252) * 100)

    def dist_to_ema(span: int) -> float:
        ema = close.ewm(span=span, adjust=False).mean().iloc[-1]
        return float((close.iloc[-1] - ema) / ema * 100)

    moves = earnings_day_returns(t, hist)
    if moves.empty:
        moves8 = pd.Series(dtype=float)
    else:
        moves8 = moves["return"].tail(8)

    return {
        "ticker": ticker,
        "last_close": round(float(close.iloc[-1]), 2),
        "earnings_day_returns_8q": [round(x, 2) for x in moves8.tolist()],
        "mean_abs_earnings_move_pct": round(float(moves8.abs().mean()), 2) if len(moves8) else None,
        "max_earnings_drawdown_pct": round(float(moves8.min()), 2) if len(moves8) else None,
        "max_earnings_gain_pct": round(float(moves8.max()), 2) if len(moves8) else None,
        "hv_30d_pct": round(hv30, 2),
        "rsi_14": round(rsi(close), 2),
        "dist_to_ema21_pct": round(dist_to_ema(21), 2),
        "dist_to_ema50_pct": round(dist_to_ema(50), 2),
        "dist_to_ema200_pct": round(dist_to_ema(200), 2),
        "volume_profile_top3": volume_profile(hist.tail(180)),
        "trailing_pe": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),
        "price_to_sales": info.get("priceToSalesTrailing12Months"),
        "eps_surprise_history": _eps_surprises(t),
    }


def _eps_surprises(t: yf.Ticker):
    try:
        ed = t.earnings_dates
    except Exception:
        return []
    if ed is None or ed.empty:
        return []
    out = []
    for date, row in ed.sort_index().tail(4).iterrows():
        out.append(
            {
                "date": str(date.date()),
                "estimated": None if pd.isna(row.get("EPS Estimate")) else round(float(row["EPS Estimate"]), 4),
                "actual": None if pd.isna(row.get("Reported EPS")) else round(float(row["Reported EPS"]), 4),
                "surprise_pct": None if pd.isna(row.get("Surprise(%)")) else round(float(row["Surprise(%)"]), 2),
            }
        )
    return out


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()
    ticker = (os.getenv("TICKER") or "PLTR").upper()
    print(json.dumps(fetch(ticker), indent=2))
