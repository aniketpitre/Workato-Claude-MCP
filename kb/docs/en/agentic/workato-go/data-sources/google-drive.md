---
url: 'https://docs.workato.com/en/agentic/workato-go/data-sources/google-drive.md'
description: >-
  Add Google Drive as a data source in Workato GO and complete the Google
  Workspace prerequisites so agents can search your Drive content.
---

# Add a Google Drive data source to Workato GO

You must configure Google Drive to allow Workato GO to search for information.

> **PREREQUISITES**
> 
> Complete the [Google Workspace prerequisites](/en/agentic/workato-go/data-sources/google-suite#prerequisites) before you add Google Drive as a data source.

## Add Google Drive as a data source

Complete the following steps to add Google Drive as a data source in Workato GO:

1. Sign in to your Workato GO account.
   
2. Expand the **Admin** menu in the sidebar and click **Data sources**.
   
   ![Data sources](/assets/data-sources.D6kxvMoA.png)_Go to **Admin > Data sources**_
   
3. Click **Add Data Source**. The **Add Data Source** page displays.
   
4. Select the Google Drive app.
   
   ![Select Google Drive](/assets/add-a-data-source.CtpmQXk_.png)_Select Google Drive_
   
5. Enter a name for your data source in the **Name** field.
   
6. Enter the admin email associated with your account in the **Admin Email** field. This is the same email you configured in the [prerequisite steps](/en/agentic/workato-go/data-sources/google-suite#create-a-custom-admin-role).
   
7. Go to the **Service Account JSON** field and paste your service account custom role JSON configuration. This is the same file that you obtained during the [prerequisite steps](/en/agentic/workato-go/data-sources/google-suite#create-a-service-account-in-google-cloud-console). The contents are similar to the following:
   
   ![Service account JSON](/assets/service-json-configuration.DMNA6VkG.png)_Service account JSON_
   
8. Click **Create Data Source**. Your data source is now listed on the **Data Sources** page.
   

### Limit Google Drive crawler scope

Workato GO integrates with Google Drive to support enterprise search and automation across your organization's documents. You can use the `google_drive.user_allowlist` property to limit the crawler scope to specific users' files and shared content.

You can use this property to enable the following:

- Limit indexing to a pilot group or specific departments.
- Restrict access to sensitive content for compliance.
- Reduce crawl volume for performance or privacy reasons.

The `google_drive.user_allowlist` property value is a comma-separated list of email addresses.

Complete the following steps to limit the crawler scope in Google Drive:

1. Sign in to your Workato GO account.
   
2. Expand the **Admin** menu in the sidebar and click **Advanced**.
   
3. Click **Add Organization Property**.
   
4. Enter `google_drive.user_allowlist` as the name for your property.
   
5. Enter a comma-separated list of email addresses as the allowlist property value. For example:
   
   ```
   alex@example.com,caroline@example.com,carlos@example.com
   ```
   
6. Click **Submit**.

---
