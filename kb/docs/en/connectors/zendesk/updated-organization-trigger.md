---
url: 'https://docs.workato.com/en/connectors/zendesk/updated-organization-trigger.md'
description: >-
  The New/updated organization trigger in the Zendesk connector picks up created
  or updated organizations as separate jobs per poll interval.
---

# Zendesk - New/updated organization trigger

This trigger picks up organizations that are created or updated. Each organization is processed as a separate job. It checks for new jobs once every poll interval.

> **Role privileges**
> 
> You need a Zendesk account with the Administrator role to use this trigger in your recipe.

![New/updated organization trigger](/assets/updated-organization-trigger.DoiX4jB7.png)_New/updated organization trigger_

## Input

| Input field | Description |
| --- | --- |
| From | Organizations created or updated after this time will be processed by the recipe. If left blank, the default date will be set to **one day** before the recipe is first started. |

## Output

The output of this trigger contains the full set of columns from the selected organization. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the organization. This is automatically assigned when the organization is created. |
| Group ID | The unique Zendesk ID of the group of this organization. |
| Organization custom fields | Includes data of organization custom fields. |

Click here for a full list of [organization outputs](/en/connectors/zendesk/organization-fields#organization-output-fields).

---
