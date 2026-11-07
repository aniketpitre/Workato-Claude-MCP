---
url: >-
  https://docs.workato.com/en/connectors/mufg/actions/account-transaction-inquiry.md
description: >-
  The Account transaction inquiry action retrieves all transaction details for a
  specified MUFG account. You can filter transactions by date range and navigate
  through large result sets using pagination.
---

# MUFG - Account transaction inquiry action

The **Account transaction inquiry** action retrieves all transaction details for a specified MUFG account. You can filter transactions by date range and navigate through large result sets using pagination.

## Input

| Input field | Description |
| --- | --- |
| Account ID | Enter the account identifier consisting of Branch (3 digits) + Account Type (1 digit) + Account Number (7 digits). For example, `00111234567`. |
| Inquiry date from | Select the start date for the transaction inquiry. Defaults to today if not specified. |
| Inquiry date to | Select the end date for the transaction inquiry. Defaults to today if not specified. |
| Next page keyword | Enter the next page keyword value from a previous response to retrieve additional pages of results. For example, `02016102020161020000111`. |
| Sequence number | Provide a 25-character unique sequence number in format `YYYYMMDD-[16 alphanumeric]`. This value is auto-generated if not provided. |

## Output

| Output field | Description |
| --- | --- |
| Next flag | Indicates if more results are available (`0` = no more results, `1` = more results available). |
| Next keyword | Pagination keyword to retrieve the next page of results. |
| Number | Total number of transactions returned. |
| Transaction date from | Start date of the returned transaction range. |
| Transaction date to | End date of the returned transaction range. |
| Transaction ID first | First transaction ID in the result set. |
| Transaction ID last | Last transaction ID in the result set. |
| Operation date | Date when the inquiry was processed. |
| Operation time | Time when the inquiry was processed. |
| Account info | Account information object. |
| Branch number | Branch number of the account. |
| Branch name | Branch name of the account. |
| Account type code | The account type code. |
| Account type name | The account type name. |
| Account number | The account number. |
| Account name (Kanji) | The account holder name in Kanji. |
| Account name (Kana) | The account holder name in Katakana. |
| Transactions | Array of transaction records. |
| Transaction date | Date of the transaction. |
| Designated date | Designated processing date for the transaction. |
| Transaction ID | Unique identifier for the transaction. |
| Transaction type | The type of transaction. |
| Remarks | Transaction remarks or description. |
| Debit credit type code | The transaction direction. |
| Amount | The transaction amount. |
| Balance | Account balance after the transaction. |
