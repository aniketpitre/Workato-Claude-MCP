---
url: >-
  https://docs.workato.com/en/connectors/plusone-solutions/get-record-details-action.md
description: >-
  The Get record details by ID action retrieves specific record information from
  PlusOne Solutions using the record's unique identifier.
---

# PlusOne Solutions - Get record details by ID action

The **Get record details by ID** action retrieves specific record information from PlusOne Solutions using the record's unique identifier.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to retrieve. |

Input fields load dynamically based on the selected **Object**. For example, the input schema is as follows if you select the **Company details** object:

| Input fields | Description |
| --- | --- |
| PlusOne Company ID | Provide the unique 13-character identifier assigned to the company in the PlusOne Network. |
| PlusOne Username | Provide the username assigned to the individual making the request. This is used for audit log entries. Leave this field blank to use the email address specified during [connection setup](/en/connectors/plusone-solutions#connection-setup). |

## Output

Output fields load dynamically based on the selected **Object**. For example, the output schema is as follows if you select the **Company details** object:

| Output field | Description |
| --- | --- |
| PlusOne ID | Unique 13-character identifier assigned to the company in the PlusOne Network. |
| Company Name | Name of the company. |
| DBA | Doing Business As (DBA) name. |
| Tax ID | Tax identifier assigned to the company. |
| Tax ID Type | Type of tax identifier, such as `EIN` or `SSN`. |
| Company Type | Type of company structure, such as `CC`. |
| Minority Type | Minority business classification. |
| URL | Company website URL. |
| State of Incorporation | State where the company is incorporated. |
| PENDOT ID | PENDOT identifier. |
| Primary Location | Indicates whether this is the primary location. |
| Phone Numbers | Array of phone number objects with type, number, and extension. |
| Addresses | Array of address objects with complete address information. |
| Emails | Array of email objects with type and email address. |
| Industries | Array of industry classification objects. |
| Contacts | Array of contact objects with detailed contact information. |
