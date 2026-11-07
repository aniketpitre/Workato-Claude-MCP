---
url: 'https://docs.workato.com/en/connectors/insightly/updated-contact-trigger.md'
description: >-
  The Updated contact trigger in the Insightly connector picks up contacts
  updated in your Insightly instance, processing each as an individual job.
---

# Insightly - Updated contact trigger

This trigger picks up contacts that are updated in your Insightly instance. Each updated contact is processed as an individual job.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | How often to poll for updated contacts. |
| When first started, this recipe should pick up events from | Contacts updated after this time are processed by the recipe. If left blank, the default is set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output of this trigger is a datatree that contains information about the updated [contact](https://api.insightly.com/v3.1/Help#!/Contacts/GetEntities).

---

---
url: >-
  https://docs.workato.com/en/connectors/insightly/updated-organization-trigger.md
description: >-
  The Updated organization trigger in the Insightly connector picks up
  organizations updated in your Insightly instance, processing each as a job.
---

# Insightly - Updated organization trigger

This trigger picks up organizations that are updated in your Insightly instance. Each updated organization is processed as an individual job.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | How often to poll for updated organizations. |
| When first started, this recipe should pick up events from | Organizations updated after this time are processed by the recipe. If left blank, the default is set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output of this trigger is a datatree that contains information about the updated [organization](https://api.insightly.com/v3.1/Help#!/organizations/GetEntity).

---

---
url: >-
  https://docs.workato.com/en/connectors/insightly/updated-opportunity-trigger.md
description: >-
  The Updated opportunity trigger in the Insightly connector picks up
  opportunities updated in your Insightly instance, processing each as a job.
---

# Insightly - Updated opportunity trigger

This trigger picks up opportunities that are updated in your Insightly instance. Each updated opportunity is processed as an individual job.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | How often to poll for updated opportunities. |
| When first started, this recipe should pick up events from | Opportunities updated after this time are processed by the recipe. If left blank, the default is set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output of this trigger is a datatree that contains information about the updated [opportunity](https://api.insightly.com/v3.1/Help#!/Opportunities/GetEntities).

---
