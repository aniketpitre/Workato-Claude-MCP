---
url: 'https://docs.workato.com/en/connectors/ukg-pro-recruiting/get-record-action.md'
description: >-
  The Get record action retrieves the details of a specific record in UKG Pro
  (Recruiting).
---

# UKG Pro (Recruiting) - Get record action

The **Get record** action retrieves the details of a specific record in UKG Pro (Recruiting).

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the type of object to retrieve details from. Additional fields load dynamically based on the object you select. |
| ID | Enter the unique identifier of the record to retrieve. |

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

---

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

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/ukg-pro-recruiting/upload-record-action.md
description: The Upload record action uploads a document to UKG Pro (Recruiting).
---

# UKG Pro (Recruiting) - Upload record action

The **Upload record** action uploads a document to UKG Pro (Recruiting).

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve a list of records. Fields load dynamically based on the object you select. |

Workato dynamically populates additional fields depending on the object you select. For example, the **Application document** object has the following input fields:

| Input fields | Description |
| --- | --- |
| Application ID | Provide the unique ID of an application. |
| File | Provide the file name and content. The file name must not be empty, contain only spaces, or include these characters: `/ \\? : \* " \< \> |`. The file extension must be: `.jpg`, `.jpeg`, `.png`, `.pdf`, `.doc`, or `.docx`. |
| Metadata | Provide the metadata associated with an uploaded file. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, the **Application document** object has the following output schema:

| Output field | Description |
| --- | --- |
| ID | The Application ID (GUID). |
| File name | The name of the uploaded file. |
| Document type | The type or category of the uploaded document. |
| Description | The description for the document. |
| Creator | The ID of the user who uploaded the document. |
| Links | URLs associated with the uploaded document. |

---
