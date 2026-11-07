---
url: 'https://docs.workato.com/en/connectors/bamboo-hr/update-table-record.md'
description: >-
  The Update table record of employee action updates a row in a selected
  BambooHR employee table.
---

# BambooHR – Update table record of employee action

The **Update table record of employee** action updates a row in an employee's table in BambooHR. You must specify the employee's internal ID, the table name, and the row ID.

You can use the [Get table records of employee](/en/connectors/bamboo-hr/get-table-records-of-employee-action) action to retrieve available row IDs from a specific table.

## Input

| Input field | Description |
| --- | --- |
| Employee ID | Enter the internal BambooHR ID of the employee. |
| Table | Choose the table that contains the record you plan to update. |
| Row ID | Enter the internal BambooHR ID of the row to update. |

Additional input fields may appear based on the selected **Table**.

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates the result of the table record update. |

---

---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/update-time-off-request-status-action.md
description: >-
  The Update time off request status action in the BambooHR connector lets you
  approve, deny, or cancel a specified time off request.
---

# BambooHR - Update time off request status action

This action updates the status of a specified time off request. Managers can approve or deny the request, whereas requester can cancel the request.

## Input

![Update time off request status action](/assets/update-time-off-request-action.Dmy6W2hi.png)_Update time off request status action_

| Input field | Description |
| --- | --- |
| Request ID _required_ | The ID of the time off request to be approved/canceled/denied. |
| Status _required_ | The new status of the time off request. Select from the picklist or input either approved, canceled or denied. |
| Note | Enter any notes you want to attach to the status updated. By default note will be made on behalf of the person performing the status update. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status indicating the outcome of the request. |

---

---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/get-employee-details-action.md
description: >-
  The Get employee details by ID action in the BambooHR connector lets you
  retrieve default and custom fields for an employee by employee ID.
---

# BambooHR - Get employee details by ID action

This action retrieves details about an employee identified by the employee ID.

## Input

![Get employee details by ID action](/assets/get-employee-details-action.CRaIxuGJ.png)_Get employee details by ID action_

| Input field | Description |
| --- | --- |
| Employee ID | The employee ID assigned by BambooHR. |
| Output field configuration | Select custom fields that will be generated as outputs to this action. If left blank, all custom fields will be returned. This is not recommended as it may cause job runtime to increase. |

## Output

The output of this action are all default employee fields and any custom fields selected. The commonly used employee fields are shown below.

| Output field. | Description |
| --- | --- |
| First name | The first name of the employee. |
| Last name | The last name of the employee. |
| Employee ID | The employee ID assigned by BambooHR. |
| Employee number | The employee number assigned by your company. |
| Job title | The current job title of this employee. |
| Department | The current department of this employee. |
| Supervisor ID | The employee ID of the current supervisor of this employee. |
| Supervisor E ID | The employee number of the current supervisor of this employee. |

Refer to the BambooHR [Field Names](https://documentation.bamboohr.com/docs/list-of-field-names) documentation for a full list of employee fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/list-employees-in-directory-action.md
description: >-
  The List employees in directory action in the BambooHR connector lets you
  retrieve all employees in your instance along with their details.
---

# BambooHR - List employees in directory action

This action lists all employees in your BambooHR instance.

## Input

There are no inputs for this action.

![List employees in directory action](/assets/list-employees-action.CgAVxyNc.png)_List employees in directory action_

## Output

![List employees in directory action - datatree](/assets/list-employees-datatree.-M3FROpu.png)_List employees in directory action - datatree_

The output of this action is a list of employees, including the **List size** and **List index**. Each employee will contain the following information.

| Output field. | Description |
| --- | --- |
| Employee ID | The employee ID assigned by BambooHR. |
| Display name | The display name of the employee. |
| First name | The first name of the employee. |
| Last name | The last name of the employee. |
| Preferred name | The preferred name of the employee. |
| Gender | The gender of the employee. |
| Job title | The current job title of this employee. |
| Work phone | The work phone number without extension. |
| Mobile phone | The mobile phone number of this employee. |
| Work Email | The work email of this employee. |
| Department | The current department of this employee. |
| Location | The location of the current office of this employee. |
| Division | The current division of this employee. |
| Linkedin | The LinkedIn URL for this employee. |
| Work phone extension | The work phone extension of this employee. |
| Phone uploaded | Whether an employee photo has been uploaded. |
| Photo URL | The URL to the employee photo. |
| Can upload photo | Whether a photo can be uploaded to this employee profile. |

---

---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/list-time-off-requests-action.md
description: >-
  The List time off requests action in the BambooHR connector lets you list time
  off requests between two dates, with filters to narrow the result.
---

# BambooHR - List time off requests action

This action lists all time off requests occurring between two specified dates. More filters can be specified to further narrow down the result.

## Input

![List time off requests action](/assets/list-time-off-requests-action._hgttR2f.png)_List time off requests action_

| Input field | Description |
| --- | --- |
| Start date _required_ | The start date of the time off. Select date or type it in YYYY-MM-DD format. |
| End date _required_ | The end date of the time off. Select date or type it in YYYY-MM-DD format. |
| Request ID | Specify a request ID to narrow the result to just this particular request. |
| Employee ID | Specify an employee ID to narrow the result to just requests from this particular employee. |
| Type | Select the type(s) of time off to narrow the result to, or input ID of each of them manually separated by comma. |
| Status | Select the status(es) of time off to narrow the result to, or input each of them manually separated by comma. |

## Output

The output of this action is a list of time off request objects, including the **List size** and **List index**. For more information on the structure of the time off request object, check out the [BambooHR documentation](https://documentation.bamboohr.com/reference/time-off-get-time-off-requests-1).

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/create-custom-report-action.md
description: >-
  The Create custom employee report action in the BambooHR connector lets you
  build a report on employees from selected fields to fetch large volumes of
  data.
---

# BambooHR - Create custom employee report action

This action creates a custom report on employees in BambooHR based on the selected fields.

Use this action if you are trying to fetch a large volume of employees data in one action.

## Input

![Create custom employee report action](/assets/create-custom-report-action.BDz8LS2K.png)_Create custom employee report action_

| Input field | Description |
| --- | --- |
| Fields | Select fields that will be returned as outputs to this action. |
| Only current | Limits the report to only current employees. Setting to no/false will include future-dated employees in the report. |
| Last changed | Include only the records that have been changed since given date. |

## Output

The output of this action is all the selected set of data for all the employees fetched by the report.

For more information, read the [BambooHR documentation](https://documentation.bamboohr.com/reference/request-custom-report-1).

---

---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/get-company-report-by-id-action.md
description: >-
  The Get company employee report by ID action in the BambooHR connector lets
  you fetch an existing employee report by its report ID.
---

# BambooHR - Get company employee report by ID action

This action fetches an existing employee report from the user's BambooHR instance.

> **DEPRECATION NOTICE**
> 
> This action is deprecated. Use the [Get report by ID (v2) action](/en/connectors/bamboo-hr/get-report-by-id-v2-action) to fetch reports using BambooHR's Custom Reports API instead.

## Input

![ Get company employee report by ID action](/assets/get-company-report-action.C07w9fie.png) \_ Get company employee report by ID action\_

| Input field | Description |
| --- | --- |
| Report ID | The ID of the existing report. You can get the report number by hovering over the report name and noting the ID from the URL. Supports only reports from my reports and manage reports. |
| Only current | Limits the report to only current employees. Setting to no/false will include future-dated employees in the report. |
| Output fields | Provide a sample JSON of the expected output fields from the report, or enter them manually. |

## Output

The output of this action is the set of data for all the employees as configured in the report.

For more information, read the [BambooHR documentation](https://documentation.bamboohr.com/reference/get-company-report-1).

---
