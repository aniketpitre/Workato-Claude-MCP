---
url: 'https://docs.workato.com/en/connectors/ukg-pro-soap/get-record-action.md'
description: The Get record action retrieves a record from your UKG Pro instance.
---

# UKG Pro (SOAP) - Get record action

The **Get record** action retrieves a record from your UKG Pro instance.

## Input

Input fields load dynamically based on the selected object. For example, the **Employee** object has the following input fields:

| Input field | Description |
| --- | --- |
| Object | Select the UKG Pro object to retrieve. Options include Employee compensation, Employee employment information, Employee person, Employee address, Employee contact, Employee contact by ID, Employee phone information, Employee last pay statement, Pay statement by range, Employee user defined fields, and Terminated employee. |
| Company code | Enter the home company code. |
| Employee number | Enter the employee number. |

## Output

Output fields load dynamically based on the selected object. For example, the action has the following common output fields:

| Output field | Description |
| --- | --- |
| Effective date | The effective date for the returned record. |
| Company code | The company code for the returned record. |
| Employee number | The employee number for the returned record. |
| Pay frequency | The pay frequency for the returned record. |
| Pay group | The pay group for the returned record. |
| Key | The key for the returned record. |
| Value | The value for the returned record. |
| Errors | The errors for the returned record. |
| Code | The code for the returned record. |
| Message | The message for the returned record. |

---
