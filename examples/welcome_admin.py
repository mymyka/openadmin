import asyncio
import random

from openadmin import AdminPage

page = AdminPage("Welcome to admin")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# Welcome to the Admin Panel

Use this panel to monitor platform health, review recent activity, and manage your system.

## Quick Links
- **Users** — manage accounts, roles, and bans
- **Posts** — moderate content and track engagement
- **Tasks** — monitor user task completion across the platform

> All times are shown in UTC.
"""
