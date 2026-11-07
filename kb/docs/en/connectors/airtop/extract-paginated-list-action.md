---
url: 'https://docs.workato.com/en/connectors/airtop/extract-paginated-list-action.md'
description: >-
  The Extract paginated list action enables you to extract a list across
  multiple pages with AI in Airtop.
---

# Airtop - Extract paginated list action

The **Extract paginated list** action uses AI to navigate pagination or infinite scroll and extract structured list data from the current page in Airtop.

## Input

| Input field | Description |
| --- | --- |
| Session ID | Enter the ID of the browser session that owns the window. |
| Window ID | Enter the Airtop window ID returned when you create a window. |
| Prompt | Enter a text description of the list to extract and how many pages to traverse. |
| Configuration | Configure **Pagination mode**, **Interaction mode**, **Experimental**, **Scrape**, and **JSON schema**. |
| Client request ID | Enter a client-provided identifier echoed back in the response metadata. |
| Cost threshold credits | Enter a threshold to cancel the operation after this amount is exceeded. Set to `0` to disable. |
| Time threshold seconds | Enter a threshold to cancel the operation after this many seconds. Set to `0` to disable. |

## Output

| Output field | Description |
| --- | --- |
| Model response | AI-extracted list data. Structure varies based on the prompt and output schema you provide. |
| Meta | Metadata about the request, including credits consumed. |
| Errors | List of errors returned for the request. |
| Warnings | List of warnings returned for the request. |

---
