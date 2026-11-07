---
url: 'https://docs.workato.com/en/connectors/sap/action-run-rfm.md'
description: >-
  The Call remote function module action in the SAP connector lets you discover
  and run a Remote Function Module through a Remote Function Call.
---

# SAP - Call remote function module action

Use this action to discover and run a Remote Function Module (RFM) through a Remote Function Call (RFC) in a SAP system.

Optionally, pair this with our **Begin transaction** and **End transaction** actions to run multiple RFMs in a single logical unit of work. This allows you to commit (or roll back) the entire sequence at the end of the transaction.

> **ARE YOU WORKING WITH BAPIS?**
> 
> Use the [Call BAPI action](/en/connectors/sap/action-call-bapi) instead.

## Input

| Field name | Description |
| --- | --- |
| RFM Description | _Optional_. Give this step a human-readable description which will show up in the recipe step. This input does not affect the RFC execution. |
| RFM name | Select the RFM you plan to run. This picklist contains all of the RFMs in your SAP system. If your SAP system has a large number of RFMs, it may take you up to 15 seconds to load and search this picklist. Searching may be faster if you copy and paste the RFM name into this field, instead of typing the name. After you select a RFM, you can find all of its data fields in the **Add/remove optional fields** section. |
| Transaction ID | _Optional_. Map the Transaction ID datapill from the **Begin transaction** action to execute this RFC in a transaction. |
| Auto commit | _Optional and disabled if Transaction ID is mapped_. Some RFMs do not commit the changes by default. - Select **Yes** if you plan to force the RFM to commit using the RFC `BAPI_TRANSACTION_COMMIT`. If the RFM fails, the RFC `BAPI_TRANSACTION_ROLLBACK` is invoked. - Select **No** if you plan to let the RFM commit on its own. If `BAPI_TRANSACTION_COMMIT` is not called within the RFM code, data is not committed to the database. |

## Output

| Field name | Description |
| --- | --- |
| RFM name | Name of the selected RFM. |
| Status | Status after RFM runs in SAP. It can be a success or failure status. |
| Error message | The error message if an error occurs. |
| Response data | Contains the response data fields from SAP after the RFM runs. |

## Calling remote function modules in a transaction

Calling RFMs in a sequence enables you to securely commit a series of updates to your SAP system at the same time. This allows you to ensure data consistency as well as easily execute a rollback if anything goes wrong.

![tRFC overview](/assets/trfc-overview.CdSTxyiM.png)

[View the sample recipe here.](https://app.workato.com/recipes/17760787?st=b766a10533c029d14d829a95ab64c7ccb853a7ee247ee470bf8e5a17c35238d1)

## How to execute RFMs in a transaction

1. Add a **Begin transaction** action where you plan your sequence of RFMs to start.
   
2. Add any number of RFMs using the **Call remote function module** action. Map the output datapill Transaction ID from the **Begin transaction** action to the **Transaction ID** input field in each **Call remote function module** action. Configure other fields as needed.
   
3. At the end of your desired sequence of RFM calls, add an **End transaction** action. Map the output datapill Transaction ID from the **Begin transaction** action to the **Transaction ID** input field and select **Commit work** to save this entire sequence to your SAP application when the job execution reaches this step.
   
4. Wrap the **Call remote function module** actions in a **Monitor for errors** block. This allows you to add an **End transaction** action with **Rollback changes** selected. This allows you to roll back the transaction if any of the steps face errors when you run your recipe.

---
