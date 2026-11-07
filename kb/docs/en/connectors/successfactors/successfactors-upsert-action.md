---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-upsert-action.md
description: >-
  The Upsert record action in the SAP SuccessFactors connector finds a record by
  object ID, then updates it or creates a new record if none exists.
---

# SAP SuccessFactors - Upsert record action

The **Upsert record** action searches for a record by the object ID. If a record exists, the action updates it to the specified value. Otherwise, the action creates a new record.

The batch version processes up to 200 records each time the recipe runs.

> **UPSERT ACTION RESPONSE BEHAVIOR**
> 
> The **Upsert record** action returns a `200 OK` response from SAP SuccessFactors even when individual record updates fail. This behavior is expected because the SuccessFactors API includes each record's result in the response body instead of the HTTP status code.
> 
> Check the `Http code` value in the action output to verify if each record succeeded. You can use an **If** condition in your recipe to detect `Http code` values other than `200` and handle those records as needed.
> 
> The job completes successfully because the API returns `200 OK` when it processes the request, even if some records fail internally.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names. |

> **ADDITIONAL ATTRIBUTES**
> 
> Depending on the object and your SuccessFactors configuration, additional fields appear where you define more attributes for the record. You can also select optional attributes to update. A common attribute is a navigation field that links this record to another record through a URI, such as a user to their manager. Refer to [Using navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information.

## Output

The output fields vary depending on the object you select. Review the output datatree in your recipe to view available datapills.

> **DATETIME FIELDS**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).
