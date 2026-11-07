---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains/apply-document-to-invoice-action.md
description: >-
  The Apply document to invoice action applies a credit memo, return or cash
  receipt to an invoice, debit memo, finance charge, service/repair or warranty
  in Microsoft Dynamics GP.
---

# Microsoft Dynamics Great Plains - Apply document to invoice action

The **Apply document to invoice** action applies a credit memo, return or cash receipt to an invoice, debit memo, finance charge, service/repair or warranty in Microsoft Dynamics GP.

## Input

| Input field | Description |
| --- | --- |
| Apply from - document type | Select the source document type you plan to apply to the target document. |
| Apply to - document type | Select the target document type you plan to apply the source document to. |
| Apply to - document number | Provide the target document number you plan to apply the source document to. |
| Apply from - document number | Provide the source document number you plan to apply to the target document. |
| Amount to apply | Enter an amount for the invoice. |
| DB connection string | Enter the database connection string to use for the action. |
| Discount taken | Specify the discount taken, if applicable. |
| Write-off amount | Specify the write-off amount, if applicable. |
| Apply date | Select the apply date from the calendar. |
| Apply posting date | Select the posting date from the calendar. |

## Output

| Output field | Description |
| --- | --- |
| Create entity result | The status of the apply action. |
