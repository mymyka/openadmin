import asyncio
import random

from fastapi import HTTPException, Request

from openadmin import AdminPage, PaginationParamsDep, Stat, Table

from . import db

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
    return Stat(value=len(db.opt_outs))


@page.stat(
    "Failed Deliveries", description="Notifications that failed to deliver today"
)
async def failed_deliveries() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=320)


@page.action_delete("Delete notification", description="Remove a broadcast notification record")
async def delete_notification(id: int) -> None:
    if id not in db.notifications:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.notifications.pop(id)


@page.action_delete("Remove opt-out", description="Re-subscribe a user who opted out")
async def remove_opt_out(id: int) -> None:
    if id not in db.opt_outs:
        raise HTTPException(status_code=404, detail="Opt-out record not found")
    db.opt_outs.pop(id)


@page.table(
    "Recent Broadcasts",
    description="Latest notifications sent to all or large user segments",
)
async def recent_broadcasts(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(db.notifications.values(), key=lambda n: n["date"], reverse=True)
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "title": n["title"],
            "recipients": n["recipients"],
            "channel": n["channel"],
            "open_rate": n["open_rate"],
            "date": n["date"],
            "__actions__": [
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(delete_notification.__name__)) + f"?id={n['id']}",
                }
            ],
        }
        for n in page_rows
    ])


@page.table(
    "Delivery Failures", description="Notifications that could not be delivered"
)
async def delivery_failures() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"user": "user#8810", "channel": "push", "reason": "token expired", "notification": "New Feature: Dark Mode", "date": "2026-05-30"},
            {"user": "user#4221", "channel": "push", "reason": "device unregistered", "notification": "New Feature: Dark Mode", "date": "2026-05-30"},
            {"user": "user#1090", "channel": "email", "reason": "invalid address", "notification": "Weekly summary", "date": "2026-05-29"},
        ]
    )


@page.table(
    "Opt-Out Trends", description="Daily notification opt-outs over the past week"
)
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


@page.table(
    "Recent Opt-Outs", description="Users who recently disabled notifications"
)
async def recent_opt_outs(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(db.opt_outs.values(), key=lambda o: o["date"], reverse=True)
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "user": o["user"],
            "channel": o["channel"],
            "reason": o["reason"],
            "date": o["date"],
            "__actions__": [
                {
                    "color": "warning",
                    "method": "DELETE",
                    "url": str(req.url_for(remove_opt_out.__name__)) + f"?id={o['id']}",
                }
            ],
        }
        for o in page_rows
    ])


@page.table(
    "Notification Preferences", description="Breakdown of user channel preferences"
)
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
