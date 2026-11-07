---
url: 'https://docs.workato.com/en/connectors/mufg.md'
description: >-
  The MUFG connector enables you to automate banking operations including
  account transaction inquiries, incoming transfer tracking, and money transfer
  requests through the MUFG corporate banking API.
---

# MUFG

[Mitsubishi UFJ Financial Group (MUFG)](https://www.bk.mufg.jp) is one of Japan's largest financial institutions, providing comprehensive banking and financial services.

The MUFG connector enables you to automate banking operations including account transaction inquiries, incoming transfer tracking, and money transfer requests through the MUFG corporate banking API.

## Prerequisites

You must have the following to establish an MUFG connection in Workato:

- An active MUFG corporate banking account with API access enabled.
- A registered application in the MUFG Developer Portal.
- A client ID. This can be either your application key or secret key.

### Register your application

Complete the following steps to register your application in the MUFG Developer Portal:

1. Sign in to the [MUFG Developer Portal](https://developer.portal.bk.mufg.jp/btmu/openapitrial/user/login).
   
2. Click **Apps**, then click **Create new app**.
   
3. Enter the name of your application in the **Title** field. Maximum is 255 characters.
   
   ![Create a new application](/assets/create-app.S3u8CIjS.png)_Create a new application_
   
4. Optional. Enter a description of the application in the **Description** field. Maximum is 65535 characters.
   
5. Enter `https://www.workato.com/oauth/callback` in the **Application OAuth Redirect URL(s)** field.
   
6. Click **Save** to register your application and obtain your application key and secret key.
   
7. Store the application key or secret key securely. You can use either value as your client ID when connecting to MUFG in Workato.
   
   ![Copy the application key or secret key](/assets/api-key-and-secret.BQIrQPDP.png)_Copy the application key or secret key_
   

## How to connect to MUFG

Complete the following steps to establish an MUFG connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `MUFG` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to MUFG](/assets/connect.BTpGu3ZX.png)_Connect to MUFG_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Enter your application key or secret key from the MUFG Developer Portal in the **Client ID** field.
   
6. Click **Connect**.

---

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

---

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

---
