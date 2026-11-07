---
url: 'https://docs.workato.com/en/agentic/workato-go/data-sources/jira.md'
description: >-
  Add a Jira data source to Workato GO by creating an API token so agents can
  search your Jira tickets directly from the GO interface.
---

# Add a Jira data source in Workato GO

You must configure Jira to allow Workato GO to search for Jira tickets.

## Create an API token in Jira

You must create an API token to allow Workato GO to access your Jira instance.

Complete the following steps to create the API token:

1. Sign in to your Atlassian account.
   
2. Click the profile icon and select **Account settings**.
   
3. Click the **Security** tab.
   
4. Click **Create and manage API tokens > Create API token**.
   
5. Enter a name for your API token in the **Name** field.
   
6. Click the **Expires on** field and use the calendar modal to select an expiration date for your token. Tokens can't last longer than a year.
   
7. Click **Create**.
   
8. Click the **Copy** button to copy your API token. This value is required to add Jira as a data source in Workato GO.
   

## Add Jira as a data source

Complete the following steps to add Jira as a data source in Workato GO:

1. Sign in to your Workato GO account.
   
2. Expand the **Admin** menu in the sidebar and click **Data sources**.
   
   ![Data sources](/assets/data-sources.D6kxvMoA.png)_Go to **Admin > Data sources**_
   
3. Click **Add Data Source**. The **Add Data Source** page displays.
   
4. Select the Jira app.
   
   ![Select Jira](/assets/add-a-data-source.CtpmQXk_.png)_Select Jira_
   
5. Enter a name for your data source in the **Name** field.
   
6. Enter the domain for your data source in the **Domain** field. For example: `https://acme.atlassian.net`
   
7. Enter the groups you plan to provide with default access in the **Default Access Groups** field. Separate groups with a comma. For example: `jira-general,jira-admins`. Refer to [Retrieve default access groups](#add-default-access-groups) for more information.
   
8. Enter your API token from your data source in **API Token** field.
   
9. Enter the email associated with the data source in the **Email** field. For example: `admin@acme.com`
   
10. Click **Next**. The **Crawl** configuration page displays.
    
11. Locate the **Would you like to start the crawl for Jira?** field and select **Crawl Now** or **Do it later**.
    
    > **CRAWLING IS NECESSARY TO BUILD A SEARCH INDEX**
    > 
    > Workato builds a search index by crawling your data source and parsing its contents, metadata, and permissions.
    
12. Click **Create**. Your data source is now listed on the **Data Sources** page.
    

## Retrieve default access groups

Default access groups define who can view and access Jira resources in Workato GO. You must have admin privileges in Jira to retrieve default access group names.

Complete the following steps to retrieve default access group names:

1. Go to [https://admin.atlassian.com/](https://admin.atlassian.com/) and sign in as an admin.
   
2. Click **Directory > Groups**.
   
3. Copy the group names you plan to add to the **Default Access Groups** field in Workato GO.

---
