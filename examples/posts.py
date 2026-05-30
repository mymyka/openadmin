import asyncio
import random

from openadmin import AdminPage, Stat, Table

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
    return Stat(value=58_741)


@page.stat("Published", description="Posts currently live")
async def published_posts() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=51_209)


@page.stat("Drafts", description="Posts saved but not published")
async def draft_posts() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=5_318)


@page.stat("Total Views", description="Cumulative views across all posts")
async def total_views() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=4_820_113)


@page.stat("Avg Views per Post", description="Mean views across published posts")
async def avg_views() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=94.1)


@page.table("Recent Posts", description="Latest published posts")
async def recent_posts() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "id": 58741,
                "title": "Getting Started with FastAPI",
                "author": "Alice Johnson",
                "views": 1204,
                "published": "2026-05-30",
            },
            {
                "id": 58740,
                "title": "10 Tips for Better Python Code",
                "author": "Bob Smith",
                "views": 876,
                "published": "2026-05-29",
            },
            {
                "id": 58739,
                "title": "Why Open Source Matters",
                "author": "Eva Martinez",
                "views": 654,
                "published": "2026-05-29",
            },
            {
                "id": 58738,
                "title": "Building Admin Panels Fast",
                "author": "Alice Johnson",
                "views": 3201,
                "published": "2026-05-28",
            },
            {
                "id": 58737,
                "title": "Async Python Deep Dive",
                "author": "Grace Kim",
                "views": 987,
                "published": "2026-05-27",
            },
        ]
    )


@page.table("Top Posts", description="Most viewed posts of all time")
async def top_posts() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "rank": 1,
                "title": "The Ultimate Python Guide",
                "author": "Alice Johnson",
                "views": 98_432,
                "category": "tutorial",
            },
            {
                "rank": 2,
                "title": "FastAPI vs Flask: Full Comparison",
                "author": "Bob Smith",
                "views": 74_211,
                "category": "comparison",
            },
            {
                "rank": 3,
                "title": "Docker for Beginners",
                "author": "Carol White",
                "views": 61_887,
                "category": "devops",
            },
            {
                "rank": 4,
                "title": "Building REST APIs in Python",
                "author": "Eva Martinez",
                "views": 54_320,
                "category": "tutorial",
            },
            {
                "rank": 5,
                "title": "Understanding Async/Await",
                "author": "Grace Kim",
                "views": 48_109,
                "category": "python",
            },
        ]
    )


@page.table("Posts by Category", description="Post count grouped by category")
async def posts_by_category() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "category": "tutorial",
                "count": 18420,
                "total_views": 1_820_340,
                "avg_views": 98.8,
            },
            {
                "category": "news",
                "count": 12301,
                "total_views": 980_102,
                "avg_views": 79.7,
            },
            {
                "category": "opinion",
                "count": 9874,
                "total_views": 742_800,
                "avg_views": 75.2,
            },
            {
                "category": "devops",
                "count": 7643,
                "total_views": 620_441,
                "avg_views": 81.2,
            },
            {
                "category": "comparison",
                "count": 3971,
                "total_views": 656_430,
                "avg_views": 165.3,
            },
        ]
    )


@page.table("Pending Review", description="Posts awaiting moderation approval")
async def pending_review() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "id": 58742,
                "title": "My Controversial Take on AI",
                "author": "Hank Davis",
                "submitted": "2026-05-30",
                "flag": "ai-content",
            },
            {
                "id": 58743,
                "title": "Crypto Will Rule the World",
                "author": "Jake Wilson",
                "submitted": "2026-05-30",
                "flag": "misinformation",
            },
            {
                "id": 58744,
                "title": "Anonymous Post #1",
                "author": "Unknown User",
                "submitted": "2026-05-29",
                "flag": "spam",
            },
            {
                "id": 58745,
                "title": "Review: Product X",
                "author": "Ivy Chen",
                "submitted": "2026-05-29",
                "flag": "promotional",
            },
            {
                "id": 58746,
                "title": "How to Hack Anything",
                "author": "Bad Actor",
                "submitted": "2026-05-28",
                "flag": "policy-violation",
            },
        ]
    )


@page.table("Deleted Posts", description="Recently deleted posts with removal reason")
async def deleted_posts() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "id": 58200,
                "title": "Old Announcement",
                "author": "Admin",
                "deleted_on": "2026-05-25",
                "reason": "outdated",
            },
            {
                "id": 57940,
                "title": "Spam Link Farm",
                "author": "Spam Bot 1",
                "deleted_on": "2026-05-22",
                "reason": "spam",
            },
            {
                "id": 57801,
                "title": "Duplicate Tutorial",
                "author": "Bob Smith",
                "deleted_on": "2026-05-20",
                "reason": "duplicate",
            },
            {
                "id": 57654,
                "title": "Hate Speech Post",
                "author": "Troll Account",
                "deleted_on": "2026-05-18",
                "reason": "policy-violation",
            },
            {
                "id": 57500,
                "title": "Test Post 999",
                "author": "Dev Team",
                "deleted_on": "2026-05-15",
                "reason": "test-content",
            },
        ]
    )
