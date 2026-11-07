---
url: 'https://docs.workato.com/en/connectors/netsuite-rest/new-custom-trigger.md'
description: The New custom record trigger detects new custom records in NetSuite REST.
---

# NetSuite REST - New custom record trigger

The **New custom record** trigger detects new custom records in NetSuite REST.

Use this trigger to monitor custom record types by internal ID or created date. The polling strategy determines how the trigger retrieves new records.

## Input

| Input field | Description |
| --- | --- |
| Record type | Enter the NetSuite custom record type ID. For example, `customrecord_1087_testing`. You can find this ID from **Customization > Records > Record Types** in NetSuite. |
| Polling strategy | Select how the trigger retrieves new records. Select **By internal ID** to retrieve records based on internal ID. Select **By created date** to retrieve records based on created date. You must enable **Show Created Date** in NetSuite to use **By created date**. |
| When first started, this recipe should pick up events from ID | Enter the internal ID to start polling from. This field applies when you select **By internal ID**. The trigger processes records with IDs greater than this value. Leave empty to start from ID 0. |
| When first started, this recipe should pick up events from | Enter the date and time to start polling from. This field applies when you select **By created date**. |
| Search query | Enter a search query to filter records. For example, `name CONTAIN test`. Don't filter by internal ID. |
| Search settings | Configure how the trigger retrieves and filters records. Refer to [Record Collection Filtering](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_1545222128.html) for more information. |

Additional fields appear based on the selected **Record type**. These fields update dynamically to match the custom record schema you select.

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

---

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

---
