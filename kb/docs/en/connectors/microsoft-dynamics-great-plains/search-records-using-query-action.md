---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-great-plains/search-records-using-query-action.md
description: >-
  The Search records using query action searches records in Microsoft Dynamics
  GP.
---

# Microsoft Dynamics Great Plains - Search records using query action

The **Search records using query** action searches records in Microsoft Dynamics GP. Datapill introspection for search queries is only available when `DB connection string` is defined in your [connection settings](/en/connectors/microsoft-dynamics-great-plains#connection-setup) and at least one record of the selected object type exists in your GP instance. Workato generates datapills based on the first record retrieved from your GP. You can use the `Output schema (Override)` field to manually define the output schema.

## Input

| Input field | Description |
| --- | --- |
| Select the object to search for | Select the object type to search for. |
| DB connection string | Enter the database connection string to use for the action. |
| Where clause | Enter a where clause to filter the query, such as `CUSTNMBR = AMERICAN0001`. |
| Row count limit | Specifies the number of records to return in the response. |
| Output type | Select the response structure for the query. This field defaults to `Complete document` when left empty. |
| Output schema (override) | Manually define or override the default output schema for this action. |

## Output

This action returns the array of objects. You can manually define the structure using the `output schema (Override)` field.
