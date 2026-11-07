---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/get-flow-task-instance-status.md
description: >-
  The Get flow task instance status action retrieves the current execution
  status of a specific task within a flow instance in Oracle Fusion Cloud's
  Human Capital Management (HCM) system.
---

# Oracle Fusion Cloud - Get flow task instance status action

The **Get flow task instance status** action retrieves the execution status of a specific task within a flow instance in Oracle Fusion Cloud's Human Capital Management (HCM) system.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Flow instance name | Enter the name of the flow instance that contains the task. |
| Flow task instance name | Specify the name of the specific task instance within the flow. |
| Legislative data group name | Enter the legislative data group name to scope the status check. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the current status of the flow task instance, such as running, completed, failed, or another execution state. |
