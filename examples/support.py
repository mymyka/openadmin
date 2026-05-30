import asyncio
import random

from openadmin import AdminPage, Stat, Table

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
    return Stat(value=47)


@page.stat("Resolved Today", description="Tickets closed in the last 24 hours")
async def resolved_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=31)


@page.stat("Avg Response Time", description="Mean first-response time this week")
async def avg_response_time() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="1h 48m")


@page.stat("Customer Satisfaction", description="CSAT score from recent surveys")
async def csat_score() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="92%")


@page.table("Open Tickets", description="All currently unresolved support requests")
async def open_tickets_list() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"id": "#T-4401", "subject": "Cannot access my account", "user": "locked@example.com", "priority": "high", "opened": "2026-05-30"},
            {"id": "#T-4400", "subject": "Wrong charge on invoice", "user": "billing@corp.com", "priority": "high", "opened": "2026-05-30"},
            {"id": "#T-4398", "subject": "Feature request: dark mode", "user": "dev@startup.io", "priority": "low", "opened": "2026-05-29"},
            {"id": "#T-4395", "subject": "Integration not working", "user": "ops@company.net", "priority": "medium", "opened": "2026-05-29"},
            {"id": "#T-4390", "subject": "How to export data?", "user": "newbie@example.com", "priority": "low", "opened": "2026-05-28"},
        ]
    )


@page.table("Recently Resolved", description="Tickets closed in the last 3 days")
async def recently_resolved() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"id": "#T-4399", "subject": "Password reset not arriving", "resolved_by": "agent_sarah", "time_to_close": "2h 10m", "date": "2026-05-30"},
            {"id": "#T-4397", "subject": "API rate limit confusion", "resolved_by": "agent_mark", "time_to_close": "45m", "date": "2026-05-30"},
            {"id": "#T-4396", "subject": "Data export failed", "resolved_by": "agent_sarah", "time_to_close": "3h 22m", "date": "2026-05-29"},
            {"id": "#T-4394", "subject": "Billing period question", "resolved_by": "agent_tom", "time_to_close": "18m", "date": "2026-05-29"},
            {"id": "#T-4391", "subject": "Can't invite team members", "resolved_by": "agent_mark", "time_to_close": "1h 05m", "date": "2026-05-28"},
        ]
    )


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
