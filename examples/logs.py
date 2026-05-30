import asyncio
import random

from openadmin import AdminPage, Stat, Table

page = AdminPage("Logs")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# Log Monitoring

Track application errors, system events, and admin actions for debugging and compliance.

## Log Severity Levels

| Level | Meaning | Response |
|---|---|---|
| `CRITICAL` | Service-threatening incident | Immediate page, incident opened |
| `ERROR` | Request or job failed | Investigate within 1 hour |
| `WARN` | Degraded behaviour, not failing | Review daily |
| `INFO` | Normal operational events | Retained for 30 days |
| `DEBUG` | Verbose trace data | Development only, not in production |

## Current Status

There are **3 critical events** in the last 7 days — all resolved. The highest-error service is `api` (84 errors this week), followed by `mailer` (32 errors), where SMTP auth failures indicate a likely credential rotation issue.

> SMTP auth failures (`mailer` service) have been recurring since 2026-05-30 10:30. If the mail provider credentials were recently rotated, update the secret in the environment configuration and redeploy the mailer service.

## Audit Log

All admin actions are captured in the audit log for compliance purposes:

- Entries are **immutable** — they cannot be deleted through the admin panel
- Retention policy: **12 months** for audit events, **30 days** for application logs
- Audit log access is restricted to `admin` and `superadmin` roles

## Log Volume

Today's ingestion is **4.2M lines**. Alerts fire if ingest drops below 500K (possible pipeline failure) or exceeds 20M (potential log flood from a runaway process).
"""


@page.stat("Errors Today", description="Application errors logged in the last 24 hours")
async def errors_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=142)


@page.stat("Warnings Today", description="Warning-level log events today")
async def warnings_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=830)


@page.stat("Critical Alerts", description="Critical-severity events in the last 7 days")
async def critical_alerts() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=3)


@page.stat("Log Volume (24h)", description="Total log lines ingested today")
async def log_volume() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="4.2M")


@page.table("Recent Errors", description="Latest application errors")
async def recent_errors() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
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
async def critical_events() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
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
async def audit_log() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
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
async def errors_by_service() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"service": "api", "errors": 84, "warnings": 410, "last_error": "2026-05-30 12:48"},
            {"service": "mailer", "errors": 32, "warnings": 90, "last_error": "2026-05-30 10:30"},
            {"service": "worker", "errors": 14, "warnings": 210, "last_error": "2026-05-30 12:21"},
            {"service": "cdn", "errors": 8, "warnings": 94, "last_error": "2026-05-30 09:14"},
            {"service": "payment", "errors": 4, "warnings": 26, "last_error": "2026-05-29 08:10"},
        ]
    )
