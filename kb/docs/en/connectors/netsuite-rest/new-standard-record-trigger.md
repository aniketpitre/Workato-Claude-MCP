---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/new-standard-record-trigger.md
description: >-
  The New standard record trigger detects when a standard record is created in
  NetSuite REST.
---

# NetSuite REST - New standard record trigger

The **New standard record** trigger detects when a standard record is created in NetSuite REST.

Use this trigger to monitor NetSuite records for new entries. The trigger polls using the record's creation date field.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record to monitor for new records. Only REST Web Services supported records appear in the list. |
| When first started, this recipe should pick up events from | Enter the date and time to start polling from. Leave empty to retrieve records from the last hour. |
| Search query | Enter a search query to filter records. For example, `email START_WITH barbara`. Don't filter by the date field used for polling. |
| Search settings | Configure how the trigger retrieves and filters records. Refer to [Record Collection Filtering](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_1545222128.html) for more information. |

Additional fields appear and update dynamically based on the **Record** you select.

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

Additional fields appear based on the **Record** you select. These fields correspond to the NetSuite record you select.
