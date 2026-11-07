---
url: 'https://docs.workato.com/en/features/api-management.md'
description: >-
  Workato API Platform is a full-lifecycle API management platform to build,
  maintain, monitor, and consume APIs entirely in the cloud.
---

# API Platform

Workato API Platform is a full-lifecycle API management platform that lets you build, maintain, and consume APIs completely in the cloud.

Monitor your APIs with the API dashboard. Control access to your endpoints with clients and access profiles. Make it your own API with a full suite of customizations.

Develop and release APIs seamlessly between development, testing, and production with [recipe lifecycle management](/en/recipe-development-lifecycle).

> **API Platform documentation**
> 
> Refer to [API Platform](/en/api-management) for more information.

---

---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration.md
description: >-
  Configure a genie knowledge base with detailed descriptions and document
  preparation to improve retrieval accuracy and response quality.
---

# Knowledge base configuration

The knowledge base component serves as your genie's memory. You must configure your knowledge base correctly to ensure optimal performance. An accurate and detailed [knowledge base description](#knowledge-base-description) improves genie information retrieval. You can also improve knowledge base information retrieval through [document preparation](#knowledge-base-document-preparation).

## Knowledge base description

You must provide a detailed description of each knowledge base you create. Accurate descriptions help your genie determine the scope and relevance of the information, which improves response accuracy and contextual relevance.

## Knowledge base document preparation

Knowledge bases receive all data and associated metadata from documents. Poorly prepared documents degrade retrieval quality. Your genie may return irrelevant content, miss key information, or surface text with formatting noise.

Unprepared documents typically result in the following genie retrieval behavior:

- Fails to find the correct document
- Returns the correct document but with missing information
- Fails to retrieve relevant information
- Returns long documents that lack context or cut off mid-thought

For example, you upload a 50-page product manual as a single PDF. A user asks `What's the return policy?`. The genie retrieves a section from the middle of page 23 that starts mid-sentence and includes header and footer artifacts, missing the actual policy statement on page 12.

This happens because Workato knowledge bases use 8,000-character chunks with no overlap. The system finds the 10 most relevant documents, then returns chunks from within those documents. The chunks that get returned may lack context or contain noise that degrades response quality if your content isn't structured for the system retrieval pattern.

Document preparation is most important in the following situations:

- Documents are long with more than 10,000 characters that are automatically chunked.
- Content contains formatting or structural elements that interfere with information retrieval.
- Source content contains structured data, such as JSON or CSV that must be made human-readable.
- Retrieval quality is critical to your use case.
- Content originates from apps using APIs.

### Document preparation best practices

Document preparation has the following general best practices:

- Keep documents focused on one topic per document to retrieve information more accurately and quickly than large documents that cover multiple topics.
- Front-load key information by placing the most important content in the first 2,000 characters to increase the likelihood that the content is included in the retrieved chunks.
- Use clear, descriptive titles to improve semantic matching. For example: `Q3 2024 Return Policy - Electronics` returns better results than `Policy_v3_final.pdf`.
- Test content retrieval after ingestion with questions that your users will ask and further edit your documents if information retrieval under performs.
- Begin document preparation on a small scale with 5 to 10 well-prepared documents before bulk uploading hundreds to refine your process.

### Prepare PDFs and structured documents

You must pre-process documents before ingestion to create clean, self-contained chunks that can be easily retrieved. Every chunk should make sense as a standalone item and contain content that the agent can use directly in a response.

Complete the following steps to prepare your document for ingestion in a Workato knowledge base:

1. Review the document content and remove formatting artifacts, such as tags or decorative lines.
   
2. Break your content into 8k chunks of information at the following points:
   
   - **H1/H2/H3 headings**: Break each major section into its own chunk.
   - **Numbered sections**: Break each numbered section, such as 1.0, 2.0, into its own chunk.
   - **Line breaks**: Find line breaks to determine where content can be broken into chunks. Remove line breaks before document ingestion.
3. Add metadata and append context to section headers for each chunk, such as `From [Document Name] - [Section Title]:`, to improve semantic matching to improve context.
   
4. Remove excessive whitespace.
   
5. Remove line breaks.
   
6. [Test your genie](/en/agentic/agent-studio/test-genie#agent-studio-test-mode) to verify that expected questions retrieve the correct chunks.
   

### Prepare HTML and web content

You must pre-process HTML and web content before ingestion to create clean, self-contained chunks that can be easily retrieved.

Complete the following steps to prepare your HTML or web content for ingestion in a Workato knowledge base:

1. Remove all HTML tags from the content.
   
2. Remove navigation elements, such as sidebars and tables of content.
   
3. Preserve paragraph structure as plain text.
   
4. Ensure your headings use plain text markers. For example: `## Section Name`.
   

### Prepare JSON and API application data

You must pre-process JSON and API application data before ingestion to create clean, self-contained chunks that can be easily retrieved.

> **KNOWLEDGE BASES AND DATABASES HAVE DIFFERENT USE CASES**
> 
> Use a knowledge base if you plan to use semantic search, such as `Find similar support tickets` or `What issues have we seen like this?`. Don't use a knowledge base if you plan to pull structured data from apps, such as tickets, CRM records, or orders, or if you plan to query by filters, get counts, or retrieve comprehensive lists. Workato recommends that you use a database for these scenarios. Refer to [Knowledge bases versus databases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases-and-databases) for more information.

Complete the following steps to prepare your JSON and API data for ingestion in a Workato knowledge base:

1. Transform raw JSON into readable prose. Don't upload raw JSON. For example:
   
   **Raw JSON**
   
   ```json
   {"ticket_id": "12345", "status": "open", "customer": "Acme Corp", "issue": "Login timeout", "created": "2024-01-15"}
   ```
   
   **Prose**
   
   ```bash
   Support Ticket #12345 for Acme Corp - Login timeout issue
   Status: Open | Created: January 15, 2024
   
   Customer reported experiencing timeout errors when attempting to log in to the portal. Issue occurs intermittently, primarily during morning hours.
   ```
   
2. Ensure that you haven't combined multiple tickets or cases into a single document. One record = one document.
   
3. Add context to each record's prose to ensure that it contains relevant information as a standalone document.
   

### Prepare call transcripts and meeting notes

You must pre-process call transcripts and meeting notes before ingestion to create clean, self-contained chunks that can be easily retrieved. Transcripts require special consideration because of conversational context. For example, splitting content by individual speaker loses the question-answer relationship.

Transcripts and meeting notes have the following best practices guidelines:

- Don't upload raw transcripts.
- Don't allow 8k auto-chunking to split content arbitrarily.
- Don't split content by individual speaker as this loses conversational flow.
- Don't include filler content, such as greetings, hold music notes, or small talk that waste chunk space.

Complete one of the following approaches based on your use case to prepare your call transcripts and meeting notes for ingestion in a Workato knowledge base:

#### Conversation turn windows

This approach is recommended for support calls or other question-and-answer conversations with short exchanges.

Complete the following steps to prepare your call transcripts and meeting notes for ingestion in a Workato knowledge base with a conversation turn windows approach:

1. Group 5 to 7 consecutive speaker turns into each chunk.
   
2. Keep questions and answers together in the same chunk.
   
3. Add a header to your chunks. For example: `Call with [Customer] on [Date] - Topic: [Subject]`.
   

#### Topic-based segments

This approach is recommended for longer discussions, strategy calls, or meetings that cover multiple subjects.

Complete the following steps to prepare your call transcripts and meeting notes for ingestion in a Workato knowledge base with a topic-based segment approach:

1. Split content into chunks when the conversation shifts topics rather than when speakers change.
   
2. Ensure that each chunk covers one complete topic thread.
   
3. Perform a manual review or keyword detection search to identify conversational transitions where a new chunk starts.
   

#### Summary documents

This approach is recommended for large transcript volumes or when verbatim quotes aren't critical. Summaries often retrieve better than fragmented transcript chunks.

Complete the following steps to prepare your call transcripts and meeting notes for ingestion in a Workato knowledge base with a document summary approach:

1. Create a 500 to 1,000-word summary for each call. You can use AI to streamline this process or use the summary generated by some sources apps, such as Gong. You must include key decisions, action items, main topics discussed, and participant names.
   
2. Optional. Add a [skill](/en/agentic/agent-studio/create-a-genie#create-skills) that retrieves the call transcript from the source by ID.
   

#### Summary and key exchanges

This hybrid approach is recommended for general searches and searches for specific quotes.

Complete the following steps to prepare your call transcripts and meeting notes for ingestion in a Workato knowledge base with a summary and key exchanges approach:

1. Upload a summary document for general retrieval.
   
2. Create and upload two to three separate chunks that highlight important question and answer exchanges verbatim. This gives you context and specificity.
   
3. Optional. Add a [skill](/en/agentic/agent-studio/create-a-genie#create-skills) that retrieves the call transcript from the source by ID.
   

### Unstructured text for emails, notes, and slack exports

You must pre-process unstructured text, such as emails, notes, Slack exports, and other content that lack clear structure before ingestion to create clean, self-contained chunks that can be easily retrieved.

Complete the following steps to prepare your unstructured text for ingestion in a Workato knowledge base:

1. Split content on double line breaks or paragraph boundaries.
   
2. Ensure that your chunks have approximately 4,000 to 5,000 characters to safely remain under the 8k quota.
   
3. Add context, such as date, author, subject, or topic where possible.

---
