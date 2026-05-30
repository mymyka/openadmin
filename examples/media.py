from openadmin import AdminPage, Stat, Table

page = AdminPage("Media")


@page.stat("Total Files", description="All files stored across the platform")
def total_files() -> Stat:
    return Stat(value=284_120)


@page.stat("Storage Used", description="Total storage consumed")
def storage_used() -> Stat:
    return Stat(value="1.84 TB")


@page.stat("Uploads Today", description="Files uploaded in the last 24 hours")
def uploads_today() -> Stat:
    return Stat(value=1_840)


@page.stat("Flagged Files", description="Files pending moderation review")
def flagged_files() -> Stat:
    return Stat(value=14)


@page.table("Recent Uploads", description="Latest files uploaded by users")
def recent_uploads() -> Table:
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
def storage_by_type() -> Table:
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
def flagged_files_list() -> Table:
    return Table(
        data=[
            {"filename": "bad-content.mp4", "uploader": "troll@example.com", "flag": "policy-violation", "reported_by": "user#8820", "date": "2026-05-30"},
            {"filename": "spam-banner.jpg", "uploader": "spam@bot.io", "flag": "spam", "reported_by": "auto-scan", "date": "2026-05-29"},
            {"filename": "pirated-movie.mp4", "uploader": "pirate@ship.net", "flag": "copyright", "reported_by": "user#4410", "date": "2026-05-29"},
        ]
    )


@page.table("Top Uploaders", description="Users with the most storage consumed")
def top_uploaders() -> Table:
    return Table(
        data=[
            {"user": "videocreator@studio.com", "files": 4_210, "storage": "210 GB", "last_upload": "2026-05-30"},
            {"user": "media@agency.io", "files": 2_840, "storage": "148 GB", "last_upload": "2026-05-29"},
            {"user": "alice@example.com", "files": 1_120, "storage": "44 GB", "last_upload": "2026-05-30"},
            {"user": "content@corp.com", "files": 940, "storage": "38 GB", "last_upload": "2026-05-28"},
        ]
    )
