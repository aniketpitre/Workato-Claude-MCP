---
url: 'https://docs.workato.com/en/connectors/canva-connect/export-a-design-action.md'
description: >-
  The Export a design action exports a design from Canva Connect to a file and
  returns the download URLs.
---

# Canva Connect - Export a design action

The **Export a design** action exports a design from Canva Connect to a file and returns the download URLs. The action waits for the export to complete and times out after `30` minutes.

## Input

| Input field | Description |
| --- | --- |
| Design ID | Enter the ID of the design you plan to export. |
| File type | Select the format to export the design as. Options are `PDF`, `JPG`, `PNG`, `PPTX`, `GIF`, or `MP4`. |
| Pages | Enter page numbers to export from a multi-page design. The first page is page 1. All pages are exported if left blank. |
| Page size | Select the paper size of the exported PDF. Options are `A4`, `A3`, `Letter`, or `Legal`. Required for PDF exports. |
| Height | Enter the height, in pixels, of the exported image. Used for JPG, PNG, or GIF exports only. |
| Width | Enter the width, in pixels, of the exported image. Used for JPG, PNG, or GIF exports only. |
| Lossless | Set to true to export the PNG with lossless compression. Defaults to false. Used for PNG exports only. |
| As single image | Set to true to merge a multi-page design into a single PNG image instead of exporting each page separately. Defaults to false. Used for PNG exports only. |
| Transparent background | Set to true to export the PNG with a transparent background. Requires Canva Pro. Used for PNG exports only. |

## Output

| Output field | Description |
| --- | --- |
| URLs | The download URLs for the exported file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/canva-connect/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action retrieves the details of a single Canva
  Connect record or job by its ID.
---

# Canva Connect - Get record details by ID action

The **Get record details by ID** action retrieves the details of a single record from Canva Connect by its ID. Supported objects are folders, assets, designs, comments, brand templates, brand template datasets, design export formats, and the status of design import, export, autofill, and asset upload jobs. Requires a Canva Pro, Teams, or Enterprise plan.

## Input

Input fields dynamically generate based on the object you select. The following field is common to all objects. Refer to the [Canva Connect](https://www.canva.dev/docs/connect/) documentation for a complete list of input fields.

| Input field | Description |
| --- | --- |
| Object | Select the Canva Connect object to retrieve. |

## Output

Output fields dynamically generate based on the object you select. Refer to the [Canva Connect](https://www.canva.dev/docs/connect/) documentation for a complete list of output fields.

---
