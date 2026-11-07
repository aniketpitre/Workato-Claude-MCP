---
url: 'https://docs.workato.com/en/connectors/teams/get-user-action.md'
description: The Get user action gets user details by ID in Microsoft Teams.
---

# Microsoft Teams - Get user action

The **Get user** action gets user details by ID in Microsoft Teams.

## Input

| Input field | Description |
| --- | --- |
| User ID | Enter the user ID (GUID) or user principal name (UPN). For example, [john@contoso.com](mailto:john@contoso.com). Enter `me` to get the signed-in user profile. `me` isn't available if you're using client credentials authentication. Provide a user ID or UPN instead. |

## Output

| Output field | Description |
| --- | --- |
| @odata.context | The metadata URL property in the OData JSON response. It describes the structure, type, and location of the returned data. |
| User ID | The user unique identifier. |
| Email | The user email address. |
| User principal name | The user principal name. |
| Job title | The user job title. |
| Department | The department the user is in. |
| Office location | The user office location. |
| Mobile phone | The user mobile phone number. |
| Business phone | The user business phone number. |
| Account enabled | A boolean response (`true` or `false`) that indicates if the user account is active, permitted to sign in, and enabled within the Microsoft Entra ID tenant. |
| Created date | The date the user was created. |

---
