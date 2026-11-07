---
url: 'https://docs.workato.com/en/agentic/workato-go/faqs.md'
description: >-
  Answers to common questions about Workato GO, including setup, data sources,
  the Action Board, and troubleshooting.
---

# Workato GO - FAQ

Get answers to frequently asked questions about Workato GO, including setup, data sources, Action Board, and troubleshooting.

## Overview

What is Workato GO?

[Workato GO](/en/agentic/workato-go) is an end-user interface that unifies AI-driven workflows, knowledge searches, and transactional interactions within a single, cohesive interface. It eliminates the need to switch between disconnected tools, search systems, and workflows.

**Key capabilities**:

- **Knowledge searches**: Combines public resources and multiple third-party applications to find answers across internal data sources like Google Drive, Slack, Confluence, Salesforce, and more.
- **Integrated chat**: Users can interact with agents and Enterprise data through a single prompt-driven interface.
- **Context-aware routing**: Determines whether a query is handled better by a genie, a search result, or both.
- **Simplified task flow**: Forms, approvals, and user confirmations are built into the interface to avoid switching between apps.

What types of knowledge can I search with Workato GO?

Workato GO provides two [knowledge sources](/en/agentic/workato-go/search):

- **World knowledge**: Search across publicly available information
- **Company knowledge**: Search across your company's third-party apps and internal documentation

What data sources does Workato GO support?

Workato GO supports a broad range of [data sources](/en/agentic/workato-go/data-sources) out-of-the-box, including Confluence, Salesforce, Slack, Google Drive, Jira, Gmail, Gong, and more. You can also add custom web crawler data sources to index internal documentation sites or public web pages.

## Setup and configuration

How do I configure a subdomain for Workato GO?

Complete the following steps to [configure your subdomain](/en/agentic/workato-go/configuration#configure-your-subdomain):

1. Go to **Manage > Workato GO admin > Subdomain**.
   
2. Enter your subdomain. For example, `acme-enhanced` creates `https://acme-enhanced.workato.ai`.
   
3. Click **Save**.
   

Your subdomain must be 3-65 characters. A unique, randomly generated subdomain is provided by default if you don't customize it.

Can I customize the branding in Workato GO?

Yes, you can [customize the company name and logo](/en/agentic/workato-go/configuration#configure-your-branding) using organization properties:

1. Go to **Admin > Advanced** in Workato GO.
   
2. Click **Add Organization Property**.
   
3. Set the property:
   
   - **Company name**: Use `ui.company_name` with your company name as the value
   - **Logo**: Use `ui.branding_logo` with your logo URL as the value

**Logo requirements**: Public URL, transparent .png or .svg, 210x40px dimensions, under 200 KB.

How do I add administrators to Workato GO?

Complete the following steps to [add administrators](/en/agentic/workato-go/admins-user-groups) to Workato GO:

1. Go to **Manage > Workato GO admin > End user access**.
   
2. Select users from the **End users** drop-down menu.
   
3. Click **Save**.
   

Administrators can manage data sources and view the activity log.

How do I change the theme in Workato GO?

Workato GO supports three themes: Light theme, Dark theme, and Sync with device, which matches your operating system settings.

You can change your theme by clicking your profile icon in the side navigation bar to open **Preferences**, then selecting your preferred theme.

Refer to [Choose a theme](/en/agentic/workato-go/preference-settings#choose-a-theme) for more information.

## Data sources

What are data sources?

[Data sources](/en/agentic/workato-go/data-sources) enable Workato GO to connect to your business systems, such as Jira, Confluence, Salesforce, and Google Drive, for enterprise search and AI workflows. This ensures search results reflect your actual business context and genies can retrieve current data to complete tasks.

How do I add a data source to Workato GO?

Each data source has specific configuration requirements. You must have administrator privileges in Workato GO to add data sources.

Refer to the connector-specific documentation for setup instructions:

- [Confluence](/en/agentic/workato-go/data-sources/confluence)
- [Gmail](/en/agentic/workato-go/data-sources/gmail)
- [Gong](/en/agentic/workato-go/data-sources/gong)
- [Google Calendar](/en/agentic/workato-go/data-sources/google-calendar)
- [Google Drive](/en/agentic/workato-go/data-sources/google-drive)
- [Highspot](/en/agentic/workato-go/data-sources/highspot)
- [Jira](/en/agentic/workato-go/data-sources/jira)
- [Okta](/en/agentic/workato-go/data-sources/okta)
- [Salesforce](/en/agentic/workato-go/data-sources/salesforce)
- [Slack](/en/agentic/workato-go/data-sources/slack)
- [Zendesk](/en/agentic/workato-go/data-sources/zendesk)

**Custom web pages**: You can also add custom web crawler data sources to index internal documentation sites or public web pages. Refer to [Add a web crawler data source](/en/agentic/workato-go/data-sources#add-a-custom-data-source).

Can I limit which Google Drive files are indexed by Workato GO?

Yes, you can [limit the Google Drive crawler scope](/en/agentic/workato-go/data-sources/google-drive#limit-google-drive-crawler-scope) to specific users' files:

1. Go to **Admin > Advanced** in Workato GO.
   
2. Click **Add Organization Property**.
   
3. Set `google_drive.user_allowlist` as the name and a comma-separated list of email addresses as the value.
   

This enables you to limit indexing to a pilot group, specific departments, or restrict access to sensitive content.

How does Workato GO handle permissions when ingesting data?

[Workato GO](/en/agentic/workato-go) respects native permissions from source systems:

- Documents private to specific users won't appear in searches for other users
- Folder-level security permissions are maintained (for example, Google Drive)
- You can restrict which users are crawled/indexed
- Permission-aware crawling ensures users only see content they have access to in the source system

## Action Board

What is Action Board?

[Action Board](/en/agentic/agent-studio/action-board) displays customizable dashboards in [Workato GO](/en/agentic/workato-go) that visualize KPI metrics configured in Agent Studio. Action Board displays:

- **Real-time KPI metrics** for each genie using customizable thumbnails for charts, tables, or stacked metrics.
- **Open action items** in the right-side panel, including business events directed to you and approvals assigned to you.
- **Genie widgets** with defined roles and job descriptions that you can engage with conversationally.

**Important**: Action Board and the KPI tab are only available for genies that use Workato GO as the chat interface. Action Board doesn't support genies using Slack or Microsoft Teams.

What are the prerequisites for using Action Board?

To use Action Board, you must:

- Have a genie configured with **Workato GO** as the chat interface.
- Create at least one KPI for your genie.
- Configure at least one Action Board thumbnail to display metrics.
- Have the appropriate user group permissions to view Action Board thumbnails.

Learn more about [Action Board](/en/agentic/agent-studio/action-board).

How do KPIs work with Action Board?

KPIs (Key Performance Indicators) are quantifiable measurements of progress toward company goals. KPIs use [data tables](/en/data-tables) to store frequently used data that KPI skills reference.

The workflow is:

1. End user triggers a KPI skill, for example, `New lead`.
2. The skill writes to the configured data table.
3. Workato loads this information and combines it with configured tasks.
4. KPI reports are generated and displayed in Action Board thumbnails.

Action Board supports four thumbnail types:

- Card format (default)
- Metric & chart
- Stacked metrics
- Detailed table

Each action board is limited to five thumbnails.

Learn more about [creating KPIs](/en/agentic/agent-studio/action-board).

## Troubleshooting

What should I do if real-time search or chat stops working?

This is typically caused by blocked or terminated Server-Sent Events (SSE) connections. SSE is a network-level issue, not a browser-specific problem.

**Symptoms**:

- Chat messages aren't updating in real-time
- Connection appears to close immediately
- No continuous event stream received

**Diagnosis**: You need to test the connection directly from the affected machine using browser Developer Tools and a curl command to determine whether the network blocks the SSE connection.

**Resolution**: If the connection closes immediately or doesn't stream events, contact your IT department. They should:

- Add your data center-specific domain to the allowlist (for example, `api-prod.matrix.workato.com`)
- Allow SSE/streaming connections to this endpoint
- Ensure proxy settings permit long-lived HTTP connections
- Verify firewall rules don't terminate persistent connections

Refer to [Troubleshoot search and real-time chat issues](/en/agentic/workato-go/search#troubleshoot-search-and-real-time-chat-issues) for more information.

Why aren't my genies appearing in Workato GO?

Verify the following if genies aren't appearing in Workato GO after configuration:

- **The genie is started** (not just configured).
- **Workato GO is selected as the chat interface** when creating the genie.
- **[End user access is configured](/en/agentic/agent-studio/manage-users-and-access#user-group-genie-access)** with the correct user groups. Go to **AI Hub > Agent Studio**, select the genie, and go to **End user access**.
- **You've activated your [Workato Identity account](/en/workato-identity/account-management#set-up-your-workato-id)**. Check your email for the invitation and activate your end user access.
- **The genie is assigned to your user group**.

If genies still don't appear after completing setup, verify you're accessing the correct Workato GO URL for your account, not a demo or dev environment.

---
