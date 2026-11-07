---
url: 'https://docs.workato.com/en/connectors/xero/new-employee.md'
description: >-
  The New/updated employee trigger in the Xero connector fires when an employee
  record is created or updated.
---

# Xero - New/updated employee trigger

The **New/updated employee** trigger activates when an employee record is created or updated.

![New/updated employee trigger](/assets/new-employee-trigger.Cs_jcFws.png)_Xero - New/updated employee trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Choose how often Workato checks for new or updated events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Determine the starting point for the trigger to fetch events. You cannot change this value after the recipe has been run or tested. |

## Output

| Output field | Description |
| --- | --- |
| Employee ID | The unique identifier assigned to the employee. |
| First name | The first name of the employee. |
| Last name | The last name of the employee. |
| Gender | The gender of the employee. |
| Date of birth | The date of birth of the employee. |
| Phone | The employee's phone number. |
| Email | The employee's email address. |
| Updated date | The date when the employee's information was last updated. |

---
