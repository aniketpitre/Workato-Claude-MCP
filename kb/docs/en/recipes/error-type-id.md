---
url: 'https://docs.workato.com/en/recipes/error-type-id.md'
description: >-
  Reference for Workato error type IDs and job error metadata fields used to
  detect, group, and target failures in Monitor actions for error blocks.
---

# Error type IDs

Error type IDs enable consistent error detection and response without parsing unstructured messages. Recipes use error type IDs to group related failures or target specific cases.

Workato surfaces structured metadata in job errors that you can reference in **Monitor actions for error** blocks.

| Field | Description |
| --- | --- |
| `error_type_id` | Stable identifier for the error type. |
| `error_type` | Display name for the error. |
| `error_id` | Unique identifier for the specific error instance. |
| `error_message` | High-level summary of what occurred. |

## Data format errors

These identifiers represent data serialization or parsing failures when transforming or reading payloads.

| Error | `error_type_id` | Description |
| --- | --- | --- |
| Avro serialization error | `err.data_format.avro_serialization_error` | Error encoding or decoding Avro data. |
| CSV parsing error | `err.data_format.csv_parsing_error` | Error parsing CSV content due to malformed structure or invalid delimiter. |
| JSON parsing error | `err.data_format.json_parsing_error` | Error parsing JSON payload due to invalid format or unescaped character. |
| XML parsing error | `err.data_format.xml_parsing_error` | Error parsing XML payload due to invalid tag or schema mismatch. |

---
