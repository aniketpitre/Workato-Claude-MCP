---
url: 'https://docs.workato.com/en/connectors/airtop/type-text-action.md'
description: >-
  The Type text action enables you to type text into the browser window in
  Airtop.
---

# Airtop - Type text action

The **Type text** action types text into the active field or a field you describe in natural language in Airtop.

## Input

| Input field | Description |
| --- | --- |
| Session ID | Enter the ID of the browser session that owns the window. |
| Window ID | Enter the Airtop window ID returned when you create a window. |
| Text | Enter text to type into the browser window. |
| Element description | Enter a natural-language description of where to type the text. For example, `Username field`. Leave blank to use the active field. |
| Wait for navigation | Select whether to wait for navigation to complete after typing. |
| Configuration | Configure **Experimental**, **Visual analysis**, and **Wait for navigation config** fields. |
| Client request ID | Enter a client-provided identifier echoed back in the response metadata. |
| Cost threshold credits | Enter a threshold to cancel the operation after this amount is exceeded. Set to `0` to disable. |
| Time threshold seconds | Enter a threshold to cancel the operation after this many seconds. Set to `0` to disable. |

## Output

| Output field | Description |
| --- | --- |
| Model response | AI-generated result of the type action. |
| Meta | Metadata about the request, including credits consumed. |
| Errors | List of errors returned for the request. |
| Warnings | List of warnings returned for the request. |

---
