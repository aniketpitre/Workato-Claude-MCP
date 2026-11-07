---
url: 'https://docs.workato.com/en/connectors/ukg-pro-rest/new-record-trigger.md'
description: The New record trigger monitors UKG Pro for new records.
---

# UKG Pro - New record trigger

The **New record** trigger monitors UKG Pro for new records. This trigger requires the connected UKG Pro account to have the `View` Web Service role.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type to monitor. |
| Company | Provide the company ID to filter the records for a specific company. |

## Output

Output fields for the **New record** trigger are loaded dynamically based on your **Object** selection.

---

---
url: >-
  https://docs.workato.com/en/connectors/ukg-pro-rest/new-updated-employee-trigger.md
description: >-
  The New/updated employee trigger monitors UKG Pro for newly created or updated
  employees.
---

# UKG Pro - New/updated employee trigger

The **New/updated employee** trigger monitors UKG Pro for newly created or updated employees.

## Input

| Input field | Description |
| --- | --- |
| Poll interval | Select the interval at which to check for newly created or updated employees. |

## Output

| Output field | Description |
| --- | --- |
| First name | The employee’s given name. |
| Last name | The employee’s surname or family name. |
| Preferred name | The name the employee prefers to be addressed by. |
| Email address | The primary work email address of the employee. |
| Country code | The country associated with the employee. |
| Language code | The preferred language of the employee. |
| Employee number | A unique identifier assigned to the employee within the organization. |
| Employee ID | The system-generated unique identifier for the employee in UKG Pro. |
| Person ID | A unique identifier for a person. This ID is used when an individual may have multiple employee records. |
| User integration key | A key used for integration purposes to track the employee across systems. |
| Company name | The legal or business name of the company the employee belongs to. |
| Company ID | A unique identifier assigned to the company in UKG Pro. |
| Supervisor ID | The unique identifier of the employee's direct supervisor. |
| Salary or hourly | Specifies whether the employee is salaried or paid hourly. |
| Full time or part time | Indicates whether the employee is a full-time or part-time worker. |
| Is active | Specifies whether the employee is currently active in the system. |
| Work location | The primary location where the employee works. |
| Job code | A unique code representing the employee’s job role. |
| Project code | The project associated with the employee, if applicable. |
| Org level 1 code | A code representing the first organizational level, such as a division or department. |
| Org level 2 code | A code representing the second organizational level, such as a sub-department. |
| Org level 3 code | A code representing the third organizational level. |
| Org level 4 code | A code representing the fourth organizational level. |
| Middle name | The employee’s middle name, if applicable. |
| Work phone | The employee’s work contact number. |
| Home phone | The employee’s personal contact number. |
| Employee address 1 | The primary address line for the employee. |
| Employee address 2 | Additional address details, such as the employee's apartment or suite number. |
| City | The city where the employee resides. |
| State | The state or province of the employee’s residence. |
| Zip code | The postal or ZIP code of the employee’s address. |
| Termination date | The date the employee was terminated, if applicable. |
| Hire date | The date the employee was hired by the company. |
| Supervisor name | The full name of the employee’s direct supervisor. |
| Prefix | An optional title such as Mr., Ms., or Dr. |
| Suffix | A suffix if applicable. |
| Alternate email address | An additional email address for the employee, if available. |
| Gender | The gender identity of the employee. |
| Employee status | The employee's current employment status. |
| Employee type | The type of employment. |
| Employee status start date | The date when the employee’s current status became effective. |
| Date in job | The date the employee started their current job position. |
| Date of last hire | The most recent date the employee was rehired. |
| Job group code | A code representing the job classification or category. |
| Alternate job title | An alternate title for the employee’s job role, if applicable. |

---

---
url: >-
  https://docs.workato.com/en/connectors/ukg-pro-rest/new-updated-record-trigger.md
description: >-
  The New/updated record trigger monitors UKG Pro for newly created or updated
  records.
---

# UKG Pro - New/updated record trigger

The **New/updated record** trigger monitors UKG Pro for newly created or updated records. This trigger requires the connected UKG Pro account to have the `View` Web Service role.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type to monitor. |

## Output

Output fields for the **New/updated record** trigger are loaded dynamically based on your **Object** selection.

---

---
url: >-
  https://docs.workato.com/en/connectors/ukg-pro-rest/terminated-employee-trigger.md
description: The Terminated employee trigger monitors UKG Pro for employee terminations.
---

# UKG Pro - Terminated employee trigger

The **Terminated employee** trigger monitors UKG Pro for employee terminations. This trigger requires the connected UKG Pro account to have the `View` Web Service role.

## Input

| Input field | Description |
| --- | --- |
| Company | Select the company to monitor. |

## Output

| Output field | Description |
| --- | --- |
| Company ID | A unique identifier assigned to the company within UKG Pro. |
| Company code | A short code representing the company. |
| Company name | The official name of the company. |
| Employee ID | The system-generated unique identifier for the employee. |
| Job description | A brief description of the employee’s job role. |
| Pay group description | The pay group to which the employee belongs. |
| Primary job code | The unique job classification code for the employee’s primary job role. |
| Org level 1 code | A code representing the first organizational level. |
| Org level 2 code | A code representing the second organizational level. |
| Org level 3 code | A code representing the third organizational level. |
| Org level 4 code | A code representing the fourth organizational level. |
| Original hire date | The date the employee was first hired by the company. |
| Last hire date | The most recent date the employee was rehired. |
| Full time or part time code | A code indicating whether the employee is full-time or part-time. |
| Primary work location code | The code representing the employee’s primary work location. |
| Language code | The employee’s preferred language. |
| Primary project code | The primary project the employee is assigned to. |
| Work phone number | The employee’s work contact number. |
| Work phone extension | The extension number for the employee’s work phone. |
| Work phone country | The country associated with the employee’s work phone. |
| Date in job | The date the employee started their current job position. |
| Date last worked | The last recorded date the employee worked. |
| Date of benefit seniority | The date used for determining benefit eligibility. |
| Date of seniority | The date used to calculate the employee’s seniority. |
| Deduction group code | A code representing the employee’s deduction group. |
| Earning group code | A code representing the employee’s earning group. |
| Employee type code | A classification code for the employee type. |
| Employee status code | A code representing the employee’s current status. |
| Employee number | The employee’s unique payroll number. |
| Job change reason code | A code indicating the reason for the employee's job change. |
| Job title | The official title of the employee’s job. |
| Leave reason code | A code specifying the reason for the employee's leave. |
| Supervisor ID | The unique identifier of the employee’s direct supervisor. |
| Supervisor first name | The first name of the employee’s supervisor. |
| Supervisor last name | The last name of the employee’s supervisor. |
| Auto allocate | Indicates whether resources or costs are automatically allocated. |
| Clock code | A code associated with the employee’s time-tracking system. |
| Date last pay date paid | The last date on which the employee was paid. |
| Date of early retirement | The employee’s early retirement date, if applicable. |
| Date of local union | The date the employee joined the local union, if applicable. |
| Date of national union | The date the employee joined the national union, if applicable. |
| Date of retirement | The official retirement date of the employee. |
| Date of suspension | The date the employee was suspended, if applicable. |
| Date of termination | The date the employee was terminated, if applicable. |
| Date paid thru | The date through which the employee has been paid. |
| Status start date | The date the employee’s current status became effective. |
| Hire source | The source from which the employee was hired. |
| Is auto allocated | Indicates whether allocations are automatic. |
| Is autopaid | Indicates whether the employee is automatically paid. |
| Is multiple job | Indicates whether the employee holds multiple jobs. |
| Job group code | A code representing the job classification or category. |
| Mailstop | The internal mailing location for the employee, if applicable. |
| Ok to rehire | Indicates whether the employee is eligible for rehire. |
| Pay group | The employee’s pay group. |
| Pay period | The frequency of payroll processing. |
| Planned leave reason | The anticipated reason for an upcoming leave. |
| Position code | A unique identifier for the employee’s job position. |
| Salary or hourly | Specifies whether the employee is salaried or hourly. |
| Scheduled annual hrs | The number of hours the employee is scheduled to work annually. |
| Scheduled FTE | The full-time equivalent (FTE) for the employee’s position. |
| Scheduled work hrs | The number of work hours scheduled per week. |
| Shift | The assigned shift code for the employee. |
| Shift group | A grouping of shifts for scheduling purposes. |
| Term reason | The reason for the employee’s termination. |
| Termination reason description | A detailed description of the reason for termination. |
| Term type | Specifies the type of termination. |
| Timeclock ID | The identifier used for the employee’s time-tracking system. |
| Union local | The local union the employee is associated with. |
| Union national | The national union the employee is associated with. |
| Weekly hours | The number of hours the employee is scheduled to work per week. |
| Date time created | The timestamp when the employee record was created. |
| Date time changed | The timestamp when the employee record was last updated. |
| Supervisor employee number | The employee number of the supervisor. |
| Supervisor COID | The company ID associated with the supervisor. |
| Supervisor company code | The company code associated with the supervisor. |
| Company GL segment | The general ledger segment for the company. |
| Location GL segment | The general ledger segment for the employee’s work location. |

---
