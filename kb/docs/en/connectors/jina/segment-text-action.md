---
url: 'https://docs.workato.com/en/connectors/jina/segment-text-action.md'
description: >-
  Chunk long text for downstream LLM steps, free of charge, up to 64,000
  characters per call.
---

# Jina - Segment text action

The **Segment text** action splits text into semantic chunks with Jina Segmenter in Jina.

## Input

| Input field | Description |
| --- | --- |
| Content | Enter the text to segment. The maximum is 64,000 characters. |
| Return chunks | Optional. Select **Yes** or **No** to return the text chunks. |
| Max chunk length | Optional. Enter the maximum length of each chunk. |
| Tokenizer | Optional. Select the tokenizer to use for counting tokens, such as **cl100k\_base** or **gpt2**. |
| Return tokens | Optional. Select **Yes** or **No** to return the tokenized input. |
| Head (tokens) | Optional. Enter a number to return only the first N tokens. Don't use this setting in combination with **Tail (tokens)**. |
| Tail (tokens) | Optional. Enter a number to return only the last N tokens. Don't use this setting in combination with **Head (tokens)**. |

## Output

| Output field | Description |
| --- | --- |
| Num tokens | The number of tokens in the input text. |
| Tokenizer | The tokenizer used. |
| Usage | Token usage. |
| Tokens (Usage) | Token usage, matching **Num tokens**. |
| Num chunks | The number of chunks returned. |
| Chunk positions | An array of start and end character offsets for each chunk. |
| Chunks | An array of the text chunks. The **Chunks** field is only available when **Return chunks** is **Yes**. |
| Tokens | An array of the tokenized input. The **Tokens** field is only available when **Return tokens** is **Yes**. |

---
