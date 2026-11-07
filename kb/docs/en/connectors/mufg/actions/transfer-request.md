---
url: 'https://docs.workato.com/en/connectors/mufg/actions/transfer-request.md'
description: >-
  The Transfer request action submits a money transfer request from your MUFG
  account to another account.
---

# MUFG - Transfer request action

The **Transfer request** action submits a money transfer request from your MUFG account to another account.

## Input

| Input field | Description |
| --- | --- |
| Debit account information | Configure debit account details for the transfer. |
| Debit account branch number | Enter the 3-digit branch number of the debit account. For example, `001`. |
| Debit account type | Select the type of debit account. Options include **Ordinary**, **Checking**, **Notification**, and **Time Deposit**. |
| Debit account number | Enter the 7-digit account number for the debit account. For example, `1111111`. |
| Payment date | Select the date when the transfer should be executed. |
| Beneficiary account information | Configure the beneficiary account details for the transfer. |
| Beneficiary financial institution number | Enter the 4-digit code identifying the beneficiary's bank. For example, `0005`. |
| Beneficiary account branch number | Enter the 3-digit branch number of the beneficiary's bank. For example, `123`. |
| Beneficiary account type | Select the type of beneficiary account. Options include **Ordinary**, **Checking**, **Savings**, **Notification**, **Time Deposit**, and **Other** |
| Beneficiary account number | Enter the account number for the beneficiary. For example, `1234567`. |
| Beneficiary account name in Kanji | Enter the beneficiary's account name in Kanji. Maximum 25 characters. |
| Beneficiary account name in Kana | Enter the beneficiary's account name in Kana. Maximum 48 characters. |
| Entered amount | Enter the transfer amount. For example, `0-9999999999`. |
| Charges paid by | Select who pays the transfer fees. Options include **Sender** and **Beneficiary**. |
| Applicant name | Enter the name of the person requesting the transfer. Maximum 48 characters. |
| Beneficiary code 1 | Enter the first identifier code for the beneficiary. Maximum 10 characters. |
| Beneficiary code 2 | Enter the second identifier code for the beneficiary. Maximum 10 characters. |
| Notes | Enter optional memo or notes for this transfer. Maximum 32 characters. |
| Payment applicant number | Enter the applicant's reference number for transfer identification. Maximum 10 digits. You can't use this field with **EDI information**. |
| EDI information | Enter Electronic Data Interchange information for transfer identification. Maximum 20 characters. You can't use this field with **Payment applicant number**. |
| Sequence number | Provide a 25-character unique sequence number in format `YYYYMMDD-[16 alphanumeric]`. This value is auto-generated if not provided. |

## Output

| Output field | Description |
| --- | --- |
| Debit account info | Details of the account debited for the transfer. |
| Debit account branch number | Branch number of the debit account. |
| Debit account branch name | The debit account branch name. |
| Debit account type code | The debit account type code. |
| Debit account type name | The debit account type name. |
| Debit account number | The debit account number. |
| Debit account name (Kanji) | The debit account holder name in Kanji. |
| Debit account name (Kana) | The debit account holder name in Katakana. |
| Applicant name | Name of the transfer applicant. |
| Payment date | Scheduled date for the transfer execution. |
| Beneficiary code 1 | First beneficiary identifier code. |
| Beneficiary code 2 | Second beneficiary identifier code. |
| Beneficiary info | Details of the beneficiary account. |
| Beneficiary account financial institution no | Financial institution number of the beneficiary. |
| Beneficiary account financial institution name | Financial institution name. |
| Beneficiary account branch number | Branch number of the beneficiary account. |
| Beneficiary account branch name | The beneficiary account branch name. |
| Beneficiary account type code | The beneficiary account type code. |
| Beneficiary account type name | The beneficiary account type name. |
| Beneficiary account number | The beneficiary account number. |
| Beneficiary account name (Kanji) | The beneficiary name in Kanji. |
| Beneficiary account name (Kana) | The beneficiary name in Katakana. |
| Notes | Transfer memo or notes. |
| Entered amount | Original transfer amount requested. |
| Payment amount | Actual amount to be transferred. |
| Payment charge | Transfer fee amount. |
| Charges paid by | Fee payment arrangement. |
| Charge to beneficiary | Fee amount charged to beneficiary if applicable. |
| Payment applicant no | Reference number for the transfer. |
| EDI info | EDI information included with the transfer. |
| Transfer ID | Unique identifier assigned to this transfer request. |
| Status | Current status of the transfer. |

---
