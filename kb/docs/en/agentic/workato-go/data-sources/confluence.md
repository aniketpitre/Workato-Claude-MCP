---
url: 'https://docs.workato.com/en/agentic/workato-go/data-sources/confluence.md'
description: >-
  Add a Confluence data source to Workato GO by enabling API access and
  providing credentials so agents can search your Confluence content.
---

# Add a Confluence data source in Workato GO

[Confluence](https://www.atlassian.com/software/confluence) provides a comprehensive collaboration environment designed to enhance team interaction and knowledge exchange.

You must enable Confluence API functionality and provide credentials to allow Workato GO to search your Confluence content.

## Prerequisites

The following prerequisites are required to add a Confluence data source to Workato GO:

- A Confluence Cloud account. This is the only account type supported.
- A Confluence account that is configured for managed users.
- The ability to retrieve Confluence user access groups.

## Enable API access in Confluence

You must enable API access to allow Workato GO to access your Confluence instance. You must have permissions for Confluence spaces, pages, users, and groups to create an API token that can retrieve these data sources.

Complete the following steps to enable API access within Confluence:

1. Sign in to your Atlassian account.
   
2. Click the profile icon and select **Account settings**.
   
3. Click the **Security** tab.
   
4. Click **Create and manage API tokens > Create API token**.
   
5. Enter a name for your API token in the **Name** field.
   
6. Click the **Expires on** field and use the calendar modal to select an expiration date for your token. Tokens can't last longer than a year.
   
7. Click **Create**.
   
8. Click the **Copy** button to copy your API token for use in Workato GO.
   

## Add Confluence as a data source

Complete the following steps to add Confluence as a data source in Workato GO:

1. Sign in to your Workato GO account.
   
2. Expand the **Admin** menu in the sidebar and click **Data sources**.
   
   ![Data sources](/assets/data-sources.D6kxvMoA.png)_Go to **Admin > Data sources**_
   
3. Click **Add Data Source**. The **Add Data Source** page displays.
   
4. Select the Confluence app.
   
   ![Select Confluence](/assets/add-a-data-source.CtpmQXk_.png)_Select Confluence_
   
5. Enter a name for your data source in the **Name** field.
   
6. Enter the domain for your data source in the **Domain** field. For example: `https://acme.atlassian.net`.
   
7. Enter the groups you plan to provide with default access in the **Default Access Groups** field. Separate groups with a comma. For example: `confluence-users-sales,confluence-admins`. Refer to [Retrieve default access groups](#retrieve-default-access-groups) for more information.
   
8. Enter the API token from your Atlassian account in the **API Token** field.
   
9. Enter the user name associated with the data source in the **Username** field. For example: `admin@acme.com`.
   
10. Click **Next**. The **Crawl** configuration page displays.
    
11. Locate the **Would you like to start the crawl for Confluence?** field and select **Crawl Now** or **Do it later**.
    
    > **CRAWLING IS NECESSARY TO BUILD A SEARCH INDEX**
    > 
    > Workato builds a search index by crawling your data source and parsing its contents, metadata, and permissions.
    
12. Click **Create**. Your data source is now listed on the **Data Sources** page.
    

### Retrieve default access groups

Default access groups define who can view and access Confluence resources in Workato GO. You must have admin privileges in Confluence to retrieve default access group names. Only members in listed groups can interact with the Confluence data source in Workato GO.

Complete the following steps to retrieve default access group names:

1. Go to [https://admin.atlassian.com/](https://admin.atlassian.com/) and sign in as an admin.
   
2. Click **Directory > Groups**.
   
3. Copy the group names you plan to add to Workato GO.
   
4. Add the group names as a comma-separated list into the **Default Access Groups** field in Workato GO. For example: `confluence-users, confluence-admins`
   

## Crawler limitations

The Confluence crawler has the following limitations:

- Crawling is only supported for documents created in a Confluence workspace. Attachments in Confluence, such as PDFs or images, aren't crawled.
  
- The Confluence crawler only works with managed accounts connected to SSO because Workato GO uses admin tokens and APIs without a marketplace app.

---
