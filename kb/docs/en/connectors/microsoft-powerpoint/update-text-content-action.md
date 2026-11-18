---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/update-text-content-action.md
description: >-
  The Update text content action replaces the text of a specific element on a
  PowerPoint slide.
---

# Microsoft PowerPoint - Update text content action

The **Update text content** action replaces the text of a specific element on a slide in a presentation in Microsoft PowerPoint. Identify the element by its element ID or existing text.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Slide number | Enter the position of the slide that contains the element. |
| Element ID | Optional. Enter the element ID from the [Get slide elements](/en/connectors/microsoft-powerpoint/get-slide-elements-action) action. Use either this field or **Find text**, not both. |
| Find text | Optional. Enter the text to locate within an element on the slide. Use either this field or **Element ID**, not both. Case-sensitive. |
| New text | Optional. Enter the replacement text. Removes the found text if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Slide number | The position of the updated slide. |
| Element ID | The unique ID of the updated element. |
| Updated text preview | A preview of the element's updated text. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |
