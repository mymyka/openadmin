import asyncio
import random

from fastapi import HTTPException, Request

from openadmin import AdminPage, PaginationParamsDep, Stat, Table

from . import db

page = AdminPage("Support")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# Support Operations

Monitor ticket volume, agent performance, and customer satisfaction across all support channels.

## SLA Targets

| Priority | First Response | Resolution |
|---|---|---|
| High | < 1 hour | < 8 hours |
| Medium | < 4 hours | < 24 hours |
| Low | < 24 hours | < 72 hours |

## This Week at a Glance

- Current CSAT score is **92%** — above the target of 90%
- Avg first response time is **1h 48m**, within SLA for high-priority tickets
- `billing` and `access` categories have the highest open counts and should be prioritised

> Tickets in the `bug-report` category have the longest average close time (4h 40m). Where possible, escalate confirmed bugs to engineering with a linked ticket so agents can close their side promptly.

## Team Performance

**agent_sarah** leads the team with 148 closed tickets and a 96% CSAT this month. Agents below 90% CSAT should be reviewed for coaching opportunities rather than penalised — low scores often correlate with inheriting the hardest ticket categories.

## Feature Requests

Feature requests currently have no average close time — this is by design. They are logged, tagged, and forwarded to the product team monthly. Agents should not promise delivery timelines to users.
"""


@page.stat("Open Tickets", description="Unresolved support tickets")
async def open_tickets() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for t in db.tickets.values() if t["status"] == "open"))


@page.stat("Resolved Today", description="Tickets closed in the last 24 hours")
async def resolved_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for t in db.tickets.values() if t["status"] == "resolved"))


@page.stat("Avg Response Time", description="Mean first-response time this week")
async def avg_response_time() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="1h 48m")


@page.stat("Customer Satisfaction", description="CSAT score from recent surveys")
async def csat_score() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="92%")


@page.action_post("Close ticket", description="Mark a ticket as resolved")
async def close_ticket(id: int) -> None:
    if id not in db.tickets:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.tickets[id]["status"] = "resolved"
    db.tickets[id]["resolved_by"] = "admin"
    db.tickets[id]["time_to_close"] = "manual"


@page.action_delete("Delete ticket", description="Permanently remove a ticket")
async def delete_ticket(id: int) -> None:
    if id not in db.tickets:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.tickets.pop(id)


@page.table("Open Tickets", description="All currently unresolved support requests")
async def open_tickets_list(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = [t for t in db.tickets.values() if t["status"] == "open"]
    rows.sort(key=lambda t: ({"high": 0, "medium": 1, "low": 2}.get(t["priority"], 3), t["opened"]))
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "id": f"#T-{t['id']}",
            "subject": t["subject"],
            "user": t["user"],
            "priority": t["priority"],
            "opened": t["opened"],
            "__actions__": [
                {
                    "color": "success",
                    "method": "POST",
                    "url": str(req.url_for(close_ticket.__name__)) + f"?id={t['id']}",
                },
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(delete_ticket.__name__)) + f"?id={t['id']}",
                },
            ],
        }
        for t in page_rows
    ])


@page.table("Recently Resolved", description="Tickets closed in the last 3 days")
async def recently_resolved(pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(
        [t for t in db.tickets.values() if t["status"] == "resolved"],
        key=lambda t: t["opened"],
        reverse=True,
    )
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "id": f"#T-{t['id']}",
            "subject": t["subject"],
            "resolved_by": t["resolved_by"],
            "time_to_close": t["time_to_close"],
            "date": t["opened"],
        }
        for t in page_rows
    ])


@page.table("Tickets by Category", description="Volume of tickets grouped by topic")
async def tickets_by_category() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"category": "billing", "open": 12, "resolved_this_month": 84, "avg_close_time": "1h 30m"},
            {"category": "access", "open": 10, "resolved_this_month": 71, "avg_close_time": "2h 15m"},
            {"category": "bug-report", "open": 9, "resolved_this_month": 45, "avg_close_time": "4h 40m"},
            {"category": "how-to", "open": 8, "resolved_this_month": 120, "avg_close_time": "0h 28m"},
            {"category": "feature-request", "open": 8, "resolved_this_month": 22, "avg_close_time": "N/A"},
        ]
    )


@page.table("Agent Performance", description="Support team stats for this month")
async def agent_performance() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"agent": "agent_sarah", "closed": 148, "avg_time": "1h 12m", "csat": "96%"},
            {"agent": "agent_mark", "closed": 132, "avg_time": "1h 44m", "csat": "94%"},
            {"agent": "agent_tom", "closed": 119, "avg_time": "2h 01m", "csat": "91%"},
            {"agent": "agent_lisa", "closed": 104, "avg_time": "1h 58m", "csat": "89%"},
        ]
    )
