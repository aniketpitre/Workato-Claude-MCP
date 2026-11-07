---
url: 'https://docs.workato.com/en/connectors/calendly/list-event-types-action.md'
description: >-
  The List event types action in the Calendly connector returns a paginated list
  of event types for an organization or user that match your search criteria.
---

# Calendly - List event types action

The **List event types** action returns a paginated list of event types that match your search criteria. By default, the action returns 20 records per page if the **Page size** field is left blank.

Use the **Organization** field to retrieve event types for the entire organization, or the **User** field to retrieve event types for a specific user within the organization.

## Input

| Input field | Description |
| --- | --- |
| Active | Select the value from the drop-down menu. Returns active event types if true, and inactive event types if false. Returns all event types if left blank. |
| Page size | Enter the number of records to return per page. Default is 20. |
| Page token | The token to pass to get the next or previous portion of the results. |
| Sort | Sorts the name column either in ascending or descending order. |
| Organization | View available personal, team, and organization event types associated with the organization's URI. |
| User | View available personal, team, and organization event types associated with the user's URI. |

## Output

| Output field | Description |
| --- | --- |
| URI | API URL of the event type resource. |
| Name | Name of the event type. |
| Active | Indicates if the event type is currently active. |
| Booking method | Specifies how the booking occurs. |
| Slug | Customizable URL identifier used in the scheduling link. |
| Scheduling URL | Public-facing URL where invitees can book this event. |
| Duration | Duration of the event in minutes. |
| Kind | Type of event owner, such as solo for individual events. |
| Pooling type | Defines how availability is pooled in team events. |
| Type | Internal classification of the event type. |
| Color | Hex code representing the event type color in the UI. |
| Created at | Timestamp when the event type was created. |
| Updated at | Timestamp when the event type was last updated. |
| Internal note | Notes visible only to the event owner for internal use. |
| Description plain | Plain-text description of the event type. |
| Description HTML | HTML-formatted description of the event type. |
| Profile | Associated user or team profile (usually refers to the host or group). |
| Secret | If true, the event type is hidden from public scheduling pages. |
| Custom questions | List of custom questions associated with the event. |
| Deleted at | Timestamp if the event type was deleted. |
| Kind description | Friendly name for the kind of event. |
| Admin managed | Indicates if the event type is managed by an admin. |
| Pagination | Container for pagination data. |
| Count | Number of event types returned in the current page. |
| Next page | URL to the next page of event types in the API response. |
| Previous page | URL to the previous page of event types in the API response. |
| Next page token | Token used to fetch the next page in paginated results. |
| Previous page token | Token used to fetch the previous page in paginated results. |

---
