---
url: 'https://docs.workato.com/en/on-prem/agents/monitoring.md'
description: >-
  Enable the Prometheus-compatible metrics endpoint and health checks on the
  Workato on-prem agent to monitor CPU, memory, JVM, and connector activity.
---

# On-prem agent monitoring

Starting with OPA version 32.0, the on-prem agent exposes a Prometheus-compatible metrics endpoint.

[Prometheus server](https://prometheus.io/) is an open-source monitoring tool that collects metrics by polling (scraping) HTTP endpoints at regular intervals and storing the results in a local time-series database. Visualization and alerting tools, such as [Grafana](https://grafana.com/), can then query that database to build dashboards and set up alerts based on metrics such as CPU usage, memory, JVM health, and connector activity. Tools that support the Prometheus exposition format directly, such as [Datadog](https://docs.datadoghq.com/integrations/openmetrics/), can also scrape the endpoint without a Prometheus server.

> **MANUAL MONITORING DEPRECATION**
> 
> The manual monitoring feature (available from OPA 2.14.0) was deprecated and isn't available in OPA version [31.0](/en/on-prem/agents/versions#v31-0) or higher. You can still access the old monitoring tool if you're running an OPA version between 2.14.0 and 30.0.

## Enable the monitoring endpoint

Add the `--mgmt-listen` flag to the agent's start parameters to enable monitoring:

**Windows service**

Complete the following steps to enable monitoring on an agent installed as a Windows service:

1. Open the Windows **Start** menu.
   
2. Go to **All apps > Workato**.
   
3. Open the **Service Wrapper Configuration** app for the agent you plan to configure.
   
4. Go to the **Startup** tab.
   
5. Enter the `--mgmt-listen=http://[HOST]:[PORT]/` flag in the **Arguments** field. Replace `[HOST]` and `[PORT]` with a host and port available in your network.
   
6. Click **OK**, then restart the agent for the changes to take effect.
   

**Windows console-based**

Use the following command to start a console-based Windows agent with monitoring enabled:

```sh
bin\run.cmd --mgmt-listen=http://[HOST]:[PORT]/
```

Replace `[HOST]` and `[PORT]` with a host and port available in your network.

**Linux, Mac, and Docker**

Use the following command to start a Linux, Mac, or Docker agent with monitoring enabled:

```sh
./bin/run.sh --mgmt-listen=http://[HOST]:[PORT]/
```

Replace `[HOST]` and `[PORT]` with a host and port available in your network.

> **NETWORK ACCESS**
> 
> Use `127.0.0.1` as the host address to restrict access to the local machine, or use a specific network interface address to allow access from other hosts. Note that Prometheus endpoints are unauthenticated by default.

The agent logs the following when the management server is ready to accept requests:

```
ManagementServer - Management server is up
```

Access the deprecated monitoring UI

Complete the following steps using an OPA version between 2.14.0 and 30.0 to access the old monitoring UI:

1. Run the agent start command for your operating system with the `--monitoring` and `--mgmt-listen` flags.
   
   **Windows**
   
   ```sh
   bin\run.cmd --monitoring=true --mgmt-listen=[HOST]:[PORT]
   ```
   
   Replace `[HOST]` and `[PORT]` with a host and port available in your network.
   
   **Linux, Mac, and Docker**
   
   ```sh
   ./bin/run.sh --monitoring=true --mgmt-listen=[HOST]:[PORT]
   ```
   
   Replace `[HOST]` and `[PORT]` with a host and port available in your network.
   
2. Go to `http://[HOST]:[PORT]/monitoring`. Replace `[HOST]` and `[PORT]` with the values defined in the previous step.
   

## Health endpoints

In OPA versions [2.13.0](/en/on-prem/agents/versions#v2-13-0) and later the management server also exposes health endpoints you can use with container orchestration platforms, load balancers, or external monitoring tools. Both endpoints return `{"status":"UP"}` when the agent is healthy:

| Endpoint | Description |
| --- | --- |
| `/health/live` | Indicates the agent process is running. |
| `/health/ready` | Indicates the agent is connected to Workato and ready to process requests. |

For example:

```sh
curl http://[HOST]:[PORT]/health/live
```

## Scrape metrics

Use the following command as a manual check to verify the endpoint is working. Refer to [Configure automated scraping](#configure-automated-scraping) for ongoing automated collection.

```sh
curl http://[HOST]:[PORT]/prometheus
```

The response is in the standard [Prometheus text exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/), with `Content-Type: text/plain;version=0.0.4;charset=utf-8`. Each metric includes a `# HELP` description, a `# TYPE` declaration, and one or more sample lines:

```
# HELP jvm_threads_live_threads The current number of live threads
# TYPE jvm_threads_live_threads gauge
jvm_threads_live_threads{session_id="abc123"} 60.0
```

The endpoint doesn't stream or push data. Each request returns a fresh snapshot of the current metric values at the time of the call.

### Configure automated scraping

Some monitoring tools, such as Grafana, require you to store OPA metrics in a [Prometheus server](https://prometheus.io/docs/prometheus/latest/getting_started/) time-series database.

You can add a scrape job to `prometheus.yml` to collect and store metrics at regular intervals. For example:

```yaml
scrape_configs:
  - job_name: 'workato-opa'
    metrics_path: '/prometheus'
    static_configs:
      - targets:
          - '[HOST]:[PORT]'
```

#### Multiple agents

Each agent in a group exposes its own `/prometheus` endpoint. Add a target for each agent in your scrape config:

```yaml
scrape_configs:
  - job_name: 'workato-opa'
    metrics_path: '/prometheus'
    static_configs:
      - targets:
          - '10.0.1.10:[PORT]'
          - '10.0.1.11:[PORT]'
```

Most metrics include a `session_id` label that uniquely identifies the agent instance they came from. Use this label in queries to filter or compare agents. Executor and HTTP metrics don't carry this label.

For example:

```
# Metrics from a specific agent
jvm_memory_used_bytes{session_id="abc123"}

# Memory usage across all agents (group or compare by session_id in your dashboard)
jvm_memory_used_bytes
```

## Available metrics

The `/prometheus` endpoint provides the following metrics groups:

| Group | Description |
| --- | --- |
| JVM | Memory usage, GC pause durations, and thread counts. For example: **jvm\_memory\_used\_bytes**: The amount of memory used by the JVM.; **jvm\_gc\_pause\_seconds**: Time spent in garbage collection pauses.; **jvm\_threads\_live\_threads**: The current number of live threads, including both daemon and non-daemon threads. |
| Process | CPU time and usage, process uptime, process memory usage, and open file descriptors. For example: **process\_cpu\_usage**: The recent CPU usage of the agent process.; **process\_cpu\_time\_ns\_total**: The total CPU time used by the agent process.; **process\_uptime\_seconds**: The uptime of the JVM.; **process\_start\_time\_seconds**: The start time of the process, in seconds since the Unix epoch.; **process\_memory\_used\_bytes**: The amount of memory used by the agent process.; **process\_files\_open\_files**: The number of open file descriptors.; **process\_files\_max\_files**: The maximum number of file descriptors available to the process. |
| System | Host-level CPU, memory, and disk statistics. For example: **system\_cpu\_usage**: The recent CPU usage of the host system., **system\_cpu\_count**: The number of processors available to the JVM., **system\_memory\_used\_bytes**: The amount of memory used on the host system., **disk\_free\_bytes**: The usable disk space for the agent's temporary file directory., **disk\_total\_bytes**: The total disk space for the agent's temporary file directory. |
| HTTP | Request counts and latency for the agent's outbound HTTP traffic to Workato's cloud services. For example: **http\_requests\_seconds**: Request count and latency for the agent's outbound HTTP calls to Workato's cloud services. |
| Executor | Thread pool activity and task throughput. For example: **executor\_active\_threads**: The approximate number of threads actively executing tasks., **executor\_completed\_tasks\_total**: The approximate total number of tasks that have completed execution., **jetty\_threads\_\***: Thread pool size and utilization for the agent's embedded Jetty server., **request\_lookup\_table\_size\_requests**: The number of requests currently in progress on the agent. |
| Connector | Per-connector invocation durations, labeled by profile. Use these metrics to identify which profiles and connections consume the most OPA resources. For example: **profile\_invocation\_duration\_seconds**: Invocation duration for a connector profile, labeled by profile name and type. |
| Agent | Identity and network metrics. For example: **instance\_info**: Runtime information about the agent instance, such as version and OS.; **netty\_channel\_ping\_rtt\_ms**: Network latency measured by ping round trip time to Workato's gateway. |
| Logging | Log event counts by severity level. For example: **logback\_events\_total**: The number of log events emitted, labeled by severity level. |

> **WINDOWS BEHAVIOR**
> 
> `process_files_open_files` is a Linux/Unix OS concept and isn't present in Windows responses. Metrics such as `process_memory_used_bytes` and `system_memory_used_bytes` may show `0.0` immediately after startup and populate correctly after the agent warms up, typically after two to three minutes.

---
