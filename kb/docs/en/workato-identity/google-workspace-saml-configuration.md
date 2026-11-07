---
url: >-
  https://docs.workato.com/en/workato-identity/google-workspace-saml-configuration.md
description: >-
  Configure Google Workspace as a SAML identity provider for Workato Identity,
  including attribute statements and user assignments.
---

# Google Workspace SAML configuration

This guide describes how to configure Google Workspace as a SAML identity provider (IdP) for Workato Identity.

SAML enables secure authentication between an IdP, such as Google Workspace, and a service provider like Workato. Users authenticate once through Google Workspace and gain access to Workato with a single login instead of managing separate credentials for each application.

> **PREREQUISITES**
> 
> - Workato Identity is available for [Agent Studio](/en/agentic/agent-studio), [Workato GO](/en/agentic/workato-go), [MCP](/en/mcp), and the [API developer portal](/en/api-mgmt/api-developer-portal).
>   
> - [Configure SAML-based authentication](/en/workato-identity/saml-sso#configure-saml-based-authentication) in Workato Identity before you begin. The **Specify Single sign-on URL** and **Service provider (SP) entity ID** values from that setup are required to complete the following steps.
>   
> - Make sure you have super administrator privileges in Google Workspace.
>   

## Configure SAML authentication in Google Workspace

Complete the following steps to configure SAML authentication in Google Workspace:

> **NOT FOR WORKFLOW APPS SAML-BASED SSO**
> 
> This documentation is specific to Workato Identity. Refer to [SAML-based single sign-on authentication](/en/workflow-apps/saml) to configure SAML authentication for [Workflow apps](/en/workflow-apps).

1. Sign in to your [Google Admin console](https://admin.google.com). You must be signed in as a super administrator.
   
2. Go to **Apps > Web and mobile apps**.
   
3. Click **Add App > Add custom SAML app**.
   
   ![Click Add App > Add custom SAML app](/assets/add-google-saml-app.BlBKnzpb.png)_Click **Add App > Add custom SAML app**._
   
4. Enter a name for the app in the **App name** field. For example, `Workato Agentic` or `MCP Servers`.
   
5. Click **Continue**.
   
6. Go to the **Google Identity Provider details** page and download the **IDP metadata** or copy the following values for later use:
   
   - **SSO URL**
   - **Entity ID**
   - **Certificate**
   
   > **GOOGLE WORKSPACE METADATA**
   > 
   > You may need to host your metadata file or verify if your Google Workspace tier exposes a metadata endpoint to provide a metadata URL in later steps.
   
7. Click **Continue**.
   
8. Go to the **Service Provider Details** window and paste the **Single sign-on URL** from Workato into the **ACS URL** field.
   
9. Paste the **Service provider (SP) entity ID** from Workato into the **Entity ID** field.
   
10. Click **Continue**.
    
11. Go to the **Attribute Mapping** section and click **Add mapping** to add the following attributes:
    
    | Google Directory attribute | App attribute |
    | --- | --- |
    | `Basic Information > Full name` | `workato_end_user_name` |
    | `Employee Details > Department` | `workato_end_user_groups` |
    
12. Click **Finish**.
    
13. Go back to **Apps > Web and mobile apps** and select your newly created app.
    
14. Click **User access** and set the service to **On for everyone**. Alternatively, you can configure access by organizational unit or group as required.
    
15. Click **Save**.
    
16. Return to the app's settings page and copy the **Metadata URL**, or use the IDP metadata file you downloaded in the previous steps. You must use this in the **Do you have your identity provider metadata URL?** section of the **Set up a new provider** modal in Workato Identity.
    
17. Go to your app's **App Access Control** to configure the settings to prevent users from seeing or launching the app directly.
    
    > **DIRECT SIGN-IN FROM IDP UNSUPPORTED**
    > 
    > You can't sign in to Workato directly from your IdP. Authentication is only supported when initiated through a conversation in your connected LLM.
