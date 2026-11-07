---
url: 'https://docs.workato.com/en/connectors/ukg-pro-soap/delete-record-action.md'
description: The Delete record action deletes a record from your UKG Pro instance.
---

# UKG Pro (SOAP) - Delete record action

The **Delete record** action deletes a record from your UKG Pro instance.

## Input

Input fields load dynamically based on the selected object. For example, the **Employee** object has the following input fields:

| Input field | Description |
| --- | --- |
| Object | Select the UKG Pro object to delete. Options include `Employee`. |
| Employee identifier | Enter the unique identifiers for the employee, including **Company code** and **Employee number**. |
| Termination date | Provide the termination date in DateTime format. For example, `2021-12-31T00:00:00`. |
| Termination reason | Select a termination reason. |
| Home company identifier | Enter the company code for the home company. |
| Paid through date | Enter a date that the employee was paid through. |

## Output

| Output field | Description |
| --- | --- |
| Success | A boolean indicating if the delete record action was successful. |

---
