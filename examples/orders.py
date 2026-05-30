import asyncio
import random

from fastapi import HTTPException, Request

from openadmin import AdminPage, PaginationParamsDep, Stat, Table

from . import db

page = AdminPage("Orders")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# Orders

Track order volume, fulfillment status, and flag suspicious transactions for review.

## Order Lifecycle

```
pending → processing → shipped → delivered
                   ↘ cancelled
```

## Status Breakdown

| Status | Count | Share | Action Required |
|---|---|---|---|
| delivered | 3,840 | 79.6% | None |
| shipped | 412 | 8.5% | Monitor transit |
| processing | 280 | 5.8% | Fulfillment queue |
| pending | 154 | 3.2% | Awaiting payment confirmation |
| cancelled | 135 | 2.8% | Refund if charged |

## Fraud Review

> Orders flagged as `fraud-risk` or `address-mismatch` must be reviewed within **4 hours** of placement. High-value orders (> $500) are automatically escalated.

- Always cross-check billing and shipping addresses for high-value orders
- Repeated orders from the same email with different cards are a strong fraud signal
- Bulk orders from new accounts (`high-value` flag) require manual approval before fulfillment

## Average Order Value

Current AOV is **$67.40**. Upsell prompts at checkout have historically lifted AOV by 12–18%.
"""


@page.stat("Orders Today", description="New orders placed in the last 24 hours")
async def orders_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for o in db.orders.values() if o["date"] == "2026-05-30"))


@page.stat("Pending Fulfillment", description="Orders awaiting processing or shipment")
async def pending_fulfillment() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for o in db.orders.values() if o["status"] in ("pending", "processing")))


@page.stat("Completed This Month", description="Orders fulfilled in May 2026")
async def completed_month() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for o in db.orders.values() if o["status"] == "delivered"))


@page.stat("Avg Order Value", description="Mean order value this month")
async def avg_order_value() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="$67.40")


@page.stat("Cancellation Rate", description="Percentage of orders cancelled this month")
async def cancellation_rate() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="2.8%")


@page.action_delete("Cancel order", description="Cancel an order and trigger a refund if charged")
async def cancel_order(id: int) -> None:
    if id not in db.orders:
        raise HTTPException(status_code=404, detail="Order not found")
    db.orders[id]["status"] = "cancelled"


@page.action_post("Mark as delivered", description="Manually mark an order as delivered")
async def mark_delivered(id: int) -> None:
    if id not in db.orders:
        raise HTTPException(status_code=404, detail="Order not found")
    db.orders[id]["status"] = "delivered"
    db.orders[id]["flag"] = None


@page.table("Recent Orders", description="Latest orders placed on the platform")
async def recent_orders(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(
        [o for o in db.orders.values() if not o["flag"]],
        key=lambda o: (o["date"], o["id"]),
        reverse=True,
    )
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "order_id": o["order_id"],
            "customer": o["customer"],
            "total": o["total"],
            "status": o["status"],
            "date": o["date"],
            "__actions__": [
                {
                    "color": "success",
                    "method": "POST",
                    "url": str(req.url_for(mark_delivered.__name__)) + f"?id={o['id']}",
                },
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(cancel_order.__name__)) + f"?id={o['id']}",
                },
            ],
        }
        for o in page_rows
    ])


@page.table("Orders by Status", description="Current distribution of order statuses")
async def orders_by_status() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    counts: dict[str, int] = {}
    for o in db.orders.values():
        counts[o["status"]] = counts.get(o["status"], 0) + 1
    total = len(db.orders) or 1
    return Table(data=[
        {"status": status, "count": count, "share": f"{count / total * 100:.1f}%"}
        for status, count in sorted(counts.items(), key=lambda x: -x[1])
    ])


@page.table("Flagged Orders", description="Orders flagged for manual review")
async def flagged_orders(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = [o for o in db.orders.values() if o["flag"]]
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "order_id": o["order_id"],
            "customer": o["customer"],
            "total": o["total"],
            "flag": o["flag"],
            "date": o["date"],
            "__actions__": [
                {
                    "color": "success",
                    "method": "POST",
                    "url": str(req.url_for(mark_delivered.__name__)) + f"?id={o['id']}",
                },
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(cancel_order.__name__)) + f"?id={o['id']}",
                },
            ],
        }
        for o in page_rows
    ])


@page.table("Top Customers", description="Customers by total lifetime spend")
async def top_customers() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"customer": "TechCorp Inc.", "orders": 142, "lifetime_value": "$18,420", "last_order": "2026-05-30"},
            {"customer": "Alice Johnson", "orders": 88, "lifetime_value": "$9,240", "last_order": "2026-05-30"},
            {"customer": "StartupXYZ", "orders": 63, "lifetime_value": "$7,800", "last_order": "2026-05-28"},
            {"customer": "Bob Smith", "orders": 54, "lifetime_value": "$5,910", "last_order": "2026-05-29"},
            {"customer": "Grace Kim", "orders": 47, "lifetime_value": "$4,230", "last_order": "2026-05-27"},
        ]
    )
