---
url: 'https://docs.workato.com/en/on-prem/agents/shutdown.md'
description: >-
  Stop a Workato on-prem agent safely using the shutdown script or SIGTERM, and
  disable it in Workato to reroute actions before restarting.
---

# Stop an on-prem agent

The Workato on-prem agent maintains an active connection between your network and Workato's [On-prem group dashboard](https://workato.com/on_prem_groups/). You may need to temporarily disable this connection when restarting or [upgrading](/en/on-prem/agents/upgrade) the agent.

An on-prem agent process is typically stopped through a `SIGTERM`. Use one of the following methods to send this signal to an agent:

- Use the `./bin/shutdown.sh` shutdown script that comes with the on-prem agent.
- Run the `kill -s TERM` command on the running agent.

The agent performs a graceful shutdown automatically. This ensures the agent terminates safely, preventing disruption to pending requests and avoiding job failures or data loss. The default shutdown timeout is 30 seconds.

## Disable an agent in Workato

We recommend that you disable the agent in Workato before stopping it to prevent new actions from routing to it.

Complete the following steps to disable an agent in Workato:

> **API INTEGRATION**
> 
> Alternatively, use the [Developer API](/en/workato-api/on-prem#update-on-prem-agent) or [Embedded API](/en/oem/oem-api/on-prem#update-on-prem-agent) to update the agent's `enabled` status to `false`.

1. Sign in to Workato.
   
2. Go to **Tools > On-prem groups** and select the on-prem group that contains the agent you plan to disable.
   
3. Confirm there is an active backup agent in the group to prevent recipe disruption. Refer to [Add an agent](/en/on-prem/groups/add-agent) if you need to create a backup agent.
   
4. Go to the agent's **Version** column and click **...** (ellipsis).
   
5. Click **Disable**.
   
   ![Disable agent](/assets/disable-agent.XkiFyUDi.png)_Disable an agent in Workato._
   

## Stop an agent on Linux, Mac, or Docker

Run the shutdown script using the following command to initiate a graceful shutdown on Linux, Mac, or Docker:

```shell
./shutdown.sh
```

The script sends `SIGTERM` to gracefully terminate the agent process. The agent terminates after the configured timeout if the shutdown hasn't completed.

> **PID FILE CREATION**
> 
> The agent doesn't create a PID file during startup by default. Start and stop the agent with the following options if you encounter an error due to a missing PID file:
> 
> ```shell
> ./run.sh --pid-file=/var/run/workato-agent/workato-agent.pid
> ```
> 
> ```shell
> ./shutdown.sh --pid-file=/var/run/workato-agent/workato-agent.pid
> ```

### Optional arguments

The shutdown script supports the following optional arguments:

| Argument | Description |
| --- | --- |
| \--pid | Specifies the process ID (PID) of the on-prem agent instance to shut down. Use this as an alternative to `--pid-file`. |
| \--pid-file | Specifies the path to the PID file, which contains the agent process ID. This defaults to `/var/run/workato-agent/workato-agent.pid`. |
| \--pid-file-purge | Purges the PID file before shutdown. |
| \--kill-signal | Specifies the signal to use. This defaults to `TERM`. |
| \--help | Displays a list of all accepted arguments. |

The following examples show how to run the shutdown script with optional arguments:

```shell
./shutdown.sh --pid-file=/var/run/workato-agent/workato-agent.pid --pid-file-purge
./shutdown.sh --kill-signal=TERM
./shutdown.sh --help
```

## Stop an agent on Windows

Complete the following steps to stop an agent as a Windows service or using a command, depending on your setup:

**Windows service**

Complete the following steps to stop the **Workato on-prem agent** Windows service:

1. Press `Win + R`, type `services.msc`, and press `Enter`.
   
2. Go to the **Services** window and locate the agent.
   
3. Right-click the agent and select **Stop**.
   
4. Wait for the agent to stop completely before closing the window.
   

**Console-based agent**

Complete the following steps to stop a console-based agent:

1. Press `Ctrl + Shift + Esc` to open Task Manager.
   
2. Go to the **Processes** tab and locate the agent process you plan to stop.
   
3. Right-click the agent process and select **End Task**.
   

## Reconnect an agent to Workato

Agents lose their connection to Workato when they stop. Complete the following steps to reconnect an agent to Workato:

> **API INTEGRATION**
> 
> Alternatively, use the [Developer API](/en/workato-api/on-prem#update-on-prem-agent) or [Embedded API](/en/oem/oem-api/on-prem#update-on-prem-agent) to update the agent's `enabled` status to `true`.

1. Refer to one of the following sections to start the agent on the host machine:
   
   - [Run an agent on Windows](/en/on-prem/agents/run#running-on-windows-64-bit)
   - [Run an agent on Linux](/en/on-prem/agents/run#run-an-agent-on-linux)
   - [Run an agent on Mac](/en/on-prem/agents/run#run-an-agent-on-mac)
   - [Run an agent using Docker](/en/on-prem/agents/run#run-an-agent-using-docker)
2. Go to **Tools > On-prem groups** and select the on-prem group that contains the agent you plan to reconnect.
   
3. Go to the agent's **Version** column, click **...** (ellipsis), and then select **Enable agent**.
   
   ![Enable on-prem agent](/assets/toggle-opa-on.CKN6egQD.png)
   

Workato sends a request to your on-prem agent to establish a connection. A successful connection request returns an **Active** status.

![On-prem agent connected](/assets/opa-connected.CNtWzBxc.png)

---
