---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/knowledge-base-management.md
description: >-
  Manage content across Workato GO and custom genie knowledge bases to search,
  organize, remove documents, and track storage footprints.
---

# Knowledge base management

Knowledge base management gives you a centralized view to monitor and manage the content stored across your [Workato GO](/en/agentic/workato-go) and custom knowledge bases.

![Knowledge base management](/assets/knowledge-base-management.C9YXiwoi.png)_Knowledge base management_

You can search, view, organize, and remove documents, track storage footprints, and manage file uploads to ensure your genie has access to accurate and up-to-date information. Storage footprint isn't supported for Workato GO.

![Knowledge base management file uploads](/assets/knowledge-management-uploads.dPiihVhh.png)_Knowledge base management file uploads_

Workato GO enforces its own permission model. Agent Studio uses this permission model to scope file visibility to your Workato GO identity and access level. This means you can only view content that you have permission to access in the connected data source. File visibility for third-party apps, such as Confluence, is also scoped to your identity permissions.

![Workato GO permissions are applied to knowledge bases](/assets/knowledge-base-workato-go-permissions.DFJFL3V2.png)_Workato GO permissions are applied to knowledge bases_

## Manage knowledge bases

Complete the following steps to access and manage your knowledge base data sources, including Workato GO sources:

1. Go to **Projects > Assets**.
   
2. Click **Knowledge bases**.
   
3. Select the knowledge base you plan to view or update.
   
4. Review the details panel for total storage size (unsupported for Workato GO), description, dependencies (how many genies use this knowledge base) and recipe or data source details.
   
   ![Knowledge base details panel](/assets/knowledge-base-details-panel.M07Ekbie.png)_Knowledge base details panel_
   
5. Click a source to view the individual source details.
   
   ![Knowledge source details](/assets/knowledge-source-details.BkjIxx8I.png)_Knowledge source details_
   
6. Optional. Select one or more source checkboxes and click **Remove documents** to remove documents from your knowledge base.
   
   ![Remove documents](/assets/remove-knowledge.7atbwQ2_.png)_Remove documents_
   

## More resources

- [Knowledge base configuration](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration)
- [Knowledge base document preparation](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#knowledge-base-document-preparation)
- [Knowledge base and database best practices](/en/agentic/agent-studio/knowledge-bases/knowledge-base-and-database-best-practices)
- [Design skills for databases](/en/agentic/skills/design-skills-for-databases)
