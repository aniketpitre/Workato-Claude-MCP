---
url: 'https://docs.workato.com/en/connectors/box/trigger-new-event-folder.md'
description: >-
  The New event in folder real-time trigger starts a recipe when Box detects
  file or folder events in a specified folder.
---

# Box - New event in folder trigger (real-time)

The **New event in folder** real-time trigger starts a recipe when Box detects file or folder events in a specified folder. The trigger fetches events as they occur. You can run only one active trigger on a folder at a time per authenticated user.

## Input

| Input field | Description |
| --- | --- |
| Folder | Select the folder to monitor. You can select from the drop-down menu or enter a folder ID. |
| Events to monitor | Select the specific events to monitor. Only the selected event types trigger the recipe. |

## Output

The output fields vary depending on the type of event. The following example shows the output for a **folder created** event:

| Output field | Description |
| --- | --- |
| Event | Short description of the event. For example, `FOLDER.CREATED`. |
| File/folder source | Source details of the folder or file where the event occurred. |
| Additional information | Notes or additional context for the event, if available. |

---
