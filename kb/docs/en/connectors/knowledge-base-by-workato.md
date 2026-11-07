---
url: 'https://docs.workato.com/en/connectors/knowledge-base-by-workato.md'
description: >-
  Manage documents in Workato knowledge bases directly from a recipe. Upsert,
  delete, list, and search documents to keep your genies' context current.
---

# Knowledge base by Workato

The Knowledge base by Workato connector gives builders a recipe-native way to manage the documents inside a Workato [knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases). Use it to programmatically insert, update, delete, list, and search documents so the context your genies retrieve stays current with your source systems.

The connector manages the **content within** knowledge bases. It doesn't create, delete, or configure the knowledge bases themselves. Refer to [Knowledge base management](/en/agentic/agent-studio/knowledge-bases/knowledge-base-management) for those tasks.

> **FEATURE AVAILABILITY**
> 
> Knowledge base by Workato is available to customers on plans with [Agent Studio](/en/agentic/agent-studio) enabled, in the US, EU, AU, SG, JP, IL, KR, and UK data centers. The connector operates on the same knowledge bases as your genies and respects data residency requirements where possible.
> 
> Contact your Customer Success representative if you're interested in Agent Studio or require additional information.

> **MIGRATING FROM THE STORE KNOWLEDGE ACTION**
> 
> Knowledge base by Workato replaces the Workato Genie connector's [Store knowledge](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/store-knowledge) action. The Store knowledge action is deprecated but continues to run in existing recipes — no immediate action is required. Refer to [Migrate from the Store knowledge action](#migrate-from-the-store-knowledge-action) for the mapping.

## Connection setup

Knowledge base by Workato is a built-in, first-party connector. It authenticates against Workato's own search service using workspace-level credentials, so it doesn't require external authentication or a connection setup. When you add the connector to a recipe, it's automatically scoped to your workspace.

## Supported knowledge bases

Knowledge base by Workato actions operate on knowledge bases whose content comes from **recipes or direct uploads**.

Knowledge bases populated by [Workato GO data sources](/en/agentic/agent-studio/knowledge-bases/data-ingestion#two-ingestion-paths) (Matrix-connected sources such as Google Drive, Confluence, SharePoint, and Notion) are managed separately and **can't** be modified with this connector. This preserves the permission-aware retrieval those data sources provide.

Each action identifies a knowledge base by its **handle**, which appears in the knowledge base URL. In the recipe editor, select a knowledge base from the list.

## Documents

A document is the unit of content stored in a knowledge base. Each document carries the following fields:

| Field | Description |
| --- | --- |
| Document ID | A unique identifier from your source system. Knowledge base by Workato uses this ID to match documents on upsert, so the same ID updates an existing document instead of creating a duplicate. |
| Title | The document title. |
| Body | The document content. For binary file types, provide the file content. |
| Content type | The MIME type of the document, such as `text/plain` or `application/pdf`. If you leave this blank, the service detects the type from the content. |
| Source URL | The source URL. Genies use this URL to cite the document when presenting information to users. |
| Metadata | Free-form key-value metadata. Include `lang: en` to improve text extraction accuracy for English-language documents. Metadata can also be used to filter results in the List and Search actions. |
| Created date | The creation timestamp from your source system. |
| Updated date | The last-updated timestamp from your source system. |

### Supported file types

In addition to plain text, Knowledge base by Workato accepts the following binary file types and extracts their text content server-side before indexing:

- PDF (`application/pdf`)
- Microsoft Word (`.docx`)
- Microsoft PowerPoint (`.pptx`)

If you provide a `Content type`, the service respects it. If you leave it blank, the service inspects the content to detect the correct type. Template and macro-enabled Office formats (for example, `.dotx`, `.pptm`, `.xlsm`) and legacy binary Office formats (for example, `.doc`, `.xls`) aren't supported and are rejected.

## Actions

The Knowledge base by Workato connector supports the following recipe actions:

- [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents) — Insert or update a batch of documents in a knowledge base.
- [Delete document](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/delete-document) — Remove a document from a knowledge base by ID.
- [List documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/list-documents) — Retrieve a paginated list of documents in a knowledge base, with optional filters.
- [Search documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/search-documents) — Run a natural-language or keyword search across one or more knowledge bases.

## Migrate from the Store knowledge action

Knowledge base by Workato carves the Workato Genie connector's [Store knowledge](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/store-knowledge) action into a dedicated set of document actions. The mapping is one-to-one for document storage:

| Workato Genie connector | Knowledge base by Workato |
| --- | --- |
| Store knowledge | [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents) |

The following points apply when you migrate:

- **Existing recipes are unaffected.** The Store knowledge action is deprecated, not removed. Recipes that already use it continue to run unchanged.
- **New knowledge base recipes use this connector.** When you create a recipe from the knowledge base view, the [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents) action is selected automatically.
- **The input fields map directly.** The document fields in Store knowledge (document ID, title, body, content type, URL, metadata, created at, updated at) correspond to the same fields in Upsert documents.
- **Dependencies are visible in the knowledge base view.** After you migrate, the knowledge base view surfaces the recipes that manage its documents through Knowledge base by Workato.

## Quotas

| Limit | Value |
| --- | --- |
| Documents per Upsert documents call | 100 |
| Default page size (List and Search documents) | 50 |
| Maximum page size (List and Search documents) | 100 |
| Rate limit | 100 requests per action, per environment, per minute |

When you exceed the rate limit, the connector applies backoff and retries. Each knowledge base selected in a [Search documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/search-documents) call is queried as a separate request, so searching many knowledge bases at once consumes more of your rate-limit budget.

---
