---
url: 'https://docs.workato.com/en/connectors/netsuite-rest/new-updated-trigger.md'
description: >-
  The New or updated standard record trigger detects when records are created or
  updated in NetSuite REST.
---

# NetSuite REST - New or updated standard record trigger

The **New or updated standard record** trigger detects when a standard record is created or updated in NetSuite REST.

Use this trigger to monitor supported NetSuite records for changes. The trigger uses a date field for polling and manages this field automatically.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record to monitor. Only [REST Web Services supported records](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_1558962745.html) appear in the list. |
| When first started, this recipe should pick up events from | Enter the date and time to start polling from. Leave empty to retrieve records from the last hour. |
| Search query | Enter a search query to filter records. For example, `email START_WITH barbara`. Don't filter by the date field used for polling. |
| Search settings | Configure how the trigger retrieves and filters records. Refer to [Record Collection Filtering](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_1545222128.html) for more information. |

Additional fields appear and update dynamically based on the **Record** you select.

## Output

The output fields vary based on the **Record** you select. The trigger returns fields that correspond to the NetSuite record you selected.

For example, if you select **Account**, the output includes the following fields:

| Output field | Description |
| --- | --- |
| Account context search | The context used to search for the account. |
| Display Name | The display name of the account. |
| Name | The name of the account. |
| Number | The account number. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/attach-contact-to-record-action.md
description: >-
  The Attach contact to record action attaches a contact to a record in NetSuite
  REST.
---

# NetSuite REST - Attach contact to a record action

The **Attach contact to a record** action attaches a contact to a record in NetSuite REST.

Use this action to associate an existing contact with a NetSuite record. Refer to [REST Web Services prerequisites and setup](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) for setup requirements.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to attach the contact to. The picklist shows only records supported by NetSuite REST Web Services. Toggle the field to use a custom record. |
| Internal ID | Enter the internal ID of the record to attach the contact to. |
| Contact ID | Enter the internal ID of the contact to attach. |
| Contact role ID | Optional. Enter the internal ID of the contact role to assign to the contact. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the contact was attached to the record successfully. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/attach-file-to-record-action.md
description: The Attach file to record action attaches a file to a record in NetSuite REST.
---

# NetSuite REST - Attach file to a record action

The **Attach file to a record** action attaches a file to a record in NetSuite REST.

Use this action to associate an existing file with a NetSuite record. Refer to [REST Web Services prerequisites and setup](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) for setup requirements..

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to attach the file to. The picklist shows only records supported by NetSuite REST Web Services. Toggle the field to use a custom record. |
| Internal ID | Enter the internal ID of the record to attach the file to. |
| File ID | Enter the internal ID of the file to attach. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the file was attached to the record successfully. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/create-custom-record-action.md
description: >-
  The Create custom record action in the NetSuite REST connector lets you create
  a custom record in NetSuite.
---

# NetSuite REST - Create custom record action

The **Create custom record** action allows you to insert a custom record into NetSuite REST.

Refer to the NetSuite [Prerequisites and Setup for REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) guide for more information.

## Input

| Input field | Description |
| --- | --- |
| Custom record | Select a NetSuite custom record type, or toggle to enter a custom value. The list populates from the custom record types located in your account at **Customization > Records > Record Types**. |
| Reference Name | Enter a reference name for the record. |

Additional optional fields appear based on the **Custom record** type you select.

## Output

| Output field | Description |
| --- | --- |
| Location | The location ID of the record created. |
| Internal ID | The internal ID of the record created. |

---
