---
url: 'https://docs.workato.com/en/features/parse-xml-document.md'
description: >-
  This action converts an XML document into structured output for use in
  recipes, with optional streaming for large payloads.
---

# XML tools by Workato - Parse XML document action

The **Parse XML document** action converts an XML document into structured output for use in subsequent recipe steps. Provide a representative sample to build the output fields, or enable streaming to process large XML documents.

## Input

| Input field | Description |
| --- | --- |
| Enable streaming? | Select **Yes** to process XML payloads up to 200 MB. Workato writes the parsed JSON to file storage and returns it as a reference. Leave the default of **No** to process payloads up to 10 MB and return the output as datapills. Refer to [Handle large XML documents](/en/connectors/xml-tools-workato#handle-large-xml-documents) for more information. |
| Sample XML document | Provide a representative XML sample. Workato uses this sample to build the action's output fields. |
| XML document | Provide the XML data to parse. Workato extracts values and generates datapills for use in subsequent recipe steps. |

## Output

When you set **Enable streaming?** to **No**, the parsed XML data appears as a structured datatree that Workato builds from the **Sample XML document**.

When you set **Enable streaming?** to **Yes**, Workato writes the parsed JSON to file storage and returns it as a reference instead of a datatree.

## Integrate XML into recipes

The **Parse XML document** action extracts structured data from XML, but some workflows require additional setup to ingest XML from external systems. Workato provides multiple ways to receive and process XML beyond parsing.

---
