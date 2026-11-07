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
