---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/delete-document.md
description: Delete a document from a knowledge base programmatically.
---

# Knowledge base by Workato connector - Delete document

The **Delete document** action deletes a document from a knowledge base by document ID.

Use this action in [knowledge base recipes](/en/agentic/agent-studio/knowledge-bases/knowledge-base-recipes) to keep a knowledge base aligned with its source system, such as, removing a document when the corresponding record is deleted or archived in the source application.

## Input

| Input field | Description |
| --- | --- |
| Knowledge base | Select the knowledge base where you plan to delete the document. Only recipe-type knowledge bases can be selected. Workato GO sources aren't supported. The handle appears in the URL. |
| Document ID | The ID of the document you plan to delete. For example:`9347x04a6d176x4ebe50xxa42x6521c0` |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the document was deleted successfully. |
| Document ID | The ID of the document that was deleted. |
