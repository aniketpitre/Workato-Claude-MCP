---
url: 'https://docs.workato.com/en/connectors/positional-file-tool/build-flat-file.md'
description: >-
  Use the Build flat file action to generate a fixed-width flat file from an
  array of rows.
---

# Positional file tool - Build flat file action

Use the **Build flat file** action to generate a fixed-width flat file from an array of rows. This action returns the flat file content as a single text blob, which you can store with the [Create file in Workato FileStorage](/en/features/filestorage/create-file-action) action.

## Input

| Input field | Description |
| --- | --- |
| Rows to output | Provide an array of row objects as a JSON string. For example, `[{"field1": "value1"}, {"field1": "value2"}]`. |
| Column layout | Define the column layout for the flat file. Click **...** (ellipses) to choose between a **Fixed list** or **Dynamic list**. Use a **Fixed list** when the column items and content are known. Use a **Dynamic list** when the column items and content depend on another list. |
| Column layout source list (Column layout) | Input a list datapill that contains the column layout. Available for column layouts configured with a **Dynamic list**. |
| Field name (Column layout) | Enter a name for this field. |
| Start position (Column layout) | Provide the 0-based start position for the field. |
| Length (Column layout) | Enter the number of characters allocated to the field. |
| Padding character | Provide a padding character. This defaults to space. |
| Pad direction | Specify whether to pad values on the right or left. The default pad direction is right. |

## Output

| Output field | Description |
| --- | --- |
| Flat file content | The content of the generated flat file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/positional-file-tool/convert-flat-file-json.md
description: >-
  Use the Convert flat file to JSON action to parse positional flat files and
  convert them to structured JSON.
---

# Positional file tool - Convert flat file to JSON action

Use the **Convert flat file to JSON** action to parse positional flat files and convert them to structured JSON. This action supports fixed width or dynamic width files, single schema (uniform rows) or multiple schemas (varied row structures), and fixed lists or dynamic lists for column definitions.

## Input

The available input fields vary based on your schema configuration.

### Input for files with a single schema

| Input field | Description |
| --- | --- |
| File content | Provide the content of the positional file to parse. For example, `HDR001,JohnSmith,USA20240401`. |
| Schema type | Select the schema type that matches your file. Select **Single schema** if all rows share the same structure. Select **Multiple schemas** if the file contains rows with different structures. |
| File structure | Select **Fixed width** if columns use specific delimiters. Select **Dynamic width** if columns have inconsistent spacing. |
| Output | Define the expected output structure of the file. The parser maps its output to this definition. You can input JSON or add fields manually. |
| Delimiter | Select the character that separates fields in the file. Options include `comma` (`,`), `space`, `tab`, `colon` (`:`), `semicolon` (`;`), and `pipe` (`|`). Available for **Fixed width** file structures. |
| Columns | Define the fields in the order they appear in the file. Each entry represents one column in the flat file. Click the **...** (ellipses) to choose between a **Fixed list** or **Dynamic list**. Use a **Fixed list** when the total number of items and their content are known. Use a **Dynamic list** if the number of items and their content depend on another list. If you choose **Fixed list**, click **\+ Add item** to add more fields. |
| Columns source list (Columns) | Input a list datapill. Available for files with column structures that use **Dynamic lists**. |
| Field name (Columns) | Provide the name for this column in the parsed JSON output. Available for files with column structures that use **Dynamic lists**. |
| Field name (Columns) (Item #{N}) | Provide the field name for each item in the list. Click **\+ Add item** to add more column fields. |
| Start position (Columns) (Item #{N}) | Define the start index position in the flat string for this field. The first character is `0`. Available for **Dynamic width** file structures and files with column structures that use **Fixed lists**. |
| Length (Columns) (Item #{N}) | Specify the number of characters this field uses in the flat file. Available for **Dynamic width** file structures and files with column structures that use **Fixed lists**. |

### Input for files with multiple schemas

Files with multiple schemas require you to select an output structure. The available input fields depend on your selection:

- **Linear fields**: Produces flat output where all schemas are at the same level
- **Child fields**: Creates nested output with parent-child relationships between record types

#### Common configuration fields

The following input fields are common to **Linear** and **Child** field structures.

| Input field | Description |
| --- | --- |
| File content | Provide the content of the positional file to parse. For example, `HDR001,JohnSmith,USA20240401`. |
| Schema type | Select the schema type that matches your file. Select **Single schema** if all rows share the same structure. Select **Multiple schemas** if the file contains rows with different structures. |
| File structure | Select **Fixed width** if columns use specific delimiters. Select **Dynamic width** if columns have inconsistent spacing. |
| Output structure | Select **Linear fields** for flat output or **Child fields** for nested output with parent-child relationships between record types. |
| Output | Define the expected output structure of the file. The parser maps its output to this definition. You can input JSON or add fields manually. |

#### Linear fields configuration

Use these fields when you select **Linear fields** as your output structure.

| Input field | Description |
| --- | --- |
| Schema identifier position | Define the position of the schema identifier in each row. |
| Start position (Schema identifier position) | Provide the index where the schema identifier starts in the line. The first character is `0`. |
| Length (Schema identifier position) | Enter the number of characters the schema identifier spans. |
| Join schemas? | Select Yes if you want to join rows from different schemas by a unique key in the output. If Yes, define the unique key in the column specification for each schema. |
| Schemas | Define schemas for parsing the flat file. Click **...** (ellipses) to choose between a **Fixed list** or **Dynamic list**. Use a **Fixed list** when the schema items and content are known. Use a **Dynamic list** when the schema items and content depend on another list. |
| Schemas source list (Schemas) | Input a list datapill. Available for schemas configured with a **Dynamic list**. |
| Schema name (Schemas) | Provide a unique name for this schema. |
| Schema identifier (Schemas) | Provide the identifier value that marks rows belonging to this schema. |
| Column specification (Schemas) | Define the columns for this schema. Click **...** (ellipses) to choose between a **Fixed list** or **Dynamic list**. Use a **Fixed list** when the column items and content are known. Use a **Dynamic list** when the column items and content depend on another list. |
| Column specification source list (Schemas) (Column specification) | Input a list datapill. Available for column specifications configured with a **Dynamic list**. |
| Field name (Schemas) (Column specification) | Provide the name to assign to this column in the output JSON. |
| Start position (Schemas) (Column specification) | Provide the index where this field starts in the line. The first character is `0`. |
| Length (Schemas) (Column specification) | Enter the number of characters this field spans. |
| Is unique key? (Schemas) (Column specification) | Select Yes if this field serves as the unique key for joining schemas. |

#### Child fields configuration

Use these fields when you select **Child fields** as your output structure.

| Input field | Description |
| --- | --- |
| Row types | Define row types for parsing the flat file. Click **...** (ellipses) to choose between a **Fixed list** or **Dynamic list**. Use a **Fixed list** when the row type items and content are known. Use a **Dynamic list** when the row type items and content depend on another list. |
| Row types source list (Row types) | Input a list datapill. Available for row types configured with a **Dynamic list**. |
| Schema identifier (Row types) | Provide a unique identifier for this row type schema. |
| Columns (Row types) | Define the columns for this row type. Click **...** (ellipses) to choose between a **Fixed list** or **Dynamic list**. Use a **Fixed list** when the column items and content are known. Use a **Dynamic list** when the column items and content depend on another list. |
| Columns source list (Row types) (Columns) | Input a list datapill. Available for columns configured with a **Dynamic list**. |
| Field name (Row types) (Columns) | Provide the name to assign to this column in the output JSON. |
| Start position (Row types) (Columns) | Provide the index where this field starts in the line. The first character is `0`. |
| Length (Row types) (Columns) | Enter the number of characters this field spans. |
| Child row types (Row types) | Define child row types that are processed after the parent row type. Click **...** (ellipses) to choose between a **Fixed list** or **Dynamic list**. Use a **Fixed list** when the child row type items and content are known. Use a **Dynamic list** when the child row type items and content depend on another list. |
| Child row types source list (Row types) (Child row types) | Input a list datapill. Available for child row types configured with a **Dynamic list**. |
| Schema name (Row types) (Child row types) | Provide the name of the child schema. Must match one of the defined schema names. |

## Output

The output for this action is a JSON object that matches the structure you defined in the **Output** input field. The format varies based on your configuration:

- **Single schema**: Flat array of objects, one per row
- **Linear fields**: Flat array where each object includes its schema identifier
- **Child fields**: Hierarchical structure with nested parent-child relationships

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/positional-file-tool/create-flat-file-streaming-action.md
description: >-
  The Create flat file (streaming) action creates a positional flat file from
  streaming CSV or JSON input in Positional file tool.
---

# Positional file tool - Create flat file (streaming) action

The **Create flat file (streaming)** action creates a positional flat file from streaming CSV or JSON input in Positional file tool.

## Input

| Input field | Description |
| --- | --- |
| Streaming content | Enter streaming content datapills from a file connector in CSV or JSON format. |
| Streaming input format | Select the format of the streaming input. Options are `CSV` or `JSON`. |
| Chunk size (MB) | Select the chunk size, in MB, to stream. |
| Line ending | Select the line ending character for the output flat file. |
| Merge flat file output? | Select `Yes` or `No` to decide to merge all schemas with the flat file output into a single file. |
| Schemas | Fields to define columns for the schema. Schema fields include `Schemas source list`, `Schemas fields`, `Schema name`, `Data source`, `Output destination`, `Upload URL`, and `Column specification`. |

## Output

| Output field | Description |
| --- | --- |
| Total lines generated | The total number of lines in the response flat file. |
| Total chunks processed | The total number of chunks processed in the streaming flat file. |
| Status | The status of the flat file response. |

---

---
url: >-
  https://docs.workato.com/en/connectors/positional-file-tool/parse-flat-file-streaming-action.md
description: >-
  The Parse flat file (streaming) action parses large positional flat files in
  chunks in Positional file tool.
---

# Positional file tool - Parse flat file (streaming) action

The **Parse flat file (streaming)** action parses large positional flat files in chunks in Positional file tool.

## Input

| Input field | Description |
| --- | --- |
| File content | Enter file content datapills from a connector. |
| Chunk size (MB) | Select the chunk size, in MB, to stream. |
| Merge file storage output? | Select `Yes` or `No` to decide to merge all schemas with the flat file output into a single file. |
| Output format | Select the format of the output. Options are `CSV` or `JSON`. |
| Record position validations | Optional. Enter a record you expect to appear at a selected line or line range. Each record entry includes an `Identifier value` and a `Line / range`. Enable `Strict match` to require every line in a range to match, instead of one line. The action fails if a validation isn't met. Blank lines aren't counted, and validation is skipped if left empty. |
| Schemas | Fields to define columns for the schema. Schema fields include `Schema name`, `Identifier start position`, `Identifier length`, `Identifier value`, `Output destination`, `Upload URL`, and `Column specification`. |

## Output

| Output field | Description |
| --- | --- |
| Total lines processed | The total number of lines processed in the response flat file. |
| Total chunks processed | The total number of chunks processed in the streaming flat file. |
| Status | The status of the flat file response. |

---

---
url: >-
  https://docs.workato.com/en/connectors/positional-file-tool/trim-csv-file-streaming-action.md
description: >-
  The Trim CSV file (streaming) action streams a large delimited file in chunks
  and splits it into row-range sections, such as header, detail, and trailer
  rows.
---

# Positional file tool - Trim CSV file (streaming) action

The **Trim CSV file (streaming)** action streams a large delimited file in chunks and splits it into row-range sections, such as header, detail, and trailer rows.

## Input

| Input field | Description |
| --- | --- |
| File content | Enter file content datapills from a connector. |
| Chunk size (MB) | Select the chunk size, in MB, to stream. |
| Schemas | Enter fields to define one or more row-range sections of the file. Schema fields include `Schema name`, `Start row`, `End row`, `Delimiter`, `Output destination`, and `Upload URL`. |
| Column names | Define column names for a schema's action output. Optionally, set a `Default value` per column. When a row is missing a value for that column (blank or absent), the default value is used instead. Applies to action output and CSV file output, though defaults on CSV output only apply when the delimiter is a comma. |

## Output

| Output field | Description |
| --- | --- |
| Total lines processed | The total number of lines processed in the response file. |
| Total chunks processed | The total number of chunks processed while streaming the file. |
| Status | The status of the file response. |

---
