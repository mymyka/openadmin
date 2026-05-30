import asyncio
import random

from openadmin import AdminPage, Stat, Table

page = AdminPage("Users Tasks")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# User Tasks

Monitor task completion rates, overdue items, and platform-wide engagement with user-assigned actions.

## Task Status Breakdown

| Status | Count | Share | Notes |
|---|---|---|---|
| `completed` | 6,820 | 78.0% | Closed tasks |
| `pending` | 933 | 10.7% | Not yet started |
| `in_progress` | 894 | 10.2% | Actively being worked |
| `overdue` | 94 | 1.1% | Past due date, incomplete |

## Completion Rate

The current monthly completion rate is **78.4%** — a healthy signal for user engagement. Tasks that remain in `pending` for more than 7 days with no status change are candidates for a nudge notification.

> Overdue tasks should not be automatically closed or deleted. Users may still complete them; closure should be user-initiated. Admins can mark tasks `cancelled` when the underlying requirement is no longer valid.

## Overdue Task Policy

- Tasks overdue by **< 7 days** — send a reminder notification
- Tasks overdue by **7–14 days** — flag for support follow-up
- Tasks overdue by **> 14 days** — eligible for admin-assisted resolution or cancellation

## Task Assignment Sources

Tasks are created either by users themselves or system-generated (e.g. onboarding steps, subscription renewals, compliance actions like "Submit tax documents"). System-generated tasks cannot be deleted by users — only admins can cancel them.
"""


@page.stat("Total Tasks", description="Total number of tasks across all users")
async def total_tasks() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=8_741)


@page.stat("Completed Today", description="Tasks marked complete today")
async def completed_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=312)


@page.stat("Overdue Tasks", description="Tasks past their due date")
async def overdue_tasks() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=94)


@page.stat("Completion Rate", description="Percentage of tasks completed this month")
async def completion_rate() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="78.4%")


@page.table("Recent Tasks", description="Latest tasks created across all users")
async def recent_tasks() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "id": 1021,
                "user": "Alice Johnson",
                "title": "Review Q2 report",
                "status": "in_progress",
                "due": "2026-06-01",
            },
            {
                "id": 1020,
                "user": "Bob Smith",
                "title": "Update billing info",
                "status": "pending",
                "due": "2026-05-31",
            },
            {
                "id": 1019,
                "user": "Carol White",
                "title": "Export user data",
                "status": "completed",
                "due": "2026-05-30",
            },
            {
                "id": 1018,
                "user": "David Brown",
                "title": "Schedule team meeting",
                "status": "completed",
                "due": "2026-05-29",
            },
            {
                "id": 1017,
                "user": "Eva Martinez",
                "title": "Submit tax documents",
                "status": "overdue",
                "due": "2026-05-25",
            },
        ]
    )


@page.table("Overdue Tasks", description="Tasks that have passed their due date")
async def overdue_task_list() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "id": 998,
                "user": "Frank Lee",
                "title": "Confirm subscription renewal",
                "due": "2026-05-20",
                "days_overdue": 10,
            },
            {
                "id": 987,
                "user": "Eva Martinez",
                "title": "Submit tax documents",
                "due": "2026-05-25",
                "days_overdue": 5,
            },
            {
                "id": 975,
                "user": "Hank Davis",
                "title": "Upload profile photo",
                "due": "2026-05-22",
                "days_overdue": 8,
            },
        ]
    )


@page.table("Task Status Summary", description="Breakdown of all tasks by status")
async def task_status_summary() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"status": "completed", "count": 6820, "percentage": "78.0%"},
            {"status": "in_progress", "count": 894, "percentage": "10.2%"},
            {"status": "pending", "count": 933, "percentage": "10.7%"},
            {"status": "overdue", "count": 94, "percentage": "1.1%"},
        ]
    )
