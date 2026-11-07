---
url: 'https://docs.workato.com/en/connectors/jira.md'
description: >-
  The Jira connector lets you automate issue tracking: create, update, and
  search issues, manage comments and attachments, and trigger on new or updated
  issues.
---

# Jira

[Jira](https://www.atlassian.com/software/jira) provides a simple way to organize and plan the release of any software. This allows development teams to lay out key steps to follow when releasing the software including:

- Plan
- Track
- Release
- Report

You can use Workato to sync projects and issues between Jira and other issue tracking systems, such as Zendesk, ServiceNow, and Salesforce's Desk.com.

> **SUMMARY**
> 
> - Workato's Jira connector synchronizes projects and issues between Jira and other systems such as Zendesk, ServiceNow, and Salesforce's Desk.com.
> - This connector supports Jira Cloud, Jira Data Center, and on-premise instances version 7.x and later.
> - We recommend using API tokens, service account API tokens, OAuth 2.0, or personal access tokens for authentication.
> - API token and service account (API token) authentication don't support on-prem Jira connections.
> - OAuth 2.0 (Cloud - Atlassian-hosted Jira) and OAuth 2.0 (Data Center) are separate authentication options; real-time triggers aren't supported with either.
> - Jira users with login access can connect using their credentials, but we recommend creating a separate user with Jira Administrator global permissions.

## Use cases

Explore Jira connector capabilities with our [use cases](/en/getting-started/workato-use-cases) documentation. Discover how you can use the Jira connector to create powerful multi-app workflows and automations:

- [Provision Jira and Okta users](/en/getting-started/use-cases/workday-jira-okta) for new employees in Workday.
- [Create or update Jira issues](/en/getting-started/use-cases/pagerduty-jira) from new PagerDuty incidents.
- [Create Jira issues](/en/getting-started/use-cases/servicenow-jira) for new ServiceNow incidents.

## API version

The Jira connector uses the [Jira Cloud REST API v2](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/#about).

## Supported editions and versions

The Jira connector works with:

- Jira Cloud instances
- Jira on-premise instances version 7.x and later
- Jira Data Center, which replaced Jira Server

## Connection setup

There are six ways to connect to Jira:

- [API token](#api-token)
- [Service account (API token)](#service-account-api-token)
- [OAuth 2.0 (Cloud - Atlassian-hosted Jira)](#oauth-2-0-cloud)
- [OAuth 2.0 (Data Center)](#oauth-2-0-data-center)
- [Personal access tokens](#personal-access-tokens)
- [Basic authentication (password)](#basic-authentication-with-password)

We strongly recommend using API tokens, service account API tokens, OAuth 2.0, or personal access tokens to connect to Jira instead of basic authentication with a password.

> **LIMITATIONS**
> 
> Authentication methods for the Jira connector have the following limitations:
> 
> - Real-time triggers aren't supported with OAuth 2.0 (Cloud - Atlassian-hosted Jira) or OAuth 2.0 (Data Center).
> - On-prem Jira connections aren't supported with API token or service account (API token) authentication.
> - Atlassian deprecated basic authentication for cloud connections in December 2018. On-premise Jira is not affected.

### API token

View API token steps

API tokens authenticate your Atlassian account without using a username and password. API token authentication doesn't support connections to on-premise Jira.

#### Prerequisites

You must generate an Atlassian API token for this authentication method. Refer to the Atlassian [Manage API tokens](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) guide for more information.

#### Connect to Jira using an API token

Complete the following steps to connect to Jira in Workato using an API token:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![API token auth](/assets/api-token-auth.CeU8zRLD.png)_API token auth_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **API token**.
   
7. Enter the URL subdomain for your Jira instance in the **Host name** field. For example: `workato.atlassian.net`
   
8. Enter the **Email** of the Jira account to link to Workato.
   
9. Enter the **API token** for your Atlassian account. Refer to the Atlassian [Manage API tokens](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) guide to generate this value.
   
10. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
11. Click **Connect**.
    

### Service account (API token)

View Service account (API token) steps

Use this authentication method to connect Workato to Jira using an Atlassian Cloud service account. A service account is a dedicated, non-personal Atlassian account used for integrations. Service accounts aren't tied to individual users, so connections remain stable when team members leave or change roles.

Service account (API token) authentication supports Jira Cloud connections only.

#### Prerequisites

Complete the following tasks before you connect:

##### Set up the service account

1. Go to [Atlassian Administration](https://admin.atlassian.com/).
   
2. Select your organization.
   
3. Select **Directory > Service accounts** and click **Create a service account**.
   
4. Enter a name and description for the service account, then click **Create a service account**.
   
5. Select the apps and roles for the service account on the **Select app role for service account** page.
   
6. Add the service account to groups to grant access to specific projects or spaces.
   
7. Click **Create**.
   
8. Click **Create credentials**.
   
9. Select **API token** on the **Choose authentication type** screen.
   
10. Enter a **Name** and **Expires on** date on the **Name API token** page.
    
11. Select the scopes for your connection. At minimum, you must select `read:jira-user` to establish the connection. Select additional scopes based on the triggers and actions your recipes use. Refer to [Manage API tokens for service accounts](https://support.atlassian.com/user-management/docs/manage-api-tokens-for-service-accounts/#Create-an-API-token-with-scopes) for the full list of available scopes.
    
12. Click **Next**.
    
13. Review the scopes assigned to your token on the **Review your API token** screen.
    
14. Click **Create**.
    
15. Click **Copy** to copy your API token. Save this value for use in Workato.
    
16. Click **Done**.
    

#### Connect to Jira using a service account API token

Complete the following steps to connect to Jira in Workato using a service account API token:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **Service account (API token)**.
   
7. Enter the URL subdomain for your Jira instance in the **Host name** field. For example: `workato.atlassian.net`
   
8. Enter the email address associated with the service account in the **Email** field.
   
9. Enter the **API token** for the service account. Refer to the Atlassian [Manage API tokens](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) guide to generate this value.
   
10. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
11. Click **Connect**.
    

### OAuth 2.0 (Cloud - Atlassian-hosted Jira)

View OAuth 2.0 (Cloud - Atlassian-hosted Jira) steps

OAuth 2.0 enables you to share specific data with an application while keeping your username, password, and other information private. OAuth 2.0 (Cloud - Atlassian-hosted Jira) supports Jira Cloud connections.

> **REAL-TIME TRIGGERS NOT SUPPORTED**
> 
> OAuth 2.0 doesn't support real-time triggers because it's incompatible with webhooks. As an alternative, you can register the [Webhooks connector](/en/connectors/workato-webhooks) in Jira to use Jira's static webhook functionality. Refer to the [Cloud Jira](https://support.atlassian.com/jira-cloud-administration/docs/manage-webhooks/) webhook documentation for registration steps.

#### Connect to Jira using OAuth 2.0 (Cloud - Atlassian-hosted Jira)

Complete the following steps to connect to Jira in Workato using OAuth 2.0 (Cloud - Atlassian-hosted Jira):

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![OAuth 2.0 auth](/assets/oauth-2-0-auth.Cd8GQFwz.png)_OAuth 2.0 auth_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **OAuth 2.0 (Cloud - Atlassian-hosted Jira)**.
   
7. Enter the URL subdomain for your Jira instance in the **Host name** field. For example: `workato.atlassian.net`
   
8. Optional. Use the **Scopes** drop-down menu to select the authorization scopes to request. Workato requests the following scopes by default:
   
   - `read:jira-user`
   - `write:jira-work`
   - `manage:jira-project`
   - `read:jira-work`
   - `manage:jira-webhook`
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Connect** and sign in to your Jira instance.
    
11. Authorize Workato's request to access your Jira instance.
    

### OAuth 2.0 (Data Center)

View OAuth 2.0 (Data Center) steps

OAuth 2.0 (Data Center) enables you to connect to an on-premise Jira Data Center instance using OAuth 2.0.

> **REAL-TIME TRIGGERS NOT SUPPORTED**
> 
> OAuth 2.0 doesn't support real-time triggers because it's incompatible with webhooks. As an alternative, you can register the [Webhooks connector](/en/connectors/workato-webhooks) in Jira to use Jira's static webhook functionality. Refer to the [Jira Datacenter](https://confluence.atlassian.com/adminjiraserver/managing-webhooks-938846912.html) webhook documentation for registration steps.

#### Prerequisites

You must generate an Atlassian client ID and client secret if you plan to connect to Jira Data Center using OAuth 2.0. Refer to the Atlassian [Configure an incoming link](https://confluence.atlassian.com/adminjiraserver/configure-an-incoming-link-1115659067.html) guide to generate these values using `https://www.workato.com/oauth/callback` as the redirect URI.

#### Connect to Jira using OAuth 2.0 (Data Center)

Complete the following steps to connect to Jira in Workato using OAuth 2.0 (Data Center):

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **OAuth 2.0 (Data Center)**.
   
7. Enter the hostname of your Jira Data Center instance in the **Host name** field. For example: `jira.yourcompany.com`
   
8. Expand the **Advanced settings** section.
   
9. Enter the **Client ID** and **Client secret** from your Jira Data Center application link configuration. Refer to the [Prerequisites](#oauth-2-0-data-center-prerequisites) section to generate these values.
   
10. Optional. Use the **Scopes** drop-down menu to select the authorization scopes to request. Defaults to **READ** and **WRITE**.
    
11. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
12. Click **Connect** and sign in to your Jira instance.
    
13. Authorize Workato's request to access your Jira instance.
    

### Personal access tokens

View Personal access tokens steps

Personal access tokens (PATs) authenticate your Atlassian account without using a username and password. PAT authentication supports on-premise Jira connections.

#### Prerequisites

You must generate an Atlassian personal access token for this authentication method. Refer to the Atlassian [Using Personal Access Tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) guide for more information.

#### Connect to Jira using a personal access token

Complete the following steps to connect to Jira in Workato using a personal access token:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Personal access token auth](/assets/personal-access-token-auth.CVFp-sGl.png)_Personal access token auth_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **Personal access token**.
   
7. Enter the URL subdomain for your Jira instance in the **Host name** field. For example: `workato.atlassian.net`
   
8. Enter the **Personal access token** of the Jira account to link to Workato. Refer to the Atlassian [Using Personal Access Tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) guide to generate this value.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Connect**.
    

### Basic authentication with password

View Basic authentication with password steps

Basic authentication connects to your Atlassian account using a username and password. Basic authentication supports on-premise Jira connections.

> **DEPRECATED PASSWORD AUTHENTICATION**
> 
> Atlassian deprecated basic authentication for cloud connections in December 2018. On-premise Jira is not affected.

#### Connect to Jira using basic authentication

Complete the following steps to connect to Jira in Workato using basic authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Basic password auth](/assets/basic-password-auth.Bp4eQ9Ja.png)_Basic password auth_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **Basic**.
   
7. Enter the URL subdomain for your Jira instance in the **Host name** field. For example: `workato.atlassian.net`
   
8. Enter your Jira **Username** and **Password**.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Connect**.
    

## Roles and permissions required to connect

Jira, Jira Cloud, and Jira Data Center users who have login access to their Jira instance can connect to Workato using their credentials. However, we recommend that you create a separate user (with Jira Administrator global permissions) for integration purposes.

Jira connection respects the **project permissions** schemes in your Jira project. You must ensure that your Jira account has sufficient permissions to perform the desired actions on the relevant Jira objects.

### Jira project permissions

There are three main ways a user can have access to objects within a project:

- People
- Issue security schemes
- Permission schemes

#### People

Users [can be added to a project](https://confluence.atlassian.com/get-started-with-jira-core/add-users-to-your-project-917965377.html) (through **Project Settings > People**) using two methods:

1. Searching for and selecting a specific user, and then specifying the user's project role. ![People project roles](/assets/project-people-roles-1.sz4nRSST.png)_Choosing a project role for a user Jan Donyada_
   
   Project roles allow users to be associated with functional roles. For example, if your organization requires all software development issues to be tested by a **QA** person before being closed, you could:
   
   - Create a project role called **QA**.
   - Create a permission scheme called **Software Development**, in which you assign the **Close issue** permission to the **QA** role.
   - Associate the **Software Development** permission scheme with all software development projects.
   - For each software development project, add your QA engineers, assigning them the **QA** project role.
2. Searching for a Group and then specifying the group's project role. ![People project group](/assets/project-people-group.59sXXbk-.png)_Choosing a project role for the Jira Administrators group_
   
   A group contains multiple members. Groups are similar to project roles, but with one key difference: _group membership is global, whereas project role membership is project-specific_. Also, group membership can be changed only by Jira administrators, whereas project role membership can be changed only by project administrators.
   

#### Issue security schemes

[Issue security schemes](https://confluence.atlassian.com/adminjiracloud/configuring-issue-level-security-776636711.html) can be created and added to each project, allowing control over who can view and edit the issues of the project.

A scheme can have several security levels, and users or groups of users can be assigned to each security level. This ensures that only users who are assigned the appropriate security level can view the issue.

If your project has a defined issue security scheme, your linked Jira account must be a member of the appropriate security level in the security scheme. Typically, a security level's members include:

- Individual members
- Groups
- Project Roles
- Issue roles such as:
  - Reporter
  - Project Lead
  - Current Assignee
- Anyone (for example, to allow anonymous access)

In the following example, the issue security scheme has a defined security level which allows access to only certain users, groups, and project roles.

![Issue security scheme](/assets/issue-security-scheme-example.CqR5sxvf.png)_Only user 'Jan Donyada', users in the 'Jira Administrators' group, and users with the 'QA' project role have access to the issues, as defined by the 'Top-secret' security level_

#### Permission schemes

Project permissions are created within **Permissions schemes**, which are then assigned to specific projects by your Jira Administrators.

Permissions control access to specific actions such as issue creation, issue editing, and issue assignment. Go to **Project Settings > Permissions** in Jira to view permissions.

Each permission can be granted across:

- Project roles
- Applications (Jira, Jira Service Desk, Jira Data Center, and more.)
- Groups

##### Project roles

If a permission scheme associated with a project has defined role-specific permissions for specific actions, your linked Jira account _must_ be assigned the same role to be authorized to use those actions in your Workato recipes.

For example, in the project permission scheme below, only the **QA** role has been permitted to perform the **Close Issues** action. ![QA role](/assets/qa-role.DoLa-Oyj.png)

If the Workato recipe wants to perform any **Close issue** actions, the linked Jira account must also be assigned the role **QA** for the action to be authorized.

##### Application access

Application access settings let you control which person has access to which products. If your site only has one product (for example, if you have a Confluence-only or Jira-only instance), users are automatically granted access to that product when they sign up.

![Application permission schemes](/assets/application-permission-schemes-1.BU9FhDST.png)

If your Workato recipes only need to perform specific actions on your Jira Software instance, then **Jira Software** must be selected for those actions.

![Jira Software only](/assets/jira-software-only.BoLWPiEX.png)_Only users of Jira Software are permitted to assign issues_

Likewise, if your Workato recipes only need to perform specific actions on your Confluence instance, then **Confluence** must be selected for those actions.

If your Workato recipes perform specific actions on both Jira Software & Confluence, then **Any logged in user** must be selected for those actions.

![any logged in user](/assets/any-logged-in-user.yWb_vdvv.png)_Any logged in user of either Jira Software or Confluence is permitted to assign issues_

##### Groups

If a permission scheme associated with a project has defined group-specific permissions for specific actions, your linked Jira account _must_ be a member of that group to be authorized to use those actions in your Workato recipes. ![Jira admin group](/assets/jira-admin-group.BcGRLgR9.png)_The Jira Administrators group is permitted to manage sprints_

## Supported Jira actions and their required permissions

### Upload/download actions

To use the upload and download attachment actions, your linked Jira account must be added to the permissions under the **Attachment Permissions** tab of the permissions page.

![Upload/download actions](/assets/upload-download-attachments-1.CamBxyTs.png)

### Comments triggers and actions

To use triggers and actions relating to **Comments**, your linked Jira account must be added to the permissions under the **Comments Permissions** tab of the permissions page.

![Comments triggers and actions](/assets/comments-permission-schemes-1.DfTZiCHq.png)

### Issues triggers and actions

To use triggers and actions relating to **Issues**, your linked Jira account must be added to the permissions under the **Issues Permissions** tab of the permissions page.

![Issues triggers and actions](/assets/issues-permission-schemes-1.DfGr3r0s.png)

A `403 - Forbidden` error displays if the connected Jira user doesn't have the required [permissions](#permission-schemes) to access an object or action.

Refer to [Jira's permissions guide](https://confluence.atlassian.com/jirakb/jira-permissions-made-simple-717062767.html) for information about how to manage project permissions.

To troubleshoot why a user is unable to access or perform actions on certain projects, issue types, or fields, you can use the [Jira permission helper](https://support.atlassian.com/jira-cloud-administration/docs/use-the-jira-admin-helper/).

## Jira permissions helper

You can use the Jira permissions helper to find out why a user is unable to view/edit certain projects or fields.

![Jira permissions helper](/assets/permissions-helper.Cl1LKFJl.png)

To use this, you must have Jira Administrator access to your Jira instance. Refer to the Jira [Permissions helper guide](https://support.atlassian.com/jira-cloud-administration/docs/use-the-jira-admin-helper/) for more information.

## Using Jira real-time triggers

To use Jira real-time triggers, a webhook must first be registered in your connecting Jira instance. Registering webhooks to Jira instances requires Jira Administrator global permissions.

If your linked Jira account has **Jira Administrators global permissions**, then Workato automatically registers a webhook in your Jira instance when your Workato recipe (containing a Jira real-time trigger) is started for the first time.

For more information on Jira administrators & global permissions, check out [Jira's global permissions guide](https://confluence.atlassian.com/adminjiraserver073/managing-global-permissions-861253290.html?_ga=2.23273789.68011281.1530500434-2085645607.1519723142#Managingglobalpermissions-sysadminAboutJIRASystemAdministratorsandJIRAAdministrators).

Your linked Jira account must have **Jira Administrators global permissions** to register webhooks. You can complete the following if you don't have the required permissions:

- Work with a user that has the correct permissions to register webhooks.
- Request access to **Jira Administrators global permissions**.
- Use a [webhook trigger with the Webhooks connector](/en/connectors/workato-webhooks) and Jira's static webhook functionality as an alternative for real-time triggers in the Jira connector.

### Registering a webhook trigger as a Jira Administrator

If you're a Jira Administrator with global permissions, you can register a webhook for your fellow Jira instance users who want to use it for their HTTP webhook trigger recipes.

This can be done from the Jira administration console. For more information on how to register a webhook through the Jira administration console, check out the Jira guide on [registering a webhook](https://developer.atlassian.com/server/jira/platform/webhooks/#registering-a-webhook).

#### How to register a webhook

1. Go to **Jira administration console > System > Webhooks**.
   
   ![Jira webhooks](/assets/jira-admin-console-webhook.7lWPIGq7.png)_You should see a list of webhooks in the webhook summary page_
   
2. Click **Create a webhook** in the top right-hand corner of the page. This should open the webhook form.
   
   ![Jira webhook form](/assets/jira-webhook-form.Cg3GWvff.png)_Form for registering a Jira webhook_
   
3. Enter the details for your new webhook in the form:
   
   1. Enter a name for your webhook.
   2. Set the status to **Enabled**.
   3. Under URL, paste the target URL of the HTTP webhook trigger your Jira user is using for their recipe. ![HTTP webhook target URL](/assets/http-webhook-target-url.CKnuUNMv.png)_Obtain the URL from an HTTP 'New event through webhook' trigger in the Jira user's recipe_
   4. Check the boxes for the Jira events you plan to listen to, then click **Create**. For a full list of events and how to configure them, check out the Jira documentation for [available Jira webhook events](https://developer.atlassian.com/cloud/jira/platform/webhooks/#configuring-a-webhook).

---
