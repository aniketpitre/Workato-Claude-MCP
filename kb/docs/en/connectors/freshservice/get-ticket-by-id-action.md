---
url: 'https://docs.workato.com/en/connectors/freshservice/get-ticket-by-id-action.md'
description: >-
  The action allows you to retrieve the details of a ticket based on the ticket
  ID.
---

# Freshservice - Get ticket by ID action

The **Get ticket by ID** action allows you to retrieve the details of a ticket based on the ticket ID.

## Input

| Input field | Description |
| --- | --- |
| Ticket ID | Provide the ID of the ticket to retrieve. |
| Embed Fields | By default, certain fields such as conversations, tags, and requester email aren't included in the response. They can be retrieved with embedding functionality. Select the fields you plan to include from the drop-down menu. |

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
  https://docs.workato.com/en/connectors/freshservice/list-agent-fields-action.md
description: The List agent fields action lists all agent fields in Freshservice.
---

# Freshservice - List agent fields action

The **List agent fields** action lists all agent fields in Freshservice.

## Input

This action doesn't require any input fields.

## Output

| Output field | Description |
| --- | --- |
| Name | The internal field name used in the system. |
| Label for admins | The display label of the field when viewed by administrators. |
| Mandatory for admins | Indicates whether the field is required for administrators. |
| Editable by admins | Specifies if administrators can edit the field. |
| Label for agents | The display label of the field when viewed by agents. |
| Editable by agents | Specifies if agents can edit the field. |
| Mandatory for agents | Indicates whether the field is required for agents. |
| Visible to agents | Determines if agents can see the field. |
| Type | The type of field. |
| Default field | Indicates whether this is a default system field. |

---

---
url: >-
  https://docs.workato.com/en/connectors/freshservice/list-onboarding-form-fields-action.md
description: Lists the onboarding form fields of Freshservice.
---

# Freshservice - List onboarding form fields action

The **List onboarding form fields** action lists the onboarding form fields of Freshservice.

## Input

This action doesn't require any input fields.

## Output

| Output field | Description |
| --- | --- |
| Placeholder | Placeholder of the field. |
| Label | Label of the field. |
| Name | Name of the field. |
| Position | Position of the field. |
| Required | Boolean, indicating whether the field is required or not during form submission. |
| Default | Boolean indicating whether the field is default or not. |
| Field type | Indicates the type of field. |
| Data source | Indicates the type of data source. This value is only available for the `custom_lookup_bigint` field type. |

---

---
url: >-
  https://docs.workato.com/en/connectors/freshservice/list-requester-fields-action.md
description: 'Lists the requester fields of Freshservice.   '
---

# Freshservice - List requester fields action

The **List requester fields** action lists the requester fields of Freshservice.

## Input

This action doesn't require any input fields.

## Output

| Output field | Description |
| --- | --- |
| Editable in signup | Set to true if the field can be updated by requesters. |
| Requester ID | ID of the requester field. |
| Label | Display name for the field. |
| Name | Name of the requester field. |
| Position | Position of the requester field in the form. |
| Type | For custom requester fields, the type of value associated with the field. |
| Default | Boolean indicating whether the field is default or not. |
| Requesters can edit | Indicates whether requesters can edit the field in the support portal. |
| Label for requesters | Display name for the field as seen in the support portal. |
| Required for requesters | Set to true if the field is mandatory in the support portal. |
| Displayed for requesters | Determines if requesters can see the field in the support portal. |
| Required for agents | Set to true if the field is mandatory for agents. |
| Created at | Timestamp when requester was created. |
| Updated at | Timestamp when requester was last updated. |
| Choices | List of values supported by the field. |

---

---
url: >-
  https://docs.workato.com/en/connectors/freshservice/list-service-item-action.md
description: Returns a list of service items based on specified filters.
---

# Freshservice - List service items action

The **List service items** action returns a list of service items based on specified filters.

## Input

| Input field | Description |
| --- | --- |
| Category ID | Provide the category ID of service item. |
| Result per page | Provide a value between 1 to 100. |
| Page number | Provide the number of pages. |

## Output

| Output field | Description |
| --- | --- |
| Service item ID | Unique ID of the item. |
| Workspace ID | ID of the workspace to which the service item belongs (applicable for Employee Support Mode). |
| Created at | The timestamp when the item was created. |
| Updated at | The timestamp when the item was last updated. |
| Name | Name of the service item. |
| Delivery time | Estimated delivery time of the item (in hours). |
| Display ID | Unique ID of the service item specific to the account. |
| Category ID | Unique ID of the category to which the service item belongs. |
| Product ID | The ID of the product mapped to the item (returns null if no product is mapped). |
| Quantity | The number of items requested. |
| Deleted | True indicates the item was deleted successfully. |
| Group visibility | 1 denotes visibility to all requesters, 2 for restricted visibility. |
| Item type | 1 indicates a normal item, 2 indicates a loaner item. |
| CI type ID | Unique ID of the asset type associated with the product. |
| Cost visibility | Set to true if the cost should be visible to the requester. |
| Delivery time visibility | Set to true if the delivery time of the item should be visible to the requester. |
| Configs | Configuration template for the service request subject. |
| Botified | Set to true if the item is "bot ready." |
| Visibility | 1 denotes draft, 2 denotes published. |
| Allow attachments | Set to true if the requester is allowed to attach files. |
| Allow quantity | Set to true to allow the requester to request more than one quantity. |
| Is bundle | Indicating whether the item contains child items. |
| Create child | Indicating whether child items will be created as separate service requests. |

---
