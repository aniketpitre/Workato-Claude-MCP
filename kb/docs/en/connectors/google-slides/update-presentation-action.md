---
url: >-
  https://docs.workato.com/en/connectors/google-slides/update-presentation-action.md
description: >-
  The Update presentation action updates the content of a specific Google Slides
  presentation by replacing text, inserting rows, adding text, or replacing
  images.
---

# Google Slides - Update presentation action

The **Update presentation** action updates a specific Google Slides presentation. You can use this action to replace text, insert table rows, insert text, or replace images.

Each action request supports one type of update per run, such as replacing all text or inserting an image.

## Input

| Input field | Description |
| --- | --- |
| Presentation ID | Enter the unique ID of the presentation. You can find this in the URL. |
| Replace all text source list | Provide a list datapill that defines replacement instructions. |
| Replace with | Enter the text to use as the replacement. |
| Find | Provide the text substring to match before replacement. |
| Insert table rows source list | Provide a list datapill that defines table row instructions. |
| Table object ID | Enter the ID of the table to insert rows into. |
| Cell location | Define the table cell to use as the insertion point. |
| Insert below | Select whether to insert rows below the reference cell. |
| Number | Enter the number of rows to insert. The maximum is 20. |
| Insert text source list | Provide a list datapill that defines text insertion instructions. |
| Object ID (text) | Enter the ID of the shape or table for text insertion. |
| Cell location (text) | Define the target table cell for text insertion. |
| Text | Enter the text to insert. |
| Insertion index | Enter the zero-based position to insert the text. |
| Create image source list | Provide a list datapill that defines image creation instructions. |
| Object ID (image) | Enter a unique ID for the image element. Leave blank to auto-generate. |
| Element properties | Define properties for the inserted image element. |
| URL (create image) | Provide the image URL. |
| Replace image source list | Provide a list datapill that defines image replacement instructions. |
| Image title | Enter the title of the image to replace, set through **Alt text** in Slides. |
| URL (replace image) | Provide the URL of the replacement image. |
| Image replace method | Select how the replacement image should fit. The default is **Center inside**. |

## Output

| Output field | Description |
| --- | --- |
| Presentation ID | ID of the updated presentation. |
| Replace all text | Details about text that was replaced. |
| Create image | Details about inserted images. |
| List size | The number of elements in the request list. |
| List index | Index position of elements in the batch request. |
| Write control | Metadata used to handle concurrent write operations. |
| Required revision ID | The revision ID after updates are applied. |
