---
url: 'https://docs.workato.com/en/recipes/connection-faqs.md'
description: >-
  Answers to common questions about Workato connections, including who can
  create them, how access works, and managing app instances.
---

# Connection FAQs

Get answers to frequently asked connection questions.

Who can create connections?

You must have the `Create Connections` privilege to create a connection. Refer to [Create connections](/en/connections#create-connections) for more information.

How does Workato access my connections?

Workato uses the app's authorization/authentication API to establish the connection, using one of the following methods:

- OAuth 2.0
- OAuth 1.0 (and variations)
- Basic authentication (username and password)
- API key or secret

The permissions granted to Workato usually correspond with those of the user authorizing the app. Refer to [Create connections](/en/connections#create-connections) for more information.

What data can Workato access in my connections?

Workato can only access the same data the user authorizing the connection has access to. For example, if you only have access to view accounts in Salesforce and you create a Salesforce connection in Workato, Workato is only able to view accounts. Refer to [Create connections](/en/connections#create-connections) for more information.

How do I manage multiple app instances within one recipe?

You may have [multiple instances of an app within a recipe](/en/connections#using-connections-in-recipes), for example, one for production and another for testing. If you have multiple instances of an app, multiple connections must be created in Workato. Each connection must authenticate to each instance of the app.

Most connectors only allow one connection per app, per recipe. If you plan to work with two separate instances of an app, you can use [secondary connectors](/en/features/secondary-connectors#secondary-connectors). Workato does not support secondary connectors for all connectors.

What are runtime user connections?

[Runtime user connections](/en/connections#using-connections-in-recipes) are available in Workbot recipes. They allow you to swap out connections when a recipe runs, so actions can be performed based on different credentials.

What should I do if I encounter connection errors?

App connections can become invalid and cause [connection errors](/en/connections#connection-errors). Common reasons for this include modified credentials and insufficient permissions. If you encounter a connection error, we recommend the following troubleshooting steps:

- Verify the authorizing user's permissions.
- Verify that the connection's credentials are correct.
- Re-authorize the connection if necessary.

What are custom OAuth profiles?

[Custom OAuth profiles](/en/custom-oauth-profiles) let you register and use your own OAuth applications when connecting to supported apps. This gives you control over scopes, security policies, branding on consent screens, and ownership of the OAuth credentials.

What connectors support custom OAuth profiles?

The following connectors support custom OAuth profiles:

- AirREGI
- Airtable
- Apttus
- Asana
- AscentERP
- Basecamp 2
- Bigtincan
- Bitbucket
- Box
- Bynder
- Chatter
- Cisco Webex Teams
- Citrix Podio
- Docusign
- Egnyte
- Eloqua
- Eventbrite
- everydayhero
- Excel
- Facebook
- Facebook Lead Ads
- Fairsail
- Feedly
- FinancialForce
- Force.com
- GitHub
- Gmail
- Gong.io
- Google Docs
- Google Drive
- Google Sheets
- GotoWebinar
- [HubSpot](/en/connectors/hubspot/custom-oauth)
- Infusionsoft
- Intercom
- Jira
- Jira Service Desk
- JobScience
- Kenandy
- Lightspeed Commerce
- Microsoft Dynamics 365
- Microsoft SharePoint
- Namely
- NationBuilder
- Nimble CRM
- OneDrive
- [Outlook](/en/connectors/outlook/custom-oauth)
- Outreach
- PlanGrid
- Propel
- QuickBooks Online
- Raiser's Edge NXT
- RingCentral
- Sage Live
- [Salesforce](/en/connectors/salesforce/custom-oauth)
- Salesforce CPQ
- [Salesforce (secondary)](/en/connectors/salesforce/custom-oauth)
- ServiceMax
- ServiceNow
- ServiceNow (secondary)
- Shopify
- [Slack](/en/custom-oauth-profiles/slack)
- [Slack (secondary)](/en/custom-oauth-profiles/slack)
- Smartsheet
- Stripe
- SurveyMonkey
- TaskRay
- TrackVia
- Trello
- TSheets
- Typeform
- Veeva CRM
- Vlocity
- Workato Genie MS Teams
- Workato Genie Slack
- [Workbot for Microsoft Teams](/en/workbot-for-teams/guides/creating-enterprise-workbot)
- [Workbot for Slack](/en/workbot/workbot-custom-bots)
- WordPress.com
- Wrike
- Wrike (secondary)
- Xero
- Xero Practice Manager
- Zenefits
- Zoho CRM
- Zoho Invoice
- [Zoom](/en/connectors/zoom#create-a-custom-oauth-profile)
- Zuora for Salesforce

---
