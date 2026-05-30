"""
In-memory dictionary database for examples.
All data persists for the server lifetime — CRUD actions modify these dicts
and every subsequent table read reflects the current state.
"""

# ── Counter helper ─────────────────────────────────────────────────────────────

_counters: dict[str, int] = {}


def next_id(table: str) -> int:
    _counters[table] = _counters.get(table, 0) + 1
    return _counters[table]


# ── Users ──────────────────────────────────────────────────────────────────────

users: dict[int, dict] = {
    1: {"id": 1, "name": "Alice Johnson", "email": "alice@example.com", "plan": "premium", "active": True, "role": "moderator", "registered": "2026-05-01"},
    2: {"id": 2, "name": "Bob Smith", "email": "bob@example.com", "plan": "free", "active": True, "role": "free", "registered": "2026-05-03"},
    3: {"id": 3, "name": "Carol White", "email": "carol@example.com", "plan": "premium", "active": False, "role": "premium", "registered": "2026-04-15"},
    4: {"id": 4, "name": "David Brown", "email": "david@example.com", "plan": "free", "active": True, "role": "free", "registered": "2026-04-20"},
    5: {"id": 5, "name": "Eva Martinez", "email": "eva@example.com", "plan": "premium", "active": True, "role": "premium", "registered": "2026-03-10"},
    14378: {"id": 14378, "name": "Jake Wilson", "email": "jake@example.com", "plan": "free", "active": True, "role": "free", "registered": "2026-05-27"},
    14379: {"id": 14379, "name": "Ivy Chen", "email": "ivy@example.com", "plan": "free", "active": True, "role": "free", "registered": "2026-05-28"},
    14380: {"id": 14380, "name": "Hank Davis", "email": "hank@example.com", "plan": "free", "active": True, "role": "free", "registered": "2026-05-29"},
    14381: {"id": 14381, "name": "Grace Kim", "email": "grace@example.com", "plan": "premium", "active": True, "role": "premium", "registered": "2026-05-29"},
    14382: {"id": 14382, "name": "Frank Lee", "email": "frank@example.com", "plan": "free", "active": True, "role": "free", "registered": "2026-05-30"},
}

_counters["users"] = 14382

banned_users: dict[int, dict] = {
    101: {"id": 101, "name": "Spam Bot 1", "email": "spam1@evil.com", "reason": "spam", "banned_on": "2026-05-10"},
    245: {"id": 245, "name": "Troll Account", "email": "troll@bad.com", "reason": "harassment", "banned_on": "2026-05-15"},
    389: {"id": 389, "name": "Fake User", "email": "fake@nowhere.com", "reason": "impersonation", "banned_on": "2026-05-20"},
    412: {"id": 412, "name": "Abuser X", "email": "abuse@dark.com", "reason": "abuse", "banned_on": "2026-05-22"},
    500: {"id": 500, "name": "Bot Account", "email": "bot@scraper.io", "reason": "scraping", "banned_on": "2026-05-28"},
}

_counters["banned_users"] = 500

# ── Posts ──────────────────────────────────────────────────────────────────────

posts: dict[int, dict] = {
    58737: {"id": 58737, "title": "Async Python Deep Dive", "author": "Grace Kim", "views": 987, "category": "python", "status": "published", "published": "2026-05-27"},
    58738: {"id": 58738, "title": "Building Admin Panels Fast", "author": "Alice Johnson", "views": 3201, "category": "tutorial", "status": "published", "published": "2026-05-28"},
    58739: {"id": 58739, "title": "Why Open Source Matters", "author": "Eva Martinez", "views": 654, "category": "opinion", "status": "published", "published": "2026-05-29"},
    58740: {"id": 58740, "title": "10 Tips for Better Python Code", "author": "Bob Smith", "views": 876, "category": "tutorial", "status": "published", "published": "2026-05-29"},
    58741: {"id": 58741, "title": "Getting Started with FastAPI", "author": "Alice Johnson", "views": 1204, "category": "tutorial", "status": "published", "published": "2026-05-30"},
}

pending_posts: dict[int, dict] = {
    58742: {"id": 58742, "title": "My Controversial Take on AI", "author": "Hank Davis", "submitted": "2026-05-30", "flag": "ai-content"},
    58743: {"id": 58743, "title": "Crypto Will Rule the World", "author": "Jake Wilson", "submitted": "2026-05-30", "flag": "misinformation"},
    58744: {"id": 58744, "title": "Anonymous Post #1", "author": "Unknown User", "submitted": "2026-05-29", "flag": "spam"},
    58745: {"id": 58745, "title": "Review: Product X", "author": "Ivy Chen", "submitted": "2026-05-29", "flag": "promotional"},
    58746: {"id": 58746, "title": "How to Hack Anything", "author": "Bad Actor", "submitted": "2026-05-28", "flag": "policy-violation"},
}

deleted_posts: dict[int, dict] = {
    57500: {"id": 57500, "title": "Test Post 999", "author": "Dev Team", "deleted_on": "2026-05-15", "reason": "test-content"},
    57654: {"id": 57654, "title": "Hate Speech Post", "author": "Troll Account", "deleted_on": "2026-05-18", "reason": "policy-violation"},
    57801: {"id": 57801, "title": "Duplicate Tutorial", "author": "Bob Smith", "deleted_on": "2026-05-20", "reason": "duplicate"},
    57940: {"id": 57940, "title": "Spam Link Farm", "author": "Spam Bot 1", "deleted_on": "2026-05-22", "reason": "spam"},
    58200: {"id": 58200, "title": "Old Announcement", "author": "Admin", "deleted_on": "2026-05-25", "reason": "outdated"},
}

_counters["posts"] = 58741

# ── Orders ─────────────────────────────────────────────────────────────────────

orders: dict[int, dict] = {
    9897: {"id": 9897, "order_id": "#ORD-9897", "customer": "Eva Martinez", "total": "$55.00", "status": "shipped", "date": "2026-05-29", "flag": None},
    9898: {"id": 9898, "order_id": "#ORD-9898", "customer": "Dan Brown", "total": "$214.00", "status": "pending", "date": "2026-05-29", "flag": None},
    9899: {"id": 9899, "order_id": "#ORD-9899", "customer": "Carol White", "total": "$31.99", "status": "delivered", "date": "2026-05-30", "flag": None},
    9900: {"id": 9900, "order_id": "#ORD-9900", "customer": "Bob Smith", "total": "$88.50", "status": "processing", "date": "2026-05-30", "flag": None},
    9901: {"id": 9901, "order_id": "#ORD-9901", "customer": "Alice Johnson", "total": "$142.00", "status": "shipped", "date": "2026-05-30", "flag": None},
    9880: {"id": 9880, "order_id": "#ORD-9880", "customer": "suspicious@email.xyz", "total": "$899.00", "status": "pending", "date": "2026-05-29", "flag": "fraud-risk"},
    9851: {"id": 9851, "order_id": "#ORD-9851", "customer": "John Doe", "total": "$412.00", "status": "pending", "date": "2026-05-28", "flag": "address-mismatch"},
    9810: {"id": 9810, "order_id": "#ORD-9810", "customer": "bulk@buyer.com", "total": "$1,800.00", "status": "pending", "date": "2026-05-27", "flag": "high-value"},
}

_counters["orders"] = 9901

# ── Support Tickets ────────────────────────────────────────────────────────────

tickets: dict[int, dict] = {
    4390: {"id": 4390, "subject": "How to export data?", "user": "newbie@example.com", "priority": "low", "opened": "2026-05-28", "status": "open", "category": "how-to", "resolved_by": None, "time_to_close": None},
    4391: {"id": 4391, "subject": "Can't invite team members", "user": "team@startup.io", "priority": "medium", "opened": "2026-05-28", "status": "resolved", "category": "access", "resolved_by": "agent_mark", "time_to_close": "1h 05m"},
    4394: {"id": 4394, "subject": "Billing period question", "user": "billing@corp.com", "priority": "low", "opened": "2026-05-29", "status": "resolved", "category": "billing", "resolved_by": "agent_tom", "time_to_close": "18m"},
    4395: {"id": 4395, "subject": "Integration not working", "user": "ops@company.net", "priority": "medium", "opened": "2026-05-29", "status": "open", "category": "bug-report", "resolved_by": None, "time_to_close": None},
    4396: {"id": 4396, "subject": "Data export failed", "user": "data@corp.com", "priority": "medium", "opened": "2026-05-29", "status": "resolved", "category": "bug-report", "resolved_by": "agent_sarah", "time_to_close": "3h 22m"},
    4397: {"id": 4397, "subject": "API rate limit confusion", "user": "dev@example.com", "priority": "low", "opened": "2026-05-30", "status": "resolved", "category": "how-to", "resolved_by": "agent_mark", "time_to_close": "45m"},
    4398: {"id": 4398, "subject": "Feature request: dark mode", "user": "dev@startup.io", "priority": "low", "opened": "2026-05-29", "status": "open", "category": "feature-request", "resolved_by": None, "time_to_close": None},
    4399: {"id": 4399, "subject": "Password reset not arriving", "user": "locked@example.com", "priority": "high", "opened": "2026-05-30", "status": "resolved", "category": "access", "resolved_by": "agent_sarah", "time_to_close": "2h 10m"},
    4400: {"id": 4400, "subject": "Wrong charge on invoice", "user": "billing@corp.com", "priority": "high", "opened": "2026-05-30", "status": "open", "category": "billing", "resolved_by": None, "time_to_close": None},
    4401: {"id": 4401, "subject": "Cannot access my account", "user": "locked@example.com", "priority": "high", "opened": "2026-05-30", "status": "open", "category": "access", "resolved_by": None, "time_to_close": None},
}

_counters["tickets"] = 4401

# ── API Keys ───────────────────────────────────────────────────────────────────

api_keys: dict[int, dict] = {
    1: {"id": 1, "key_prefix": "sk_live_aB3x…", "owner": "alice@example.com", "scope": "read:all", "created": "2026-05-30", "active": True, "requests_week": 1_840_200, "last_used": "2026-05-30 12:48", "usage_pct": 82, "plan": "Pro", "limit": "100k req/day"},
    2: {"id": 2, "key_prefix": "sk_live_qR7m…", "owner": "bob@corp.com", "scope": "write:posts", "created": "2026-05-30", "active": True, "requests_week": 410_500, "last_used": "2026-05-30 11:30", "usage_pct": 41, "plan": "Pro", "limit": "100k req/day"},
    3: {"id": 3, "key_prefix": "sk_live_zT9k…", "owner": "carol@startup.io", "scope": "read:users", "created": "2026-05-29", "active": True, "requests_week": 95_300, "last_used": "2026-05-30 08:00", "usage_pct": 10, "plan": "Basic", "limit": "10k req/day"},
    4: {"id": 4, "key_prefix": "sk_live_nW2p…", "owner": "ops@company.net", "scope": "admin", "created": "2026-05-29", "active": True, "requests_week": 920_100, "last_used": "2026-05-30 12:45", "usage_pct": 91, "plan": "Business", "limit": "500k req/day"},
    5: {"id": 5, "key_prefix": "sk_test_hJ5r…", "owner": "dev@example.com", "scope": "read:all", "created": "2026-05-28", "active": True, "requests_week": 12_000, "last_used": "2026-05-29 17:00", "usage_pct": 12, "plan": "Free", "limit": "1k req/day"},
    6: {"id": 6, "key_prefix": "sk_live_yK1d…", "owner": "analytics@corp.com", "scope": "read:all", "created": "2026-05-20", "active": True, "requests_week": 288_400, "last_used": "2026-05-30 10:00", "usage_pct": 58, "plan": "Business", "limit": "500k req/day"},
    7: {"id": 7, "key_prefix": "sk_live_mX8w…", "owner": "data@lab.dev", "scope": "read:all", "created": "2026-05-18", "active": True, "requests_week": 184_000, "last_used": "2026-05-30 09:10", "usage_pct": 37, "plan": "Pro", "limit": "500k req/day"},
}

revoked_keys: dict[int, dict] = {
    8: {"id": 8, "key_prefix": "sk_test_dU0f…", "owner": "intern@corp.com", "revoked_by": "admin", "reason": "test key cleanup", "date": "2026-05-24"},
    9: {"id": 9, "key_prefix": "sk_live_vL6s…", "owner": "leaked@secret.com", "revoked_by": "superadmin", "reason": "compromised", "date": "2026-05-26"},
    10: {"id": 10, "key_prefix": "sk_live_oP4c…", "owner": "former@employee.com", "revoked_by": "superadmin", "reason": "offboarding", "date": "2026-05-28"},
}

_counters["api_keys"] = 10

# ── Servers ────────────────────────────────────────────────────────────────────

servers: dict[str, dict] = {
    "web-01": {"node": "web-01", "status": "healthy", "cpu": "12%", "memory": "34%", "uptime": "42d 6h"},
    "web-02": {"node": "web-02", "status": "healthy", "cpu": "18%", "memory": "41%", "uptime": "42d 6h"},
    "web-03": {"node": "web-03", "status": "degraded", "cpu": "87%", "memory": "78%", "uptime": "42d 6h"},
    "api-01": {"node": "api-01", "status": "healthy", "cpu": "24%", "memory": "52%", "uptime": "14d 2h"},
    "api-02": {"node": "api-02", "status": "healthy", "cpu": "31%", "memory": "58%", "uptime": "14d 2h"},
    "db-primary": {"node": "db-primary", "status": "healthy", "cpu": "45%", "memory": "71%", "uptime": "89d 14h"},
    "db-replica": {"node": "db-replica", "status": "healthy", "cpu": "22%", "memory": "68%", "uptime": "89d 14h"},
    "worker-01": {"node": "worker-01", "status": "healthy", "cpu": "9%", "memory": "28%", "uptime": "7d 3h"},
}

deployments: dict[int, dict] = {
    1: {"id": 1, "version": "v2.14.1", "deployed_by": "alice@example.com", "nodes": "all", "status": "success", "date": "2026-05-30 10:00"},
    2: {"id": 2, "version": "v2.14.0", "deployed_by": "ops@company.net", "nodes": "api-01, api-02", "status": "success", "date": "2026-05-28 14:30"},
    3: {"id": 3, "version": "v2.13.9", "deployed_by": "alice@example.com", "nodes": "web-01, web-02, web-03", "status": "success", "date": "2026-05-25 09:00"},
    4: {"id": 4, "version": "v2.13.8", "deployed_by": "dev@example.com", "nodes": "all", "status": "rolled-back", "date": "2026-05-22 16:00"},
    5: {"id": 5, "version": "v2.13.7", "deployed_by": "ops@company.net", "nodes": "worker-01", "status": "success", "date": "2026-05-20 11:00"},
}

server_alerts: dict[int, dict] = {
    1: {"id": 1, "alert": "High CPU on web-03", "severity": "warning", "node": "web-03", "since": "2026-05-30 11:42"},
    2: {"id": 2, "alert": "Memory threshold 70% on db-primary", "severity": "info", "node": "db-primary", "since": "2026-05-30 09:15"},
}

_counters["deployments"] = 5
_counters["server_alerts"] = 2

# ── Media ──────────────────────────────────────────────────────────────────────

media_files: dict[int, dict] = {
    1: {"id": 1, "filename": "banner_summer.png", "uploader": "alice@example.com", "size": "2.4 MB", "type": "image", "date": "2026-05-30", "flag": None},
    2: {"id": 2, "filename": "product_demo.mp4", "uploader": "bob@corp.com", "size": "84.1 MB", "type": "video", "date": "2026-05-30", "flag": None},
    3: {"id": 3, "filename": "report_q1.pdf", "uploader": "carol@startup.io", "size": "1.1 MB", "type": "document", "date": "2026-05-29", "flag": None},
    4: {"id": 4, "filename": "avatar_hank.jpg", "uploader": "hank@example.com", "size": "0.3 MB", "type": "image", "date": "2026-05-29", "flag": None},
    5: {"id": 5, "filename": "tutorial_slides.pdf", "uploader": "grace@example.com", "size": "5.2 MB", "type": "document", "date": "2026-05-28", "flag": None},
    6: {"id": 6, "filename": "inappropriate_video.mp4", "uploader": "badactor@dark.com", "size": "120.0 MB", "type": "video", "date": "2026-05-29", "flag": "adult-content"},
    7: {"id": 7, "filename": "spam_promo.png", "uploader": "spam1@evil.com", "size": "0.8 MB", "type": "image", "date": "2026-05-28", "flag": "spam"},
    8: {"id": 8, "filename": "pirated_movie.mp4", "uploader": "pirate@nowhere.com", "size": "700.0 MB", "type": "video", "date": "2026-05-27", "flag": "copyright"},
}

_counters["media_files"] = 8

# ── Email Campaigns ────────────────────────────────────────────────────────────

email_campaigns: dict[int, dict] = {
    1: {"id": 1, "campaign": "May Newsletter", "sent": 14_200, "open_rate": "38.4%", "click_rate": "12.1%", "date": "2026-05-28", "status": "sent", "recipients": 14_200, "scheduled": None},
    2: {"id": 2, "campaign": "New Feature Announcement", "sent": 9_800, "open_rate": "52.1%", "click_rate": "24.8%", "date": "2026-05-25", "status": "sent", "recipients": 9_800, "scheduled": None},
    3: {"id": 3, "campaign": "Re-engagement Drive", "sent": 3_200, "open_rate": "19.3%", "click_rate": "4.2%", "date": "2026-05-20", "status": "sent", "recipients": 3_200, "scheduled": None},
    4: {"id": 4, "campaign": "Premium Upsell", "sent": 2_891, "open_rate": "41.7%", "click_rate": "18.9%", "date": "2026-05-15", "status": "sent", "recipients": 2_891, "scheduled": None},
    5: {"id": 5, "campaign": "June Newsletter", "sent": 0, "open_rate": "—", "click_rate": "—", "date": None, "status": "scheduled", "recipients": 14_382, "scheduled": "2026-06-01 09:00"},
    6: {"id": 6, "campaign": "Summer Sale", "sent": 0, "open_rate": "—", "click_rate": "—", "date": None, "status": "scheduled", "recipients": 14_382, "scheduled": "2026-06-05 10:00"},
    7: {"id": 7, "campaign": "Webinar Invite", "sent": 0, "open_rate": "—", "click_rate": "—", "date": None, "status": "scheduled", "recipients": 5_000, "scheduled": "2026-06-10 08:00"},
}

email_bounces: dict[int, dict] = {
    1: {"id": 1, "email": "olduser@defunct.net", "type": "hard", "campaign": "May Newsletter", "date": "2026-05-28"},
    2: {"id": 2, "email": "typo@gmial.com", "type": "hard", "campaign": "May Newsletter", "date": "2026-05-28"},
    3: {"id": 3, "email": "full@inbox.com", "type": "soft", "campaign": "New Feature Announcement", "date": "2026-05-25"},
    4: {"id": 4, "email": "noreply@company.com", "type": "hard", "campaign": "Re-engagement Drive", "date": "2026-05-20"},
    5: {"id": 5, "email": "inactive@example.org", "type": "soft", "campaign": "Premium Upsell", "date": "2026-05-15"},
}

_counters["email_campaigns"] = 7
_counters["email_bounces"] = 5

# ── Notifications ──────────────────────────────────────────────────────────────

notifications: dict[int, dict] = {
    1: {"id": 1, "title": "New Feature: Dark Mode", "recipients": 14_382, "channel": "push", "open_rate": "61.2%", "date": "2026-05-29"},
    2: {"id": 2, "title": "Your order has shipped", "recipients": 412, "channel": "email", "open_rate": "78.4%", "date": "2026-05-29"},
    3: {"id": 3, "title": "Security alert: new login", "recipients": 28, "channel": "sms", "open_rate": "94.1%", "date": "2026-05-28"},
    4: {"id": 4, "title": "Weekly digest", "recipients": 9_104, "channel": "email", "open_rate": "32.8%", "date": "2026-05-26"},
    5: {"id": 5, "title": "Flash sale starts now!", "recipients": 14_382, "channel": "push", "open_rate": "44.7%", "date": "2026-05-24"},
}

opt_outs: dict[int, dict] = {
    1: {"id": 1, "user": "tired@example.com", "channel": "push", "reason": "too many notifications", "notification": "Flash sale starts now!", "date": "2026-05-24"},
    2: {"id": 2, "user": "quiet@startup.io", "channel": "email", "reason": "unsubscribe", "notification": "Weekly digest", "date": "2026-05-26"},
    3: {"id": 3, "user": "nomobile@corp.com", "channel": "sms", "reason": "prefer email", "notification": "Security alert: new login", "date": "2026-05-28"},
    4: {"id": 4, "user": "spam@nowhere.com", "channel": "push", "reason": "spam report", "notification": "New Feature: Dark Mode", "date": "2026-05-29"},
    5: {"id": 5, "user": "unsubscribe@me.com", "channel": "email", "reason": "unsubscribe", "notification": "Your order has shipped", "date": "2026-05-29"},
}

_counters["notifications"] = 5
_counters["opt_outs"] = 5

# ── Permissions ────────────────────────────────────────────────────────────────

roles: dict[str, dict] = {
    "superadmin": {"role": "superadmin", "users": 2, "can_delete": True, "can_ban": True, "can_export": True},
    "admin": {"role": "admin", "users": 12, "can_delete": True, "can_ban": True, "can_export": True},
    "moderator": {"role": "moderator", "users": 87, "can_delete": False, "can_ban": True, "can_export": False},
    "premium": {"role": "premium", "users": 2891, "can_delete": False, "can_ban": False, "can_export": True},
    "free": {"role": "free", "users": 11179, "can_delete": False, "can_ban": False, "can_export": False},
}

role_requests: dict[int, dict] = {
    1: {"id": 1, "user": "bob@corp.com", "current_role": "premium", "requested_role": "moderator", "reason": "Wants to help moderate the community", "date": "2026-05-30"},
    2: {"id": 2, "user": "grace@example.com", "current_role": "free", "requested_role": "premium", "reason": "Long-time contributor", "date": "2026-05-29"},
    3: {"id": 3, "user": "hank@example.com", "current_role": "moderator", "requested_role": "admin", "reason": "Team lead, needs admin tools", "date": "2026-05-28"},
}

role_changes: dict[int, dict] = {
    1: {"id": 1, "user": "alice@example.com", "change": "free → moderator", "changed_by": "superadmin", "date": "2026-05-01"},
    2: {"id": 2, "user": "eva@example.com", "change": "free → premium", "changed_by": "admin", "date": "2026-05-10"},
    3: {"id": 3, "user": "former@employee.com", "change": "admin → banned", "changed_by": "superadmin", "date": "2026-05-26"},
    4: {"id": 4, "user": "carol@example.com", "change": "free → premium", "changed_by": "admin", "date": "2026-05-15"},
}

_counters["role_requests"] = 3
_counters["role_changes"] = 4
