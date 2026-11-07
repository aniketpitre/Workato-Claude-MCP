---
url: 'https://docs.workato.com/en/datacenter/cn-data-center.md'
description: >-
  Feature availability and operational considerations for Workato's China (CN)
  data center, hosted on AWS China (Ningxia) Region.
---

# China data center

The Workato China data center is hosted on AWS China (Ningxia) Region and operated by Workato (Beijing) Technology Co., Ltd. (京ICP备2026009801号), in compliance with local regulatory requirements. Feature availability and operational behavior may differ from other Workato regions.

## Feature availability

The following feature limitations apply to both multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) workspaces in the China region.

### AI and Agentic features

AI and Agentic features aren't available in the China data center. This includes the following features:

- Model Context Protocol (MCP)
- Workato GO
- Agent Studio
- Copilots
- AIRO
- IDP by Workato
- AI by Workato

### API platform custom domains

API platform custom domains aren't supported in the China data center.

### Community library

The Community library isn't accessible to workspaces in the China data center.

Customers using the China data center must build custom solutions or work with the Professional Services team to develop recipe templates, custom connectors, and best practices. [Recipe lifecycle management (RLCM)](/en/recipe-development-lifecycle#recipe-lifecycle-management) features are supported for the China data center. This means that users can deploy assets to higher environments and import or export `.zip` files to their workspaces.

### Connector availability

The following connectors aren't available to workspaces in the China data center:

- Dropbox
- Facebook
- Facebook Lead Ads
- GitHub
- Gmail
- Google BigQuery
- Google Calendar
- Google Cloud Storage
- Google Contacts
- Google Dialogflow
- Google Drive
- Google People
- Google Sheets
- Google Speech to Text
- Google Text to Speech
- Google Translate
- Google Vision
- Google Workspace
- Instagram
- LinkedIn
- MailChimp
- OneDrive
- OpenAI
- Slack
- Slack secondary
- Watson Tone Analyzer
- Workbot for Slack
- X

### OAuth 2.0 connectivity

OAuth 2.0 connectivity requires additional configuration for workspaces using the China data center.

Customers using the China data center must configure [Custom OAuth profiles](/en/custom-oauth-profiles) before establishing connections to connectors that support OAuth 2.0 authentication. Custom OAuth profiles can require the following customer-provided credentials:

- Client IDs
- Client secrets
- OAuth 2.0 endpoint URLs

### Email by Workato

[Email by Workato](/en/connectors/email-by-workato#email-by-workato) connector capabilities for workspaces in the China data center are supported through the following channels only:

- Custom SMTP configuration.
- Out-of-the-box Workato notifications. This includes error notifications, billing and usage alerts, and platform communications such as workspace sign-ups and password resets.

### Platform CLI

The Platform CLI isn't available to workspaces in the China data center.

### Workflow apps

Workflow apps aren't available to workspaces in the China data center.

## Product support

Customers using the China data center must submit support tickets through the Workato Global Freshdesk instance to access product support.

---
