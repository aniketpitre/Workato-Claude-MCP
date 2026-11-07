---
url: 'https://docs.workato.com/en/connectors/google-docs/get-document-action.md'
description: Retrieves the document based on specified document ID.
---

# Google Docs - Get document action

The **Get document** action retrieves the document based on the specified document ID.

## Input

| Input field | Description |
| --- | --- |
| Document ID | Specify the ID of the document you plan to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| Document ID | A unique identifier for the Google Docs document. |
| Title | A user visible name of the tab. |
| Body | The main body of the document tab. Refer to Google's documentation for the [detailed schema](https://developers.google.com/docs/api/reference/rest/v1/documents#body). |
| Content | The contents of the body. Refer to Google's documentation for the [detailed schema](https://developers.google.com/docs/api/reference/rest/v1/documents#structuralelement). |
| Document style | The style of the document tab. Refer to Google's documentation for the [detailed schema](https://developers.google.com/docs/api/reference/rest/v1/documents#documentstyle). |
| Background | The background of the document. Documents cannot have a transparent background color. Refer to Google's documentation for the [detailed schema](https://developers.google.com/docs/api/reference/rest/v1/documents#background). |
| Page number start | The page number from which to start counting the number of pages. |
| Margin top | The top page margin. Refer to Google's documentation for the [detailed schema](https://developers.google.com/docs/api/reference/rest/v1/documents#dimension). |
| Margin bottom | The bottom page margin. Refer to Google's documentation for the [detailed schema](https://developers.google.com/docs/api/reference/rest/v1/documents#dimension). |
| Margin right | The right page margin. Refer to Google's documentation for the [detailed schema](https://developers.google.com/docs/api/reference/rest/v1/documents#dimension). |
| Margin left | The left page margin. Refer to Google's documentation for the [detailed schema](https://developers.google.com/docs/api/reference/rest/v1/documents#dimension). |
| Page size | The size of a page in the document. Refer to the Google [size schema](https://developers.google.com/docs/api/reference/rest/v1/documents#size) documentation for more information. |
| Margin header | The amount of space between the top of the page and the contents of the header. Refer to the Google [dimension schema](https://developers.google.com/docs/api/reference/rest/v1/documents#dimension) documentation for more information. |
| Use custom header footer margins | Indicates whether the **Document Style** [margin header](https://developers.google.com/docs/api/reference/rest/v1/documents#DocumentStyle.FIELDS.margin_header), **Section Style** [margin header](https://developers.google.com/docs/api/reference/rest/v1/documents#SectionStyle.FIELDS.margin_header), **Document Style** [margin footer](https://developers.google.com/docs/api/reference/rest/v1/documents#DocumentStyle.FIELDS.margin_footer), and **Section Style** [margin footer](https://developers.google.com/docs/api/reference/rest/v1/documents#SectionStyle.FIELDS.margin_footer) settings are applied. If `false`, the default values in the Docs editor for header and footer margins are used. |
| Named styles | The named styles of the document tab. Refer to Google's documentation for the [detailed schema](https://developers.google.com/docs/api/reference/rest/v1/documents#namedstyles). |
| Styles | The named styles. Refer to Google's documentation for the [detailed schema](https://developers.google.com/docs/api/reference/rest/v1/documents#namedstyle). |
| Revision ID | The revision ID of the document. |
| Suggestions view mode | The suggestions view mode of the document. |

---
