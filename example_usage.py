"""
example_usage.py -- Demonstrates ShoppingCartROISimulatorClient
"""
from client import ShoppingCartROISimulatorClient

def main():
    client = ShoppingCartROISimulatorClient()
    result = client.simulate_roi(
        cart_items=[
            {"price": 50.0, "cost": 15.0, "quantity": 2},
            {"price": 30.0, "cost": 10.0, "quantity": 1}
        ],
        discount_pct=15.0
    )
    print("[Cart ROI Simulation]")
    print(f"Revenue: ${result['gross_revenue']}")
    print(f"Profit: ${result['net_profit']} (Margin: {result['profit_margin_pct']}%)")
    print(f"ROI Ratio: {result['roi_ratio']}x")

if __name__ == "__main__":
    main()
