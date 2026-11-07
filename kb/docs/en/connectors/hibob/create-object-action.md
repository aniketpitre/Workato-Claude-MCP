---
url: 'https://docs.workato.com/en/connectors/hibob/create-object-action.md'
description: >-
  **Create object** action enables you to create any standard or custom record,
  such as employee, in HiBob.
---

# HiBob - Create object action

The **Create object** action enables you to create a standard or custom record, such as an employee record, in HiBob.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to create in the drop-down menu. |

Input fields are dynamically loaded based on the object you select. The following example shows the input for the **Company list item** object:

| Input fields | Description |
| --- | --- |
| List name | Provide the internal name of the list. |
| Name | Provide the name of the item to be created. |
| Parent ID | Provide the ID of new hierarchy parent node. |

## Output

The output fields are determined by the object you selected in the input. Map the relevant datapills from the data tree to subsequent steps. The following example provides the output for the **Company list item** object:

| Output field | Description |
| --- | --- |
| ID | Unique identifier for the created item. |

---
