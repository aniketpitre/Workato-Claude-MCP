---
url: 'https://docs.workato.com/en/agentic/workato-go/data-sources/highspot.md'
description: >-
  Add a Highspot data source to Workato GO by enabling API access and providing
  your subdomain so agents can search Highspot content.
---

# Add a Highspot data source in Workato GO

You must enable Highspot API functionality and provide credentials to allow Workato GO to search Highspot content.

The Highspot crawler can't crawl the APIs to determine the specific permissions for admins. Highspot admins can access all crawled information in Workato GO search results, regardless of the actual permissions for individual content.

> **CONTACT HIGHSPOT SUPPORT FOR API ENABLEMENT**
> 
> You must contact the Highspot support team and request API instance enablement. Workato GO requires **User Impersonation** privileges to crawl spots.

You must provide your Highspot subdomain. Your Highspot instance subdomain is determined by the URL used to access that instance. For example, your subdomain is `acme` if your URL is `acme.highspot.com`.

## Add Highspot as a data source

Complete the following steps to add Highspot as a data source in Workato GO:

1. Sign in to your Workato GO account.
   
2. Expand the **Admin** menu in the sidebar and click **Data sources**.
   
   ![Data sources](/assets/data-sources.D6kxvMoA.png)_Go to **Admin > Data sources**_
   
3. Click **Add Data Source**. The **Add Data Source** page displays.
   
4. Select the Highspot app.
   
   ![Select Highspot](/assets/add-a-data-source.CtpmQXk_.png)_Select Highspot_
   
5. Enter a name for your data source in the **Name** field.
   
6. Enter the subdomain for your data source in the **Highspot Subdomain** field. For example, your subdomain is `acme` if your URL is `https://acme.highspot.com/`.
   
7. Enter your API URL in the **API URL** field. Refer to [Retrieve your client credentials](#client-credentials) for more information.
   
8. Enter your API client key in the **API Client Key** field. Refer to [Retrieve your client credentials](#client-credentials) for more information.
   
9. Enter your API client secret in the **API Client Secret** field. Refer to [Retrieve your client credentials](#client-credentials) for more information.
   
10. Click **Next**. The **Crawl** configuration page displays.
    
11. Locate the **Would you like to start the crawl for Highspot?** field and select **Crawl Now** or **Do it later**.
    
    > **CRAWLING IS NECESSARY TO BUILD A SEARCH INDEX**
    > 
    > Workato builds a search index by crawling your data source and parsing its contents, metadata, and permissions.
    
12. Click **Create**. Your data source is now listed on the **Data Sources** page.
    

## Retrieve your client credentials

You must provide API client credentials when you add Highspot as a data source in Workato GO.

Complete the following steps to obtain your Highspot API client credentials:

1. Sign in to your Highspot account.
   
2. Go to **User Settings > Developer**.
   
3. Go to **Developer settings > API credentials**.
   
4. Copy the **API URL**. Highspot URLs typically use the following format, but may vary depending on the integration: `https://api-xxx.highspot.com/v0.5/`
   
5. Copy the **Client key**, also called **Client ID**, and the **Client secret**.
   
6. Ensure that **API Impersonation** is enabled.

---
