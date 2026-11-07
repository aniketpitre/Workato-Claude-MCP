---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/update-rows-in-list-action-batch.md
description: >-
  The update rows action in the SharePoint connector lets you update a batch of
  rows in a list you specify using row IDs and field values.
---

# SharePoint - Update rows in SharePoint list action (batch)

This action updates a batch of rows in a SharePoint list you specify. To update multiple rows, select the list containing the rows you plan to update, provide the row/item IDs and the updated values of the list fields.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| List | Specify the list where you plan to update rows. |
| Batch | Specify the batch of rows you plan to update. Each row should contain the row ID and the fields you plan to update. |
| Batch source list | Input a list datapill to specify which rows to update. [Learn more about list input](/en/features/list-management#list-batch-action). |
| Row ID | Provide the ID of the row or item you plan to update. |
| **{List fields}** | Provide input for the list fields you plan to update. These fields are dynamic and are determined by the list you select. For example, a list of employees could include fields for the employee name, title, and contact information. |

## Output

The output datatree contains the status of the update operation for each row.

| Field | Description |
| --- | --- |
| Record status | The status of the update operation for each row. This object contains the Row ID, whether the operation was successful, and the list size and list index. |
