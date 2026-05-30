import asyncio
import random

from fastapi import HTTPException, Request

from openadmin import AdminPage, PaginationParamsDep, Stat, Table

from . import db

page = AdminPage("Servers")


@page.markdown("Overview")
async def overview() -> str:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return """
# Infrastructure Overview

Monitor the health, performance, and capacity of all server nodes in the cluster.

## Node Types

| Node Group | Count | Role |
|---|---|---|
| `api-*` | 3 | Handle inbound HTTP traffic |
| `worker-*` | 2 | Process background jobs and queues |
| `db-primary` | 1 | Primary read/write database |
| `db-replica` | 1 | Read replica and failover target |
| `cache-01` | 1 | In-memory cache layer (Redis) |

## Current Alerts

> **worker-02** is running at 89% CPU and 91% memory. This node should be investigated before it causes job queue delays. Consider draining and restarting if the condition persists beyond 30 minutes.

## Capacity Thresholds

- CPU > **80%** sustained for 5 min → scale or investigate
- Memory > **85%** → risk of OOM kills on that node
- Disk > **80%** → schedule cleanup or expand volume
- Request rate spike > **2×** baseline → check for traffic anomaly or DDoS

## Deployment Policy

All production deployments go through `ci-bot` with a mandatory rollback plan. Manual deployments by named admins are permitted for hotfixes but must be logged and reviewed within 24 hours.
"""


@page.stat("Total Nodes", description="Active server nodes in the cluster")
async def total_nodes() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=len(db.servers))


@page.stat("Avg CPU Usage", description="Mean CPU utilization across all nodes")
async def avg_cpu() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="34.2%")


@page.stat("Avg Memory Usage", description="Mean RAM utilization across all nodes")
async def avg_memory() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="61.8%")


@page.stat("Disk Usage", description="Total disk used across all nodes")
async def disk_usage() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value="4.1 TB / 10 TB")


@page.stat("Requests/sec", description="Current aggregate requests per second")
async def requests_per_sec() -> Stat:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Stat(value=8_420)


@page.action_delete("Dismiss alert", description="Acknowledge and dismiss an infrastructure alert")
async def dismiss_alert(id: int) -> None:
    if id not in db.server_alerts:
        raise HTTPException(status_code=404, detail="Alert not found")
    db.server_alerts.pop(id)


@page.action_delete("Remove deployment", description="Remove a deployment record")
async def remove_deployment(id: int) -> None:
    if id not in db.deployments:
        raise HTTPException(status_code=404, detail="Deployment not found")
    db.deployments.pop(id)


@page.table("Node Status", description="Health and resource usage per server node")
async def node_status() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(data=list(db.servers.values()))


@page.table("Recent Deployments", description="Latest code deployments to production")
async def recent_deployments(req: Request, pagination: PaginationParamsDep) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    rows = sorted(db.deployments.values(), key=lambda d: d["date"], reverse=True)
    start = pagination.page * pagination.per_page
    page_rows = rows[start : start + pagination.per_page]
    return Table(data=[
        {
            "version": d["version"],
            "deployed_by": d["deployed_by"],
            "nodes": d["nodes"],
            "status": d["status"],
            "date": d["date"],
            "__actions__": [
                {
                    "color": "danger",
                    "method": "DELETE",
                    "url": str(req.url_for(remove_deployment.__name__)) + f"?id={d['id']}",
                }
            ],
        }
        for d in page_rows
    ])


@page.table("Active Alerts", description="Infrastructure alerts currently firing")
async def active_alerts(req: Request) -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(data=[
        {
            "alert": a["alert"],
            "severity": a["severity"],
            "node": a["node"],
            "since": a["since"],
            "__actions__": [
                {
                    "color": "warning",
                    "method": "DELETE",
                    "url": str(req.url_for(dismiss_alert.__name__)) + f"?id={a['id']}",
                }
            ],
        }
        for a in db.server_alerts.values()
    ])


@page.table(
    "Network Traffic", description="Inbound and outbound traffic by node (last hour)"
)
async def network_traffic() -> Table:
    await asyncio.sleep(random.uniform(0.05, 0.3))
    return Table(
        data=[
            {"node": "api-01", "inbound_mb": 1_240, "outbound_mb": 3_820, "connections": 8_400},
            {"node": "api-02", "inbound_mb": 1_180, "outbound_mb": 3_610, "connections": 8_100},
            {"node": "api-03", "inbound_mb": 1_090, "outbound_mb": 3_390, "connections": 7_800},
            {"node": "worker-01", "inbound_mb": 480, "outbound_mb": 210, "connections": 120},
            {"node": "worker-02", "inbound_mb": 520, "outbound_mb": 190, "connections": 118},
        ]
    )
