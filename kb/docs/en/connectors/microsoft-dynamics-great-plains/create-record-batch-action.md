---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains/create-record-batch-action.md
description: >-
  The Create records in batches action creates records in Microsoft Dynamics GP
  in batches.
---

# Microsoft Dynamics Great Plains - Create records in batches action

The **Create records in batches** action creates records in Microsoft Dynamics GP in batches. This action requires a list of records as an input. For example, the following are the input and output schemas if you select **Cash receipt** as the object:

## Input

| Input field | Description |
| --- | --- |
| DB connection string | Enter the database connection string to use for the action. |
| Customer number | Enter the unique identifier of the customer making the payment. |
| Document number | Provide the unique reference number for the cash receipt transaction. |
| Document date | Select the creation date for the cash receipt document. |
| Transaction amount | Enter the total amount received from the customer. |
| GL posting date | Enter the date to post the transaction to the general ledger. |
| Batch number | Specify the batch number to assign this cash receipt to. |
| Cash receipt type | Select the type of receipt, such as cash, check, or credit card. |
| Checkbook ID | Enter the ID of the checkbook to deposit the receipt in. |
| Check number or credit card number | Provide the check number or credit card number used for the payment. |
| Credit card ID | Enter the identifier for the credit card, if applicable. |
| Transaction description | Add a brief description or note about the cash receipt transaction. |
| Last user to edit | Specify the username of the last person who modified this transaction. |
| Checkbook ID for the batch | Provide a checkbook ID to associate with the batch, if different from the transaction's `Checkbook ID`. |
| Currency ID | Select the currency used for this transaction. |
| Exchange rate | Enter the applicable exchange rate if using a foreign currency. |
| Rate type ID | Specify the rate type ID used to calculate the exchange rate. |
| Expiration date | Provide the expiration date for the exchange rate. |
| Exchange ID description | Add a description for the exchange rate ID, if applicable. |
| Exchange rate source | Specify the source of the exchange rate. |
| Rate expiration | Enter the date or time to no longer use the exchange rate. |
| Days to increment | Set the number of days to increment for calculating due or expiration dates. |
| Rate variance | Define the allowable variation in exchange rate for the transaction. |
| Transaction date | Enter the actual date when the transaction occurred. |
| Rate calculation method | Select the method for exchange rate calculation. |
| Previous day’s quotas | Specify the acceptable range or quotas for the previous day’s exchange rate. |
| Date limits | Set constraints on the transaction date, if required. |
| Time 1 | Provide a timestamp or time reference for posting or workflow purposes. |
| Flag to autocreate distributions | Select whether to automatically generate distribution entries for the transaction. |
| Requester transactions | Select whether to populate the requester shadow table. |
| User-defined fields 1–5 | Use these fields to capture any additional custom information needed for your use case. |

## Output

| Output field | Description |
| --- | --- |
| Create entity result | The status of the **Create records in batches** action. |
