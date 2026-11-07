---
url: 'https://docs.workato.com/en/connectors/rpa-by-workato/get-process-details.md'
description: >-
  The Get process details action retrieves information from a process you
  specify.
---

# RPA by Workato - Get process details action

The **Get process details** action retrieves information from a process you specify.

## Input

| Input fields | Description |
| --- | --- |
| Process ID | Provide the ID of the process you plan to retrieve. |

## Output

| Output fields | Description |
| --- | --- |
| Process info ID | The ID of the retrieved process. |
| Department ID | The ID of the department associated with the retrieved process. |
| Name | The name of the retrieved process. |
| Description | The description of the retrieved process. |
| Version | The version of the retrieved process. |
| Start arguments | Contains information about the starting arguments for the retrieved process, such as its Name, Type, and Value. |
| Department name | The name of the department associated with the retrieved process. |
| Process ID | The ID of the retrieved process. |

---

---
url: >-
  https://docs.workato.com/en/connectors/rpa-by-workato/list-departments-batch.md
description: >-
  The List departments batch action retrieves a list of all departments in your
  RPA instance.
---

# RPA by Workato - List departments action (batch)

The **List departments** batch action retrieves a list of all departments in your RPA instance.

## Input

This action does not require any input.

## Output

| Output fields | Description |
| --- | --- |
| Department ID | The ID of the retrieved department. |
| Department name | The name of the retrieved department. |
| List size | The total number of departments retrieved. |
| List index | The position of the department within the list. |

---

---
url: >-
  https://docs.workato.com/en/connectors/rpa-by-workato/list-processes-by-department-batch.md
description: >-
  The List processes by department batch action retrieves all processes from a
  department and stage you specify.
---

# RPA by Workato - List processes by department action (batch)

The **List processes by department** batch action retrieves all processes from a department and stage you specify.

## Input

| Input fields | Description |
| --- | --- |
| Department | Select the department associated with the process you plan to retrieve. Alternatively, you can switch to **Use department ID** and input a Department ID datapill. |
| Stage | Select the stage of the process you plan to retrieve. Alternatively, you can switch to **Use stage ID** and enter `0` for `DEV`, `1` for `TEST`, or `2` for `PROD`. |

## Output

| Output fields | Description |
| --- | --- |
| Process info ID | The ID of the retrieved process. |
| Department ID | The ID of the department associated with the retrieved process. |
| Name | The name of the retrieved process. |
| Description | The description of the retrieved process. |
| Version | The version of the retrieved process. |
| Start arguments | Contains information about the starting arguments for the retrieved process, such as its Name, Type, and Value. |
| Department name | The name of the department associated with the retrieved process. |
| Process ID | The ID of the retrieved process. |
| List size | The total number of processes retrieved. |
| List index | The position of the process within the list. |

---
