---
url: >-
  https://docs.workato.com/en/connectors/freshbooks/new-updated-record-trigger.md
description: >-
  The New/updated record trigger runs the recipe when there is a new or updated
  record in FreshBooks.
---

# FreshBooks - New/updated record trigger

The **New/updated record** trigger runs the recipe when there is a new or updated record in FreshBooks.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object to monitor from the drop-down menu. Fields load dynamically based on the object you select. |
| Account ID | Select the FreshBooks account ID to trigger the record. |
| Trigger poll interval | Select the frequently to check for new events from the drop-down menu. The minimum value allowed is 5 minutes. [Learn more](/en/recipes/polling-intervals). |
| When first started, this recipe should pick up events from | When you first start a recipe, it picks up events from this specified date and time. It processes new or updated records from 1 hour ago if left blank. Once a recipe has been run or tested, the value cannot be changed. |
| Set trigger condition | Defines further guidelines added to a specific trigger that filter what type of trigger events should be selected for processing. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, if you select the **Payment** object, the output schema is as follows:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the payment. |
| Invoice ID | ID of the associated invoice. |
| Amount | Payment amount with amount and currency code. |
| Date | Date when the payment was made. |
| Type | Method of payment (Check, Credit, Cash). |
| Notes | Additional notes about the payment. |
| Gateway | Payment processor used. |
| From credit | Whether payment is from client credit. |
| Accounting System ID | Accounting system identifier. |
| Bulk Payment ID | Associated bulk payment ID. |
| Client ID | Associated client ID. |
| Credit ID | Associated credit ID. |
| Log ID | Payment log ID. |
| Note | Payment note. |
| Order ID | Associated order ID. |
| Overpayment ID | Associated overpayment ID. |
| Send client notification | Whether to send a notification to the client. |
| Transaction ID | Associated transaction ID. |
| Updated | Last update timestamp. |
| Visibility state | Visibility state of the payment. |
