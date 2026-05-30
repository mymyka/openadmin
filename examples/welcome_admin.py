import asyncio
import random

from openadmin import AdminPage, Stat, Table

page = AdminPage("Welcome to admin")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# Welcome to the Admin Panel

Use this panel to monitor platform health, review recent activity, and manage your system.

## Quick Links
- **Users** — manage accounts, roles, and bans
- **Posts** — moderate content and track engagement
- **Tasks** — monitor user task completion across the platform

> All times are shown in UTC.
"""


@page.stat("Total Users", description="All registered users on the platform")
async def total_users() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=14_382)


@page.stat("Active Sessions", description="Users currently logged in")
async def active_sessions() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=203)


@page.stat("Open Issues", description="Unresolved support tickets")
async def open_issues() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=17)


@page.stat("Server Uptime", description="System uptime since last restart")
async def server_uptime() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="14d 6h 42m")


@page.table("Recent Activity", description="Latest admin actions across the panel")
async def recent_activity() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "time": "2026-05-30 12:31",
                "admin": "superadmin",
                "action": "Banned user #500",
                "target": "bot@scraper.io",
            },
            {
                "time": "2026-05-30 11:18",
                "admin": "moderator1",
                "action": "Deleted post #8821",
                "target": "spam content",
            },
            {
                "time": "2026-05-30 10:05",
                "admin": "superadmin",
                "action": "Updated site settings",
                "target": "maintenance_mode=false",
            },
            {
                "time": "2026-05-29 18:44",
                "admin": "moderator2",
                "action": "Resolved ticket #1034",
                "target": "billing issue",
            },
            {
                "time": "2026-05-29 15:22",
                "admin": "superadmin",
                "action": "Created new admin account",
                "target": "moderator3",
            },
        ]
    )


@page.table("System Health", description="Key service status indicators")
async def system_health() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "service": "API",
                "status": "healthy",
                "latency_ms": 42,
                "uptime": "99.98%",
            },
            {
                "service": "Database",
                "status": "healthy",
                "latency_ms": 8,
                "uptime": "99.99%",
            },
            {
                "service": "Cache",
                "status": "healthy",
                "latency_ms": 1,
                "uptime": "100%",
            },
            {
                "service": "Email",
                "status": "degraded",
                "latency_ms": 1820,
                "uptime": "97.40%",
            },
            {
                "service": "Storage",
                "status": "healthy",
                "latency_ms": 15,
                "uptime": "99.95%",
            },
        ]
    )
