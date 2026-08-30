# USAR PRE-EARNINGS QUANTITATIVE TRADING SIGNAL REPORT

**Date:** 2026-08-31 | **Next Earnings:** 2026-11-05 (66 days out)

---

## 1. EXECUTIVE SUMMARY TABLE

| Metric | Value | Signal Implication |
|--------|-------|-------------------|
| **Implied Move (Options)** | ±39.19% | Extremely elevated; market pricing massive binary event |
| **Historical Mean Earnings Move** | +7.14% | Positive drift historically, but small sample (n=6) |
| **Historical Std Dev** | ±9.17% | High dispersion around mean |
| **Prob. Move > 10%** | 16.7% | Low probability of extreme move |
| **Prob. Move > 15%** | 16.7% | Same as >10% — bimodal distribution |
| **RSI-14** | 48.87 | Neutral momentum, no overbought/oversold |
| **Distance to 50-EMA** | -3.73% | Below 50-EMA, bearish tilt |
| **Distance to 200-EMA** | -5.47% | Below 200-EMA, longer-term downtrend |
| **Trailing P/E** | N/A (negative earnings) | Cannot use P/E |
| **Forward P/E** | -415.19 | Deeply negative earnings expectations |
| **Price/Sales** | 334.49 | Extreme valuation vs peers (2,509% premium) |
| **Best Pre-Earnings Entry** | 30 days before | Mean +16.82%, but only 50% win rate |

---

## 2. PRE-EARNINGS DRIFT BACKTEST (THE EDGE)

### Full Drift Table:

| Window (Days) | Mean Return % | Median % | Win Rate % | Sample Size | Statistical Read |
|---------------|--------------|----------|------------|-------------|------------------|
| **1** | **-3.42** | -3.27 | 16.7% | 6 | Strong negative drift into earnings |
| **3** | -1.41 | -6.08 | 33.3% | 6 | Negative drift, weak |
| **5** | -5.82 | -13.78 | 33.3% | 6 | Strong negative drift |
| **7** | -1.95 | -10.36 | 33.3% | 6 | Negative drift |
| **10** | -1.02 | -0.01 | 50.0% | 6 | Neutral |
| **15** | -8.15 | -9.13 | 50.0% | 6 | Strong negative drift |
| **20** | -5.95 | -10.59 | 50.0% | 6 | Negative drift |
| **30** | **+16.82** | +15.53 | 50.0% | 6 | Positive drift, but 50% win rate |

### Statistical Assessment:

**CRITICAL FINDING:** The drift data shows a **bimodal pattern**:
- **Short-term (1-7 days):** Consistently negative mean returns (-1.41% to -5.82%) with low win rates (16.7-33.3%). This suggests selling pressure into earnings.
- **Long-term (30 days):** Positive mean (+16.82%) but only 50% win rate — this is NOT statistically reliable.

**Key Statistical Red Flags:**
1. **Sample size = 6:** No statistical significance possible. The t-statistic for the 30-day window is only 0.84 (not >2.0).
2. **Median vs Mean divergence:** At 5-day window, mean is -5.82% but median is -13.78% — suggests one outlier is pulling the mean up.
3. **Win rates are poor:** Best win rate is only 50% — coin flip.

**VERDICT: NO STATISTICALLY MEANINGFUL PRE-EARNINGS DRIFT EDGE EXISTS.**

---

## 3. DIRECTIONAL SIGNAL & ENTRY TIMING

### Signal Synthesis:

| Factor | Reading | Weight |
|--------|---------|--------|
| Pre-Earnings Drift (1-7d) | Negative (-1.41% to -5.82%) | Bearish |
| Pre-Earnings Drift (30d) | Positive (+16.82%) but unreliable | Neutral |
| RSI-14 | 48.87 (Neutral) | Neutral |
| EMA Positioning | Below 50 & 200 EMA | Bearish |
| Surprise vs Move Correlation | -0.049 (No link) | Neutral |
| Surprise Momentum | Expanding | Mildly Bullish |
| IV vs HV | 94% vs 90% (slight premium) | Neutral |
| Valuation | Extreme premium (2,509% vs peers) | Bearish |
| Earnings History | 4/6 positive moves, mean +7.14% | Mildly Bullish |

### FINAL BIAS: **NEUTRAL (FLAT)**

**Rationale:** The conflicting signals (negative short-term drift vs positive earnings-day history) combined with an extremely small sample size (n=6) and extreme implied move (39.19%) create an unquantifiable risk/reward. The options market is pricing a move 4.3x larger than the historical mean absolute move (8.14%).

### Entry Timing Recommendation:

**DO NOT ENTER A DIRECTIONAL POSITION BEFORE EARNINGS.**

The 1-day drift shows -3.42% mean with only 16.7% win rate — entering long 1 day before earnings has historically lost money 83.3% of the time. The 30-day window shows +16.82% but with 50% win rate, the risk of a -20% gap (as modeled below) far exceeds any expected edge.

---

## 4. OPTIONS STRATEGY (IBKR)

### Strategy: **SHORT STRANGLE** (Defined Risk via Stop)

Given the extreme IV (94% ATM) and the 39.19% implied move, selling premium is statistically favored IF you believe the historical mean absolute move (8.14%) is more representative than the options market's expectation.

**Structure (per contract):**
- **Sell** 1x USAR 2026-12-18 $12.00 Put (Delta ~0.15)
- **Sell** 1x USAR 2026-12-18 $26.00 Call (Delta ~0.15)
- **Buy** 1x USAR 2026-12-18 $8.00 Put (Protection, Delta ~0.05)
- **Buy** 1x USAR 2026-12-18 $32.00 Call (Protection, Delta ~0.05)

**Strike Selection Logic:** Using the implied move of ±39.19%, the 1-standard deviation range is $10.94 to $25.04. We sell at 1.5x implied move ($12/$26) and buy protection at 2.5x implied move ($8/$32).

**Pricing Estimate (based on IV skew):**
- Credit from short put: ~$0.85
- Credit from short call: ~$0.75
- Debit from long put: ~$0.25
- Debit from long call: ~$0.20
- **Net Credit: ~$1.15 per spread**

**Risk Metrics:**
- **Max Loss:** ($12 - $8) - $1.15 = $2.85 per spread (if stock < $8)
- **Max Gain:** $1.15 per spread (if stock stays between $12-$26)
- **Upper Breakeven:** $26 + $1.15 = $27.15
- **Lower Breakeven:** $12 - $1.15 = $10.85
- **Probability of Success:** ~65% (based on historical 8.14% mean move vs 39.19% implied)

**IV Crush Analysis:** With IV at 94% vs HV at 90%, there's only a 4% IV premium. Post-earnings, IV typically drops 20-30%. This strategy benefits from IV crush as short options lose value faster than long options.

**Position Size:** 5 spreads per $100,000 account (max loss = $1,425, or 1.43% of account)

---

## 5. WORST-CASE SIMULATION

### Scenario A: -20% Overnight Gap (Stock drops from $17.99 to $14.39)

**Impact on $100,000 account with 5 short strangles:**

| Position | P&L |
|----------|-----|
| Short $12 Put | +$0.85 (option expires worthless) |
| Short $26 Call | +$0.75 (option expires worthless) |
| Long $8 Put | -$0.25 (option expires worthless) |
| Long $32 Call | -$0.20 (option expires worthless) |
| **Total per spread** | **+$1.15** |
| **Total P&L (5 spreads)** | **+$575** |

**Verdict:** The -20% gap is WITHIN our short put strike ($12) — we profit because the stock stays above our short strike.

### Scenario B: Historical Max Drawdown (-2.32% earnings-day move)

Stock drops from $17.99 to $17.57. All options expire worthless. **P&L: +$575** (full credit captured).

### Scenario C: Catastrophic -50% Gap (Stock drops to $9.00)

| Position | P&L |
|----------|-----|
| Short $12 Put | -$3.00 |
| Long $8 Put | +$1.00 |
| Short $26 Call | +$0.75 |
| Long $32 Call | -$0.20 |
| **Total per spread** | **-$1.45** |
| **Total P&L (5 spreads)** | **-$725** |

**Liquidation Triggers:**
1. **Delta Hedge Trigger:** If stock drops below $13.50 (1.5x short strike), buy 100 shares per short put to neutralize delta.
2. **Stop-Loss Trigger:** Close entire position if loss exceeds $2,000 (2% of account).
3. **Time Stop:** Close all positions 2 days before earnings if IV hasn't decayed as expected.

---

## FINAL RECOMMENDATION

**DO NOT TRADE DIRECTIONALLY.** The data does not support a statistically valid directional edge. The only actionable strategy is the short strangle to harvest the extreme IV premium, sized conservatively at 1.43% max risk.

---

```json
{
  "ticker": "USAR",
  "bias": "NEUTRAL",
  "confidence": 0.15,
  "entry_window_days_before_earnings": 0,
  "entry": 0.0,
  "target": 0.0,
  "stop": 0.0,
  "position_size_pct": 0.0,
  "expected_move_pct": 39.19,
  "rationale": "No statistically significant pre-earnings drift edge exists (best window 30d has only 50% win rate with n=6), while options imply a 39.19% move versus 8.14% historical mean absolute move, making directional positioning a negative expectancy bet."
}
```