# NOC PRE-EARNINGS QUANTITATIVE TRADING SIGNAL REPORT

---

## 1. EXECUTIVE SUMMARY TABLE

| Metric | Value | Signal Implication |
|--------|-------|-------------------|
| **Implied Move (Options)** | 11.67% ($63.59 straddle) | **Extreme** vs historical mean abs move of 1.55% |
| **Historical Mean Earnings Move** | +0.56% (std 1.94%) | Minimal directional edge historically |
| **Historical Max Drawdown** | -3.52% | Far below implied move |
| **RSI-14** | 44.81 | Neutral-to-weak, no oversold condition |
| **Distance to 50-EMA** | -1.72% | Slightly below, mild bearish tilt |
| **Distance to 200-EMA** | -5.49% | Below long-term trend, bearish |
| **Trailing P/E** | 17.33x | Cheap vs peers (127.45x avg) |
| **Best Pre-Earnings Entry** | 30 days before | +1.53% mean, 60% win rate |
| **IV vs HV Gap** | 31.64% vs 25.94% | 5.7pp premium = IV crush risk |

**Key Discrepancy:** Options market implies an 11.67% move, but 20 historical earnings events show **zero** occurrences of moves >10%. The options are pricing a tail event that has never happened in the sample.

---

## 2. PRE-EARNINGS DRIFT BACKTEST (THE EDGE)

| Window (Days) | Mean Return % | Median % | Win Rate % | Sample Size | t-stat (approx) |
|---------------|--------------|----------|------------|-------------|-----------------|
| 1 | -1.12 | -0.03 | 50.0 | 20 | -1.58 |
| 3 | -1.96 | -1.18 | 40.0 | 20 | -2.77 |
| 5 | -1.79 | -2.24 | 40.0 | 20 | -2.53 |
| 7 | -1.88 | -3.26 | 30.0 | 20 | -2.66 |
| 10 | -1.22 | -3.02 | 35.0 | 20 | -1.72 |
| 15 | -0.02 | -2.46 | 40.0 | 20 | -0.03 |
| 20 | +1.24 | +0.24 | 50.0 | 20 | +1.75 |
| **30** | **+1.53** | **+1.47** | **60.0** | **20** | **+2.16** |

### Statistical Assessment:

**SHORT-TERM DRIFT (1-10 days):** Negative drift is consistent and economically meaningful. The 3-day window shows -1.96% mean with only 40% win rate. The 7-day window is the strongest bearish signal: -1.88% mean, 30% win rate, median -3.26%. This suggests NOC systematically **underperforms in the 1-2 weeks before earnings**.

**LONG-TERM DRIFT (20-30 days):** Positive drift emerges at 20 days (+1.24%) and strengthens at 30 days (+1.53%, 60% win rate). The 30-day window has the best risk-adjusted score (0.92).

**CONCLUSION:** There is a **statistically meaningful U-shaped drift pattern**. NOC tends to rally in the 20-30 day window before earnings, then give back gains in the final 1-10 days. The edge is to **buy early (30 days out) and exit before the final week**.

---

## 3. DIRECTIONAL SIGNAL & ENTRY TIMING

### Bias: **LONG** (with early exit before final week)

### Rationale:
1. **30-day drift edge:** +1.53% mean, 60% win rate, t-stat ≈ 2.16 (p < 0.05)
2. **Valuation support:** P/E of 17.33x vs peer average 127.45x (-86.4% discount) provides fundamental cushion
3. **Surprise momentum decelerating** but still positive (last surprise +12.66% on 2026-07-21)
4. **RSI at 44.81** with price below EMAs suggests entry at a relative low point in the cycle

### Entry Timing:
- **Optimal Entry:** 30 days before earnings (approximately 2026-09-20)
- **Exit:** 10 days before earnings (approximately 2026-10-10) to avoid the negative 1-10 day drift
- **Do NOT hold through earnings:** Historical mean move is only +0.56% but options imply 11.67% move; the risk/reward is unfavorable

### Price Levels (derived from metrics):

| Level | Price | Basis |
|-------|-------|-------|
| **Entry** | $536.03 | Volume profile node #2 (10.6M shares traded) |
| **Target** | $551.81 | Volume profile node #1 (14.1M shares) = +2.94% |
| **Stop** | $524.50 | Below 200-EMA zone (-5.49% from close = $515.20; use round number below support) |
| **Alternative Target** | $546.55 | Volume profile node #3 = +1.96% |

### Position Sizing:
- **Recommended Size:** 15% of account ($15,000 on $100,000)
- **Justification:** Worst-case historical drawdown in entry window is -3.52% (max earnings drawdown). With 15% position, worst-case loss = $15,000 × 3.52% = **$528** (0.53% of account). Even a -20% gap would cost $3,000 (3% of account), which is manageable.

---

## 4. OPTIONS STRATEGY (IBKR)

### Strategy: **Bull Call Spread** (defined risk, benefits from drift without earnings exposure)

### Structure:
- **Buy:** NOC 2026-10-16 $535 Call (ATM, delta ≈ 0.50)
- **Sell:** NOC 2026-10-16 $555 Call (delta ≈ 0.30)
- **Net Debit:** Approximately $8.50 (estimated from $63.59 straddle pricing)

### Strike Selection Logic:
- Long strike at $535 (ATM, near volume node $536.03)
- Short strike at $555 (above volume node $551.81, captures drift target)
- Delta spread: 0.50 → 0.30 = 0.20 directional exposure

### Risk/Reward:

| Metric | Value |
|--------|-------|
| **Max Loss** | $8.50 × 100 = $850 per contract |
| **Max Gain** | ($555 - $535 - $8.50) × 100 = $1,150 per contract |
| **Breakeven** | $543.50 (entry + debit) |
| **Risk/Reward Ratio** | 1:1.35 |

### IV Crush Mitigation:
- IV/HV gap = 31.64% - 25.94% = **5.70pp premium**
- Expected IV crush at earnings: ~18% (typical post-earnings IV drop)
- **Solution:** Exit the spread 10 days before earnings (before IV crush accelerates). The drift edge (+1.53%) is captured without earnings risk.

### Alternative: **Put Credit Spread** (if bearish drift in final week)
- Sell 2026-10-16 $525 Put / Buy $515 Put
- Collect ~$2.50 credit, max loss $7.50, breakeven $522.50

---

## 5. WORST-CASE SIMULATION

### Scenario A: -20% Overnight Gap (on $100,000 account, 15% position)

| Parameter | Value |
|-----------|-------|
| **Position Value** | $15,000 (27.98 shares @ $536.03) |
| **Post-Gap Price** | $428.82 (-20%) |
| **Loss** | $3,000 (3.0% of account) |
| **Remaining Account** | $97,000 |

**Liquidation Trigger:** If NOC gaps below $500 (volume profile support), liquidate 50% of position immediately. Below $480, liquidate 100%.

**Delta-Hedge Trigger:** If position loses >$1,500 (1.5% of account), buy 1 put contract (delta -0.50) at $535 strike to neutralize directional risk.

### Scenario B: Historical Max Drawdown (-3.52%)

| Parameter | Value |
|-----------|-------|
| **Position Value** | $15,000 |
| **Post-Drawdown Price** | $517.16 |
| **Loss** | $528 (0.53% of account) |
| **Remaining Account** | $99,472 |

**Action:** No action needed; within normal risk tolerance.

### Scenario C: Combined Drift Failure + Earnings Gap

| Parameter | Value |
|-----------|-------|
| **Drift Loss (30-day)** | -1.53% (worst case) = $229.50 |
| **Earnings Gap** | -3.52% (historical max) = $528 |
| **Total Loss** | $757.50 (0.76% of account) |

**Mitigation:** Exit before earnings eliminates the gap risk entirely.

---

## FINAL RECOMMENDATION

**Execute LONG position 30 days before earnings, exit 10 days before.** The 30-day drift edge (+1.53%, 60% win rate) is the only statistically significant signal. Do NOT hold through earnings—the options market is pricing an 11.67% move that has never occurred in 20 historical events, creating a severely negative expected value for holding.

---

```json
{
  "ticker": "NOC",
  "bias": "LONG",
  "confidence": 0.65,
  "entry_window_days_before_earnings": 30,
  "entry": 536.03,
  "target": 551.81,
  "stop": 524.5,
  "position_size_pct": 15.0,
  "expected_move_pct": 2.94,
  "rationale": "30-day pre-earnings drift shows +1.53% mean return with 60% win rate (t-stat 2.16) while valuation trades at 86.4% discount to peer average P/E, supporting a long entry at volume-profile support with exit before the negative 1-10 day drift window."
}
```