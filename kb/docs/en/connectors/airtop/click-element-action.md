---
url: 'https://docs.workato.com/en/connectors/airtop/click-element-action.md'
description: >-
  The Click element action enables you to click an element described in natural
  language in Airtop.
---

# Airtop - Click element action

The **Click element** action uses AI to locate and click an element you describe in natural language in Airtop.

## Input

| Input field | Description |
| --- | --- |
| Session ID | Enter the ID of the browser session that owns the window. |
| Window ID | Enter the Airtop window ID returned when you create a window. |
| Element description | Enter a natural-language description of the element to click. For example, `The login button`. |
| Wait for navigation | Select whether to wait for navigation to complete after clicking. |
| Configuration | Configure **Click type**, **Experimental**, **Visual analysis**, and **Wait for navigation config** fields. |
| Client request ID | Enter a client-provided identifier echoed back in the response metadata. |
| Cost threshold credits | Enter the number of credits at which to cancel the operation. Set to `0` to disable. |
| Time threshold seconds | Enter a threshold to cancel the operation after this many seconds. Set to `0` to disable. |

## Output

| Output field | Description |
| --- | --- |
| Model response | AI-generated result of the click action. |
| Meta | Metadata about the request, including credits consumed. |
| Errors | List of errors returned for the request. |
| Warnings | List of warnings returned for the request. |

---
