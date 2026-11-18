---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/delete-slide-action.md
description: >-
  The Delete slide action permanently removes one or more slides from a
  PowerPoint presentation.
---

# Microsoft PowerPoint - Delete slide action

The **Delete slide** action removes one or more slides from a presentation in Microsoft PowerPoint. At least one slide must remain in the presentation.

> **THIS ACTION CAN'T BE UNDONE**
> 
> You can't recover deleted slides. Confirm the slide numbers before you run this action.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Slide numbers | Enter the position of the slide or slides to delete. Accepts a single number or a list. |

## Output

| Output field | Description |
| --- | --- |
| Slides deleted | The number of slides the action deleted. |
| Remaining slides | The number of slides remaining in the presentation. |
| Skipped slide numbers (out of range) | The slide numbers the action excluded because they fall outside the presentation's range. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |
