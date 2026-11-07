---
url: 'https://docs.workato.com/en/workflow-apps/limits.md'
description: >-
  Reference for Workato Workflow apps quotas, including data table quotas and
  the asset import and export support for apps, tables, and pages.
---

# Workflow apps quotas

Workflow apps has the following quotas:

> **DEFAULT QUOTAS**
> 
> The quotas on this page are defaults based on Workato best practices and are configured to enable optimal platform performance. Customers on Enterprise plans or above can contact their Customer Success Representative to request an extension of these quotas for their specific use cases.

| Feature | Description | Quota |
| --- | --- | --- |
| Tasks | Maximum expiration time for a task | 370 days |
| Workflow stages | Maximum number of workflow stages | 1,000 |
| User groups | Maximum number of user groups per user | 50 |
| Pages | Maximum file size for files uploaded to standard Pages | 500 MB |
| Pages | Maximum file size for files uploaded to public Pages | 100 MB |
| Recipe as a data source for drop-down components | Maximum number of records the **Workflow apps New open or search event from a drop-down** component trigger can return. If the number of records exceeds this quota, you can enable typeahead search and use the recipe to search for and load search results. | 1,000 |
| Data tables as a data source for drop-down components | Maximum number of records searchable using `contains` logic. If the data table has more than 100 records, Workflow apps uses `starts with` search logic instead. | 100 |
| Workflow apps connector | Maximum number of users or user groups you can share a request with using the Share requests action | 20 |

[General data tables and data tables column quotas](/en/limits#data-tables-limits) also apply to Workflow apps.

Additionally, Workato supports the import and export of all assets related to Workflow apps, including apps, data tables, and pages.

However, the recipe lifecycle management feature does not currently support importing/exporting certain [column types](/en/data-tables/user-interface/column-types)/components, or their data. These include the following column types/components:

- File: This column does not support the "Include data" option and the content of the files is not present in the manifest.

> **FURTHER READING**
> 
> Refer to the [Platform quotas](/en/limits) documentation for more information about Workato quotas.

---
