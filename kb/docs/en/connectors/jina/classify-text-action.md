---
url: 'https://docs.workato.com/en/connectors/jina/classify-text-action.md'
description: >-
  Assign labels to text automatically, using either zero-shot candidate labels
  or a classifier you've trained in Jina.
---

# Jina - Classify text action

The **Classify text** action classifies text in Jina.

> **TWO WAYS TO CLASSIFY**
> 
> Provide the **Model** and **Labels** for zero-shot classification against a list of candidate labels, or provide a **Classifier ID** to use a trained classifier instead. The action fails unless you configure the **Model** and **Labels** fields, or **Classifier ID**.

## Input

| Input field | Description |
| --- | --- |
| Model | Required for zero-shot classification, unless a **Classifier ID** is configured. Select a model, or enter a custom model ID. Don't configure this field when using a **Classifier ID**. |
| Input | Enter one or more strings to classify. |
| Labels | The **Labels** field is required for zero-shot classification unless **Classifier ID** is set. Enter the candidate labels. Don't configure this field when using a **Classifier ID**. |
| Classifier ID | Optional. Enter a trained classifier's ID. Don't configure the **Model** and **Labels** fields when specifying a classifier ID. |

## Output

| Output field | Description |
| --- | --- |
| Data | A list of classification results. |
| Object (Data) | The result type. Returns `classification` by default. |
| Index (Data) | The classified input's position in the **Input** array, starting at 0. |
| Prediction (Data) | The predicted label. |
| Score (Data) | The predicted label's confidence score, between 0 and 1. |
| Predictions (Data) | A list of scores for every candidate label. |
| Label (Predictions) | The candidate label. |
| Score (Predictions) | The candidate label's confidence score, between 0 and 1. |
| Usage | Token usage. |
| Total tokens (Usage) | Token usage. |

---
