---
url: 'https://docs.workato.com/en/connectors/netsuite-rest/get-async-job.md'
description: >-
  The Get async job result action retrieves the status and result of an
  asynchronous job in NetSuite REST.
---

# NetSuite REST - Get async job result action

The **Get async job result** action retrieves the status and result of an asynchronous job in NetSuite REST.

Use this action to check the progress and outcome of jobs created by the [Create records (async)](/en/connectors/netsuite-rest/create-record-async), [Update records (async)](/en/connectors/netsuite-rest/update-records-async), [Upsert records (async)](/en/connectors/netsuite-rest/upsert-records-async), or [Delete records (async)](/en/connectors/netsuite-rest/delete-record-async) batch actions.

## Input

| Input field | Description |
| --- | --- |
| Async job ID | Enter the identifier of the asynchronous job to retrieve. Use the **Async job ID** returned by an async create, update, upsert, or delete action. |

## Output

| Output field | Description |
| --- | --- |
| Started at | The timestamp when the job started processing. |
| Completed at | The timestamp when the job completed. |
| Progress | The current progress of the job. |
| Task results | A list containing one entry per record submitted in the batch. Each entry reports the outcome for a single record. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/initialize-record-action.md
description: >-
  The Initialize record action retrieves a pre-filled record without creating it
  in NetSuite REST.
---

# NetSuite REST - Initialize record action

The **Initialize record** action retrieves a pre-filled record without creating it in NetSuite REST.

The action populates a target record with data from an existing reference record and returns it without saving it in NetSuite, so you can inspect or modify the values before you create the record.

Use the [Transform record](/en/connectors/netsuite-rest/transform-record-action) action to create a record from an existing source instead of filling and retrieving it.

The **Record** and **Reference record** types must form a supported transformation pair. Refer to the [Supported transformation types](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4267258715.html#bridgehead_4327469981) for valid source-to-target combinations. For setup requirements, see [REST Web Services prerequisites and setup](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html).

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to initialize. The action returns a pre-filled record of this type. |
| Reference record | Select the NetSuite record type of the existing reference record. The action uses data from this record to pre-fill the target record. |
| Reference record ID | Enter the internal ID of the existing reference record instance. |

## Output

The output is the pre-filled target record. The output schema reflects the record type you select in the **Record** field, including its standard fields and any custom fields configured in NetSuite. The available output fields vary by record type because the schema is dynamic. After you select a record type, the recipe editor displays the output fields for that record.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/search-custom-records-action.md
description: >-
  The Search custom records action in the NetSuite REST connector lets you
  search and filter custom records in NetSuite.
---

# NetSuite REST - Search custom records action

The **Search custom records** action allows you to search for custom records in NetSuite REST. You can either enter a **Search query** or use the **Search settings** input fields to filter records. Workato prioritizes the **Search query** field if you specify both.

You can only use fields with known data types to filter the input fields. Use a custom **Search query** to filter by other fields.

> **PREREQUISITES**
> 
> You must complete the following before you use this action:
> 
> - Enable the **SuiteAnalytics Workbook** feature on your account.
> - Have the **SuiteAnalytics Workbook (View)** permission on your role.
> 
> Refer to the NetSuite [Prerequisites and Setup for REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) guide for more information about the features and permissions required for REST Web Services.

## Input

| Input field | Description |
| --- | --- |
| Custom record | Select a NetSuite custom record type, or toggle to enter a custom value. The list populates from the custom record types located in your account at **Customization > Records > Record Types**. |
| Search query | Provide a search query to filter records, such as `name START_WITH test`. Refer to the [NetSuite Records Catalog](https://system.netsuite.com/app/recordscatalog/rcbrowser.nl) for more information on field names, types, and availability. |
| Search settings | Expand this section to configure search settings. |
| String fields | Select the search operator for all String fields. Default is **CONTAIN**. |
| Number fields | Select the search operator for all Integer, Number, Float, Double, and Duration fields. Default is **EQUAL**. |
| Date/Time fields | Select the search operator for all Date, Time, and DateTime fields. Default is **ON**. |
| Limit | Specify the number of records to retrieve on a single page. The maximum is `1000`. The default is `200`. |
| Offset | Specify the starting position for retrieving records. The default is `0`. |

## Output

| Output field | Description |
| --- | --- |
| Items | A list of records returned as a result of the search. Each item's fields depend on the **Custom record** type you select. |
| Has more | Indicates whether there are more records associated with the search query that weren't included in the output. |
| Count | The number of records returned in the current response. |
| Offset | The starting index of the records in the current response relative to the full result set. |
| Total results | The total number of results matching the search criteria. |

---
