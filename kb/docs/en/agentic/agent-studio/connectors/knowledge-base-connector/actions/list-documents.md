---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/list-documents.md
description: List documents in a knowledge base programmatically.
---

# Knowledge base by Workato connector - List documents

The **List documents** action returns documents from a recipe or direct-upload [knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) you specify with optional filtering and pagination. Use the filters to narrow the list by content type, metadata, or date, and page through large result sets with the page number.

Use this action to audit, reconcile, or report on the documents in a knowledge base from within a recipe.

## Input

| Input field | Description |
| --- | --- |
| Knowledge base ID | Select the ID of the knowledge base. Only recipe-type knowledge bases can be selected. Workato GO sources aren't supported. The handle appears in the URL. |
| Page | The page number to retrieve. Starts at `1`. Defaults to `1`. |
| Page size | Results per page (1–100). Defaults to `50`. |
| Content type | Filter by MIME type (stored in document metadata as `mime_type`). |
| Metadata filters | Optional key-value pairs stored with the document. For example, `lang` or source-system fields. |
| Created after | Return only documents created after this date. |
| Created before | Return only documents created before this date. |
| Updated after | Return only documents updated after this date. |
| Updated before | Return only documents updated before this date. |

## Output

| Output field | Description |
| --- | --- |
| Documents | The list of documents that match the request. |
| Document ID (Documents) | The unique identifier of the document. |
| Title (Documents) | The document title. |
| Source URL (Documents) | The source URL of the document. |
| Content type (Documents) | The MIME type of the document. |
| Owner email (Documents) | The email of the document owner, when available. |
| Created date (Documents) | The creation timestamp of the document. |
| Updated date (Documents) | The last-updated timestamp of the document. |
| Document content (Documents) | The document content. |
| Metadata (Documents) | The key-value metadata stored with the document. |
| List size (Documents) | The total number of documents returned on this page. |
| List index (Documents) | The index of the current item in the documents list. |
| Total count | The total number of documents that match the request, across all pages. |
| Current page | The page number of the returned results. |
| Page size | The page size used for the request. |
