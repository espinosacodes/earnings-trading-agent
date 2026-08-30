```json
{
  "ticker": "LMT",
  "asset_type": "stock",
  "bias": "NEUTRAL",
  "confidence": 0.55,
  "entry_window_days_before_earnings": 20,
  "entry": 563.85,
  "target": 573.21,
  "stop": 536.65,
  "position_size_pct": 2.0,
  "expected_move_pct": 1.66,
  "hold_through_earnings": false,
  "holding_period_days": 20,
  "rationale": "Pre-earnings drift is positive (+1.66% mean, 55% win rate) over 20 days, but earnings-day moves are historically small (mean 0.24%, std 1.59%) with no >10% moves, and surprise momentum is decelerating with negative surprise-price correlation (-0.092), so we capture drift but exit before the release."
}
```