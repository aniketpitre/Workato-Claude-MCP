---
url: 'https://docs.workato.com/en/on-prem/groups/add-agent/docker.md'
description: >-
  Deploy a Workato on-prem agent using a Docker image, from retrieving the agent
  to running it in your on-prem group.
---

# Deploy an on-prem agent using a Docker image

This page provides steps on how to deploy an on-prem agent using Docker image.

> **PREREQUISITES**
> 
> You must complete the following prerequisites to deploy an on-prem agent using Docker image:
> 
> - [Create an on-prem group](/en/on-prem/groups/create-group).
> - Ensure that Docker is installed on your machine.

## Retrieve the on-prem agent

Complete the following steps to retrieve the on-prem agent:

1. Sign in to your Workato account.
   
2. Go to **Tools > On-prem groups** and select your on-prem group.
   
3. Click **Add on-prem agent**.
   
4. Provide a descriptive agent name in the **Agent name** field, and select **Docker** as the operating system (OS) in the **Operating system** field.
   
   ![Choose OS](/assets/select-docker.DyZMu7-1.png)_Choose OS_
   
5. Copy and paste the Docker pull command provided by Workato into your terminal to pull the Docker image from the repository:
   
   ```shell
   docker pull "daa34553.workato.com/semi-public/amd64/workato-agent:<version>";
   ```
   
   ![Pull Docker](/assets/docker-pull.DxKXF5dL.png)_Pull Docker image_
   

## Activate and run the on-prem agent

Complete the following steps to activate and run the on-prem agent:

1. Copy and paste the activation command provided by Workato. The command should look similar to the example below, with `"secret-agent-code"` replaced by your unique activation code.
   
   Running this command automatically generates the agent key and certificate within the agent container. Note that the activation code is valid for one hour.
   
   ```shell
   docker run -it -e WORKATO_AGENT_ACTIVATION_CODE="secret-agent-code" "daa34553.workato.com/semi-public/amd64/workato-agent:<version>
   ```
   
     
   
   > **ALLOW TRAFFIC TO WORKATO FROM YOUR SERVER**
   > 
   > Ensure traffic to Workato is allowed from your server to use OPA. Refer to [security allowlists](/en/security/ip-allowlists#traffic-to-workato) to add Workato to your allowlist.
   
   ![Activate](/assets/docker-activate.DtkgqplN.png)_Activate agent and run docker image_
   
   > **CERTIFICATE VALIDITY PERIOD**
   > 
   > The agent certificate remains valid for 1 year after the generation date.
   > 
   > Renew the certificate before its expiration date to avoid interruptions. Refer to the [Renew agent keys](/en/on-prem/agents/key#renew-agent-keys) guide for more information.
   
2. Optional. Run the following command if you plan to export your agent certificate and key to a directory on your host machine:
   
   ```shell
   docker run -it --rm -v /<YOUR_DIRECTORY>/conf:/var/lib/workato-agent/conf -e WORKATO_AGENT_ACTIVATE_ONLY=y -e WORKATO_AGENT_ACTIVATION_CODE="secret-agent-code" "daa34553.workato.com/semi-public/amd64/workato-agent:<VERSION>";
   ```
   
   Replace `<YOUR_DIRECTORY>` with the directory name and `<VERSION>` with the agent version.
   
3. Optional. Run the OPA docker using the following command if you already have a valid agent key and certificate:
   
   ```shell
   docker run -d -v /<YOUR_DIRECTORY>/conf:/var/lib/workato-agent/conf daa34553.workato.com/semi-public/amd64/workato-agent:<VERSION>
   ```
   
   Replace `<YOUR_DIRECTORY>` with the directory name and `<VERSION>` with the agent version.
   
4. Click **Test agent** after the agent starts to verify that the connection is successful.
   
   ![Test](/assets/test-agent-setup.BqTxbvVM.png)_Test agent_
   

> **PRIVATE KEY**
> 
> Workato doesn't have access to your private key file (`cert.key`) in the OPA `conf` folder. Ensure you protect this file from unauthorized access.

---
