---
url: >-
  https://docs.workato.com/en/workato-identity/microsoft-entra-id-saml-configuration.md
description: >-
  Configure Microsoft Entra ID as a SAML identity provider for Workato Identity,
  including attribute statements and user assignments.
---

# Microsoft Entra ID SAML configuration

This guide describes how to configure Microsoft Entra ID as a SAML identity provider (IdP) for Workato Identity.

SAML enables secure authentication between an IdP, such as Microsoft Entra ID, and a service provider like Workato. Users authenticate once through Microsoft Entra ID and gain access to Workato with a single login instead of managing separate credentials for each application. Refer to Microsoft Entra ID [SAML-based authentication](https://learn.microsoft.com/en-us/power-pages/security/authentication/saml2-settings-azure-ad) documentation for more information.

> **PREREQUISITES**
> 
> - Workato Identity is available for [Agent Studio](/en/agentic/agent-studio), [Workato GO](/en/agentic/workato-go), [MCP](/en/mcp), and the [API developer portal](/en/api-mgmt/api-developer-portal).
>   
> - [Configure SAML-based authentication](/en/workato-identity/saml-sso#configure-saml-based-authentication) in Workato Identity before you begin. The **Specify Single sign-on URL** and **Service provider (SP) entity ID** values from that setup are required to complete the following steps.
>   

## Configure SAML authentication in Microsoft Entra ID

Complete the following steps to configure SAML authentication in Microsoft Entra ID:

> **NOT FOR WORKFLOW APPS SAML-BASED SSO**
> 
> This documentation is specific to Workato Identity. Refer to [SAML-based single sign-on authentication](/en/workflow-apps/saml) to configure SAML authentication for [Workflow apps](/en/workflow-apps).

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) or the [Azure portal](https://portal.azure.com).
   
2. Go to **Identity > Applications > Enterprise applications** and click **New application**.
   
3. Click **Create your own application**.
   
4. Enter a name for the app in the **What's the name of your app?** field. For example, `Workato Agentic` or `MCP Servers`.
   
5. Select **Integrate any other application you don't find in the gallery (Non-gallery)** and click **Create**.
   
6. Go to **Manage > Single sign-on** and select **SAML** as the single sign-on method.
   
7. Go to the **Basic SAML Configuration** section and click **Edit**.
   
8. Paste the **Service provider (SP) entity ID** from Workato into the **Identifier (Entity ID)** field.
   
9. Paste the **Single sign-on URL** from Workato into the **Reply URL (Assertion Consumer Service URL)** field.
   
   ![Paste the Single sign-on URL from Workato into the Reply URL (Assertion Consumer Service URL) field](/assets/reply-url-entra-id.B-lr-qMo.png)_Paste the **Single sign-on URL** from Workato into the **Reply URL (Assertion Consumer Service URL)** field_
   
10. Click **Save**.
    
11. Go to the **Attributes & Claims** section and click **Edit**.
    
12. Click **\+ Add new claim** and add the following attribute:
    
    | Name | Source attribute |
    | --- | --- |
    | `workato_end_user_name` | `user.displayname` |
    
13. Click **Save**.
    
14. Click **\+ Add a group claim** and configure the following settings:
    
    | Setting | Value |
    | --- | --- |
    | Which groups should be returned in the claim? | **Groups assigned to the application** |
    | Source attribute | **Cloud-only group display names** |
    | Customize the name of the group claim | Enabled |
    | Name | `workato_end_user_groups` |
    | Namespace | Leave empty |
    
    ![Configure group claims settings in Microsoft Entra ID](/assets/group-claims-entra-id.Z5UPu0wM.png)_Configure the group claims settings in Microsoft Entra ID_
    
15. Click **Save**.
    
16. Go to **Manage** and select **Users and groups**.
    
17. Click **Add user/group** and add one or more users or groups that should have access to the application.
    
18. Click **Assign**.
    
19. Return to **Single sign-on** and scroll to the **SAML Certificates** section.
    
20. Copy the **App Federation Metadata URL**. You must use this URL in the **Do you have your identity provider metadata URL?** section of the **Set up a new provider** modal in Workato Identity.
    
21. Return to your Microsoft Entra ID account and go to **Properties**.
    
22. Set **Visible to users?** to **No** to prevent the app from appearing in the user's app launcher.
    
    > **DIRECT SIGN-IN FROM IDP UNSUPPORTED**
    > 
    > You can't sign in to Workato directly from your IdP. Authentication is only supported when initiated through a conversation in your connected LLM.
