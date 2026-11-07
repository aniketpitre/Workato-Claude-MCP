---
url: 'https://docs.workato.com/en/workflow-apps/saml-sso-entra.md'
description: >-
  Set up SAML-based SSO authentication for Workflow apps using Microsoft Entra
  ID, including user group syncing to manage app access through your IdP.
---

# Enforce SAML-based SSO for Workflow apps with Microsoft Entra ID

This guide demonstrates how to set up SAML-based SSO authentication for Workflow apps using Microsoft Entra ID. It includes instructions for enabling user group syncing between Workflow apps and Microsoft Entra ID, allowing you to manage access to specific Workflow apps through your Identity Provider (IdP).

Setup involves retrieving values from your Workflow apps portal, creating an enterprise application in Microsoft Entra ID, syncing your user groups, and completing the configuration in Workato.

> **NOT FOR WORKATO IDENTITY SAML-BASED SSO**
> 
> This documentation is specific to Workflow apps. Refer to [Workato Identity SAML-based SSO](/en/workato-identity/saml-sso) to configure SAML authentication for Workato Identity features, such as [Agent Studio](/en/agentic/agent-studio), [Workato GO](/en/agentic/workato-go), and [MCP](/en/mcp).

> **DEFAULT SESSION DURATION**
> 
> The default session duration is seven days when you authenticate using SAML-based SSO without group syncing enabled. When group syncing is enabled, the default session timeout is one day.
> 
> You can use a [Conditional Access sign-in frequency policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-session-lifetime) to control how often users must reauthenticate with Microsoft Entra ID.

## Prerequisites

To complete the steps in this guide, you must have the following:

**In Workato:**

- One of the following, depending on your workspace's permission model:
  - **Legacy roles:** the **Admin** or **Analyst** [system role](/en/roles#system-roles).
  - **RBAC 2.0:** an [environment role](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles) that grants the **Apps portal > Settings** [privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#apps-portal), such as **Environment admin** or **Environment manager**.
- Access to Workflow apps.

**In Microsoft Entra ID:**

- Privileges that enable you to add, edit, and manage an enterprise application.
- Privileges that enable you to create users and groups, assign users to groups, and assign users and groups to applications.

## Retrieve values from Workato

You need the **Single Sign-On URL** and **Service provider (SP) entity ID** from your Workflow apps portal to configure Microsoft Entra ID. These values appear after you set the portal's authentication method to SAML-based SSO.

1. Sign in to Workato.
   
2. Go to **Platform > Workflow apps portal > Portal settings > Security**.
   
3. Select **SAML based SSO** in the **Authentication method** field. The portal displays the **Single Sign-On URL** and **Service provider (SP) entity ID**.
   
4. Copy the **Single Sign-On URL** and **Service provider (SP) entity ID**.
   
   > **URL FORMATS VARY**
   > 
   > The **Single Sign-On URL** and **Service provider (SP) entity ID** are unique to your Workflow apps portal subdomain or [custom domain](/en/workflow-apps/custom-domain-email-server) and the data center your account is located in. They follow these formats, where `{subdomain}` is your portal's subdomain and `{custom-domain}` is your custom domain name:
   > 
   > - **Single Sign-On URL**
   >   - Default domain: `https://{subdomain}.workato.app/portal/sso/saml/acs`
   >   - Custom domain: `https://{custom-domain}/portal/sso/saml/acs`
   > - **Service provider (SP) entity ID**
   >   - Default domain: `https://{subdomain}.workato.app/portal/sso/saml/metadata`
   >   - Custom domain: `https://{custom-domain}/portal/sso/saml/metadata`
   

## Create an enterprise application

Complete the following steps to register an enterprise application in Microsoft Entra ID and configure SAML-based SSO for your Workflow apps portal:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
   
2. Go to **Entra ID > Enterprise apps > All applications** and click **New application**.
   
3. Click **Create your own application**.
   
4. Provide a unique name for the app in the **What's the name of your app?** field. For example, `Workflow apps`.
   
5. Select **Integrate any other application you don't find in the gallery (Non-gallery)** and click **Create**.
   
6. Go to **Manage > Single sign-on** and select **SAML** as the single sign-on method.
   
7. Go to the **Basic SAML Configuration** section and click **Edit**.
   
8. Enter the values you retrieved from Workato:
   
   | Workato value | Microsoft Entra ID field |
   | --- | --- |
   | **Service provider (SP) entity ID** | **Identifier (Entity ID)** |
   | **Single Sign-On URL** | **Reply URL (Assertion Consumer Service URL)** |
   
9. Click **Save**.
   
   ![Basic SAML Configuration in Microsoft Entra ID with the Identifier and Reply URL filled from Workato.](/assets/basic-saml-config.lnxFyAyS.png)_Basic SAML Configuration in Microsoft Entra ID_
   
10. Go to the **Attributes & Claims** section and click **Edit**.
    
11. Click **\+ Add new claim**, add the following attribute, and click **Save**:
    
    | Name | Source attribute |
    | --- | --- |
    | `workato_app_user_name` | `user.displayname` |
    
    ![Manage claim panel in Microsoft Entra ID mapping workato\_app\_user\_name to user.displayname.](/assets/user-name-claim.Cx2Ptdv9.png)_The user name claim in Microsoft Entra ID_
    
12. Optional. Sync user group assignments between Microsoft Entra ID and the Workflow apps portal. Skip this step if you don't plan to manage user groups through Microsoft Entra ID.
    
    Click **\+ Add a group claim**, configure the following settings, and click **Save**:
    
    | Setting | Value |
    | --- | --- |
    | Which groups associated with the user should be returned in the claim? | **Groups assigned to the application** |
    | Source attribute | **Cloud-only group display names** |
    | Customize the name of the group claim | Enabled |
    | Name | `workato_app_user_groups` |
    | Namespace | Leave empty |
    
    ![Group claim in Microsoft Entra ID returning cloud-only group display names as workato\_app\_user\_groups.](/assets/group-claim.EU--GvWm.png)_The group claim in Microsoft Entra ID_
    
13. Go back to **Manage > Single sign-on**, scroll to the **SAML Certificates** section, and copy the **App Federation Metadata URL**. You paste this value into Workato in [Complete setup in Workato](#setup-complete).
    

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

## Configure Microsoft Entra ID SAML user group sync

You can sync user group assignments between Microsoft Entra ID and the Workflow apps portal. This section is only necessary if you manage user groups through Microsoft Entra ID. After you add the group claim in [Create an enterprise application](#enterprise-application-create), assign groups and users to your application to complete the sync.

> **GROUP NAMES MUST MATCH**
> 
> The user group name in your Workflow apps portal **must exactly match** the group display name in Microsoft Entra ID. If the names don't match, group assignments don't sync and users don't receive the intended app access.

This process involves the following tasks:

1. [Assign groups to your application](#groups-app-assign)
2. [Assign users to your application](#users-app-assign)

### Assign groups to your application

Complete the following steps to assign your Microsoft Entra ID groups to your application:

1. Sign in to the Microsoft Entra admin center and open your application.
   
2. Go to **Manage > Users and groups**.
   
3. Click **\+ Add user/group**.
   
4. Select one or more groups whose display names match the user group names in your Workflow apps portal.
   
5. Click **Assign**.
   

### Assign users to your application

Complete the following steps to grant users access to your application:

1. Add users to the Microsoft Entra ID groups you assigned to your application. Users receive the same access granted to the matching user group in your Workflow apps portal.
   
2. Provide the Workflow apps portal URL to your users so that they can sign in and access your Workflow apps.
   

## Complete setup in Workato

Return to Workato to provide the metadata from Microsoft Entra ID and enforce SAML-based SSO. Complete the following steps:

1. Sign in to Workato.
   
2. Go to **Platform > Workflow apps portal > Portal settings > Security**.
   
3. Ensure the **Authentication method** field is set to **SAML based SSO**.
   
   ![Workato SAML setup](/assets/workato-saml-setup._hTQes9j.png)_Workato SAML setup_
   
4. Select **Yes** in the **Do you have your identity provider metadata URL** field and paste the **App Federation Metadata URL** you [copied from Microsoft Entra ID](#copy-metadata-url).
   
5. Use the **Enforce SAML authentication for** field to specify whether SAML authentication applies to all Workflow apps users or only users in specific domains. Users outside the specified domains can sign in with password authentication.
   
6. Optional. Click **Enable JIT (Just-In-Time) provisioning** to automatically add users to the portal the first time they sign in through SSO.
   
7. Click **Enable user groups syncing** to sync user groups from Microsoft Entra ID. This step is mandatory if you plan to manage user groups through Microsoft Entra ID.
   
   > **GROUP SYNCING TIMING**
   > 
   > User group syncing doesn't take effect immediately. It's enforced each time a user signs into the portal through Microsoft Entra ID.
   
   The SAML attributes required for group syncing are configured in [Create an enterprise application](#enterprise-application-create). If you completed that section, no further setup is needed here.
   
8. Click **Save changes**.

---
