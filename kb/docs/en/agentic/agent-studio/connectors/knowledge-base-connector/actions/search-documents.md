---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/search-documents.md
description: Search documents in a knowledge base programmatically.
---

# Knowledge base by Workato connector - Search documents

The **Search documents** action searches the knowledge base you specify by natural language or keyword search query.

The **Search documents** action runs a natural-language or keyword search across one or more [knowledge bases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) and returns the matching documents. Use the filters to narrow results by content type, metadata, or date.

You can select multiple knowledge bases in a single call. Each selected knowledge base is queried as a separate request. The request volume counted against your [rate limit](/en/connectors/knowledge-base-by-workato#limits) increases when you select more knowledge bases.

## Input

| Input field | Description |
| --- | --- |
| Knowledge base | Select the knowledge base you plan to search. Only recipe-type knowledge bases can be selected. Workato GO sources aren't supported. The handle appears in the URL. |
| Query | The search query, as natural language or keywords. |
| Page | The page number to retrieve. Starts at `1`. Defaults to `1`. |
| Page size | Results per page (1–100). Defaults to `50`. |
| Content type | Filter by MIME type (stored in document metadata as `mime_type`). |
| Metadata filters | Optional key-value pairs stored with the document. For example, `lang` or source-system fields. Applied to all selected knowledge bases. |
| Created after | Return only documents created after this date. |
| Created before | Return only documents created before this date. |
| Updated after | Return only documents updated after this date. |
| Updated before | Return only documents updated before this date. |

## Output

| Output field | Description |
| --- | --- |
| Documents | The list of documents that match the search. |
| Document ID | The ID of the document that contained the natural language search query or keyword you provided. For example: `br689aec2ie03218te706l76y157nn12` |
| Title | The title of the document returned in the search. |
| Source URL (Documents) | The source URL of the document. |
| Content type | The content type of the document returned in the search. For example: `application/vnd.openxmlformats-officedocument.presentationml.presentation` |
| Workspace email | The email address of the user who owns each document returned in the search. |
| Created date | The date each document returned in the search was created. |
| Updated date | The date each document returned in the search was updated, if any. |
| Document content | The content that matches the search query. |
| Relevance score | The relevance score of the data returned. For example: `0.87`. |
| Metadata (Documents) | The key-value metadata stored with the document. |
| Document type (Documents) | The type of the returned item, for example `document`. |
| List size (Documents) | The total number of documents returned on this page. |
| List index (Documents) | The index of the current item in the documents list. |
| Total count | The total number of documents that match the search, across all pages. |
| Current page | The page number of the returned results. |
| Page size | The page size. |
