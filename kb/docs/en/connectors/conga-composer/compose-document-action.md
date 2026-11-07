---
url: >-
  https://docs.workato.com/en/connectors/conga-composer/compose-document-action.md
description: >-
  The Compose document action generates a document by merging one or more
  templates with data collected from multiple sources in Conga Composer.
---

# Conga Composer - Compose document action

The **Compose document** action generates a document by merging one or more templates with data collected from multiple sources in Conga Composer.

## Input

| Input field | Description |
| --- | --- |
| JSON data | Enter the JSON data to include in the document. |
| Destinations | Enter information about the sources you plan to use to compose a document. |
| Template sources | Enter information about sources for the template you plan to use. |
| Salesforce request | Enter a **Session ID** for a salesforce request you plan to use to compose a document. |
| Activity | Enter the **Attach operation** you plan to use to compose a document. |

## Output

| Output field | Description |
| --- | --- |
| Status code | A code indicating the status of the document. |
| Is successful | A message indicating if the action was successful. |
| Pre signed create response model | Information about the response model, including `Correlation ID` and `File info details list`. |
