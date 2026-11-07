---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents.md
description: Upsert documents in a knowledge base programmatically.
---

# Knowledge base by Workato connector - Upsert documents

The **Upsert documents** action inserts or updates documents in a [knowledge base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases). It runs as a batch action, processing up to 100 documents per run.

> The maximum supported file size is 100MB, including batch files. An additional 16MB limit is applied to each file's raw text as files pass through the Workato indexing and extraction engine.

The action matches documents by **Document ID**. The action updates an existing document with the same ID or creates a new document if an existing document ID isn't found. Reusing an ID updates the existing document, so re-running the action overwrites the previous version rather than creating duplicates.

Use this action to build [knowledge base recipes](/en/agentic/agent-studio/knowledge-bases/knowledge-base-recipes) that sync and update information from your connected applications. Refer to [Knowledge base data ingestion](/en/agentic/agent-studio/knowledge-bases/data-ingestion) for ingestion best practices.

## Input

| Input field | Description |
| --- | --- |
| Knowledge base | Select the knowledge base to store the documents in. Only recipe-type knowledge bases are supported. Workato GO sources aren't supported. The handle appears in the URL. |
| Documents source list | Specify a list datapill. Each item in the list represents one document to upsert. Up to 100 documents per run. |
| Document ID (Documents) | Unique ID in the source system. Reusing an ID updates the existing document. |
| Title (Documents) | The document title. |
| Body (Documents) | The document content. Required unless you provide binary file content with a binary content type. |
| Source URL (Documents) | The URL of the document in the source system. Genies use this URL to cite sources when presenting information to users. |
| Content type (Documents) | The MIME type of the document, such as `text/plain` or `application/pdf`. For binary formats (PDF, `.docx`, `.pptx`), the service extracts text server-side. Leave blank to let the service detect the type from the content. |
| Metadata (Documents) | Additional key-value metadata for the document. Include `lang: en` to improve text extraction accuracy for English-language documents. |
| Created date (Documents) | The creation timestamp of the document in the source system. |
| Updated date (Documents) | The last-updated timestamp of the document in the source system. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether all documents were sent to the ingestion pipeline successfully. |
| Failed documents | A list of documents that couldn't be sent to the ingestion pipeline. Empty when all documents succeed. Common reasons a document fails include an undetectable or invalid content type (MIME) and a blank body on a text-based document. |
| Document ID (Failed documents) | The ID of the document that failed. |
| Title (Failed documents) | The title of the document that failed. |
| List size (Failed documents) | The total number of failed documents. |
| List index (Failed documents) | The index of the current item in the failed documents list. |
