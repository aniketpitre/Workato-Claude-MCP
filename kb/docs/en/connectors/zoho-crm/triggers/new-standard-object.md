---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/triggers/new-standard-object.md
description: >-
  The New standard object trigger checks for new standard objects in Zoho CRM
  once every polling interval.
---

# Zoho CRM - New standard object trigger

The **New standard object** trigger checks for new standard objects in Zoho CRM once every polling interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| Module name | Select the name of the module to monitor for new records. Options include: `Accounts`, `Contacts`, `Deals`, `Vendors`, `Leads`, `Campaigns`, `Products`, `Invoices`, `Price Books`, `Quotes`, `Sales Orders`, `Purchase Orders`, `Cases`, `Solutions`, and `Appointments`. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. You can't change this value after running or testing the recipe. |

## Output

Output fields are dynamically generated based on the selected module.
