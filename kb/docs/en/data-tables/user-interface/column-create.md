---
url: 'https://docs.workato.com/en/data-tables/user-interface/column-create.md'
description: >-
  Create a new column in a Workato data table and set its name, column type,
  default value, and hint from the data tables interface.
---

# Create a new column

To create a new column:

1. Click the **+** (plus) button.
   
2. Choose a **column name, column type, default value** (optional), and **hint** (optional) for your column.
   
3. Alternatively, you can also create a new column by clicking **...** (ellipsis) next to the column name. Select **insert column left** or **insert column right** to create a new column next to an existing column.
   

![Data tables](/assets/data-table-column-create.Df-N8nVq.png)_Add a new column_

* * *

## Create a new column with keyboard shortcuts

* * *

### Mac

Press **command + i** to create a new column on Mac.

### Windows

Press **ctrl + i** to create a new column on Windows.

See [Keyboard shortcuts](/en/data-tables/user-interface/keyboard-shortcuts) for a complete list of keyboard shortcuts you can use to interact with your data tables.

* * *

## Supported column types

Reference our [column types](/en/data-tables/user-interface/column-types) documentation for a list of column types data tables support.

* * *

## Default values

Set the default value for each column (optional). Workato assigns the default value to all new records when the user does not provide any other value. If the column is marked as **Required** and the table already has rows, Workato automatically assigns the default value to all records.

Workato automatically assigns a default value for **Date** and **DateTime** column types. Users can determine the default value for all other column types except the **Link to another table** and **File** column types.

* * *

## Hints

Assign a hint for each column (optional). If you choose to assign a hint to a column, Workato displays the hint in the recipe editor, under the input field. Workato also displays the hint as a tooltip when you view a data table.

![Data tables](/assets/image12.CNDj8Zi0.png)_Workato displays hints in the recipe editor_

* * *

## Set as required

Set the column as required (optional). If you choose to set the column as required, the user must add data to the column when adding a new row. If you do not add data to a required column, Workato displays an error message, and cannot save the record, until you add data to the column.

Certain [column types](/en/data-tables/user-interface/column-types) cannot be marked as required. These include the **Link to another table** and **File** column types.

---
