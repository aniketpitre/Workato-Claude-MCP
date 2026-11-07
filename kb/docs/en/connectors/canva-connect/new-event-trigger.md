---
url: 'https://docs.workato.com/en/connectors/canva-connect/new-event-trigger.md'
description: >-
  The New event trigger starts a recipe when a selected webhook event occurs in
  Canva Connect.
---

# Canva Connect - New event trigger

The **New event** trigger starts a recipe when a selected webhook event occurs in Canva Connect. Supported events include design access requested, folder access requested, team invite, design approval requested, design approval response, comment, share design, and share folder.

## Input

| Input field | Description |
| --- | --- |
| Event | Select the Canva Connect event you plan to monitor. |

## Output

Output fields dynamically generate based on the event you select. Refer to the [Canva Connect](https://www.canva.dev/docs/connect/) documentation for a complete list of output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/canva-connect/create-design-autofill-action.md
description: >-
  The Create design autofill action autofills a Canva Connect brand template
  with your data and returns the created design once the job finishes.
---

# Canva Connect - Create design autofill action

The **Create design autofill** action autofills a brand template with data you provide and returns the created design once the job finishes in Canva Connect. The action waits for the autofill job to complete and times out after 30 minutes. This action requires the `brandtemplate:content:read`, `design:content:write`, and `design:meta:read` scopes, and is only available on Canva Enterprise plans.

## Input

Input fields dynamically generate based on the brand template you select. The following fields are common to all brand templates. Refer to the [Canva Connect](https://www.canva.dev/docs/connect/) documentation for a complete list of input fields.

| Input field | Description |
| --- | --- |
| Brand template | Enter or select the brand template to autofill. |
| Title | Enter the title to use for the autofilled design. Maximum length is `255` characters. The design uses the brand template's title if left blank. |
| Email | Enter the email to autofill the brand template with. |
| Name | Enter the name to autofill the brand template with. |

## Output

Output fields dynamically generate based on the brand template you select. The following fields are common to all brand templates. Refer to the [Canva Connect](https://www.canva.dev/docs/connect/) documentation for a complete list of input fields.

| Output field | Description |
| --- | --- |
| Type | The autofill result type. |
| Design ID | The unique ID of the created design. |
| Title | The title of the design. |
| URL | The URL of the created design. |
| Thumbnail | The width, height, and URL of the design's thumbnail image. |
| URLs | The edit URL and view URL for the design. |
| Created at | The date and time the design was created. |
| Updated at | The date and time the design was last updated. |
| Page count | The number of pages in the design. |

---

---
url: >-
  https://docs.workato.com/en/connectors/canva-connect/create-design-autofill-job-action.md
description: >-
  The Create design autofill job action starts an asynchronous job that
  autofills a brand template with data and returns the job ID in Canva.
---

# Canva Connect - Create design autofill job action

The **Create design autofill job** action starts an asynchronous job that autofills a brand template with data and returns the job ID immediately in Canva Connect, instead of waiting for the job to finish. Use the [Get record details by ID](/en/connectors/canva-connect/get-record-details-by-id-action) action with the **Design autofill job** object to poll the job for its status and resulting design.

This action requires the `brandtemplate:content:read`, `design:content:write`, and `design:meta:read` scopes, and is only available on Canva Enterprise plans.

## Input

| Input field | Description |
| --- | --- |
| Brand template ID | Enter the ID of the brand template you plan to autofill. |
| Title | Enter the title you plan to use for the autofilled design. The design uses the brand template's title if left blank. |
| Data values | Enter the data you plan to autofill into the brand template. Each entry has a key, a type, and the value to insert. |

## Output

| Output field | Description |
| --- | --- |
| Job ID | The ID of the autofill job. |
| Status | The status of the autofill job. |

---

---
url: >-
  https://docs.workato.com/en/connectors/canva-connect/create-design-export-job-action.md
description: >-
  The Create design export job action starts an asynchronous export job for a
  design in Canva and returns the job ID immediately, instead of waiting for the
  export to finish.
---

# Canva Connect - Create design export job action

The **Create design export job** action starts an asynchronous export job for a design in Canva Connect and returns the job ID immediately, instead of waiting for the export to finish. Use the [Get record details by ID](/en/connectors/canva-connect/get-record-details-by-id-action) action with the **Design export job** object to poll the job for its status and download URLs.

## Input

| Input field | Description |
| --- | --- |
| Design ID | Enter the ID of the design you plan to export. |
| File type | Select the format you plan to export the design as. Options include `PDF`, `JPG`, `PNG`, `PPTX`, `GIF`, or `MP4`. |
| Pages | Enter the page numbers to export from a multi-page design. The first page is page 1. All pages are exported if left blank. |
| Page size | Select the paper size of the exported PDF. Options are `A4`, `A3`, `Letter`, or `Legal`. Required for PDF exports. |
| Height | Enter the height, in pixels, of the exported image. Used for JPG, PNG, or GIF exports only. |
| Width | Enter the width, in pixels, of the exported image. Used for JPG, PNG, or GIF exports only. |
| Lossless | Set to true to export the PNG with lossless compression. Defaults to false. Used for PNG exports only. |
| As single image | Set to true to merge a multi-page design into a single PNG image instead of exporting each page separately. Defaults to false. Used for PNG exports only. |
| Transparent background | Set to true to export the PNG with a transparent background. Requires Canva Pro. Used for PNG exports only. |

## Output

| Output field | Description |
| --- | --- |
| Job ID | The ID of the export job. |
| Status | The status of the export job. |

---
