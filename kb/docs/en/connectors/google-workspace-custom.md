---
url: 'https://docs.workato.com/en/connectors/google-workspace-custom.md'
description: >-
  The Google Workspace (Custom) connector uses Google batch APIs to automate
  user and group management, including creation, updates, aliases, and
  membership.
---

# Google Workspace (Custom)

[Google Workspace](https://developers.google.com/workspace/guides/get-started) offers tools to integrate with or extend apps like Gmail, Drive, and Chat. This custom connector enables efficient user and group management using [Google's batch APIs](https://developers.google.com/workspace/admin/directory/v1/guides/batch), allowing streamlined operations like user creation, updates, alias handling, and group membership—all optimized with batch processing to reduce API calls and boost performance.

## Prerequisites

To connect to the custom Google Workspace connector, you must complete the following prerequisite steps:

- [Set up your Google Cloud project](#cloud-project)
- Complete steps specific to your authentication method:
  - **OAuth 2.0**: [Create OAuth 2.0 credentials](#oauth-prerequisites)
  - **Service account**: [Set up your service account](#service-account-prerequisites)
- [Assign Super Admin privileges in Google Workspace](#admin-access)

### Set up your Google Cloud project

Complete the following steps to set up your Google Cloud project:

1. Create or select an existing Google Cloud project.
   
2. Enable the **Admin SDK API** and any other required APIs (for example, Gmail, Drive, Chat) in the Google Cloud Console.
   

### Create OAuth 2.0 credentials

Complete the following steps to create OAuth 2.0 credentials:

1. In your Google Cloud project, navigate to the Cloud Console.
   
2. Select **APIs & Services > Credentials**.
   
3. Click **\+ Create credentials** and select **OAuth client ID**.
   
4. Configure the consent screen and authorized redirect URIs.
   

Use this method for user-level access instead of domain-wide admin control.

### Set up your service account

1. Create a service account and enable **Domain-wide delegation**.
   
2. Download the service account JSON key file.
   
3. In the Google Admin Console, authorize the client ID and grant the necessary scopes. Example scopes include:
   
   - `https://www.googleapis.com/auth/cloud-platform`
   - `https://www.googleapis.com/auth/directory.user`
   - `https://www.googleapis.com/auth/admin.directory.user`
   - `https://www.googleapis.com/auth/admin.directory.group`
   - `https://www.googleapis.com/auth/admin.directory.group.member`

### Assign Super Admin privileges in Google Workspace

Super Admin access is required to manage users, groups, scopes, and service account delegation.

Refer to the [Google Workspace Admin Help documentation](https://support.google.com/a/answer/172176?hl=en&co=DASHER._Family%3DDomain-verified) for steps on how to assign these privileges.

## How to connect to Google Workspace (Custom)

The Google Workspace custom connector supports the following authentication methods:

- [OAuth 2.0 (user-delegated access)](#oauth-2-0)
- [Service account (domain-wide delegation)](#service-account)

### OAuth 2.0

Complete the following steps to establish a connection to the Google Workspace custom connector using OAuth 2.0 authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Workspace (Custom)** as your connection on the **New connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
   ![OAuth Connection Setup](/assets/oauth.BwlRZCfp.png)_OAuth Connection Setup_
   
4. Select **OAuth 2.0** as the **Authentication type**.
   
5. Enter the **Client ID** and **Client secret** from your Google Cloud project.
   
6. Click **Sign in with Google**.
   
7. Select your Google account and grant the required permissions.
   

### Service account

Complete the following steps to establish a connection to the Google Workspace custom connector using service account authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Workspace (Custom)** as your connection on the **New connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
   ![Service Account Connection Setup](/assets/service.n18k7gjG.png)_Service Account Connection Setup_
   
4. Select **Service account** as the **Authentication type**.
   
5. Enter the email address of the service account in the **Issuer** field.
   
6. Enter the private key from your downloaded JSON key in the **Private key** field.
   
7. Enter email address of the user to impersonate in the **Email address** field.
   
8. Click **Sign in with Google**.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-workspace-custom/create-records-action.md
description: >-
  The Create records action enables you to create multiple records in Google
  Workspace.
---

# Google Workspace (Custom) - Create records action

The **Create records** action enables you to create multiple records in Google Workspace.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create records for. Fields load dynamically based on the object you select. |

For example, the following input fields correspond to the **Users** object.

| Input field | Description |
| --- | --- |
| Users | Provide the details for the users you plan to create. |
| Primary email | Provide the user's primary email address. |
| Password | Provide the user's password. |
| Suspended | Indicates if the user is suspended. |
| Change password at next login | If true, the user must change their password at the next login. |
| IP whitelisted | Indicates if the IP is whitelisted. |
| Name | Provide objects containing the user's name information. |
| Emails | Provide values for the user's email addresses object. |
| External ids | Provide values for the user's external IDs object. |
| Relations | Provide values for the user's relations object. |
| Aliases | Provide values for the object of email aliases for the user. |
| Addresses | Provide details for the user's addresses. |
| Organizations | Provide values for the user's organization object. |
| Last login time | Provide the last login timestamp. |
| Phones | Provide values for the user's phone numbers object. |
| Suspension reason | Provide a reason for suspension. |
| Thumbnail photo URL | Provide the URL of the user's thumbnail photo. |
| Languages | Provide values for the languages users speak. |
| POSIX accounts | Provide values for POSIX (Portable Operating System Interface) accounts. |
| SSH public keys | Provide values for the user's SSH public keys object. |
| Notes | Provide details for the user’s notes object. |
| Websites | Provide values for the user's website object. |
| Locations | Provide users' locations. |
| Include in global address list | Specify if the user is in the global address list. |
| Keywords | Provide values for the user's keywords object. |
| Deletion time | Provide the time when the user was deleted. |
| Gender | Provide values for the user's gender object. |
| Thumbnail photo ETag | Provide the eTag of the thumbnail photo. |
| Instant messenger accounts | Provide instant messaging accounts. |
| Recovery email | Provide a recovery email address. |
| Recovery phone | Provide recovery phone number. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, the following output fields correspond to the **Users** object.

| Output field | Description |
| --- | --- |
| Users | An array of User objects. |
| Primary email | The user's primary email address. |
| Suspended | Indicates if the user is suspended. |
| Change password at next login | If true, the user must change their password at the next login. |
| IP whitelisted | Indicates if the IP is whitelisted. |
| Name | Object containing the user's name information. |
| Kind | Type of the resource. |
| Etag | ETag of the resource. |
| Emails | Users' email addresses. |
| External ids | Object for the user's external IDs. |
| Relations | Object containing the user's relations. |
| Aliases | Object of email aliases for the user. |
| Addresses | An object that contains the user's addresses. |
| Organizations | Object containing the user's organizations. |
| Last login time | Last login timestamp. |
| Phones | Users' phone numbers. |
| Suspension reason | Reason for suspension. |
| Thumbnail photo URL | URL of the user's thumbnail photo. |
| Languages | Languages the user speaks. |
| POSIX accounts | POSIX (Portable Operating System Interface) accounts information. |
| SSH public keys | Object for the user's SSH public keys. |
| Notes | Object that contains user notes details. |
| Websites | Object containing the user's website information. |
| Locations | User's locations object. |
| Include in global address list | Indicates if the user is in the global address list. |
| Keywords | User's keywords. |
| Deletion time | Time when the user was deleted. |
| Gender | User's gender. |
| Thumbnail photo ETag | ETag of the thumbnail photo. |
| Ims | Instant messaging accounts object. |
| Org unit path | Path to organizational unit. |
| Recovery email | Recovery email address. |
| Recovery phone | Recovery phone number. |

---

---
url: >-
  https://docs.workato.com/en/connectors/google-workspace-custom/delete-records-action.md
description: >-
  The Delete records action enables you to delete multiple records in Google
  Workspace.
---

# Google Workspace (Custom) - Delete records action

The **Delete records** action enables you to delete multiple records in Google Workspace.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to delete records from. Fields load dynamically based on the object you select. |

For example, the following input fields correspond to the **Membership** object.

| Input field | Description |
| --- | --- |
| Group email address | Enter the value for the group email address. |
| Group member email address | Provide the group members’ email addresses. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, the following output fields correspond to the **Membership** object.

| Output field | Description |
| --- | --- |
| Status | Status of the membership after the delete operation. |

---

---
url: >-
  https://docs.workato.com/en/connectors/google-workspace-custom/get-records-action.md
description: >-
  The Update record action enables you to retrieve multiple records in Google
  Workspace.
---

# Google Workspace (Custom) - Get records action

The **Get records** action enables you to retrieve multiple records in Google Workspace.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve details for. Fields load dynamically based on the object you select. |

For example, the following input fields correspond to the **Groups** object.

| Input field | Description |
| --- | --- |
| User keys | Provide the array of keys for group members. |
| Group member email address | Provide the group members’ email addresses. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, the following output fields correspond to the **Groups** object.

| Output field | Description |
| --- | --- |
| Groups | Array of group objects. |
| Kind | Kind of the resource. |
| ID | Unique identifier for the group. |
| Entity tag | Entity tag for the group. |
| Group email | Group’s email address. |
| Group name | Group’s name. |
| Direct members count | Number of direct members in the group. |
| Description | Description of the group. |
| Admin created | Indicates if the group was created by an admin. |
| Aliases | The object of email aliases associated with the group. |
| Non editable aliases | Object of email aliases that cannot be edited. |

---

---
url: >-
  https://docs.workato.com/en/connectors/google-workspace-custom/update-records-action.md
description: >-
  The Update records action enables you to update the details of multiple
  records in Google Workspace.
---

# Google Workspace (Custom) - Update records action

The **Update records** action enables you to update the details of multiple records in Google Workspace.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object type of the records you plan to update. Fields load dynamically based on the object you select. |

For example, the following input fields correspond to the **Membership** object.

| Input field | Description |
| --- | --- |
| Members | An array of Member objects. |
| Group email address | Provide the group’s email address. |
| Group member email address | Provide the group members’ email addresses. |
| Mail delivery preferences | Provide preference for mail delivery. |
| Group member role | Provide a role for the group member. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, the following output fields correspond to the **Membership** object.

| Output field | Description |
| --- | --- |
| Group Member | An array of group member objects. |
| ID | Unique identifier for membership. |
| Kind | Kind of the resource. |
| Entity tag | Entity tag for the membership. |
| Member email | Email address of group member. |
| Member type | Details about the type of member. |
| Member status | Current status of the member. |
| Delivery preference | Preference for mail delivery. |

---
