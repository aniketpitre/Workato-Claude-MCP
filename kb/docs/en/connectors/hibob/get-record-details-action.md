---
url: 'https://docs.workato.com/en/connectors/hibob/get-record-details-action.md'
description: >-
  The **Get record details** action allows you to retrieve the details of any
  standard or custom record, such as, employee.
---

# HiBob - Get record details action

The **Get record details** action allows you to retrieve the details of a standard or custom record, such as an employee record.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object to be retrieved from the drop-down menu. |

More input fields are dynamically loaded based on the object you select. The following example shows the input schema for the **Timeoff** object:

| Input fields | Description |
| --- | --- |
| Employee ID | Provide the ID of the employee whose timeoff data is to be retrieved. |
| Request ID | Provide the request ID for which details are to be retrieved. |

## Output

Output fields are dynamically loaded based on the selected object. The following example shows the output schema for the **Timeoff** object:

| Output field | Description |
| --- | --- |
| Request ID | Unique identifier of the time off request. |
| Employee ID | Unique identifier of the employee associated with the time off request. |
| Policy type display name | Name of the leave policy under which the time off is requested. |
| Type | Unit type used for time off measurement. |
| Start date | The first date of the requested time off. |
| Start portion | Portion of the day when the time off begins. |
| End date | The last date of the requested time off. |
| End portion | Portion of the day when the time off ends. |
| Date | Specific date associated with the daily breakdown of the request. |
| Hours on date | Number of hours taken off on the specified date. |
| Approved | Indicates whether the time off request has been approved. |

---
