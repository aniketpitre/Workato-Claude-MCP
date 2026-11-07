---
url: 'https://docs.workato.com/en/on-prem/groups/add-agent/linux-rpm.md'
description: >-
  Install a Workato on-prem agent on Red Hat, Fedora, or CentOS using the RPM
  Linux package, run as the workato system user.
---

# Install an on-prem agent using the RPM Linux package

Complete the following steps to install an on-prem agent using the RPM Linux package on operating systems such as Red Hat, Fedora, and Centos:

> **PREREQUISITES**
> 
> You must complete the following prerequisites to install an on-prem agent using the RPM Linux package:
> 
> - Obtain `sudo` privileges on the machine where you plan to install the agent.
> - Ensure traffic to Workato is allowed from your server. Refer to [security allowlists](/en/security/ip-allowlists#traffic-to-workato) to add Workato to your allowlist.
> - [Create an on-prem group](/en/on-prem/groups/create-group).

> **USE THE WORKATO SYSTEM USER**
> 
> The OPA installer automatically creates a `workato` system user. Workato strongly recommends running set up commands as this system user to avoid permission errors during activation. Refer to the [On-prem setup & installation issues](/en/on-prem/agents/opa-troubleshooting/troubleshoot-setup#linux) guide for more information.

1. Sign in to your Workato account.
   
2. Go to **Tools > On-prem groups** and select the group where you plan to activate the agent.
   
3. Click **Add new agent**. The **Add agent** dialog opens.
   
4. Provide an **Agent name**, use the **Operating system** drop-down menu to select **Linux**, and use the **Installation method** drop-down menu to select **RPM package**. ![Choose OS](/assets/select-linux-rpm.DX4TOLB-.png)_Choose OS_
   
5. Click **Next**.
   
6. **yum installation**
   
   Complete the following steps to install the agent using yum:
   
   1. Create a `workato.repo` file in the `/etc/yum.repos.d/` directory with the following content to add Workato to the yum repository list:
      
      ```shell
      [workato-x86_64]
      name=Workato RPM Repo
      baseurl=https://workato-public.s3.amazonaws.com/DAA34553/repo/rpm/x86_64/
      enabled=1
      gpgkey=https://workato-public.s3.amazonaws.com/DAA34553/repo/archive.key
      gpgcheck=1
      ```
      
   2. Run the following command to update the yum package cache and confirm that the Workato repository was added successfully:
      
      ```shell
      sudo yum makecache
      ```
      
      The output should look similar to the following:
      
      ```shell
      Updating Subscription Management repositories.
      Unable to read consumer identity
      This system is not registered with an entitlement server. You can use subscription-manager to register.
      Red Hat Update Infrastructure 3 Client Configuration Server 8 HA                         49 kB/s | 2.0 kB     00:00
      Red Hat Enterprise Linux 8 for x86_64 - AppStream from RHUI (RPMs)                       79 kB/s | 4.5 kB     00:00
      Red Hat Enterprise Linux 8 for x86_64 - BaseOS from RHUI (RPMs)                          74 kB/s | 4.1 kB     00:00
      Red Hat Enterprise Linux 8 for x86_64 - High Availability (RPMs) from RHUI               71 kB/s | 4.0 kB     00:00
      Red Hat Ansible Engine 2 for RHEL 8 (RPMs) from RHUI                                     67 kB/s | 4.0 kB     00:00
      Workato RPM Repo
      Metadata cache created.
      ```
      
   3. Run the following command to find the Workato agent for your [data center](/en/datacenter/datacenter-overview) if your OPA version is earlier than [v26.0](/en/on-prem/agents/versions#v26-0):
      
      ```shell
      sudo yum search workato
      ```
      
      The output should look similar to the following:
      
      ```shell
      Updating Subscription Management repositories.
      Unable to read consumer identity
      This system is not registered with an entitlement server. You can use subscription-manager to register.
      Last metadata expiration check: 0:00:44 ago on Thu 09 Nov 2022 10:25:51 AM UTC.
      =========================================== Name & Summary Matched: workato ============================================
      workato-agent.x86_64 : workato-agent
      ```
      
        
      
      > **DATA CENTER-SPECIFIC PACKAGES ARE DEPRECATED**
      > 
      > From [OPA v26.0](/en/on-prem/agents/versions#v26-0) onward, the on-prem agent is available as a single package for all data centers. Packages with suffixes `-eu`, `-sg`, `-jp`, and `-au` still function but are no longer supported.
      > 
      > To upgrade a data center-specific agent, uninstall the old package and [install the latest version](/en/on-prem/groups/add-agent) of the single package distribution. You can retain the `conf` and `lib_ext` folders.
      
   4. Install the agent using the following command:
      
      ```shell
      sudo yum install workato-agent.x86_64
      ```
      
   
   **zypper installation**
   
   Complete the following steps in the CLI to install the agent using zypper:
   
   1. Import the Workato repository into zypper:
      
      ```shell
      sudo zypper addrepo --check --gpgcheck https://workato-public.s3.amazonaws.com/DAA34553/repo/rpm/x86_64/ workato
      ```
      
   2. Install curl, if it's not already installed:
      
      ```shell
      sudo zypper install curl
      ```
      
   3. Download and import the Workato GPG key:
      
      ```shell
      curl -LO https://workato-public.s3.amazonaws.com/DAA34553/repo/archive.key
      ```
      
   4. Refresh your repositories:
      
      ```shell
      sudo zypper refresh
      ```
      
   5. Install the agent:
      
      ```shell
      sudo zypper install workato-agent
      ```
      
   
7. Return to Workato and click **Next**.
   
8. Copy the command provided by the wizard and run it in the directory where the agent is installed. This automatically creates the agent key and certificate in the agent package. We strongly recommend you run this command as the `workato` system user to avoid permission errors. Refer to the [On-prem setup & installation issues](/en/on-prem/agents/opa-troubleshooting/troubleshoot-setup#linux) guide for more information.
   
   The activation code is valid for one hour. Click **Regenerate code** to generate a new code if it expires.
   
   ![Activate](/assets/activate-linux.BWFoVrYC.png)_Activate_
   
   > **AGENT ACTIVATION USING A PROXY**
   > 
   > You must add the `--proxy-host=<host-ip-address>` and `--proxy-port=<port number>` parameters to the **Activation command** if you're using a proxy. Refer to the [Set up proxy access for your on-prem agent](/en/on-prem/agents/proxy) guide for more information.
   > 
   > Run the `activate` script with the `--help` parameter to display the list of accepted input properties.
   
   > **CERTIFICATE VALIDITY PERIOD**
   > 
   > The agent certificate remains valid for 1 year after the generation date.
   > 
   > Renew the certificate before its expiration date to avoid interruptions. Refer to the [Renew agent keys](/en/on-prem/agents/key#renew-agent-keys) guide for more information.
   
9. Return to Workato and click **Next**.
   
10. Use the following command to start the agent service in the background:
    
    ```shell
    sudo systemctl start workato-agent.service
    ```
    
11. Optional. Use the following command to enable the agent to start automatically:
    
    ```shell
    sudo systemctl enable workato-agent.service
    ```
    
12. Return to Workato and click **Next**.
    
13. Click **Test agent** to confirm that your on-prem agent is working as expected.
    
    ![Click Test agent](/assets/linux-test-agent-setup.CL7LT58k.png)_Click **Test agent**_
    
14. Click **Done** to complete the setup.
    

> **PRIVATE KEY**
> 
> Workato doesn't have access to your private key file (`cert.key`) in the OPA `conf` folder. Ensure you protect this file from unauthorized access.

---
