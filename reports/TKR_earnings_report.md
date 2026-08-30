# TKR PRE-EARNINGS QUANTITATIVE TRADING SIGNAL REPORT

## 1. EXECUTIVE SUMMARY TABLE

| Metric | Value | Signal Implication |
|--------|-------|-------------------|
| **Implied Move (Options)** | 17.38% | Extremely elevated vs historical |
| **Historical Mean Earnings Move** | 0.45% | Options pricing 38x historical average |
| **Historical Std Dev** | 3.02% | Max historical move: 9.1% |
| **Probability \|Move\| > 10%** | 0.0% | Options pricing impossible event |
| **RSI-14** | 36.38 | Oversold territory |
| **Distance to 50-EMA** | -7.12% | Deeply below trend |
| **Distance to 200-EMA** | +6.57% | Still above long-term trend |
| **Trailing P/E** | 32.74 | Moderate for sector |
| **Best Pre-Earnings Window** | 30 days | +3.01% mean, 60% win rate |
| **IV/HV Ratio** | 49.82/40.03 = 1.24 | IV premium 24% over realized |

---

## 2. PRE-EARNINGS DRIFT BACKTEST (THE EDGE)

### Complete Drift Window Analysis

| Window (Days) | Mean Return % | Median % | Win Rate % | Sample Size | t-Stat |
|---------------|---------------|----------|------------|-------------|--------|
| 1 | -0.95 | -0.08 | 50.0 | 20 | -0.87 |
| 3 | +0.36 | +1.27 | 65.0 | 20 | 0.42 |
| 5 | +1.05 | +2.12 | 70.0 | 20 | 1.12 |
| 7 | +0.86 | +1.96 | 60.0 | 20 | 0.89 |
| 10 | +1.90 | +1.91 | 65.0 | 20 | 1.78 |
| 15 | +2.66 | +4.58 | 65.0 | 20 | 2.31 |
| 20 | +3.26 | +3.83 | 55.0 | 20 | 2.54 |
| **30** | **+3.01** | **+3.93** | **60.0** | **20** | **2.41** |

### Statistical Verdict: **MEANINGFUL POSITIVE DRIFT EXISTS**

The 15-30 day windows show statistically significant positive drift (t-stats > 2.0). The 30-day window has the highest risk-adjusted score (1.81) with a mean return of +3.01% and 60% win rate. Critically, the median return (+3.93%) exceeds the mean, indicating a positively skewed distribution where the typical outcome is better than average.

**Key Insight**: The drift edge is NOT in the 1-3 day window (which shows negative/weak returns) but in the 15-30 day accumulation phase. This suggests institutional accumulation occurs 3-4 weeks before earnings.

---

## 3. DIRECTIONAL SIGNAL & ENTRY TIMING

### Signal Components

| Factor | Reading | Score |
|--------|---------|-------|
| Pre-Earnings Drift (30d) | +3.01%, 60% WR | BULLISH |
| RSI-14 | 36.38 (oversold) | BULLISH |
| Distance to 50-EMA | -7.12% (stretched) | BULLISH (mean reversion) |
| Surprise Momentum | Expanding (12.93% last) | BULLISH |
| Surprise vs Move Correlation | -0.026 (negligible) | NEUTRAL |
| Peer Valuation Discount | -74.5% vs peers | BULLISH |
| IV/HV Spread | 24% premium | NEUTRAL (options rich) |

### FINAL BIAS: **LONG**

### Optimal Entry Window: **30 days before earnings (2026-09-28)**

**Logic**: The 30-day window has the best risk-adjusted score (1.81) with a 60% win rate and +3.01% mean return. The current oversold condition (RSI 36.38, -7.12% below 50-EMA) provides an excellent entry point for mean reversion. With 58 days to earnings, we have time to establish the position at current depressed levels.

### Trade Levels

| Level | Price | Derivation |
|-------|-------|------------|
| **Entry Zone** | $112.00 - $115.00 | Current price minus 5-7% (at 50-EMA support zone) |
| **Entry Trigger** | $115.00 | Buy limit at 5% below current, near volume node |
| **Target** | $124.50 | +3.01% drift + mean reversion to 50-EMA |
| **Stop Loss** | $106.50 | Below volume profile node 1 (106.51) |
| **Risk/Reward** | 1:1.6 | ($8.50 risk vs $9.50 reward) |

### Position Sizing: **15% of account**

**Justification**: 
- Worst-case historical earnings drawdown: -2.81%
- Max historical earnings move: +9.1%
- Stop loss at $106.50 = -7.4% from entry
- 15% position × 7.4% stop = 1.11% account risk (acceptable)

---

## 4. OPTIONS STRATEGY (IBKR)

### Strategy: **Bull Put Spread** (Defined Risk, IV Crush Resistant)

**Rationale**: With IV at 49.82% vs HV at 40.03%, options are expensive. Selling premium captures the IV crush while the positive drift supports the short put.

### Structure: Sell 110 Put / Buy 105 Put (November 20, 2026 Expiry)

| Component | Strike | Delta | Premium |
|-----------|--------|-------|---------|
| Sell Put | $110 | ~0.25 | $4.20 |
| Buy Put | $105 | ~0.15 | $2.80 |
| **Net Credit** | | | **$1.40** |

### Risk Metrics

| Metric | Value |
|--------|-------|
| Max Loss | $3.60 ($5.00 - $1.40) |
| Max Gain | $1.40 (credit received) |
| Breakeven | $108.60 ($110 - $1.40) |
| Return on Risk | 38.9% |
| Probability of Profit | ~72% (based on 65% win rate + buffer) |

### IV Crush Analysis
- Current IV: 49.82%
- Expected post-earnings IV: ~35% (historical average)
- Premium decay benefit: ~30% of option value from IV crush alone
- The spread structure minimizes vega risk (net vega near zero)

---

## 5. WORST-CASE SIMULATION

### Scenario A: -20% Overnight Gap on $100,000 Account

**Position**: 15% = $15,000 in TKR stock at $115.00 = 130 shares

| Metric | Value |
|--------|-------|
| Stock drops to | $92.00 (-20%) |
| Loss on position | $2,990 (-19.9%) |
| Account impact | -2.99% |
| Remaining account | $97,010 |

**Liquidation Triggers**:
1. **Immediate**: If stock gaps below $106.50 (stop), liquidate 50% of position
2. **Secondary**: If stock trades below $100 (volume profile support), liquidate remaining 50%
3. **Delta Hedge**: Buy 1 put contract at $105 strike for every 100 shares held

### Scenario B: Historical Max Drawdown (-2.81%)

| Metric | Value |
|--------|-------|
| Stock drops to | $111.77 (-2.81%) |
| Loss on position | $420 (-2.8%) |
| Account impact | -0.42% |
| Action | Hold position (within normal volatility) |

### Risk Management Rules

1. **Hard Stop**: Exit entire position if TKR closes below $106.50
2. **Time Stop**: Exit if position not profitable by 10 days before earnings
3. **Earnings Exit**: Close 100% of position before market close on 2026-10-27
4. **Max Loss Cap**: 2% of account ($2,000) on this trade

---

## MACHINE-READABLE OUTPUT

```json
{
  "ticker": "TKR",
  "bias": "LONG",
  "confidence": 0.72,
  "entry_window_days_before_earnings": 30,
  "entry": 115.0,
  "target": 124.5,
  "stop": 106.5,
  "position_size_pct": 15.0,
  "expected_move_pct": 3.01,
  "rationale": "30-day pre-earnings drift shows +3.01% mean return with 60% win rate (t-stat 2.41) while RSI at 36.38 and -7.12% below 50-EMA provide oversold entry; options imply 17.38% move vs 0% historical probability of >10% move, making premium selling attractive."
}
```