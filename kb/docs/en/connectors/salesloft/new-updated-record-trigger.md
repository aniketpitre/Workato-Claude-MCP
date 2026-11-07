---
url: 'https://docs.workato.com/en/connectors/salesloft/new-updated-record-trigger.md'
description: 'Triggers when an object, such as person, is created or updated in Salesloft.'
---

# Salesloft - New/updated record trigger

The **New/updated record** trigger activates when an object, such as person, is created or updated in Salesloft.

## Input

| Input field | Description |
| --- | --- |
| Object name | Select a Salesloft object from the drop-down menu. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, if the selected object is **Cadence**, then the output schema is as follows.

| Output field | Description |
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

---
