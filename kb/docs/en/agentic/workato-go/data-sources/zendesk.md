---
url: 'https://docs.workato.com/en/agentic/workato-go/data-sources/zendesk.md'
description: >-
  Configure Zendesk as a Workato GO data source to index and search Help Center
  articles while following user-level article permissions.
---

# Add a Zendesk data source to Workato GO

You must configure Zendesk to allow Workato GO to search across Zendesk Help Center articles, follow user-level article permissions, and sync content and permission updates multiple times per hour after initial indexing.

> **INDEXED DATA**
> 
> Workato GO indexes only Zendesk Help Center articles.

## Enable API access in Zendesk

You must enable API access to allow Workato GO to access your Zendesk instance.

> **PRIVILEGE REQUIREMENTS**
> 
> You must be a Zendesk admin to complete this configuration.

Complete the following steps to enable API access within Zendesk:

1. Sign in to your Zendesk Admin Center.
   
2. Go to **Apps and Integrations > APIs > Zendesk API**.
   
3. Enable **Token Access**.
   
4. Generate a new API token.
   
5. Store the API token in a secure location. Your API token is required when you add Zendesk as a data source.
   

## Add Zendesk as a data source

You must complete the following steps to add Zendesk as a data source in Workato GO:

1. Sign in to your Workato GO account.
   
2. Expand the **Admin** menu in the sidebar and click **Data sources**.
   
   ![Data sources](/assets/data-sources.D6kxvMoA.png)_Go to **Admin > Data sources**_
   
3. Click **Add Data Source**. The **Add Data Source** page displays.
   
4. Select the Zendesk app.
   
   ![Select Zendesk](/assets/add-a-data-source.CtpmQXk_.png)_Select Zendesk_
   
5. Enter a name for your data source in the **Name** field.
   
6. Enter the domain for your data source in the **Zendesk Domain** field. For example: `https://acme.zendesk.com`
   
7. Enter your API token from your data source in **API Token** field.
   
8. Enter the email associated with the data source in the **Email** field. For example: `admin@acme.com`
   
9. Click **Next**. The **Crawl** configuration page displays.
   
10. Optional. Click the **Allow ticket crawl** and **Allow article crawl** toggles to disable ticket and article crawling. Ticket and article crawling are enabled by default.
    
    > **CRAWLING IS NECESSARY TO BUILD A SEARCH INDEX**
    > 
    > Workato builds a search index by crawling your data source and parsing its contents, metadata, and permissions.
    
11. Click **Create**. Your data source is now listed on the **Data Sources** page.

---

---
url: >-
  https://docs.workato.com/en/agentic/workato-go/data-sources/crawler-failure-notifications.md
description: >-
  Configure Workato GO crawler failure notifications to email a list of
  recipients when a data source crawler fails to fetch content.
---

# Crawler failure notifications

Workato GO crawlers fetch data from connected sources, such as Google Drive, Confluence, Slack, and more. You can configure crawler notifications to send emails when a crawler fails.

## Configure notifications

You can create a property with a list of emails that receive crawler failure notifications in Workato GO.

Complete the following steps to configure crawler failure notifications:

1. Sign in to your Workato GO account.
   
2. Expand the **Admin** menu in the sidebar and click **Advanced**.
   
3. Click **Add Organization Property**.
   
4. Enter a name for your property. For example: `crawler.failure_notification_emails`
   
5. Enter the email addresses that should receive notifications. You must separate user email addresses with commas. For example:
   
   ```
   alex@example.com,caroline@example.com,carlos@example.com
   ```
   
6. Click **Submit**.
   

## Crawler failure error codes

Workato GO returns specific error codes when crawlers fail to access or process data. You can use these codes to identify the root cause of failures and take corrective action. The following tables list common error codes by data source, their descriptions, and the required actions:

### General error codes

| Code | Description | Required action |
| --- | --- | --- |
| GENERAL\_1 | Network connection timeout | The crawler couldn't reach the target service. |
| GENERAL\_2 | DNS resolution failed | The website URL couldn't be resolved. Verify that your data source URL is correct. |
| GENERAL\_3 | Invalid crawler configuration | Your data source is missing required settings. Review and update your configuration. |
| GENERAL\_4 | Service temporarily unavailable | The service is temporarily unavailable. Try again later. |
| GENERAL\_5 | Record not found | The data source may have been deleted. Verify it still exists in your workspace. |
| GENERAL\_6 | API rate limit exceeded | The target service is limiting requests. The crawler automatically retries after the rate limit resets. |
| GENERAL\_7 | API endpoint not found | The API URL in your configuration may be incorrect. Update your data source settings. |

### Confluence error codes

| Code | Description | Required action |
| --- | --- | --- |
| CONFLUENCE\_1 | Confluence authentication failed | Your API token is expired or invalid. Generate a new token in Confluence and update your data source. |
| CONFLUENCE\_3 | Insufficient Confluence permissions | The Confluence user doesn't have access to the requested content. Check the user's space and page permissions. |
| CONFLUENCE\_99 | Unknown Confluence error | An unexpected error occurred. Contact support if the issue persists. |

### Custom web data source error codes

| Code | Description | Required action |
| --- | --- | --- |
| WEB\_1 | Web crawler authentication failed | The website requires login credentials. Only publicly accessible websites are supported. |
| WEB\_99 | Unknown web crawler error | An unexpected error occurred. Contact support if the issue persists. |

### Google Drive error codes

| Code | Description | Required action |
| --- | --- | --- |
| GDRIVE\_1 | Google Drive service account authentication failed | Service account credentials are invalid or expired. Re-upload your credentials JSON file. |
| GDRIVE\_3 | Insufficient Google Drive permissions | The service account doesn't have access to the files or folders. Share the files or folders with your service account email. |
| GDRIVE\_99 | Unknown Google Drive error | An unexpected error occurred. Contact support if the issue persists. |

### Highspot error codes

| Code | Description | Required action |
| --- | --- | --- |
| HIGHSPOT\_1 | Highspot authentication failed | Your API credentials are invalid or expired. Update your Highspot API credentials in the data source. |
| HIGHSPOT\_3 | Insufficient Highspot permissions | The API user doesn't have the required access. Contact your Highspot administrator to grant permissions. |
| HIGHSPOT\_99 | Unknown Highspot error | An unexpected error occurred. Contact support if the issue persists. |

### Jira error codes

| Code | Description | Required action |
| --- | --- | --- |
| JIRA\_1 | JIRA authentication failed | Your API token or credentials are invalid. Generate a new API token in JIRA and update your data source. |
| JIRA\_3 | Insufficient JIRA permissions | The JIRA user doesn't have access to the requested project. Check the user's project permissions. |
| JIRA\_99 | Unknown JIRA error | An unexpected error occurred. Contact support if the issue persists. |

### People directory error codes

| Code | Description | Required action |
| --- | --- | --- |
| PEOPLE\_1 | People directory authentication failed | Your Okta or Google Workspace connection has expired. Re-authenticate in your data source settings. |
| PEOPLE\_3 | Insufficient directory permissions | The connected account doesn't have directory read permissions. Ask your IT admin to grant access to the necessary permissions. |
| PEOPLE\_99 | Unknown people sync error | An unexpected error occurred. Contact support if the issue persists. |

### Slack error codes

| Code | Description | Required action |
| --- | --- | --- |
| SLACK\_1 | Slack authentication failed | Your bot token is invalid or the app was uninstalled. Reconnect Slack in your data source settings. |
| SLACK\_3 | Missing required Slack OAuth scopes | The Slack app needs additional permissions. Re-authorize the Slack connection with the required scopes. |
| SLACK\_99 | Unknown Slack error | An unexpected error occurred. Contact support if the issue persists. |

---
