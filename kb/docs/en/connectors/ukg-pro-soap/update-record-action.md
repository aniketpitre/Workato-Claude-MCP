---
url: 'https://docs.workato.com/en/connectors/ukg-pro-soap/update-record-action.md'
description: The Update record action updates an existing record in your UKG Pro instance.
---

# UKG Pro (SOAP) - Update record action

The **Update record** action updates an existing record in your UKG Pro instance.

## Input

Input fields load dynamically based on the selected object. For example, the **Employee** object has the following input fields:

| Input field | Description |
| --- | --- |
| Object | Select the UKG Pro object to update. Options include `Employee`, `Employee job`, `Employee compensation`, `Employee employment information`, `Employee person`, `Employee address`, `Employee contact`, `Employee phone information`, and `Employee user defined fields`. |
| Employee identifier | Unique identifiers for the employee, including **Company code** and **Employee number**. |
| Effective date | Enter the effective date for the update. |

## Output

Output fields load dynamically based on the selected object.

| Output field | Description |
| --- | --- |
| Success | A boolean indicating if the update record action was successful. |

---
