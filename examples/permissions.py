import asyncio
import random

from fastapi import HTTPException, Request

from openadmin import AdminPage, PaginationParamsDep, Stat, Table

from . import db

page = AdminPage("Permissions")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# Access Control & Permissions

Manage roles, review privilege grants, and ensure least-privilege access across the platform.

## Role Capability Matrix

| Role | Delete Content | Ban Users | Export Data | User Count |
|---|---|---|---|---|
| `superadmin` | Yes | Yes | Yes | 2 |
| `admin` | Yes | Yes | Yes | 12 |
| `moderator` | Yes | No | No | 34 |
| `analyst` | No | No | Yes | 18 |
| `support` | No | No | No | 42 |
| `editor` | No | No | No | 210 |
| `member` | No | No | No | 13,940 |
| `guest` | No | No | No | 120 |

## Security Policies

- **MFA is mandatory** for all `admin` and `superadmin` accounts
- Any admin without MFA enabled (`carol@platform.com`) must be remediated within 24 hours
- Role upgrades require approval from an existing `admin` or `superadmin`

> The principle of least privilege applies: grant the minimum role necessary for the task. A content contributor needs `editor`, not `admin`, even if they ask for broader access.

## Access Requests

There are **5 pending requests** to review. All requests older than 3 days without a decision should be escalated — prolonged uncertainty degrades the user's onboarding experience.

## Audit Trail

All role changes are logged with the granting admin's identity and timestamp. Role revocations are also captured — see the Recent Role Changes table for the full history.
"""


@page.stat("Total Roles", description="Defined roles in the system")
async def total_roles() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=len(db.roles))


@page.stat("Admin Users", description="Users with admin-level access")
async def admin_users() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=db.roles.get("admin", {}).get("users", 0) + db.roles.get("superadmin", {}).get("users", 0))


@page.stat("Pending Access Requests", description="Unreviewed role upgrade requests")
async def pending_requests() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=len(db.role_requests))


@page.action_post("Approve request", description="Grant the requested role to the user")
async def approve_request(id: int) -> None:
    if id not in db.role_requests:
        raise HTTPException(status_code=404, detail="Request not found")
    req = db.role_requests.pop(id)
    change_id = db.next_id("role_changes")
    db.role_changes[change_id] = {
        "id": change_id,
        "user": req["user"],
        "change": f"{req['current_role']} → {req['requested_role']}",
        "changed_by": "admin",
        "date": "2026-05-30",
    }


@page.action_delete("Deny request", description="Reject a role upgrade request")
async def deny_request(id: int) -> None:
    if id not in db.role_requests:
        raise HTTPException(status_code=404, detail="Request not found")
    db.role_requests.pop(id)


@page.table(
    "Role Overview", description="All system roles and their assigned user counts"
)
async def role_overview() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(data=list(db.roles.values()))


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


@page.table(
    "Pending Access Requests", description="Users requesting elevated permissions"
)
async def pending_access_requests(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = list(db.role_requests.values())
    start = pagination.page * pagination.per_page
    return Table(data=[
        {
            "user": r["user"],
            "current_role": r["current_role"],
            "requested_role": r["requested_role"],
            "reason": r["reason"],
            "date": r["date"],
            "__actions__": [
                {
                    "color": "success",
                    "method": "POST",
                    "url": str(req.url_for(approve_request.__name__)) + f"?id={r['id']}",
                },
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(deny_request.__name__)) + f"?id={r['id']}",
                },
            ],
        }
        for r in rows[start : start + pagination.per_page]
    ])


@page.table(
    "Recent Role Changes",
    description="Role assignments and revocations in the last 30 days",
)
async def recent_role_changes(pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(db.role_changes.values(), key=lambda c: c["date"], reverse=True)
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "user": c["user"],
            "change": c["change"],
            "changed_by": c["changed_by"],
            "date": c["date"],
        }
        for c in page_rows
    ])
