---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/search-expense-reports-batch.md
description: >-
  The Search expense reports batch action searches for expense reports in SAP
  Concur based on specified criteria.
---

# SAP Concur - Search expense reports action (batch)

The **Search expense reports** batch action searches for expense reports in SAP Concur based on specified criteria. This action retrieves 100 records maximum. When no search criteria is provided, reports owned by the current user are returned.

## Input

| Input field | Description |
| --- | --- |
| User | Specify the user to filter reports by report owner. If set to `ALL`, reports for all report owners are returned. Note: Works only if you are the admin. |
| Approval status | Select the approval status to filter reports. Options include: Not submitted, Submitted, Submission triggered an anomaly and fraud check, Pending reviews, Pending external validation, Pending Budget approval, Pending Cost object approval, Pending manager approval, Pending prepayment validation, Pending receipt images, Needs to be resubmitted, Approved, Expired in approval queue |
| Payment status | Select the payment status to filter reports. Options include: On hold, Not paid, Confirmed, In process to be paid, Paid |
| Currency code | Enter the three-letter ISO 4217 currency code for the report currency (for example, USD). |
| Payment type | Select the payment method for the report entries. Options include: Company Paid, Out-of-Pocket, Pending Card Transaction |
| Reimbursement method | Select how the report owner is reimbursed. Options include: ADP payroll, AP (Company Check), Expense pay, Other Payment Service |
| Approver login ID | Enter the login ID for the report approver that is the current approver assigned to the report. |
| Expense type | Select the expense type code to filter reports that contain at least one expense entry of the specified type. Options include: Airfare, Car Rental, Hotel, Hotel Tax, Train, Fuel |
| Attendee type | Select the attendee type to filter reports that contain expense entries with attendees of the specified type. Options include: Business Guest, Detailed Attendee Information, Employee (Not using Concur), Spouse, Associate |
| Country code | Enter the ISO 3166-1 alpha-2 country code (for example, US for United States). |
| Has VAT | Select whether to filter reports that have at least one expense entry with VAT details. |
| Has images | Select whether to filter reports with at least one expense entry with an entry image or a report image. |
| Has attendees | Select whether to filter reports with at least one expense entry with an attendee. |
| Has billable expenses | Select whether to filter reports with at least one billable expense entry. |
| Is test user | Select whether to filter reports whose owner is a test user using the report for testing purposes in a non-production environment. |
| Expense group configuration | Select the expense group configuration to filter reports. Options include: Global, US Group, AU Group, CA Group, DE Group, FR Group, GB Group, IE Group, SG Group |
| Entry transaction date before | Enter the date to filter reports with expense entry transactions before this date. |
| Entry transaction date after | Enter the date to filter reports with expense entry transactions after this date. |
| Created date before | Enter the date to filter reports created before this date. |
| Created date after | Enter the date to filter reports created after this date. |
| User defined date before | Enter the date to filter reports with user-defined dates before this date. |
| User defined date after | Enter the date to filter reports with user-defined dates after this date. |
| Submit date before | Enter the date to filter reports submitted before this date. |
| Submit date after | Enter the date to filter reports submitted after this date. |
| Processing payment date before | Enter the date to filter reports that completed approvals and were ready for payment extraction before this date. |
| Processing payment date after | Enter the date to filter reports that completed approvals and were ready for payment extraction after this date. |
| Paid date before | Enter the date to filter reports where all journal entries were integrated with the financial system before this date. |
| Paid date after | Enter the date to filter reports where all journal entries were integrated with the financial system after this date. |
| Modified date before | Enter the date to filter reports last modified before this date. |
| Modified date after | Enter the date to filter reports last modified after this date. |

## Output

| Output field | Description |
| --- | --- |
| Expense reports | List of expense reports matching the search criteria. |
| Report name (Expense reports) | The name of the expense report. |
| Report ID (Expense reports) | The unique identifier of the resource. |
| Report URI (Expense reports) | The URI to the resource. |
| Total (Expense reports) | The total amount of the report. |
| Currency code (Expense reports) | The three-letter ISO 4217 currency code for the expense report currency. |
| Country (Expense reports) | The report country. Format: ISO 3166-1 alpha-2. |
| Country subdivision (Expense reports) | The report country subdivision. Format: ISO 3166-2:2007 country subdivision. |
| Personal amount (Expense reports) | The total amount of expenses marked as personal. |
| Amount due employee (Expense reports) | The total amount due to the employee for the report. |
| Amount due company card (Expense reports) | The total amount due to the company card for the report. |
| Total claimed amount (Expense reports) | The total amount of all non-personal expenses in the report. |
| Total approved amount (Expense reports) | The total amount of approved expenses in the report. |
| Receipts received (Expense reports) | Indicates whether the receipts have been received. If true, this entry has been marked as confirmed by the Expense Processor. |
| Ever sent back (Expense reports) | Indicates whether the report has ever been sent back to the employee. |
| Has exception (Expense reports) | Indicates whether the report has exceptions. |
| Last comment (Expense reports) | The text of the most recent comment on the report. |
| Owner login ID (Expense reports) | The Login ID of the user this report belongs to. |
| Owner name (Expense reports) | The name of the expense report owner. |
| Approver login ID (Expense reports) | The Login ID of the report owner's expense approver. |
| Approval status name (Expense reports) | The report's approval status, in the OAuth consumer's language. |
| Approval status code (Expense reports) | The approval status code for the report. |
| Payment status name (Expense reports) | The report's payment status, in the OAuth consumer's language. |
| Payment status code (Expense reports) | The payment status code for the report. |
| Ledger name (Expense reports) | The name of the expense report ledger. |
| Policy ID (Expense reports) | The unique identifier of the policy that applies to this report. |
| Workflow action URL (Expense reports) | The URL to post a workflow action to the report. |
| Create date (Expense reports) | The date the report was created. |
| Submit date (Expense reports) | The date the report was submitted. |
| Processing payment date (Expense reports) | The date that the report completed approvals and was ready for payment extraction. |
| Paid date (Expense reports) | The date when all journal entries were integrated with the financial system. |
| User defined date (Expense reports) | The report date assigned by the user. |
| Last modified date (Expense reports) | The date the report was last modified. |
