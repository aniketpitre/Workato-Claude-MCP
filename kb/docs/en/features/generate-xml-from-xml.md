---
url: 'https://docs.workato.com/en/features/generate-xml-from-xml.md'
description: >-
  The Generate XML document from a sample XML action infers the structure of an
  XML document from a sample payload and generates an XML document that matches
  that structure.
---

# XML tools by Workato - Generate XML document from a sample XML action

The **Generate XML document from a sample XML** action generates an XML document based on the structure inferred from a sample XML payload. This action reads the provided sample, builds a dynamic input schema from its elements and attributes, and returns an XML document that matches that structure.

You can use this action when an XSD isn't available, or when your XSD contains `anyType` or wildcard elements that can't map directly. You can provide an XSD document inline or reference a [resource](/en/resources).

> **IMPROVED XML CAPABILITIES**
> 
> XML tools by Workato replaces the XML parser by Workato connector and includes an enhanced feature set.

## Input

| Input field | Description |
| --- | --- |
| Sample XML document | Provide a representative XML document. The action uses this file to infer the structure of the generated XML document. |
| XSD Document | Optional. Select **Define manually** to provide the XSD document below, or select **Use a resource** to use a resource as the XSD schema. |
| XSD document | Optional. Upload an XSD file, or provide it as a string, to validate the generated XML document against. The action merges the input schema built from the sample XML with the structure defined in the XSD. This field appears when you select **Define manually** in the **XSD Document** drop-down menu. |
| XSD references | Optional. If the XSD document includes any import or include references, list the names and corresponding values of the imported XSDs. This field appears when you select **Define manually** in the **XSD Document** drop-down menu. |
| XSD Resource | Optional. Select the resource to use as the XSD schema. This field appears when you select **Use a resource** in the **XSD Document** drop-down menu. |

Additional input fields are generated based on the structure of the sample XML you provide. Elements that repeat in the sample are treated as lists.

## Output

| Output field | Description |
| --- | --- |
| Generated XML | The generated XML document, structured according to the provided sample. |

## Quotas

This action supports sample XML files with up to the following quotas:

- Maximum number of fields: 5000 fields
- Maximum combined file size: 10MB (sample XML and XSD combined)

This action doesn't generate a form if the sample XML exceeds 5,000 fields. You must simplify the sample by reducing the number of fields, or split it into smaller samples before you use this action.

---
