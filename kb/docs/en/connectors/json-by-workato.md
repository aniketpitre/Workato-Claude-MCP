---
url: 'https://docs.workato.com/en/connectors/json-by-workato.md'
description: >-
  The JSON tools by Workato connector enables you to parse JSON documents and
  extract values into usable datapills from structured data sources.
---

# JSON tools by Workato

The JSON tools by Workato connector enables you to extract values from raw JSON content. This connector can process structured data stored in files or passed through other sources when Workato doesn't automatically expose the content as datapills.

## How JSON tools by Workato works

JSON tools by Workato provides the [Parse JSON document](/en/connectors/json-by-workato/parse-json-action) action, which parses a JSON document using a sample structure to define the output schema. The result is an array or object of usable datapills.

## Setup

JSON tools by Workato is a built-in connector. It doesn't require authentication or connection setup.

## Support for key names

The **Parse JSON** action supports spaces and special characters in key names. You can extract values from keys like `Customer Name` without automatic transformation to `Customer_Name`.

> **VERSION DEPRECATION**
> 
> A previous version of this action replaced spaces in JSON key names with underscores. That version is now deprecated. It remains available in existing recipes and continues to function without changes. New recipes use the updated version, which preserves original key names and reflects current datapill capabilities.
> 
> You can update an existing recipe step by selecting the **Parse JSON document** action and choosing the version without the **Deprecated** tag in the **Action** tab.

---
