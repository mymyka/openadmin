"""
SQLite database module for examples.
Uses Python stdlib sqlite3 wrapped in asyncio.to_thread for async compatibility.
DB file is created at examples/admin.db on first use.
"""

import asyncio
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "admin.db"


def _get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def _run(fn):
    """Run a blocking sqlite3 function in a thread pool."""
    return asyncio.to_thread(fn)


# ── Schema ─────────────────────────────────────────────────────────────────────

def _create_schema() -> None:
    conn = _get_conn()
    with conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id          INTEGER PRIMARY KEY,
                name        TEXT    NOT NULL,
                email       TEXT    NOT NULL UNIQUE,
                plan        TEXT    NOT NULL DEFAULT 'free',
                active      INTEGER NOT NULL DEFAULT 1,
                role        TEXT    NOT NULL DEFAULT 'free',
                registered  TEXT    NOT NULL
            );

            CREATE TABLE IF NOT EXISTS banned_users (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name        TEXT    NOT NULL,
                email       TEXT    NOT NULL,
                reason      TEXT    NOT NULL,
                banned_on   TEXT    NOT NULL
            );
        """)
    conn.close()


# ── Query helpers ───────────────────────────────────────────────────────────────

async def fetchall(sql: str, params: tuple = ()) -> list[dict]:
    def _run_query():
        conn = _get_conn()
        rows = conn.execute(sql, params).fetchall()
        conn.close()
        return [dict(r) for r in rows]
    return await asyncio.to_thread(_run_query)


async def fetchone(sql: str, params: tuple = ()) -> dict | None:
    def _run_query():
        conn = _get_conn()
        row = conn.execute(sql, params).fetchone()
        conn.close()
        return dict(row) if row else None
    return await asyncio.to_thread(_run_query)


async def execute(sql: str, params: tuple = ()) -> int:
    """Execute a write statement, return lastrowid."""
    def _run_exec():
        conn = _get_conn()
        with conn:
            cur = conn.execute(sql, params)
            rowid = cur.lastrowid
        conn.close()
        return rowid
    return await asyncio.to_thread(_run_exec)


async def count(table: str, where: str = "", params: tuple = ()) -> int:
    clause = f"WHERE {where}" if where else ""
    row = await fetchone(f"SELECT COUNT(*) AS n FROM {table} {clause}", params)
    return row["n"] if row else 0


# ── Initialise on import ────────────────────────────────────────────────────────

_create_schema()
