---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/search-list-items-in-library-action.md
description: >-
  The search list items action in the SharePoint connector lets you search for
  list items in a library you specify.
---

# SharePoint - Search list items in SharePoint library action

This action searches for list items in a specified SharePoint library.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| List | Specify the list to search for items. |
| Filter | Provide a filter condition to use to search for items. |
| Search by | Specify the how you plan to search for items. This section of the UI includes options to Search by list or specify search fields individually. |
| Page size | Specify the maximum number of records to return in a single response. |
| Next page link | Provide the link to the next page of results. |

## Output

The output datatree contains the details of the list items that match the search criteria.

| Field | Description |
| --- | --- |
| \[List fields\] | The fields of the list with their respective values. |
| Next page link | The link to the next page of results. |
