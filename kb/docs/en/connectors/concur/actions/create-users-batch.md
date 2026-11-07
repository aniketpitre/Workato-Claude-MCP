---
url: 'https://docs.workato.com/en/connectors/concur/actions/create-users-batch.md'
description: >-
  The Create users batch action creates multiple user profiles with identity,
  spend, and travel attributes.
---

# SAP Concur - Create users action (batch)

The **Create users** batch action creates multiple user profiles with identity, spend, and travel attributes.

## Input

| Input field | Description |
| --- | --- |
| Users | Provide details of the users to create. |
| Users source list (Users) | Provide a list datapill containing multiple user records. |
| Name | Configure the user's name. |
| Family name (Name) | Enter the family name or last name of the user. |
| Given name (Name) | Enter the given name or first name of the user. |
| Active (Users) | Select whether the user is active. |
| User name (Users) | Enter the username for the user. Username should end with `@` followed by the company domain. |
| Company ID (Enterprise user) | Enter the Concur ID of the company. Required for users that belong to or act on behalf of a business enterprise. |
| Start date (Enterprise user) | Enter the start date for the user's employment or relationship with the enterprise. |

> **ADDITIONAL INPUT FIELDS**
> 
> This action supports additional input fields for user attributes including emails, phone numbers, addresses, travel preferences, and spend settings. Refer to the [SAP Concur User Provisioning v4 API documentation](https://developer.concur.com/api-reference/user-provisioning/v4.user-provisioning.html) for the complete list of available fields.

## Output

| Output field | Description |
| --- | --- |
| Provision ID | The provisioning request ID. This is a unique number used for querying status on the request. |
| Schemas | SCIM schema identifiers for the response. |
| Meta | Metadata information about the provisioning request. |
| Location (Meta) | The URL for retrieving detailed provisioning status. |
| Created (Meta) | The timestamp when the provisioning request was created. |
| Last modified (Meta) | The timestamp of the last modification to the provisioning request. |
| Provision type (Meta) | The type of provision request. |
| Resource type (Meta) | The type of resource. |
| Correlation ID (Meta) | A unique identifier value attached to requests and messages for tracking purposes. |
| Completed (Meta) | The timestamp when the provisioning request completed. |
| Operations count | Counts across provisioning operations within the request. |
| Total (Operations count) | The total number of operations requests within the provisioning request. |
| Success (Operations count) | The number of operations that were successful. |
| Failed (Operations count) | The number of operations that failed. |
| Pending (Operations count) | The number of operations that are still processing. |
| Status | The overall completion and success status of the provisioning request. |
| Completed (Status) | Indicates whether the provisioning request has completed processing. |
| Success (Status) | Indicates whether the user provisioning was successful. |

---
