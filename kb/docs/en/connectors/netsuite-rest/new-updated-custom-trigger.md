---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/new-updated-custom-trigger.md
description: >-
  The New or updated custom record trigger detects when custom records are
  created or updated in NetSuite REST.
---

# NetSuite REST - New or updated custom record trigger

The **New or updated custom record** trigger detects when a custom record is created or updated in NetSuite REST.

Use this trigger to monitor custom record types for changes. The trigger polls using the last modified field. You must enable **Show Last Modified** on the custom record type in NetSuite to use this trigger.

## Input

| Input field | Description |
| --- | --- |
| Record type | Enter the NetSuite custom record type ID. For example, `customrecord_1087_testing`. You can find this ID in **Customization > Records > Record Types** in NetSuite. |
| When first started, this recipe should pick up events from | Enter the date and time to start polling from. Leave empty to retrieve records from the last hour. |
| Search query | Enter a search query to filter records. For example, `name CONTAIN test`. Don't filter by last modified. |
| Search settings | Configure how the trigger retrieves and filters records. Refer to [Record Collection Filtering](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_1545222128.html) for more information. |

Additional fields appear based on the **Record type** you select. These fields update dynamically to match the custom record schema you select.

## Output

The trigger returns the following standard fields:

| Output field | Description |
| --- | --- |
| Last modified by | The user who last modified the record. |
| Links | The related resource links for the record. |
| Owner | The owner of the record. |
| Reference Name | The reference name of the record. |
| User notes | Notes associated with the record. |
| Abbreviation | The abbreviation defined for the record. |
| Created | The date and time when the record was created. |

Additional fields appear based on the **Record type** you select. These fields include custom fields defined for the custom record type ID you specify.
