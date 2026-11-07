---
url: >-
  https://docs.workato.com/en/connectors/mufg/actions/incoming-transfer-inquiry.md
description: >-
  The Incoming transfer inquiry action retrieves incoming transfer details for a
  specified MUFG account, showing transfers received from other accounts with
  detailed sender information.
---

# MUFG - Incoming transfer inquiry action

The **Incoming transfer inquiry** action retrieves incoming transfer details for a specified MUFG account, showing transfers received from other accounts with detailed sender information.

## Input

| Input field | Description |
| --- | --- |
| Account ID | Enter the account identifier consisting of Branch (3 digits) + Account Type (1 digit) + Account Number (7 digits). For example, `00111234567`. |
| Inquiry date from | Select the start date for the transfer inquiry. Defaults to today if not specified. |
| Inquiry date to | Select the end date for the transfer inquiry. Defaults to today if not specified. |
| Next page keyword | Enter the next keyword value from a previous response to retrieve additional pages of results. For example, `02016102020161020000111`. |
| Sequence number | Provide a 25-character unique sequence number in format `YYYYMMDD-[16 alphanumeric]`. This value is auto-generated if not provided. |

## Output

| Output field | Description |
| --- | --- |
| Next flag | Indicates if more results are available (`0` = no more results, `1` = more results available). |
| Next keyword | Pagination keyword to retrieve the next page of results. |
| Number | Total number of incoming transfers returned. |
| Transaction date from | Start date of the returned transfer range. |
| Transaction date to | End date of the returned transfer range. |
| Transaction ID first | First transaction ID in the result set. |
| Transaction ID last | Last transaction ID in the result set. |
| Operation date | Date when the inquiry was processed. |
| Operation time | Time when the inquiry was processed. |
| Account info | Account information object. |
| Branch number | The branch number of the account. |
| Branch name | The branch name. |
| Account type code | The account type code. |
| Account type name | The account type name. |
| Account number | The account number. |
| Account name (Kanji) | The account holder name in Kanji. |
| Account name (Kana) | The account holder name in Katakana. |
| Payment arrivals | Array of incoming transfer records. |
| Transaction date | Date of the incoming transfer. |
| Designated date | Designated processing date for the transfer. |
| Transaction ID | Unique identifier for the transfer. |
| Transaction type | Type of transfer. |
| Applicant name | Name of the transfer sender. |
| Payment financial institution name Kana | Sending bank name in Katakana. |
| Branch name (Kana) | Sending bank branch name in Katakana. |
| Payment applicant no | Sender's reference number for the transfer. |
| EDI info | Electronic Data Interchange information included with the transfer. |
| Debit credit type code | The transaction direction. |
| Amount | The transfer amount. |
