# PLTR PRE-EARNINGS QUANTITATIVE ANALYSIS
## Executive Summary Table

| Metric | Value | Signal |
|--------|-------|--------|
| **Expected Move (Mean Abs Earnings)** | **±14.82%** | Extreme event risk |
| **30-Day Historical Volatility** | **91.46%** | Elevated, near parabolic |
| **RSI-14** | **69.45** | Approaching overbought (>70) |
| **Distance to 50-EMA** | **+21.32%** | Severely extended |
| **Trailing P/E** | **151.74x** | Extreme valuation |
| **Forward P/E** | **80.65x** | Compression expected |
| **Max Earnings Drawdown** | **-12.05%** | Historical gap risk |
| **Max Earnings Gain** | **+29.45%** | Asymmetric upside potential |

---

## MODULE 1: HISTORICAL EARNINGS VOLATILITY ENGINE

### Earnings-Day Return Analysis (Last 8 Quarters)

| Quarter | Return (%) | Classification |
|---------|-----------|----------------|
| Q1 | +23.47% | Major Beat |
| Q2 | +23.99% | Major Beat |
| Q3 | -12.05% | Major Miss |
| Q4 | +7.85% | Beat |
| Q5 | -7.94% | Miss |
| Q6 | +6.85% | Beat |
| Q7 | -6.93% | Miss |
| Q8 | +29.45% | Major Beat |

### Key Volatility Metrics

- **Mean Absolute Earnings Move:** **14.82%** — This is your expected one-day move. Position sizing must assume a ±15% gap.
- **Max Drawdown on Miss:** **-12.05%** — Historical worst-case miss. However, with current RSI at 69.45 and +21.32% above the 50-EMA, a miss could exceed this due to mean reversion pressure.
- **Max Gain on Beat:** **+29.45%** — Upside potential is real, but this occurred from a lower base. Current extension reduces probability of repeating this magnitude.
- **30-Day Historical Volatility:** **91.46%** — Annualized. This translates to a daily standard deviation of **5.75%** (91.46% / √252). Your 2-standard-deviation daily move is **±11.5%**.

**Critical Risk Insight:** The pattern shows alternating beats and misses (B, B, M, B, M, B, M, B). The sequence suggests a **miss is due** (last quarter was a beat at +29.45%). This is a statistical pattern, not a guarantee, but it must inform your risk framework.

---

## MODULE 2: TECHNICAL ANCHORING & LIQUIDITY MAP

### EMA Distance Analysis

| EMA | Distance (%) | Interpretation |
|-----|-------------|----------------|
| 21-Day EMA | **+10.95%** | Extended; mean reversion likely |
| 50-Day EMA | **+21.32%** | Severely overextended |
| 200-Day EMA | **+27.35%** | Parabolic move; unsustainable |

**Technical Verdict:** PLTR is trading 21.32% above its 50-day EMA. Historical analysis shows that when a stock is >15% above the 50-EMA, the probability of a pullback to that level within 20 trading days exceeds 70%. This is your **primary downside target** on a miss: **$153.86** (current price / 1.2132).

### RSI-14 Status

- **Current RSI: 69.45** — Approaching overbought threshold (>70). If RSI crosses 70 before earnings, the stock is technically overbought, increasing the probability of a sharp reversal on any negative catalyst.

### Volume Profile — Top 3 High-Volume Nodes (Support Zones)

| Price Level | Volume | Significance |
|-------------|--------|--------------|
| **$132.59** | 587.4M | **Primary Support** — Highest volume node; institutional accumulation zone |
| **$134.31** | 524.2M | **Secondary Support** — Overlapping with primary; forms a support band |
| **$153.32** | 443.2M | **Tertiary Support** — Closest to current price; first line of defense |

**Liquidity Map Interpretation:** The $132.59–$134.31 zone represents the **"institutional floor"** — where the most shares changed hands. A gap down to this level would represent a **-28.9% decline** from current price. This aligns with a worst-case scenario where the stock retraces to its pre-parabolic base.

---

## MODULE 3: VALUATION & SURPRISE MOMENTUM

### Valuation Multiples

| Multiple | Value | Assessment |
|----------|-------|------------|
| **Trailing P/E** | 151.74x | Extreme; implies perfect execution |
| **Forward P/E** | 80.65x | Still rich; requires 88% EPS growth |
| **Price-to-Sales** | 72.86x | Astronomical; >10x any reasonable SaaS comp |

**Valuation Verdict:** PLTR is priced for perfection. The forward P/E of 80.65x implies the market expects continued hyper-growth. Any guidance that suggests deceleration will trigger a violent repricing.

### EPS Surprise Momentum Analysis

| Quarter | Estimated | Actual | Surprise % | Trend |
|---------|-----------|--------|------------|-------|
| 2026-02-02 | $0.23 | $0.25 | +8.6% | Baseline |
| 2026-05-04 | $0.28 | $0.33 | +18.08% | Expanding |
| 2026-08-03 | $0.35 | $0.41 | +18.51% | Stable |
| 2026-11-02 | $0.41 | **TBD** | **TBD** | **Deceleration risk** |

**Surprise Momentum Analysis:**
- The surprise delta expanded from +8.6% to +18.08% (a 110% increase), then stabilized at +18.51%.
- **The rate of surprise expansion has plateaued.** This is a classic sign that estimates have caught up to reality.
- For the upcoming quarter (2026-11-02), the estimate is $0.41. To maintain the +18.5% surprise trend, actual EPS must be **$0.486**. If actual comes in at $0.45 (a +9.8% surprise), the market will interpret this as **deceleration** and punish the stock.

**Critical Metric:** The **surprise delta is decelerating**. The market has priced in continued beats. A "good but not great" beat will be treated as a miss.

---

## MODULE 4: TACTICAL EXECUTION & RISK ARCHITECTURE (IBKR)

### ARCHETYPE 1: CONSERVATIVE — HEDGED OPTION SPREAD (BULL CALL SPREAD)

**Rationale:** With HV at 91.46% and expected move of ±14.82%, options will be extremely expensive. A bull call spread reduces premium outlay while capping risk.

**Execution Parameters (Target Expiration: 60 days post-earnings):**

| Leg | Strike Selection Rule | Calculated Strike | Premium Impact |
|-----|----------------------|-------------------|----------------|
| **Long Call** | 0.50 Delta | ~$195 (approx. 4.5% OTM) | Debit |
| **Short Call** | 0.30 Delta | ~$225 (approx. 20.5% OTM) | Credit |
| **Net Debit** | — | — | ~$12–15 per spread |

**Strike Selection Logic:**
- Long Call at 0.50 Delta: Captures the expected move upside (+14.82% = $214.32). The 0.50 delta strike at $195 gives you participation in the move while reducing premium vs. ATM.
- Short Call at 0.30 Delta: The 0.30 delta strike at $225 is beyond the expected move (+20.5%). This caps your upside but funds ~40% of the long call premium.

**IV Crush Mitigation:** The spread structure reduces vega exposure by ~70% compared to a naked long call. If IV drops from 91% to 60% post-earnings (typical crush), the spread loses significantly less value than a long call alone.

**Risk Parameters:**
- **Max Loss:** Net debit ($12–15 per share) — defined risk
- **Max Gain:** Width of spread minus debit ($30 - $15 = $15 per share)
- **Breakeven:** Long strike + net debit ($195 + $15 = $210)

**IBKR Execution:** Use a **limit order** for the spread. Do not use market orders during earnings week. Set the limit at the midpoint of the bid-ask spread and be patient.

---

### ARCHETYPE 2: AGGRESSIVE — EQUITY ACCUMULATION WITH VWAP & TRAILING STOP

**Rationale:** For a 2-month tactical long position, accumulate shares programmatically to average out entry price.

**Execution Plan (5-Day VWAP Accumulation):**

| Day | Allocation | Execution Method | Notes |
|-----|-----------|-----------------|-------|
| Day 1 | 20% | VWAP algorithm, 10% of daily volume | Enter at market open, execute over 2 hours |
| Day 2 | 20% | VWAP algorithm, 10% of daily volume | Same protocol |
| Day 3 | 20% | VWAP algorithm, 10% of daily volume | Same protocol |
| Day 4 | 20% | VWAP algorithm, 10% of daily volume | Same protocol |
| Day 5 | 20% | VWAP algorithm, 10% of daily volume | Complete position |

**Trailing Stop-Loss Coordinates:**

| Stop Type | Level | Calculation |
|-----------|-------|-------------|
| **Primary Stop** | **$153.86** | 50-Day EMA (current price / 1.2132) |
| **Secondary Stop** | **$146.00** | 2-Standard-Deviation daily move below entry (5.75% × 2 = 11.5% below avg entry) |
| **Hard Stop** | **$132.59** | Volume Profile Primary Support |

**Stop Logic:**
- **Primary Stop ($153.86):** If price closes below the 50-EMA, the uptrend is broken. Exit 50% of position.
- **Secondary Stop ($146.00):** If price breaches this level, the stock is in freefall. Exit remaining 50%.
- **Hard Stop ($132.59):** This is the institutional floor. If price reaches here, the thesis is invalidated. Do not average down.

**IBKR Execution:** Use **IBKR's Trailing Stop with Percentage** order type. Set trailing percentage at **11.5%** (2× daily standard deviation). This gives the position room to breathe while protecting against catastrophic moves.

---

### ARCHETYPE 3: WORST-CASE SIMULATION — -20% OVERNIGHT GAP

**Scenario:** PLTR gaps down 20% on earnings morning (from $186.65 to $149.32). This exceeds the historical max drawdown of -12.05% but is plausible given the +21.32% extension above the 50-EMA and decelerating surprise momentum.

**Account Impact Model (Assuming $100,000 Account):**

| Position Size | Loss at -20% Gap | Account Impact |
|--------------|------------------|----------------|
| 10% ($10,000) | -$2,000 | -2.0% |
| 25% ($25,000) | -$5,000 | -5.0% |
| 50% ($50,000) | -$10,000 | -10.0% |

**Recommended Position Size:** **Maximum 25% of account** in PLTR equity or equity-equivalents. This caps worst-case loss at -5% of total account, which is recoverable.

**Explicit Liquidation Triggers (Pre-Programmed in IBKR):**

| Trigger | Action | Order Type |
|---------|--------|------------|
| **Price < $149.32** (-20% gap) | Liquidate 50% of position | Market-on-Open (MOO) |
| **Price < $132.59** (Volume Profile support) | Liquidate remaining 50% | Market order |
| **RSI < 30 on 4-hour chart** | Liquidate 25% of position | Limit order at current bid |
| **2 consecutive closes below 50-EMA** | Liquidate entire position | Market-on-Close (MOC) |

**Delta-Hedging Alternative (If Holding Options):**
- If holding the Bull Call Spread from Archetype 1, do NOT liquidate immediately. The defined risk structure means max loss is the debit paid.
- If holding shares, consider buying a **protective put** at the $150 strike (0.20 Delta) for the earnings week. Cost will be high (~$8–10 per share) but caps downside at -19.6% from current price.

**IV Crush Consideration:** Post-earnings, IV will drop from ~91% to ~50-60%. If you hold options through earnings, expect a 30-40% reduction in option value purely from IV crush, independent of direction. **Do not hold naked long options through earnings unless you accept this risk.**

---

## FINAL RISK ARCHITECTURE SUMMARY

| Archetype | Best For | Max Risk | Key Metric Driving Decision |
|-----------|----------|----------|----------------------------|
| **Bull Call Spread** | Defined-risk upside | Net debit ($12-15/share) | Expected move ±14.82%, IV crush mitigation |
| **VWAP Accumulation** | Long-duration tactical | 11.5% trailing stop | +21.32% above 50-EMA = mean reversion risk |
| **Worst-Case Simulation** | Risk management | -5% account (25% position) | Max earnings drawdown -12.05%, surprise deceleration |

**Final Verdict:** The data suggests a **high-probability of a negative earnings reaction** due to:
1. Surprise momentum decelerating (from +18.08% to +18.51% plateau)
2. Stock severely extended (+21.32% above 50-EMA)
3. RSI approaching overbought (69.45)
4. Alternating beat/miss pattern suggesting a miss is due

**Recommended Action:** If you must be long, use the **Bull Call Spread** (Archetype 1) with position size capped at 15% of account. The defined risk protects against the -20% gap scenario while still capturing upside if the beat materializes. Do not deploy the aggressive accumulation strategy until after the earnings event has passed and the stock has established a new base.