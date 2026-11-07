---
url: 'https://docs.workato.com/en/connectors/airwallex/new-record-trigger.md'
description: >-
  The New record trigger runs the recipe when a new record is detected in
  Airwallex
---

# Airwallex - New record trigger

The **New record** trigger runs the recipe when a new record is detected in Airwallex.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the record type. Output fields load dynamically based on the selected object. |
| Trigger poll interval | Select the frequency to check for new events from the drop-down menu. The minimum value allowed is 5 minutes. [Learn more](https://docs.workato.com/en/recipes/polling-intervals.html). |
| When first started, this recipe should pick up events from | The recipe picks up events from this specified date and time when you start it for the first time. The recipe processes new or updated records from `1` hour ago if left blank. You can't change this value after a recipe has been run or tested. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. Refer to the example output fields for the **Direct debit** object:

| Output field | Description |
| --- | --- |
| Amount | Amount of the transaction. |
| Created at | Date and time when the transaction was created. |
| Currency | Currency in which the transaction was processed. |
| Debtor name | Name of the debtor associated with the transaction. |
| Global account ID | Unique global identifier of the account. |
| Mandate ID | Identifier of the mandate related to the transaction. |
| Statement reference | Reference text appearing on the account statement. |
| Status | Current status of the transaction. |
| Transaction ID | Unique identifier of the transaction. |

---
