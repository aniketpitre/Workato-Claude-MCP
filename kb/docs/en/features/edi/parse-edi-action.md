---
url: 'https://docs.workato.com/en/features/edi/parse-edi-action.md'
description: >-
  Use the Parse EDI action in EDI tools by Workato to convert EDIFACT, HL7, or
  X12 documents into datapills for downstream recipe steps.
---

# EDI tools by Workato - Parse EDI action

The Parse EDI action enables you to convert EDI documents into Workato datapills.

![Parse EDI action configuration](/assets/parse-edi-action.CsAmST0T.png)_Parse EDI action configuration_

To use this action you must select the EDI standard, provide a sample document, and the EDI document content to parse. A sample document is essential for Workato to generate the schema that is then used in configuring downstream actions of the recipe.

## Input

| Input field | Description |
| --- | --- |
| Populate the datatree with | Choose to generate datapills for the full transaction schema or only the segments you need. |
| EDI standard | Specify the EDI document standard you plan to use. The following choices are available: EDIFACT, HL7, and X12. |
| Standard subset/version | Specify the EDI subset or version of the EDI standard. This option is only available if you choose to generate datapills for all transaction segments. |
| EDI message sample | Provide the sample EDI document used to generate the schema. After providing a sample it is parsed and datapills appear in the recipe builder. |
| Document | Provide the EDI document you plan to parse. |
| CharSet | Specify the encoding of the file contents. Defaults to Unicode (UTF-8) if left blank. |

---
