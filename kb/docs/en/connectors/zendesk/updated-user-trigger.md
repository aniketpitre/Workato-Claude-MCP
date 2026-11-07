---
url: 'https://docs.workato.com/en/connectors/zendesk/updated-user-trigger.md'
description: >-
  The New/updated user trigger in the Zendesk connector picks up created or
  updated users, processing each as a separate job per poll interval.
---

# Zendesk - New/updated user trigger

This trigger picks up users that are created or updated. Each user is processed as a separate job. It checks for new jobs once every poll interval.

> **Role privileges**
> 
> You need a Zendesk account with the Administrator role to use this trigger in your recipe.

![New/updated user trigger](/assets/updated-user-trigger.DrXs9RQw.png)_New/updated user trigger_

## Input

| Input field | Description |
| --- | --- |
| From | Users created or updated after this time will be processed by the recipe. If left blank, the default date will be set to **one day** before the recipe is first started. |

## Output

The output of this action contains the full set of columns from the selected user. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the user. This is automatically assigned when the user is created. |
| Role | The role of the user. Permitted values are `End-user`, `Agent`, or `Administrator`. |
| Email | The primary email of the user. |
| Organization ID | The unique Zendesk ID of the user's organization. If the user has more than one organization membership, it will display the user's default organization. |
| User custom fields | Includes data of user custom fields. |

Click here for a full list of [user outputs](/en/connectors/zendesk/user-fields#user-output-fields).

---
