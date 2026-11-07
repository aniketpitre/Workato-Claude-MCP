---
url: 'https://docs.workato.com/en/connectors/insightly/new-contact-trigger.md'
description: >-
  The New contact trigger in the Insightly connector picks up new contacts
  created in your Insightly instance, processing each as an individual job.
---

# Insightly - New contact trigger

This trigger picks up new contacts that are created in your Insightly instance. Each new contact is processed as an individual job.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | How often to poll for new contacts. |
| When first started, this recipe should pick up events from | Contacts created after this time are processed by the recipe. If left blank, the default is set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output of this trigger is a datatree that contains information about the new [contact](https://api.insightly.com/v3.1/Help#!/Contacts/GetEntities).

---
