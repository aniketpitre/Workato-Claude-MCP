---
url: >-
  https://docs.workato.com/en/connectors/ukg-pro-recruiting/create-record-action.md
description: The Create record action creates a new record in UKG Pro (Recruiting).
---

# UKG Pro (Recruiting) - Create record action

The **Create record** action creates a new record in UKG Pro (Recruiting).

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the type of object to create. Additional fields load dynamically based on the object you select. |

Workato dynamically populates additional fields depending on the object you select. For example, the **Candidate** object has the following input fields:

| Input fields | Description |
| --- | --- |
| First | Provide the first name of the candidate. |
| Last | Provide the last name of the candidate. |
| Middle | Provide the middle name of the candidate. |
| Former | Provide the former name of the candidate. |
| Preferred name | Provide the preferred name of the candidate. |
| Prefix | Provide the prefix for the candidate's name. |
| Suffix | Provide the suffix for the candidate's name. |
| Contact information | Provide the contact information of the candidate. |
| Provider | Provide the provider details. |
| Integration user ID | Provide the ID of the integration user. |
| Is willing to relocate | Specify whether the candidate is willing to relocate. |
| Is internal | Specify whether the candidate is an internal employee. |
| Is active | Specify whether the candidate is an active employee. |
| Work experience | Provide details about the applicant's work experience. |
| Education | Provide details about the applicant's education. |
| Skills | Provide details about the applicant's skills. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, the **Candidate** object has the following output schema:

| Output field | Description |
| --- | --- |
| ID | The unique ID of a candidate in GUID format. |
| Creator | The creator of a candidate record. |
| Created at | The date and time a candidate was created. |
| Util person ID | The UKG Pro person ID. |
| EEID | The employee Identifier. |
| Preferred\_locale | The preferred language of the candidate. |
| Integration user ID | The user ID used in 3rd party integrations, such as background check integrations. |
| Is internal | indicator of whether or not a candidate is an internal employee. |
| Is active | indicator of whether or not a candidate is an active employee. |
| Updated at | The date and time a candidate was last updated. |
