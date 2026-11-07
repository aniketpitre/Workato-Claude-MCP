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
