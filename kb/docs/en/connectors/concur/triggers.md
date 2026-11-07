---
url: 'https://docs.workato.com/en/connectors/concur/triggers.md'
description: >-
  Browse the triggers available in the SAP Concur connector for Workato to start
  recipes from expense report and related events.
---

# SAP Concur - Triggers

The SAP Concur connector supports the following triggers.

- [New expense report submission trigger](/en/connectors/concur/triggers/new-expense-report-submission)
- [New expense report trigger](/en/connectors/concur/triggers/new-expense-report)
- [New/updated expense report trigger](/en/connectors/concur/triggers/new-updated-expense-report)
- [New/updated invoice trigger](/en/connectors/concur/triggers/new-updated-invoice)
- [New/updated user trigger](/en/connectors/concur/triggers/new-updated-user)

---

---
url: >-
  https://docs.workato.com/en/connectors/concur/triggers/new-expense-report-submission.md
description: >-
  The New expense report submission trigger activates when an expense report is
  first submitted or re-submitted in SAP Concur.
---

# SAP Concur - New expense report submission trigger

The **New expense report submission** trigger activates when an expense report is first submitted or re-submitted in SAP Concur.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Specify when the recipe should start picking up expense reports. When you start the recipe for the first time, it picks up expense reports submitted after the specified date and time. Leave this field empty to get reports from one hour ago. You can't change this value after running or testing the recipe. |
| Trigger poll interval | Select how frequently to check for new events. |
| Approval status | Select the approval status to filter expense reports. If selected, only expense reports with this approval status are processed. Options include: Not submitted, Submitted, Submission triggered an anomaly and fraud check, Pending reviews, Pending external validation, Pending Budget approval, Pending Cost object approval, Pending manager approval, Pending prepayment validation, Pending receipt images, Needs to be resubmitted, Approved, Expired in approval queue |
| Payment status | Select the payment status to filter expense reports. If selected, only expense reports with this payment status are processed. Options include: On hold, Not paid, Confirmed, In process to be paid, Paid |

## Output

| Output field | Description |
| --- | --- |
| Report name | The name of the expense report. |
| Report ID | The unique identifier of the resource. |
| Report URI | The URI to the resource. |
| Total | The total amount of the report. |
| Currency code | The three-letter ISO 4217 currency code for the expense report currency. |
| Country | The report country. Format: ISO 3166-1 alpha-2. |
| Country subdivision | The report country subdivision. Format: ISO 3166-2:2007 country subdivision. |
| Personal amount | The total amount of expenses marked as personal. |
| Amount due employee | The total amount due to the employee for the report. |
| Amount due company card | The total amount due to the company card for the report. |
| Total claimed amount | The total amount of all non-personal expenses in the report. |
| Total approved amount | The total amount of approved expenses in the report. |
| Receipts received | Indicates whether the receipts have been received. If true, this entry has been marked as confirmed by the Expense Processor. |
| Ever sent back | Indicates whether the report has ever been sent back to the employee. |
| Has exception | Indicates whether the report has exceptions. |
| Last comment | The text of the most recent comment on the report. |
| Owner login ID | The Login ID of the user this report belongs to. |
| Owner name | The name of the expense report owner. |
| Approver login ID | The Login ID of the report owner's expense approver. |
| Approval status name | The report's approval status, in the OAuth consumer's language. |
| Approval status code | The approval status code for the report. |
| Payment status name | The report's payment status, in the OAuth consumer's language. |
| Payment status code | The payment status code for the report. |
| Ledger name | The name of the expense report ledger. |
| Policy ID | The unique identifier of the policy that applies to this report. |
| Workflow action URL | The URL to post a workflow action to the report. |
| Create date | The date the report was created. |
| Submit date | The date the report was submitted. |
| Processing payment date | The date that the report completed approvals and was ready for payment extraction. |
| Paid date | The date when all journal entries were integrated with the financial system. |
| User defined date | The report date assigned by the user. |
| Last modified date | The date the report was last modified. |

---
