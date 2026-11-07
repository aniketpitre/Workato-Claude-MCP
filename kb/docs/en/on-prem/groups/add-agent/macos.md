---
url: 'https://docs.workato.com/en/on-prem/groups/add-agent/macos.md'
description: >-
  Install a Workato on-prem agent (OPA) on Mac to connect on-premises apps and
  databases to your recipes.
---

# Install an on-prem agent on Mac

Complete the following steps to install an on-prem agent (OPA) on a Mac operating system (OS):

> **PREREQUISITES**
> 
> You must [create an on-prem group](/en/on-prem/groups/create-group) before you can set up an on-prem agent.

1. Sign in to your Workato account.
   
2. Go to **Tools > On-prem groups** and select the group where you plan to add an agent.
   
3. Click **Add agent**. The Add agent dialog opens.
   
4. Provide an **Agent name**, use the **Operating system** drop-down menu to select **Mac**, and then click **Next**.
   
   ![Select Mac](/assets/macos-example.BQCfotzO.png)_Select Mac as your operating system_
   
5. Click **Download agent package** and then click **Next**. This downloads the required Mac package to your machine as a `.tar.gz` archive file.
   
6. Extract the package into the folder you plan to use for your configuration.
   
7. Open the folder that contains the download package in terminal.
   
8. Copy and paste the **Activation command** from Workato into the terminal and run it. The agent key and certificate are automatically created in the agent package.
   
   > **AGENT ACTIVATION USING A PROXY**
   > 
   > You must add the `--proxy-host=<host-ip-address>` and `--proxy-port=<port number>` parameters to the **Activation command** if you're using a proxy. Refer to the [Set up proxy access for your on-prem agent](/en/on-prem/agents/proxy) guide for more information.
   > 
   > Run the `activate` script with the `--help` parameter to display the list of accepted input properties.
   
   ![Copy and paste the Activation command](/assets/mac-activation.DcT3Qvxq.png)_Copy and paste the Activation command_
   
   > **CODE IS VALID FOR ONE HOUR**
   > 
   > The code is valid for one hour. Click **Regenerate code** to generate a new code if it expires.
   
   > **ALLOW TRAFFIC TO WORKATO FROM YOUR SERVER**
   > 
   > Ensure traffic to Workato is allowed from your server to use OPA. Refer to [security allowlists](/en/security/ip-allowlists#traffic-to-workato) to add Workato to your allowlist.
   
9. Return to your Workato On-prem window and click **Next**.
   
10. Use the following command to run the on-prem agent, replacing `<YOUR_DIRECTORY>` with the directory name:
    
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
    
    ![Run the on-prem agent](/assets/mac-run-agent.CpGvjnw0.png)_Run the on-prem agent_
    
11. Click **Next**.
    
12. Click **Test agent** to confirm that your on-prem agent is working as expected.
    
    ![Test the on-prem agent](/assets/mac-test-agent.DVIUFgf7.png)_Test the on-prem agent_
    
13. Click **Done** to complete the installation.
    

> **PRIVATE KEY**
> 
> Workato doesn't have access to your private key file (`cert.key`) in the OPA `conf` folder. Ensure you protect this file from unauthorized access.

---
