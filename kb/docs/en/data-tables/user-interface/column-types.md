---
url: 'https://docs.workato.com/en/data-tables/user-interface/column-types.md'
description: >-
  Reference for the column data types supported in Workato data tables, with
  available operands for each type.
---

# Column types

Data tables support columns of the following data types:

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

## Available operands

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

---
