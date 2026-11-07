---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/get-user-provisioning-status-details.md
description: >-
  The Get user provisioning status details action retrieves a detailed status
  report for a provisioning request.
---

# SAP Concur - Get user provisioning status details action

The **Get user provisioning status details** action retrieves a detailed status report for a provisioning request. The provisioning status is stored for seven days from the provisioning request date.

## Input

| Input field | Description |
| --- | --- |
| Provision ID | Enter the unique identifier of the provisioning request. |
| Start index | Specify the 1-based index of the first query result. |
| Count | Specify the desired number of operations per page. |
| State | Select the state to filter results. Options include: Pending, Success, Failed |

## Output

| Output field | Description |
| --- | --- |
| Schemas | SCIM schema identifiers for the response. |
| ID | The provisioning request ID. This is a unique number used for querying status. |
| Meta | Metadata information about the provisioning request. |
| Location (Meta) | The location URL to receive status on the provisioning request. |
| Created (Meta) | The timestamp when the provisioning request was created. |
| Last modified (Meta) | The timestamp of the last modification to the provisioning request. |
| Resource type (Meta) | The type of resource. |
| Correlation ID (Meta) | A unique identifier value attached to requests and messages for tracking purposes. |
| Status | The overall completion and success status of the provisioning request. |
| Completed (Status) | Indicates whether the provisioning request has completed processing. |
| Success (Status) | Indicates whether the user provisioning was successful. |
| Operations count | Counts across provisioning operations within the request. |
| Total (Operations count) | The total number of operations requests within the provisioning request. |
| Success (Operations count) | The number of operations that were successful. |
| Failed (Operations count) | The number of operations that failed. |
| Pending (Operations count) | The number of operations that are still processing. |
| Operations | List of individual provisioning operations within the request. |
| ID (Operations) | The unique identifier of the operation. |
| Status (Operations) | The status of the operation. |
| Resource (Operations) | The resource associated with the operation. |
| Extensions (Operations) | Additional extension data for the operation. |
| Total results | The total number of results available. |
| Start index | The 1-based index of the first result in the current set of list results. |
| Items per page | The number of operations returned per page. |
