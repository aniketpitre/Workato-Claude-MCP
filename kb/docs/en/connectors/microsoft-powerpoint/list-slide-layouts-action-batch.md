---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/list-slide-layouts-action-batch.md
description: >-
  The List slide layouts (batch) action retrieves the slide layouts and
  placeholders defined in a PowerPoint presentation.
---

# Microsoft PowerPoint - List slide layouts action (batch)

The **List slide layouts (batch)** action retrieves the slide layouts defined in a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |

## Output

| Output field | Description |
| --- | --- |
| Layouts | The slide layouts defined in the presentation. Returns one entry per layout. |
| Layout ID (Layouts) | The layout's unique ID. |
| Layout name (Layouts) | The layout's name. |
| Slide master (Layouts) | The name of the slide master the layout belongs to. |
| Placeholders (Layouts) | The placeholders defined in the layout. Returns one entry per placeholder. |
| Placeholder type (Placeholders) | The placeholder's type. |
| Placeholder index (Placeholders) | The placeholder's index. |
