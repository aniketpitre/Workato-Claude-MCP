---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/get-slide-elements-action.md
description: >-
  The Get slide elements action retrieves the position, size, and content of
  every element on a PowerPoint slide.
---

# Microsoft PowerPoint - Get slide elements action

The **Get slide elements** action retrieves every element on a single slide in a presentation in Microsoft PowerPoint, including its position, size, and content.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Slide number | Enter the position of the slide to retrieve elements from. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor to view the remaining fields.

| Output field | Description |
| --- | --- |
| Elements | The elements on the slide. Returns one entry per element. |
| Element ID (Elements) | The element's unique ID. |
| Element type (Elements) | The element's type. |
| Placeholder type (Elements) | The type of placeholder the element occupies, if any. |
| Position (Elements) | The element's position on the slide, in English Metric Units (EMU). |
| X (Position) | The element's horizontal position, in EMU. |
| Y (Position) | The element's vertical position, in EMU. |
| Size (Elements) | The element's size, in English Metric Units (EMU). |
| Width (Size) | The element's width, in EMU. |
| Height (Size) | The element's height, in EMU. |
| Text preview (Elements) | A preview of the element's text content. |
