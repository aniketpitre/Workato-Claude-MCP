---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/remove-contact-from-list-batch.md
description: >-
  The Remove contact from list batch action in the HubSpot connector removes
  contacts from a specified static list in your HubSpot instance.
---

# HubSpot - Remove contact from list action (batch)

The **Remove contact from list** batch action removes contacts from a specified contact list. You can only remove a contact from a static HubSpot list, not from a dynamic list.

## Input

| Input field | Description |
| --- | --- |
| List | The ID of the target contact list where you plan to remove contacts. |
| Contact IDs | Contact IDs source list | The array of contacts to be removed from the list. |
| ID | The ID of the contact you plan to remove from the list. |

## Output

| Output field | Description |
| --- | --- |
| Record IDs removed | Record IDs of contacts removed from the list. |
| Record IDs added | Record IDs of contacts successfully added to the list. |
| Record IDs missing | Record IDs of contacts not found in your HubSpot instance. |
