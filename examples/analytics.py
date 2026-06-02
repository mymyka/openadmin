from openadmin import AdminPage, AreaChart

page = AdminPage("Analytics")


@page.area_chart(
    "User Growth", description="New vs returning users over the last 6 months"
)
async def user_growth() -> AreaChart:
    return AreaChart(
        data=[
            {"month": "Jan", "new": 420, "returning": 1200},
            {"month": "Feb", "new": 380, "returning": 1350},
            {"month": "Mar", "new": 510, "returning": 1480},
            {"month": "Apr", "new": 670, "returning": 1620},
            {"month": "May", "new": 590, "returning": 1740},
            {"month": "Jun", "new": 740, "returning": 1890},
        ],
        config={
            "new": {"label": "New Users", "color": "hsl(var(--chart-1))"},
            "returning": {"label": "Returning Users", "color": "hsl(var(--chart-2))"},
        },
    )


@page.area_chart("Revenue Breakdown", description="Monthly revenue by plan tier")
async def revenue_breakdown() -> AreaChart:
    return AreaChart(
        data=[
            {"month": "Jan", "free": 0, "pro": 8400, "enterprise": 32000},
            {"month": "Feb", "free": 0, "pro": 9100, "enterprise": 34500},
            {"month": "Mar", "free": 0, "pro": 10200, "enterprise": 37000},
            {"month": "Apr", "free": 0, "pro": 11800, "enterprise": 41000},
            {"month": "May", "free": 0, "pro": 13400, "enterprise": 44500},
            {"month": "Jun", "free": 0, "pro": 15200, "enterprise": 49000},
        ],
        config={
            "free": {"label": "Free", "color": "hsl(var(--chart-3))"},
            "pro": {"label": "Pro", "color": "hsl(var(--chart-1))"},
            "enterprise": {"label": "Enterprise", "color": "hsl(var(--chart-2))"},
        },
    )


@page.area_chart("API Requests", description="Daily API call volume over the past week")
async def api_requests() -> AreaChart:
    return AreaChart(
        data=[
            {"day": "Mon", "requests": 142000},
            {"day": "Tue", "requests": 168000},
            {"day": "Wed", "requests": 195000},
            {"day": "Thu", "requests": 173000},
            {"day": "Fri", "requests": 210000},
            {"day": "Sat", "requests": 98000},
            {"day": "Sun", "requests": 74000},
        ],
        config={
            "requests": {"label": "API Requests", "color": "hsl(var(--chart-4))"},
        },
    )
