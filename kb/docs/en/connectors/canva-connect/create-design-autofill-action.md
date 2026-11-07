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
