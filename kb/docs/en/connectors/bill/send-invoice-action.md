---
url: 'https://docs.workato.com/en/connectors/bill/send-invoice-action.md'
description: The Send invoice action emails an invoice to a customer in BILL."
---

# BILL - Send invoice action

The **Send invoice** action emails an invoice to a customer in BILL.

## Input

| Input field | Description |
| --- | --- |
| Invoice ID | Provide the BILL-generated ID of the invoice to send. |
| Headers | Expand this section to configure header information. |
| From (headers) | Provide the ID of the user sending the invoice. |
| To (headers) | Provide a comma-separated list of recipient email addresses. |
| Cc me (headers) | Specify whether to send yourself a copy of the customer invoice. |
| Subject (headers) | Provide the subject line for the email. Leave this field blank to use the default BILL email template. |
| Content | Expand this section to configure the email content. |
| Body (content) | Enter the email body as a single string. Use `\n\n` for line breaks. Leave this field blank to use the default BILL email template. |

## Output

| Output field | Description |
| --- | --- |
| Response status | The status of the send request. `0` indicates a successful response, while `1` indicates an error response. |
| Response message | A message about the result. Possible values include `Success` or `Error`. |
| Response data | An object that contains additional response data. |
| Error code (response data) | A code that indicates the type of error, if any. |
| Error message (response data) | A description of the error, if applicable. |

---
