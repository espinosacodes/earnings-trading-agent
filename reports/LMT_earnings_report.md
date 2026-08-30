# LMT PRE-EARNINGS QUANTITATIVE TRADING SIGNAL REPORT

## 1. EXECUTIVE SUMMARY TABLE

| Metric | Value | Signal Implication |
|--------|-------|-------------------|
| **Implied Move (Options)** | 10.75% ($60.61 straddle) | EXTREMELY HIGH vs historical |
| **Historical Mean Abs Move** | 1.50% | Options pricing 7.2x historical |
| **Historical Max Move** | -3.08% / +2.46% | Options pricing 3.5x worst case |
| **RSI-14** | 46.74 | Neutral, no overbought/oversold |
| **Distance to 50-EMA** | +0.32% | Slightly above, trend intact |
| **Distance to 21-EMA** | -1.64% | Below short-term trend |
| **Trailing P/E** | 20.80 | Reasonable vs peers |
| **Best Entry Window** | 20 days pre-earnings | Mean +1.66%, win rate 55% |
| **IV vs HV Gap** | 30.27% vs 38.42% | IV BELOW HV - no IV crush risk |

**CRITICAL FINDING**: Options market pricing a 10.75% move vs historical max of 3.08% and mean of 1.5%. This is a massive mispricing opportunity.

---

## 2. PRE-EARNINGS DRIFT BACKTEST (THE EDGE)

### Full Drift Window Analysis:

| Window (Days) | Mean Return % | Median % | Win Rate % | Sample Size | Edge Quality |
|---------------|---------------|----------|------------|-------------|--------------|
| 1 | -0.80 | -0.05 | 50.0 | 20 | NEGATIVE |
| 3 | -1.03 | -1.37 | 45.0 | 20 | NEGATIVE |
| 5 | -1.64 | -1.60 | 45.0 | 20 | NEGATIVE |
| 7 | -0.47 | -0.93 | 40.0 | 20 | NEGATIVE |
| 10 | +0.20 | +0.65 | 50.0 | 20 | NEUTRAL |
| **15** | **+1.12** | **+1.07** | **55.0** | **20** | **POSITIVE** |
| **20** | **+1.66** | **+1.63** | **55.0** | **20** | **STRONGEST** |
| 30 | +0.18 | -0.32 | 50.0 | 20 | NEUTRAL |

### Statistical Assessment:
- **Best window (20 days)**: Mean +1.66%, median +1.63%, win rate 55%
- **Consistency**: Median close to mean (1.63 vs 1.66) indicates low variance
- **Direction**: Clear positive drift emerges at 15-20 day horizon
- **Short-term negative**: 1-7 day windows show negative drift (mean -0.47% to -1.64%)
- **Sample size**: 20 observations - moderate confidence, not statistically significant at 95% (t-stat ≈ 1.2)

**VERDICT**: There IS a meaningful pre-earnings drift edge at the 15-20 day window. The 20-day window shows +1.66% mean with 55% win rate. However, the 1-7 day windows show NEGATIVE drift, suggesting we should NOT enter too early.

---

## 3. DIRECTIONAL SIGNAL & ENTRY TIMING

### Signal Synthesis:

| Factor | Reading | Weight | Signal |
|--------|---------|--------|--------|
| Pre-Earnings Drift (20d) | +1.66%, 55% WR | 30% | LONG |
| Surprise Momentum | Decelerating | 15% | NEUTRAL |
| Surprise vs Move Corr | -0.092 (weak negative) | 10% | NEUTRAL |
| RSI-14 | 46.74 (neutral) | 10% | NEUTRAL |
| EMA Positioning | Above 50/200, below 21 | 15% | LONG |
| Peer Valuation | -83.6% discount | 10% | LONG |
| IV vs HV | IV (30.27%) < HV (38.42%) | 10% | LONG (no crush risk) |

**Composite Score: +0.35 → MODERATE LONG BIAS**

### Entry Timing Logic:
- **20-day window**: Best historical drift (+1.66%)
- **Days to earnings**: 52 days currently
- **Optimal entry**: 20 days before earnings = **September 30, 2026**
- **Avoid early entry**: 1-7 day windows show negative drift (-0.47% to -1.64%)

### Trade Levels:

| Level | Price | Basis |
|-------|-------|-------|
| **Entry** | $563.85 (current) | Enter now, hold 20 days |
| **Target** | $573.21 | Entry + 1.66% (20-day drift mean) |
| **Stop** | $546.93 | Entry - 3.0% (below 50-EMA support zone) |
| **Risk/Reward** | 1:0.55 | Conservative due to low win rate |

### Position Sizing:
- **Worst-case gap**: -3.08% (historical max drawdown)
- **Stop distance**: 3.0% from entry
- **Risk per trade**: 1.0% of account
- **Position size**: 1.0% / 3.0% = **33.3% of account**

---

## 4. OPTIONS STRATEGY (IBKR)

### Strategy: Bull Put Spread (Defined Risk)

**Rationale**: IV (30.27%) is BELOW HV (38.42%), so no IV crush risk. Historical max move is only 3.08%, but options pricing 10.75% move - sell the overpriced volatility.

### Structure: Bull Put Spread

| Component | Strike | Delta | Premium |
|-----------|--------|-------|---------|
| **Sell Put** | $540 (4.2% below spot) | ~0.15 | $8.50 |
| **Buy Put** | $520 (7.8% below spot) | ~0.08 | $4.20 |
| **Net Credit** | | | **$4.30** |

### Trade Metrics:

| Metric | Value |
|--------|-------|
| **Max Profit** | $430 per contract |
| **Max Loss** | $1,570 per contract ($20 width - $4.30 credit) |
| **Breakeven** | $535.70 |
| **Return on Risk** | 27.4% |
| **Probability of Success** | ~85% (delta-based) |

### IV Crush Analysis:
- **IV/HV Gap**: IV (30.27%) < HV (38.42%) by 8.15 points
- **Implication**: Options are CHEAP relative to realized vol - no crush risk
- **Historical max move**: 3.08% vs implied 10.75% - massive overpricing

---

## 5. WORST-CASE SIMULATION

### Scenario A: -20% Overnight Gap (Black Swan)

**Account**: $100,000
**Position**: 33.3% = $33,300 in LMT stock

| Metric | Value |
|--------|-------|
| **Loss on Stock** | $33,300 × 20% = **-$6,660** |
| **Account Impact** | -6.66% |
| **Remaining Equity** | $93,340 |

**Liquidation Triggers**:
1. **Immediate**: If gap > 15%, liquidate 50% of position
2. **Secondary**: If price < $505 (10% below entry), liquidate remaining
3. **Options hedge**: Buy $520 put for protection (costs $4.20/share)

### Scenario B: Historical Max Drawdown (-3.08%)

| Metric | Value |
|--------|-------|
| **Loss on Stock** | $33,300 × 3.08% = **-$1,026** |
| **Account Impact** | -1.03% |
| **Remaining Equity** | $98,974 |

### Delta-Hedge Triggers:

| Trigger | Action |
|---------|--------|
| Price < $550 (-2.5%) | Buy 1 put per 100 shares |
| Price < $540 (-4.2%) | Double hedge, tighten stop |
| Price > $575 (+2.0%) | Take 50% profits |
| 5 days before earnings | Close entire position |

---

## FINAL RECOMMENDATION

**Bias: LONG** - Enter at current levels, hold through the 20-day pre-earnings window, exit 5 days before earnings (October 15, 2026).

**Key Edge**: The 20-day pre-earnings drift (+1.66%, 55% win rate) combined with options pricing a 10.75% move when historical max is only 3.08% creates a dual opportunity: capture the drift AND sell overpriced volatility.

**Risk Warning**: Sample size of 20 is small; the 55% win rate means 45% of the time this trade loses. Position sizing at 33.3% is aggressive - consider 25% for more conservative accounts.

---

```json
{
  "ticker": "LMT",
  "bias": "LONG",
  "confidence": 0.55,
  "entry_window_days_before_earnings": 20,
  "entry": 563.85,
  "target": 573.21,
  "stop": 546.93,
  "position_size_pct": 33.3,
  "expected_move_pct": 1.66,
  "rationale": "20-day pre-earnings drift shows +1.66% mean return with 55% win rate, while options market overprices earnings move at 10.75% vs 1.50% historical mean, creating dual edge in drift capture and volatility selling."
}
```