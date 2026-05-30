import asyncio
import random

from fastapi import HTTPException, Request

from openadmin import AdminPage, PaginationParamsDep, Stat, Table

from . import db

page = AdminPage("Users")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# User Management

Manage accounts, monitor growth, and maintain community standards across the platform.

## Role Hierarchy

| Role | Scope | Count |
|---|---|---|
| `superadmin` | Full system access | 2 |
| `admin` | Manage users & content | 12 |
| `moderator` | Moderate posts & reports | 87 |
| `premium` | Paid plan features | 2,891 |
| `free` | Default registered user | 11,179 |

## Account Health

- **63.3%** of users are active in the last 30 days — a strong engagement signal
- **20.1%** are on a paid plan, the primary revenue-generating segment
- **1.48%** of accounts are currently banned; review periodically for false positives

> Before banning an account, always check for shared IPs or device fingerprints — a single bad actor may operate multiple accounts.

## New User Trend

47 users registered today. Maintain onboarding flow quality: a user who does not complete a key action in the first 48 hours is significantly less likely to convert to a paid plan.
"""


@page.stat("Total Users", description="Total number of registered users")
async def total_users() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=len(db.users))


@page.stat("Active Users", description="Users active in the last 30 days")
async def active_users() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for u in db.users.values() if u["active"]))


@page.stat("New Today", description="Users who registered today")
async def new_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for u in db.users.values() if u["registered"] == "2026-05-30"))


@page.stat("Premium Users", description="Users on a paid plan")
async def premium_users() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for u in db.users.values() if u["plan"] == "premium"))


@page.stat("Banned Users", description="Accounts currently suspended")
async def banned_users_stat() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=len(db.banned_users))


@page.action_delete(
    "Delete user", description="Delete user from database, no recovery !"
)
async def delete_user(id: int) -> None:
    if id not in db.users:
        raise HTTPException(status_code=404, detail="User not found")
    db.users.pop(id)


@page.action_post(
    "Ban user", description="Move user to banned list"
)
async def ban_user(id: int) -> None:
    if id not in db.users:
        raise HTTPException(status_code=404, detail="User not found")
    user = db.users.pop(id)
    ban_id = db.next_id("banned_users")
    db.banned_users[ban_id] = {
        "id": ban_id,
        "name": user["name"],
        "email": user["email"],
        "reason": "manual",
        "banned_on": "2026-05-30",
    }


@page.table("User List", description="All registered users")
async def user_list(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = []
    for user in db.users.values():
        rows.append({
            **user,
            "__actions__": [
                {
                    "color": "warning",
                    "method": "POST",
                    "url": str(req.url_for(ban_user.__name__)) + f"?id={user['id']}",
                },
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(delete_user.__name__)) + f"?id={user['id']}",
                },
            ],
        })
    start = pagination.page * pagination.per_page
    return Table(data=rows[start : start + pagination.per_page])


@page.table("Recent Signups", description="Users who registered in the last 7 days")
async def recent_signups(pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    recent = sorted(
        [u for u in db.users.values() if u["registered"] >= "2026-05-24"],
        key=lambda u: u["registered"],
        reverse=True,
    )
    rows = [
        {"id": u["id"], "name": u["name"], "email": u["email"], "registered": u["registered"]}
        for u in recent
    ]
    start = pagination.page * pagination.per_page
    return Table(data=rows[start : start + pagination.per_page])


@page.table("Top Users", description="Users with the most activity")
async def top_users() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"rank": 1, "name": "Alice Johnson", "posts": 342, "comments": 1204, "score": 9850},
            {"rank": 2, "name": "Eva Martinez", "posts": 289, "comments": 987, "score": 8420},
            {"rank": 3, "name": "Bob Smith", "posts": 201, "comments": 854, "score": 7130},
            {"rank": 4, "name": "Grace Kim", "posts": 178, "comments": 732, "score": 6540},
            {"rank": 5, "name": "Ivy Chen", "posts": 155, "comments": 609, "score": 5820},
        ]
    )


@page.table("Banned Users", description="Suspended accounts with reasons")
async def banned_user_list(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = list(db.banned_users.values())
    start = pagination.page * pagination.per_page
    return Table(data=rows[start : start + pagination.per_page])


@page.table("Role Distribution", description="Breakdown of users by assigned role")
async def role_distribution() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"role": "admin", "count": 12, "percentage": "0.08%"},
            {"role": "moderator", "count": 87, "percentage": "0.60%"},
            {"role": "premium", "count": 2891, "percentage": "20.10%"},
            {"role": "free", "count": 11179, "percentage": "77.73%"},
            {"role": "banned", "count": len(db.banned_users), "percentage": "1.48%"},
        ]
    )
