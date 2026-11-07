---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/get-table-records-of-employee-action.md
description: >-
  The Get table records of employee action in the BambooHR connector lets you
  retrieve table data for an employee identified by the employee ID.
---

# BambooHR - Get table records of employee action

This action retrieves table data of an employee identified by the employee ID.

## Input

![Get table records of employee action](/assets/get-table-records-of-employee-action.H6m6hYjx.png)_Get table records of employee action_

| Input field | Description |
| --- | --- |
| Employee ID | The employee ID assigned by BambooHR. |
| Table | Select the table to retrieve. Each table will return a different datatree. |

## Output

The output of this action is a list of table records according to which table was select, including the **List size** and **List index**. Find out more about [BambooHR tables](https://www.bamboohr.com/api/documentation/tables.php).

> **Iterate through list items**
> 
> Remember to use a [Repeat step](/en/recipes/steps#repeat-step) to iterate through the table records.
