---
url: 'https://docs.workato.com/en/data-tables/data-table-connector.md'
description: >-
  Learn how the Workato Data table connector provides triggers and actions to
  use your data tables in recipes, with selectable JSON output formats.
---

# Data table connector

Workato’s Data table connector supports triggers and actions that enable you to use your data tables in your recipes.

![Available actions](/assets/data-table-connector.CelKt9qQ.png)_Data table connector actions_

## Output formats

Every column (field) in a data table is internally represented by a hash value. This allows Workato to preserve relations and references even when column names change. However, if you plan to work with the connector's JSON output directly, referencing the hash value of a column is not as intuitive as referencing its name.

The **Choose the desired output format** field lets you select the output format that supports your use case. Available output formats include:

- **Field hash to value** (default): This output format allows Workato to preserve relations and references even when the column's name changes but provides a less intuitive JSON output.
- **Field name to value**: This output format makes the output datapills susceptible to column name changes but results in a more human-readable output, which is ideal for working with JSON objects directly using formulas.

You can observe the differences in output formats by logging the step output or copying the JSON from the output tab:

### Field hash to value

```
{
  "a5612739_5401_4ae7_bd07_782c1a6fb2d1": "2023-10-20T07:26:38.453000+00:00",
  "61aae604_a95e_4519_9091_bb0bf754a67f": "2023-10-20T07:26:38.453000+00:00",
  "11fbe9a6_a16d_4d7e_86ea_afe42ec03005": "e04b77b7-31d0-4602-92ee-505270baaf52",
  "565653a5_9411_4290_8b15_3a229ddb4d0a": "John Doe",
  "d944b778_611d_4294_a324_4d9cda9165bf": {
    "record_id": "8e5ab08c-af6f-4d58-a1b4-73b19a1960a0",
    "display_name": "Jane Smith"
  }
}
```

### Field name to value

```
{
  "Created at": "2023-10-20T07:26:38.453000+00:00",
  "Updated at": "2023-10-20T07:26:38.453000+00:00",
  "Record ID": "e04b77b7-31d0-4602-92ee-505270baaf52",
  "Name": "John Doe",
  "Relation": {
    "record_id": "8e5ab08c-af6f-4d58-a1b4-73b19a1960a0",
    "display_name": "Jane Smith"
  }
}
```

## Triggers and actions

Available triggers and actions include:

- [New records trigger (batch)](/en/data-tables/connector/new-records-batch-trigger)
- [New record trigger (real-time)](/en/data-tables/connector/new-record-trigger)
- [New/updated records trigger (batch)](/en/data-tables/connector/new-updated-records-batch-trigger)
- [New/updated record trigger (real-time)](/en/data-tables/connector/new-updated-record-trigger)
- [Create record action](/en/data-tables/connector/create-record-action)
- [Create records action (batch)](/en/data-tables/connector/create-record-batch-action)
- [Delete record action](/en/data-tables/connector/delete-record-action)
- [Delete records action (batch)](/en/data-tables/connector/delete-record-batch-action)
- [Delete records by condition action (batch)](/en/data-tables/connector/delete-records-condition-action)
- [Remove values from a record](/en/data-tables/connector/remove-values-from-record-action)
- [Search records action (batch)](/en/data-tables/connector/search-records-action)
- [Truncate table action (batch)](/en/data-tables/connector/truncate-table-action)
- [Update record action](/en/data-tables/connector/update-record-action)
- [Update records action (batch)](/en/data-tables/connector/update-record-batch-action)
- [Upsert record action](/en/data-tables/connector/upsert-record-action)
- [Upsert records action (batch)](/en/data-tables/connector/upsert-record-batch-action)

> **RECREATE LOOKUP TABLE BEHAVIOR**
> 
> The **Data tables** connector doesn't include the [Get all entries](/en/features/lookup-tables#get-all-entries-action-batch) or [Lookup entry](/en/features/lookup-tables#lookup-entry-action) actions from the **Lookup tables** connector. Refer to the [Recreate Lookup table behavior](/en/data-tables/connector/search-records-action#recreate-lookup-table-behavior) guide for ways to achieve similar results using the **Search records** action.

---
