from openadmin import AdminPage, Stat, Table

page = AdminPage("Logs")


@page.stat("Errors Today", description="Application errors logged in the last 24 hours")
def errors_today() -> Stat:
    return Stat(value=142)


@page.stat("Warnings Today", description="Warning-level log events today")
def warnings_today() -> Stat:
    return Stat(value=830)


@page.stat("Critical Alerts", description="Critical-severity events in the last 7 days")
def critical_alerts() -> Stat:
    return Stat(value=3)


@page.stat("Log Volume (24h)", description="Total log lines ingested today")
def log_volume() -> Stat:
    return Stat(value="4.2M")


@page.table("Recent Errors", description="Latest application errors")
def recent_errors() -> Table:
    return Table(
        data=[
            {
                "time": "2026-05-30 12:48",
                "level": "ERROR",
                "service": "api",
                "message": "Database connection timeout",
                "count": 14,
            },
            {
                "time": "2026-05-30 12:21",
                "level": "ERROR",
                "service": "worker",
                "message": "Job queue backlog exceeded 10k",
                "count": 1,
            },
            {
                "time": "2026-05-30 11:54",
                "level": "ERROR",
                "service": "api",
                "message": "Unhandled exception in /checkout",
                "count": 3,
            },
            {
                "time": "2026-05-30 10:30",
                "level": "ERROR",
                "service": "mailer",
                "message": "SMTP auth failed",
                "count": 28,
            },
            {
                "time": "2026-05-30 09:14",
                "level": "ERROR",
                "service": "cdn",
                "message": "Asset not found: /static/v2/logo.png",
                "count": 88,
            },
        ]
    )


@page.table("Critical Events", description="High-severity incidents in the last 7 days")
def critical_events() -> Table:
    return Table(
        data=[
            {
                "time": "2026-05-28 03:12",
                "service": "database",
                "event": "Primary replica went offline",
                "resolved": True,
                "duration": "8m 42s",
            },
            {
                "time": "2026-05-26 14:55",
                "service": "api",
                "event": "500 error rate exceeded 5%",
                "resolved": True,
                "duration": "3m 10s",
            },
            {
                "time": "2026-05-25 22:30",
                "service": "payment",
                "event": "Stripe webhook signature mismatch",
                "resolved": True,
                "duration": "12m 00s",
            },
        ]
    )


@page.table("Audit Log", description="Admin actions logged for compliance")
def audit_log() -> Table:
    return Table(
        data=[
            {"time": "2026-05-30 12:31", "admin": "superadmin", "action": "ban_user", "target": "spammer@example.com", "ip": "192.168.1.1"},
            {"time": "2026-05-30 11:18", "admin": "moderator1", "action": "delete_post", "target": "post#8821", "ip": "10.0.0.4"},
            {"time": "2026-05-30 10:05", "admin": "superadmin", "action": "update_settings", "target": "maintenance_mode", "ip": "192.168.1.1"},
            {"time": "2026-05-29 18:44", "admin": "moderator2", "action": "resolve_ticket", "target": "ticket#1034", "ip": "10.0.0.7"},
            {"time": "2026-05-29 15:22", "admin": "superadmin", "action": "create_admin", "target": "moderator3", "ip": "192.168.1.1"},
        ]
    )


@page.table("Errors by Service", description="Error count grouped by service this week")
def errors_by_service() -> Table:
    return Table(
        data=[
            {"service": "api", "errors": 84, "warnings": 410, "last_error": "2026-05-30 12:48"},
            {"service": "mailer", "errors": 32, "warnings": 90, "last_error": "2026-05-30 10:30"},
            {"service": "worker", "errors": 14, "warnings": 210, "last_error": "2026-05-30 12:21"},
            {"service": "cdn", "errors": 8, "warnings": 94, "last_error": "2026-05-30 09:14"},
            {"service": "payment", "errors": 4, "warnings": 26, "last_error": "2026-05-29 08:10"},
        ]
    )
