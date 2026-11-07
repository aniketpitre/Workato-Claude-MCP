---
url: 'https://docs.workato.com/en/workflow-apps/setup-and-access.md'
description: >-
  Set up a Workflow app by customizing its name and icon, previewing its URL,
  and managing app access for users and groups.
---

# Setup and access

The top portion of the **Workflow app** tab contains controls that enable you to determine your application's name, upload a custom icon, and manage app access.

![App view](/assets/app-view-name.DjJVeSmi.png)_App view_

## Customize app name and icon

Complete the following steps to customize your app's name and icon:

1. Click the existing name to edit the name of your app. This name is displayed in the [Workflow apps portal](/en/workflow-apps/portal-homepage).
   
2. Click the existing icon.
   
3. Upload a unique icon for your app.
   
4. Click the existing app name to view a read-only preview of your app's URL. You can [customize the URL prefix](/en/workflow-apps/portal-settings#general) in **Platform > Workflow apps portal > Portal settings > General**.
   

* * *

## Manage app access

This section of the **App** tab enables you to determine who can access your application by assigning user groups to your app.

> **BEFORE YOU BEGIN**
> 
> You must add app-users to the Workflow apps portal before you can assign user groups to your Workflow app.
> 
> Workato enables you to add internal and external users to your application, meaning app-users don't need a Workato account to join the Workflow apps portal.
> 
> Learn how to invite users in our [Administration guide](/en/workflow-apps/app-user-groups#add-users).

To manage app access:

1. Underneath your app's name the number of users and groups already assigned to this Workflow app appears. In the [preceding example](#app-setup), this is **2 groups, 10 users**.
   
   Click into this field to open the **Manage access** modal.
   
2. Click **\+ Add group**
   
   ![Add user group to app](/assets/add-group.BiNDt7mw.png)_Assign user groups to your app_
   
3. Select a user group from the picklist.
   
4. Assign each group a role. Their role determines the user group's permissions to interact with the app.
   
   ![Manage access for user groups](/assets/manage-access.DVYlS6E1.png)_Manage access for user groups_
   
   The following roles are available:
   
   - **Member**: Members can create new requests and respond to tasks assigned to them. Users with the **member** role can only access tasks in the **Assigned to me**, **Created by me**, and **Due today** tabs in the Workflow apps portal. The **All requests** tab is visible to users with the **member** role, but only includes tasks assigned to/created by the user.
     
   - **Manager**: Managers can view and update all requests created by users within the app, in addition to member permissions. Users with the **manager** role can access tasks in the **All requests**, **Assigned to me**, **Created by me**, and **Due today** tabs in the Workflow apps portal.
     
   
   ![Workflow apps portal roles](/assets/apps-portal-roles.B4h-Tmcc.png)_Roles determine the tasks users can access in the Workflow apps portal_
   
5. Click **Save changes**.
   

> **SET UP USER GROUPS**
> 
> You can set up user groups in **Platform > Workflow apps portal > Users and groups**. Refer to [Organize users and groups](/en/workflow-apps/app-user-groups#organize-users-groups) for more information.

---
