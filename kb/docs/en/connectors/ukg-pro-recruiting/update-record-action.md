---
url: >-
  https://docs.workato.com/en/connectors/ukg-pro-recruiting/update-record-action.md
description: >-
  The Update record action updates the details of a specific record in UKG Pro
  (Recruiting).
---

# UKG Pro (Recruiting) - Update record action

The **Update record** action updates the details of a specific record in UKG Pro (Recruiting).

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the type of object to update. Additional fields load dynamically based on the object you select. |

Workato dynamically populates additional fields depending on the object you select. For example, the **Candidate** object has the following input fields:

| Input fields | Description |
| --- | --- |
| Candidate ID | Provide the unique ID of a candidate. |
| Reference ID | Provide the unique ID of a candidate reference. |
| First | Provide the first name of the candidate. |
| Last | Provide the last name of the candidate. |
| Middle | Provide the middle name of the candidate. |
| Former | Provide the former name of the candidate. |
| Preferred name | Provide the preferred name of the candidate. |
| Prefix | Provide the prefix for the candidate's name. |
| Suffix | Provide the suffix for the candidate's name. |
| Contact information | Provide the contact information of the candidate. |
| Company | Provide the company details. |
| Job title | Provide the Job title details. |
| Relationship | Provide the relationship details. |
| Recommendation | Provide the recommendation details. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, the **Candidate** object has the following output schema:

| Output fields | Description |
| --- | --- |
| ID | The unique ID of a candidate. |
| First | The first name of the candidate. |
| Last | The last name of the candidate. |
| Middle | The middle name of the candidate. |
| Former | The former name of the candidate. |
| Preferred name | The preferred name of the candidate. |
| Prefix | The prefix for the candidate's name. |
| Suffix | The suffix for the candidate's name. |
| Contact information | The contact information of the candidate. |
| Company | The company details. |
| Job title | The candidate's job title. |
| Relationship | The relationship details. |
| Recommendation | The recommendation details. |
