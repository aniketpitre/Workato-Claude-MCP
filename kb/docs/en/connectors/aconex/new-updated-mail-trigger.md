---
url: 'https://docs.workato.com/en/connectors/aconex/new-updated-mail-trigger.md'
description: The New/updated mail trigger monitors Aconex for new or updated mail items.
---

# Aconex - New/updated mail trigger

The **New/updated mail** trigger monitors Aconex for new or updated mail items.

## Input

| Input field | Description |
| --- | --- |
| Project | Select the project to monitor for new/updated mail items. |
| Mail box | Select the mailbox to monitor for new/updated mail items. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| Mail ID | The ID of the new/updated mail item. |
| Last modified date | The date that the new/updated mail item was modified. |

---

---
url: >-
  https://docs.workato.com/en/connectors/aconex/check-document-registration-status-action.md
description: >-
  The Check document registration status action checks the background job for
  the status of large file registration in Aconex.
---

# Aconex - Check document registration status action

The **Check document registration status** action checks the background job for the status of large file registration in Aconex.

## Input

| Input field | Description |
| --- | --- |
| Project | Enter the project ID of the document registration status you plan to check. |
| Job ID | Enter the job ID of the large file registration. |

## Output

| Output field | Description |
| --- | --- |
| Job ID | The ID of the job associated with the document registration status. |
| Project ID | The ID of the project associated with the document registration status. |
| Status | The status of the document registration. |
| Document ID | The ID of the registered document. |
| Error message | A message indicating the reason the action failed, if applicable. |

---
