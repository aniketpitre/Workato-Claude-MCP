---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/copy-slide-action.md
description: The Copy slide action duplicates a slide within a PowerPoint presentation.
---

# Microsoft PowerPoint - Copy slide action

The **Copy slide** action duplicates a slide within a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Source slide number | Enter the position of the slide to copy. |
| Position | Optional. Enter the position to insert the copied slide at. Inserts the copied slide immediately after the source slide if left blank. |

## Output

| Output field | Description |
| --- | --- |
| New slide number | The position of the new slide. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |
