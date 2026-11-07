---
url: 'https://docs.workato.com/en/agentic/agent-studio/upload-files-and-images.md'
description: >-
  Upload files and images to genies in Agent Studio through the chat interface,
  with supported file types, size quotas, and parsing behavior.
---

# Upload files and images

You can upload files and images to your genies through your chat interface. This enables your end users to use files and images with text prompts when interacting with your genie.

## Files

You can upload up to 10 files per message. Each file must be 25MB or smaller. An error displays if any file exceeds 25MB.

Genies inspect only the first 100,000 characters of each file in the conversation to avoid flooding the chat history. The genie passes the full file to skills as input. Skills can't return binary file output.

> **IMAGES IN DOCUMENT FILES AREN'T PARSED**
> 
> Images within document files aren't parsed. Genies only extract and use text content. For example, if you upload a case study PDF with infographic images showing before-and-after metrics, the genie only parses the text. The infographic images aren't parsed.

**Files**:

Agent Studio supports the following document file types:

- `.pdf`
- `.doc`
- `.csv`
- `.md`
- `.txt`
- `.xls`
- `.xlsx`

> **UNSUPPORTED FILE TYPES**
> 
> Agent Studio doesn't support presentation formats, including `.ppt`, `.pptx`, and `.pps`.

## Images

The maximum supported image size is 25MB per file with a maximum of 10 files in a single message. An error displays if any file in a batch exceeds 25MB. Genies can only inspect images up to 4MB in size but are able to send the entire image to a skill. File extensions are used to determine whether an upload is an image or file. Your upload defaults to file if the extension isn't `.jpg` or `.png`.

**Images**:

Agent Studio supports the following image formats:

- `.jpg`
- `.png`

> **UNSUPPORTED IMAGE FORMATS**
> 
> Agent Studio doesn't support the following image formats: `.gif`, `.tiff`, `.eps`,`.svg`, or `.webp`. Video files aren't supported.

## File and image data retention

Files and images uploaded to your genie's chat interface are automatically stored within a temporary folder in [Workato FileStorage](/en/features/workato-filestorage). File and image data is retained for 30 days Time to Live (TTL), after which data is automatically deleted from Workato FileStorage. Ensure that you download or transfer files and images to a permanent storage location within your workflow if you need to preserve this data for a longer period of time.

## Upload a file or image to a genie

You can upload files and images through the genie chat interface. The steps in this section use Workato GO as an example.

> **STEP-BY-STEP GUIDE**
> 
> Review the [Validate Coupa expenses with an expense genie](/en/getting-started/use-cases/agent-studio/genies/expense-genie-coupa-use-case) use case for a step-by-step guide for uploading files and images to your genie.

Complete the following steps to upload a file or image in Agent Studio:

1. Go to the chat interface configured for your genie. For example: Workato GO.
   
2. Go to **AI Genies** and select the genie you plan to use.
   
3. Start a chat with your genie.
   
4. Click the attachment icon (paperclip).
   
   ![Click the attachment icon](/assets/upload-file-in-genie-chat.ZRX9jqpA.png)_Click the attachment icon_
   
5. Go to the file or image you plan to upload in your file system.
   
6. Click the file or image and click **Open**.
   

### File and image upload use case examples

Refer to the following example use cases to determine how file and image uploads can be applied in your conversations:

- **Document analysis and extraction**: Ask your genie to extract and structure key information from uploaded files. For example:
  
  - **Contract review**: Upload a PDF contract and ask your genie to identify key terms, dates, and obligations.
  - **Resume screening**: Upload a resume file and ask your genie to summarize the candidate's qualifications, experience, and skills.
- **Content transformation and generation**: Ask your genie to convert file content into different formats or generate new content based on file data. For example:
  
  - **Report generation**: Upload sales data and ask your genie to generate an executive summary.
  - **Proposal creation**: Upload case study PDFs and ask your genie to draft a customized sales proposal.
- **Compliance and validation**: Ask your genie to verify file content against standards, policies, or regulations. For example:
  
  - **Document completeness**: Upload legal documents and ask your genie to verify required sections are present.
- **Multi-file comparison and synthesis**: Upload multiple files and ask your genie to identify patterns, discrepancies, or create consolidated outputs. For example:
  
  - **Version comparison**: Upload two contract versions and ask your genie to highlight changes.
  - **Competitive analysis**: Upload competitor specification sheets and ask your genie to create a comparison document.

## Add files and images to your skills

You can create skills that accept the same file and images you uploaded in genie conversations as inputs in your [skills](/en/agentic/agent-studio/create-a-genie#create-skills).

Agent Studio genies can interpret text from document files and use the content in [skills](/en/agentic/agent-studio/create-a-genie#create-skills) through the **File** input parameter type. This input passes file data to the recipe as a datapill.

For example, a data analyst genie can export a CSV from Snowflake, then use a skill to parse and aggregate the data.

You can also use images within your [skills](/en/agentic/agent-studio/create-a-genie#create-skills). Genies pass the image data to the recipe using the same **File** input parameter.

### Create a skill with a File input parameter

Agent Studio uses the File input parameter to accept uploaded files and images in a [skill](/en/agentic/agent-studio/create-a-genie#create-skills). This passes file or image data to the recipe as a datapill.

Complete the following steps to create a skill with a **File** input parameter:

1. Search for `Workato Skill` and select it as your app.
   
2. Select the **Start workflow** trigger.
   
3. Use the **Require user confirmation before executing skill?** drop-down menu to determine whether [verified user access](/en/agentic/agent-studio/verified-user-access) is required to run the skill.
   
   ![Start workflow trigger setup](/assets/start-workflow-trigger-file-example.CxaowAdM.png)_Start workflow trigger setup_
   
4. Provide a clear description and instructions to help your genie understand when to execute the skill in the **When should your genie run this skill?** field. For example:
   
   ```plaintext
   
   Run this skill when:
   - A user uploads a file or image
   - The user asks to process, summarize, or analyze a file
   
   Keywords to trigger: upload, file, document, process, analyze, summarize
   
   Do not run this skill for:
   - General questions about files without an actual upload
   - Requests that don't involve file manipulation or review
   ```
   
5. Go to the **What inputs will your genie require to run this skill?** section and click **\+ Add Field**.
   
6. Enter `File` in the **Label** field.
   
   ![File input parameter setup](/assets/file-input-parameter.Bo_yHcJS.png)_File input parameter setup_
   
7. Use the **Data type** drop-down menu to select **File**.
   
8. Use the **Optional** drop-down menu to select **No**.
   
9. Click **Save**.
   
10. Go to the **What should be returned to the genie after this skill is run?** section and click **\+ Add Field**.
    
11. Enter `File_content` in the **Label** field.
    
12. Use the **Data type** drop-down menu to select **String**.
    
13. Use the **Optional** drop-down menu to select **No**.
    
14. Click **Save**.
    
15. Click **\+ Add step** and select **Action in app**.
    
16. Search for `Workato Skill` and select it as your app.
    
17. Select the **Return response** action.
    
18. Map the **File** parameter datapills you plan to use in your response to the **File content** field.
    
    ![Map the File parameter datapills](/assets/map-file-response.BWdx8OB1.png)_Map the **File** parameter datapills_
    

### File and image use case examples in skills

Refer to the following example use cases to determine how your genie can pass files and images to skills to enhance workflows:

- **Document processing and routing**: Upload files that need to be extracted, processed, and sent to specific systems. For example:
  
  - **Invoice processing**: Upload invoice PDFs to your finance genie. A skill uses the IDP by Workato connector to extract line items, totals, and vendor information, then sends the structured data to NetSuite or QuickBooks for payment processing.
- **Image processing**: Upload images that require specialized processing and downstream actions. For example:
  
  - **Expense management**: Upload receipt images to your expense genie. A skill uses the IDP by Workato connector to extract merchant name, date, total amount, and line items, then creates an expense report in Coupa or Concur.
- **Data transformation and integration**: Upload data files that need to be validated, transformed, and distributed. For example:
  
  - **Report distribution**: Upload a quarterly report PDF to your reporting genie. A skill extracts key metrics, generates a summary, then distributes the report to stakeholders through email and posts it to a Slack channel.

## Access files in external systems

Use a knowledge base or a skill to handle reference content that persists across conversations rather than relying on users to upload files.

### Knowledge bases

Use a knowledge base when the genie needs to search across reference content rather than retrieve a specific file.

**Use a knowledge base when**:

- The file contains reference content the genie needs to search, not retrieve in full
- Multiple documents exist and the genie needs to find the most relevant document
- The content is stable enough to ingest in advance

**Supported file types**: `.pdf`, `.pptx`, `.xlsx`, `.docx`

**Quotas**: 16MB maximum per file. Split large documents before ingestion or ingest only the relevant sections. The ingestion process extracts text content only. Images within documents are not indexed.

### Skills

Use a skill when the genie needs to retrieve a specific file by identifier. Build the skill to retrieve the file from its source, extract only the relevant content, and return it to the genie. Don't return the full raw file content to the genie.

**Use a skill when**:

- The genie needs a specific file by identifier, such as a contract for a specific account
- The file is structured enough to query, such as a CSV with specific columns or a JSON document with known fields
- The file is under 250KB and can be filtered before returning content to the genie

## Chat upload and external systems decision matrix

Find the row that matches your scenario to select the right file handling path:

| Scenario | Recommended path | Why | Watch for |
| --- | --- | --- | --- |
| User uploads a contract PDF and asks for a summary of key clauses | Chat upload | The genie reads text content and extracts clauses in the conversation. No skill call is needed for summarization. The genie calls a skill and passes the extracted text as input if clauses must be stored or processed downstream. | Scanned contracts with clauses in image format aren't readable. Inform users that the genie reads text content only. |
| Genie needs to answer questions about HR policies stored in multiple Confluence pages | Knowledge base | Ingest the Confluence pages into a scoped knowledge base. The genie retrieves the relevant policy fragment with a source link. No file upload is needed. | Policy documents with key information in tables or diagrams may have gaps in the content retrieved. Ensure critical policy content is in text format in the source documents. |
| User submits an expense report as a CSV and asks the genie to validate it against the expense policy | Chat upload | The genie reads the CSV content, checks it against the expense policy from a knowledge base or the job description, and identifies policy violations. The genie calls a skill and passes the relevant data as structured inputs if the report must be submitted to an expense system. | Large CSV files produce large text content when extracted. Don't pass the entire CSV as a single text block if only some rows are relevant. |
| CPQ genie must retrieve the current contract for a specific account from Google Drive to check renewal terms | Skill | Build a skill that takes the account name as input, searches Google Drive for the contract, extracts the relevant clauses, and returns the values as structured fields. Don't return the full document to the genie. | The 250KB recommendation applies. Consider ingesting key clauses into a knowledge base for large contracts. |

---
