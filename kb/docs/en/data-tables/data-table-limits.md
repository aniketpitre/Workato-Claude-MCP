---
url: 'https://docs.workato.com/en/data-tables/data-table-limits.md'
description: >-
  Reference for Workato data table quotas, covering general table size, column,
  and connector trigger and action quotas.
---

# Quotas

Data tables have the following quotas:

> **DEFAULT QUOTAS**
> 
> The quotas on this page are defaults based on Workato best practices and are configured to enable optimal platform performance. Customers on Enterprise plans or above can contact their Customer Success Representative to request an extension of these quotas for their specific use cases.

## General data table quotas

| Description | Quota |
| --- | --- |
| Maximum number of data tables per workspace | 100 |
| Maximum number of rows per table | 1,000,000 |
| Maximum number of rows in a data table that can be [exported](/en/recipe-development-lifecycle/export.html#export-a-manifest-as-a-package) or [deployed](/en/features/environments/deployment.html#what-can-be-deployed) | 10,000 |
| Maximum number of columns per table | 100 |
| Maximum number of **Link to a table** column types per table | 20 |
| Maximum number of **Multi-value** column types per table | 20 |
| Maximum record size | 100,000 bytes |
| Maximum table size | 1,000,000,000 bytes |
| Maximum number of visible records (rows) at one time in the data tables UI | 200 |
| Maximum number of filters that can be applied simultaneously to a table in the data tables UI. Note that each additional filter is treated as an `AND` operand. | 10 |
| Maximum number of filters that can be applied to a field/column | 1 |

## Data table column quotas

| Column type | Description | Quota | Example |
| --- | --- | --- | --- |
| Short text | Text field used to store small strings or textual data. Typically, this data type is for names, short descriptions, status codes, or small identifiers. | Maximum of 10,000 characters. Sorting and filtering is supported for only the first 756 characters. | `A very short description`, `user@example.com`, `John Doe` |
| Long text | Multi-line text field. Typically, this data type is for large amounts of text, such as descriptions, comments, or any large block of text. | Maximum of 10,000 characters. Sorting and filtering is supported for only the first 756 characters. | `A long description or comment that can span many lines…` |
| Integer | Whole numbers without any fractional or decimal parts. Integers can represent both positive and negative values, including zero. | Integers are 64-bit (8-byte) and can range between `-9223372036854775808` and `9223372036854775807`. | `5000`, `100000`, `2147483647` |
| Decimal | IEEE-754 floating-point numbers. Commonly used for precise calculations involving fractional numbers, such as percentages or scientific measurements. | Floating-point numbers do not enforce a fixed number of decimal places. Precision is determined by the number’s range. For example, smaller values can represent more decimal places accurately, while larger values lose precision due to spacing between representable values. | `0.1`, `3.141592653589793`, `1.7976931348623157 × 10³⁰⁸` |
| Boolean | A true/false value. | NA | `TRUE`, `FALSE` |
| Date | Calendar dates (such as, year, month, and day) without time information. Useful for fields such as birthdates, event dates, or transaction dates. Date columns inherit the timezone and date and time format of your workspace. This means that the exact date format can vary, depending on your settings. | Supports a range of dates between 262,145 BCE and 262,143 CE. | `13/11/2024`, `11/13/2024` |
| DateTime | Date and time (including hours, minutes, seconds). Used to track exact moments of events, transactions, or logs. DateTime columns inherit the timezone and date and time format of your workspace. This means that the exact date and time format can vary, depending on your settings. | Follows RFC 3339 protocol. | `13/11/2024 00:00:00`, `11/13/2024 12:00 AM` |
| File | Allows you to upload or download files to/from your data tables. | Maximum file size: `500 MB`. File names can have up to `255` characters. | NA |
| Link to a table | Display data from a different data table in your workspace. Choose a **Linked data table** to select another data table to link to your current table and **Display data from** to determine which column from the data table you have selected displays as a dropdown. | Each data table can link to a maximum of `20` data tables. Data tables supports linking to **short text** and **long text** column types. | NA |
| Multi-value | This column supports storing multiple values in a single cell. Multi-value columns do not support nulls, empty strings, or duplicate values. Sorting columns is not supported. Supported value types include short **Text**, **Integer**, **Decimal**, **Date**, **DateTime**, and **Link to a table**. | Each data table can have a maximum of `20` multi-value columns. Each cell within a multi-value column can store up to `20` values. | NA |

## Data table connector quotas

| Description | Quota |
| --- | --- |
| Maximum batch size for all Data table connector batch triggers | 1,000 |
| Maximum batch size for all Data table connector batch actions, except **Delete records by condition**, which deletes up to 200 records per run | 1,000 |

> **FURTHER READING**
> 
> Refer to the [Platform quotas](/en/limits) documentation for more information about Workato quotas.

---
