from openadmin import AdminPage, Stat, Table

page = AdminPage("Orders")


@page.stat("Orders Today", description="New orders placed in the last 24 hours")
def orders_today() -> Stat:
    return Stat(value=348)


@page.stat("Pending Fulfillment", description="Orders awaiting processing or shipment")
def pending_fulfillment() -> Stat:
    return Stat(value=84)


@page.stat("Completed This Month", description="Orders fulfilled in May 2026")
def completed_month() -> Stat:
    return Stat(value=4_821)


@page.stat("Avg Order Value", description="Mean order value this month")
def avg_order_value() -> Stat:
    return Stat(value="$67.40")


@page.stat("Cancellation Rate", description="Percentage of orders cancelled this month")
def cancellation_rate() -> Stat:
    return Stat(value="2.8%")


@page.table("Recent Orders", description="Latest orders placed on the platform")
def recent_orders() -> Table:
    return Table(
        data=[
            {"order_id": "#ORD-9901", "customer": "Alice Johnson", "total": "$142.00", "status": "shipped", "date": "2026-05-30"},
            {"order_id": "#ORD-9900", "customer": "Bob Smith", "total": "$88.50", "status": "processing", "date": "2026-05-30"},
            {"order_id": "#ORD-9899", "customer": "Carol White", "total": "$31.99", "status": "delivered", "date": "2026-05-30"},
            {"order_id": "#ORD-9898", "customer": "Dan Brown", "total": "$214.00", "status": "pending", "date": "2026-05-29"},
            {"order_id": "#ORD-9897", "customer": "Eva Martinez", "total": "$55.00", "status": "shipped", "date": "2026-05-29"},
        ]
    )


@page.table("Orders by Status", description="Current distribution of order statuses")
def orders_by_status() -> Table:
    return Table(
        data=[
            {"status": "delivered", "count": 3_840, "share": "79.6%"},
            {"status": "shipped", "count": 412, "share": "8.5%"},
            {"status": "processing", "count": 280, "share": "5.8%"},
            {"status": "pending", "count": 154, "share": "3.2%"},
            {"status": "cancelled", "count": 135, "share": "2.8%"},
        ]
    )


@page.table("Flagged Orders", description="Orders flagged for manual review")
def flagged_orders() -> Table:
    return Table(
        data=[
            {"order_id": "#ORD-9880", "customer": "suspicious@email.xyz", "total": "$899.00", "flag": "fraud-risk", "date": "2026-05-29"},
            {"order_id": "#ORD-9851", "customer": "John Doe", "total": "$412.00", "flag": "address-mismatch", "date": "2026-05-28"},
            {"order_id": "#ORD-9810", "customer": "bulk@buyer.com", "total": "$1,800.00", "flag": "high-value", "date": "2026-05-27"},
        ]
    )


@page.table("Top Customers", description="Customers by total lifetime spend")
def top_customers() -> Table:
    return Table(
        data=[
            {"customer": "TechCorp Inc.", "orders": 142, "lifetime_value": "$18,420", "last_order": "2026-05-30"},
            {"customer": "Alice Johnson", "orders": 88, "lifetime_value": "$9,240", "last_order": "2026-05-30"},
            {"customer": "StartupXYZ", "orders": 63, "lifetime_value": "$7,800", "last_order": "2026-05-28"},
            {"customer": "Bob Smith", "orders": 54, "lifetime_value": "$5,910", "last_order": "2026-05-29"},
            {"customer": "Grace Kim", "orders": 47, "lifetime_value": "$4,230", "last_order": "2026-05-27"},
        ]
    )
