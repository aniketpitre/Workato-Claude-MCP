---
url: 'https://docs.workato.com/en/connectors/workday-rest/search-worker-action.md'
description: >-
  The Search workers action in the Workday REST connector lets you search for
  workers by name and return their full worker records.
---

# Workday REST - Search workers action

Use this action to search for workers by name.

![Search workers by name action](/assets/search-worker.Ch2LnkTV.png)_Search workers action_

## Input

| Input field | Description |
| --- | --- |
| Name filter | This must be at least 3 characters long and is not case sensitive. Workers with names that start with the provided value will be returned. |

## Output

Output is a list of workers. Each worker object has an output defined in the following table.

| Output field | Description |
| --- | --- |
| Descriptor | Worker full name |
| ID | Workday ID or the worker record. |
| HREF | API resource URL of the worker record. |
| Primary supervisory organization | Primary supervisory organization object of this worker record. Contains descriptor (full name), Workday ID and HREF. |
| Business title | Full business title of the worker record. |
| Primary work email | Primary work email of the worker record. |
| Is manager | Boolean data. `True` if the worker record is a manager. |
| Primary work phone | Primary phone number of the worker record. |
| Location | Location object of this worker record. Contains descriptor (full name) and Workday ID. |
| Primary work address text | Full primary address of the worker record. |
| Supervisory organizations managed | Supervisory organizations managed by the worker record. |
| Years of service | Years of service, as an integer, by the worker. |
| Date of birth | Date of birth of the worker record. Format: YYYY-MM-DD |

---

---
url: >-
  https://docs.workato.com/en/connectors/workday-rest/create-job-change-action.md
description: >-
  The Create a job change action in the Workday REST connector lets you initiate
  a job change for a specified worker, such as moving them to a new
  organization.
---

# Workday REST - Create a job change action

Use this action to initiate a job change for a specified worker. Refer to [Workday REST API documentation](https://doc.workday.com/reader/wsiU0cnNjCc_k7shLNxLEA/3Zi_EjiDLCyNVUNtcI9~Nw#dan1370797990026__POST) for more details.

![Create a job change action](/assets/create-job-change.bWtoSYbC.png)_Create a job change action_

## Input

| Input field | Description |
| --- | --- |
| Worker ID | Workday ID of the worker record to initiate the job change for. |
| Job change reason | Reason for the job change. Select from the list or provide the Job change reason ID. |
| Supervisory organization | The worker will be in this organization after the job change. Select from the list or provide the organization ID. |
| Effective date | **Optional**. Effective date of the job change. If left blank, is set to current date. |
| Move manager team? | **Optional**. Choose to transfer the manager team to the new organization. |
| Proposed organizations | **Optional**. Set of proposed organizations to which the worker is to be assigned. |

## Output

| Output field | Description |
| --- | --- |
| Descriptor | Indicates _Approval by Manager_ task. |
| ID | Workday ID of the inbox task. |
| HREF | API resource URL of the inbox task. |
| Job change reason | Job change reason object. Contains descriptor, Workday ID and HREF. |
| Move manager team? | Boolean value indicating if the manager team was transferred to the new organization. |
| Proposed organizations | List of proposed organizations to which the worker is to be assigned. |
| Supervisory organization | The worker will be in this organization after the job change is complete. |

---
