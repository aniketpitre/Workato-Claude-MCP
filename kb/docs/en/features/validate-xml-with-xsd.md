---
url: 'https://docs.workato.com/en/features/validate-xml-with-xsd.md'
description: >-
  Use XML tools by Workato to validate an XML document against an XSD schema,
  enforcing structure, element order, and data types.
---

# XML tools by Workato - Validating XML document with XSD

An XML Schema Definition (XSD) defines the structure, content, and data types of an XML document. This specifies exactly what an XML payload should look like, including which elements are allowed, the order of the elements, and the data types used. You can provide the XSD document inline or reference a [resource](/en/resources).

> **IMPROVED XML CAPABILITIES**
> 
> XML tools by Workato replaces the XML parser by Workato connector and includes an enhanced feature set.

Validating an XML payload against your XSD ensures that the XML conforms to this expected structure. This is critical for catching errors early, enforcing data integrity, and ensuring interoperability between systems. Validation helps prevent malformed or incomplete XML that lead to processing errors, downstream failures, or data inconsistencies, especially in complex integrations and data exchanges.

We strongly recommend that you perform XSD validation to help maintain reliability and trust in your XML-based workflows.

## Setup

No connection configuration is required for this connector.

## Input

Configure the following input fields to set up the XML tools by Workato connector:

| Field | Description |
| --- | --- |
| **XML Document** | The input XML data to be validated. |
| **XSD Document** | Select **Define manually** to provide the XSD document below, or select **Use a resource** to use a resource as the XSD schema. |
| **XSD document** | Optional. The XML Schema Definition (XSD) document to validate the XML structure with. This field appears when you select **Define manually** in the **XSD Document** drop-down menu. |
| **XSD references** | Optional. If the XSD document includes any import or include references, list the names and corresponding values of the imported XSDs. This field appears when you select **Define manually** in the **XSD Document** drop-down menu. |
| **XSD Resource** | Optional. Select the resource to use as the XSD schema. This field appears when you select **Use a resource** in the **XSD Document** drop-down menu. |

## Output

The output displays the raw XML document if validation is successful.

---
