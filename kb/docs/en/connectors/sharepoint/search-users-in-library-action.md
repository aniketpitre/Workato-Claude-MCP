---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/search-users-in-library-action.md
description: >-
  The search users action in the SharePoint connector lets you search for users
  on a SharePoint site by filter and pagination criteria.
---

# SharePoint - Search users in SharePoint library action (batch)

This action searches for users in a SharePoint library you specify.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Filter | Provide a filter condition to use to search for the user. For example, `Email eq xyz@microsoft.com and Id eq 6`. |
| Search by | Specify the how you plan to search for users. You can search by a fixed list or a dynamic list using a list datapill. |
| Search by source list | Input a list datapill to search for users using a list. Learn more about [list input](/en/features/list-management#list-batch-action). |
| ID | Search by the unique identifier assigned to the user. |
| Is hidden in UI? | Search by whether this field is hidden in the user interface. |
| Title | Search by the title or name associated with the user. |
| Login name | Search by the user's login name used for authentication. |
| Expiration | Search by the date when the user's account or access expires. |
| User principal name | Search by the principal name of the user in the domain. |
| Is email authentication guest user? | Search by whether the user is authenticated as a guest via email. |
| Is shared by email guest user? | Search by whether the user account is shared as a guest user via email. |
| Is site Admin? | Search by whether the user has administrative privileges on the site. |
| Principal type | Search by the type of principal, such as user or group, associated with the user. Refer to the Microsoft [SharePoint principal types](https://learn.microsoft.com/en-us/previous-versions/office/sharepoint-csom/ee541430\(v=office.15\)#members) documentation for more information. |
| Email | Search by the email address associated with the user. |
| OData ID | Search by the unique identifier in the OData format for the user. |
| OData type | Search by the type of data as per OData specifications. |
| Pagination | Specify how you plan for Workato to handle the search results. This section of the UI includes input fields allowing you to specify the **Page size**, **Offset**, and **Order by** |
| Page size | The maximum number of records to return in a single response. |
| Offset | The number of records to skip. |
| Order by | The field to order the results by. |

## Output

The output datatree contains the details of the users that match the search criteria.

| Field | Description |
| --- | --- |
| ID | The unique identifier assigned to the user in Sharepoint. |
| Is hidden in UI? | Indicates whether the user's profile is hidden in the user interface (UI). |
| Title | The display name or title associated with the user. |
| Login name | The login name or identifier used by the user to access SharePoint. |
| Expiration | The date or status indicating when the user's account or access expires. |
| User principal name | The user's principal name, typically in the format of an email address, used for identification purposes. |
| Is email authentication guest user? | Indicates whether the user is authenticated through email as a guest user. |
| Is shared by email guest user? | Indicates whether the user account is shared via email as a guest user. |
| Is site Admin? | Indicates whether the user has administrative privileges on the site. |
| Principal type | The type of principal, such as user or group, associated with the user. Refer to the Microsoft [SharePoint principal types](https://learn.microsoft.com/en-us/previous-versions/office/sharepoint-csom/ee541430\(v=office.15\)#members) documentation for more information. |
| Email | The primary email address associated with the user account. |
| User ID | The unique identifier assigned to the user within the system. |
| Odata ID | The unique identifier assigned to the user's data entry in the OData format. |
| Odata type | The type or category of data represented by the OData entry related to the user. |
| Odata edit link | A link or URL that allows editing of the user's data entry in OData format. |
| List size | The size or number of items in a list associated with the user. |
| List index | The index or position of the user's entry within a list. |
