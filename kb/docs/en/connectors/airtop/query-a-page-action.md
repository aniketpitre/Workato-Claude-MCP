---
url: 'https://docs.workato.com/en/connectors/airtop/query-a-page-action.md'
description: >-
  The Query a page action enables you to ask an AI prompt about the current page
  in Airtop.
---

# Airtop - Query a page action

The **Query a page** action submits a natural-language prompt about the current browser window. Use this action to extract information or answer questions about the page in Airtop.

## Input

| Input field | Description |
| --- | --- |
| Session ID | Enter the ID of the browser session that owns the window. |
| Window ID | Enter the Airtop window ID returned when you create a window. |
| Prompt | Enter a natural-language question or extraction instruction for the page. |
| Configuration | Configure **Visual analysis** related fields, such as **Max scan scrolls**, **Overlap percentage**, **Partition direction**, **Result selection strategy**, **Scan scroll delay**, **Scope**, and **Output schema**. |
| Client request ID | Enter a client-provided identifier echoed back in the response metadata. |
| Cost threshold credits | Enter a threshold to cancel the operation after this amount is exceeded. Set to `0` to disable. |
| Time threshold seconds | Enter a threshold to cancel the operation after this many seconds. Set to `0` to disable. |

## Output

| Output field | Description |
| --- | --- |
| Model response | AI-generated answer to the prompt. Structure varies based on the prompt and output schema you provide. |
| Meta | Metadata about the request, including credits consumed. |
| Errors | List of errors returned for the request. |
| Warnings | List of warnings returned for the request. |

---
