---
url: 'https://docs.workato.com/en/connectors/xml-creator/create-xml.md'
description: >-
  Use the Create XML action to generate an XML document from a sample XML
  message and mapped datapills.
---

# XML Creator - Create XML action

Use the **Create XML** action to generate an XML document. Upload a sample XML message to generate input fields, then map values to those fields to produce a new XML document.

## Configuration

Configure the following fields to define how the action builds your input schema and generates the XML document:

| Field | Description |
| --- | --- |
| Sample XML message | Upload a sample XML file in the format you plan to generate. This sample file is used to create the input parameter schema. Ensure that list elements are repeated at least once in the sample, and that the first occurrence of each list element contains all expected fields. |
| Preserve XML namespaces and prefixed attributes | Select `Yes` to enable this option and preserve full XML namespace declarations and attributes when parsing. Select `No` for a simplified structure without namespace details. `No` is selected by default. |
| Preserve XML element order | Select `Yes` to enable this option to generate the XML in the same sequence as your XML template. Enable this option when element order matters for your receiving system. `No` is selected by default. |
| Order | Enter the order of XML elements. |

## Output

| Output field | Description |
| --- | --- |
| XML Document | The generated XML document. |

---
