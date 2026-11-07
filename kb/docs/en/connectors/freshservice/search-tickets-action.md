---
url: 'https://docs.workato.com/en/connectors/freshservice/search-tickets-action.md'
description: >-
  The Search action will return results that match all your search criteria.
  Returns a maximum of 30 records.
---

# Freshservice - Search tickets action

The **Search tickets** action returns results that match your search criteria. Returns a maximum of 30 records.

## Input

| Input field | Description |
| --- | --- |
| Requester | Provide either the email or unique ID of requester. |
| Predefined filters | Select the option from the drop-down menu. |
| Sort by | Select the field from the drop-down menu to sort the result by field. |

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
