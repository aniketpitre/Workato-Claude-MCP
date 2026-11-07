---
url: 'https://docs.workato.com/en/connectors/wrike/modify-user-action.md'
description: >-
  The Modify user action in the Wrike connector updates the details of a user
  that you identify by user ID in Wrike.
---

# Wrike - Modify user action

The **Modify user** action updates a user’s details in Wrike. You can retrieve the user ID from the [List users](/en/connectors/wrike/list-users-action) action.

## Input

| Input field | Description |
| --- | --- |
| User ID | Enter the ID of the user to update. |
| Job role ID | Enter the job role ID to assign to the user. |
| Current bill rate | Expand to define the bill rate details for the user. |
| Rate scope | Define the scope for the bill rate. |
| Rate source | Define the source for the bill rate, such as **Job role** or **User**. |
| Rate value | Enter the bill rate value. Leave empty if the rate source is **Job role**. |
| Current cost rate | Expand to define the cost rate details for the user. |
| Rate scope | Define the scope for the cost rate. |
| Rate source | Define the source for the cost rate, such as **Job role** or **User**. This field is required. |
| Rate value | Enter the cost rate value. Leave empty if the rate source is **Job role**. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier for the updated user. |
| First name | First name of the user. |
| Last name | Last name of the user. |
| Type | Type of user account. |
| Profiles | List of user profiles associated with the account. |
| Avatar URL | URL of the user’s avatar image. |
| Timezone | Time zone set in the user’s profile. |
| Locale | Language and region settings of the user. |
| Deleted | Indicates whether the user is deleted. |
| Me | Indicates whether the updated user is the authenticated user. |
| Metadata | Additional metadata associated with the user. |
| Title | Job title of the user, if applicable. |
| Company name | Name of the company the user is associated with. |
| Phone | Phone number of the user, if available. |
| Primary email | Primary email address of the user. |

---
