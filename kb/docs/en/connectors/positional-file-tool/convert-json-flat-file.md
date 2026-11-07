---
url: >-
  https://docs.workato.com/en/connectors/positional-file-tool/convert-json-flat-file.md
description: >-
  Use the Convert JSON to flat file action to convert JSON data structures into
  fixed-width positional flat files.
---

# Positional file tool - Convert JSON to flat file action

Use the **Convert JSON to flat file** action to convert JSON data structures into fixed-width positional flat files. You can define field paths, positions, lengths, data types, and formatting rules for each field. This action supports nested structures, arrays, and complex data hierarchies.

## Input

| Input field | Description |
| --- | --- |
| JSON Input | Provide the JSON content you plan to convert to flat file format. |
| Schema | Define schema templates for converting JSON data to flat file format. Each schema defines how to process a specific part of the JSON data. Click **...** (ellipses) to choose between a **Fixed list** or **Dynamic list** of schemas. Use a **Fixed list** when the total number of schema items and content is known. Use a **Dynamic list** if the schema items or content depend on another list. If you choose **Fixed list**, click **\+ Add schema template** to define additional schemas. |
| Schema source list (Schema) | Input a list datapill that contains the schemas for your JSON. Available for schemas configured with a **Dynamic list**. |
| Schema ID (Schema) | Provide a unique name for this schema, such as `header`, `detail`, or `customer`. |
| JSON field name (Schema) | Provide the JSON key to read for this schema. For example, `order`, or `items`. Leave empty to use the current or root object as the key. |
| Is array? (Schema) | Specify whether the JSON field is an array and each item should be processed one at a time. |
| Record type prefix (Schema) | Enter a prefix to identify the record type, such as `USER`, `HDR`, or `DTL`. The record type prefix is automatically added to the start of each line. |
| Field mappings (Schema) | Define how JSON fields map to fixed positions in the flat file output. Click **...** (ellipses) to choose between a **Fixed list** or **Dynamic list** of field mappings. Use a **Fixed list** when the total number of field mappings and content is known. Use a **Dynamic list** if the field mappings depend on another list. If you choose **Fixed list**, click **\+ Add field** to define additional field mappings. |
| Field mappings source list (Schema) (Field mappings) | Input a list datapill that contains field mappings. Available for field mappings configured with a **Dynamic list**. |
| JSON field name (Schema) (Field mappings) | Provide the JSON key to extract value from. For example, `customer_id` is extracted from `{"customer_id": "12345"}` and `name` is extracted from `{"name": "John"}`. Leave empty to use the default value. |
| Start position (Schema) (Field mappings) | Enter the start character position in the flat file line. `0` is the first character, while `10` is the second if the first field is `10` characters in length. |
| Field length (Schema) (Field mappings) | Enter the number of characters this field should occupy in the flat file. For example, you can specify that names are `15` characters and account numbers are `12`. |
| Data type (Schema) (Field mappings) | Select the data type of your JSON. Specify the correct data type to ensure proper formatting and control how numbers, dates, and text are converted. Use `number` for IDs, `decimal` for monetary values, and `string` for names. |
| Text alignment (Schema) (Field mappings) | Specify how to align the text within the fixed-width field. For example, you can use `Left` for names, `Right` for numbers, and `Center` for headers. |
| Padding character (Schema) (Field mappings) | Provide a character to fill empty space in the fixed-width field. For example, you can use `0` for numbers, space for text, and `A` for codes. |
| Default value (Schema) (Field mappings) | Provide a default field to use when a JSON field is empty or missing. For example, `N/A` for missing data, `0` for amounts, or `UNKNOWN` for missing names. |
| Child schemas (Schemas) | Specify child schemas when you require schema processing in a defined order. Child schemas are processed after the parent schema. Click **...** (ellipses) to choose between a **Fixed list** or **Dynamic list** of child schemas. Use a **Fixed list** when the total number of schema items and content is known. Use a **Dynamic list** if the child schema items or content depend on another list. If you choose **Fixed list**, click **\+ Add child** to define additional child schemas. |
| Child schemas source list (Schemas) (Child schemas) | Input a list datapill that contains child schemas. Available for child schemas configured with a **Dynamic list**. |
| Schema reference (Schemas) (Child schemas) | Provide the name of another schema defined in this list. |

## Output

| Output field | Description |
| --- | --- |
| Flat file content | The generated flat file content. |
| Individual lines | An array of text strings, where each string represents a single row in the flat file. |
| Total lines | The total number of lines in the flat file. |
