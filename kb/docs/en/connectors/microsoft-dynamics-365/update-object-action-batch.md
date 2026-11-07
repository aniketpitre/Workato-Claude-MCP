---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/update-object-action-batch.md
description: >-
  The Update object batch action in the Microsoft Dynamics 365 connector lets
  you update multiple records for a specified object in a single batch.
---

# Microsoft Dynamics 365 - Update object batch action

This action updates multiple records for a specified object in Microsoft Dynamics 365 in a single batch.

> **BATCH FAILURE BEHAVIOR**
> 
> Microsoft Dynamics 365 fails the entire batch if any record update encounters an error when the **Allow partial batch create field** is set to **No**. None of the records update, even if some are valid.
> 
> Set the **Allow partial batch create field** to **Yes** to update all valid records and skip those that fail. Dynamics 365 then returns mixed results that show which records succeed and which fail.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| Objects | List of objects to update. |
| Allow partial batch create | Select **Yes** to allow successful records to be updated even if some records fail (commonly due to invalid field input). You can receive a mixed result, in which some operations may succeed while others fail. This allows for more flexibility in handling requests, but it also requires that you manage potential inconsistencies. Select **No** to roll back the entire batch if any record update attempt fails. This ensures that either all operations succeed or none do. If one update attempt fails, none of the records are updated. Defaults to **No**. |
| ID | Dynamics ID of the records to update. |

## Output

The output datatree contains the IDs of the updated objects.

| Field | Description |
| --- | --- |
| Batch IDs | A list of IDs for the successfully updated objects. |
