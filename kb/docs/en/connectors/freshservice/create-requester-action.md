---
url: 'https://docs.workato.com/en/connectors/freshservice/create-requester-action.md'
description: >-
  Creates a requester in Freshservice by providing Primary email, Work phone
  number, or Mobile phone number - one of the three is mandatory to create a
  requester.
---

# Freshservice - Create requester action

The **Create requester** action creates a requester in Freshservice by providing the primary email, work phone number, or mobile phone number. At least one of these values is required to create a requester.

## Input

| Input field | Description |
| --- | --- |
| First name | Select the object you plan to delete from the drop-down menu. Fields load dynamically based on the object you select. |
| Last name | Provide the unique ID of the object you plan to delete. |
| Job title | Provide the requester's job title. |
| Primary email | Provide the requester's primary email. |
| Secondary emails | Provide the requester's secondary emails. |
| Work phone number | Provide the requester's work phone number. |
| Mobile phone number | Provide the requester's mobile phone number. |
| Department IDs | Provide the unique IDs of the departments associated with the requester. |
| Can see all tickets from associated departments | Indicates whether the agent has access to all tickets within their department (true/false). |
| Reporting manager ID | Provide the user ID of the requester’s reporting manager. |
| Address | Provide the requester's address. |
| Time zone | Provide the requester's timezone. |
| Time format | Provide the time format of the requester, such as 12h or 24h. |
| Language | Provide the requester's language. Default is English. |
| Location ID | Provide the unique ID of the location associated with the requester. |
| Background information | Provide background information of the requester. |
| Custom fields | Key-value pair containing the names and values of the (custom) fields. |

## Output

| Field | Description |
| --- | --- |
| Requester ID | A unique identifier assigned to the requester. |
| Is agent | Indicates whether the requester is an agent. |
| First name | Select the object you wish to delete, from the drop-down menu. Fields will dynamically load based on selected object. |
| Last name | Provide unique ID of the object to be deleted. |
| Job title | Provide job title of the requester. |
| Primary email | Provide the primary email of the requester. |
| Secondary emails | Provide secondary emails of the requester. |
| Work phone number | Provide work phone number of the requester. |
| Mobile phone number | Provide mobile phone number of the requester. |
| Department IDs | Provide unique IDs of the departments associated with the requester. |
| Can see all tickets from associated departments | Indicates whether the agent has access to all tickets within their department (true/false). |
| Reporting manager ID | Provide user ID of requester’s reporting manager. |
| Address | Provide the address of the requester. |
| Time zone | Provide timezone of the requester. |
| Time format | Provide the time format of the requester, such as 12h or 24h. |
| Language | Provide the language of the requester. |
| Location ID | Provide unique ID of the location associated with the requester. |
| Background information | Provide background information of the requester. |
| Custom fields | Key-value pair containing the names and values of the (custom) fields. |
| Active | Indicates whether the requester is currently active. |
| Has logged in | Indicates whether the requester has ever logged into the system. |
| Created at | The timestamp when the requester was created. |
| Updated at | The timestamp when the requester was last updated. |
| Department names | The name of the requester’s department. |
| External ID | A unique identifier for external system integrations. |
| Location name | The name linked to the requester’s location ID. |
| Work schedule ID | The identifier for the requester’s assigned work schedule. |
| VIP user | Indicates whether the requester is considered a VIP user. |

---

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

---
