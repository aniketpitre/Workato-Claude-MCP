---
url: 'https://docs.workato.com/en/connectors/json-by-workato/parse-json-action.md'
description: >-
  This action parses raw JSON into structured datapills based on a sample
  document.
---

# JSON tools by Workato - Parse JSON document action

The **Parse JSON document** action extracts values from raw JSON content and converts them into structured datapills for use in recipes. It parses the input using a sample document to define the output schema.

This action supports spaces and special characters in key names. For example, Workato preserves key names like `Customer Name` instead of converting them to `Customer_Name`.

> **VERSION DEPRECATION**
> 
> A previous version of this action replaced spaces in JSON key names with underscores. That version is now deprecated. It remains available in existing recipes and continues to function without changes. New recipes use the updated version, which preserves original key names and reflects current datapill capabilities.
> 
> You can update an existing recipe step by selecting the **Parse JSON document** action and choosing the version without the **Deprecated** tag in the **Action** tab.

## Input

| Input field | Description |
| --- | --- |
| Sample document | Provide a sample JSON document that defines the expected structure of the input. Workato uses this to generate the output schema. |
| Document | Provide the raw JSON content to parse. This must match the structure of the sample document. |
| Encoding of the file content | Set the encoding format of the JSON string. If left blank, Workato uses **UTF-8** by default. |
| Edit schema | Select fields to override in the generated schema. Use this to refine the datatree if the sample doesn't fully reflect the actual data. |

## Output

| Output fields | Description |
| --- | --- |
| Document | Workato generates datapills based on the structure defined in the **Sample document**. These datapills reflect the hierarchy and keys of the sample JSON, including any nested objects or arrays. |

## Example usage

The following example defines a JSON structure for an array of contacts. Each contact includes a `Name` object, an `Address` object, and a `phone` field.

```json
[
  {
    "Name": {
      "first_name": "Sally",
      "last_name": "Jones"
    },
    "Address": {
      "street": "20450 Stevens Creek Blvd #150",
      "city": "Cupertino",
      "st": "CA",
      "postal": "95014"
    },
    "phone": "4105554119"
  },
  {
    "Name": {
      "first_name": "Bob",
      "last_name": "Towner"
    },
    "Address": {
      "street": "1 Hacker Way",
      "city": "Menlo Park",
      "st": "CA",
      "postal": "94025"
    },
    "phone": "8552982507"
  }
]
```

Use this structure in the **Sample document** field. Workato generates output datapills that reflect this structure, including nested fields under `Name` and `Address`.

---
