# AVGO PRE-EARNINGS QUANTITATIVE TRADING SIGNAL

## 1. EXECUTIVE SUMMARY TABLE

| Metric | Value | Signal Implication |
|--------|-------|-------------------|
| **Implied Move** | 8.12% (straddle $29.94) | Market pricing moderate move |
| **Historical Mean Move** | 2.06% (std 8.94%) | Positive drift historically |
| **Historical Mean Abs Move** | 10.83% | Actual moves exceed implied |
| **IV vs HV Gap** | 85.66% vs 41.9% | IV premium = 104% over HV |
| **RSI-14** | 42.75 | Neutral-bearish momentum |
| **Distance to 50-EMA** | -4.67% | Below key support |
| **Trailing P/E** | 61.26x | Premium valuation |
| **Best Entry Window** | 30 days (mean +7.27%) | Strong pre-earnings drift |
| **Days to Earnings** | 4 | Late entry window |

---

## 2. PRE-EARNINGS DRIFT BACKTEST (THE EDGE)

### Complete Drift Window Analysis:

| Window (Days) | Mean Return % | Median % | Win Rate % | Sample Size | t-Stat |
|---------------|---------------|----------|------------|-------------|--------|
| 1 | +0.21 | -0.35 | 45.0 | 20 | 0.31 |
| 3 | +0.99 | +0.65 | 60.0 | 20 | 1.47 |
| 5 | +2.68 | +2.54 | 63.2 | 19 | 3.11 |
| 7 | +3.25 | +4.03 | 68.4 | 19 | 3.89 |
| 10 | +2.24 | +2.21 | 52.6 | 19 | 2.18 |
| 15 | +2.67 | +2.42 | 52.6 | 19 | 2.31 |
| 20 | +5.32 | +4.28 | 68.4 | 19 | 4.12 |
| **30** | **+7.27** | **+5.28** | **78.9** | **19** | **5.74** |

### Statistical Verdict:
**YES - STRONG POSITIVE DRIFT EXISTS.** The 30-day window shows a mean return of +7.27% with a 78.9% win rate and a t-statistic of 5.74 (p < 0.001). The 20-day window also confirms this edge (+5.32%, 68.4% win rate). However, with only 4 days to earnings, we've missed the optimal entry window. The 3-day window (+0.99%, 60% win rate) offers a modest residual edge.

---

## 3. DIRECTIONAL SIGNAL & ENTRY TIMING

### Signal Synthesis:

| Factor | Reading | Weight |
|--------|---------|--------|
| Pre-Earnings Drift (3-day) | +0.99%, 60% WR | Bullish |
| Surprise Momentum | Decelerating | Bearish |
| Surprise-Move Correlation | -0.144 (negative) | Bearish |
| RSI-14 | 42.75 | Neutral |
| Distance to 50-EMA | -4.67% | Bearish |
| IV Premium | 104% over HV | Bearish (IV crush risk) |
| Peer P/E Premium | -51.6% discount | Bullish |

### **BIAS: NEUTRAL (FLAT) with SHORT-TERM LONG TILT**

**Rationale:** The 30-day drift edge (+7.27%) has been missed. The remaining 3-day window offers only +0.99% mean return with 60% win rate - insufficient to overcome the 8.12% implied move risk. The negative surprise-move correlation (-0.144) and decelerating surprise momentum suggest limited upside catalyst. However, the 60% win rate on 3-day drift provides a marginal long bias.

### Entry Parameters (if trading):
- **Entry Window:** 1 day before earnings (T-1)
- **Entry Price:** $365.77 (volume profile node support)
- **Target:** $395.45 (implied move upside: $365.77 × 1.0812)
- **Stop:** $348.00 (below 50-EMA at $351.55, round number support)
- **Position Size:** 2% of account (reduced due to late entry)

---

## 4. OPTIONS STRATEGY (IBKR)

### Strategy: LONG PUT SPREAD (Defined Risk)

**Rationale:** With IV at 85.66% vs HV at 41.9%, buying options is expensive. However, the negative surprise-move correlation (-0.144) and decelerating momentum suggest downside risk. A put spread limits cost while maintaining defined risk.

### Structure:
- **Buy:** AVGO 2026-09-02 $365 Put (ATM-1, ~45 delta)
- **Sell:** AVGO 2026-09-02 $340 Put (~25 delta)
- **Net Debit:** ~$8.50 (estimated from 90.23% put IV)

### Risk/Reward:
| Metric | Value |
|--------|-------|
| Max Loss | $850 per contract (net debit) |
| Max Gain | $1,650 per contract ($25 spread - $8.50) |
| Breakeven | $356.50 (strike - debit) |
| Max Return | 194% on risk |
| Probability of Profit | ~35% (based on 25% historical prob of >10% move) |

### IV Crush Mitigation:
- IV premium of 104% over HV will compress post-earnings
- Spread structure reduces vega exposure vs long puts alone
- Entry at T-1 minimizes time premium paid

---

## 5. WORST-CASE SIMULATION

### Scenario A: -20% Overnight Gap on $100,000 Account

**Position:** 2% = $2,000 in AVGO stock (5 shares @ $368.79)

| Metric | Value |
|--------|-------|
| Loss on Stock | $368.79 × 5 × (-20%) = -$368.79 |
| Loss % of Account | -0.37% |
| Liquidation Trigger | Stop at $348.00 (loss of $103.95) |
| Delta Hedge Trigger | If stock drops >5% pre-earnings, buy 1 put spread |

**Options Position (2 contracts @ $850 debit):**
| Metric | Value |
|--------|-------|
| Max Loss | -$1,700 (if stock > $365 at expiry) |
| Max Gain | +$3,300 (if stock < $340 at expiry) |
| Total Account Risk | -$2,069 (2.07% of account) |

### Scenario B: Historical Max Drawdown (-12.59%)

| Position | Loss |
|----------|------|
| Stock (5 shares) | -$232.15 |
| Options (2 spreads) | -$1,700 (max loss) |
| **Total** | **-$1,932 (1.93% of account)** |

### Risk Management Triggers:
1. **Hard Stop:** Exit stock position if AVGO closes below $348.00
2. **Delta Hedge:** If pre-earnings drift turns negative (stock < $360), buy 1 additional $355 put for protection
3. **Time Stop:** Exit all positions if stock moves >5% against within 48 hours of entry

---

## FINAL RECOMMENDATION

**DO NOT TRADE THE EARNINGS GAP.** The optimal 30-day entry window (+7.27% mean, 78.9% WR) has passed. The residual 3-day edge (+0.99%, 60% WR) does not justify the 8.12% implied move risk. The negative surprise-move correlation (-0.144) and decelerating surprise momentum further reduce the probability of a positive surprise driving upside.

**If forced to trade:** Use the defined-risk put spread (max loss $1,700) rather than stock, with position size capped at 2% of account.

---

```json
{
  "ticker": "AVGO",
  "bias": "NEUTRAL",
  "confidence": 0.65,
  "entry_window_days_before_earnings": 1,
  "entry": 365.77,
  "target": 395.45,
  "stop": 348.00,
  "position_size_pct": 2.0,
  "expected_move_pct": 8.12,
  "rationale": "Optimal 30-day pre-earnings drift window (+7.27%, 78.9% WR) missed; residual 3-day edge (+0.99%, 60% WR) insufficient vs 8.12% implied move, with negative surprise-move correlation (-0.144) and decelerating momentum favoring flat positioning."
}
```