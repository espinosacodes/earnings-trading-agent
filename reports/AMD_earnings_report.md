# AMD (NASDAQ: AMD) — Pre-Earnings Quantitative Trade Analysis

**Analysis Date:** 2026-08-31 | **Next Earnings:** 2026-11-03 (64 days out)

---

## 1. EXECUTIVE SUMMARY TABLE

| Metric | Value | Signal |
|--------|-------|--------|
| **Implied Move (Options)** | ±21.1% | Extremely elevated |
| **Historical Mean Abs Move** | 8.82% | Options overpricing risk |
| **IV vs HV Gap** | ATM IV 57.5% vs HV 72.4% | IV below realized vol |
| **RSI-14** | 44.83 | Neutral-bearish momentum |
| **Distance to 50-EMA** | -3.62% | Below short-term trend |
| **Distance to 200-EMA** | +26.06% | Above long-term trend |
| **Trailing P/E** | 121.88x | Rich valuation |
| **Best Pre-Earnings Window** | 20 days (mean +6.79%, 60% WR) | Positive drift edge |
| **Recommended Action** | **LONG** — enter 20 days before earnings, exit before release | Drift capture |

---

## 2. PRE-EARNINGS DRIFT BACKTEST (The Edge)

| Window (Days) | Mean Return % | Median % | Win Rate % | Sample Size |
|---------------|---------------|----------|------------|-------------|
| 1 | +1.04 | +0.95 | 60.0 | 20 |
| 3 | +2.60 | +1.92 | 75.0 | 20 |
| 5 | +3.33 | +4.04 | 70.0 | 20 |
| 7 | +1.97 | +1.86 | 60.0 | 20 |
| 10 | +3.02 | +3.70 | 60.0 | 20 |
| **15** | **+5.40** | **+3.94** | **60.0** | **20** |
| **20** | **+6.79** | **+2.80** | **60.0** | **20** |
| 30 | +7.54 | -1.82 | 45.0 | 20 |

**Verdict:** There is a **statistically meaningful positive pre-earnings drift** in AMD. The 20-day window shows +6.79% mean return with 60% win rate. The 30-day window has higher mean (+7.54%) but **negative median (-1.82%) and sub-50% win rate (45%)** — indicating the drift decays and reverses beyond 20 days. The 3-day window offers the best win rate (75%) with +2.60% mean.

---

## 3. HOLD THROUGH EARNINGS OR EXIT BEFORE

**Comparison at Best Window (20 days):**

| Metric | Exit Before (Pre-Drift) | Hold Through | Delta |
|--------|------------------------|--------------|-------|
| Mean Return | +6.79% | +6.43% | **-0.36%** |
| Median Return | +2.80% | -6.09% | **-8.89%** |
| Win Rate | 60% | 45% | **-15%** |

**Verdict: EXIT BEFORE EARNINGS.**

Holding through the release destroys value: median return collapses from +2.80% to **-6.09%**, and win rate drops from 60% to 45%. The earnings-day distribution confirms this — mean of -0.75% with 20% probability of a >10% move against you. The 8-quarter earnings-day returns show 5 negative prints in the last 8 quarters (62.5% negative).

---

## 4. DIRECTIONAL SIGNAL, ENTRY TIMING & HOLDING PERIOD

### Bias: **LONG** (pre-earnings drift capture only)

### Entry Timing
- **Optimal Entry:** 20 days before earnings (2026-10-14)
- **Alternative:** 3-day window (2026-10-31) for higher win rate (75%) but smaller edge
- **Exit:** Day before earnings (2026-11-02) — do NOT hold through release

### Position Levels (based on $465.58 close)

| Level | Price | Basis |
|-------|-------|-------|
| **Entry** | $465.58 | Current price (or limit at $460.00 for better entry) |
| **Target** | $497.20 | Entry + 6.79% (20-day mean drift) |
| **Stop-Loss** | $427.30 | Entry - 2× ATR (2 × $19.14) |

### Position Sizing
- **Recommended Size:** 15% of account
- **Worst-Case Gap:** -17.31% (historical max earnings drawdown)
- **Max Loss at 15% size:** 15% × 17.31% = **2.60% of account**

---

## 5. OPTIONS STRATEGY (IBKR)

### Strategy: Bull Call Spread (Defined Risk)

| Component | Strike | Delta | Premium |
|-----------|--------|-------|---------|
| Buy Call | $470 (ATM) | ~0.50 | ~$49.13 |
| Sell Call | $530 (OTM) | ~0.25 | ~$24.56 |
| **Net Debit** | | | **$24.57** |

**Structure Economics (per contract):**
- **Max Loss:** $2,457 (net debit × 100)
- **Max Gain:** $3,043 (width $60 - debit $24.57) × 100
- **Breakeven:** $494.57 (strike + net debit)
- **Risk/Reward:** 1.24:1

**IV Crush Analysis:**
- ATM IV: 57.49% vs HV: 72.42% — **IV is BELOW realized volatility**
- This is unusual; typically IV > HV before earnings
- IV crush risk is **limited** — options are relatively cheap vs actual volatility
- However, the 21.1% implied move is still 2.4× the historical mean (8.82%)

**Alternative — Iron Condor (if neutral bias):**
- Sell $530 Call / Buy $550 Call
- Sell $410 Put / Buy $390 Put
- Collect ~$15.00 credit, max loss $5.00

---

## 6. WORST-CASE SIMULATION

### Scenario A: -20% Overnight Gap (Post-Earnings)

| Parameter | Value |
|-----------|-------|
| Account Size | $100,000 |
| Position Size | 15% ($15,000) |
| Entry Price | $465.58 |
| Gap Price | $372.46 (-20%) |
| Loss on Position | $3,000 |
| **Account Impact** | **-3.00%** |

**Liquidation Triggers:**
- **Hard Stop:** $427.30 (entry - 2× ATR) — triggers at -8.2%
- **Delta Hedge Trigger:** If position drops below $440 (-5.5%), buy 0.5× position size in puts (strike $440) to cap further downside

### Scenario B: Historical Max Drawdown (-65.45%)

| Parameter | Value |
|-----------|-------|
| Account Size | $100,000 |
| Position Size | 15% ($15,000) |
| Max Drawdown Price | $160.90 |
| Loss on Position | $4,570 |
| **Account Impact** | **-4.57%** |

**Risk Management:** The 2× ATR stop ($427.30) would trigger long before this scenario, limiting actual loss to ~$1,147 (1.15% of account).

---

## MACHINE-READABLE OUTPUT

```json
{
  "ticker": "AMD",
  "asset_type": "stock",
  "bias": "LONG",
  "confidence": 0.65,
  "entry_window_days_before_earnings": 20,
  "entry": 465.58,
  "target": 497.2,
  "stop": 427.3,
  "position_size_pct": 15.0,
  "expected_move_pct": 6.79,
  "hold_through_earnings": false,
  "holding_period_days": 20,
  "rationale": "Positive pre-earnings drift of +6.79% (60% win rate) over 20-day window with median collapse to -6.09% if held through earnings, justifying LONG entry with exit before release."
}
```