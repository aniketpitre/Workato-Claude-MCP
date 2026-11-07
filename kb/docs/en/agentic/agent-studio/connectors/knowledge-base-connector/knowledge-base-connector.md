---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/knowledge-base-connector/knowledge-base-connector.md
description: Manage documents stored within knowledge bases directly within your recipe.
---

# Knowledge base by Workato connector

The Knowledge base by Workato connector lets you manage knowledge base documents directly within a recipe stored in a Workato [knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases). This enables you to sync documents from any source into a knowledge base so genies can retrieve them.

Use it to programmatically insert, update, delete, list, and search documents so the context your genies retrieve stays current with your source systems.

The connector manages the **content within** knowledge bases. It doesn't create, delete, or configure the knowledge bases themselves. Refer to [Knowledge base management](/en/agentic/agent-studio/knowledge-bases/knowledge-base-management) for more information.

> **CONNECTOR ACCESS**
> 
> The Knowledge base by Workato connector is available to customers on plans with [Agent Studio](/en/agentic/agent-studio) enabled.

## Connection setup

The Knowledge base by Workato connector is a built-in connector. It doesn't require authentication or connection setup. The connector automatically scoped to your workspace when you add it to a recipe.

> **MIGRATION FROM THE STORE KNOWLEDGE ACTION**
> 
> Knowledge base by Workato replaces the Workato Genie connector's [Store knowledge](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/store-knowledge) action. The Store knowledge action is deprecated but continues to run in existing recipes. No immediate action is required for recipes running this action. Refer to [Migrate from the Store knowledge action](#migrate-from-the-store-knowledge-action) for more information.

## Supported knowledge bases

Knowledge base by Workato actions runs in knowledge bases with content sourced from recipes or direct uploads.

Knowledge bases populated by [Workato GO data sources](/en/agentic/agent-studio/knowledge-bases/data-ingestion#two-ingestion-paths), such as, Google Drive, Confluence, SharePoint, and Notion, are managed separately and can't be modified with this connector. This preserves the permission-aware retrieval those data sources provide.

Each action identifies a knowledge base by its handle, which appears in the knowledge base URL.

## Documents

A document is the unit of content stored in a knowledge base. Each document includes the following fields:

| Field | Description |
| --- | --- |
| Document ID | A unique identifier from your source system. Knowledge base by Workato uses this ID to match documents on upsert. This lets the action update an existing document instead of creating a duplicate. |
| Title | The document title. |
| Body | The document content. For binary file types, provide the file content. |
| Content type | The MIME type of the document, such as `text/plain` or `application/pdf`. The service detects the type from the content if you leave this blank. |
| Source URL | The source URL. Genies use this URL to cite the document when presenting information to users. |
| Metadata | Free-form key-value metadata. Include `lang: en` to improve text extraction accuracy for English-language documents. Use Metadata to filter results in the **List documents** and **Search documents** actions. |
| Created date | The creation timestamp from your source system. |
| Updated date | The last-updated timestamp from your source system. |

### Supported file types

The Knowledge base by Workato supports plaintext and accepts the following binary file types and extracts their text content server-side before indexing:

- PDF: `application/pdf`
- Microsoft Word: `.docx`
- Microsoft PowerPoint: `.pptx`

The service respects the `Content type` you provide. The service inspects the content to detect the correct content type if you leave it blank. Template and macro-enabled Office formats, such as `.dotx`, `.pptm`, `.xlsm`, and legacy binary Office formats, such as , `.doc`, `.xls`, aren't supported and are rejected.

## Actions

The Knowledge base by Workato connector supports the following recipe actions:

- [Delete document](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/delete-document)
- [List documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/list-documents)
- [Search documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/search-documents)
- [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents)

## Migrate from the Store knowledge action

Knowledge base by Workato breaks down the Workato Genie connector's [Store knowledge](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/store-knowledge) action into a dedicated set of document actions. The mapping is one-to-one for document storage:

| Workato Genie connector | Knowledge base by Workato |
| --- | --- |
| Store knowledge | [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents) |

The following workflows apply when you migrate:

- **Existing recipes are unaffected**: The **Store knowledge** action is deprecated, not removed. Recipes that already use this recipe continue to run unchanged.
- **New knowledge base recipes use this connector**: The [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents) action is selected automatically when you create a recipe from the knowledge base view.
- **The input fields map directly**: The document fields in the **Store knowledge** action, including document ID, title, body, content type, URL, metadata, created at, and updated at, correspond to the same fields in the **Upsert documents** action.
- **Dependencies are visible in the knowledge base view**: After you migrate, the knowledge base view surfaces the recipes that manage its documents through Knowledge base by Workato.

## Quotas

| Limit | Value |
| --- | --- |
| Documents per Upsert documents call | 100 |
| Default page size (List and Search documents) | 50 |
| Maximum page size (List and Search documents) | 100 |
| Rate limit | 100 requests per action, per environment, per minute |

The connector applies backoff and retries when you exceed the rate limit. Each knowledge base selected in the [Search documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/search-documents) action call is queried as a separate request. This means that searching multiple knowledge bases at once consumes more of your rate-limit budget.
