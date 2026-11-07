---
url: 'https://docs.workato.com/en/connectors/bamboo-hr/delete-table-record.md'
description: >-
  The Delete table record action removes a row from a selected BambooHR employee
  table.
---

# BambooHR – Delete table record action

The **Delete table record** action removes a row from an employee's table in BambooHR. You must specify the employee's internal ID, the table name, and the row ID.

You can use the [Get table records of employee](/en/connectors/bamboo-hr/get-table-records-of-employee-action) action to retrieve available row IDs from a specific table.

## Input

| Input field | Description |
| --- | --- |
| Employee ID | Enter the internal BambooHR ID of the employee. |
| Table | Choose the table that contains the record you plan to delete. |
| Row ID | Enter the internal BambooHR ID of the row to delete. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates the result of the table record deletion. |

---
