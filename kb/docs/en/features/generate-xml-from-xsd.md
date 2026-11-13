---
url: 'https://docs.workato.com/en/features/generate-xml-from-xsd.md'
description: >-
  The Generate XML document from XSD action interprets an XSD file and generates
  a sample XML document that aligns with its structure and data types.
---

# XML tools by Workato - Generate XML document from XSD action

The **Generate XML document from XSD** action generates an XML document that follows the structure and data types defined in an XML Schema Definition (XSD) file. This action reads the provided XSD, builds a dynamic input schema, and returns an XML document that matches the XSD.

You can use this action to ensure the generated XML document is structurally accurate and complete for downstream systems.

> **IMPROVED XML CAPABILITIES**
> 
> XML tools by Workato replaces the XML parser by Workato connector and includes an enhanced feature set.

## Input

| Input field | Description |
| --- | --- |
| XSD document | Upload the XML Schema Definition (XSD) file. The action uses this file to generate the structure of the XML document. |
| XSD references | Optional. Provide referenced XSDs if the main XSD includes `import` or `include` elements. Include the file names and their values. |

Additional input fields are generated based on the XSD documents you provide.

> **DECIMAL FIELDS DISPLAY AS STRING INPUTS**
> 
> XSD schemas with `decimal` fields display those fields as **String** inputs in the recipe editor. This prevents large decimal values from converting to E notation (for example, `1.23E+10`), which produces invalid XML.
> 
> If an existing recipe uses an XSD with decimal fields, those inputs change from Number to String the next time you open the recipe. Runtime behavior is unaffected.

## Output

| Output field | Description |
| --- | --- |
| Generated XML | The generated XML document, structured according to the provided XSD. |

## Quotas

This action supports XSD schemas with a maximum of 5,000 fields total. This action doesn't generate a form if an XSD exceeds this limit. You must simplify or split the schema into smaller schemas before using this action.

---
