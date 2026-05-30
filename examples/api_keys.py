import asyncio
import random

from openadmin import AdminPage, Stat, Table

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
    return Stat(value=1_842)


@page.stat("Keys Created Today", description="New API keys issued in the last 24 hours")
async def keys_created_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=28)


@page.stat("Keys Revoked This Month", description="API keys disabled in May 2026")
async def keys_revoked_month() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=64)


@page.stat(
    "Requests Today (API)", description="Total API calls authenticated by key today"
)
async def api_requests_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=2_841_002)


@page.table("Recently Created Keys", description="Newest API keys issued")
async def recently_created() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "key_prefix": "sk_live_aB3x…",
                "owner": "alice@example.com",
                "scope": "read:all",
                "created": "2026-05-30",
            },
            {
                "key_prefix": "sk_live_qR7m…",
                "owner": "bob@corp.com",
                "scope": "write:posts",
                "created": "2026-05-30",
            },
            {
                "key_prefix": "sk_live_zT9k…",
                "owner": "carol@startup.io",
                "scope": "read:users",
                "created": "2026-05-29",
            },
            {
                "key_prefix": "sk_live_nW2p…",
                "owner": "ops@company.net",
                "scope": "admin",
                "created": "2026-05-29",
            },
            {
                "key_prefix": "sk_test_hJ5r…",
                "owner": "dev@example.com",
                "scope": "read:all",
                "created": "2026-05-28",
            },
        ]
    )


@page.table("High Usage Keys", description="API keys with the most requests this week")
async def high_usage_keys() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "key_prefix": "sk_live_aB3x…",
                "owner": "alice@example.com",
                "requests_week": 1_840_200,
                "last_used": "2026-05-30 12:48",
            },
            {
                "key_prefix": "sk_live_nW2p…",
                "owner": "ops@company.net",
                "requests_week": 920_100,
                "last_used": "2026-05-30 12:45",
            },
            {
                "key_prefix": "sk_live_qR7m…",
                "owner": "bob@corp.com",
                "requests_week": 410_500,
                "last_used": "2026-05-30 11:30",
            },
            {
                "key_prefix": "sk_live_yK1d…",
                "owner": "analytics@corp.com",
                "requests_week": 288_400,
                "last_used": "2026-05-30 10:00",
            },
            {
                "key_prefix": "sk_live_mX8w…",
                "owner": "data@lab.dev",
                "requests_week": 184_000,
                "last_used": "2026-05-30 09:10",
            },
        ]
    )


@page.table("Recently Revoked Keys", description="API keys that were recently disabled")
async def recently_revoked() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "key_prefix": "sk_live_oP4c…",
                "owner": "former@employee.com",
                "revoked_by": "superadmin",
                "reason": "offboarding",
                "date": "2026-05-28",
            },
            {
                "key_prefix": "sk_live_vL6s…",
                "owner": "leaked@secret.com",
                "revoked_by": "superadmin",
                "reason": "compromised",
                "date": "2026-05-26",
            },
            {
                "key_prefix": "sk_test_dU0f…",
                "owner": "intern@corp.com",
                "revoked_by": "admin",
                "reason": "test key cleanup",
                "date": "2026-05-24",
            },
        ]
    )


@page.table(
    "Keys Approaching Rate Limit",
    description="Keys that hit over 80% of their rate limit today",
)
async def rate_limit_warnings() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {
                "key_prefix": "sk_live_aB3x…",
                "owner": "alice@example.com",
                "usage": "82%",
                "limit": "100k req/day",
                "plan": "Pro",
            },
            {
                "key_prefix": "sk_live_nW2p…",
                "owner": "ops@company.net",
                "usage": "91%",
                "limit": "500k req/day",
                "plan": "Business",
            },
        ]
    )
