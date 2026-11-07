---
url: >-
  https://docs.workato.com/en/connectors/docusign/action-get-template-document-tabs.md
description: >-
  The Get template document tabs action retrieves the tabs configured on the
  specified document within a Docusign template.
---

# Docusign - Get template document tabs action

The **Get template document tabs** action retrieves the tabs configured on the specified document within a Docusign template.

Refer to the Docusign [TemplateDocumentTabs:get](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/get/) documentation for more information.

## Input

| Input field | Description |
| --- | --- |
| Template | Select the template that contains the document. |
| Document ID | Enter the unique identifier of the document within the template. This value is available in the Document ID field returned by the [Get template](/en/connectors/docusign/action-get-template) action. |

## Output

The action returns tab collections grouped by tab type. Each tab datapill contains the configuration and placement details for an individual tab. Available nested fields vary by tab type.

| Output field | Description |
| --- | --- |
| Sign here tabs | The signature tabs configured on the document. |
| Initial here tabs | The initials tabs configured on the document. |
| Date signed tabs | The tabs that display the date when a recipient signs. |
| Full name tabs | The tabs that display a recipient's full name. |
| First name tabs | The tabs that display a recipient's first name. |
| Last name tabs | The tabs that display a recipient's last name. |
| Email address tabs | The tabs that display a recipient's email address. |
| Title tabs | The tabs that display a recipient's title. |
| Company tabs | The tabs that display a recipient's company name. |
| Email tabs | The email-entry tabs configured on the document. |
| SSN tabs | The Social Security number-entry tabs configured on the document. |
| ZIP tabs | The ZIP or postal-code entry tabs configured on the document. |
| Text tabs | The text-entry tabs configured on the document. |
| Number tabs | The numeric-entry tabs configured on the document. |
| Date tabs | The date-entry tabs configured on the document. |
| Checkbox tabs | The checkbox tabs configured on the document. |
| List tabs | The drop-down list tabs configured on the document. |
| Radio group tabs | The radio-button group tabs configured on the document. |
| Note tabs | The note tabs configured on the document. |
| Prefill tabs | The sender-prefill tabs grouped by tab type. |
