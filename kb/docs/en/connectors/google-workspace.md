---
url: 'https://docs.workato.com/en/connectors/google-workspace.md'
description: >-
  Google Workspace is a collection of cloud computing, productivity, and
  collaboration tools.
---

# Google Workspace

[Google Workspace](https://workspace.google.com/), formerly known as G Suite, is a collection of cloud computing, productivity, and collaboration tools developed by Google.

Workato's Google Workspace connector allows you to add, delete, update, fetch, or search for objects, such as users, groups, or roles. For example, when onboarding new employees, you can automatically add their details to Google Workspace.

> **FEATURE AVAILABILITY**
> 
> The Google Workspace connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The Google Workspace connector uses the [Google Admin SDK](https://developers.google.com/admin-sdk) to connect to admin services.

## How to connect to Google Workspace

The Google Workspace connector supports the following authentication methods:

- [OAuth 2.0](/en/connectors/google-workspace#oauth-2-0)
- [Service account](/en/connectors/google-workspace#service-account)

> **SERVICE ACCOUNT AUTHENTICATION**
> 
> You can use a service account to authenticate without a personal user account. For consistent use, Workato recommends service account authentication.

### OAuth 2.0 authentication

Complete the following steps to connect to Google Workspace using OAuth 2.0 authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Workspace** as your connection.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
6. Optional. Expand the **Advanced settings** section and select OAuth 2.0 scopes to request for your connection.
   
   Workato requests the following scopes by default in addition to the scopes you select:
   
   | Description | Scope requested |
   | --- | --- |
   | View and manage the provisioning of users on your domain | `admin.directory.user` |
   | View and manage organization units on your domain | `admin.directory.orgunit` |
   | View and manage the provisioning of domains for your customers | `admin.directory.domain` |
   | View and manage the provisioning of user schemas on your domain | `admin.directory.userschema` |
   | View and manage the provisioning of groups on your domain | `admin.directory.group` |
   | View and manage group subscriptions on your domain | `admin.directory.group.member` |
   | View and manage data transfers between users in your organization | `admin.datatransfer` |
   | Manage your mobile devices by performing administrative tasks | `admin.directory.device.mobile.action` |
   | View audit reports for your Google Workspace domain | `admin.reports.audit.readonly` |
   | View usage reports for your Google Workspace domain | `admin.reports.usage.readonly` |
   | Manage delegated admin roles for your domain | `admin.directory.rolemanagement` |
   | Manage data access permissions for users on your domain | `admin.directory.user.security` |
   
   Refer to the [Google Directory API scopes](https://developers.google.com/admin-sdk/directory/v1/guides/authorizing) or [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes) guide for more information about scopes.
   
7. Click **Sign in with Google**.
   
   ![Connect to Google Workspace](/assets/setup-1.CAQwtw4I.png)_Connect to Google Workspace_
   
8. Sign in with your Google account. Your Google account must have admin privileges to make organization-wide changes in Google Workspace.
   
9. Click **Allow** to enable Workato to access your Google account.
   
   ![Enable Workato to access your Google account](/assets/oauth-scopes.qLH22Y9E.png)_Enable Workato to access your Google account_
   

### Service account authentication

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

##### Set up a Google service account

Complete the following steps to set up a Google service account:

1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
   
2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account.
   
   ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
   
3. Click the **Email** of the service account you intend to use.
   
   ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
   
4. Copy the service account's **Email** and save it to configure your connection later.
   
   ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
   
5. Go to the **KEYS** tab.
   
6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
   
7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
   

You must enable the Google Workspace API to complete the connection setup.

> **REQUIRED SCOPES FOR SERVICE ACCOUNT AUTHENTICATION**
> 
> Ensure that you have the following required permissions to successfully connect to Google Workspace using a service account:
> 
> - `admin.directory.user`
> - `admin.directory.orgunit`
> - `admin.directory.domain`
> - `admin.directory.group`
> - `admin.directory.group.member`
> - `admin.datatransfer`
> - `admin.directory.device.mobile.action`
> - `admin.directory.userschema`
> - `admin.reports.audit.readonly`
> - `admin.reports.usage.readonly`
> - `admin.directory.rolemanagement`
> - `admin.directory.user.security`
> 
> The service account impersonates the user based on the email address you provide during the connection setup after authentication is complete.

#### Complete setup in Workato

Complete the following steps to connect to Google Workspace using service account authentication:

Service account authentication requires the following prerequisites:

- [Create a service account and generate a private key](#set-up-a-google-service-account)
- [Enable the Google Workspace API](https://support.google.com/googleapi/answer/6158841)

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Workspace** as your connection.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Service account**.
   
6. Enter the service account's email address in the **GCP project service account email** field.
   
   ![Retrieve your GCP Project service account email](/assets/service-auth-email.BdQybqOr.png)_Retrieve your GCP Project service account email_
   
7. Enter the **Private key** and **User email**. Retrieve the private key from the downloadable JSON. Include both the `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n`.
   
8. Click **Sign in with Google**.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/trigger-new-admin-activity-event.md
description: >-
  This trigger runs the recipe every time a Google admin performs an activity in
  the Google Workspace.
---

# Google Workspace - New admin activity event trigger

The **New admin activity event** trigger runs the recipe every time a Google admin performs an activity in Google Workspace, such as creating a new resource in Calendar or changing a Gmail setting for an organizational unit.

### Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Enter the date and time when the trigger starts monitoring for events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Event name | Locate the Google Workspace app in Google's [Admin event names](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/admin-event-names) guide to find the event name. Use the value from the **Event name** row that corresponds with the activity you plan to monitor. For example, to configure the trigger to monitor for new Calendar resources, enter `CREATE_CALENDAR_RESOURCE`. |
| Filters | Select filters to narrow down the returned list of events. Separate each filer with a comma. Refer to Google's [filter parameter](https://developers.google.com/admin-sdk/reports/reference/rest/v1/activities/list#query-parameters) guide for more information. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Event name** selection.

### Output

The **Create object** action's output fields vary based on your selected Object type. Refer to [Google Workspace's API documentation](https://developers.google.com/workspace) for more information about the output fields for each type.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/trigger-new-app-activity-event.md
description: >-
  The New application event trigger runs the recipe every time a specific event
  occurs in the selected Google Workspace application.
---

# Google Workspace - New application event trigger

The **New application event** trigger runs the recipe every time a specific event occurs in the selected Google Workspace application.

### Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Enter the date and time when the trigger starts monitoring for events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Application name | Select the Google Workspace app you plan to monitor from the drop-down list. |
| Event name | Enter the **Event name** of the event you plan to monitor. Open the [Google Workspace API reference](https://developers.google.com/admin-sdk/reference-overview) and go to the **Reports > Activity audit** page for your workspace app to find the **Event name**. Copy the value from the **Event name** row of the activity you plan to monitor. For example, enter `change_calendar_acls` to configure the trigger to monitor changes to a calendar. |
| Filters | Enter filters to narrow down the returned list of events. Separate each filter with a comma. Refer to the [filter parameters](https://developers.google.com/admin-sdk/reports/reference/rest/v1/activities/list#query-parameters) for more information. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional input fields based on your **Event name** selection.

### Output

The **Create object** action's output fields vary based on your selected Object type. Refer to [Google Workspace's API documentation](https://developers.google.com/workspace) for more information about the output fields for each type.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/trigger-new-user-event.md
description: >-
  The **New user event** trigger listens to new user related events that are
  created in your Google Workspace instance.
---

# Google Workspace - New user event trigger

The **New user event** trigger monitors your Google Workspace instance for new user related events. This trigger processes each event as a separate job.

### Input

| Input field | Description |
| --- | --- |
| User Event | Select the user event to monitor. Options include `User created`, `User deleted`, `User Admin status changed`, `User undeleted`, and `User updated.` |
| Domain | Select the domain to retrieve users from. Leave this field blank to retrieve users from all domains. |

### Output

The **Create object** action's output fields vary based on your selected Object type. Refer to [Google Workspace's API documentation](https://developers.google.com/workspace) for more information about the output fields for each type.

---
