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
