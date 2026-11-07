---
url: 'https://docs.workato.com/en/on-prem/agents/upgrade.md'
description: >-
  Upgrade your Workato on-prem agent to a new version with zero downtime or by
  replacing the existing agent.
---

# Upgrade an agent

We recommend upgrading your on-prem agent to a new version on a regular basis. With every release, we add new features along with improved performance, stability, and security. Refer to the [release notes](/en/on-prem/agents/versions) for more information about all the changes.

If you encounter issues during or after the upgrade, refer to the [On-prem upgrade & configuration issues](/en/on-prem/agents/opa-troubleshooting/troubleshoot-upgrade) section for troubleshooting guidance.

> **HOW TO UPGRADE**
> 
> There are several ways to upgrade an existing on-prem agent:
> 
> - [Upgrade an existing agent with zero downtime](/en/on-prem/agents/upgrade#upgrade-existing-agent-with-zero-downtime)
> - [Upgrade an existing agent by stopping and replacing the old one](/en/on-prem/agents/upgrade#upgrade-the-existing-agent-by-replacing-the-old-one)
> - [Upgrade an existing agent older than 2.15.0 and configure connections directly in Workato](/en/on-prem/agents/upgrade#upgrade-existing-agent-older-than-2-15-0-and-start-configuring-connections-directly-in-workato)

> **PRIVATE KEY**
> 
> Workato doesn't have access to your private key file (`cert.key`) in the OPA `conf` folder. Ensure you protect this file from unauthorized access.

> **ALLOW TRAFFIC TO WORKATO FROM YOUR SERVER**
> 
> Ensure traffic to Workato is allowed from your server to use OPA. Refer to [security allowlists](/en/security/ip-allowlists#traffic-to-workato) to add Workato to your allowlist.

## Upgrade an existing agent with zero downtime

When you are running your agent in the production environment and don't want interruptions, you can upgrade by adding a new agent to your on-prem group and then removing the old one. Complete the following recommended steps to upgrade your OPA:

1. Sign in to Workato.
   
2. Go to **Tools > On-prem groups** and select the on-prem group that contains the agent you plan to upgrade.
   
3. Ensure your on-prem group has more than one active agent. [Add](/en/on-prem/groups/add-agent) and [start](/en/on-prem/agents/run) another agent if you only have one.
   
   > **CONFIGURING A NEW AGENT**
   > 
   > If you use a `config.yml` file to set up your connections, copy it from your old agent to your new one. This allows agents to connect to the same resources. Additionally, if you use [password encryption](/en/on-prem/agents/password-encryption), you must encrypt your passwords again for the new agent since the encryption is based on agent-specific keys.
   
4. [Check the logs](/en/on-prem/agents/logging) of the new agent to ensure it is working properly.
   
5. Go to the old agent's **Version** column, click **...** (ellipsis), and then select **Disable agent**. Alternatively, for agents installed on Windows machines, you can stop the old agent by terminating the **Workato Agent** Windows service or the console-based agent. The other agents continue processing incoming jobs.
   
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
      
   
   ![Disable agent](/assets/disable-agent.XkiFyUDi.png)_Disable the old agent in Workato._
   
6. Confirm that the new agent is working properly and there are no errors in your running recipes.
   
7. Go to the old agent's **Version** column, click **...** (ellipsis), and then select **Delete agent**. Alternatively, you can leave it disabled so that if you encounter any issues, you can disable the new agent and restart the old one.
   
   ![Delete agent](/assets/delete-agent.CObPze2D.png)_Delete the old agent._
   

## Upgrade an existing agent by replacing the old one

You can upgrade an existing agent by stopping it and replacing it with the latest version.

The steps to replace an existing agent vary based on your operating system:

- [Windows](#windows)
- [Linux](#linux)

### Windows

1. Sign in to Workato.
   
2. Go to **Tools > On-prem groups** and select the on-prem group that contains the agent you plan to upgrade.
   
3. Go to the **Version** column and click **Update** to open the upgrade wizard.
   
   ![Update on-prem agent to latest version](/assets/on-prem-upgrade.z39OC8pb.png)_Update on-prem agent to the latest version_
   
4. Read the release notes and then click **Next**.
   
   ![On-prem agent upgrade wizard](/assets/on-prem-upgrade-wizard.2KQNg3oD.png)_On-prem agent upgrade wizard_
   
5. Stop the existing agent by terminating the **Workato on-prem agent** Windows service or the console-based agent.
   
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
      
   
6. Uninstall the old agent (for example, go to **Start Menu > Workato > Uninstall**).
   
   > **REMAINING FILES AFTER UNINSTALL**
   > 
   > Some files, such as `config.yml` and the certificate files (`cert.key`, `cert.pem`), may remain in the OPA directory after uninstalling the agent. Remove these files manually to avoid potential issues. Retain the `conf` and `lib_ext` folders if you plan to upgrade the agent.
   
7. Run the installer. The installer stores the agent in `C:\Program Files\Workato Agent`, creates a Workato group in the **Start** menu, and installs a Windows service called `Workato on-prem agent` by default.
   
   > **OPA WINDOWS SERVICE USER ACCOUNTS**
   > 
   > From OPA version [2.18.0](/en/on-prem/agents/versions#v2-18) onwards, the Workato OPA Windows service user account is set to `Local Service` instead of `Local System`, which was used in previous versions.
   > 
   > Complete the following steps to access the settings of an OPA Windows service user account:
   > 
   > 1. Press `Win + R`, type `services.msc`, and press `Enter`.
   >    
   > 2. Go to the **Services** window and locate the agent.
   >    
   > 3. Right-click the agent and select **Properties**
   >    
   
   > **CONFIGURING A NEW AGENT**
   > 
   > If you use a `config.yml` file to set up your connections, copy it from your old agent to your new one. This allows agents to connect to the same resources. Additionally, if you use [password encryption](/en/on-prem/agents/password-encryption), you must encrypt your passwords again for the new agent since the encryption is based on agent-specific keys.
   
8. Copy and paste the **Activation command** from Workato when prompted. The code is valid for one hour. Click **Regenerate code** in the setup wizard to generate a new code if it expires.
   
   Alternatively, you can select **Activate agent manually** and activate the OPA after installation using the activation script.
   
   Activate an agent after installation
   
   Complete the following steps to activate the agent using a command script:
   
   1. Go to the `bin` folder inside your OPA installation folder. `C:\Program Files\Workato Agent` is the default path for Windows.
      
   2. Run the `activate.cmd` script. Refer to the [Set up proxy access for your on-prem agent](/en/on-prem/agents/proxy) page to configure the `activate.cmd` script for use with a proxy.
      
      You can run the `activate.cmd` script with the `--help` parameter to display the full list of accepted input properties.
      
   3. Provide the **Activation command** from Workato's OPA setup wizard when prompted. The code is valid for one hour. Click **Regenerate code** in the setup wizard to generate a new code if it expires.
      
   
   ![Copy and paste the Activation code](/assets/windows-activation.CHMwuD3e.png)_Copy and paste the **Activation code**_
   
9. Go **Tools > On-prem groups** in Workato, select your on-prem group, and verify the new agent is active and has the correct **Version** number.
   

### Linux

The command to upgrade your agent varies based on your package format:

**Linux DEB package**

```shell
% sudo apt upgrade workato-agent
```

**Linux RPM package**

```shell
% sudo yum upgrade workato-agent.x86_64
```

The service should automatically stop, upgrade and restart for systemd-based distributions. If the service doesn't start, you must start it manually.

> **NON-US DATA CENTERS**
> 
> Workato no longer publishes data center-specific OPA versions. Packages with the suffixes `-eu`, `-sg`, `-jp`, and `-au` still function but are no longer supported.
> 
> To upgrade a data center-specific agent, uninstall the old package and [install the latest version](/en/on-prem/groups/add-agent) of the single package distribution. You can retain the `conf` and `lib_ext` folders.

## Upgrade an existing agent older than 2.15.0 and configure connections directly in Workato

Beginning with on-prem agent [version 2.15.0](/en/on-prem/agents/versions#v2-15), Workato introduced [cloud profiles](/en/on-prem/agents/connection#cloud-profile), which allow you to configure connections directly in Workato instead of through the `config.yml` file.

Complete the following steps to upgrade an agent older than version 2.15.0 to a new version that uses cloud profiles:

1. [Create a new on-prem group.](/en/on-prem/groups/create-group)
   
2. Open the new on-prem group and [install a new agent](/en/on-prem/groups/add-agent) on the same machine as your existing agent.
   
3. Set up the required connections directly in Workato. Ensure you can successfully connect using the new on-prem agent.
   
4. Clone or edit your recipes and switch them to the new cloud profile agent. Ensure all recipe connections are updated.
   
5. Go to the old agent's **Version** column, click **...** (ellipsis), and then select **Disable agent**. Alternatively, for agents installed on Windows machines, you can stop the old agent by terminating the **Workato Agent** Windows service or the console-based agent. The new agent continues processing incoming jobs.
   
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
      
   
   ![Disable agent](/assets/disable-agent.XkiFyUDi.png)_Disable the old agent in Workato._
   

If you need any help with the upgrade process, reach out to your Workato account representative for assistance.

---
