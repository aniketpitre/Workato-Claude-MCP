---
url: 'https://docs.workato.com/en/connectors/bynder.md'
description: >-
  The Bynder connector lets you automate digital asset workflows: upload,
  download, search, and update assets and records, and trigger on new or updated
  assets.
---

# Bynder

[Bynder](https://www.bynder.com/en/) is a digital asset management platform that enables teams to collaborate in the cloud, get content to market faster, and maximize the impact of marketing assets.

## API version

The Bynder connector uses [Bynder REST API v4](https://bynder.docs.apiary.io/#reference).

## How to connect to Bynder on Workato

### Bynder connection

The Bynder connector uses OAuth 2.0 to authenticate with Bynder.

- **Connection name**
  
  Give this Bynder connection a unique name that identifies which Bynder instance it is connected to.
  
- **Domain**
  
  Enter your Bynder domain as found in your Bynder URL. If your Bynder url is [https://acme.getbynder.com](https://acme.getbynder.com) , then domain is acme.getbynder.com
  
- **Scopes**
  
  Enter the scope for which the user has permissions for. The default scopes can be overridden in the advanced settings. Refer to the Bynder [OAuth scopes](https://bynder.docs.apiary.io/#introduction/oauth-scopes) documentation for the full list of scopes and the actions that require them.
  
  The following scopes are required to be included :
  
  - "offline",
  - "meta.assetbank:read"
  
  The other scopes that are selected by default includes :
  
  - "asset.usage:read",
  - "asset:read",
  - "asset:write",
  - "asset.usage:write",
  - "collection:read",
  - "collection:write",
  - "workflow.campaign:read",
  - "workflow.campaign:write",
  - "workflow.group:read",
  - "workflow.group:write",
  - "workflow.job:read",
  - "workflow.job:write",
  - "workflow.preset:read",
  - "meta.workflow:read

![Bynder Connection 2](/assets/bynder_connection_2.CqCOP_G8.png)

Click on connect and a Bynder dialog box will pop-up, requesting your Bynder Account credentials, and granting access to Workato.

### Roles and permissions required to connect

Bynder users who can log in to Bynder can connect to Bynder from Workato. The user will have the same [user permissions](https://support.bynder.com/hc/en-us/articles/360013936559-Types-of-user-profiles-in-Bynder) on Workato as in Bynder. This means that they will have the same capabilities to view,update, delete, upload, and download assets as per their respective permissions on the Bynder platform. Bynder categorizes users into three groups: Light, Regular and Heavy users. Regular user role is sufficient to use most of the actions in the Bynder connector.

## Working with Bynder connector

### Terminology

The terminology for Bynder can be found below.

- **Assets**
  
  Any type of digital files including images, movies, music files, and PDF documents. Refer to the Bynder [Supported file formats](https://support.bynder.com/hc/en-us/articles/360013936359-Supported-File-Formats) documentation for the full list of supported file formats.
  
- **Collections**
  
  Collections are assets that belong together or that are grouped together.
  
- **Tags**
  
  You can add tags manually, or get Bynder to tag assets for you using AI-based automated tags. Shortly after upload, the automated tags will be available under the Automated Tags drop-down in the asset detail screen. Refer to the Bynder [Asset tagging](https://support.bynder.com/hc/en-us/articles/360013869900-Asset-tagging) documentation for more information on tag management.
  
- **Metaproperties**
  
  Campaign metaproperties are recurring fields that can be added to specific campaign presets.
  
- **Metaproperty option**
  
  Options that belong to specific metaproperties. For example, if you have a Country metaproperty, you can add countries as options to this metaproperty.

---
