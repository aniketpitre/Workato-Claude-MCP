---
url: 'https://docs.workato.com/en/connectors/jina/search-web-action.md'
description: >-
  Run a Google, Bing, or Jina-native web search and return clean, LLM-ready
  results, at a 10,000-token minimum per call.
---

# Jina - Search web action

The **Search web** action searches the web with Jina and returns clean, LLM-friendly results in Jina.

> **MINIMUM TOKEN COST**
> 
> Each call uses at least 10,000 tokens, regardless of query size.

> **SHARED READER OPTIONS**
> 
> Most input fields on this action are also available in the [Read URL](/en/connectors/jina/read-url-action) action, because both actions send the same Jina Reader headers.

## Input

The following are a representative set of input fields.

This action has additional optional input fields inherited from Jina Reader's header options available in the recipe editor. Refer to the Jina [Reader](https://jina.ai/reader/) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Query | Enter the search query string. |
| Country | Optional. Enter a country code, for example `us`. |
| Language | Optional. Enter a language code, for example `en`. |
| Location | Optional. Enter a search location, such as a city. |
| Number of results | Optional. Enter the number of results to return. |
| Search type | Optional. Select the type of search. Options are **Web**, **Images**, or **News**. |
| Provider | Optional. Select the provider. Options are **Google**, **Bing**, or **Reader**. |
| Fallback | Optional. Select **Yes** or **No** to fall back to another provider on failure. |
| Site | Optional. Enter a domain to limit results to, for example `example.com`. |
| Return format | Optional. Select the response format. Options are **Markdown**, **HTML**, **Text**, **Screenshot**, or **Pageshot**. The default is **Markdown**. |
| Custom output fields | Optional. Add fields to create datapills for output fields that the default response doesn't include. These fields aren't sent in the request. |

## Output

The following are a representative set of output fields. Refer to the Jina [Search](https://jina.ai/reader/) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Code | The response's HTTP-style status code. |
| Status | Jina's internal status code. |
| Data | The search results. |
| Title (Data) | The result's title. |
| Description (Data) | The result's meta description. |
| URL (Data) | The result's URL. |
| Content (Data) | The result's extracted content, in the format selected by **Return format**. |
| Meta | Token usage for the request. |

---
