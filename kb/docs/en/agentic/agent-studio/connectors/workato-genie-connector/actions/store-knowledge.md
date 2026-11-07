---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/workato-genie-connector/actions/store-knowledge.md
description: Store documents in a knowledge base as part of a knowledge base recipe.
---

# Workato Genie connector - Store knowledge action

The **Store knowledge** action stores documents in a knowledge base. It runs as a batch action, processing all documents in the source list in a single operation.

Use this action to build knowledge base recipes that sync and update information from connected applications. Refer to [Knowledge base recipes](/en/agentic/agent-studio/knowledge-bases/knowledge-base-recipes) for full setup steps and [Knowledge base data ingestion](/en/agentic/agent-studio/knowledge-bases/data-ingestion) for ingestion best practices.

> **DEPRECATED**
> 
> The **Store knowledge** action is deprecated. It's replaced by the [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents) action in [Knowledge base by Workato](/en/agentic/agent-studio/connectors/knowledge-base-connector/knowledge-base-connector), a dedicated connector for managing documents in a knowledge base.
> 
> Existing recipes that use the **Store knowledge** action continue to run unchanged. No immediate action is required. New knowledge base recipes use Knowledge base by Workato by default. Refer to [Migrate from the Store knowledge action](/en/agentic/agent-studio/connectors/knowledge-base-connector/knowledge-base-connector#migrate-from-the-store-knowledge-action) for the field mapping.

## Input

| Input field | Description |
| --- | --- |
| Knowledge base | Select the knowledge base to store the documents in. |
| Documents source list | Specify a list datapill. Each item in the list represents one document to store. |
| Document ID (Documents source list) | Enter the external ID of the document in the source system. A document with a matching ID updates the existing entry instead of creating a duplicate. |
| Document title (Documents source list) | Enter the title of the document. |
| Document body (Documents source list) | Enter the document content. |
| Content type (Documents source list) | Select the content type of the document: **PDF**, **Microsoft Word (.docx)**, **Microsoft Excel (.xlsx)**, or **Microsoft PowerPoint (.pptx)**. |
| Document URL (Documents source list) | Enter the URL of the document in the source system. Genies use this URL to cite sources when presenting information to users. |
| Document metadata (Documents source list) | Enter additional metadata for the document. Include `lang: en` to improve text extraction accuracy for English-language documents. |
| Created at (Documents source list) | Enter the creation timestamp of the document in the source system. |
| Updated at (Documents source list) | Enter the last updated timestamp of the document in the source system. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether all documents were stored successfully. |
| Failed documents | A list of documents that failed to store. |
| Title (Failed documents) | The title of the document that failed to store. |
| List size (Failed documents) | The total number of failed documents. |
| List index (Failed documents) | The index of the current item in the failed documents list. |
