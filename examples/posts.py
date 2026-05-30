import asyncio
import random

from fastapi import HTTPException, Request

from openadmin import AdminPage, PaginationParamsDep, Stat, Table

from . import db

page = AdminPage("Posts")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# Content Management

Review post performance, manage moderation queues, and track publishing activity across the platform.

## Post Status Summary

| Status | Count | Notes |
|---|---|---|
| Published | 51,209 | Live and publicly visible |
| Draft | 5,318 | Not yet submitted for review |
| Pending Review | 3 | Awaiting moderation decision |
| Deleted | — | Soft-deleted; recoverable for 30 days |

## Category Performance

`comparison` posts drive the highest average views (165.3) despite having fewer total posts. This signals strong reader intent — comparison content is actively searched for.

> The `tutorial` category accounts for the most total views (1.82M), but its per-post average (98.8) is lower than `comparison` (165.3). Consider cross-linking tutorial content to comparison posts to lift average engagement.

## Moderation Queue

**5 posts are pending review.** Posts are held when they match one or more auto-flag criteria:

- `ai-content` — generated or heavily AI-assisted text detected
- `misinformation` — claims flagged by automated fact-check signals
- `spam` — bulk or duplicate submission patterns
- `promotional` — undisclosed commercial content
- `policy-violation` — explicit, harmful, or illegal content

> `policy-violation` posts must be reviewed within **2 hours** of flagging. All other categories have a 24-hour SLA.

## Top Authors

**Alice Johnson** is the platform's most prolific author (342 posts) and also appears as the author of the highest single-post view count (3,201 views for "Building Admin Panels Fast"). High-volume authors in good standing may be eligible for a `verified` badge.
"""


@page.stat("Total Posts", description="All posts ever created")
async def total_posts() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=len(db.posts) + len(db.pending_posts) + len(db.deleted_posts))


@page.stat("Published", description="Posts currently live")
async def published_posts() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=len(db.posts))


@page.stat("Drafts", description="Posts saved but not published")
async def draft_posts() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=5_318)


@page.stat("Total Views", description="Cumulative views across all posts")
async def total_views() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(p["views"] for p in db.posts.values()))


@page.stat("Avg Views per Post", description="Mean views across published posts")
async def avg_views() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    count = len(db.posts)
    avg = round(sum(p["views"] for p in db.posts.values()) / count, 1) if count else 0
    return Stat(value=avg)


@page.action_delete("Delete post", description="Permanently remove a published post")
async def delete_post(id: int) -> None:
    if id not in db.posts:
        raise HTTPException(status_code=404, detail="Post not found")
    post = db.posts.pop(id)
    db.deleted_posts[id] = {**post, "deleted_on": "2026-05-30", "reason": "manual"}


@page.action_delete("Reject pending post", description="Reject and soft-delete a pending post")
async def reject_post(id: int) -> None:
    if id not in db.pending_posts:
        raise HTTPException(status_code=404, detail="Pending post not found")
    post = db.pending_posts.pop(id)
    db.deleted_posts[id] = {**post, "deleted_on": "2026-05-30", "reason": post.get("flag", "rejected")}


@page.action_post("Approve pending post", description="Publish a post from the moderation queue")
async def approve_post(id: int) -> None:
    if id not in db.pending_posts:
        raise HTTPException(status_code=404, detail="Pending post not found")
    post = db.pending_posts.pop(id)
    db.posts[id] = {
        "id": post["id"],
        "title": post["title"],
        "author": post["author"],
        "views": 0,
        "category": "uncategorized",
        "status": "published",
        "published": "2026-05-30",
    }


@page.table("Recent Posts", description="Latest published posts")
async def recent_posts(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(db.posts.values(), key=lambda p: p["published"], reverse=True)
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "id": p["id"],
            "title": p["title"],
            "author": p["author"],
            "views": p["views"],
            "published": p["published"],
            "__actions__": [
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(delete_post.__name__)) + f"?id={p['id']}",
                }
            ],
        }
        for p in page_rows
    ])


@page.table("Top Posts", description="Most viewed posts of all time")
async def top_posts(pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(db.posts.values(), key=lambda p: p["views"], reverse=True)
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {"rank": start + i + 1, "title": p["title"], "author": p["author"], "views": p["views"], "category": p["category"]}
        for i, p in enumerate(page_rows)
    ])


@page.table("Posts by Category", description="Post count grouped by category")
async def posts_by_category() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"category": "tutorial", "count": 18420, "total_views": 1_820_340, "avg_views": 98.8},
            {"category": "news", "count": 12301, "total_views": 980_102, "avg_views": 79.7},
            {"category": "opinion", "count": 9874, "total_views": 742_800, "avg_views": 75.2},
            {"category": "devops", "count": 7643, "total_views": 620_441, "avg_views": 81.2},
            {"category": "comparison", "count": 3971, "total_views": 656_430, "avg_views": 165.3},
        ]
    )


@page.table("Pending Review", description="Posts awaiting moderation approval")
async def pending_review(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = list(db.pending_posts.values())
    start = pagination.page * pagination.per_page
    return Table(data=[
        {
            **p,
            "__actions__": [
                {
                    "color": "success",
                    "method": "POST",
                    "url": str(req.url_for(approve_post.__name__)) + f"?id={p['id']}",
                },
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(reject_post.__name__)) + f"?id={p['id']}",
                },
            ],
        }
        for p in rows[start : start + pagination.per_page]
    ])


@page.table("Deleted Posts", description="Recently deleted posts with removal reason")
async def deleted_posts_list(pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = list(db.deleted_posts.values())
    start = pagination.page * pagination.per_page
    return Table(data=rows[start : start + pagination.per_page])
