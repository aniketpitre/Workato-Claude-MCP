---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-search-action.md
description: >-
  Use the Search records action to retrieve a list of records that match your
  search criteria for the selected object in SAP SuccessFactors.
---

# SAP SuccessFactors - Search records action

Retrieves a list of the records that match your search criteria, such as users who work remotely.

## Input

| Field | Description |
| --- | --- |
| Object | Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names. |
| Navigation fields | Select the related records to include in the output. Navigation fields appear only when the connection uses OData V2 and the object has navigation properties. Refer to [Use navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information. |
| Additional attributes | Per-field search filters generated from the selected object. The fields depend on the selected object and your SuccessFactors configuration. Enter a value in any field to filter the search by that attribute. For example, selecting the **User** object exposes inputs such as **Display name**, **Email**, **User ID**, and **Username**. |
| Output fields | Workato fetches all available fields in the selected record by default. Use this input to filter for only the output fields you need. Optional field. |

## Output

The output fields vary depending on the object you select. To view the available datapills, review the output datatree.

> **DateTime fields**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).
