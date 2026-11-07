---
url: >-
  https://docs.workato.com/en/connectors/plusone-solutions/create-record-action.md
description: >-
  The Create record action creates a standard record, such as a company, in
  PlusOne Solutions.
---

# PlusOne Solutions - Create record action

The **Create record** action creates a standard record, such as a company, in PlusOne Solutions.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to create. |

Input fields load dynamically based on the selected **Object**. For example, the input schema is as follows if you select the **Company** object:

| Input fields | Description |
| --- | --- |
| PlusOne Client ID | Provide the unique 13-character identifier assigned to each client in the PlusOne Network. |
| PlusOne Username | Provide the username assigned to the individual making the request. This is used for audit log entries. Leave this field blank to use the email address specified during [connection setup](/en/connectors/plusone-solutions#connection-setup). |
| Tax ID | Provide the tax identifier for the company. A full tax ID should only be passed when a company is first created. |
| Tax ID Type | Provide the type of tax identifier, such as `SSN` or `EIN`. |
| Company Name | Provide the name of the company to create. |
| DBA | Provide the DBA (Doing Business As) name of the company. |
| Company Type | Provide the type of company structure, such as `CC`. |
| Minority Type | Provide the minority business classification, such as `MINOR`. |
| URL | Provide the company website URL. |
| State of Incorporation | Provide the state ID where the company is incorporated, such as `AL` for Alabama. |
| PENDOT ID | Provide the PENDOT identifier for the company. |
| Addresses | Provide an array of address objects containing the company's type, address lines, city, state, country, and ZIP code. |

## Output

Output fields load dynamically based on the selected **Object**. For example, the output schema is as follows if you select the **Company** object:

| Output field | Description |
| --- | --- |
| Company PlusOne ID | PlusOne's unique company identifier for the newly created company. |
| Company | Object containing details about the newly created company. |
| Client PlusOne ID | PlusOne's unique client identifier. |
| Company ID | Internal company identifier. |
| Company Registration Date | Date when the company was registered. |
| Company Contract Expiration | Contract expiration date. |
