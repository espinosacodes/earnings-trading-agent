# Long-Term Portfolio Framework (5-10 years)

Value + growth screen across AI, semiconductors, software, robotics, defence,
aerospace, and manufacturing. Metrics pulled from `yfinance` (trailing P/E,
forward P/E, revenue growth, profit margin, ROE). This is a framework, not
financial advice.

## Core holdings

### AI / Semiconductors
| Ticker | P/E | Fwd P/E | Rev growth | Margin | ROE | Note |
|---|---|---|---|---|---|---|
| NVDA | 29 | 14 | +106% | 64% | 117% | Cheap fwd P/E for growth; cyclical risk |
| AVGO | 61 | 19 | +48% | 39% | 37% | Diversified AI infrastructure |
| TSM | 31 | 19 | +36% | 50% | 40% | The picks-and-shovels foundry |
| ASML | 57 | 28 | +21% | 30% | 54% | EUV lithography monopoly |

### Software / AI
| Ticker | P/E | Fwd P/E | Rev growth | Margin | ROE | Note |
|---|---|---|---|---|---|---|
| MSFT | 28 | 22 | +18% | 40% | 34% | Moat + AI |
| ADBE | 17 | 11 | +13% | 29% | 63% | Cheapest quality software |
| ORCL | 26 | 14 | +21% | 25% | 53% | Cloud/AI, very reasonable |
| CRM | 23 | 16 | +11% | 22% | 19% | Solid value |

### Defence / Aerospace
| Ticker | P/E | Fwd P/E | Rev growth | Margin | ROE | Note |
|---|---|---|---|---|---|---|
| LMT | 21 | 17 | +10% | 8% | 89% | High ROE via buybacks |
| NOC | 17 | 18 | +5% | 10% | 27% | Cheapest of the primes |
| GD | 23 | 20 | +8% | 8% | 18% | Stable |
| RTX | 37 | 27 | +14% | 8% | 12% | Defence rebound |
| GE | 40 | 38 | +21% | 18% | 48% | Aerospace aftermarket compounder |

### Robotics / Automation
| Ticker | P/E | Fwd P/E | Rev growth | Margin | ROE | Note |
|---|---|---|---|---|---|---|
| ISRG | 42 | 31 | +18% | 28% | 17% | Robotic surgery monopoly |
| TER | 51 | 30 | +104% | 26% | 36% | Robotics + semi test |
| ROK | 40 | 29 | +8% | 13% | 31% | Industrial automation, modest growth |

### Manufacturing / Industrials
| Ticker | P/E | Fwd P/E | Rev growth | Margin | ROE | Note |
|---|---|---|---|---|---|---|
| ETN | 41 | 25 | +21% | 13% | 20% | Electrification + data centers |
| CAT | 35 | 25 | +24% | 15% | 57% | Quality ROE |
| PH | 35 | 25 | +10% | 17% | 25% | Motion & control |
| MOG-A | 32 | 32 | +15% | 9% | 18% | Defence + motion control |
| TKR | 33 | 17 | +8% | 5% | 9% | Cyclical, cheap fwd P/E |

## Speculative satellite (small size)

| Ticker | Theme | Risk |
|---|---|---|
| MP | Rare earths | Pre-earnings momentum unreliable |
| USAR | Rare earths (recent IPO) | Only 6 earnings events |
| SYM | Warehouse robotics | Near-zero margin, P/E 996 |
| GCUMF | Copper (OTC) | Penny stock, 1 data point |
| SUUFF | Uranium (OTC) | Sub-penny, no reliable price data |
| KOID | Humanoid robotics ETF | Basket, not an individual stock |

## Suggested allocation

```
40%  AI / Semiconductors   NVDA, AVGO, TSM, ASML
20%  Software              MSFT, ADBE, ORCL
20%  Defence / Aerospace   LMT, NOC, RTX, GE
10%  Robotics / Automation ISRG, TER
10%  Satellite / thematic  MP, SYM, MOG-A, TKR (small)
```

## Data caveats

- `HON` excluded: trailing P/E 8.5 is a one-time-gain artifact.
- `FANUY` and `SYM` have distorted metrics; treat with caution.
- `DE` has negative revenue growth; excluded.
