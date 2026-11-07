---
url: 'https://docs.workato.com/en/connectors/openai/edit-text.md'
description: >-
  The Edit text action in the OpenAI connector revises input text based on your
  instructions to improve clarity, grammar, and conciseness.
---

# OpenAI - Edit text action

Edit text for the provided input, instruction, and parameters. You can use this action across workflows in a variety of use cases:

- **Proposal/pitch generation:** Sales teams can use the edit text feature to improve the quality of their proposals, quotes, and other sales collaterals. The action can be used to generate sales documents and automatically edit the content for clarity and conciseness.
- **Brainstorming:** Marketing teams can use the edit text feature to improve the quality of their messaging and content. It can be used in workflows that generate marketing materials, and automatically edit the content to ensure it is grammatically correct and engaging.
- **Documentation generation:** The action can be used to generate documentation from release notes for faster internal and external communication.

![Edit text action](/assets/edit-text.BMCkcds4.png)_Edit Text Action_

## Input

| Field | Description |
| --- | --- |
| Model | Use the **Model** drop-down menu to select the OpenAI model you plan to use. You can click into the **Model** field and enter the model if it isn't listed. |
| Input | Enter a text prompt that you would like modified. |
| Instruction | Provide specific instructions based on which the model will edit the input text. |
| Top p | Enter a value between 0 and 1 for controlling the diversity of completions. A higher value results in more varied responses. We recommend using this or temperature but not both. Refer to the OpenAI [top\_p parameter](https://platform.openai.com/docs/api-reference/edits/create#edits/create-top_p) documentation for more information. |
| Temperature | Enter a value between 0 and 2 to control the randomness of completions. Higher values will make the output more random, while lower values will make it more focused and deterministic. We recommend using this or top p but not both. Refer to the OpenAI [temperature parameter](https://platform.openai.com/docs/api-reference/edits/create#edits/create-temperature) documentation for more information. |
| Number of edits | The number of edits to generate for the prompt. The minimum is 1 and the maximum is 20. |

## Output

| Field | Description |
| --- | --- |
| Created | The datetime stamp of when the response was generated. |
| Choices | Text | The response of the model for the specified input. |
| Best choice | Contains the response which OpenAI probabilistically considers to be the ideal selection. |
| Usage | Prompt tokens | The number of tokens utilized by the prompt. |
| Completions tokens | The number of tokens utilized for editing text. |
| Total tokens | The total number of tokens utilized by the prompt and response. |

---
