---
url: 'https://docs.workato.com/en/connectors/firecrawl/scrape-a-page-action.md'
description: >-
  Fetch a single webpage's content in the format you select, from clean markdown
  to AI-ready structured JSON.
---

# Firecrawl - Scrape a page action

The **Scrape a page** action scrapes a single URL to markdown, HTML, JSON, or other formats in Firecrawl. The **JSON** format extracts data from the page using a prompt, a schema, or both.

## Input

The following input fields are the most commonly used. Refer to the Firecrawl [Scrape API](https://docs.firecrawl.dev/api-reference/endpoint/scrape) documentation for the complete list of input fields.

| Input field | Description |
| --- | --- |
| URL | Enter the absolute URL to scrape, for example `https://docs.firecrawl.dev`. |
| Formats | Optional. Select the output formats to return. Options are **Markdown**, **HTML**, **Screenshot**, or **JSON**. The default is **Markdown**. **JSON** requires a prompt, a schema, or both. |
| JSON prompt | Optional. Enter natural-language instructions for JSON extraction. This field is only available when **JSON** is in **Formats**. |
| JSON extract schema | Optional. Enter a JSON schema for JSON extraction. This field is only available when **JSON** is in **Formats**. The schema is sent to Firecrawl only. Add matching fields in **Custom output fields** to get datapills for the extracted data. |
| Only main content | Optional. Select **Yes** or **No** to exclude headers, navigation, and footers from the output. The default is **Yes**. |
| Skip TLS verification | Optional. Select **Yes** or **No** to skip TLS certificate verification. When **Yes**, Firecrawl connects to the target site even if its certificate is invalid, expired, or self-signed. The default is **Yes**. |
| Remove base64 images | Optional. Select **Yes** or **No** to strip base64 images from the markdown output. The default is **Yes**. |
| Block ads | Optional. Select **Yes** or **No** to enable ad and cookie-popup blocking. The default is **Yes**. |
| Store in cache | Optional. Select **Yes** or **No** to store the page in the Firecrawl index. The default is **Yes**. |
| Custom output fields | Optional. Add fields to create datapills for data that the default output doesn't include, such as JSON extraction fields or extra page metadata. |

## Output

The output fields dynamically generate based on the **Formats** you select. The following are common to all formats. Refer to the Firecrawl [Scrape API](https://docs.firecrawl.dev/api-reference/endpoint/scrape) documentation for the complete list of output fields.

| Output field | Description |
| --- | --- |
| Success | A `true` or `false` boolean response that indicates if the scrape completed successfully. |
| Metadata | The page's metadata, such as its title, description, and status code. |
| Warning | A warning message about the scrape, if any. |

---
