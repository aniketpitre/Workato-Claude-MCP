---
url: >-
  https://docs.workato.com/en/connectors/plusone-solutions/search-records-action.md
description: >-
  The Search records action retrieves a list of records matching the specified
  criteria from PlusOne Solutions.
---

# PlusOne Solutions - Search records action

The **Search records** action retrieves a list of records matching the specified criteria from PlusOne Solutions.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to search for. |

Input fields load dynamically based on the selected **Object**. For example, the input schema is as follows if you select the **Company relationship** object:

| Input fields | Description |
| --- | --- |
| PlusOne Client ID | Provide the unique 13-character identifier assigned to each client in the PlusOne Network. |
| PlusOne Username | Provide the username assigned to the Individual making the request by PlusOne. Used to create audit log entries. Leaving this blank will use the email address from the connection. |
| PlusOne Client Company ID | Provide the unique identifier assigned to each company by the client. This can be different from the Company PlusOne ID. |
| Include Inactive | Select the boolean value from the drop-down menu. Choose 'Yes' to include inactive records or 'No' to exclude them. |
| Offset | Provide the number of records to skip from the beginning of the result set. |
| Page Size | Provide the number of records to return. Defaults to 1000 if not specified. |

## Output

Output fields load dynamically based on the selected **Object**. For example, the output schema is as follows if you select the **Company relationship** object:

| Output fields | Description |
| --- | --- |
| Records | Array of company relationship records. |
| Company PlusOne ID | PlusOne's unique company identifier for each record. |
| Client PlusOne ID | PlusOne's unique client identifier for each record. |
| Company ID | Internal company identifier for each record. |
| Company Registration Date | Date when the company was registered. |
| Company Contract Expiration | Contract expiration date. |
| Company | Object containing basic company information including name, DBA, tax information, and company type. |
