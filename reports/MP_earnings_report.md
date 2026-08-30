# MP EARNINGS TRADING SIGNAL REPORT

## 1. EXECUTIVE SUMMARY TABLE

| Metric | Value | Signal Implication |
|--------|-------|-------------------|
| **Implied Move (Options)** | 29.22% | Extremely elevated; market pricing massive event risk |
| **Historical Mean Earnings Move** | 0.8% | Actual expected move much smaller than implied |
| **Historical Std Dev** | 6.13% | 1σ move = ±6.13%; 2σ = ±12.26% |
| **RSI-14** | 53.69 | Neutral; no overbought/oversold condition |
| **Distance to 50-EMA** | +4.13% | Slightly extended above trend |
| **Distance to 200-EMA** | +1.16% | Near long-term trend |
| **Forward P/E** | 63.43x | Rich valuation |
| **P/S Premium vs Peers** | +87.3% | Significant premium to peer group |
| **Best Pre-Earnings Window** | 30 days | Mean +3.65%, but median -5.13% (negative skew) |
| **Surprise Momentum** | Decelerating | Last quarter surprise was -173.22% (miss) |

---

## 2. PRE-EARNINGS DRIFT BACKTEST (THE EDGE)

### Complete Drift Window Analysis:

| Window (Days) | Mean % | Median % | Win Rate % | Sample Size | Risk-Adjusted Score |
|---------------|--------|----------|------------|-------------|-------------------|
| 1 | +0.91% | +0.30% | 60.0% | 20 | Moderate |
| 3 | +0.97% | -0.72% | 50.0% | 20 | Low |
| 5 | +0.32% | -0.85% | 35.0% | 20 | Negative |
| 7 | +1.20% | -0.45% | 50.0% | 20 | Low |
| 10 | +0.08% | -1.59% | 40.0% | 20 | Negative |
| 15 | -1.84% | -0.93% | 40.0% | 20 | Negative |
| 20 | +2.88% | -0.24% | 50.0% | 20 | Moderate |
| **30** | **+3.65%** | **-5.13%** | **45.0%** | **20** | **1.64 (Best)** |

### Critical Findings:

**The "best" window (30 days) is a statistical illusion.** While the mean is +3.65%, the median is -5.13%, and the win rate is only 45%. This indicates:
- **Extreme positive outliers** are driving the mean
- **Most periods actually lose money** (55% of the time)
- The distribution is **negatively skewed** (median << mean)

**The only statistically meaningful window is 1-day:** +0.91% mean with 60% win rate. This is the only window where the median (+0.30%) aligns with the mean direction.

**Conclusion: NO reliable pre-earnings drift edge exists.** The 30-day window's positive mean is driven by outliers, not consistent behavior. The 1-day window offers marginal positive expectancy but insufficient magnitude to justify risk.

---

## 3. DIRECTIONAL SIGNAL & ENTRY TIMING

### Signal Synthesis:

| Factor | Reading | Weight |
|--------|---------|--------|
| **Pre-Earnings Drift** | Weak/Unreliable | Negative |
| **Surprise Momentum** | Decelerating (last miss: -173.22%) | Negative |
| **Surprise vs Move Correlation** | -0.109 (inverse) | Negative |
| **IV vs HV Spread** | 71% IV vs 74.7% HV (IV < HV) | Neutral |
| **Technical Position** | Above 50-EMA (+4.13%), RSI 53.69 | Neutral |
| **Valuation** | 87.3% P/S premium to peers | Negative |
| **Historical Earnings Distribution** | Mean +0.8%, 10% chance of >10% move | Neutral |

### Final Recommendation: **NEUTRAL (FLAT)**

**Rationale:**
1. **No directional edge**: Surprise momentum is decelerating, correlation between surprises and price moves is negative (-0.109), and the last quarter was a significant miss
2. **Unreliable drift**: The 30-day "best" window has 55% losing probability
3. **Extreme implied move**: 29.22% implied move vs 5.57% historical average suggests options are pricing in tail risk that may not materialize
4. **Rich valuation**: 87.3% P/S premium to peers limits upside potential

### If Forced to Trade (Low Probability):
- **Bias**: NEUTRAL (no directional position)
- **Entry**: No entry before earnings; wait for post-earnings confirmation
- **Entry Price**: N/A
- **Target**: N/A
- **Stop**: N/A
- **Position Size**: 0% (flat)

---

## 4. OPTIONS STRATEGY (IBKR)

### Recommended Structure: **Short Straddle (Defined-Risk via Spread)**

Given the extreme IV (71% call, 64.8% put) and the historical mean move of only 0.8%, selling premium is statistically favored.

### Strategy: **Iron Condor**

| Leg | Strike | Type | Delta Target |
|-----|--------|------|--------------|
| Sell Call | $65 (ATM + ~16%) | Call | ~0.20 |
| Buy Call | $70 (ATM + ~25%) | Call | ~0.10 |
| Sell Put | $45 (ATM - ~20%) | Put | ~0.20 |
| Buy Put | $40 (ATM - ~29%) | Put | ~0.10 |

### Position Metrics (per contract):

| Metric | Value |
|--------|-------|
| **Max Loss** | $500 (width between strikes) |
| **Max Gain** | ~$400 (net credit received) |
| **Upper Breakeven** | ~$69 |
| **Lower Breakeven** | ~$41 |
| **Probability of Success** | ~70% (based on historical 6.13% std dev) |

### IV Crush Analysis:
- **Current IV**: 71% (call), 64.8% (put)
- **Historical HV**: 74.7%
- **IV is NOT elevated** relative to realized volatility
- **Risk**: IV may expand further if volatility persists; position sizing must account for this

### Alternative: **Long Put Spread (Bearish Hedge)**
- Buy $50 Put / Sell $45 Put
- Cost: ~$1.50
- Max Gain: $3.50
- Breakeven: $48.50

---

## 5. WORST-CASE SIMULATION

### Scenario 1: -20% Overnight Gap on $100,000 Account

**Position Size**: 0% (flat) → No loss from gap

**If position were 5% ($5,000)**:
- Loss: $1,000 (20% of position)
- Account impact: -1.0%

### Scenario 2: Historical Max Drawdown (-7.97%)

**Position Size**: 0% (flat) → No loss

**If position were 5% ($5,000)**:
- Loss: $398.50
- Account impact: -0.40%

### Scenario 3: Options Position (Iron Condor)

**Max Loss**: $500 per contract
- With 2 contracts: $1,000 max loss
- Account impact: -1.0%

### Risk Management Triggers:

| Trigger | Action |
|---------|--------|
| **Delta exceeds +0.25** | Close call spread |
| **Delta exceeds -0.25** | Close put spread |
| **Loss reaches 50% of max** | Reduce position by 50% |
| **IV drops below 50%** | Close entire position (IV crush complete) |
| **Price breaks $70 or $40** | Liquidate immediately |

---

## FINAL MACHINE-READABLE OUTPUT

```json
{
  "ticker": "MP",
  "bias": "NEUTRAL",
  "confidence": 0.65,
  "entry_window_days_before_earnings": 0,
  "entry": 0.0,
  "target": 0.0,
  "stop": 0.0,
  "position_size_pct": 0.0,
  "expected_move_pct": 5.57,
  "rationale": "No reliable directional edge: surprise momentum decelerating (-173.22% last miss), negative surprise-price correlation (-0.109), and unreliable pre-earnings drift (30-day window has 55% losing probability despite positive mean) warrant flat positioning ahead of earnings."
}
```

---

**DISCLAIMER**: This analysis is based on historical statistical patterns and does not guarantee future results. The recommended NEUTRAL stance reflects the absence of a statistically significant edge, not a prediction of direction. Any options strategies should be sized appropriately for the account and risk tolerance.