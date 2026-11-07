---
url: 'https://docs.workato.com/en/connectors/creatomate/create-record-action.md'
description: The Create record action enables you to create a template in Creatomate.
---

# Creatomate - Create record action

The **Create record** action creates a template in Creatomate.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create. **Template** is the only available object. |
| Name | Name for the template. Must be a non-empty string so you can recognize it later. |
| Composition layers | Select the number of composition layers, from `1` to `3`, to show as input fields under **Source**. Only select more than one layer when an element's type is **Composition**. Pass deeper child elements as JSON if you need more than 3 layers. |
| Source | Template's RenderScript source, including the following properties. |
| Output format | Rendered file format. For example, `mp4` or `jpg`. |
| Width | Output width, in pixels. |
| Height | Output height, in pixels. |
| Frame rate | Video frame rate, in fps. |
| Duration | Output duration, in seconds. |
| Snapshot time | Time, in seconds, to capture the JPEG preview image. |
| Snapshot location | Whether the snapshot replaces the first or last video frame instead of exporting separately. |
| Emoji style | Emoji design style to use in the template. |
| Elements | Visual elements that make up the template, such as text, image, video, audio, shape, or composition. Each element supports properties for position, styling, animation, and media source, and can nest child elements up to the number of Composition layers you select. Deeper nesting is passed as JSON. Refer to the [Creatomate RenderScript documentation](https://creatomate.com/docs/api/reference/introduction) for the complete element schema. |
| Tags | Labels used to organize templates and to filter the list in Search records. |

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
