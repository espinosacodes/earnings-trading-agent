# earnings-trading-agent

Automated quantitative pre-earnings analysis. Fetches live market data via
`yfinance`, computes risk metrics, and generates a structured Markdown report
using DeepSeek. Runs locally or on a weekly GitHub Actions schedule.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your DEEPSEEK_API_KEY
```

## Usage

```bash
TICKER=PLTR python fetch_data.py > metrics.json
TICKER=PLTR python analyze.py < metrics.json
# writes reports/PLTR_earnings_report.md + reports/PLTR_signal.json
```

Any ticker works; `TICKER` defaults to `PLTR`. Set `PEERS` (comma-separated)
to override the default software/AI peer set.

## GitHub Actions

- Weekly schedule (Monday 14:00 UTC) plus manual `workflow_dispatch`.
- Add `DEEPSEEK_API_KEY` as a repository secret and `TICKER` as a variable.
- Each run commits a fresh report to `reports/`.

## Layout

- `fetch_data.py` — pulls 5y of prices plus the options chain and computes the
  full quant stack: earnings-day move distribution (mean/std/skew/kurtosis),
  pre-earnings drift backtest per window, best entry window, surprise-vs-move
  correlation, surprise momentum, HV, RSI, EMA distances, volume profile,
  valuation, peer premium, and implied move vs HV.
- `analyze.py` — sends metrics to DeepSeek with `prompts/system_prompt.md`,
  writes the report and extracts the machine-readable trading signal JSON.
- `.github/workflows/earnings_analysis.yml` — automation.
