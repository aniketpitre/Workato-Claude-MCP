---
url: 'https://docs.workato.com/en/features/parse-xml-action.md'
description: >-
  This action extracts data from XML and converts it into datapills for use in
  recipes. This action is deprecated.
---

# XML tools by Workato - Parse XML document (Deprecated) action

The **Parse XML document (Deprecated)** action extracts data from an XML document and converts it into datapills for use in subsequent recipe steps.

> **DEPRECATED**
> 
> This action is deprecated. Use the [Parse XML document](/en/features/parse-xml-document) action instead.

## Input

| Input field | Description |
| --- | --- |
| XML type | Select the level of detail to parse from the XML document. Workato determines the data type of each datapill based on the XML content. Choose **Simple XML without attributes** to generate a streamlined datatree that includes only the default XML syntax and the `type` attribute, ignoring all other attributes. Choose **Full XML with attributes** to include all attributes in the output. Each XML tag appears as an Array datapill, with values stored under a Content datapill. Refer to the [Output](#output) section for more information. |
| Sample document | Provide a sample XML document that matches the expected format of the XML data. Workato uses this sample to generate the output datatree. |
| Encoding of the file content | Specify the encoding format for the XML file. If left blank, Workato defaults to **UTF-8**. |
| Document | Provide the XML data to parse. Workato extracts values based on the selected XML type and generates datapills for use in subsequent recipe steps. |

## Output

The parsed XML data appears as a structured datatree. The structure depends on the **XML type** selected.

For example, given the following XML input:

```xml
<list>
  <Contact>
      <Name type="C">
        <First>Donna</First>
        <Last>Noble</Last>
      </Name>
  </Contact>
  <Contact>
      <Name type="C">
        <First>Rose</First>
        <Last>Tyler</Last>
      </Name>
  </Contact>
</list>
```

The resulting datatree varies based on the **XML type**:

SIMPLE XML WITHOUT ATTRIBUTES

```shell
. List
  └── Contact
      ├── Name
      |   ├── Type (C)
      |   ├── First (Rose)
      |   └── Last (Tyler)
      ├── List size
      └── List index
```

FULL XML WITH ATTRIBUTES

```shell
. List
  ├── Contact
  |     ├── Name
  |     |   ├── Type (C)
  |     |   ├── First
  |     |   |     ├── Content (Rose)
  |     |   |     ├── List size
  |     |   |     └── List index
  |     |   ├── Last
  |     |   |     ├── Content (Tyler)
  |     |   |     ├── List size
  |     |   |     └── List index
  |     |   ├── List size
  |     |   └── List index
  |     ├── List size
  |     └── List index
  ├── List size
  └── List index
```

## Integrate XML into recipes

The **Parse XML document** action extracts structured data from XML, but some workflows require additional setup to ingest XML from external systems. Workato provides multiple ways to receive and process XML beyond parsing.

---
