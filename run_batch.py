"""Run fetch + analyze over a universe of tickers and print a signal summary.

Usage:
    TICKERS=NVDA,AMD,LMT python run_batch.py
    # defaults to DEFAULT_UNIVERSE below
"""
import json
import os

from dotenv import load_dotenv

from analyze import generate_report, write_outputs
from fetch_data import DEFAULT_PEERS, fetch

DEFAULT_UNIVERSE = [
    "PLTR", "NVDA", "AMD", "AVGO", "MSFT", "ORCL", "CRM",
    "LMT", "RTX", "NOC", "GE",
    "MOG-A", "SYM", "MP", "USAR", "TKR", "KOID",
]


def main():
    load_dotenv()
    env = os.getenv("TICKERS", "")
    tickers = [t.strip().upper() for t in env.split(",") if t.strip()] or DEFAULT_UNIVERSE
    peers = [p.strip().upper() for p in os.getenv("PEERS", "").split(",") if p.strip()] or list(DEFAULT_PEERS)

    rows = []
    for t in tickers:
        try:
            metrics = fetch(t, peers)
            report = generate_report(t, metrics)
            write_outputs(t, report)
            with open(os.path.join("reports", f"{t}_signal.json")) as f:
                rows.append(json.load(f))
        except Exception as e:
            print(f"[{t}] SKIP: {e}")

    if not rows:
        return
    hdr = f"{'TICKER':7}{'BIAS':9}{'CONF':6}{'WIN':5}{'SIZE%':7}{'EXP_MOVE%':11}"
    print("\n" + hdr)
    for d in rows:
        print(
            f"{d['ticker']:7}{d['bias']:9}{d['confidence']:<6}{d['entry_window_days_before_earnings']:<5}"
            f"{d['position_size_pct']:<7}{d['expected_move_pct']:<11.2f}"
        )


if __name__ == "__main__":
    main()
