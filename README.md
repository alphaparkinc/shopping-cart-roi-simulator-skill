# genpark-shopping-cart-roi-simulator-skill

> **GenPark AI Agent Skill** -- Shopping cart deal bundler and margin ROI analyzer.

## Quick Start

```python
from client import ShoppingCartROISimulatorClient
client = ShoppingCartROISimulatorClient()
res = client.simulate_roi([{"price": 100, "cost": 40}], 10)
print(res["net_profit"])
```
