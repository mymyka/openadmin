"""
Seed script — populates examples/admin.db with realistic data.
Run once: python -m examples.seed
Re-running is safe: it clears existing rows first.
"""

import random
import sqlite3
from datetime import date, timedelta
from pathlib import Path

DB_PATH = Path(__file__).parent / "admin.db"

FIRST_NAMES = [
    "Alice",
    "Bob",
    "Carol",
    "David",
    "Eva",
    "Frank",
    "Grace",
    "Hank",
    "Ivy",
    "Jake",
    "Karen",
    "Leo",
    "Mia",
    "Noah",
    "Olivia",
    "Paul",
    "Quinn",
    "Rachel",
    "Sam",
    "Tina",
    "Uma",
    "Victor",
    "Wendy",
    "Xander",
    "Yara",
    "Zoe",
    "Aaron",
    "Beth",
    "Carlos",
    "Diana",
    "Eric",
    "Fiona",
    "George",
    "Hannah",
    "Ian",
    "Julia",
    "Kevin",
    "Laura",
    "Mike",
    "Nina",
    "Oscar",
    "Priya",
    "Raj",
    "Sara",
    "Tom",
    "Ursula",
    "Vince",
    "Willa",
    "Xena",
    "Yusuf",
    "Zara",
    "Adam",
    "Bella",
    "Chris",
    "Dana",
    "Eli",
    "Faith",
    "Gary",
    "Holly",
    "Igor",
    "Jane",
    "Kyle",
    "Lisa",
    "Mark",
    "Nancy",
    "Owen",
    "Penny",
    "Quincy",
    "Rita",
    "Steve",
    "Tracy",
]

LAST_NAMES = [
    "Johnson",
    "Smith",
    "White",
    "Brown",
    "Martinez",
    "Lee",
    "Kim",
    "Davis",
    "Wilson",
    "Anderson",
    "Taylor",
    "Thomas",
    "Jackson",
    "Harris",
    "Martin",
    "Thompson",
    "Garcia",
    "Clark",
    "Lewis",
    "Young",
    "Walker",
    "Hall",
    "Allen",
    "Scott",
    "Green",
    "Adams",
    "Baker",
    "Carter",
    "Mitchell",
    "Nelson",
    "Perez",
    "Roberts",
    "Turner",
    "Phillips",
    "Campbell",
    "Parker",
    "Evans",
    "Edwards",
    "Collins",
    "Stewart",
    "Morris",
    "Rogers",
    "Reed",
    "Cook",
    "Morgan",
    "Bell",
    "Murphy",
    "Bailey",
    "Rivera",
    "Cooper",
    "Richardson",
    "Cox",
    "Ward",
]

EMAIL_DOMAINS = [
    "example.com",
    "corp.com",
    "startup.io",
    "company.net",
    "dev.org",
    "mail.co",
    "inbox.dev",
    "webmail.net",
    "fastmail.io",
    "proton.me",
]

BAN_REASONS = [
    "spam",
    "harassment",
    "abuse",
    "impersonation",
    "scraping",
    "policy-violation",
]

PLANS = ["free", "free", "free", "free", "premium", "premium", "enterprise"]
ROLES = ["free", "free", "free", "free", "premium", "premium", "moderator", "admin"]
AVATARS = [f"/static/avatars/avatar_{i}.svg" for i in range(1, 9)]


def random_date(start: date, end: date) -> str:
    delta = (end - start).days
    return (start + timedelta(days=random.randint(0, delta))).isoformat()


def make_email(first: str, last: str, used: set[str]) -> str:
    base = f"{first.lower()}.{last.lower()}"
    for domain in random.sample(EMAIL_DOMAINS, len(EMAIL_DOMAINS)):
        candidate = f"{base}@{domain}"
        if candidate not in used:
            used.add(candidate)
            return candidate
    # fallback with number
    for i in range(1, 100):
        candidate = f"{base}{i}@{random.choice(EMAIL_DOMAINS)}"
        if candidate not in used:
            used.add(candidate)
            return candidate
    raise RuntimeError("Could not generate unique email")


def seed(conn: sqlite3.Connection) -> None:
    conn.execute("DELETE FROM banned_users")
    conn.execute("DELETE FROM users")

    today = date(2026, 5, 30)
    start = date(2025, 1, 1)
    used_emails: set[str] = set()
    users = []

    for i in range(1, 401):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        email = make_email(first, last, used_emails)
        plan = random.choice(PLANS)
        role = (
            "premium"
            if plan == "premium"
            else (
                "moderator"
                if random.random() < 0.02
                else ("admin" if random.random() < 0.005 else "free")
            )
        )
        active = random.random() > 0.1
        registered = random_date(start, today)
        document = "/static/sample_document.txt" if random.random() > 0.3 else None
        avatar = random.choice(AVATARS)
        users.append(
            (
                i,
                f"{first} {last}",
                email,
                plan,
                int(active),
                role,
                registered,
                document,
                avatar,
            )
        )

    # Force a few users registered today for "New Today" stat
    today_str = today.isoformat()
    for j in range(8):
        idx = random.randint(0, len(users) - 1)
        u = users[idx]
        users[idx] = (u[0], u[1], u[2], u[3], u[4], u[5], today_str, u[7], u[8])

    conn.executemany(
        "INSERT INTO users (id, name, email, plan, active, role, registered, document, avatar) VALUES (?,?,?,?,?,?,?,?,?)",
        users,
    )

    # Seed banned users (50 rows)
    ban_start = date(2025, 6, 1)
    banned = []
    for k in range(1, 51):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        email = make_email(first + str(k), "ban", used_emails)
        reason = random.choice(BAN_REASONS)
        banned_on = random_date(ban_start, today)
        banned.append((k, f"{first} {last}", email, reason, banned_on))

    conn.executemany(
        "INSERT INTO banned_users (id, name, email, reason, banned_on) VALUES (?,?,?,?,?)",
        banned,
    )

    conn.commit()
    print(f"Seeded {len(users)} users, {len(banned)} banned users into {DB_PATH}")


if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    seed(conn)
    conn.close()
