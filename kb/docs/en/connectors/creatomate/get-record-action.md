---
url: 'https://docs.workato.com/en/connectors/creatomate/get-record-action.md'
description: The Get record action enables you to retrieve a template by ID in Creatomate.
---

# Creatomate - Get record action

The **Get record** action retrieves a template you specify in Creatomate.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to retrieve. **Template** is the only available object. |
| Template ID | Enter the ID of the template you plan to retrieve. Get the ID using the Search records action or in the template editor URL. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the template. |
| Name | Name of the template. |
| Tags | List of tags applied to the template. |
| Created at | Date and time when the template was created. |
| Updated at | Date and time when the template was last updated. |
| Warnings | List of warnings about the template's RenderScript source. |
| Source | Template's RenderScript source, including the following properties. |
| Output format | Rendered file format. For example, `mp4` or `jpg`. |
| Width | Output width, in pixels. |
| Height | Output height, in pixels. |
| Frame rate | Video frame rate, in fps. |
| Duration | Output duration, in seconds. |
| Snapshot time | Time, in seconds, to capture the JPEG preview image. |
| Snapshot location | Whether the snapshot replaces the first or last video frame instead of exporting separately. |
| Emoji style | Emoji design style used in the template. |
| Elements | Visual elements that make up the template, including text, image, video, audio, shape, or, composition. Each element supports properties for position, styling, animation, and media source, and can nest child elements. Refer to the [Creatomate RenderScript documentation](https://creatomate.com/docs/api/reference/introduction) for the element schema. |

---
