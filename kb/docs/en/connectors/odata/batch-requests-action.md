---
url: 'https://docs.workato.com/en/connectors/odata/batch-requests-action.md'
description: >-
  The Batch requests action sends batch requests for multiple objects using
  Odata with Workato.
---

# OData - Batch requests action

The **Batch requests** action sends batch requests for multiple objects using one action in OData. Allowed operations are Get, Search, Update, Create, and Delete.

## Input

| Input fields | Description |
| --- | --- |
| Operation groups | Provide the operation group to perform batch requests. This includes, operation type and object for each item. |

## Output

| Output fields | Description |
| --- | --- |
| Response code | The response code indicating if the client connected to the server successfully. |
| Headers | Headers associated with the batch requested objects, such as content type, content length, cache control, and data service version. |
| Data | Data associated with the batch requested objects. |

---
