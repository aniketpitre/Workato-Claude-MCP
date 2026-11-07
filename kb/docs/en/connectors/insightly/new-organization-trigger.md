---
url: 'https://docs.workato.com/en/connectors/insightly/new-organization-trigger.md'
description: >-
  The New organization trigger in the Insightly connector picks up new
  organizations created in your Insightly instance, processing each as a job.
---

# Insightly - New organization trigger

This trigger picks up new organizations that are created in your Insightly instance. Each new organization is processed as an individual job.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | How often to poll for new organizations. |
| When first started, this recipe should pick up events from | Organizations created after this time are processed by the recipe. If left blank, the default is set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output of this trigger is a datatree that contains information about the new [organization](https://api.insightly.com/v3.1/Help#!/organizations/GetEntity).

---
