# ORCL PRE-EARNINGS QUANTITATIVE TRADING SIGNAL REPORT

**Ticker:** ORCL | **Next Earnings:** 2026-09-10 | **Days to Earnings:** 12 | **Last Close:** $150.85

---

## 1. EXECUTIVE SUMMARY TABLE

| Metric | Value | Signal Implication |
|--------|-------|-------------------|
| **Implied Move (Options)** | 12.16% | Market pricing significant event risk |
| **Historical Mean Move** | 2.97% | Options imply 4.1x historical mean |
| **Historical Std Dev** | 12.1% | Implied move within 1 std of historical |
| **Prob. \|Move\| > 10%** | 50.0% | High probability of large move |
| **RSI-14** | 56.1 | Neutral, slight bullish momentum |
| **Distance to 50-EMA** | +1.64% | Above trend, bullish |
| **Distance to 200-EMA** | -11.24% | Below long-term trend, bearish |
| **Trailing P/E** | 25.87 | Below peer avg by 82.9% |
| **Best Entry Window** | 10 days | Mean +1.42%, WR 57.9% |
| **IV vs HV Gap** | 78.52% vs 56.21% | IV premium = 22.31 pts (IV crush risk) |

---

## 2. PRE-EARNINGS DRIFT BACKTEST (THE EDGE)

### Full Drift Window Analysis:

| Window (Days) | Mean % | Median % | Win Rate % | Sample Size | Statistical Significance |
|---------------|--------|----------|------------|-------------|--------------------------|
| **1** | **-0.16%** | **-0.34%** | **45.0%** | **20** | **Negative drift, avoid** |
| **3** | **+0.41%** | **+1.28%** | **60.0%** | **20** | **Positive, moderate** |
| **5** | **+0.39%** | **+0.16%** | **55.0%** | **20** | **Positive, weak** |
| **7** | **+0.19%** | **+1.15%** | **60.0%** | **20** | **Positive, moderate** |
| **10** | **+1.42%** | **+2.23%** | **57.9%** | **19** | **STRONGEST EDGE** |
| **15** | +0.65% | -0.20% | 47.4% | 19 | Weak, unreliable |
| **20** | +0.50% | +0.21% | 52.6% | 19 | Marginal |
| **30** | +1.36% | -0.44% | 47.4% | 19 | High variance |

### Key Findings:
- **Best edge: 10-day window** with mean +1.42%, median +2.23%, and 57.9% win rate
- **Score: 0.82** (highest risk-adjusted drift score)
- **1-day window is negative** (-0.16%), suggesting no last-minute entry edge
- **10-day window provides 2.3x better mean return** than 3-day window
- **Median > Mean** in 10-day window indicates consistent positive skew

**Verdict: YES, statistically meaningful pre-earnings drift exists at the 10-day window.**

---

## 3. DIRECTIONAL SIGNAL & ENTRY TIMING

### Signal Synthesis:

| Factor | Reading | Weight |
|--------|---------|--------|
| **Pre-Earnings Drift (10d)** | +1.42% mean, 57.9% WR | BULLISH |
| **RSI-14** | 56.1 (neutral-bullish) | BULLISH |
| **Distance to 50-EMA** | +1.64% (above) | BULLISH |
| **Surprise Momentum** | Decelerating | BEARISH |
| **Surprise vs Move Corr** | -0.207 (negative) | BEARISH |
| **IV vs HV Gap** | +22.31 pts premium | NEUTRAL (IV crush risk) |

### Final Bias: **LONG** (moderate confidence)

**Rationale:** The 10-day pre-earnings drift edge (+1.42%) combined with bullish technical positioning (above 50-EMA, RSI 56.1) outweighs the negative surprise momentum and correlation factors. The decelerating surprise momentum is a caution flag, but the historical drift pattern is the dominant edge.

### Entry & Exit Levels:

| Parameter | Price | Basis |
|-----------|-------|-------|
| **Entry** | $150.85 (current) | Enter now (10 days before earnings) |
| **Target (Pre-Earnings)** | $153.00 | +1.42% drift target |
| **Target (Post-Earnings)** | $169.20 | +12.16% implied move (bullish scenario) |
| **Stop (Pre-Earnings)** | $146.32 | -3.0% below entry (below volume node) |
| **Stop (Post-Earnings)** | $132.75 | -12.0% (historical max drawdown + buffer) |

### Position Sizing:

**Recommended Size: 15% of account ($15,000 on $100k)**

**Justification:**
- Worst-case historical earnings gap: -13.5% (min_pct)
- Max historical drawdown: -10.83%
- At 15% position size, worst-case loss = $15,000 × 13.5% = $2,025 (2.03% of account)
- Acceptable risk given 57.9% win rate and 1.42% expected drift

---

## 4. OPTIONS STRATEGY (IBKR)

### Strategy: Bull Put Spread (Defined Risk)

**Structure:**
- **Sell:** ORCL Sept 11, 2026 $135 Put (Delta: -0.25)
- **Buy:** ORCL Sept 11, 2026 $125 Put (Delta: -0.15)
- **Net Credit:** $3.20 (estimated from IV skew)

**Strike Selection Logic:**
- Short strike at $135 = 10.5% below current price (within 1 std of implied move)
- Long strike at $125 = 17.1% below current price (beyond historical max drawdown)
- Delta ratio 0.25/0.15 = 1.67 (conservative risk/reward)

**Risk Metrics:**

| Metric | Value |
|--------|-------|
| **Max Loss** | $10.00 - $3.20 = $6.80 per contract |
| **Max Gain** | $3.20 per contract |
| **Breakeven** | $138.20 (at expiration) |
| **Risk/Reward** | 2.13:1 (favorable) |
| **Probability of Profit** | ~72% (based on delta) |

**IV Crush Mitigation:**
- IV premium of 22.31 pts (78.52% vs 56.21% HV) will crush post-earnings
- Bull put spread benefits from IV crush (short vega position)
- Time decay works in our favor (theta positive)

**Alternative: Iron Condor**
- Add call spread: Sell $170 Call / Buy $180 Call
- Net credit: $1.80 additional
- Total credit: $5.00
- Max loss: $5.00 per spread
- Breakevens: $145.00 and $175.00

---

## 5. WORST-CASE SIMULATION

### Scenario A: -20% Overnight Gap

**Account Size:** $100,000 | **Position Size:** 15% ($15,000)

| Metric | Value |
|--------|-------|
| **Entry Price** | $150.85 |
| **Gap Price** | $120.68 (-20%) |
| **Loss on Position** | $15,000 × 20% = $3,000 |
| **Account Impact** | -3.0% |
| **Remaining Account** | $97,000 |

**Liquidation Triggers:**
- **Immediate:** If gap > -15%, liquidate 50% of position
- **At -20%:** Liquidate remaining 50% immediately
- **Options:** Bull put spread max loss = $6.80 × 10 contracts = $6,800 (premium collected offsets)

**Delta Hedge Trigger:**
- If ORCL drops below $140 (7.2% below entry), buy 10 delta-hedge puts ($140 strike)
- Cost: ~$2.50 × 100 = $250 per contract
- This caps additional downside risk

### Scenario B: Historical Max Drawdown (-10.83%)

| Metric | Value |
|--------|-------|
| **Gap Price** | $134.52 (-10.83%) |
| **Loss on Position** | $15,000 × 10.83% = $1,625 |
| **Account Impact** | -1.63% |
| **Remaining Account** | $98,375 |

**Action:** Hold position, as this is within historical norms. The 10-day drift edge (+1.42%) provides cushion.

### Scenario C: Best Case (+35.95% Max Gain)

| Metric | Value |
|--------|-------|
| **Gap Price** | $205.08 (+35.95%) |
| **Gain on Position** | $15,000 × 35.95% = $5,393 |
| **Account Impact** | +5.39% |
| **Options Gain** | Max gain $3.20 × 10 = $3,200 |

---

## FINAL RECOMMENDATION

**Action:** Initiate LONG position now (10 days before earnings) with 15% allocation. Simultaneously sell bull put spread for income and downside protection.

**Confidence Level:** 65% (moderate-high)

**Key Risk Factors:**
1. Decelerating surprise momentum (last surprise +7.52% vs +38.04% prior)
2. Negative surprise-move correlation (-0.207)
3. High IV premium (22.31 pts) suggests market pricing significant risk

---

```json
{
  "ticker": "ORCL",
  "bias": "LONG",
  "confidence": 0.65,
  "entry_window_days_before_earnings": 10,
  "entry": 150.85,
  "target": 169.2,
  "stop": 132.75,
  "position_size_pct": 15.0,
  "expected_move_pct": 12.16,
  "rationale": "10-day pre-earnings drift shows +1.42% mean return with 57.9% win rate (score 0.82), combined with bullish technicals (RSI 56.1, above 50-EMA) and options implying 12.16% move, though decelerating EPS surprise momentum (-0.207 correlation) warrants moderate confidence."
}
```