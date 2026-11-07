---
url: 'https://docs.workato.com/en/on-prem/agents/key.md'
description: >-
  Create and renew the cert.key and cert.pem files that connect a Workato
  on-prem agent to the cloud through a gateway.
---

# On-prem agent key management

The `cert.key` and `cert.pem` files are required to connect an on-prem agent (OPA) to Workato cloud through a gateway. Refer to the following sections to manage these files:

- [Create agent keys](#create-agent-keys)
- [Renew agent keys](#renew-agent-keys)

## Create agent keys

Complete the following steps to create `cert` files for your agent:

1. Save the **Activation code** for your agent during setup. Refer to the [Add an agent](/en/on-prem/groups/add-agent) page for more information about agent setup.
   
2. Open a command-line interface and set the working directory to the `bin` folder inside your OPA installation folder (`C:\Program Files\Workato Agent` by default if using Windows).
   
3. Run the `activate` script and pass the activation code as an input parameter to create the `cert.key` and `cert.pem` files. For example:
   
   ```shell
   activate.cmd --code=ACTIVATION_CODE
   ```
   
   The certificate remains valid for 1 year after the generation date.
   
   > **PROXY USAGE**
   > 
   > You must pass additional parameters to the `activate` script if you're using a proxy. Refer to the [Set up proxy access for your on-prem agent](/en/on-prem/agents/proxy) page for more information.
   > 
   > Run the `activate` script with the `--help` parameter to display the full list of accepted input properties.
   

> **PRIVATE KEY**
> 
> Workato doesn't have access to your private key file (`cert.key`) in the OPA `conf` folder. Ensure you protect this file from unauthorized access.

## Renew agent keys

Workato recommends upgrading the on-prem agent to generate a new key and certificate. Refer to the [Upgrade an existing agent with zero downtime](/en/on-prem/agents/upgrade#upgrade-existing-agent-with-zero-downtime) guide for more information.

Alternatively, you can complete the following steps to generate a new key and certificate without upgrading:

1. Create a new on-prem agent in the same on-prem group as the original agent. You don't need to download the installer during the setup unless you plan to upgrade the original agent. Refer to the [Add an agent](/en/on-prem/groups/add-agent) or [Upgrade an agent](/en/on-prem/agents/upgrade) page for more information.
   
2. Save the **Activation code** for the new agent during setup.
   
3. Go to the `conf` folder inside your existing OPA installation folder (`C:\Program Files\Workato Agent` by default if using Windows).
   
4. Move the `cert.pem` and `cert.key` files to a backup location.
   
5. Open a command-line interface and set the working directory to the `bin` folder inside your existing OPA installation folder.
   
6. Run the `activate` script and pass the activation code as an input parameter to create new `cert.key` and `cert.pem` files. For example:
   
   ```shell
   activate.cmd --code=ACTIVATION_CODE
   ```
   
     
   
   > **PROXY USAGE**
   > 
   > You must pass additional parameters to the `activate` script if you're using a proxy. Refer to the [Set up proxy access for your on-prem agent](/en/on-prem/agents/proxy) page for more information.
   > 
   > Run the `activate` script with the `--help` parameter to display the full list of accepted input properties.
   
7. Return to Workato and click **Test**.
   
8. Ensure your new agent appears as **Active**, then click **Done**. The existing on-prem agent installation becomes the new agent. The new certificate remains valid for 1 year after the generation date.
   
9. Optional. Go to the old agent's **Version** column, click **...** (ellipsis), and then select **Delete agent**. ![Delete agent](/assets/delete-agent.CObPze2D.png)_Delete the old agent._

---
