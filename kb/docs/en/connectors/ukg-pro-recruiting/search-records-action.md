---
url: >-
  https://docs.workato.com/en/connectors/ukg-pro-recruiting/search-records-action.md
description: >-
  The Search records action retrieves a list of records from UKG Pro
  (Recruiting) that match your search criteria.
---

# UKG Pro (Recruiting) - Search records action

The **Search records** action retrieves a list of records from UKG Pro (Recruiting) that match your search criteria.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the type of object to search. Additional fields load dynamically based on the object you select. |

Workato dynamically populates additional fields depending on the object you select. For example, the **Candidate** object has the following input fields:

| Input fields | Description |
| --- | --- |
| Page | Specify a page number to return paginated records. |
| Per page | Specify the number of records to return per page. |
| Candidate type | Select the type of candidate to return. Defaults to all. |
| Updated after | Specify a date to filter records by. The action only returns records updated after this date. |
| Role | Select the role to filter the returned candidates. |
| Updated before | Specify a date to filter records by. The action only returns records updated before this date. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, the **Candidate** object has the following output schema:

| Output field | Description |
| --- | --- |
| ID | The unique ID of a candidate in GUID format. |
| Creator | The creator of a candidate record. |
| Created at | The date and time a candidate was created. |
| Util person ID | The UKG Pro person ID. |
| EEID | The employee identifier. |
| Preferred\_locale | The preferred language of the candidate. |
| Integration user ID | The user ID used in 3rd party integrations, such as background check integrations. |
| Is internal | indicator of whether or not a candidate is an internal employee. |
| Is active | indicator of whether or not a candidate is an active employee. |
| Updated at | The date and time a candidate was last updated. |
