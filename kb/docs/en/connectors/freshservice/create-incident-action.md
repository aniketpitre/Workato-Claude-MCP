---
url: 'https://docs.workato.com/en/connectors/freshservice/create-incident-action.md'
description: This action enables you to create tickets of type **Incident**.
---

# Freshservice - Create incident action

The **Create incident** action enables you to create incident tickets.

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Select the workspace ID from the drop-down menu. |
| Subject | Subject of the ticket. The default value is null. |
| Description | The description loads dynamically based on the selected file. |
| Requester | Provide the requester details such as the requester ID, email, phone, and name. |
| Status | Select a value from the drop-down menu. |
| Priority | Select a value from the drop-down menu. |
| Group ID | Select a value from the drop-down menu. |
| Department ID | Select a value from the drop-down menu. |
| Agent ID | Select a value from the drop-down menu. |
| Type | Select a value from the drop-down menu. |
| CC email | Email address added in the 'cc' field of the incoming ticket email. |
| Custom fields | Provide the key-value pair containing the names and values of the (custom) agent fields. |
| Email config ID | Provide the ID of the email config used for this ticket. |
| Category | Select a value from the drop-down menu. |
| Sub category | Select a value from the drop-down menu. |
| Item category | Select a value from the drop-down menu. |
| Source | Select a value from the drop-down menu. |
| Tags | Provide tags that have been associated with the ticket. |
| Response within | Provide the timestamp that denotes when the first response is due. |
| Resolve within | Provide the timestamp that denotes when the ticket must be resolved. |
| Urgency | Select a value from the drop-down menu. |
| Impact | Select a value from the drop-down menu. |
| Planned start date | Provide the planned start date in timestamp format. |
| Planned end date | Provide the planned end date in timestamp format. |
| Planned effort | Provide planned efforts in this field. |

## Output

| Field | Description |
| --- | --- |
| Ticket ID | A unique identifier assigned to the ticket. |
| Department ID | The ID of the department handling the ticket. |
| CC emails | Email addresses that receive copies of ticket updates. |
| Forward emails | Email addresses where the ticket can be forwarded. |
| Reply CC emails | Email addresses that are copied in replies to the ticket. |
| Custom fields | Additional fields for capturing specific information related to the ticket. |
| Deleted | Indicates whether the ticket has been deleted (true/false). |
| Description | Detailed text describing the issue or request. |
| Due by | The deadline by which the ticket needs to be resolved. |
| Email config ID | The email configuration associated with this ticket. |
| First response due by | The deadline for the first response to the ticket. |
| First response escalated | Indicates if the first response deadline was missed (true/false). |
| Group ID | The ID of the support group handling the ticket. |
| Is escalated | Indicates whether the ticket has been escalated (true/false). |
| Priority | The urgency level of the ticket, typically on a scale (with 1 being high priority). |
| Category | The main category assigned to the ticket. |
| Sub category | A more specific classification under the main category. |
| Item category | Further classification of the issue within the subcategory. |
| Requester ID | The unique identifier of the person who raised the ticket. |
| Responder ID | The unique identifier of the person handling the ticket. |
| Requested for ID | The unique identifier of the individual for whom the request is made. |
| Source | The origin of the ticket (e.g., email, portal, phone call). |
| Spam | Indicates if the ticket was marked as spam (true/false). |
| Subject | A short summary of the ticket's issue or request. |
| Tags | Keywords or labels used for categorizing the ticket. |
| Status | The current state of the ticket (e.g., open, in progress, resolved). |
| To emails | The primary email addresses to which the ticket notifications are sent. |
| Type | Specifies whether the ticket is an incident, service request, etc. |
| Urgency | The level of urgency assigned to the ticket. |
| Impact | The extent to which the issue affects operations. |
| Workspace ID | The ID of the workspace or environment where the ticket belongs. |
| Resolution notes | Notes describing how the issue was resolved. |
| Department name | The name of the department handling the ticket. |
| Resolution notes (HTML) | HTML-formatted version of the resolution notes. |
| Attachments | Files attached to the ticket for reference. |
| Planned start date | The date when work on the ticket is planned to start. |
| Planned end date | The expected completion date for the ticket resolution. |
| Planned effort | The estimated amount of effort required to resolve the ticket. |
| Created at | The timestamp when the ticket was created. |
| Updated at | The timestamp when the ticket was last modified. |
| Closed at | The timestamp when the ticket was marked as resolved/closed. |
| Tasks dependency type | Specifies whether the ticket is dependent on other tasks. |
| SLA policy ID | The service level agreement (SLA) policy applied to the ticket. |
| BCC emails | Email addresses that receive blind carbon copies of ticket updates. |
| Applied business hours | The working hours applicable to the ticket. |
| Status page ref ID | Reference ID for the status page associated with the ticket. |
| Human display ID | A human-friendly identifier for the ticket. |
| Display ID | Another identifier used for displaying the ticket. |
| Created within business hours | Indicates whether the ticket was created during working hours. |
| Is editable | Specifies whether the ticket details can be modified. |
| Email failure | Indicates if there was a failure in sending an email related to the ticket. |
| Requester | Will return requester details like id, name, mobile, phone. |
| Requested for | Will return details of the user on behalf of whom the request has been raised |
| Problem | Returns details of associated problem |
| Stats | Will return the ticket’s closed\_at, resolved\_at and first\_responded\_at time |
| Change | Returns list of associated changes and the causing changes details |
| Change initiated by ticket | Indicates if this ticket has triggered a change request. |
| Change initiating ticket | Details of the ticket that initiated a change request. |
| Changes initiated by ticket | The list of changes triggered by this ticket. |
| Conversations | Communication and discussions related to the ticket. |
| Related tickets | Returns child ticket IDs/parent ticket IDs based on the ticket. No IDs are returned for parent tickets without child tickets. |
| Impacted services | Services affected by the issue reported in the ticket. |
| Assets | Returns set of associated asset details |

---

---
url: >-
  https://docs.workato.com/en/connectors/freshservice/create-onboarding-request-action.md
description: 'This action creates employee onboarding request in Freshservice. '
---

# Freshservice - Create onboarding request action

The **Create onboarding request** action creates an employee onboarding request in Freshservice.

## Input

| Input field | Description |
| --- | --- |
| Reporting manager | Select the reporting manager from the drop-down menu. |
| Employee first name (preferred) | Provide the first name of the employee. |
| Employee last name | Provide the last name of the employee. |
| Start date | Provide the start date of the employee. |
| Job title | Provide the job title held by the employee. |
| Department | Select a value from the drop-down menu or provide a custom value of the department of the employee. |
| Location | Select a value from the drop-down menu or provide a custom value of the location of the employee. |
| Mobile device election | Select a value from the drop-down menu or provide a custom value. |

## Output

| Output field | Description |
| --- | --- |
| Onboarding request ID | A unique identifier assigned to the onboarding request. |
| Created at | The timestamp when the onboarding request was created. |
| Updated at | The timestamp when the onboarding request was last updated. |
| Status | The current status of the onboarding request. |
| Subject | The title or subject of the onboarding request. |
| Ticket ID | A unique identifier linked to the onboarding ticket. |
| HR manager | This object contains the details of the HR manager, such as name and email. |
| Field | Returns the fields provided in request. |
| Reporting manager | This object contains the details of the reporting manager, such as name, ID, phone, and email. |
| Department | The object contains the department details such as name and description. |
| Location | This object contains the details of the location. |

---
