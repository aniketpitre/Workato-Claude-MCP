---
url: 'https://docs.workato.com/en/connectors/canva-connect/import-a-design-action.md'
description: >-
  The Import a design action imports an external file as a new design in Canva
  Connect and returns the imported design.
---

# Canva Connect - Import a design action

The **Import a design** action imports an external file as a new design in Canva Connect and returns the imported design. The action waits for the import to complete and times out after `30` minutes.

## Input

| Input field | Description |
| --- | --- |
| Title | Enter the title of the imported design. Maximum length is `50` characters. |
| File content | Enter the file you plan to import. Supported formats are PDF (`.pdf`), Adobe Illustrator (`.ai`), Adobe Photoshop (`.psd`), Microsoft Word (`.docx`), Microsoft PowerPoint (`.pptx`), Microsoft Excel (`.xls`, `.xlsx`), OpenOffice Draw (`.odg`), OpenOffice Presentation (`.odp`), OpenOffice Sheets (`.ods`), and OpenOffice Text (`.odt`). |

## Output

| Output field | Description |
| --- | --- |
| Design ID | The unique ID of the imported design. |
| Title | The title of the design. |
| Owner | The user ID and team ID of the design's owner. |
| Thumbnail | The width, height, and URL of the design's thumbnail image. |
| URLs | The edit URL and view URL for the design. |
| Created at | The date and time the design was created. |
| Updated at | The date and time the design was last updated. |
| Page count | The number of pages in the design. |

---
