---
url: 'https://docs.workato.com/en/connectors/marketo/add-custom-activity-action.md'
description: >-
  The Add custom activity action in the Marketo connector lets you add custom
  activities to lead records in batches of up to 300 records at once.
---

# Marketo - Add custom activity action (batch)

This action allows you to add custom activities to lead records in Marketo, processing up to 300 activity records at once. The **Attributes** array must include non-primary attributes.

## Input

| Field | Description |
| --- | --- |
| Input | Expand to configure the list of custom activities to add. |
| Input source list (input) | Input a list datapill from which the custom activities are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Lead ID (input) | Enter the lead's unique integer ID associated with the activity. |
| Activity date (input) | Specify the activity's datetime. |
| Activity type ID (input) | Provide the unique ID of the activity type or select it from the drop-down menu. |
| Primary attribute value (input) | Enter the primary attribute's value for the custom activity. |
| Attributes (input) | Expand to specify secondary attributes for the custom activity. |
| Attributes source list (attributes) | Input a list datapill from which secondary attributes are retrieved. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Name (attributes) | Enter the attribute name. |
| Value (attributes) | Provide the attribute value. |
| API name (attributes) | Specify the attribute's API name. |
| Errors (input) | Expand to configure fields for custom activity errors. |
| Errors source list (errors) | Input a list datapill from which errors are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Code (errors) | Enter the error code. Refer to [Marketo error codes](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/error-codes) for more information. |
| Message (errors) | Provide a message explaining the error. |
| ID (input) | Enter the integer identifier of the custom activity. |
| Marketo GUID (input) | Specify the unique identifier (GUID) of the activity. |
| API name (input) | Enter the API name of the activity. |
| Status (input) | Specify the operation's status on the record. Accepted values include `created`, `updated`, `deleted`, `skipped`, `added`, and `removed`. |

## Output

| Field | Description |
| --- | --- |
| Success | Indicates whether the request succeeded. |
| Request ID | A unique identifier for the request. |
| Errors | An array of errors encountered during the request, if any. |
| Code (errors) | The error code for any encountered error. Refer to [Marketo error codes](https://experienceleague.adobe.com/en/docs/marketo-developer/marketo/rest/error-codes) for more information. |
| Message (errors) | A detailed message explaining the error. |
| Warnings | An array of warnings encountered, if any. |
| More result | Indicates if there are additional results beyond the current batch. |
| Next page token | A token for retrieving the next page of results, if applicable. |
| Result | An array containing the individual results of the operation. |
| Lead ID (result) | The unique ID of the lead associated with the custom activity. |
| Activity date (result) | The datetime for the activity. |
| Activity type ID (result) | The unique ID of the custom activity type. |
| Primary attribute value (result) | The value of the primary attribute for the custom activity. |
| Attributes (result) | A list of secondary attributes related to the custom activity. |
| Name (attributes) | The name of the attribute. |
| Value (attributes) | The value of the attribute. |
| API name (attributes) | The API name of the attribute. |
| Errors (result) | An array of errors for the result, if applicable. |
| Code (errors) | The error code related to the result, if applicable. |
| Message (errors) | A detailed message explaining the error for the result. |
| ID (result) | The unique identifier of the custom activity. |
| Marketo GUID (result) | The globally unique identifier (GUID) for the custom activity in Marketo. |
| API name (result) | The API name of the custom activity. |
| Status (result) | The status of the operation on the record, with values like `created`, `updated`, `deleted`, `skipped`, `added`, and `removed`. |

---
