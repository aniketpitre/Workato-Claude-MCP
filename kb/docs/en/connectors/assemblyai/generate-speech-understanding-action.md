---
url: >-
  https://docs.workato.com/en/connectors/assemblyai/generate-speech-understanding-action.md
description: >-
  Run translation, speaker identification, custom formatting, summarization, or
  action item extraction on a transcript in AssemblyAI.
---

# AssemblyAI - Generate speech understanding action

The **Generate speech understanding** action runs a structured speech understanding feature on a transcript in AssemblyAI.

> **FILL IN ONLY THE MATCHING FEATURE'S FIELDS**
> 
> Only the field group matching **Feature** is required. For example, select **Translation**, then fill in the **Translation** fields. The action errors if the matching group is empty.

## Input

| Input field | Description |
| --- | --- |
| Transcript ID | Enter the ID of the transcript to process. |
| Feature | Select the feature to run. Options are **Translation**, **Speaker identification**, **Custom formatting**, **Summarization**, or **Action items**. |
| Translation | This field is only available when **Feature** is **Translation**. Set **Target languages** with comma-separated codes, for example `es, de`. Optional fields are **Formal** and **Match original utterance**. |
| Speaker identification | This field is only available when **Feature** is **Speaker identification**. Optional fields are **Speaker type**, **Known values** (known roles or names), and **Speakers** (**Role**, **Name**, **Description**, **Company**, or **Title**). |
| Custom formatting | This field is only available when **Feature** is **Custom formatting**. Optional fields are **Date**, **Phone number**, and **Email** format patterns. |
| Summarization | This field is only available when **Feature** is **Summarization**. Set **Summary type**. Optional field is **Effort**. |
| Action items | This field is only available when **Feature** is **Action items**. Optional fields are **Include decisions** and **Effort**. |

## Output

The following are a representative set of output fields. Refer to the AssemblyAI [Create speech understanding](https://www.assemblyai.com/docs/api-reference/llm-gateway/create-speech-understanding) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Request ID | The LLM Gateway request's unique identifier. |
| Translated texts | A list of translated text (one per target language). The **Translated texts** field is only available for **Translation**. |
| Language (Translated texts) | The target language's code, for example `es`. |
| Text (Translated texts) | The translated text for this language. |
| Utterances | A list of diarized utterances. The **Utterances** field is only available for **Speaker identification**. |
| Speaker (Utterances) | The identified speaker's label, for example `A`, or a custom name if you provided one. |
| Text (Utterances) | The utterance's transcribed text. |
| Start (Utterances) | The utterance's start time, in milliseconds. |
| End (Utterances) | The utterance's end time, in milliseconds. |
| Formatted text | The transcript text reformatted per your settings. The **Formatted text** field is only available for **Custom formatting**. |

This action's response also includes an echo of the request and feature status (**Speech understanding**), word-level timing data (**Words**), and a **Confidence** score nested under **Utterances**. Refer to the AssemblyAI [Create speech understanding](https://www.assemblyai.com/docs/api-reference/llm-gateway/create-speech-understanding) documentation for more information on these fields.
