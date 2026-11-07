---
url: 'https://docs.workato.com/en/connectors/tavily/extract-page-content-action.md'
description: >-
  The Extract page content action retrieves the content of one or more URLs and
  returns it as Markdown or plain text.
---

# Tavily - Extract page content action

The **Extract page content** action retrieves the content of one or more URLs using Tavily and returns it as Markdown or plain text.

## Input

| Input field | Description |
| --- | --- |
| URLs | Enter one or more full URLs you plan to extract content from. The maximum is `20`. |
| Query | Enter a query to re-rank extracted content chunks by relevance. |
| Chunks per source | Enter the number of content chunks to return per source, from `1` to `5`. Only used when **Query** is set. Defaults to `3`. |
| Include favicon | Select whether to include the favicon URL for each result. |
| Include images | Select whether to include images extracted from the URLs. |

## Output

| Output field | Description |
| --- | --- |
| Results | The extracted pages. Each result includes the URL, title, raw content, images, and favicon. |
| Failed results | URLs that couldn't be extracted, each with the URL and the resulting error. |
| Response time | The time Tavily took to process the extraction, in seconds. |
| Usage | The number of credits the extraction consumed. |
| Request ID | The unique identifier for this extraction request. |

---
