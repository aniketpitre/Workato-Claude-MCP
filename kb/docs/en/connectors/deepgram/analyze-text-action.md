---
url: 'https://docs.workato.com/en/connectors/deepgram/analyze-text-action.md'
description: >-
  Analyze plain text or a text URL in Deepgram to summarize it and detect
  topics, intents, and sentiment.
---

# Deepgram - Analyze text action

The **Analyze text** action analyzes plain text or the text at a URL in Deepgram. Optionally summarize the text and detect topics, intents, and sentiment.

## Input

Input fields dynamically generate based on the **Text source** you select. The following are a representative set of input fields. Refer to the Deepgram [API](https://developers.deepgram.com/reference/text-intelligence/analyze-text) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Text source | Select **Text** to send plain text, or **Text URL** to send a hosted file. |
| Text | Enter the plain text to analyze. Summaries require more than 50 words. The **Text** field is only available when **Text source** is **Text**. |
| Text URL | Enter the publicly reachable URL of the text to analyze. The **Text URL** field is only available when **Text source** is **Text URL**. |
| Language | Optional. Select the language of the text. Deepgram text analysis supports English only. Defaults to **English (en)** if left blank. |
| Summarize | Optional. Select **Yes** to summarize the text. Leave blank to return no summary. |
| Topics | Optional. Select **Yes** to detect the topics in the text. Leave blank to skip topic detection. |
| Intents | Optional. Select **Yes** to detect the intents in the text. Leave blank to skip intent detection. |
| Sentiment | Optional. Select **Yes** to analyze the sentiment of the text. Leave blank to skip sentiment analysis. |
| Tags | Optional. Enter comma-separated labels to attach to the request for usage reporting. Leave blank to send no tags. |
| Callback URL | Optional. Enter the URL where Deepgram sends the result when processing finishes. The action returns only the **Request ID** when you set a callback URL. Leave blank to return the result in the action output. |

## Output

The following are a representative set of output fields. Refer to the Deepgram [API](https://developers.deepgram.com/reference/text-intelligence/analyze-text) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Request ID | The unique ID of the request. |
| Metadata | Information about the request. The **Metadata** field is only available when **Callback URL** is blank. |
| Created (Metadata) | The date and time Deepgram processed the request. |
| Language (Metadata) | The language of the analyzed text. |
| Results | The analysis results. The **Results** field is only available when **Callback URL** is blank. |
| Summary (Results) | The summary of the text. The **Summary** field is only available when **Summarize** is **Yes**. |
| Text (Summary) | The text of the summary. |
| Topics (Results) | The topics detected in each segment of the text. The **Topics** field is only available when **Topics** is **Yes**. |
| Intents (Results) | The intents detected in each segment of the text. The **Intents** field is only available when **Intents** is **Yes**. |
| Sentiments (Results) | The sentiment of each segment and the average sentiment of the text. The **Sentiments** field is only available when **Sentiment** is **Yes**. |

---
