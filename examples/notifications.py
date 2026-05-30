from openadmin import AdminPage, Stat, Table

page = AdminPage("Notifications")


@page.stat("Sent Today", description="Push and in-app notifications delivered today")
def sent_today() -> Stat:
    return Stat(value=84_210)


@page.stat("Open Rate", description="Notification open rate this week")
def open_rate() -> Stat:
    return Stat(value="21.4%")


@page.stat("Opted-Out Users", description="Users who disabled all notifications")
def opted_out() -> Stat:
    return Stat(value=2_840)


@page.stat("Failed Deliveries", description="Notifications that failed to deliver today")
def failed_deliveries() -> Stat:
    return Stat(value=320)


@page.table("Recent Broadcasts", description="Latest notifications sent to all or large user segments")
def recent_broadcasts() -> Table:
    return Table(
        data=[
            {
                "title": "New feature: Dark Mode",
                "recipients": 14_200,
                "channel": "push",
                "open_rate": "24.8%",
                "date": "2026-05-30",
            },
            {
                "title": "Your weekly summary is ready",
                "recipients": 12_800,
                "channel": "in-app",
                "open_rate": "41.2%",
                "date": "2026-05-29",
            },
            {
                "title": "Scheduled maintenance tonight",
                "recipients": 14_382,
                "channel": "push",
                "open_rate": "32.1%",
                "date": "2026-05-28",
            },
            {
                "title": "You have unread messages",
                "recipients": 8_400,
                "channel": "email",
                "open_rate": "19.4%",
                "date": "2026-05-27",
            },
        ]
    )


@page.table("Delivery Failures", description="Notifications that could not be delivered")
def delivery_failures() -> Table:
    return Table(
        data=[
            {"user": "user#8810", "channel": "push", "reason": "token expired", "notification": "New feature: Dark Mode", "date": "2026-05-30"},
            {"user": "user#4221", "channel": "push", "reason": "device unregistered", "notification": "New feature: Dark Mode", "date": "2026-05-30"},
            {"user": "user#1090", "channel": "email", "reason": "invalid address", "notification": "Weekly summary", "date": "2026-05-29"},
        ]
    )


@page.table("Opt-Out Trends", description="Daily notification opt-outs over the past week")
def opt_out_trends() -> Table:
    return Table(
        data=[
            {"date": "2026-05-24", "opt_outs": 84, "opt_ins": 210},
            {"date": "2026-05-25", "opt_outs": 91, "opt_ins": 198},
            {"date": "2026-05-26", "opt_outs": 78, "opt_ins": 182},
            {"date": "2026-05-27", "opt_outs": 64, "opt_ins": 220},
            {"date": "2026-05-28", "opt_outs": 110, "opt_ins": 140},
            {"date": "2026-05-29", "opt_outs": 72, "opt_ins": 191},
            {"date": "2026-05-30", "opt_outs": 54, "opt_ins": 174},
        ]
    )


@page.table("Notification Preferences", description="Breakdown of user channel preferences")
def channel_preferences() -> Table:
    return Table(
        data=[
            {"channel": "in-app", "enabled": 12_840, "disabled": 1_542, "rate": "89.3%"},
            {"channel": "push", "enabled": 9_210, "disabled": 5_172, "rate": "64.0%"},
            {"channel": "email", "enabled": 11_400, "disabled": 2_982, "rate": "79.3%"},
            {"channel": "sms", "enabled": 3_820, "disabled": 10_562, "rate": "26.6%"},
        ]
    )
