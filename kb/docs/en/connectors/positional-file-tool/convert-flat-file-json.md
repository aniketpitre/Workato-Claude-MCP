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
