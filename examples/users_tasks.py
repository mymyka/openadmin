from openadmin import AdminPage, Stat, Table

page = AdminPage("Users Tasks")


@page.stat("Total Tasks", description="Total number of tasks across all users")
def total_tasks() -> Stat[int]:
    return Stat(value=8_741)


@page.stat("Completed Today", description="Tasks marked complete today")
def completed_today() -> Stat[int]:
    return Stat(value=312)


@page.stat("Overdue Tasks", description="Tasks past their due date")
def overdue_tasks() -> Stat[int]:
    return Stat(value=94)


@page.stat("Completion Rate", description="Percentage of tasks completed this month")
def completion_rate() -> Stat[str]:
    return Stat(value="78.4%")


@page.table("Recent Tasks", description="Latest tasks created across all users")
def recent_tasks() -> Table:
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
def overdue_task_list() -> Table:
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
def task_status_summary() -> Table:
    return Table(
        data=[
            {"status": "completed", "count": 6820, "percentage": "78.0%"},
            {"status": "in_progress", "count": 894, "percentage": "10.2%"},
            {"status": "pending", "count": 933, "percentage": "10.7%"},
            {"status": "overdue", "count": 94, "percentage": "1.1%"},
        ]
    )
