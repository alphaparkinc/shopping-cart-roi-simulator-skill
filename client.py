"""
shopping-cart-roi-simulator-skill: Client SDK
Calculates bundling discounts against product cost bases to output final profit ratios.
"""
from __future__ import annotations
from typing import Optional


class ShoppingCartROISimulatorClient:
    """
    SDK for deal modeling and ROI estimation.
    """

    def simulate_roi(
        self,
        cart_items: list[dict],
        discount_pct: float = 0.0,
    ) -> dict:
        total_rev = 0.0
        total_cost = 0.0

        for item in cart_items:
            price = float(item.get("price", 0.0))
            cost = float(item.get("cost", 0.0))
            qty = int(item.get("quantity", 1))

            total_rev += price * qty
            total_cost += cost * qty

        # Apply bundling discount
        discount_amount = total_rev * (discount_pct / 100.0)
        gross_rev = total_rev - discount_amount

        net_profit = gross_rev - total_cost
        margin_pct = (net_profit / gross_rev) * 100.0 if gross_rev > 0 else 0.0

        return {
            "gross_revenue": round(gross_rev, 2),
            "total_cost": round(total_cost, 2),
            "net_profit": round(net_profit, 2),
            "profit_margin_pct": round(margin_pct, 1),
            "roi_ratio": round(net_profit / max(1.0, total_cost), 2)
        }
