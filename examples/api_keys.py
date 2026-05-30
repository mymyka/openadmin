import asyncio
import random

from fastapi import HTTPException, Request

from openadmin import AdminPage, PaginationParamsDep, Stat, Table

from . import db

page = AdminPage("API Keys")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# API Keys

Monitor active API keys, usage patterns, and security events across all integrations.

## Key Scopes

| Scope | Access Level | Typical Use Case |
|---|---|---|
| `read:all` | Read any resource | Dashboards, reporting tools |
| `read:users` | Read user data only | CRM integrations |
| `write:posts` | Create and edit posts | Publishing tools |
| `admin` | Full API access | Trusted internal services |

## Key Prefixes

Keys are prefixed to distinguish environment:

- `sk_live_` — production keys; treat as credentials, never log
- `sk_test_` — sandbox keys; safe to rotate freely during development

> **Never commit API keys to version control.** If a `sk_live_` key is found in a repository, revoke it immediately regardless of whether the repository is private. Treat the key as compromised.

## Rate Limit Alerts

Two keys are currently above **80% of their daily quota**:

- `ops@company.net` at 91% — on the Business plan (500K req/day)
- `alice@example.com` at 82% — on the Pro plan (100K req/day)

Contact key owners before they hit their limit to avoid unexpected `429` errors in their integrations.

## Security Events

A key belonging to `leaked@secret.com` was revoked on 2026-05-26 due to confirmed compromise. Keys revoked for this reason should also trigger a security review of any data accessed using that key in the preceding 72 hours.
"""


@page.stat("Total Active Keys", description="API keys currently in use")
async def total_active_keys() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for k in db.api_keys.values() if k["active"]))


@page.stat("Keys Created Today", description="New API keys issued in the last 24 hours")
async def keys_created_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=sum(1 for k in db.api_keys.values() if k["created"] == "2026-05-30"))


@page.stat("Keys Revoked This Month", description="API keys disabled in May 2026")
async def keys_revoked_month() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=len(db.revoked_keys))


@page.stat(
    "Requests Today (API)", description="Total API calls authenticated by key today"
)
async def api_requests_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=2_841_002)


@page.action_delete("Revoke key", description="Immediately disable an API key")
async def revoke_key(id: int) -> None:
    if id not in db.api_keys:
        raise HTTPException(status_code=404, detail="API key not found")
    key = db.api_keys.pop(id)
    key["revoked_by"] = "admin"
    key["reason"] = "manual revocation"
    key["date"] = "2026-05-30"
    db.revoked_keys[id] = key


@page.table("Recently Created Keys", description="Newest API keys issued")
async def recently_created(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(db.api_keys.values(), key=lambda k: k["created"], reverse=True)
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "key_prefix": k["key_prefix"],
            "owner": k["owner"],
            "scope": k["scope"],
            "created": k["created"],
            "__actions__": [
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(revoke_key.__name__)) + f"?id={k['id']}",
                }
            ],
        }
        for k in page_rows
    ])


@page.table("High Usage Keys", description="API keys with the most requests this week")
async def high_usage_keys(req: Request) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(db.api_keys.values(), key=lambda k: k["requests_week"], reverse=True)
    return Table(data=[
        {
            "key_prefix": k["key_prefix"],
            "owner": k["owner"],
            "requests_week": k["requests_week"],
            "last_used": k["last_used"],
            "__actions__": [
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(revoke_key.__name__)) + f"?id={k['id']}",
                }
            ],
        }
        for k in rows[:5]
    ])


@page.table("Recently Revoked Keys", description="API keys that were recently disabled")
async def recently_revoked(pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(db.revoked_keys.values(), key=lambda k: k["date"], reverse=True)
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "key_prefix": k["key_prefix"],
            "owner": k["owner"],
            "revoked_by": k["revoked_by"],
            "reason": k["reason"],
            "date": k["date"],
        }
        for k in page_rows
    ])


@page.table(
    "Keys Approaching Rate Limit",
    description="Keys that hit over 80% of their rate limit today",
)
async def rate_limit_warnings() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = [k for k in db.api_keys.values() if k.get("usage_pct", 0) >= 80]
    return Table(data=[
        {
            "key_prefix": k["key_prefix"],
            "owner": k["owner"],
            "usage": f"{k['usage_pct']}%",
            "limit": k["limit"],
            "plan": k["plan"],
        }
        for k in rows
    ])
