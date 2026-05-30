import asyncio
import random

from openadmin import AdminPage, Stat, Table

page = AdminPage("Permissions")


@page.stat("Total Roles", description="Defined roles in the system")
async def total_roles() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=8)


@page.stat("Admin Users", description="Users with admin-level access")
async def admin_users() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=14)


@page.stat("Pending Access Requests", description="Unreviewed role upgrade requests")
async def pending_requests() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=5)


@page.table("Role Overview", description="All system roles and their assigned user counts")
async def role_overview() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"role": "superadmin", "users": 2, "can_delete": True, "can_ban": True, "can_export": True},
            {"role": "admin", "users": 12, "can_delete": True, "can_ban": True, "can_export": True},
            {"role": "moderator", "users": 34, "can_delete": True, "can_ban": False, "can_export": False},
            {"role": "analyst", "users": 18, "can_delete": False, "can_ban": False, "can_export": True},
            {"role": "support", "users": 42, "can_delete": False, "can_ban": False, "can_export": False},
            {"role": "editor", "users": 210, "can_delete": False, "can_ban": False, "can_export": False},
            {"role": "member", "users": 13_940, "can_delete": False, "can_ban": False, "can_export": False},
            {"role": "guest", "users": 120, "can_delete": False, "can_ban": False, "can_export": False},
        ]
    )


@page.table("Admin Users", description="All users with admin-level privileges")
async def admin_users_list() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"user": "superadmin@platform.com", "role": "superadmin", "last_login": "2026-05-30", "mfa": True},
            {"user": "alice@platform.com", "role": "admin", "last_login": "2026-05-30", "mfa": True},
            {"user": "bob@platform.com", "role": "admin", "last_login": "2026-05-29", "mfa": True},
            {"user": "carol@platform.com", "role": "admin", "last_login": "2026-05-28", "mfa": False},
            {"user": "moderator1@platform.com", "role": "moderator", "last_login": "2026-05-30", "mfa": True},
        ]
    )


@page.table("Pending Access Requests", description="Users requesting elevated permissions")
async def pending_access_requests() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"user": "newmod@example.com", "current_role": "member", "requested_role": "moderator", "reason": "applying for mod team", "date": "2026-05-30"},
            {"user": "analyst@corp.com", "current_role": "member", "requested_role": "analyst", "reason": "data project access", "date": "2026-05-29"},
            {"user": "editor@agency.io", "current_role": "guest", "requested_role": "editor", "reason": "content contributor", "date": "2026-05-29"},
        ]
    )


@page.table("Recent Role Changes", description="Role assignments and revocations in the last 30 days")
async def recent_role_changes() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"user": "moderator3@platform.com", "change": "member → moderator", "changed_by": "superadmin", "date": "2026-05-29"},
            {"user": "former_mod@example.com", "change": "moderator → member", "changed_by": "superadmin", "date": "2026-05-25"},
            {"user": "analyst2@corp.com", "change": "member → analyst", "changed_by": "alice@platform.com", "date": "2026-05-22"},
            {"user": "spammer@example.com", "change": "member → banned", "changed_by": "moderator1@platform.com", "date": "2026-05-20"},
        ]
    )
