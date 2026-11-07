---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-upsert-single.md
description: >-
  The Upsert records (single object) batch action searches for multiple records
  by a specified field and updates or creates them in bulk.
---

# SAP SuccessFactors - Upsert records (single object) batch action

The **Upsert records (single object)** batch action searches for records in SAP SuccessFactors by a specified field (primary key). The action updates it with the provided data if a record exists. Otherwise, it creates the record with the provided data.

This action processes up to 200 records each time the recipe runs and only supports OData V2.

> **UPSERT ACTION RESPONSE BEHAVIOR**
> 
> The **Upsert records (single object)** batch action returns a `200 OK` response from SAP SuccessFactors even when individual record updates fail. This behavior is expected because the SuccessFactors API includes each record's result in the response body instead of the HTTP status code.
> 
> Check the `Http code` value in the action output to verify if each record succeeded. You can use an **If** condition in your recipe to detect `Http code` values other than `200` and handle those records as needed.
> 
> The job completes successfully because the API returns `200 OK` when it processes the request, even if some records fail internally.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names. |
| Object source list | Insert a list datapill. See [List input datapills](/en/features/list-management#list-batch-action). |

> **ADDITIONAL ATTRIBUTES**
> 
> Depending on the object and your SuccessFactors configuration, additional fields appear where you define more attributes for each record. You can also select optional attributes to update. A common attribute is a navigation field that links this record to another record through a URI, such as a user to their manager. Refer to [Using navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information.

## Output

The output fields vary depending on the object you select. Review the output datatree in your recipe to view available datapills.

> **DATETIME FIELDS**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).
