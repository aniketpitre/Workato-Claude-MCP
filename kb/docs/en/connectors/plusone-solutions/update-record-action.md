---
url: >-
  https://docs.workato.com/en/connectors/plusone-solutions/update-record-action.md
description: The Update record action updates the specified record in PlusOne Solutions.
---

# PlusOne Solutions - Update record action

The **Update record** action updates the specified record in PlusOne Solutions.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to update. |

Input fields load dynamically based on the selected **Object**. For example, the input schema is as follows if you select the **Company relationship** object:

| Input fields | Description |
| --- | --- |
| PlusOne Client ID | Provide the unique 13-character identifier assigned to each client in the PlusOne Network. |
| PlusOne Company ID | Provide the unique 13-character identifier assigned to each company in the PlusOne Network. |
| PlusOne Username | Provide the username assigned to the individual making the request. This is used for audit log entries. Leave this field blank to use the email address specified during [connection setup](/en/connectors/plusone-solutions#connection-setup). |
| Jobscope Vendor Number | Provide a valid Jobscope vendor number for the update. |

## Output

Output fields load dynamically based on the selected **Object**. For example, the output schema is as follows if you select the **Company relationship** object:

| Output field | Description |
| --- | --- |
| Company PlusOne ID | PlusOne's unique company identifier. |
| Company | Updated company information object containing all company details. |
| Client PlusOne ID | PlusOne's unique client identifier. |
| Company ID | Internal company identifier. |
| Company Registration Date | Date when the company was registered. |
| Company Contract Expiration | Updated contract expiration date. |
