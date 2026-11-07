---
url: 'https://docs.workato.com/en/connectors/sap/action-call-bapi.md'
description: >-
  The Call BAPI action in the SAP connector lets you run BAPIs in an SAP system
  and automatically raises structured BAPI errors and validation issues.
---

# SAP - Call BAPI action

Use this action to run BAPIs (Business Application Programming Interfaces) in an SAP system.

> **LIST OF BAPIs**
> 
> Beginning with OPA version 24.1, we offer a catalog of BAPIs organized by Business Objects. This makes it easy to navigate and select the appropriate BAPI by browsing through the relevant Business Objects. You must enter the BAPI names manually when creating a recipe using the call BAPI action if you are using an older version.
> 
> ![call bapi action](/assets/call-bapi-dropdown.CG-txonk.png)_Call BAPI action_
> 
> ![business process drop-down](/assets/call-bapi-bp-dropdown.DGzfFrUV.png)_Business Objects catalog_
> 
> ![bapi name drop-down](/assets/call-bapi-bn-dropdown.CeIKPnz0.png)_BAPI catalog_

Previously, you could invoke BAPIs using our [Call remote function module action](/en/connectors/sap/action-run-rfm). However, this approach is limited when calling BAPIs: Even when a BAPI operation in the SAP system failed, Workato considered the action successful because the call itself succeeded. This meant that you had to include conditional logic ("if" steps) in your recipes to identify errors based on the response from SAP.

Conversely, the **Call BAPI** action leverages the standardized error message structure present in BAPIs to raise errors when a BAPI execution encounters issues automatically. It also highlights the [validation errors](#validation-errors) detected by the SAP system and returns them to Workato. This eliminates the need to build recipe steps to check the SAP system for errors, streamlining recipe logic.

![Call BAPI/RFM action comparison](/assets/action-bapi-rfm-comparison.CzF_EnpX.png)_The Call BAPI action (right) reduces recipe steps and streamlines logic_

Use this action with our existing **Begin transaction** and **End transaction** actions to run multiple RFMs in a single logical unit of work. This allows you to commit (or roll back) the entire sequence at the end of the transaction.

> **REMOTE FUNCTION CALLS FOR BAPIS AND RFMS**
> 
> Remote function calls enable you to run both BAPIs and RFMs (Remote-Enabled Function Modules) within a SAP system. BAPIs are distinct from RFMs in the following ways:
> 
> - BAPIs are standardized interfaces to SAP business objects, while RFMs are less standardized and can be multi-step processes.
>   
> - In BAPIs, error messages or warnings are presented in a structured and clear manner within the response, unlike RFMs.
>   
> - BAPIs generally don't perform immediate commits to an SAP system. This allows you to make a series of actions within a single transaction. You can commit these changes to the SAP system collectively or roll them back if errors occur.
>   

See [How to run BAPIs in a transaction](#bapi-run) for the example flow.

## Input

- BAPI description
  
- Give this step a human-readable description, which will show up in the recipe step. This input does not affect the BAPI execution. For example, **Create sales order**.
  
- BAPI name
  
- Provide the exact name of the BAPI you plan to use. This input is case-sensitive.
  
- Transaction ID
  
- Provide the transaction ID from the output of the **Begin transaction** action. If this is mapped, **Force auto commit** is disabled.
  
- Force auto-commit
  
- Some BAPIs do not commit the changes by default. Select **Yes** if you plan to force the RFM to commit using the RFC `BAPI_TRANSACTION_COMMIT`. If the RFM fails, the RFC `BAPI_TRANSACTION_ROLLBACK` is invoked. Select **No** if you plan to let the RFM commit on its own. If `BAPI_TRANSACTION_COMMIT` is not called within the RFM code, data is not committed to the database.
  
- Timeout
  
- Configure the timeout for this call to up to 30 minutes. If you select 30 minutes, you cannot run this RFC in a transaction.
  

## Validation errors

If the following return types are included in the response, Workato raises an error:

| Return type | Description |
| --- | --- |
| A | Termination message (abort) |
| E | Error message |

> **ERROR BEHAVIOR**
> 
> The Call BAPI action applies BAPI-specific validation and may raise errors automatically for certain return types. Other technical and business errors may still surface differently at runtime. Refer to [Error behavior in the SAP RFC connector](/en/connectors/sap/sap-error-behavior) for details on how technical errors, schema mismatches, and business errors surface during recipe execution.

## How to run BAPIs in a transaction

Some BAPIs may need you to execute a `BAPI_TRANSACTION_COMMIT` to commit the work into your SAP application. You can do so using the **Force auto commit** input or by running the BAPI in a transaction.

1. Add a **Begin transaction** action where you plan your sequence of BAPIs to start.
   
2. Add one or more BAPIs using the **Call BAPI** action. Map the output datapill Transaction ID from the **Begin transaction** action to the **Transaction ID** field. Configure other fields as necessary.
   
3. Add an **End transaction** action at the end of your desired sequence of BAPI calls. Map the output datapill Transaction ID from the **Begin transaction** action to the **Transaction ID** input field and select **Commit work** to save this entire sequence to your SAP application when the job execution reaches this step.
   
4. Wrap the **Call BAPI** action in a **Monitor for errors** block. This allows you to add an **End transaction** action with **Roll back changes** selected, enabling you to roll back the transaction if any of the steps face errors when you run your recipe.

---
