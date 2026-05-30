import asyncio
import random

from fastapi import HTTPException, Request

from openadmin import AdminPage, PaginationParamsDep, Stat, Table

from . import db

page = AdminPage("Emails")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# Email Campaigns

Monitor campaign performance, delivery health, and upcoming sends.

## Performance Benchmarks

| Metric | This Month | Industry Average | Status |
|---|---|---|---|
| Open Rate | 28.4% | 20–25% | Above average |
| Click Rate | 4.1% | 2–5% | On target |
| Bounce Rate | 0.73% | < 2% | Healthy |
| Unsubscribe Rate | 0.14% | < 0.5% | Healthy |

## Campaign Types

- **Product updates** — highest engagement; users want to know what's new
- **Re-engagement** — lower open rates are expected; measure by reactivation, not opens
- **Weekly digest** — consistent performer; schedule consistency matters more than copy
- **Feature announcements** — best click-through rates when linked to a specific landing page

> The "Feature Announcement: Exports" campaign achieved an **8.1% click rate** — the highest this month. Attribute it to a direct CTA linking to a specific feature page rather than the homepage.

## Delivery Health

- **Hard bounces** (`old@deactivated.com`) should be removed from lists immediately to protect sender reputation
- **Soft bounces** retry automatically; remove after 3 consecutive failures
- **Blocked** emails (`noreply@block.org`) indicate domain-level filtering — do not retry

## Upcoming Sends

June Newsletter (21,400 recipients) is scheduled for **2026-06-01 09:00 UTC**. Ensure the content is finalised and preview-tested at least 24 hours before dispatch.
"""


@page.stat("Sent Today", description="Emails dispatched in the last 24 hours")
async def sent_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=24_810)


@page.stat("Open Rate", description="Average open rate for this month's campaigns")
async def open_rate() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="28.4%")


@page.stat("Click Rate", description="Average click-through rate this month")
async def click_rate() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="4.1%")


@page.stat("Bounced", description="Emails that failed delivery today")
async def bounced() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=len(db.email_bounces))


@page.stat("Unsubscribes Today", description="Users who opted out in the last 24 hours")
async def unsubscribes_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=34)


@page.action_delete("Cancel campaign", description="Cancel a scheduled campaign")
async def cancel_campaign(id: int) -> None:
    if id not in db.email_campaigns:
        raise HTTPException(status_code=404, detail="Campaign not found")
    if db.email_campaigns[id]["status"] == "sent":
        raise HTTPException(status_code=400, detail="Cannot cancel a campaign that has already been sent")
    db.email_campaigns.pop(id)


@page.action_delete("Remove bounce", description="Remove an address from the bounce list")
async def remove_bounce(id: int) -> None:
    if id not in db.email_bounces:
        raise HTTPException(status_code=404, detail="Bounce record not found")
    db.email_bounces.pop(id)


@page.table("Recent Campaigns", description="Last email campaigns sent")
async def recent_campaigns(pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(
        [c for c in db.email_campaigns.values() if c["status"] == "sent"],
        key=lambda c: c["date"],
        reverse=True,
    )
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "campaign": c["campaign"],
            "sent": c["sent"],
            "open_rate": c["open_rate"],
            "click_rate": c["click_rate"],
            "date": c["date"],
        }
        for c in page_rows
    ])


@page.table("Delivery Failures", description="Emails that bounced or failed recently")
async def delivery_failures(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = list(db.email_bounces.values())
    start = pagination.page * pagination.per_page
    return Table(data=[
        {
            "email": b["email"],
            "type": b["type"],
            "campaign": b["campaign"],
            "date": b["date"],
            "__actions__": [
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(remove_bounce.__name__)) + f"?id={b['id']}",
                }
            ],
        }
        for b in rows[start : start + pagination.per_page]
    ])


@page.table(
    "Scheduled Campaigns", description="Upcoming email campaigns queued for delivery"
)
async def scheduled_campaigns(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = [c for c in db.email_campaigns.values() if c["status"] == "scheduled"]
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "campaign": c["campaign"],
            "recipients": c["recipients"],
            "scheduled": c["scheduled"],
            "status": c["status"],
            "__actions__": [
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(cancel_campaign.__name__)) + f"?id={c['id']}",
                }
            ],
        }
        for c in page_rows
    ])


@page.table(
    "Top Links Clicked",
    description="Most-clicked links across all campaigns this month",
)
async def top_links() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"url": "/pricing", "clicks": 4_820, "campaign": "Feature Announcement: Exports", "ctr": "21.8%"},
            {"url": "/blog/new-exports", "clicks": 3_210, "campaign": "Feature Announcement: Exports", "ctr": "14.5%"},
            {"url": "/changelog", "clicks": 2_108, "campaign": "May Product Update", "ctr": "11.4%"},
            {"url": "/dashboard", "clicks": 1_840, "campaign": "Weekly Digest #21", "ctr": "14.4%"},
        ]
    )
