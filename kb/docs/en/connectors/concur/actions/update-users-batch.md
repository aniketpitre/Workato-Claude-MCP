---
url: 'https://docs.workato.com/en/connectors/concur/actions/update-users-batch.md'
description: >-
  The Update users batch action updates multiple user profiles with identity,
  spend, and travel attributes.
---

# SAP Concur - Update users action (batch)

The **Update users** batch action updates multiple user profiles with identity, spend, and travel attributes.

## Input

| Input field | Description |
| --- | --- |
| Replace user? | Select **Yes** to replace the complete details of the user. Select **No** to update the data attributes listed within the request. Default is false. |
| Users | Provide details of the users to update. |
| Users source list (Users) | Provide a list datapill containing multiple user records. |
| User ID (Users) | Enter the unique identifier of the SAP Concur user to update. |

> **ADDITIONAL INPUT FIELDS**
> 
> This action supports additional input fields for user attributes including emails, phone numbers, addresses, travel preferences, and spend settings. Refer to the [SAP Concur User Provisioning v4 API documentation](https://developer.concur.com/api-reference/user-provisioning/v4.user-provisioning.html) for the complete list of available fields.

## Output

| Output field | Description |
| --- | --- |
| Meta | Metadata information about the provisioning request. |
| Location (Meta) | The URL for retrieving detailed provisioning status. |
| Created (Meta) | The timestamp when the provisioning request was created. |
| Last modified (Meta) | The timestamp of the last modification to the provisioning request. |
| Provision type (Meta) | The type of provision request. |
| Resource type (Meta) | The type of resource. |
| Correlation ID (Meta) | A unique identifier value attached to requests and messages for tracking purposes. |
| Completed (Meta) | The timestamp when the provisioning request completed. |
| Schemas | SCIM schema identifiers for the response. |
| Provision ID | The provisioning request ID. This is a unique number used for querying status on the request. |
| Operations count | Counts across provisioning operations within the request. |
| Total (Operations count) | The total number of operations requests within the provisioning request. |
| Success (Operations count) | The number of operations that were successful. |
| Failed (Operations count) | The number of operations that failed. |
| Pending (Operations count) | The number of operations that are still processing. |
| Status | The overall completion and success status of the provisioning request. |
| Completed (Status) | Indicates whether the provisioning request has completed processing. |
| Success (Status) | Indicates whether the user provisioning was successful. |

---
