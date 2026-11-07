---
url: 'https://docs.workato.com/en/connectors/smartsheet/update-row.md'
description: >-
  The Update row action in the Smartsheet connector lets you update an existing
  row in a sheet, including its cell data, position, and formatting.
---

# Smartsheet - Update row action

The **Update row** action enables you to update an existing row within your Smartsheet sheet.

![Update row action](/assets/update-row-action.BznJ_Kdf.png)_Smartsheet - Update row action_

## Input

| Input field | Description |
| --- | --- |
| Sheet name | Select the Smartsheet where the row you plan to update is located. |
| Row ID | The unique identifier of the row in Smartsheet that you plan to update. |
| Columns | The columns in the Smartsheet where the data is updated. Leave this field blank to display the first 100 columns. |
| Parent ID | The ID of the parent row, if you are updating a child row. If `To bottom` is set to true, the system adds the row as the last child of the specified parent row. |
| Locked | Specifies whether the row should be locked after the update. |
| Expanded | Indicates if the row should be expanded to show details after the update. |
| Font | The font style to be applied to the text in the row. Valid values are 0 to 3. |
| Sibling ID | The ID of the sibling row, if the updated row is to be positioned relative to another row. If `above` is set to true, the system adds the row above the specified ID. Otherwise, it adds the row below the specified ID. |
| To top | If set, the updated row is moved to the top of the sheet. |
| To bottom | If set, the updated row is moved to the bottom of the sheet. |
| Above | The ID of the row above which the updated row should be positioned. If set to true, the system inserts the new row above the row specified by the `Sibling ID`. |
| Cells | Specific cell data to be updated in the row, such as `Task Name`, `Assigned To`, `Complete`, `Status`, and `Comments`. |

## Output

| Output field | Description |
| --- | --- |
| Row ID | The unique identifier of the row that was updated in Smartsheet. |
| Row number | The number assigned to the updated row within the sheet. |
| Parent ID | The ID of the parent row, if the updated row is a child row. |
| Parent row number | The row number of the parent row, if applicable. |
| Locked | Indicates whether the row is locked after the update. |
| Locked for user | Shows if the row is locked specifically for the user after the update. |
| Expanded | Indicates if the row details are expanded after the update. |
| Created at | The timestamp of when the row was first created. |
| Modified at | The timestamp of the last modification of the row. |
| Sibling ID | The ID of a sibling row, if the updated row is positioned relative to another row. |
| Cells | Details of the specific cell data in the row after the update, such as `Task Name`, `Assigned To`, `Complete`, `Status`, and `Comments`. |

---
