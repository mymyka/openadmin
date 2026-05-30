import random

from fastapi import HTTPException, Request

from openadmin import AdminPage, PaginationParamsDep, Stat, Table

from . import db

_AVATARS = [f"/static/avatars/avatar_{i}.svg" for i in range(1, 9)]

page = AdminPage("Users")


@page.stat("Total Users", description="Total number of registered users")
async def total_users() -> Stat:
    return Stat(value=await db.count("users"))


@page.stat("Active Users", description="Users active in the last 30 days")
async def active_users() -> Stat:
    return Stat(value=await db.count("users", "active = 1"))


@page.stat("New Today", description="Users who registered today")
async def new_today() -> Stat:
    return Stat(value=await db.count("users", "registered = '2026-05-30'"))


@page.stat("Premium Users", description="Users on a paid plan")
async def premium_users() -> Stat:
    return Stat(value=await db.count("users", "plan = 'premium'"))


@page.stat("Banned Users", description="Accounts currently suspended")
async def banned_users_stat() -> Stat:
    return Stat(value=await db.count("banned_users"))


@page.action_delete(
    "Delete user", description="Delete user from database, no recovery !"
)
async def delete_user(id: int) -> None:
    row = await db.fetchone("SELECT id FROM users WHERE id = ?", (id,))
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    await db.execute("DELETE FROM users WHERE id = ?", (id,))


@page.action_patch("Delete document", description="Remove the document attached to a user")
async def delete_document(id: int) -> None:
    row = await db.fetchone("SELECT id FROM users WHERE id = ?", (id,))
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    await db.execute("UPDATE users SET document = NULL WHERE id = ?", (id,))


@page.action_post("Refresh avatar", description="Assign a new random avatar to a user")
async def refresh_avatar(id: int) -> None:
    row = await db.fetchone("SELECT avatar FROM users WHERE id = ?", (id,))
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    current = row.get("avatar")
    choices = [a for a in _AVATARS if a != current] or _AVATARS
    await db.execute("UPDATE users SET avatar = ? WHERE id = ?", (random.choice(choices), id))


@page.action_post("Ban user", description="Move user to banned list")
async def ban_user(id: int) -> None:
    user = await db.fetchone("SELECT * FROM users WHERE id = ?", (id,))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await db.execute("DELETE FROM users WHERE id = ?", (id,))
    await db.execute(
        "INSERT INTO banned_users (name, email, reason, banned_on) VALUES (?,?,?,?)",
        (user["name"], user["email"], "manual", "2026-05-30"),
    )


@page.table("User List", description="All registered users")
async def user_list(req: Request, pagination: PaginationParamsDep) -> Table:
    offset = pagination.page * pagination.per_page
    rows = await db.fetchall(
        "SELECT id, name, email, plan, active, role, registered, document, avatar FROM users ORDER BY id LIMIT ? OFFSET ?",
        (pagination.per_page, offset),
    )
    total = await db.count("users")
    base_url = str(req.base_url).rstrip("/")
    for row in rows:
        row["active"] = bool(row["active"])
        if row["document"]:
            row["document"] = f"{base_url}{row['document']}"
        if row["avatar"]:
            row["avatar"] = f"{base_url}{row['avatar']}"
        row["__actions__"] = [
            {
                "color": "secondary",
                "method": "PATCH",
                "url": str(req.url_for(delete_document.__name__)) + f"?id={row['id']}",
            },
            {
                "color": "info",
                "method": "POST",
                "url": str(req.url_for(refresh_avatar.__name__)) + f"?id={row['id']}",
            },
            {
                "color": "warning",
                "method": "POST",
                "url": str(req.url_for(ban_user.__name__)) + f"?id={row['id']}",
            },
            {
                "color": "danger",
                "method": "DELETE",
                "url": str(req.url_for(delete_user.__name__)) + f"?id={row['id']}",
            },
        ]
    return Table(data=rows)


@page.table("Recent Signups", description="Users who registered in the last 7 days")
async def recent_signups(pagination: PaginationParamsDep) -> Table:
    offset = pagination.page * pagination.per_page
    rows = await db.fetchall(
        "SELECT id, name, email, registered FROM users "
        "WHERE registered >= '2026-05-24' ORDER BY registered DESC LIMIT ? OFFSET ?",
        (pagination.per_page, offset),
    )
    return Table(data=rows)


@page.table("Top Users", description="Users with the most activity")
async def top_users() -> Table:
    return Table(
        data=[
            {
                "rank": 1,
                "name": "Alice Johnson",
                "posts": 342,
                "comments": 1204,
                "score": 9850,
            },
            {
                "rank": 2,
                "name": "Eva Martinez",
                "posts": 289,
                "comments": 987,
                "score": 8420,
            },
            {
                "rank": 3,
                "name": "Bob Smith",
                "posts": 201,
                "comments": 854,
                "score": 7130,
            },
            {
                "rank": 4,
                "name": "Grace Kim",
                "posts": 178,
                "comments": 732,
                "score": 6540,
            },
            {
                "rank": 5,
                "name": "Ivy Chen",
                "posts": 155,
                "comments": 609,
                "score": 5820,
            },
        ]
    )


@page.table("Banned Users", description="Suspended accounts with reasons")
async def banned_user_list(req: Request, pagination: PaginationParamsDep) -> Table:
    offset = pagination.page * pagination.per_page
    rows = await db.fetchall(
        "SELECT * FROM banned_users ORDER BY id LIMIT ? OFFSET ?",
        (pagination.per_page, offset),
    )
    return Table(data=rows)


@page.table("Role Distribution", description="Breakdown of users by assigned role")
async def role_distribution() -> Table:
    rows = await db.fetchall(
        "SELECT role, COUNT(*) AS count FROM users GROUP BY role ORDER BY count DESC"
    )
    total = await db.count("users")
    for row in rows:
        row["percentage"] = f"{row['count'] / total * 100:.2f}%" if total else "0%"
    banned_count = await db.count("banned_users")
    rows.append(
        {
            "role": "banned",
            "count": banned_count,
            "percentage": f"{banned_count / (total + banned_count) * 100:.2f}%"
            if total
            else "0%",
        }
    )
    return Table(data=rows)
