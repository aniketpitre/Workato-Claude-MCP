---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/get-slide-content-action.md
description: >-
  The Get slide content action retrieves the text content and speaker notes for
  slides in a PowerPoint presentation.
---

# Microsoft PowerPoint - Get slide content action

The **Get slide content** action retrieves the text content and speaker notes of slides in a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Slide numbers | Optional. Enter the slide numbers to retrieve. Retrieves up to the first 50 slides if left blank. Accepts up to 50 slides per request. |
| Include speaker notes | Optional. Select to include each slide's speaker notes in the response. Options are **Yes** and **No**. Defaults to **Yes** if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Slides | The slides in the presentation. Returns one entry per slide. |
| Slide number (Slides) | The slide's position in the presentation. |
| Slide title (Slides) | The slide's title. |
| Speaker notes (Slides) | The slide's speaker notes. |
| Text elements (Slides) | The text elements on the slide. Returns one entry per element. |
| Element ID (Text elements) | The text element's unique ID. |
| Placeholder type (Text elements) | The type of placeholder the text element occupies. |
| Text (Text elements) | The element's text content. |
| Has more slides | A boolean response (`true` or `false`) that indicates whether the presentation has slides beyond those included in the response. |
| Total slide count | The total number of slides in the presentation. |
| Skipped slide numbers (out of range) | The slide numbers the action excluded from the response because they fall outside the presentation's range. |
