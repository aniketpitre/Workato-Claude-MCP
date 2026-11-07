---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/add-contact-to-list-batch.md
description: >-
  The Add contact to list batch action adds existing contact records to a
  contact list in HubSpot.
---

# HubSpot - Add contact to list action (batch)

The **Add contact to list** batch action adds existing contact records to a contact list. You can only add contacts to a static HubSpot list, not to a dynamic list.

## Input

| Input field | Description |
| --- | --- |
| List | The ID of the target contact list you plan to add contacts to. |
| Contact IDs | Contact IDs source list | The array of contacts to be added to the list. |
| ID | The ID of the contact to be added to the list. |

## Output

| Output field | Description |
| --- | --- |
| Record IDs removed | Record IDs of contacts that have been removed from the list. |
| Record IDs added | Record IDs of contacts successfully added to the list. |
| Record IDs missing | Record IDs of contacts not found in your HubSpot instance. |
