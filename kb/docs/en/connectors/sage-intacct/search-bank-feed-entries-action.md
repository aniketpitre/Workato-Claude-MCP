---
url: >-
  https://docs.workato.com/en/connectors/sage-intacct/search-bank-feed-entries-action.md
description: >-
  The Search bank feed entries action retrieves the bank feed entries matching
  the search criteria from Sage Intacct.
---

# Sage Intacct (Custom) - Search bank feed entries action

The **Search bank feed entries** action retrieves the bank feed entries matching the search criteria from Sage Intacct.

## Input

| Input field | Description |
| --- | --- |
| Record number | Provide the record number of the bank feed entry to search for. |
| Bank account ID | Provide the bank account ID to search for. |
| Bank account name | Provide the bank account name to search for. |
| Description | Provide the description to search for. |

## Output

| Output fields | Description |
| --- | --- |
| Record number | Unique identifier for the individual bank feed entry record. |
| Bank account ID | The unique identifier or code of the bank account linked to the feed entry. |
| Bank account name | The name or label of the bank account associated with the transaction. |
| Account transaction feed key | Internal system key identifying the bank feed transaction. |
| Transaction ID | External or internal transaction identifier (often from the bank). |
| Bank account reconciliation key | Internal key for the reconciliation batch the transaction belongs to. |
| Posting date | The date the transaction is posted to the general ledger or bank account. |
| Transaction type | Type of transaction. |
| Document type | Type of source document. |
| Document number | Identifier of the document linked to the transaction. |
| Payee | The name of the entity or individual associated with the transaction. |
| Transaction amount | The total amount of the bank transaction. |
| Description | Textual description or memo associated with the transaction. |
| Cleared | Indicates if the transaction has been cleared during bank reconciliation. |
| Amount to match | The portion of the transaction amount that remains to be matched or reconciled. |
| Record data | Raw or structured data details captured from the bank feed. |
| When created | Timestamp when the feed entry was created in Intacct. |
| When modified | Timestamp of the most recent modification to the entry. |
| Created by | User ID or system that created the feed record. |
| Modified by | User ID who last modified the feed record. |
| Feed type | Indicates how the data was fed into Intacct. |
| Currency | The currency in which the transaction was made. |
