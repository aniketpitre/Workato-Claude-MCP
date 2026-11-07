---
url: >-
  https://docs.workato.com/en/connectors/freshservice/create-service-request-action.md
description: Creates a new service request in Freshservice.
---

# Freshservice - Create service request action

The **Create service request** action creates a new service request in Freshservice.

## Input

| Input field | Description |
| --- | --- |
| Service item | Select the service item from the drop-down menu. |
| Quantity | Provide the quantity number. |
| Email | Provide the email ID of the requester. |
| Requested for | Provide the email ID of the requester on whose behalf the service request is created. |
| Custom fields | Provide custom fields in key-value pairs. |
| Child service items | Select the child service items from the drop-down menu. |

## Output

| Output field | Description |
| --- | --- |
| Service request ID | A unique identifier assigned to the service request. |
| Type | The type of request, such as a Service Request or Incident. |
| CC emails | List of email addresses copied in the request. |
| Forward emails | List of email addresses the request has been forwarded to. |
| Reply CC emails | Email addresses copied in replies to the request. |
| Fr escalated | Indicates if the request was escalated for the first response. |
| Spam | Indicates if the request was marked as spam. |
| Email config ID | The identifier for the email configuration used. |
| Group ID | The unique identifier of the group handling the request. |
| Priority | The priority level of the request. |
| Requester ID | The unique identifier of the person who raised the request. |
| Responder ID | The unique identifier of the agent assigned to the request. |
| Source | The channel through which the request was created. |
| Status | The current status of the request. |
| Subject | The subject line or title of the request. |
| To emails | List of recipient email addresses in the request. |
| SLA policy ID | The identifier for the SLA (Service Level Agreement) applied to the request. |
| Department ID | The unique identifier of the department responsible for the request. |
| Workspace ID | The unique identifier of the workspace the request belongs to. |
| Due by | The deadline by which the request should be resolved. |
| Fr due by | The deadline for the first response to the request. |
| Is escalated | Indicates if the request has been escalated. |
| Description | A detailed explanation of the request. |
| Description text | A plain-text version of the request description. |
| Created at | The timestamp when the request was created. |
| Updated at | The timestamp when the request was last updated. |
| Urgency | The urgency level of the request, affecting prioritization. |
| Impact | The level of impact the request has on operations or users. |
| Category | The high-level classification of the request. |
| Sub category | A more specific classification under the main category. |
| Item category | The specific item or service related to the request. |
| Deleted | Indicates if the request has been deleted. |
| Attachments | Files or documents attached to the request. |
| Approval status | The current approval state of the request. |
| Approval status name | The name of the approval status for better readability. |
| Custom fields | Additional custom attributes associated with the request. |
