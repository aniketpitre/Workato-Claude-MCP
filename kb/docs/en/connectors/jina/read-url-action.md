---
url: 'https://docs.workato.com/en/connectors/jina/read-url-action.md'
description: 'Turn any URL into LLM-ready markdown, HTML, or a screenshot using Jina Reader.'
---

# Jina - Read URL action

The **Read URL** action fetches a URL with Jina Reader and returns clean content in Jina.

> **SHARED READER OPTIONS**
> 
> Most input fields on this action are also available in the [Search web](/en/connectors/jina/search-web-action) action, because both actions send the same Jina Reader headers.

## Input

The following are a representative set of input fields.

This action has additional optional input fields inherited from Jina Reader's header options available in the recipe editor. Refer to the Jina [Reader](https://jina.ai/reader/) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| URL | Enter the absolute URL to read. |
| Return format | Optional. Select the response format. Options are **Markdown**, **HTML**, **Text**, **Screenshot**, or **Pageshot**. The default is **Markdown**. |
| Engine | Optional. Select the Reader engine, such as **Browser** or **Direct**. |
| Timeout (seconds) | Optional. Enter a timeout limit, in seconds. Valid values are 1-180. |
| Target selector | Optional. Enter a CSS selector for the main content, for example `article` or `.main`. |
| No cache | Optional. Select **Yes** or **No** to bypass the cache and fetch fresh content. |
| Retain images | Optional. Select how images are kept in the output. Options are **All**, **None**, **Alt**, **All\_p**, or **Alt\_p**. |
| Retain links | Optional. Select how links are kept in the output. Options are **All**, **None**, **Text**, or **GPT OSS**. |
| Token budget | Optional. Enter a token budget for the response. |
| PDF page | Optional. Enter a PDF page index to read. |
| Custom output fields | Optional. Add fields to create datapills for output fields that the default response doesn't include. These fields aren't sent in the request. |

## Output

The following are a representative set of output fields. Refer to the Jina [Reader](https://jina.ai/reader/) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Code | The response's HTTP-style status code. |
| Status | Jina's internal status code. |
| Data | The page's content. |
| Title (Data) | The page's title. |
| Description (Data) | The page's meta description. |
| URL (Data) | The page's URL. |
| Content (Data) | The page's extracted content, in the format selected by **Return format**. |
| HTTP status (Data) | The origin page's HTTP status code. |
| Meta | Token usage for the request. |

---
