---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-advanced-search-action.md
description: >-
  Use the Search records using OData query action to retrieve records that match
  a specific OData query in SAP SuccessFactors.
---

# SAP SuccessFactors - Search records using OData query action

Retrieves the records that match a specific OData query.

## Input

| Field | Description |
| --- | --- |
| Object | Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names. |
| Query | Enter the OData query filter. Required. Refer to the [SAP documentation](https://help.sap.com/doc/7efdca36492e47c7b20ab92c4ca6323c/2211/en-US/SF_EC_OData_API_REF.pdf#page=36) to learn more about filtering with the OData v2 API. |
| Output fields | Workato fetches all available fields in the selected record by default. Use this input to filter for only the output fields you need. Optional field. |
| Page size | Specify the maximum number of records to return. Default: 100. Maximum: 1000. Optional field. |
| Offset | Specify the number of records to skip. Default: 0. Optional field. |
| Order by | Order the returned records by a field. For example, `lastModified asc` or `lastModified desc`. Optional field. |
| From date | Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from "from date" to the effective end date. You can't use "from date" together with "as of date". This field isn't supported on OData V4 connections. Optional field. |
| To date | Pick a date or enter it in MM/DD/YYYY format. SuccessFactors returns records from the effective start date to the "to date". You can't use "to date" together with "as of date". This field isn't supported on OData V4 connections. Optional field. |
| As of date | Pick a date or enter it in MM/DD/YYYY format. You can't use "as of date" together with "from date" or "to date". This field isn't supported on OData V4 connections. Optional field. |
| Navigation fields | Select the related records to include in the output. Navigation fields appear only when the connection uses OData V2 and the object has navigation properties. Refer to [Use navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information. |

## Output

The output fields vary depending on the object you select. To view the available datapills, review the output datatree.

> **DateTime fields**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).
