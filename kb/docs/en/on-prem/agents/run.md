---
url: 'https://docs.workato.com/en/on-prem/agents/run.md'
description: >-
  Start an existing Workato on-prem agent on Windows, Linux, Mac, or Docker, and
  reconnect an agent to Workato.
---

# Run an on-prem agent

This guide explains how to start an existing on-prem agent (OPA). Refer to the [Add an agent](/en/on-prem/groups/add-agent) guide to install and activate an agent.

> **ALLOW TRAFFIC TO WORKATO FROM YOUR SERVER**
> 
> Ensure traffic to Workato is allowed from your server to use OPA. Refer to [security allowlists](/en/security/ip-allowlists#traffic-to-workato) to add Workato to your allowlist.

## Run an agent on Windows

Complete the following steps to start an agent as a Windows service or using a command, depending on your setup:

**Windows service**

Complete the following steps to start an agent as a Windows service:

1. Press `Win + R`, type `services.msc`, and press `Enter`.
   
2. Go to the **Services** window and locate the agent.
   
3. Optional. Complete the following steps to set the agent to start automatically:
   
   1. Right-click the agent and select **Properties**.
      
   2. Use the **Startup type** drop-down menu to select **Automatic**.
      
   3. Click **Apply**.
      
4. Right-click the agent and select **Start**.
   
5. Wait for the agent to finish starting before closing the window.
   

**Command script**

Use the following command to run the on-prem agent, replacing `<YOUR_DIRECTORY>` with the directory name:

```shell
<YOUR_DIRECTORY>\bin\run.cmd
```

## Run an agent on Linux

Complete the following steps to start an agent on Linux:

1. Use the following command to start the agent service in the background:
   
   ```shell
   sudo systemctl start workato-agent.service
   ```
   
2. Optional. Use the following command to enable the agent to start automatically:
   
   ```shell
   sudo systemctl enable workato-agent.service
   ```
   

## Run an agent on Mac

Use the following command to run the on-prem agent, replacing `<YOUR_DIRECTORY>` with the directory name:

```shell
sh <YOUR_DIRECTORY>/bin/run.sh
```

  

> **SSH SCRIPT CONFIGURATION**
> 
> You can access the server through SSH to allow the agent to run in the background independent of your shell session if you add the nohup command (`&`) at the end of the script. You can also include a `> file_name` command to ensure that the outputs are logged.
> 
> ```shell
> sh <YOUR_DIRECTORY>/bin/run.sh > opa_output.txt &
> ```

## Run an agent using Docker

Use the following command to run the agent as a Docker container, replacing `<YOUR_DIRECTORY>` with the directory name and `<VERSION>` with the agent version:

```shell
docker run -d -v /<YOUR_DIRECTORY>/conf:/var/lib/workato-agent/conf daa34553.workato.com/semi-public/amd64/workato-agent:<VERSION>
```

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
