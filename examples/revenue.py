import asyncio
import random

from openadmin import AdminPage, Stat, Table

page = AdminPage("Revenue")


@page.stat("MRR", description="Monthly Recurring Revenue")
async def mrr() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="$84,320")


@page.stat("ARR", description="Annualized Recurring Revenue")
async def arr() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="$1,011,840")


@page.stat("Revenue Today", description="Total revenue collected today")
async def revenue_today() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="$12,480")


@page.stat("Refunds This Month", description="Total refunded amount in May 2026")
async def refunds_month() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="$1,204")


@page.stat("Churn Rate", description="Monthly subscription churn rate")
async def churn_rate() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="2.1%")


@page.table("Recent Transactions", description="Last 5 completed payments")
async def recent_transactions() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"id": "txn_98821", "user": "alice@example.com", "amount": "$99.00", "plan": "Pro", "date": "2026-05-30"},
            {"id": "txn_98820", "user": "bob@corp.com", "amount": "$299.00", "plan": "Business", "date": "2026-05-30"},
            {"id": "txn_98819", "user": "carol@startup.io", "amount": "$29.00", "plan": "Starter", "date": "2026-05-30"},
            {"id": "txn_98818", "user": "dan@example.net", "amount": "$99.00", "plan": "Pro", "date": "2026-05-29"},
            {"id": "txn_98817", "user": "eva@lab.dev", "amount": "$599.00", "plan": "Enterprise", "date": "2026-05-29"},
        ]
    )


@page.table("Revenue by Plan", description="Breakdown of MRR by subscription tier")
async def revenue_by_plan() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"plan": "Starter", "subscribers": 1840, "mrr": "$26,680", "share": "31.6%"},
            {"plan": "Pro", "subscribers": 920, "mrr": "$36,080", "share": "42.8%"},
            {"plan": "Business", "subscribers": 210, "mrr": "$15,680", "share": "18.6%"},
            {"plan": "Enterprise", "subscribers": 24, "mrr": "$5,880", "share": "7.0%"},
        ]
    )


@page.table("Recent Refunds", description="Latest refund requests processed")
async def recent_refunds() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"id": "ref_1044", "user": "unhappy@user.com", "amount": "$99.00", "reason": "not as described", "date": "2026-05-29"},
            {"id": "ref_1043", "user": "cancel@corp.com", "amount": "$299.00", "reason": "cancellation", "date": "2026-05-28"},
            {"id": "ref_1042", "user": "duplicate@pay.com", "amount": "$29.00", "reason": "duplicate charge", "date": "2026-05-27"},
        ]
    )


@page.table("Monthly Revenue Trend", description="Revenue totals for the past 6 months")
async def monthly_trend() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"month": "December 2025", "revenue": "$71,200", "growth": "+4.1%"},
            {"month": "January 2026", "revenue": "$74,800", "growth": "+5.1%"},
            {"month": "February 2026", "revenue": "$77,100", "growth": "+3.1%"},
            {"month": "March 2026", "revenue": "$79,400", "growth": "+3.0%"},
            {"month": "April 2026", "revenue": "$81,900", "growth": "+3.1%"},
            {"month": "May 2026", "revenue": "$84,320", "growth": "+3.0%"},
        ]
    )
