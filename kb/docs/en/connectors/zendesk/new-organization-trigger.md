---
url: 'https://docs.workato.com/en/connectors/zendesk/new-organization-trigger.md'
description: >-
  The New organization trigger in the Zendesk connector picks up newly created
  organizations, processing each as a separate job per poll interval.
---

# Zendesk - New organization trigger

This trigger picks up new organizations that are created. Each organization is processed as a separate job. It checks for new organizations once every poll interval.

> **Role privileges**
> 
> You need a Zendesk account with the Administrator role to use this trigger in your recipe.

![New organization trigger](/assets/new-organization-trigger.DcdIBEJO.png)_New organization trigger_

## Input

| Input field | Description |
| --- | --- |
| From | Organizations created after this time will be processed by the recipe. If left blank, the default date will be set to **one day** before the recipe is first started. |

## Output

The output of this trigger contains the full set of columns from the selected organization. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the organization. This is automatically assigned when the organization is created. |
| Group ID | The unique Zendesk ID of the group of this organization. |
| Organization custom fields | Includes data of organization custom fields. |

Click here for a full list of [organization outputs](/en/connectors/zendesk/organization-fields#organization-output-fields).

---
