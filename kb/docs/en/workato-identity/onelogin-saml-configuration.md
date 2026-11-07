---
url: 'https://docs.workato.com/en/workato-identity/onelogin-saml-configuration.md'
description: >-
  Configure OneLogin as a SAML identity provider for Workato Identity, including
  attribute statements and user assignments.
---

# OneLogin SAML configuration

This guide describes how to configure OneLogin as a SAML identity provider (IdP) for Workato Identity.

SAML enables secure authentication between an IdP, such as OneLogin, and a service provider like Workato. Users authenticate once through OneLogin and gain access to Workato with a single login instead of managing separate credentials for each application. Refer to the OneLogin [SAML-based authentication](https://developers.onelogin.com/quickstart/saml) documentation for more information.

> **PREREQUISITES**
> 
> - Workato Identity is available for [Agent Studio](/en/agentic/agent-studio), [Workato GO](/en/agentic/workato-go), [MCP](/en/mcp), and the [API developer portal](/en/api-mgmt/api-developer-portal).
>   
> - [Configure SAML-based authentication](/en/workato-identity/saml-sso#configure-saml-based-authentication) in Workato Identity before you begin. The **Specify Single sign-on URL** and **Service provider (SP) entity ID** values from that setup are required to complete the following steps.
>   
> - Make sure you have administrator privileges in OneLogin.
>   

## Configure SAML authentication in OneLogin

Complete the following steps to configure SAML authentication in OneLogin:

> **NOT FOR WORKFLOW APPS SAML-BASED SSO**
> 
> This documentation is specific to Workato Identity. Refer to [SAML-based single sign-on authentication](/en/workflow-apps/saml) to configure SAML authentication for [Workflow apps](/en/workflow-apps).

1. Sign in to your [OneLogin](https://app.onelogin.com/login) instance as an administrator.
   
2. Go to **Applications > Applications** and click **Add App**.
   
3. Search for and select **SAML Test Connector (IdP w/ attr w/ sign response)**.
   
4. Enter a name for the app in the **Display Name** field. For example, `Workato Agentic` or `MCP Servers`.
   
5. Click **Save**.
   
6. Select the **Configuration** tab and enter the following values based on your Workato data center:
   
   **Audience**:
   
   | Workato Enterprise customers | Value |
   | --- | --- |
   | US | `https://www.workato.com/saml/metadata` |
   | EU | `https://app.eu.workato.com/saml/metadata` |
   | JP | `https://app.jp.workato.com/saml/metadata` |
   | SG | `https://app.sg.workato.com/saml/metadata` |
   | AU | `https://app.au.workato.com/saml/metadata` |
   | IL | `https://app.il.workato.com/saml/metadata` |
   | CN | `https://app.workatoapp.cn/saml/metadata` |
   | KR | `https://app.kr.workato.com/saml/metadata` |
   | UK | `https://app.uk.workato.com/saml/metadata` |
   
   | Self-service (Workato Free, Workato Pro, or Developer Sandbox) users | Value |
   | --- | --- |
   | Self-service | `https://app.trial.workato.com/saml/metadata` |
   
   **Recipient** and **ACS (Consumer) URL**:
   
   | Workato Enterprise customers | Value |
   | --- | --- |
   | US | `https://www.workato.com/saml/consume` |
   | EU | `https://app.eu.workato.com/saml/consume` |
   | JP | `https://app.jp.workato.com/saml/consume` |
   | SG | `https://app.sg.workato.com/saml/consume` |
   | AU | `https://app.au.workato.com/saml/consume` |
   | IL | `https://app.il.workato.com/saml/consume` |
   | CN | `https://app.workatoapp.cn/saml/consume` |
   | KR | `https://app.kr.workato.com/saml/consume` |
   | UK | `https://app.uk.workato.com/saml/consume` |
   
   | Self-service (Workato Free, Workato Pro, or Developer Sandbox) users | Value |
   | --- | --- |
   | Self-service | `https://app.trial.workato.com/saml/consume` |
   
   **ACS (Consumer) URL Validator**:
   
   | Workato Enterprise customers | Value |
   | --- | --- |
   | US | `^https:\/\/www.workato.com\/saml\/*$` |
   | EU | `^https:\/\/app.eu.workato.com\/saml\/*$` |
   | JP | `^https:\/\/app.jp.workato.com\/saml\/*$` |
   | SG | `^https:\/\/app.sg.workato.com\/saml\/*$` |
   | AU | `^https:\/\/app.au.workato.com\/saml\/*$` |
   | IL | `^https:\/\/app.il.workato.com\/saml\/*$` |
   | CN | `^https:\/\/app.workatoapp.cn\/saml\/*$` |
   | KR | `^https:\/\/app.kr.workato.com\/saml\/*$` |
   | UK | `^https:\/\/app.uk.workato.com\/saml\/*$` |
   
   | Self-service (Workato Free, Workato Pro, or Developer Sandbox) users | Value |
   | --- | --- |
   | Self-service | `^https:\/\/app.trial.workato.com\/saml\/*$` |
   
7. Click **Save**.
   
8. Select the **Parameters** tab and click the **+** (plus) icon to add the following attributes:
   
   | Field name | Value |
   | --- | --- |
   | `workato_end_user_name` | `Display Name` |
   | `workato_end_user_groups` | `Group Name` |
   
9. Check the **Include in SAML assertion** checkbox for each attribute and click **Save**.
   
10. Go to the **Users** tab and assign one or more users or groups to the application.
    
11. Click **More Actions**.
    
    ![Click More Actions](/assets/onelogin-more-actions.DojVGhea.png)_Click **More Actions**_
    
12. Right-click **SAML Metadata** and select **Copy link address**.
    
13. Paste the SAML Metadata link address into the **Do you have your identity provider metadata URL?** section of the **Set up a new provider** modal in Workato Identity.
    
14. Go to your app's **Info** tab and disable the **Visible in portal** option to hide the application from users' OneLogin dashboards.
    
    > **DIRECT SIGN-IN FROM IDP UNSUPPORTED**
    > 
    > You can't sign in to Workato directly from your IdP. Authentication is only supported when initiated through a conversation in your connected LLM.

---
