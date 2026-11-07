---
url: 'https://docs.workato.com/en/data-tables/user-interface/view.md'
description: >-
  View, filter, sort, and hide columns in Workato data tables to organize
  records in the data table interface.
---

# View, filter, and sort table data

You can view table data in the Workato UI. The Data table interface enables you to filter, sort, and hide/display column data.

By default, the interface displays the first 200 (two hundred) records of the data table. Workato loads additional pages automatically as you scroll through the table.

## Filter

Create custom filters to organize your data. The types of available filters depend on the data type of the filtered column. You can add multiple filters. All filters are chained using AND.

User-generated filters are case-sensitive.

![Data tables](/assets/filter.CLdJqzTy.png)_Filter records with multiple filters_

To create a filter:

1. Click **\+ Add filter**.
   
2. Select a column to filter.
   
3. Select the type of filter.
   
4. Enter a value.
   
5. Click **✓** (check mark).
   

### Available operands

The following table lists the operands available for each data table column type.

| Column type | Available operands |
| --- | --- |
| ID | `equals`, `not equals` |
| String, File | `equals`, `not equals`, `is null`, `is not null`, `starts with` |
| Integer, Number | `equals`, `not equals`, `greater than`, `less than`, `greater than or equals`, `less than or equals`, `is null`, `is not null` |
| Date, Date-time | `equals`, `not equals`, `is after`, `is before`, `is on or after`, `is on or before`, `is null`, `is not null` |
| Boolean | `is true`, `is false`, `is null`, `is not null` |
| Relation | `equals`, `not equals`, `in`, `is null`, `is not null` |
| Set types (string set, number set, integer set, date set, date-time set, relation set) | `contains`, `is null`, `is not null` |

## Sort

Sort data in ascending or descending order by sorting an individual column.

If you sort one column and then an additional column, the most recent sort selection is applied, overriding the first sorting selection.

![Data tables](/assets/sort-columns.CmGx2iKm.png)_Sort column data_

Multi-value columns cannot be sorted. You can only sort single-value column types, such as text, number, date, and boolean.

Complete the following steps to sort column data:

1. Choose the column you plan to sort.
   
2. Next to the column name, click **...** (ellipsis).
   
3. Select **Sort descending** or **Sort ascending**. You can reverse the sort direction by clicking the ↑(arrow) next to the column name (optional).
   
   <dl><dt>Sort descending</dt><dd>Sorts column data in descending order.<br>For example, it sorts text fields in reverse alphabetical order, numeric fields from the highest number to the lowest, and date fields from most recent to most remote. Null values appear at the bottom of the sorted column.</dd><dt>Sort ascending</dt><dd>Sorts column data in ascending order.<br>For example, it sorts text fields in alphabetical order, numeric fields from the lowest number to the highest, and date fields from the most remote past to current time. Null values appear at the top of the column.</dd></dl>
   

## Hide and display columns

You can hide or display columns in your table. By default, Workato hides all auto-generated columns.

[Learn more about auto-generated columns](/en/data-tables/user-interface/create#auto-generated-columns).

![Data tables](/assets/image21.C_W0jER3.png)_Select/deselect column names to display/hide columns_

When you hide columns in the table, Workato informs you of this by updating the numerical value in the **Hide columns** button. For example, when you create a new table, this button reads **3 hidden columns**, referencing the three auto-generated columns that Workato hides by default. When you hide additional columns, Workato updates this button.

If you choose not to hide any columns, Workato displays this button as **Hide columns**.

To hide or display a column:

1. Click **Hide columns/X columns hidden**.
   
2. Workato displays a list of columns.
   
3. Hide a column by deselecting the column name. Conversely, to display a column, select that column name.

---
