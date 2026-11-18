---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/update-speaker-notes-action.md
description: >-
  The Update speaker notes action replaces the speaker notes for a slide in a
  PowerPoint presentation.
---

# Microsoft PowerPoint - Update speaker notes action

The **Update speaker notes** action replaces the speaker notes for a slide in a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Slide number | Enter the position of the slide to update. |
| Notes content | Optional. Enter the speaker notes text. Replaces the existing notes entirely. Accepts up to 5,000 characters. Clears the notes if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Slide number | The position of the updated slide. |
| Notes preview | A preview of the slide's updated speaker notes. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |
