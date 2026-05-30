from openadmin import AdminPage, Stat, Table

page = AdminPage("Servers")


@page.stat("Total Nodes", description="Active server nodes in the cluster")
def total_nodes() -> Stat:
    return Stat(value=12)


@page.stat("Avg CPU Usage", description="Mean CPU utilization across all nodes")
def avg_cpu() -> Stat:
    return Stat(value="34.2%")


@page.stat("Avg Memory Usage", description="Mean RAM utilization across all nodes")
def avg_memory() -> Stat:
    return Stat(value="61.8%")


@page.stat("Disk Usage", description="Total disk used across all nodes")
def disk_usage() -> Stat:
    return Stat(value="4.1 TB / 10 TB")


@page.stat("Requests/sec", description="Current aggregate requests per second")
def requests_per_sec() -> Stat:
    return Stat(value=8_420)


@page.table("Node Status", description="Health and resource usage per server node")
def node_status() -> Table:
    return Table(
        data=[
            {"node": "api-01", "status": "healthy", "cpu": "28%", "memory": "58%", "uptime": "14d 6h"},
            {"node": "api-02", "status": "healthy", "cpu": "31%", "memory": "62%", "uptime": "14d 6h"},
            {"node": "api-03", "status": "healthy", "cpu": "24%", "memory": "55%", "uptime": "14d 6h"},
            {"node": "worker-01", "status": "healthy", "cpu": "44%", "memory": "70%", "uptime": "14d 6h"},
            {"node": "worker-02", "status": "degraded", "cpu": "89%", "memory": "91%", "uptime": "14d 6h"},
            {"node": "db-primary", "status": "healthy", "cpu": "18%", "memory": "74%", "uptime": "30d 2h"},
            {"node": "db-replica", "status": "healthy", "cpu": "12%", "memory": "68%", "uptime": "30d 2h"},
            {"node": "cache-01", "status": "healthy", "cpu": "8%", "memory": "42%", "uptime": "14d 6h"},
        ]
    )


@page.table("Recent Deployments", description="Latest code deployments to production")
def recent_deployments() -> Table:
    return Table(
        data=[
            {"version": "v2.14.1", "deployed_by": "ci-bot", "nodes": "all", "status": "success", "date": "2026-05-30 08:00"},
            {"version": "v2.14.0", "deployed_by": "alice", "nodes": "api-*", "status": "success", "date": "2026-05-28 14:30"},
            {"version": "v2.13.5", "deployed_by": "ci-bot", "nodes": "all", "status": "success", "date": "2026-05-25 09:00"},
            {"version": "v2.13.4", "deployed_by": "bob", "nodes": "worker-*", "status": "rolled-back", "date": "2026-05-22 16:00"},
        ]
    )


@page.table("Active Alerts", description="Infrastructure alerts currently firing")
def active_alerts() -> Table:
    return Table(
        data=[
            {"alert": "High CPU on worker-02", "severity": "warning", "node": "worker-02", "since": "2026-05-30 11:40"},
            {"alert": "Disk > 80% on db-primary", "severity": "warning", "node": "db-primary", "since": "2026-05-29 08:00"},
        ]
    )


@page.table("Network Traffic", description="Inbound and outbound traffic by node (last hour)")
def network_traffic() -> Table:
    return Table(
        data=[
            {"node": "api-01", "inbound_mb": 1_240, "outbound_mb": 3_820, "connections": 8_400},
            {"node": "api-02", "inbound_mb": 1_180, "outbound_mb": 3_610, "connections": 8_100},
            {"node": "api-03", "inbound_mb": 1_090, "outbound_mb": 3_390, "connections": 7_800},
            {"node": "worker-01", "inbound_mb": 480, "outbound_mb": 210, "connections": 120},
            {"node": "worker-02", "inbound_mb": 520, "outbound_mb": 190, "connections": 118},
        ]
    )
