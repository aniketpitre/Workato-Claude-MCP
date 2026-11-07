---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/list-documents-advanced-filters.md
description: List documents with advanced filters in a knowledge base programmatically.
---

# Knowledge base by Workato connector - List documents advanced filters

The **List documents (advanced filters)** batch action returns documents from a recipe or direct-upload [knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) you specify with optional filtering and pagination. Use the filters to narrow the list by content type, metadata, or date, and page through large result sets with the page number. Filter metadata with a **data\_filters** JSON object to retrieve data that dedicated fields can't express, such as matching against a list of values, OR groups of conditions, or combining several conditions at once.

Refer to [Metadata filters](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/metadata-filters) for more information on advanced filters.

## Input

| Input field | Description |
| --- | --- |
| Knowledge base | Select the ID of the knowledge base. Only recipe-type knowledge bases can be selected. Workato GO sources aren't supported. The handle appears in the URL. |
| Page | The page number to retrieve. Starts at `1`. Defaults to `1`. |
| Page size | Results per page (1–100). Defaults to `50`. |
| Sort by | Add one row per sort field. Multiple rows are applied in order. |
| Include metadata | Use the option drop-down menu to determine whether metadata is included or not. |
| Data filters | Filter by document metadata using JSON. For example: exact match: `{"status":"active"}`. |

## Output

| Output field | Description |
| --- | --- |
| Documents | The list of documents that match the request. |
| Document ID (Documents) | The unique identifier of the document. |
| Title (Documents) | The document title. |
| Source URL (Documents) | The source URL of the document. |
| Content type (Documents) | The MIME type of the document. |
| Workspace email (Documents) | The email of the document owner, when available. |
| Created date (Documents) | The creation timestamp of the document. |
| Updated date (Documents) | The last-updated timestamp of the document. |
| Document content (Documents) | The document content. |
| Metadata (Documents) | The key-value metadata stored with the document. |
| List size (Documents) | The total number of documents returned on this page. |
| List index (Documents) | The index of the current item in the documents list. |
| Total count | The total number of documents that match the request, across all pages. |
| Current page | The page number of the returned results. |
| Page size | The page size used for the request. |
