import asyncio
import random

from fastapi import HTTPException, Request

from openadmin import AdminPage, PaginationParamsDep, Stat, Table

from . import db

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
    return Stat(value=len(db.media_files))


@page.stat("Storage Used", description="Total storage consumed")
async def storage_used() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="1.84 TB")


@page.stat("Uploads Today", description="Files uploaded in the last 24 hours")
async def uploads_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for f in db.media_files.values() if f["date"] == "2026-05-30"))


@page.stat("Flagged Files", description="Files pending moderation review")
async def flagged_files_stat() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for f in db.media_files.values() if f["flag"]))


@page.action_delete("Delete file", description="Permanently remove a media file")
async def delete_file(id: int) -> None:
    if id not in db.media_files:
        raise HTTPException(status_code=404, detail="File not found")
    db.media_files.pop(id)


@page.action_post("Clear flag", description="Mark a flagged file as reviewed and safe")
async def clear_flag(id: int) -> None:
    if id not in db.media_files:
        raise HTTPException(status_code=404, detail="File not found")
    db.media_files[id]["flag"] = None


@page.table("Recent Uploads", description="Latest files uploaded by users")
async def recent_uploads(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(
        [f for f in db.media_files.values() if not f["flag"]],
        key=lambda f: f["date"],
        reverse=True,
    )
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "filename": f["filename"],
            "uploader": f["uploader"],
            "size": f["size"],
            "type": f["type"],
            "date": f["date"],
            "__actions__": [
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(delete_file.__name__)) + f"?id={f['id']}",
                }
            ],
        }
        for f in page_rows
    ])


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
async def flagged_files_list(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = [f for f in db.media_files.values() if f["flag"]]
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "filename": f["filename"],
            "uploader": f["uploader"],
            "flag": f["flag"],
            "date": f["date"],
            "__actions__": [
                {
                    "color": "success",
                    "method": "POST",
                    "url": str(req.url_for(clear_flag.__name__)) + f"?id={f['id']}",
                },
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(delete_file.__name__)) + f"?id={f['id']}",
                },
            ],
        }
        for f in page_rows
    ])


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
