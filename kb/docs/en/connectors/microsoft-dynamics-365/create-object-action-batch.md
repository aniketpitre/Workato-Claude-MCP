---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/create-object-action-batch.md
description: >-
  The Create object batch action in the Microsoft Dynamics 365 connector lets
  you create multiple records for a specified object in a single batch.
---

# Microsoft Dynamics 365 - Create object batch action

This action creates multiple records for a specified object in Microsoft Dynamics 365 in a single batch.

> **BATCH FAILURE BEHAVIOR**
> 
> Microsoft Dynamics 365 fails the entire batch if any record creation encounters an error when the **Allow partial batch create** field is set to **No**. None of the records create, even if some are valid.
> 
> Set the **Allow partial batch create** field to **Yes** to create all valid records and skip those that fail. Dynamics 365 then returns mixed results that show which records succeed and which fail.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to create in batches. For example, `Lead`. |
| Allow partial batch create | Select **Yes** to allow successful records to be created even if some records fail (commonly due to invalid field input). You can receive a mixed result, in which some operations may succeed while others fail. This allows for more flexibility in handling requests, but it also requires that you manage potential inconsistencies. Select **No** to roll back the entire batch if any record creation fails. This ensures that either all operations succeed or none do. If one creation fails, none of the records in the batch are created. Defaults to **No**. |
| Object Fields | Specify fields for the new object that you plan to create. |

## Output

The output datatree contains the IDs of the newly created objects.

| Field | Description |
| --- | --- |
| Batch IDs | A list of IDs for the successfully created objects. |
