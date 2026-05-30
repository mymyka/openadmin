from openadmin import AdminPage, Stat, Table

page = AdminPage("Analytics")


@page.stat("Page Views Today", description="Total page views in the last 24 hours")
def page_views_today() -> Stat:
    return Stat(value=128_450)


@page.stat("Unique Visitors", description="Distinct visitors today")
def unique_visitors() -> Stat:
    return Stat(value=42_318)


@page.stat("Bounce Rate", description="Percentage of single-page sessions")
def bounce_rate() -> Stat:
    return Stat(value="38.4%")


@page.stat("Avg Session Duration", description="Mean time users spend per session")
def avg_session_duration() -> Stat:
    return Stat(value="4m 12s")


@page.stat("Conversion Rate", description="Visitors who completed a goal action")
def conversion_rate() -> Stat:
    return Stat(value="3.7%")


@page.table("Top Pages", description="Most visited pages in the last 7 days")
def top_pages() -> Table:
    return Table(
        data=[
            {"path": "/", "views": 98_210, "unique": 61_400, "avg_time": "1m 05s"},
            {"path": "/blog", "views": 54_320, "unique": 38_200, "avg_time": "3m 44s"},
            {"path": "/pricing", "views": 31_880, "unique": 24_100, "avg_time": "2m 58s"},
            {
                "path": "/docs",
                "views": 29_440,
                "unique": 18_750,
                "avg_time": "7m 21s",
            },
            {
                "path": "/signup",
                "views": 18_920,
                "unique": 17_300,
                "avg_time": "0m 52s",
            },
        ]
    )


@page.table("Traffic Sources", description="Where visitors are coming from")
def traffic_sources() -> Table:
    return Table(
        data=[
            {"source": "Organic Search", "sessions": 58_400, "share": "45.4%", "conversions": 2104},
            {"source": "Direct", "sessions": 31_200, "share": "24.3%", "conversions": 1388},
            {"source": "Referral", "sessions": 18_900, "share": "14.7%", "conversions": 820},
            {"source": "Social", "sessions": 14_300, "share": "11.1%", "conversions": 490},
            {"source": "Email", "sessions": 5_800, "share": "4.5%", "conversions": 390},
        ]
    )


@page.table("Top Countries", description="Visitor geography breakdown")
def top_countries() -> Table:
    return Table(
        data=[
            {"country": "United States", "visitors": 41_200, "share": "32.1%", "avg_pages": 4.2},
            {"country": "United Kingdom", "visitors": 18_400, "share": "14.3%", "avg_pages": 3.8},
            {"country": "Germany", "visitors": 12_100, "share": "9.4%", "avg_pages": 3.5},
            {"country": "India", "visitors": 10_800, "share": "8.4%", "avg_pages": 3.1},
            {"country": "Canada", "visitors": 9_200, "share": "7.2%", "avg_pages": 4.0},
        ]
    )


@page.table("Device Breakdown", description="Sessions split by device type")
def device_breakdown() -> Table:
    return Table(
        data=[
            {"device": "Desktop", "sessions": 68_400, "share": "53.2%", "bounce_rate": "31.2%"},
            {"device": "Mobile", "sessions": 48_200, "share": "37.5%", "bounce_rate": "48.7%"},
            {"device": "Tablet", "sessions": 11_800, "share": "9.2%", "bounce_rate": "39.1%"},
        ]
    )


@page.table("Recent Events", description="Latest tracked user interactions")
def recent_events() -> Table:
    return Table(
        data=[
            {"time": "2026-05-30 12:44", "event": "signup", "user": "anonymous", "page": "/signup"},
            {"time": "2026-05-30 12:43", "event": "purchase", "user": "user#9821", "page": "/checkout"},
            {"time": "2026-05-30 12:41", "event": "download", "user": "user#4412", "page": "/docs"},
            {"time": "2026-05-30 12:40", "event": "signup", "user": "anonymous", "page": "/signup"},
            {"time": "2026-05-30 12:38", "event": "video_play", "user": "user#3301", "page": "/demo"},
        ]
    )
