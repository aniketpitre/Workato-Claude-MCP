---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/data-ingestion.md
description: >-
  Learn how to ingest content into a genie knowledge base using Workato GO data
  sources or recipes, and how to chunk it for retrieval.
---

# Knowledge base data ingestion

Ingesting data correctly determines whether the data can be retrieved reliably. A well-scoped knowledge base with poorly ingested content produces the same poor retrieval as a badly scoped knowledge base. This page covers the ingestion decisions that determine retrieval quality.

## Two ingestion paths

There are two methods to add content to a knowledge base:

- **Workato GO data sources**: Prebuilt connectors available in the [Workato GO](/en/agentic/workato-go) interface. Workato GO data sources connect to common content sources, including Google Drive, Confluence, SharePoint, and Notion, and ingest content with permission-awareness. A user who doesn't have access to a document in the source system can't retrieve fragments from that document through the genie.

Use Workato GO data sources when:

- The content has access restrictions in the source system
  
- A pre-built connector exists for your content source
  
- You need permission-aware retrieval without building custom ingestion logic
  
- **Knowledge base recipes**: Custom recipes you build in the Workato recipe editor. Knowledge base recipes fetch content from any source, including sources not supported by Workato GO data sources, and write it to the knowledge base using the [Knowledge base by Workato](/en/agentic/agent-studio/connectors/knowledge-base-connector/knowledge-base-connector) connector, which can upsert, delete, list, and search documents in a knowledge base. Knowledge base recipes aren't permission-aware. All ingested content is accessible to all users who interact with the genie.
  

Use knowledge base recipes when:

- No Workato GO data source exists for your content source
- The content is appropriate for all users and permission-awareness isn't required
- You need custom ingestion logic, such as transformation, filtering, or format conversion, that a pre-built connector doesn't support

Use Workato GO data sources When both options are available and the content has access restrictions. Content ingested through a recipe isn't retroactively permission-aware if you later switch to a Workato GO data source.

## Chunk content logically

[Content chunking](/en/agentic/agent-studio/knowledge-bases/knowledge-base-configuration#document-preparation-best-practices) before ingestion is the single biggest determinant of retrieval quality after scope. Chunking is the process of dividing content into the individual units that are stored in the knowledge base and retrieved as fragments.

The knowledge base retrieval mechanism returns the most semantically similar fragments rather than the most semantically similar documents. Retrieval quality depends on whether the fragments themselves contain the answer, not whether the document contains the answer.

**The problem with whole-document ingestion**

Retrieval for a question about annual leave accrual may return the entire document as the matching fragment if you ingest a 20-page HR policy document as a single knowledge base entry. The useful information is in the document, but the fragment is too large and too general for the retrieval mechanism to pinpoint it.

**The benefit of logical chunking**

Splitting the same document into individual sections enables section-specific retrieval for a question about annual leave accrual. Create entries for annual leave accrual, sick leave policy, and parental leave eligibility. These fragments are specific, relevant, and citable.

Logical chunking means splitting content at natural boundaries, such as sections, subsections, individual policy items, and individual FAQ entries, rather than at arbitrary size boundaries. A policy document with five sections becomes five knowledge base entries. A FAQ with thirty questions becomes thirty entries. A CSV file with one hundred products becomes one hundred entries.

### Chunking guidelines by content type

| Content type | Chunking approach |
| --- | --- |
| Policy documents | One entry per section or subsection. Split long sections further at logical paragraph breaks. |
| FAQ content | One entry per question-answer pair. Don't batch multiple FAQs into a single entry. |
| Closed tickets | One entry per ticket, including the title, description, and resolution notes. |
| CSV or tabular data | One entry per row, formatted as a structured document in JSON or YAML, not as a raw CSV row. |
| Meeting notes or call summaries | One entry per meeting or call, with key topics and outcomes clearly labeled. |
| Product documentation | One entry per feature or capability, not one entry per product. |

## Source URL

Every entry ingested into a knowledge base should include the URL of the original source document. Your genie uses this URL to cite its sources when presenting information to the user.

Source URLs serve two purposes:

- **Trust and verifiability**: A user who receives a policy answer from the genie can click the link to verify the answer in the original document. This builds trust in genie responses and reduces escalations to human experts.
- **Debugging**: When a retrieval produces incorrect results, the source URL in the knowledge base entry makes it easy to identify which document the incorrect fragment came from and update or remove it.

Include the source URL as a dedicated field in every knowledge base entry. Don't embed the source URL in the text content. Your genie can reference the URL in its response when it retrieves the fragment: `According to the Annual Leave Policy (link).`

## Data format and quality

The quality of content in the knowledge base directly affects retrieval quality. Poorly formatted, noisy, or outdated content produces poor results regardless of how well the knowledge base is scoped or chunked.

- **Use Markdown for structured content**: Plain text is acceptable, but Markdown improves the structure of retrieved fragments. Headers make section boundaries clear. Bold text highlights key terms. Lists present enumerable items cleanly. A knowledge base entry formatted in Markdown is easier for both the retrieval mechanism and the LLM to process than a wall of plain text.
  
- **Convert structured data to JSON or YAML before ingesting**: Raw CSV rows, raw SQL output, and raw tabular data aren't ideal for vector storage. Convert each row or record to a structured document format with labeled fields before ingesting. `annual_leave_days: 20, eligibility: all permanent employees, accrual_rate: 1.67 days per month` is more retrievable than a raw CSV row.
  
- **Clean content before ingesting**: Remove HTML tags, formatting artifacts, navigation elements, and boilerplate text that appears in every document but isn't useful for retrieval. Content that arrives from a web scrape or document export often contains significant noise that degrades retrieval quality if left in.
  
- **Remove outdated content**: A knowledge base that contains both the current version of a policy and an older version produces retrieval results that contradict each other. Check whether the content source already contains outdated versions before ingesting and exclude these versions. Implement logic to detect and remove deleted or superseded content for delta ingestion.
  

## Full load vs. delta load

Content ingestion isn't a one-time event. It requires an ongoing process to keep the knowledge base current. There are two ingestion modes, full load and delta load, and both are needed for a production knowledge base.

### Full load

A full load ingests all content from a source from scratch. Run it once when the knowledge base is first created to establish the baseline content.

Full load guidelines:

- **Apply specific filters, not blanket imports**: Don't ingest an entire Google Drive or an entire Confluence space. Define specific folders, labels, or tags that identify content relevant to this knowledge base. A Google Drive full load should specify the exact folder, such as `HR Policies`, not the entire drive.
- **Apply exclusion logic**: Exclude file types that aren't supported or useful, such as image-only PDFs, video files, and template files not intended for retrieval. Exclude documents with names or labels indicating they are drafts, archived, or internal-only if they shouldn't be retrieved.
- **Run the full load recipe once**: Mark it clearly. A recipe name like `FULL LOAD - Run Once - HR Policies KB` prevents future builders from accidentally re-running it and creating duplicate entries.
- **Verify the output**: Run the full load and check a sample of ingested entries to confirm the chunking, formatting, and source URLs are correct. Fix any issues before configuring the delta load.

### Delta load

A delta load ingests only content that has changed since the last run. Run it on a schedule to keep the knowledge base current as the source content evolves.

Delta load guidelines:

- **Set frequency based on content volatility**: Policies that change quarterly can be updated monthly. Product documentation that changes weekly should be updated daily. Match the ingestion frequency to how often the content changes and how quickly outdated content would cause user-facing problems.
- **Detect and handle deleted content**: When a document is deleted from the source system, remove the corresponding entries in the knowledge base. Delta loads that only add new content and don't remove deleted content accumulate stale entries over time. Implement deletion detection by comparing the current source document list against the knowledge base entries and removing entries for documents that no longer exist.
- **Handle updated content correctly**: When a document is updated, the old knowledge base entries should be replaced with entries reflecting the updated content. Avoid accumulating multiple versions of the same document as separate entries.

## Current data ingestion limitations

Understand the following platform limitations before designing your ingestion process:

| Limitation | Detail |
| --- | --- |
| Maximum file size | 100 MB per file for uploads to knowledge base. Knowledge base uploads follow a separate process and maintain separate limits from [file and image uploads](/en/agentic/agent-studio/upload-files-and-images) in the genie chat interface. |
| Supported file types | PDF, PPTX, XLSX, DOCX. Other file types, including images, videos, and audio files, aren't supported. |
| Text content only | Only the text content of documents is extracted during ingestion. Images within documents aren't extracted or indexed. If a policy document contains important information in an image or diagram rather than in text, that information isn't available for retrieval. |
| Images not supported | Image files such as JPG and PNG can't be ingested as knowledge base documents. Convert the visual to a text description before ingesting if the visual content is critical for a use case. |

These limitations affect how you approach ingestion for certain content types. A policy document that contains tables as images rather than formatted text requires a manual conversion step before ingestion. A product catalog that includes product images needs the image-based information captured as text.

## Track ingestion

Maintain a [Data table](/en/data-tables) that records what's been ingested into each knowledge base. Each row must contain:

- Source document identifier, such as the Confluence page ID or the Google Drive file ID
- Source document name
- Knowledge base it was ingested into
- Date of ingestion
- Number of entries created
- Status field: active, deleted, or superseded

This record serves two purposes. It makes it possible to audit what's in your knowledge base without reading every entry. It also provides the reference data needed for delta load deletion detection by comparing the current source document list against the ingestion record to identify documents that have been deleted from the source.
