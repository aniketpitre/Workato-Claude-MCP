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
