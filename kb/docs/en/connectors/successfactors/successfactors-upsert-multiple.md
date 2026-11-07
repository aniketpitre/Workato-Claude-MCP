---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-upsert-multiple.md
description: >-
  The Upsert records (multiple objects) batch action performs simultaneous
  operations on multiple SuccessFactors objects with transactional behavior.
---

# SAP SuccessFactors - Upsert records (multiple objects) batch action

The **Upsert records (multiple objects)** batch action performs simultaneous operations on one or more SuccessFactors objects. It follows transactional behavior. The entire batch fails when one operation fails. This action only supports OData V2.

> **UPSERT ACTION RESPONSE BEHAVIOR**
> 
> The **Upsert record (multiple objects)** batch action returns a `200 OK` response from SAP SuccessFactors even when individual record updates fail. This behavior is expected because the SuccessFactors API includes each record's result in the response body instead of the HTTP status code.
> 
> Check the `Http code` value in the action output to verify if each record succeeded. You can use an **If** condition in your recipe to detect `Http code` values other than `200` and handle those records as needed.
> 
> The job completes successfully because the API returns `200 OK` when it processes the request, even if some records fail internally.

## Input

| Input field | Description |
| --- | --- |
| Objects | Select one or more SuccessFactors objects. Because objects can have similar names, the list includes their internal names. For example, `User`. |
| Object attributes | For each selected object, define the required key fields, such as `ID` or `Key`. The action updates existing records if the keys exist or creates new records otherwise. |

> **ADDITIONAL ATTRIBUTES**
> 
> Depending on the object and your SuccessFactors configuration, additional fields appear where you define more attributes for the record. You can also select optional attributes to update. A common attribute is a navigation field that links this record to another record through a URI, such as a user to their manager. Refer to [Using navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information.

## Output

| Output field | Description |
| --- | --- |
| Batch ID | Unique identifier for the batch operation. |
| Objects | Contains object-level results for each record included in the batch. |
