from openadmin import AdminPage, Stat, Table

page = AdminPage("Users")


@page.stat("Total Users", description="Total number of registered users")
def total_users() -> Stat[int]:
    return Stat(value=14_382)


@page.stat("Active Users", description="Users active in the last 30 days")
def active_users() -> Stat[int]:
    return Stat(value=9_104)


@page.stat("New Today", description="Users who registered today")
def new_today() -> Stat[int]:
    return Stat(value=47)


@page.stat("Premium Users", description="Users on a paid plan")
def premium_users() -> Stat[int]:
    return Stat(value=2_891)


@page.stat("Banned Users", description="Accounts currently suspended")
def banned_users() -> Stat[int]:
    return Stat(value=213)


@page.table("User List", description="All registered users")
def user_list() -> Table:
    return Table(
        data=[
            {
                "id": 1,
                "name": "Alice Johnson",
                "email": "alice@example.com",
                "plan": "premium",
                "active": True,
            },
            {
                "id": 2,
                "name": "Bob Smith",
                "email": "bob@example.com",
                "plan": "free",
                "active": True,
            },
            {
                "id": 3,
                "name": "Carol White",
                "email": "carol@example.com",
                "plan": "premium",
                "active": False,
            },
            {
                "id": 4,
                "name": "David Brown",
                "email": "david@example.com",
                "plan": "free",
                "active": True,
            },
            {
                "id": 5,
                "name": "Eva Martinez",
                "email": "eva@example.com",
                "plan": "premium",
                "active": True,
            },
        ]
    )


@page.table("Recent Signups", description="Users who registered in the last 7 days")
def recent_signups() -> Table:
    return Table(
        data=[
            {
                "id": 14382,
                "name": "Frank Lee",
                "email": "frank@example.com",
                "registered": "2026-05-30",
            },
            {
                "id": 14381,
                "name": "Grace Kim",
                "email": "grace@example.com",
                "registered": "2026-05-29",
            },
            {
                "id": 14380,
                "name": "Hank Davis",
                "email": "hank@example.com",
                "registered": "2026-05-29",
            },
            {
                "id": 14379,
                "name": "Ivy Chen",
                "email": "ivy@example.com",
                "registered": "2026-05-28",
            },
            {
                "id": 14378,
                "name": "Jake Wilson",
                "email": "jake@example.com",
                "registered": "2026-05-27",
            },
        ]
    )


@page.table("Top Users", description="Users with the most activity")
def top_users() -> Table:
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
def banned_user_list() -> Table:
    return Table(
        data=[
            {
                "id": 101,
                "name": "Spam Bot 1",
                "email": "spam1@evil.com",
                "reason": "spam",
                "banned_on": "2026-05-10",
            },
            {
                "id": 245,
                "name": "Troll Account",
                "email": "troll@bad.com",
                "reason": "harassment",
                "banned_on": "2026-05-15",
            },
            {
                "id": 389,
                "name": "Fake User",
                "email": "fake@nowhere.com",
                "reason": "impersonation",
                "banned_on": "2026-05-20",
            },
            {
                "id": 412,
                "name": "Abuser X",
                "email": "abuse@dark.com",
                "reason": "abuse",
                "banned_on": "2026-05-22",
            },
            {
                "id": 500,
                "name": "Bot Account",
                "email": "bot@scraper.io",
                "reason": "scraping",
                "banned_on": "2026-05-28",
            },
        ]
    )


@page.table("Role Distribution", description="Breakdown of users by assigned role")
def role_distribution() -> Table:
    return Table(
        data=[
            {"role": "admin", "count": 12, "percentage": "0.08%"},
            {"role": "moderator", "count": 87, "percentage": "0.60%"},
            {"role": "premium", "count": 2891, "percentage": "20.10%"},
            {"role": "free", "count": 11179, "percentage": "77.73%"},
            {"role": "banned", "count": 213, "percentage": "1.48%"},
        ]
    )
