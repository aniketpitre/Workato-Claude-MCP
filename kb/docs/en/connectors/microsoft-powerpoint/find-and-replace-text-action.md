---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/find-and-replace-text-action.md
description: >-
  The Find and replace text action finds and replaces text across every slide in
  a PowerPoint presentation.
---

# Microsoft PowerPoint - Find and replace text action

The **Find and replace text** action finds and replaces text across every slide in a presentation in Microsoft PowerPoint. The action fails if it finds more than 1,000 matches. Narrow your search text or update slides individually with the [Update text content](/en/connectors/microsoft-powerpoint/update-text-content-action) action.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Find text | Enter the text to search for across all slides. |
| Replace with | Optional. Enter the replacement text. Deletes every instance of the found text if left blank. |
| Match case | Optional. Select to match the exact case of the **Find text** value. Options are **Yes** and **No**. Defaults to **Yes** if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Total replacements made | The total number of replacements across the presentation. |
| Affected slides | The slides that contain replacements. |
| Slide number | The position of the affected slide. |
| Replacements on this slide | The number of replacements on the slide. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |
