import asyncio
import random

from openadmin import AdminPage, Stat, Table

page = AdminPage("Notifications")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# Notifications

Track delivery rates, engagement, and opt-out trends across push, in-app, email, and SMS channels.

## Channel Opt-In Rates

| Channel | Enabled | Opt-In Rate | Notes |
|---|---|---|---|
| In-App | 12,840 | 89.3% | Default on; highest reach |
| Email | 11,400 | 79.3% | Transactional vs. marketing rules apply |
| Push | 9,210 | 64.0% | Requires explicit browser/device permission |
| SMS | 3,820 | 26.6% | Lowest adoption; high engagement when used |

## Engagement Benchmarks

- **Open Rate** — current average is **21.4%**; industry median for SaaS push is 18–25%
- **In-app notifications** typically outperform push in open rate by 15–20 percentage points
- Broadcasts with a personalised subject line see 30–40% higher open rates

> Sending more than **3 broadcast notifications per week** significantly increases opt-out rates. Reserve broadcasts for genuinely important events — feature launches, maintenance windows, and security notices.

## Opt-Out Trend

Opt-outs spiked on **2026-05-28** (110 opt-outs vs. 140 opt-ins) following the maintenance window notification. Review the messaging for that broadcast — users who opt out after operational notices often prefer a lower-urgency format (e.g. in-app banner instead of push).

## Failed Deliveries

320 failures today. Most are due to expired push tokens (devices unregistered or app uninstalled). These should be pruned from the active token store to avoid inflating delivery attempt counts.
"""


@page.stat("Sent Today", description="Push and in-app notifications delivered today")
async def sent_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=84_210)


@page.stat("Open Rate", description="Notification open rate this week")
async def open_rate() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="21.4%")


@page.stat("Opted-Out Users", description="Users who disabled all notifications")
async def opted_out() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=2_840)


@page.stat("Failed Deliveries", description="Notifications that failed to deliver today")
async def failed_deliveries() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=320)


@page.table("Recent Broadcasts", description="Latest notifications sent to all or large user segments")
async def recent_broadcasts() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
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
async def delivery_failures() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"user": "user#8810", "channel": "push", "reason": "token expired", "notification": "New feature: Dark Mode", "date": "2026-05-30"},
            {"user": "user#4221", "channel": "push", "reason": "device unregistered", "notification": "New feature: Dark Mode", "date": "2026-05-30"},
            {"user": "user#1090", "channel": "email", "reason": "invalid address", "notification": "Weekly summary", "date": "2026-05-29"},
        ]
    )


@page.table("Opt-Out Trends", description="Daily notification opt-outs over the past week")
async def opt_out_trends() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
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
async def channel_preferences() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"channel": "in-app", "enabled": 12_840, "disabled": 1_542, "rate": "89.3%"},
            {"channel": "push", "enabled": 9_210, "disabled": 5_172, "rate": "64.0%"},
            {"channel": "email", "enabled": 11_400, "disabled": 2_982, "rate": "79.3%"},
            {"channel": "sms", "enabled": 3_820, "disabled": 10_562, "rate": "26.6%"},
        ]
    )
