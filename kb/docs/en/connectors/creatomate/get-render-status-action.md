---
url: 'https://docs.workato.com/en/connectors/creatomate/get-render-status-action.md'
description: >-
  The Get render status action enables you to retrieve the status of a render by
  ID in Creatomate.
---

# Creatomate - Get render status action

The **Get render status** action retrieves a render you specify, including the status, output URL, snapshot URL, file size, and error message if it failed. Use this action to check on a render after the [Create render action](/en/connectors/creatomate/create-render-action) has timed out, since queued renders keep running and complete later.

## Input

| Input field | Description |
| --- | --- |
| Render ID | Enter the ID of the render you plan to check. Returned when the render was submitted. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the render. |
| Status | Status of the render. For example, `succeeded`. |
| Error message | Reason the render failed. |
| URL | URL of the rendered file. |
| Snapshot URL | URL of the JPEG preview image. |
| Template ID | ID of the source template, if the render was created from one. |
| Template name | Name of the source template, if a template was used to create the render. |
| Template tags | Tags on the source template, if a template was used to create the render. |
| Output format | Rendered file format. |
| Render scale | Scale applied to the output. |
| Width | Output width, in pixels. |
| Height | Output height, in pixels. |
| Frame rate | Video frame rate, in fps. |
| Duration | Output duration, in seconds. |
| File size | Size of the rendered file, in bytes. |
| Modifications | Key-value pairs applied to the template, if any. |
| Webhook URL | Webhook URL called when the render finished. |
| Metadata | Metadata value passed through from the input. |
| Warnings | List of warnings about the render, if any. |

---
