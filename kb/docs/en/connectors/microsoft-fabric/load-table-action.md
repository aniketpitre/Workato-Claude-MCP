---
url: 'https://docs.workato.com/en/connectors/microsoft-fabric/load-table-action.md'
description: The Load table action enables you to load data to a table in Microsoft Fabric.
---

# Microsoft Fabric - Load table action

The **Load table** action enables you to load data to a table in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Select or enter the ID of the workspace where the item is located. |
| Lakehouse ID | Select or enter the ID of the lakehouse to delete. |
| Table name | Enter the name of the table. |
| Path type | Select the path type from file or folder. |
| Relative path | Enter the relative path of the data file or folder. |
| File extension | Enter the file extension of the file. |
| Format options | Specify the format of the file. |
| Mode | Select the operation mode from overwrite or append. |
| Recursive | Specify whether to search files recursively or not. |

## Output

| Output field | Description |
| --- | --- |
| Location | Location of the table. |
| Microsoft operation ID | ID of the Microsoft operation. |
| Retry after | Time in seconds to retry after. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-fabric/query-activity-run-action.md
description: >-
  The Query activity run action enables you to query the activities inside a job
  of an item in Microsoft Fabric.
---

# Microsoft Fabric - Query activity run action

The **Query activity run** action enables you to query the activities inside a job of an item in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Enter the ID of the workspace where the item is located. |
| Job ID | Enter the ID of the Job to query the activities of. |
| Last updated after | Enter the date & time of the activity from which to run the query. |
| Last updated before | Enter the date & time of the activity up to where to run the query. |
| Continuation token | Enter the token to make the next request. Useful for pagination. |
| Filters | Enter the list of operands, operators and values to add filters to the query. |
| Order by | Enter the list of orders and order by attributes to apply sorting on the query records. |

## Output

| Output field | Description |
| --- | --- |
| Continuation token | Token used for pagination. |
| values | Array of returned items. |
| Activity name | Name of the activity. |
| Activity run end | Date and time when the activity run ended. |
| Activity run ID | ID of the activity run. |
| Activity run start | Date and time when the activity run started. |
| Activity type | Type of the activity. |
| Duration in ms | Duration in milliseconds for which the activity ran. |
| Error | Error occurred during the activity, if any. |
| Linked service name | Name of any linked service. |
| Input | Key-value pairs of input data to the activity. |
| Output | Key-value pairs of output data from the activity. |
| Pipeline name | Name of the pipeline. |
| Pipeline run ID | ID of the pipeline run. |
| Status | Status of the activity. |
| User properties | User properties, if any. |
| Iteration hash | Hash of the iteration. |
| Retry attempt | Number of retry attempts, if any. |
| Recovery status | Recovery status of the pipeline. |
| Execution details | Details of the execution of the activity. |
| Integration runtime names | Names of the integration runtimes, if any. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-fabric/run-on-demand-item-job-action.md
description: >-
  The Run on-demand item job action enables you to run any item job in Microsoft
  Fabric.
---

# Microsoft Fabric - Run on-demand item job action

The **Run on-demand item job** action enables you to run any item job in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Select or enter the ID of the workspace where the item is located. |
| Item ID | Enter the ID of the Item to run the job on. |
| Job type | Enter the type of job. |
| Execution data | Enter the execution data if required. |

## Output

| Output field | Description |
| --- | --- |
| Location | Link to the location of the item job in Microsoft Fabric. |
| Retry after | Time in seconds to retry the job after. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-fabric/run-on-demand-table-maintenance-action.md
description: >-
  The Run on-demand table maintenance action enables you to run on-demand table
  maintenance in Microsoft Fabric.
---

# Microsoft Fabric - Run on-demand table maintenance action

The **Run on-demand table maintenance** action enables you to run on-demand table maintenance in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Select or enter the ID of the workspace where the item is located. |
| Lakehouse ID | Select or enter the ID of the lakehouse to run table maintenance on. |
| Job type | Enter the type of job for table maintenance. |
| Execution data | Enter the execution data, including Optimize settings, Schema name, Table name, Vacuum settings, and more. |

## Output

| Output field | Description |
| --- | --- |
| Location | Link to the location of the item job in Microsoft Fabric. |
| Retry after | Time in seconds to retry the job after. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-fabric/update-record-action.md
description: >-
  The Update record action enables you to update the specified record in
  Microsoft Fabric.
---

# Microsoft Fabric - Update record action

The **Update record** action enables you to update the specified record in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to update its record. Fields load dynamically based on the selected object. |

For example, if the selected object is **Lakehouse**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Workspace ID | Select or enter the ID of the workspace where the item is located. |
| Lakehouse ID | Select or enter the ID of the lakehouse to update. |
| Display name | Enter the name of the lakehouse. |
| Description | Enter the description for the lakehouse. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. To take an example of the **Lakehouse** object, the following are the output fields.

| Output field | Description |
| --- | --- |
| Description | Description of the lakehouse. |
| Display name | Name of the lakehouse. |
| Folder ID | ID of the folder where the lakehouse is created. |
| ID | ID of the lakehouse. |
| Properties | Properties of the lakehouse include the following data. Type, Default schema, One lake files path, One lake tables path, SQL endpoint properties, Connection string, ID, Provisioning status. |
| Item tag | The list of tags attached to the lakehouse is any. |
| Type | Type of the item. Lakehouse in this case. |
| Workspace ID | ID of the workspace where the Lakehouse was created. |
| Status | Status of provisioning of the lakehouse. |

---
