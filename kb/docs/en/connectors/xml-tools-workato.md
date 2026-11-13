---
url: 'https://docs.workato.com/en/connectors/xml-tools-workato.md'
description: >-
  XML tools by Workato is a utility connector that parses, generates,
  transforms, and validates XML documents directly inside your recipes.
---

# XML tools by Workato

XML tools by Workato provides actions to extract values, transform XML structures, and process attributes, enabling seamless recipe integration.

XML (eXtensible Markup Language) is a widely used format for storing and exchanging data, especially in APIs. Workato recipes typically expose XML data as input fields and datapills, but some workflows require direct interaction with XML content.

## How XML tools by Workato works

XML tools by Workato provides the following actions to process XML data:

- The [Parse XML document action](/en/features/parse-xml-document) extracts values from XML and converts them into datapills for use in recipes.
  
- The [Parse XML document (Deprecated) action](/en/features/parse-xml-action) is deprecated. Use the **Parse XML document** action instead.
  
- The [Generate XML document from XSD action](/en/features/generate-xml-from-xsd) generates an XML document that follows the structure and data types defined in an XML Schema Definition (XSD) file.
  
- The [Generate XML document from a sample XML action](/en/features/generate-xml-from-xml) generates an XML document based on the structure inferred from a sample XML payload. Use this action when an XSD isn't available, or when your XSD contains `anyType` or wildcard elements that can't be mapped directly.
  
- The [Transform XML using XSLT action](/en/features/transform-xml-using-xslt) applies an XSLT script to transform XML into another XML structure, JSON, HTML, plain text, or other formats for compatibility with external systems. You can provide the XSLT inline or select a [resource](/en/resources) as the stylesheet.
  
- The [Transform XML using XSLT (Deprecated) action](/en/features/transform-xml-using-xslt-deprecated) is deprecated, doesn't support resources, and requires you to define the XSLT script inline. Use the **Transform XML using XSLT** action instead.
  
- The [Validate XML document with XSD](/en/features/validate-xml-with-xsd) action checks an XML payload against an XSD to confirm it meets the expected structure, content, and data types.
  

## Setup

This connector doesn't require authentication or a connection setup.

## Handle large XML documents

XML tools by Workato actions support XML payloads up to 10 MB at runtime by default. This applies to actions that process XML documents, such as parsing, generating, transforming, and validating XML.

The [Parse XML document action](/en/features/parse-xml-document) supports payloads up to 200 MB when you set **Enable streaming?** to **Yes**.

### Enable streaming

The **Enable streaming?** field controls how the **Parse XML document** action handles XML payloads at runtime.

- No (default)
  
- The action supports XML payloads up to 10 MB and returns the parsed output as datapills. Results return faster, which makes this the right choice for smaller payloads.
  
- Yes
  
- The action supports XML payloads up to 200 MB. Workato writes the parsed JSON to file storage and returns it as a reference. Streamed processing is optimized for throughput.
  

Set **Enable streaming?** to **Yes** when you anticipate large XML payloads.

## Quotas

The XML tools by Workato connector has the following quotas:

### File size quotas

| Description | Quota |
| --- | --- |
| XML tools by Workato actions, default payload quota | 10 MB |
| Parse XML document action, with streaming enabled | 200 MB |

### Action-specific quotas

| Description | Quota |
| --- | --- |
| Maximum number of fields for the Generate XML document from XSD action | 5,000 fields |

### Schema building quotas

| Description | Quota |
| --- | --- |
| Maximum nesting depth of a schema built from XSD or sample XML | 300 |
| Maximum number of properties, objects, and arrays in a schema built from XSD or sample XML | 15,000 |
| Maximum number of child properties in a single object of an XML-derived schema | 5,000 |
| Maximum time to build one XML schema, per request or response | 10 seconds |

---
