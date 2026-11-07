---
url: 'https://docs.workato.com/en/connectors/salesforce/actions/get-report.md'
description: This action retrieves report details from Salesforce.
---

# Salesforce - Get report by ID action

This action retrieves columns and rows from a Salesforce report.

## Input

| Input fields | Description |
| --- | --- |
| Report | Select a report to retrieve. Alternatively, use the drop-down menu to toggle this field to **Enter the report ID** and enter a report ID from the output of another action, such as [Search records](/en/connectors/salesforce/actions/search-records). |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

| Output fields | Description |
| --- | --- |
| Attributes | An object containing the report's attributes. For example: the `Report name`, `Report ID`, and `Type`. |
| Columns | An object containing information about the report's columns. For example: `Label`, `Name`, and `Type`. |
| Rows | An object containing information about the report's rows. For example: a `Columns` object, `List index`, and `List size`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/list-category-groups.md
description: This action retrieves all data category groups from Salesforce in batches.
---

# Salesforce - List data category groups action (batch)

This action retrieves all data category groups from Salesforce in batches.

## Input

There are no input fields for this action.

## Output

| Output fields | Description |
| --- | --- |
| Full name | The name of the data category group. |
| Created by ID | The Salesforce ID of the user who created the group. |
| Created date | The date and time the group was created. |
| Created by name | The name of the user who created the group. |
| File name | The file path and name for the group. |
| Last modified by ID | The Salesforce ID of the user who last modified the group. |
| Last modified date | The date and time the group was last modified. |
| Last modified by name | The name of the user who last modified the group. |
| Type | The object type. |
| List size | The total number of category group records returned. |
| List index | The position of the current category group record in the list. |

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/publish-platform-event.md
description: This action publishes a platform event message in Salesforce.
---

# Salesforce - Publish platform event action

This action publishes a platform event message in Salesforce.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the platform event to publish. |

Additional fields load dynamically based on the selected **Object**. Use these fields to configure the platform event message.

## Output

| Output fields | Description |
| --- | --- |
| Object ID | The Salesforce ID of the published platform event. |

---
