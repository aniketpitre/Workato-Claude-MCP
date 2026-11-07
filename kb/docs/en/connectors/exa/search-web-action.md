---
url: 'https://docs.workato.com/en/connectors/exa/search-web-action.md'
description: >-
  Run a natural-language web search in Exa and return ranked results, with
  optional summaries and structured output.
---

# Exa - Search web action

The **Search web** action runs a natural-language web search in Exa and returns ranked results. Optionally return a summary for each result, or a structured answer that matches an output schema you define.

## Input

The following are a representative set of input fields. Refer to the Exa [Search](https://exa.ai/docs/reference/search) documentation for more information on available input fields.

### Search input

| Input field | Description |
| --- | --- |
| Query | Enter the natural-language search query. |
| Search type | Optional. Select the search mode. Options are **Auto**, **Fast**, **Instant**, **Deep lite**, **Deep**, or **Deep reasoning**. **Auto** lets Exa decide, **Fast** and **Instant** return results with low latency, **Deep lite** returns synthesized results faster than **Deep**, and **Deep** and **Deep reasoning** search more thoroughly. Defaults to **Auto** if left blank. |
| Number of results | Optional. Enter the number of results to return. Valid values are `1`\-`100`. Defaults to `10` if left blank. |
| Additional queries | Optional. Enter extra query variations. Valid values are `1`\-`10` entries. Only deep search types use additional queries. Leave blank to search with the **Query** alone. |
| Include domains | Optional. Enter the domains to restrict results to, one per entry. Leave blank to search all domains. |
| Exclude domains | Optional. Enter the domains to exclude from results, one per entry. Leave blank to exclude none. |
| Summary | Optional. Add this field to return an LLM-generated summary for each result. Using it adds cost. Leave blank to return no summary. |
| Summary schema | Optional. Define the fields of a structured summary for each result. Add fields manually or generate a schema from a sample. Each field becomes an individual datapill. Leave blank to return a plain-text summary when you add the **Summary** field. |

### Output schema input

| Input field | Description |
| --- | --- |
| Output schema type | Optional. Select the format of the synthesized answer. Select **Text** to return prose, or **Object** to return structured JSON that matches your schema. Leave blank to return search results only. |
| Output schema description | Optional. Enter a description of the output you want. Required when **Output schema type** is **Text**. Leave blank to send no description when **Output schema type** is **Object**. The **Output schema description** field is only available when you select an **Output schema type**. |
| Output schema properties | Optional. Define the properties of the structured output. Each property becomes an individual datapill. Leave blank to return no individual property datapills. The **Output schema properties** field is only available when **Output schema type** is **Object**. |
| Output schema required fields | Optional. Enter the names of the properties the output requires. Leave blank to require none. The **Output schema required fields** field is only available when **Output schema type** is **Object**. |
| Allow additional properties | Optional. Select **Yes** to allow properties beyond the ones you define. Defaults to **No** if left blank. The **Allow additional properties** field is only available when **Output schema type** is **Object**. |

## Output

The following are a representative set of output fields. Refer to the Exa [Search](https://exa.ai/docs/reference/search) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Request ID | The unique ID of the request. |
| Resolved search type | The search mode Exa used. |
| Results | The ranked search results. |
| ID (Results) | The unique ID of the result. |
| Title (Results) | The title of the result page. |
| URL (Results) | The URL of the result page. |
| Summary (Results) | The summary of the result page. When you define a **Summary schema**, each field becomes an individual datapill. |
| Output | The synthesized answer. Exa returns this value only when you select an **Output schema type**. |
| Content (Output) | The synthesized answer, as text or as an object that matches your output schema. |
| Grounding (Output) | The citations and confidence level for each field in the answer. |

---
