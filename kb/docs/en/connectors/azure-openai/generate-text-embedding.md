---
url: 'https://docs.workato.com/en/connectors/azure-openai/generate-text-embedding.md'
description: >-
  The Generate text embedding action allows you to represent text data as
  numerical vectors.
---

# Azure OpenAI - Generate text embedding action

The **Generate text embedding** action allows you to represent text data as numerical vectors. This action uses deep neural networks to learn the patterns in large amounts of text data and generate vector representations that capture the meaning and context of the text. These vectors are used for a variety of natural language processing tasks such as sentiment analysis, text classification, and text similarity. Generating text embedding is a common preliminary step before other machine learning tasks. Refer to the [OpenAI documentation](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings) for more information.

![Generate text embedding action](/assets/azure-openai-generate-text-embedding.B7ud2uVt.png)_Generate text embedding action_

## Input

| Input field | Description |
| --- | --- |
| Deployment ID | Enter the deployment ID of the model you plan to use. You can find the deployment ID in **Azure AI Studio > Deployment**. |
| Input | Enter the text for which to obtain an embedding. The input must not exceed 8192 tokens, approximately 6000 words. |
| User | Enter a unique identifier representing your end-user. This helps OpenAI to monitor and detect abuse. |

## Output

| Output field | Description |
| --- | --- |
| Object | The type of object the data value is. This is commonly a list with a single value. |
| Model | The model used for text embedding. |
| Embedding | A list containing the embedding scores for the text that you input. This is generally used in tandem with another machine learning model. An array of embeddings is returned if you provide an array of inputs. |
| Prompt Tokens | The number of tokens used by the prompt. |
| Total Tokens | The total number of tokens used by the prompt and response. |

---
