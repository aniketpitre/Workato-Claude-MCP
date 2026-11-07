---
url: 'https://docs.workato.com/en/agentic/workato-go/data-sources/google-calendar.md'
description: >-
  Add Google Calendar as a data source in Workato GO and complete the Google
  Workspace prerequisites so agents can search your calendar content.
---

# Add a Google Calendar data source to Workato GO

You must configure Google Calendar to allow Workato GO to search for information.

> **PREREQUISITES**
> 
> Complete the [Google Workspace prerequisites](/en/agentic/workato-go/data-sources/google-suite#prerequisites) before you add Google Calendar as a data source.

## Add Google Calendar as a data source

Complete the following steps to add Google Calendar as a data source in Workato GO:

1. Sign in to your Workato GO account.
   
2. Expand the **Admin** menu in the sidebar and click **Data sources**.
   
   ![Data sources](/assets/data-sources.D6kxvMoA.png)_Go to **Admin > Data sources**_
   
3. Click **Add Data Source**. The **Add Data Source** page displays.
   
   ![Add data source](/assets/add-data-source.DGJRZeBw.png)_Click **Add Data Source**_
   
4. Select the **Google Calendar** app.
   
   ![Select Google Calendar](/assets/add-a-data-source.CtpmQXk_.png)_Select Google Calendar_
   
5. Enter a name for your data source in the **Name** field.
   
   ![Configure your data source](/assets/configure-data-source-calendar.CGt4yMA8.png)_Configure your data source_
   
6. Enter the admin email associated with your account in the **Admin Email** field. This is the same email you configured in the [prerequisite steps](/en/agentic/workato-go/data-sources/google-suite#create-a-custom-admin-role).
   
7. Go to the **Service Account** field and paste your service account custom role JSON configuration. This is the same file that you obtained during the [prerequisite steps](/en/agentic/workato-go/data-sources/google-suite#create-a-service-account-in-google-cloud-console). The contents are similar to the following:
   
   ![Service account JSON](/assets/service-json-configuration.DMNA6VkG.png)_Service account JSON_
   
8. Click **Create**. Your data source is now listed on the **Data Sources** page.

---
