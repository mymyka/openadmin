import asyncio
import random

from openadmin import AdminPage, Stat, Table

page = AdminPage("Media")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# Media Storage

Manage uploaded files, monitor storage consumption, and review flagged content.

## Storage Breakdown

| Type | Files | Size | Share |
|---|---|---|---|
| Video | 8,420 | 1.12 TB | 60.9% |
| Image | 198,400 | 0.48 TB | 26.1% |
| Document | 64,100 | 0.18 TB | 9.8% |
| Audio | 12,800 | 0.04 TB | 2.2% |
| Other | 400 | 0.02 TB | 1.1% |

**Video dominates storage** despite accounting for fewer than 3% of total files. Per-user video upload limits are the most effective lever for controlling storage growth.

## Storage Capacity

Currently using **1.84 TB of an estimated 10 TB provisioned limit**. At the current upload rate of ~1,840 files/day, the platform has approximately **8–12 months** of headroom before requiring expansion.

> Files uploaded through the API bypass client-side size limits. Monitor the top uploaders table for users who may be exploiting this — `videocreator@studio.com` alone holds 210 GB.

## Content Moderation

14 files are pending review. Flagged files are held from public access until cleared or removed:

- `policy-violation` — manual admin decision required
- `copyright` — forward to legal team before acting
- `spam` — safe to delete immediately after auto-scan confirmation

## Accepted File Types

```
Images:    .jpg  .jpeg  .png  .gif  .webp  .svg
Video:     .mp4  .webm  .mov
Audio:     .mp3  .wav  .ogg
Documents: .pdf  .docx  .xlsx  .csv  .txt
```

Files outside these types are rejected at upload time.
"""


@page.stat("Total Files", description="All files stored across the platform")
async def total_files() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=284_120)


@page.stat("Storage Used", description="Total storage consumed")
async def storage_used() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="1.84 TB")


@page.stat("Uploads Today", description="Files uploaded in the last 24 hours")
async def uploads_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=1_840)


@page.stat("Flagged Files", description="Files pending moderation review")
async def flagged_files() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=14)


@page.table("Recent Uploads", description="Latest files uploaded by users")
async def recent_uploads() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"filename": "product-hero.png", "uploader": "alice@example.com", "size": "2.4 MB", "type": "image/png", "date": "2026-05-30"},
            {"filename": "q2-report.pdf", "uploader": "bob@corp.com", "size": "1.1 MB", "type": "application/pdf", "date": "2026-05-30"},
            {"filename": "demo-video.mp4", "uploader": "carol@startup.io", "size": "84.2 MB", "type": "video/mp4", "date": "2026-05-30"},
            {"filename": "avatar-update.jpg", "uploader": "dan@example.net", "size": "0.3 MB", "type": "image/jpeg", "date": "2026-05-30"},
            {"filename": "data-export.csv", "uploader": "eva@lab.dev", "size": "5.6 MB", "type": "text/csv", "date": "2026-05-29"},
        ]
    )


@page.table("Storage by File Type", description="Disk usage breakdown by media type")
async def storage_by_type() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"type": "video", "files": 8_420, "total_size": "1.12 TB", "share": "60.9%"},
            {"type": "image", "files": 198_400, "total_size": "0.48 TB", "share": "26.1%"},
            {"type": "document", "files": 64_100, "total_size": "0.18 TB", "share": "9.8%"},
            {"type": "audio", "files": 12_800, "total_size": "0.04 TB", "share": "2.2%"},
            {"type": "other", "files": 400, "total_size": "0.02 TB", "share": "1.1%"},
        ]
    )


@page.table("Flagged Files", description="Files reported or auto-flagged for review")
async def flagged_files_list() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"filename": "bad-content.mp4", "uploader": "troll@example.com", "flag": "policy-violation", "reported_by": "user#8820", "date": "2026-05-30"},
            {"filename": "spam-banner.jpg", "uploader": "spam@bot.io", "flag": "spam", "reported_by": "auto-scan", "date": "2026-05-29"},
            {"filename": "pirated-movie.mp4", "uploader": "pirate@ship.net", "flag": "copyright", "reported_by": "user#4410", "date": "2026-05-29"},
        ]
    )


@page.table("Top Uploaders", description="Users with the most storage consumed")
async def top_uploaders() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"user": "videocreator@studio.com", "files": 4_210, "storage": "210 GB", "last_upload": "2026-05-30"},
            {"user": "media@agency.io", "files": 2_840, "storage": "148 GB", "last_upload": "2026-05-29"},
            {"user": "alice@example.com", "files": 1_120, "storage": "44 GB", "last_upload": "2026-05-30"},
            {"user": "content@corp.com", "files": 940, "storage": "38 GB", "last_upload": "2026-05-28"},
        ]
    )
