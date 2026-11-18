---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/add-slide-action.md
description: >-
  The Add slide action inserts a new slide into a PowerPoint presentation using
  a layout you specify.
---

# Microsoft PowerPoint - Add slide action

The **Add slide** action inserts a new slide into a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Layout ID | Optional. Enter the layout ID from the [List slide layouts (batch)](/en/connectors/microsoft-powerpoint/list-slide-layouts-action-batch) action. Uses a blank-compatible layout if left blank. |
| Position | Optional. Enter the position to insert the slide at. Appends the slide to the end of the presentation if left blank. |

## Output

| Output field | Description |
| --- | --- |
| New slide number | The position of the new slide. |
| Layout used | The ID of the layout the action applied to the new slide. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |
