---
url: 'https://docs.workato.com/en/connectors/exa/get-answer-action.md'
description: >-
  Ask Exa a question and get an AI-generated answer with cited sources, as prose
  or as structured JSON.
---

# Exa - Get answer action

The **Get answer** action submits a question or research prompt to Exa and returns an AI-generated answer with cited sources. Return the answer as prose or as structured JSON that matches an output schema you define.

## Input

The following are a representative set of input fields. Refer to the Exa [Answer](https://exa.ai/docs/reference/answer) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Query | Enter the question or instructions for the request. The minimum is 1 character. |
| Model | Optional. Select the model that generates the answer. Options are **Exa**, **Exa Pro**, **Exa Research**, or **Exa Fast**. **Exa** balances speed and thoroughness, **Exa Pro** researches more thoroughly, and **Exa Fast** responds the quickest. Defaults to **Exa** if left blank. |
| Include citation text | Optional. Select **Yes** to return the full page text for each citation. Defaults to **No** if left blank. |
| Output schema type | Optional. Select **Text** to return prose, or **Object** to return structured JSON that matches your schema. Defaults to **Text** when left blank. |
| Output schema description | Optional. Enter a description of the output. Required when **Output schema type** is **Text**. Leave blank to send no description when **Output schema type** is **Object**. The **Output schema description** field is only available when you select an **Output schema type**. |
| Output schema properties | Optional. Define the properties of the structured answer. Each property becomes an individual datapill. Leave blank to return no individual property datapills. The **Output schema properties** field is only available when **Output schema type** is **Object**. |
| Output schema required fields | Optional. Enter the names of the properties the answer requires. Leave blank to require none. The **Output schema required fields** field is only available when **Output schema type** is **Object**. |
| Allow additional properties | Optional. Select **Yes** to allow properties beyond the ones you define. Defaults to **No** if left blank. The **Allow additional properties** field is only available when **Output schema type** is **Object**. |

## Output

The following are a representative set of output fields. Refer to the Exa [Answer](https://exa.ai/docs/reference/answer) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Request ID | The unique ID of the request. |
| Answer | The answer to your query. Each property you define becomes an individual datapill when you select **Object** for **Output schema type**. |
| Citations | The sources Exa cites in the answer. |
| ID (Citations) | The unique ID of the cited source. |
| Title (Citations) | The title of the cited page. |
| URL (Citations) | The URL of the cited page. |
| Text (Citations) | The full text of the cited page. Exa returns this value only when you select **Yes** for **Include citation text**. |
| Cost dollars | The cost of the request in US dollars. |

---
