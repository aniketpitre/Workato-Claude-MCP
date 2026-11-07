---
url: 'https://docs.workato.com/en/on-prem/groups/add-agent/linux-deb.md'
description: >-
  Install a Workato on-prem agent on Debian or Ubuntu using the DEB Linux
  package, run as the workato system user.
---

# Install an on-prem agent using the DEB Linux package

Complete the following steps to install an on-prem agent using the DEB Linux package on operating systems such as Debian and Ubuntu:

> **PREREQUISITES**
> 
> You must complete the following prerequisites to install an on-prem agent using the DEB Linux package:
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
   
4. Provide an **Agent name**, use the **Operating system** drop-down menu to select **Linux**, and use the **Installation method** drop-down menu to select **DEB package**. ![Choose OS](/assets/select-linux-deb.k8SWn-LA.png)_Choose OS_
   
5. Click **Next**.
   
6. Open the terminal and run the following commands to install the agent:
   
   Install the agent
   
   1. Run the following command to create the APT config file and add the Workato repository to the APT sources list:
      
      ```shell
      echo 'deb [ signed-by=/usr/share/keyrings/workato.gpg ] https://workato-public.s3.amazonaws.com/DAA34553/repo/deb/ stable main' | sudo tee /etc/apt/sources.list.d/workato.list
      ```
      
   2. Run the following command to import the Workato GPG public key and save it as a keyring file for repository validation:
      
      ```shell
      wget -qO - 'https://workato-public.s3.amazonaws.com/DAA34553/repo/archive.key' | sudo gpg -o /usr/share/keyrings/workato.gpg --dearmor
      ```
      
   3. Run the following command to update the APT package cache:
      
      ```shell
      sudo apt-get update
      ```
      
      The output should look similar to the following:
      
      ```shell
      Hit:1   jammy InRelease
      Get:2   jammy-updates InRelease [109 kB]
      Get:3   jammy-backports InRelease [99.8 kB]
      Hit:4 https://workato-public.s3.amazonaws.com/repo/deb stable InRelease
      Get:5   jammy-security InRelease [110 kB]
      Get:6   jammy-updates/main amd64 Packages [277 kB]
      Get:7   jammy-updates/universe amd64 Packages [116 kB]
      Get:8   jammy-updates/universe Translation-en [40.1 kB]
      Get:9   jammy-updates/universe amd64 c-n-f Metadata [2344 B]
      Get:10   jammy-security/universe amd64 c-n-f Metadata [1128 B]
      Fetched 756 kB in 1s (1107 kB/s)
      Reading package lists... Done
      ```
      
   4. Run the following command to find the Workato agent for your [data center](/en/datacenter/datacenter-overview) if your OPA version is earlier than [v26.0](/en/on-prem/agents/versions#v26-0):
      
      ```shell
      sudo apt-cache search workato
      ```
      
      The output should look similar to the following:
      
      ```shell
      workato-agent - workato-agent
      workato-agent-eu - workato-agent-eu
      workato-agent-jp - workato-agent-jp
      workato-agent-sg - workato-agent-sg
      workato-agent-au - workato-agent-au
      ```
      
        
      
      > **DATA CENTER-SPECIFIC PACKAGES ARE DEPRECATED**
      > 
      > From [OPA v26.0](/en/on-prem/agents/versions#v26-0) onward, the on-prem agent is available as a single package for all data centers. Packages with suffixes `-eu`, `-sg`, `-jp`, and `-au` still function but are no longer supported.
      > 
      > To upgrade a data center-specific agent, uninstall the old package and [install the latest version](/en/on-prem/groups/add-agent) of the single package distribution. You can retain the `conf` and `lib_ext` folders.
      
   5. Install the agent using the following command:
      
      ```shell
      sudo apt install workato-agent
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
