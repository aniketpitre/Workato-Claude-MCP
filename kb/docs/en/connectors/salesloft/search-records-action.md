---
url: 'https://docs.workato.com/en/connectors/salesloft/search-records-action.md'
description: >-
  The search record action enables you to retrieve multiple records of an
  object, such as person or call, from Salesloft.
---

# Salesloft - Search records action

The **Search records** action enables you to retrieve multiple records of an object, such as person or call, from Salesloft. The records can be filtered, paginated, and sorted according to the specified fields. By default, this action returns a maximum of 25 records. You can use the **Page size** field to increase this quota up to 100 records.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object to be retrieved from the drop-down menu. |
| IDs of record to fetch | Provide the unique ID of the object to be retrieved. |
| Page size | Specify the number of records to show per page. The default is 25. |
| Sort by | Select the field to sort the records with from the drop-down menu. |
| Sort direction | Select direction to sort the records from the drop-down menu. |

Input fields are loaded dynamically based on the object you select.

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, if the select object is **Cadence** then the output schema is as follows.

| Output fields | Description |
| --- | --- |
| Cadence ID | The unique identifier assigned to the cadence in Salesloft. |
| Created at | Timestamp indicating when the cadence was originally created. |
| Updated at | Timestamp of the most recent update made to the cadence. |
| Archived at | Timestamp showing when the cadence was archived, if applicable. |
| Team cadence | Indicates whether the cadence is shared with a team. |
| Shared | Denotes if the cadence is shared with other users. |
| Remove bounces enabled | Boolean value showing if bounced leads are automatically removed from the cadence. |
| Remove replies enabled | Boolean indicating whether replied leads are automatically removed from the cadence. |
| Opt out link included | Indicates whether an opt-out/unsubscribe link is included in the cadence communications. |
| Cadence name | The title or label of the cadence, used for identification. |
| Tags | Labels or categories assigned to the cadence for grouping or filtering. |
| Creator | Name or identifier of the user who created the cadence. |
| Owner | The current owner or manager of the cadence. |
| Bounced stage | Stage in the cadence where bounced emails are moved to. |
| Replied stage | Stage where contacts go when they reply to cadence communication. |
| Added stage | The initial stage where leads enter the cadence. |
| Finished stage | The final stage where completed cadence contacts are placed. |
| Counts | Object showing statistics related to the cadence. |
| Paging | Object showing the metadata of the result set, such as current page, per page. |

---
