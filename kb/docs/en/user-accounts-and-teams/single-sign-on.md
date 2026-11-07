---
url: 'https://docs.workato.com/en/user-accounts-and-teams/single-sign-on.md'
description: >-
  Set up SAML-based Single Sign-On for a Workato workspace to provide authorized
  access for members and enable just-in-time provisioning.
---

# Enable Single Sign-On for a Workato workspace

Workato supports authentication using SAML-based Single Sign-On (SSO), allowing you to provide authorized access to Workato for multiple workspace members.

You can use [just-in-time (JIT) provisioning](/en/user-accounts-and-teams/just-in-time-provisioning) to eliminate pre-provisioning Workato accounts.

> **ENFORCE SAML AUTHENTICATION**
> 
> You can enforce SAML SSO for your workspace. When you do so, all workspace members (except for the workspace account owner) must authenticate through your identity provider. They cannot access the workspace and its resources by logging in with a Workato username and password.
> 
> Note that the account owner of the workspace cannot use SAML-based SSO to authenticate with the workspace. They must sign in with their username and password instead.

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

* * *

## Prerequisites

You must have the following information to configure SSO for Workato:

- SAML SSO privileges in Workato.
  
- Knowledge of which Workato [data center](/en/datacenter/datacenter-overview) supports your account. The values for some configuration settings vary depending on your account's data center.
  
  Refer to the following data center URLs for configuring a SAML app:
  
  - **Workato Enterprise customers:**
    
    - [US Data Center (USDC)](/en/datacenter/datacenter-overview#us-data-center): `https://www.workato.com`
    - [European Union Data Center (EUDC)](/en/datacenter/datacenter-overview#european-union-data-center): `https://app.eu.workato.com`
    - [Japan Data Center (JPDC)](/en/datacenter/datacenter-overview#japan-data-center): `https://app.jp.workato.com`
    - [Singapore Data Center (SGDC)](/en/datacenter/datacenter-overview#singapore-data-center): `https://app.sg.workato.com`
    - [Australia Data Center (AUDC)](/en/datacenter/datacenter-overview#australia-data-center): `https://app.au.workato.com`
    - [Israel Data Center (ILDC)](/en/datacenter/datacenter-overview#israel-data-center): `https://app.il.workato.com`
    - [China Data Center (CNDC)](/en/datacenter/datacenter-overview#china-data-center): `https://app.workatoapp.cn`
    - [South Korea Data Center (KRDC)](/en/datacenter/datacenter-overview#korea-data-center): `https://app.kr.workato.com`
    - [United Kingdom Data Center (UKDC)](/en/datacenter/datacenter-overview#uk-data-center): `https://app.uk.workato.com`
  - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
    
    - [Self-service Data Center](/en/datacenter/datacenter-overview#self-service): `https://app.trial.workato.com`
- Privileges in your SAML provider that enable you to complete the following actions:
  
  - Create and modify SAML applications.
  - Assign applications to users.

* * *

## Step 1: Create a Workato SAML application

You must create a SAML application for dedicated Workato use in your SAML provider to enable SSO for Workato.

Locate the instructions for your SAML provider to get started:

- [Google Workspace](/en/user-accounts-and-teams/single-sign-on#google-g-suite-single-sign-on)
- [Microsoft Entra ID](/en/user-accounts-and-teams/single-sign-on#azure-ad-single-sign-on)
- [CyberArk Identity](/en/user-accounts-and-teams/single-sign-on#cyberark-idaptive-single-sign-on)
- [Okta](/en/user-accounts-and-teams/single-sign-on#okta-single-sign-on)
- [OneLogin](/en/user-accounts-and-teams/single-sign-on#onelogin-single-sign-on)

> **KNOW YOUR WORKATO DATA CENTER?**
> 
> Verify which [data center](/en/datacenter/datacenter-overview) your Workato account is in before proceeding.
> 
> Make sure to use the SSO URLs for your data center when setting up your SAML application.

### Google Workspace

VIEW GOOGLE WORKSPACE INSTRUCTIONS

Refer to the [Google Workspace Admin documentation](https://support.google.com/a/answer/6087519?hl=en) for more details.

> **FEATURE AVAILABILITY**
> 
> Google Workspace isn't available as an IdP for workspaces in the China data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

#### In Workato

1. Go to **Workspace admin > Settings > Login methods**.
   
2. Use the **Authentication method** drop-down menu to select **SAML based SSO**.
   
3. Provide a **Workspace handle** for the workspace. The maximum length is 20 characters. Workato converts any uppercase letters you enter in this field to lowercase.
   
4. Use the **SAML provider** drop-down menu to select **Other SAML IdP**.
   
5. Copy the **Service provider (SP) entity ID**.
   
   ![Retrieve entity ID](/assets/retrieve-entity-id.x-dtZ70U.png)_Retrieve entity ID_
   

#### In your Google Admin console

1. Go to **Apps > Web and mobile apps**.
   
2. Click **Add App > Add custom SAML app**.
   
3. Go to the **Service Provider Details** section and provide the following configuration information:
   
   - **ACS URL**
     - Use the URL for your Workato data center.
     - **Workato Enterprise customers:**
       - US data center: `https://www.workato.com/saml/consume`
       - EU data center: `https://app.eu.workato.com/saml/consume`
       - JP data center: `https://app.jp.workato.com/saml/consume`
       - SG data center: `https://app.sg.workato.com/saml/consume`
       - AU data center: `https://app.au.workato.com/saml/consume`
       - IL data center: `https://app.il.workato.com/saml/consume`
     - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
       - Self-service data center: `https://app.trial.workato.com/saml/consume`
   - **Entity ID**
     - Enter the [Service provider (SP) entity ID](/en/user-accounts-and-teams/single-sign-on#sp-entity-id) obtained from Workato.
   - **Start URL**
     - Optional. This sets the RelayState parameter in a SAML request, which can be a URL to redirect users to after authentication. We recommend leaving this field empty, or providing the final destination to which you plan to direct users.
4. Finish configuring the app and defining settings as needed.
   

Complete [the set up](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup) in Workato.

### Microsoft Entra ID

VIEW MICROSOFT ENTRA ID INSTRUCTIONS

Follow the Microsoft documentation for a complete step-by-step guide on [Enable SAML single sign-on for an enterprise application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-setup-sso).

#### In your Workato account

1. Go to **Workspace admin > Settings > Login methods**.
   
2. Select **SAML based SSO** in the **Authentication method** menu.
   
3. Fill in the **Workspace handle** field. The maximum length is 20 characters. Workato converts any uppercase letters you enter in this field to lowercase.
   
4. Select **Azure Active Directory** (Microsoft Entra ID) in the **SAML provider** menu.
   
5. Copy the **Service provider (SP) entity ID**:
   
   ![Retrieve entity ID](/assets/azure-active-directory-setting.fiXnLC9Q.png)_Retrieve entity ID_
   

#### In your Azure portal

1. Create a **Non-gallery application** to connect Microsoft Entra ID SSO to Workato:
   
   - Select **Microsoft Entra ID** > **Enterprise applications**.
   - Create a **New application** and choose **Non-gallery application**.
   
   Refer to the [Enable SAML single sign-on for an enterprise application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-setup-sso) for more details.
   
2. Go to the new application's **Single sign-on** tab and select **SAML**.
   
3. Fill in the configuration details as follows:
   
   - **Identifier (Entity ID)**
     - Enter the [Service provider (SP) entity ID](/en/user-accounts-and-teams/single-sign-on#azure-sp-entity-id) obtained from Workato.
   - **Reply URL (Assertion Consumer Service URL)**
     - Use the URL for your Workato data center.
     - **Workato Enterprise customers:**
       - US data center: `https://www.workato.com/saml/consume`
       - EU data center: `https://app.eu.workato.com/saml/consume`
       - JP data center: `https://app.jp.workato.com/saml/consume`
       - SG data center: `https://app.sg.workato.com/saml/consume`
       - AU data center: `https://app.au.workato.com/saml/consume`
       - IL data center: `https://app.il.workato.com/saml/consume`
       - CN data center: `https://app.workatoapp.cn/saml/consume`
     - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
       - Self-service data center: `https://app.trial.workato.com/saml/consume`
   - **Sign on URL**
     - Locate your **Workspace handle** in Workato. Then, configure the URL for the data center you use. Replace `{WORKSPACE_HANDLE}` in the following URL with your actual workspace handle.
     - **Workato Enterprise customers:**
       - US data center: `https://www.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
       - EU data center: `https://app.eu.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
       - JP data center: `https://app.jp.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
       - SG data center: `https://app.sg.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
       - AU data center: `https://app.au.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
       - IL data center: `https://app.il.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
       - CN data center: `https://app.workatoapp.cn/saml/init?team_handle={WORKSPACE_HANDLE}`
     - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
       - Self-service data center: `https://app.trial.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
   
   ![Azure SAML Configuration](/assets/azure-saml-config-sign-on-url.Dp5FEqs8.png)_Azure SAML Configuration_
   
4. Click **Save**.
   

You must configure the **Attributes & Claims** section to ensure email addresses are transformed to lowercase after saving the SAML configuration. This prevents case-sensitive login issues. Complete the following steps to configure **Attributes & Claims**:

1. Go to the **Attributes & Claims** section.
   
2. Click **Edit**.
   
3. Click **Unique User Identifier (Name ID)** to open and edit the required claim.
   
   ![Edit required claim](/assets/edit-required-claim.BarSZLrg.png)_Edit required claim_
   
4. Set the **Source** to **Transformation** on the **Manage claim** page.
   
   ![Set source](/assets/set-source.BXMKceOK.png)_Set the source_
   
5. Choose `ToLowercase()` from the **Transformation** drop-down menu on the **Manage transformation** page.
   
   ![Select your transformation](/assets/select-transformation.DWyj6Vdv.png)_Select your transformation_
   
6. Select **Attribute** as the parameter.
   
7. Enter `user.mail` in the **Attribute name** field.
   
8. Click **Add** to add the transformation.
   
9. Click **Save** to complete the configuration.
   

Next, obtain your **Microsoft Entra ID Metadata URL**. This is required to complete the [SSO setup in Workato](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup).

1. Go to the **Single sign-on** tab and locate the **SAML Certificate** details.
   
2. Copy the **App Federation Metadata URL**.
   
   ![Microsoft Entra ID metadata URL](/assets/azure-saml-config-app-metadata.DnlUTx58.png)_Microsoft Entra ID metadata URL_
   

After you've finished the preceding steps, proceed to [the next step](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup) to complete the setup.

### CyberArk Identity

VIEW CYBERARK IDENTITY INSTRUCTIONS

#### In CyberArk Identity

1. Sign in to your CyberArk Identity admin console.
   
2. Go to the **Apps & Widgets** sidebar and select **Add custom SAML app**.
   
3. Name the application Workato.
   
4. Click **Trust** to configure SAML Settings.
   
5. Go to the **Service Provider Configuration** section and select **Manual Configuration**.
   
6. Provide the SAML settings as follows:
   
   - **Audience**
     - Use the URL for your Workato data center.
     - **Workato Enterprise customers:**
       - US data center: `https://www.workato.com/saml/metadata`
       - EU data center: `https://app.eu.workato.com/saml/metadata`
       - JP data center: `https://app.jp.workato.com/saml/metadata`
       - SG data center: `https://app.sg.workato.com/saml/metadata`
       - AU data center: `https://app.au.workato.com/saml/metadata`
       - IL data center: `https://app.il.workato.com/saml/metadata`
       - CN data center: `https://app.workatoapp.cn/saml/metadata`
     - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
       - Self-service data center: `https://app.trial.workato.com/saml/metadata`
   - **Recipient**
     - Use the URL for your Workato data center.
     - **Workato Enterprise customers:**
       - US data center: `https://www.workato.com/saml/consume`
       - EU data center: `https://app.eu.workato.com/saml/consume`
       - JP data center: `https://app.jp.workato.com/saml/consume`
       - SG data center: `https://app.sg.workato.com/saml/consume`
       - AU data center: `https://app.au.workato.com/saml/consume`
       - IL data center: `https://app.il.workato.com/saml/consume`
       - CN data center: `https://app.workatoapp.cn/saml/consume`
     - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
       - Self-service data center: `https://app.trial.workato.com/saml/consume`
   - **ACS (Consumer) URL Validator**
     - Use the URL for your Workato data center.
     - **Workato Enterprise customers:**
       - US data center: `^https:\/\/www.workato.com\/saml\/*$`
       - EU data center: `^https:\/\/app.eu.workato.com\/saml\/*$`
       - JP data center: `^https:\/\/app.jp.workato.com\/saml\/*$`
       - SG data center: `^https:\/\/app.sg.workato.com\/saml\/*$`
       - AU data center: `^https:\/\/app.au.workato.com\/saml\/*$`
       - IL data center: `^https:\/\/app.il.workato.com\/saml\/*$`
       - CN data center: `^https:\/\/app.workatoapp.cn\/saml\/*$`
     - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
       - Self-service data center: `^https:\/\/app.trial.workato.com\/saml\/*$`
   - **ACS (Consumer) URL**
     - Use the URL for your Workato data center.
     - **Workato Enterprise customers:**
       - US data center: `https://www.workato.com/saml/consume`
       - EU data center: `https://app.eu.workato.com/saml/consume`
       - JP data center: `https://app.jp.workato.com/saml/consume`
       - SG data center: `https://app.sg.workato.com/saml/consume`
       - AU data center: `https://app.au.workato.com/saml/consume`
       - IL data center: `https://app.il.workato.com/saml/consume`
       - CN data center: `https://app.workatoapp.cn/saml/consume`
     - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
       - Self-service data center: `https://app.trial.workato.com/saml/consume`
7. Select **Assertion**.
   
8. Leave other settings as the default unless otherwise specified by your Workato implementation details.
   
   ![Metadata URL Configuration 2](/assets/metadata-updated.C4cDX4TH.png)_CyberArk Identity service provider configuration_
   
9. Click **Save**.
   

After saving the basic SAML configuration, you must configure user account mapping to ensure email addresses are lowercase:

1. Go to the **Account Mapping** page.
   
2. Select the **Account Mapping Script** option.
   
3. Add the following custom JavaScript to map the login email to lowercase:
   
   ```
   LoginUser.Username = LoginUser.Get('mail').toLowerCase();
   ```
   
   This script retrieves the user's email from the `mail` attribute in Active Directory, converts it to lowercase, and assigns it as the `LoginUser.Username`. This ensures consistency and prevents case-sensitive login issues in Workato.
   
4. Click **Test** to verify the script.
   
   ![Verify the script](/assets/verify-script.D8nRjFoz.png)_Verify the script_
   
5. Click **Save** to apply the account mapping changes.
   

After you configure account mapping, complete the following steps to finalize the SAML setup:

1. Locate and copy the **Metadata URL** provided by CyberArk Identity. This is required to complete the [SSO setup in Workato](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup).
   
   ![Metadata URL Configuration](/assets/metadata-1.Cb2O48vf.png)_CyberArk Identity metadata URL configuration_
   
2. Obtain your **Identity provider single sign-on URL**, **Identity provider issuer**, and **Signing certificate** from CyberArk Identity. These values are required to complete the [SSO setup in Workato](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup).
   
3. Deploy the Workato SAML app to make it available to users in CyberArk Identity.
   
4. Go to the **Permissions** section in your CyberArk Identity admin console.
   
5. Click **Add** and select a user, typically a system administrator responsible for app deployment.
   
6. Click **Save** to deploy the Workato SAML app.
   

You must assign role permissions to the Workato SAML app so that users can access Workato. Complete the following steps to assign role permissions:

1. Go to **Core Services > Roles** in your CyberArk Identity admin console.
   
2. Select **Add Role** and name the role `Workato Users` to define permissions for users using Workato.
   
3. Go to **Assigned Applications**, locate the Workato SAML app, and click **Add** to associate it with the `Workato Users` role.
   
4. Click **Save** to confirm the role assignments and complete the setup process.
   
   ![Assign app to roles](/assets/assigned-app-add.Dy1hfsH0.png)_Assign the Workato SAML app to roles_
   
5. Users assigned the `Workato Users` role can find the Workato SAML app in their CyberArk Identity user portal. Clicking this app enables them to sign in to Workato and automatically provisions their account.
   

After you've finished the preceding steps, continue to [the next step](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup) to complete the setup in Workato.

### Okta

VIEW OKTA INSTRUCTIONS

#### In Okta

1. Sign in to your Okta instance.
   
2. Go to **Applications > Applications**.
   
3. Click **Create App Integration**.
   
   ![Add application on Okta](/assets/okta-saml-config-new-app-integration.CvmRcMJy.png)_Add application on Okta_
   
   Refer to the [Okta documentation](http://developer.okta.com/standards/SAML/setting_up_a_saml_application_in_okta) for more information.
   
4. Select **SAML 2.0** for the **Sign on method**.
   
   ![Create a new application on Okta](/assets/okta-saml-config-create-app.CQarAWjI.png)_Create a new application on Okta_
   
5. Click **Next**.
   
6. Provide an **App name** for your SAML application. This can be any descriptive name (such as "Workato") and doesn't need to match your Workato workspace handle.
   
   ![Provide an App name for your SAML application](/assets/okta-saml-app-name.Cn3QHelR.png)_Provide an **App name** for your SAML application_
   
7. Click **Next** to continue to the SAML configuration settings.
   
8. Provide the **Single Sign-On URL** for your Workato data center:
   
   - **Workato Enterprise customers:**
     - US data center: `https://www.workato.com/saml/consume`
     - EU data center: `https://app.eu.workato.com/saml/consume`
     - JP data center: `https://app.jp.workato.com/saml/consume`
     - SG data center: `https://app.sg.workato.com/saml/consume`
     - AU data center: `https://app.au.workato.com/saml/consume`
     - IL data center: `https://app.il.workato.com/saml/consume`
     - KR data center: `https://app.kr.workato.com/saml/consume`
     - CN data center: `https://app.workatoapp.cn/saml/consume`
     - UK data center: `https://app.uk.workato.com/saml/consume`
   - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
     - Self-service data center: `https://app.trial.workato.com/saml/consume`
9. Select the **Use this for Recipient URL and Destination URL** checkbox.
   
10. Provide the **Audience URI (SP Entity ID)** for your Workato data center.
    
    - **Workato Enterprise customers:**
      - US data center: `https://www.workato.com/saml/metadata`
      - EU data center: `https://app.eu.workato.com/saml/metadata`
      - JP data center: `https://app.jp.workato.com/saml/metadata`
      - SG data center: `https://app.sg.workato.com/saml/metadata`
      - AU data center: `https://app.au.workato.com/saml/metadata`
      - IL data center: `https://app.il.workato.com/saml/metadata`
      - CN data center: `https://app.workatoapp.cn/saml/metadata`
    - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
      - Self-service data center: `https://app.trial.workato.com/saml/metadata`
11. Set **Application username** to **Custom** and enter the following expression to convert user email addresses to lowercase:
    
    ```text
    toLowerCase(user.email)
    ```
    
    ![Set Application username to Custom](/assets/custom-application-name.FmWyRGwN.png)_Set Application username to Custom_
    
12. Optional. Click **Show Advanced Settings**. In the **Other Requestable SSO URLs** field, click **Add Another** and provide the ACS URL for your Workato data center.
    
    - **Workato Enterprise customers:**
      - US data center: `https://www.workato.com/saml/consume`
      - EU data center: `https://app.eu.workato.com/saml/consume`
      - JP data center: `https://app.jp.workato.com/saml/consume`
      - SG data center: `https://app.sg.workato.com/saml/consume`
      - AU data center: `https://app.au.workato.com/saml/consume`
      - IL data center: `https://app.il.workato.com/saml/consume`
      - CN data center: `https://app.workatoapp.cn/saml/consume`
    - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
      - Self-service data center: `https://app.trial.workato.com/saml/consume`
13. Click **Next** and then click **Finish** to complete the SAML application setup.
    
14. Copy the **Metadata URL** from Okta.
    

After you've finished the preceding steps, continue to [the next step](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup) to complete the setup in Workato.

### OneLogin

VIEW ONELOGIN INSTRUCTIONS

#### In OneLogin

1. Sign in to your OneLogin instance.
   
2. Go to **Applications > Applications**.
   
3. Click **Add App**.
   
   ![Add application on OneLogin](/assets/onelogin-add-application.D0sVYSNZ.png)_Add application on OneLogin_
   
4. Search for and select `SAML Test Connector (IdP w/ attr w/ sign response)`.
   
   ![SAML test connector](/assets/onelogin-saml-test-connector.BFeGKN2r.png)_SAML test connector_
   
5. In the **Application details**, fill in the configuration details as follows:
   
   - **Audience**
     - Use the URL for your Workato data center.
     - **Workato Enterprise customers:**
       - US data center: `https://www.workato.com/saml/metadata`
       - EU data center: `https://app.eu.workato.com/saml/metadata`
       - JP data center: `https://app.jp.workato.com/saml/metadata`
       - SG data center: `https://app.sg.workato.com/saml/metadata`
       - AU data center: `https://app.au.workato.com/saml/metadata`
       - IL data center: `https://app.il.workato.com/saml/metadata`
       - CN data center: `https://app.workatoapp.cn/saml/metadata`
     - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
       - Self-service data center: `https://app.trial.workato.com/saml/metadata`
   - **Recipient**
     - Use the URL for your Workato data center.
     - **Workato Enterprise customers:**
       - US data center: `https://www.workato.com/saml/consume`
       - EU data center: `https://app.eu.workato.com/saml/consume`
       - JP data center: `https://app.jp.workato.com/saml/consume`
       - SG data center: `https://app.sg.workato.com/saml/consume`
       - AU data center: `https://app.au.workato.com/saml/consume`
       - IL data center: `https://app.il.workato.com/saml/consume`
       - CN data center: `https://app.workatoapp.cn/saml/consume`
     - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
       - Self-service data center: `https://app.trial.workato.com/saml/consume`
   - **ACS (Consumer) URL Validator**
     - Use the URL for your Workato data center.
     - **Workato Enterprise customers:**
       - US data center: `^https:\/\/www.workato.com\/saml\/*$`
       - EU data center: `^https:\/\/app.eu.workato.com\/saml\/*$`
       - JP data center: `^https:\/\/app.jp.workato.com\/saml\/*$`
       - SG data center: `^https:\/\/app.sg.workato.com\/saml\/*$`
       - AU data center: `^https:\/\/app.au.workato.com\/saml\/*$`
       - IL data center: `^https:\/\/app.il.workato.com\/saml\/*$`
       - CN data center: `^https:\/\/app.workatoapp.cn\/saml\/*$`
     - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
       - Self-service data center: `^https:\/\/app.trial.workato.com\/saml\/*$`
   - **ACS (Consumer) URL**
     - Use the URL for your Workato data center.
     - **Workato Enterprise customers:**
       - US data center: `https://www.workato.com/saml/consume`
       - EU data center: `https://app.eu.workato.com/saml/consume`
       - JP data center: `https://app.jp.workato.com/saml/consume`
       - SG data center: `https://app.sg.workato.com/saml/consume`
       - AU data center: `https://app.au.workato.com/saml/consume`
       - IL data center: `https://app.il.workato.com/saml/consume`
       - CN data center: `https://app.workatoapp.cn/saml/consume`
     - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
       - Self-service data center: `https://app.trial.workato.com/saml/consume`
6. Click **Save**.
   
7. Next, retrieve your **OneLogin Metadata URL**. This is needed to complete the [SSO setup in Workato](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup).
   
   1. On the application's page, click **More Actions**.
   2. Right-click **SAML Metadata** and select **Copy link address**:
   
   ![OneLogin metadata URL](/assets/onelogin-metadata-link.DI52wC1d.gif)_OneLogin metadata URL_
   

After you've finished the preceding steps, proceed to [the next step](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup) to complete the setup.

### Other Identity Providers

OTHER IDENTITY PROVIDERS INSTRUCTIONS

If your Identity Provider (IdP) is not listed, you can still configure SAML-based Single Sign-On (SSO) in Workato using the common SAML 2.0 standard.

Complete the following steps to configure SAML SSO for other Identity Providers:

1. Sign in to your Identity Provider (IdP) and begin setting up a SAML application.
   
2. Provide the **Audience URI (SP Entity ID)** for your Workato data center in the SAML configuration settings.
   
   - **Workato Enterprise customers:**
     - US data center: `https://www.workato.com/saml/metadata`
     - EU data center: `https://app.eu.workato.com/saml/metadata`
     - JP data center: `https://app.jp.workato.com/saml/metadata`
     - SG data center: `https://app.sg.workato.com/saml/metadata`
     - AU data center: `https://app.au.workato.com/saml/metadata`
     - IL data center: `https://app.il.workato.com/saml/metadata`
     - CN data center: `https://app.workatoapp.cn/saml/metadata`
   - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
     - Self-service data center: `https://app.trial.workato.com/saml/metadata`
3. Provide the **ACS URL (Assertion Consumer Service URL)** based on your data center.
   
   - **Workato Enterprise customers:**
     - US data center: `https://www.workato.com/saml/consume`
     - EU data center: `https://app.eu.workato.com/saml/consume`
     - JP data center: `https://app.jp.workato.com/saml/consume`
     - SG data center: `https://app.sg.workato.com/saml/consume`
     - AU data center: `https://app.au.workato.com/saml/consume`
     - IL data center: `https://app.il.workato.com/saml/consume`
     - CN data center: `https://app.workatoapp.cn/saml/consume`
   - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
     - Self-service data center: `https://app.trial.workato.com/saml/consume`
4. Optional. Provide the **SSO URL** (Single Sign-On URL). This URL may be optional depending on your Identity Provider. You must locate your Workspace handle in Workato and replace `{WORKSPACE_HANDLE}` in the URL for the data center you use.
   
   - **Workato Enterprise customers:**
     - US data center: `https://www.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
     - EU data center: `https://app.eu.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
     - JP data center: `https://app.jp.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
     - SG data center: `https://app.sg.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
     - AU data center: `https://app.au.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
     - IL data center: `https://app.il.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
     - CN data center: `https://app.workatoapp.cn/saml/init?team_handle={WORKSPACE_HANDLE}`
   - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
     - Self-service data center: `https://app.trial.workato.com/saml/init?team_handle={WORKSPACE_HANDLE}`
5. Set additional parameters required by your Identity Provider and **Save** your SAML application setup.
   
6. Retrieve the **Metadata URL** from your Identity Provider. This URL is required to complete the SSO setup in Workato.
   

After you've finished the preceding steps, proceed to [set up your Workato SSO](/en/user-accounts-and-teams/single-sign-on#workato-single-sign-on-setup) to complete the setup.

## Step 2: Finish setup in Workato

1. Sign in to Workato and go to **Workspace admin > Settings > Login methods**.
   
2. Use the **Authentication method** drop-down menu to select **SAML based SSO**.
   
3. Provide a **Workspace handle** for the workspace. The maximum length is 20 characters. Workato converts uppercase letters to lowercase in this field.
   
4. Use the **SAML provider** drop-down menu to select your SAML provider. Select **Other SAML IdP** if using Google Workspace.
   
5. Locate the **Do you have your identity provider metadata URL?** field and select **Yes** or **No** depending on whether you have access to your IdP metadata URL.
   
   **Yes: you have your IdP metadata URL**
   
   #### I have my metadata URL
   
   1. Provide your metadata URL in the **Metadata URL** field.
      
      ![Yes: you have your IdP metadata URL](/assets/yes-metadata-url.CWtgUFb_.png)_Provide your metadata URL_
      
   
   **No: you don't have your IdP metadata URL**
   
   #### I don't have my metadata URL
   
   1. Provide your IdP SSO URL in the **Identity provider single sign-on URL** field.
      
      ![No: you don't have your IdP metadata URL](/assets/no-metadata-url.DBQU-Va3.png)_Provide your IdP information_
      
   
6. Enable JIT provisioning. Refer to our [Just-in-time provisioning guide](/en/user-accounts-and-teams/just-in-time-provisioning) for more information.
   
7. Enforce SAML SSO for all users. Workato requires all collaborators (except the workspace owner) to authenticate through your identity provider when you enable the **Enforce SAML authentication for all users** toggle. You can't disable SAML for individual users while enforcement is enabled.
   
   You must disable the **Enforce SAML authentication for all users** toggle at the workspace level to allow a user to access the workspace without SAML authentication.
   
8. Click **Validate settings**.
   
   > **VALIDATION ERROR**
   > 
   > Perform the following actions if you encounter a validation error:
   > 
   > 1. Verify that the certificate is valid with a tool like [sslshopper](https://www.sslshopper.com/). Certificates must start with `-----BEGIN CERTIFICATE-----` and end with `-----END CERTIFICATE-----`.
   >    
   > 2. Verify that your IdP SSO URL/metadata URL is in a valid format. Refer to your identity provider's SAML configuration guide.
   >    
   
9. Click **Save** after successful validation.
   

* * *

## Step 3: Assign SAML to users

You can assign the SAML application to your workspace members after completing the SSO configuration.

The following example uses an Okta application:

1. Go to the newly created SAML application in Okta:
   
   - **Applications > Workato > Assignments > Assign Users to App**.
2. Use list to assign workspace members to the application.
   

* * *

## Sign in to an SSO-enabled Workato workspace

Your SAML provider controls access to a Workato workspace when you enable SSO in Workato. You must [assign the SAML application](/en/user-accounts-and-teams/single-sign-on#assign-saml-to-users) to your workspace members to grant them access to a Workato workspace. Workspace members can then access their Workato accounts from the SAML provider, such as:

- **Google Workspace**
  - Use your company or organization sign-in URL. For example, `google.com/abc-example`
- **Microsoft Entra ID**
  - `https://myapps.microsoft.com/`
- **Okta**
  - Use your company or organization sign-in URL. For example, `123-example.okta.com`
- **OneLogin**
  - Use your company or organization sign-in URL. For example, `xyz-example.onelogin.com`

> **REQUEST THE SSO URL FROM YOUR ADMIN**
> 
> Reach out to your admin to request the SSO URL for your company or organization.

The steps to sign in to an SSO-enabled Workato workspace can vary depending on the SAML provider and the configuration set by your administrator. For instance, Okta and OneLogin accounts usually provide dashboards that allow you to select Workato (and other) applications with SSO enabled. In the Okta dashboard, you can click the Workato application to sign in:

![Workato app on Okta](/assets/okta-saml-sso-user-login.DTVZXtNi.png)_Workato app on Okta_

Workspace members must authenticate through the SAML provider when switching from their personal account to an SSO-enabled workspace account. This process varies depending on the SAML provider and the configuration selected by the administrator. The following example demonstrates this process:

![Workspace Switch with Okta](/assets/okta-saml-sso-team-switch.Dk5Atr5F.gif)_Switch to workspace account with Okta authorization_

> **WORKSPACE ACCOUNT OWNERS**
> 
> Workspace owners cannot use SAML-based SSO to authenticate with the workspace. They must use their username and password instead.

### Email verification for SAML JIT provisioning

A user logging in for the first time through either SP-initiated SSO or IdP-initiated SSO must verify their email address for SAML JIT Provisioning.

Workato prompts users to verify their email when accessing the workspace for the first time.

![Workspace verification](/assets/check-email.BHaM0Y09.png)

**Receive Invitation Email**: Workato sends an email invitation to the selected users. Instruct users to click the link in the email to verify their email address:

![Email invitation to join a workspace](/assets/scim-azure-ad-email-notification.kjKQFcUM.png) _Email invitation to join a workspace_

The collaborator can then sign in to the assigned workspace with the roles you have configured.

> **TROUBLESHOOTING**
> 
> You likely already have a Workato account associated with the same email if you click the invitation and are redirected to the Workato login page instead of your organization’s workspace. Reset your password if you have forgotten your login credentials.

**Verify Activity Audit Log**: You can check the Workato [activity audit log](/en/features/activity-audit-log) to confirm the addition of the user:

![Activity audit log showing that a user has accepted an invitation](/assets/scim-azure-ad-audit-log.CNCV_sJm.png) _Activity audit log showing that a user has accepted an invitation_

## IdP-initiated SSO flow

The IdP may provide the `team_id` as a GET parameter to execute IdP-initiated flows (accepting SAML Responses directly generated by the IdP). This allows Workato to identify the workspace the user is trying to access. The SAML Response is ignored and Workato starts a fresh SP-initiated SSO flow if Workato doesn't have the `team_id` information.

Configure the following value at the IdP:

- **ACS URL**
  - Use the URL for your Workato data center.
  - **Workato Enterprise customers:**
    - US data center: `https://www.workato.com/saml/consume?team_id={WORKSPACE_HANDLE}`
    - EU data center: `https://app.eu.workato.com/saml/consume?team_id={WORKSPACE_HANDLE}`
    - JP data center: `https://app.jp.workato.com/saml/consume?team_id={WORKSPACE_HANDLE}`
    - SG data center: `https://app.sg.workato.com/saml/consume?team_id={WORKSPACE_HANDLE}`
    - AU data center: `https://app.au.workato.com/saml/consume?team_id={WORKSPACE_HANDLE}`
    - IL data center: `https://app.il.workato.com/saml/consume?team_id={WORKSPACE_HANDLE}`
    - KR data center: `https://app.kr.workato.com/saml/consume?team_id={WORKSPACE_HANDLE}`
    - CN data center: `https://app.workatoapp.cn/saml/consume?team_id={WORKSPACE_HANDLE}`
    - UK data center: `https://app.uk.workato.com/saml/consume?team_id={WORKSPACE_HANDLE}`
  - **Self-service (Workato Free, Workato Pro, or Developer Sandbox) users:**
    - Self-service data center: `https://app.trial.workato.com/saml/consume?team_id={WORKSPACE_HANDLE}`

Where `{WORKSPACE_HANDLE}` is the Workspace handle configured in **Workspace admin > Settings > Login methods**.

* * *

---

---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/just-in-time-provisioning.md
description: >-
  Set up SAML just-in-time provisioning in Workato to automatically add team
  members to your workspace and assign roles and groups.
---

# Team collaboration - Just in time provisioning

Just-in-Time (JIT) provisioning eliminates the need for workspace admins to create Workato user accounts in advance on behalf of team members. When an employee signs up for a new Workato account using SAML SSO, they are automatically added to the organization's workspace.

> **Employee Email already Registered?**
> 
> If an employee has an existing Workato account, Workato automatically adds them to the organization's workspace.

* * *

## How to Enable JIT provisioning

You can enable SAML Just-In-Time provisioning in **Workspace admin** > **Settings** > **Authentication & provisioning**.

![Enable SAML Just-In-Time provisioning](/assets/saml-jitp.Dw2BQaB8.png)_Enable SAML Just-In-Time provisioning_

## Customize JIT provisioning

You can customize JIT provisioning to relay user-specific information to Workato. Workato takes SAML attributes (for example, `workato_role` ) and applies it to the provisioned Workato user. This enables you to provision new users with the appropriate information according to your workflow.

Workato supports the following attributes:

| Workato user field | SAML attribute | Default value |
| --- | --- | --- |
| User name | `NameID` | Sets the Workato login ID. Must use `emailAddress` format. |
| Display name | `emailaddress` claim | Sets the UI display name. The claim name is `emailaddress`. The IdP controls which directory attribute supplies the value (for example, `user.displayname` or `userPrincipalName`). |
| User team role | `workato_role` | Defaults to `Member` in [new permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2) workspaces, or `Operator` in workspaces using the legacy permissions model Learn more about [Workato environment roles](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles). |
| Collaborator groups | `workato_user_groups` | If empty or omitted, no changes are made to existing group memberships. If the value includes `All collaborators`, all explicit collaborator-group memberships are removed. Only supported in workspaces on the [new permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2) with project-level access control. |

## Why customize JIT provisioning

In the [new permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2), Workato uses environment roles and collaborator groups to manage access:

- [Environment roles](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles) define what a user can do within an environment, such as **Environment admin**, **Builder**, or **Operator**.
- [Collaborator groups](/en/user-accounts-and-teams/role-based-access/new-model/collaborator-groups) control project-level access when enabled.

In workspaces using the legacy permissions model, Workato assigns one of the default workspace-level system roles, such as **Admin**, **Analyst**, or **Operator**. These roles aren't used in workspaces on the new permissions model.

By customizing JIT provisioning, you can:

- Assign users to the correct environment roles automatically.
- Place users into collaborator groups for project-level access.
- Reduce manual provisioning and improve security compliance.

This approach ensures consistent access control, minimizes administrative overhead, and supports efficient user onboarding.

## How to customize JIT provisioning

To assign user information during JIT provisioning, you first need complete the basic setup:

- Enable [SAML based SSO](/en/user-accounts-and-teams/single-sign-on)
- Enable [SAML Just-in-Time provisioning](#jit-enable) in Workato
- [Configure the SAML attribute](#configure-saml-attribute) on the SAML provider's application page.
- (Optional) Create [custom roles](/en/user-accounts-and-teams/role-based-access/#creating-custom-roles) in Workato to enforce custom privileges. For example, `mktg_ops` role with only access to the Marketing folder within your workspace.

## Configure custom attributes on your SAML provider

When setting up JIT provisioning, configure the SAML attributes needed to assign environment roles and, optionally, project-level collaborator groups. This example uses Okta.

1. Go to **Directory > Profile Editor**.
   
2. Select your Workato SAML App profile.
   
3. Select **Add attribute**.
   
4. Fill in the attribute details for assigning environment roles:
   
   | Field | Description |
   | --- | --- |
   | Variable name | Use `workato_role`. This is case-sensitive. |
   | Attribute members | For each attribute, use a descriptive **Display name** and provide Workato-specific values. The **Value** corresponds to [environment roles](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles). Workspaces using the legacy permissions model still use roles like `Admin`, `Analyst`, and `Operator`. This is case-sensitive. |
   
   > **ENVIRONMENTS**
   > 
   > If your organization uses environments, you can configure attribute statements to assign environment-specific roles as well. Simply add the additional attributes with the variable name set to `workato_role_test` for the **TEST** environment and `workato_role_prod` for the **PROD** environment. The default `workato_role` attribute maps to the **DEV** environment.
   
5. Optional. Use the `workato_user_groups` attribute to assign users to collaborator groups for project-level access:
   
   | Field | Description |
   | --- | --- |
   | Variable name | Use `workato_user_groups`. This is case-sensitive. |
   | Attribute members | Provide a **Display name** and group names matching existing collaborator groups in Workato. |
   
   > **PROJECT-LEVEL ACCESS**
   > 
   > This attribute only applies to workspaces on the [new permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2). If the `workato_user_groups` attribute is empty or omitted, existing group memberships aren't changed. If the value includes **All collaborators**, all explicit collaborator-group memberships are removed.
   
6. Locate the Workato **SAML app**.
   
7. Select **SAML settings > edit**.
   
8. Skip to **Configure SAML**.
   
9. Locate **App attribute statement**.
   
   | Field | Description |
   | --- | --- |
   | Name | Use the attribute name, such as `workato_role` or `workato_user_groups`. This is case-sensitive. The **Name** must match a Workato-supported attribute. See [which fields are accepted](#customize-jit-provisioning). |
   | Value | Use `appuser.workato_role`. The **value** is the [attribute you have just configured](#attribute-name-in-saml). |
   
   > **Attribute Values for Different SAMLs**
   > 
   > Each SAML uses a different syntax.
   > 
   > | SAML application | Value |
   > | --- | --- |
   > | Okta | `appuser.<attribute_name>` |
   > | Onelogin | `appuser.<attribute_name>` |
   > | Microsoft Entra ID | `user.<attribute_name>` |
   > | Google IDP | `<attribute_name>` |
   
10. Click **Save** to confirm your changes
    

Lastly, [assign custom roles in your SAML application](#assign-roles-for-team-members).

* * *

## Assign roles for workspace members

Let's assign custom SAML attributes for Workato on Okta.

1. When an employee is onboarded with Okta, select a value for `workato_role`.
   
2. Alternatively, for existing Okta users, assign `workato_role` on their profile page. This only applies if this Okta user **does not have** an existing Workato account.
   
3. Now, when a user logs in to Workato [using SSO](/en/user-accounts-and-teams/single-sign-on), the identity provider passes `workato_role` for this new user. For a new hire in the Marketing department, the provisioned Workato user is configured with the custom role `mktg_ops`.
   

* * *

## JIT provisioning for users with access to multiple workspaces

In some situations, you may have one or more users that require access to multiple workspaces. For example, consider a scenario where your organization has separate Finance, Legal, and HR workspaces and you have one dedicated user who acts as a builder for all three workspaces. In this situation, the process of enabling JIT provisioning is the same, but Workato automatically adds an extra layer of security to prevent unauthorized access to your organization's workspaces.

When you enable JIT provisioning for users and then give them access to multiple workspaces, Workato follows this typical flow.

1. Your organization's Workato administrator assigns the user access to the Workato application in your identity provider. This workspace, named Finance, is the first Workato workspace within your organization that the user has joined.
   
2. The user signs up for a new Workato account using SAML SSO with your organization's authentication provider.
   
3. Workato automatically creates an account for the user, using your organization's identity provider.
   
4. The user joins the Finance workspace.
   
5. Your organization's Workato administrator assigns the user to the HR Workspace in your identity provider, which they haven't used before.
   
6. Because they already have an account created with JIT provisioning, Workato does not prompt the user to create an account again.
   
   Instead, Workato prompts the user to verify their identity using the email address associated with their account.
   
7. After the user verifies their identity, they can join the HR workspace.
   
8. The user can switch between the Finance and HR workspaces, as necessary.

---
