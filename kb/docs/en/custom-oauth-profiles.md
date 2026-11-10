---
url: 'https://docs.workato.com/en/custom-oauth-profiles.md'
description: >-
  Use custom OAuth profiles to connect Workato with your own OAuth apps for
  greater control over scopes, security, branding, and authentication.
---

# Custom OAuth profiles

[Custom OAuth profiles](https://app.workato.com/custom_oauth_keys) let you use your own OAuth applications when connecting Workato to third-party services. This gives you greater control over scopes, security, branding, and how authentication is managed.

You can create a custom OAuth profile by going to **Tools > Custom OAuth profiles** and clicking **\+ New custom profile**. This process typically involves creating the OAuth app in the vendor's developer console and entering the client ID and secret in Workato.

> **FEATURE AVAILABILITY**
> 
> The Custom OAuth profiles feature is included in specific pricing plans. Refer to your pricing plan and contract to learn more.
> 
> Additionally, Customers using the China data center must configure [Custom OAuth profiles](/en/custom-oauth-profiles) before establishing connections to connectors that support OAuth 2.0 authentication. Custom OAuth profile configuration can require the following customer-provided credentials:
> 
> - Client IDs
> - Client secrets
> - OAuth 2.0 endpoint URLs

## Key benefits

Custom OAuth profiles provide the following key benefits:

- **Granular scope control**: Request only the permissions (scopes) your integration needs, adhering to the principle of least privilege.
- **Enhanced security and compliance**: Manage your own OAuth app, including client secret rotation, auditing, and alignment with your organization's policies.
- **Custom branding**: Display your organization's branding on OAuth consent screens.
- **Access isolation**: Deploy multiple custom apps to segment access for different teams, environments, or customers.
- **Vendor compliance**: Meet requirements from vendors that mandate using your own registered app.

Custom OAuth profiles also enable you to install multiple custom Workbots onto a single Slack workspace, each with distinct identities, permissions, and branding.

## Supported connectors

You can create custom OAuth profiles for the following connectors:

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
- Monday.com
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
