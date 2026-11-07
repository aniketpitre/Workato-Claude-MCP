---
url: 'https://docs.workato.com/en/connectors/jira/create-user-action.md'
description: This action creates a new user in your Jira instance.
---

# Jira - Create user action

The **Create user** action creates a new user in your Jira instance.

> **CREATING USERS INCREASES JIRA LICENSES**
> 
> Creating a new user increases the number of Jira licenses for your organization, which affects Jira subscription fees.

## Input

| Input field | Description |
| --- | --- |
| Email | Enter an email address for the user. |
| Password | Optional. Enter a password for the user. |
| Products | Select products to provide the new user access to. Select `none` to create a user without any product access. Leave the field empty to provide default access. |

## Output

| Output field | Description |
| --- | --- |
| Self URL | The API URL of the new user. |
| Key | The human-readable Jira identifier for the new user. |
| Name | The login username of the new user. |
| Account ID | The Atlassian account identifier for the new user. |
| Email address | The email address of the new user. |
| Avatar URLs | URLs for the new user's avatar images. |
| Display name | The display name of the new user. |
| Active | Indicates whether the new user's account is active. |
| Time zone | The timezone of the new user. |
| Locale | The language and formatting preferences of the new user. |
| Groups | Contains information about groups the new user is a member of, including `Size` and `Items`. |
| Application roles | Contains information about the application roles assigned to the new user, including `Size` and `Items`. |
| Expand | Fields expanded in the response, such as groups and application roles the user is a member of. |
| Last login time | The date and time the new user last logged in to Jira. |

## Troubleshooting

Ensure the connected Jira account has sufficient permissions to create users if you encounter difficulties with this action.

Refer to the [Jira connector permissions guide](/en/connectors/jira#jira-permissions-helper) or the Jira [Permissions helper](https://confluence.atlassian.com/adminjiracloud/using-the-permission-helper-868982879) documentation for more details.

---
