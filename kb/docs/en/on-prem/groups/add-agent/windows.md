---
url: 'https://docs.workato.com/en/on-prem/groups/add-agent/windows.md'
description: >-
  Install a Workato on-prem agent (OPA) on Windows to connect on-premises apps
  and databases to your recipes.
---

# Install an on-prem agent on Windows

Refer to the information on this page to install an on-prem agent using Windows package.

> **PREREQUISITES**
> 
> You must [create an on-prem group](/en/on-prem/groups/create-group) before you can set up an on-prem agent.

Complete the following steps to create an on-prem agent (OPA) for a Windows operating system (OS):

1. Sign in to your Workato account.
   
2. Go to **Tools > On-prem groups** and select the group where you plan to add an agent.
   
3. Click **Add agent**. The **Add agent** dialog opens.
   
4. Provide an **Agent name**, use the **Operating system** drop-down menu to select **Windows**, and then click **Next**.
   
   ![Select Windows](/assets/windows-select-os.eI4n6XDp.png)_Select Windows as your operating system_
   
5. Click **Download installer** and click **Next**.
   
   ![Download agent package](/assets/windows-download-installer.ps7UsM4C.png)_Click Download agent package_
   
6. Run the installer. The installer creates a Workato group in the **Start** menu, and installs a Windows service called `Workato on-prem agent` by default.
   
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
   
7. Select where to store the agent private key and certificate:
   
   - **Windows Certificate Store**: Stores the private key and certificate in the system-managed certificate store. Access requires appropriate Windows permissions on both the certificate store and private key. This is the default option.
   - **File system**: Stores the private key and certificate in the `C:\Program Files\Workato Agent\conf` folder. You must [protect the `conf` folder from unauthorized access](#how-to-set-permissions) if you select this option as your storage location. This option is only available in OPA versions [30.0](/en/on-prem/agents/versions#v30) and later. Refer to the [Security](/en/on-prem/groups/add-agent/windows#security) section for more information.
   
   > **CERTIFICATE NOT FOUND**
   > 
   > You may encounter a `Certificate not found` error when activating the agent with **Windows Certificate Store** selected. This is typically caused by insufficient permissions to access the certificate store on your machine. You can resolve this issue by storing the key and certificate in the file system or updating your Windows account permissions.
   
   ![Choose where to store OPA key and certificate](/assets/windows-security.Qc0qhBoT.png)_Choose where to store OPA key and certificate_
   
8. Copy and paste the **Activation command** from Workato. The code is valid for one hour. Click **Regenerate code** to generate a new code if it expires.
   
   Alternatively, you can select **Activate agent manually** and activate the OPA after installation using the activation script.
   
   Activate an agent after installation
   
   Complete the following steps to activate the agent using a command script:
   
   1. Go to the `bin` folder inside your OPA installation folder. `C:\Program Files\Workato Agent` is the default path for Windows.
      
   2. Run the `activate.cmd` script. Refer to the [Set up proxy access for your on-prem agent](/en/on-prem/agents/proxy) page to configure the `activate.cmd` script for use with a proxy.
      
      You can run the `activate.cmd` script with the `--help` parameter to display the full list of accepted input properties.
      
   3. Provide the **Activation command** from Workato's OPA setup wizard when prompted. The code is valid for one hour. Click **Regenerate code** in the setup wizard to generate a new code if it expires.
      
   
   ![Copy and paste the Activation code](/assets/windows-activation.CHMwuD3e.png)_Copy and paste the **Activation code**_
   
   > **ALLOW TRAFFIC TO WORKATO FROM YOUR SERVER**
   > 
   > Ensure traffic to Workato is allowed from your server to use OPA. Refer to [security allowlists](/en/security/ip-allowlists#traffic-to-workato) to add Workato to your allowlist.
   
9. Return to Workato and click **Next**.
   
10. Click **Test agent** to confirm that your on-prem agent is working as expected.
    
    ![Test the on-prem agent](/assets/windows-test-agent.CeNvEOTo.png)_Test the on-prem agent_
    
11. Click **Done** to complete the installation.
    

> **CERTIFICATE VALIDITY PERIOD**
> 
> The agent certificate remains valid for 1 year after the generation date.
> 
> Renew the certificate before its expiration date to avoid interruptions. Refer to the [Renew agent keys](/en/on-prem/agents/key#renew-agent-keys) guide for more information.

## Security

OPA [2.18.0](/en/on-prem/agents/versions#v2-18) and later versions run the OPA Windows service under the `Local Service` system account by default. You can alter this account to better match your security requirements, for example, by running it under a domain user account with dedicated privileges.

OPA [30.0](/en/on-prem/agents/versions#v30) and later versions enable you to choose whether to store the agent private key (`cert.key`) and certificate (`cert.pem`) in the `conf` folder or the Windows Certificate Store. The default storage location is the Windows Certificate Store.

It's _extremely important_ to restrict access to the OPA `conf` folder if you store the private key and certificate in the local file system. Workato doesn't have access to your private key.

The `conf` folder also contains a `config.yml` file where you can configure options and [connection properties](/en/on-prem/agents/connection/profile) if you aren't using [cloud profiles](/en/on-prem/agents/connection/cloud). Ensure you protect this file from unauthorized access.

### How to set permissions

Complete the following steps to protect the OPA's `conf` folder:

1. Right-click the `conf` folder and select **Properties**.
   
2. Go to the **Security** tab.
   
3. Click **Advanced** and remove any unnecessary explicit or implicit access to the `conf` folder.
   
4. Explicitly allow **Read** access to the `conf` folder for the `LOCAL SERVICE` system account (or the account assigned to run OPA as a Windows service).
   
   ![OPA conf directory permissions](/assets/opa-permissions.whGVFXAi.png)_OPA conf directory permissions_
   
5. Click **Apply**.

---
