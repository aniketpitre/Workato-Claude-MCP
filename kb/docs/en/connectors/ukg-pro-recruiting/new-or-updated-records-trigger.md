---
url: >-
  https://docs.workato.com/en/connectors/ukg-pro-recruiting/new-or-updated-records-trigger.md
description: >-
  The New or updated records trigger monitors UKG Pro (Recruiting) for newly
  created or updated records.
---

# UKG Pro (Recruiting) - New or updated records trigger

The **New or updated records** trigger monitors UKG Pro (Recruiting) for newly created or updated records.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the type of object to monitor. Additional fields load dynamically based on the object you select. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. Defaults to 1 hour ago if left blank. You can't change this value after the recipe runs or tests successfully. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, the **Candidate** object has the following output schema:

| Output field | Description |
| --- | --- |
| ID | The unique ID of a candidate in GUID format. |
| Creator | The creator of a candidate record. |
| Created at | The date and time a candidate was created. |
| Util person ID | The UKG Pro person ID. |
| EEID | The employee identifier. |
| Preferred locale | The preferred language of the candidate. |
| Integration user ID | The user ID used in 3rd party integrations, such as background check integrations. |
| Is internal | An indicator of whether or not a candidate is an internal employee. |
| Is active | An indicator of whether or not a candidate is an active employee. |
| Updated at | The date and time a candidate was last updated |
