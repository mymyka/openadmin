from openadmin import AdminPage, Stat, Table

page = AdminPage("Emails")


@page.stat("Sent Today", description="Emails dispatched in the last 24 hours")
def sent_today() -> Stat:
    return Stat(value=24_810)


@page.stat("Open Rate", description="Average open rate for this month's campaigns")
def open_rate() -> Stat:
    return Stat(value="28.4%")


@page.stat("Click Rate", description="Average click-through rate this month")
def click_rate() -> Stat:
    return Stat(value="4.1%")


@page.stat("Bounced", description="Emails that failed delivery today")
def bounced() -> Stat:
    return Stat(value=182)


@page.stat("Unsubscribes Today", description="Users who opted out in the last 24 hours")
def unsubscribes_today() -> Stat:
    return Stat(value=34)


@page.table("Recent Campaigns", description="Last email campaigns sent")
def recent_campaigns() -> Table:
    return Table(
        data=[
            {
                "campaign": "May Product Update",
                "sent": 18_400,
                "open_rate": "31.2%",
                "click_rate": "5.8%",
                "date": "2026-05-28",
            },
            {
                "campaign": "Re-engagement: Inactive Users",
                "sent": 4_200,
                "open_rate": "18.7%",
                "click_rate": "2.4%",
                "date": "2026-05-25",
            },
            {
                "campaign": "Weekly Digest #21",
                "sent": 12_800,
                "open_rate": "29.4%",
                "click_rate": "4.2%",
                "date": "2026-05-24",
            },
            {
                "campaign": "Feature Announcement: Exports",
                "sent": 22_100,
                "open_rate": "34.8%",
                "click_rate": "8.1%",
                "date": "2026-05-20",
            },
        ]
    )


@page.table("Delivery Failures", description="Emails that bounced or failed recently")
def delivery_failures() -> Table:
    return Table(
        data=[
            {"email": "old@deactivated.com", "type": "hard-bounce", "campaign": "May Product Update", "date": "2026-05-28"},
            {"email": "full@inbox.net", "type": "soft-bounce", "campaign": "May Product Update", "date": "2026-05-28"},
            {"email": "noreply@block.org", "type": "blocked", "campaign": "Weekly Digest #21", "date": "2026-05-24"},
            {"email": "typo@@example.com", "type": "invalid", "campaign": "May Product Update", "date": "2026-05-28"},
        ]
    )


@page.table("Scheduled Campaigns", description="Upcoming email campaigns queued for delivery")
def scheduled_campaigns() -> Table:
    return Table(
        data=[
            {"campaign": "June Newsletter", "recipients": 21_400, "scheduled": "2026-06-01 09:00", "status": "queued"},
            {"campaign": "Promo: Summer Sale", "recipients": 18_900, "scheduled": "2026-06-05 10:00", "status": "draft"},
            {"campaign": "Onboarding Day 7", "recipients": 840, "scheduled": "2026-06-02 08:00", "status": "queued"},
        ]
    )


@page.table("Top Links Clicked", description="Most-clicked links across all campaigns this month")
def top_links() -> Table:
    return Table(
        data=[
            {"url": "/pricing", "clicks": 4_820, "campaign": "Feature Announcement: Exports", "ctr": "21.8%"},
            {"url": "/blog/new-exports", "clicks": 3_210, "campaign": "Feature Announcement: Exports", "ctr": "14.5%"},
            {"url": "/changelog", "clicks": 2_108, "campaign": "May Product Update", "ctr": "11.4%"},
            {"url": "/dashboard", "clicks": 1_840, "campaign": "Weekly Digest #21", "ctr": "14.4%"},
        ]
    )
