---
url: 'https://docs.workato.com/en/connectors/openapi/execute-operation-action.md'
description: Execute an operation via OpenAPI.
---

# OpenAPI - Execute operation action

The **Execute operation** action performs an operation using OpenAPI. The list of operations is dynamically generated based on the API endpoints found in the OpenAPI document. If an API endpoint doesn't match any Create, Get, Search, Update, or Delete actions, it is displayed in the [Execute operation action](https://restfulapi.net/).

![Execute operation action](/assets/openapi-execute-operation-action.B8H8-otw.png)_Execute operation action_

## Input

| Input fields | Description |
| --- | --- |
| OpenAPI document source | Define how to provide the OpenAPI document to the connector. Workato recommends loading it from a URL. Alternatively, you can copy and paste the contents of the file. |
| Server URL | Provide a URL to the target host or service, for example, `https://app.example.com` or `https://example.com/app`. Relative endpoint paths from the OpenAPI document are appended to the server URL to construct the full endpoint URL. |
| Operation | Select an object from the drop-down list of linked objects. |
| Filter operations | Select an item to filter the list of operations. |
| Operation name | Customize this operation by providing a more descriptive name. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/openapi/get-record-details-by-id-action.md
description: Retrieve the details of a record by ID via OpenAPI.
---

# OpenAPI - Get record details by ID action

The **Get record details by ID** action retrieves the details of a record by ID using OpenAPI. The list of objects is dynamically generated based on the API endpoints found in the [OpenAPI document](https://restfulapi.net/).

![Get record details by ID action](/assets/openapi-get-details-by-id-action.BI3FsBwZ.png)_Get record details by ID action_

## Input

| Input fields | Description |
| --- | --- |
| OpenAPI document source | Define how to provide the OpenAPI document to the connector. Workato recommends loading it from a URL. Alternatively, you can copy and paste the contents of the file. |
| Server URL | Provide a URL to the target host or service, for example, `https://app.example.com` or `https://example.com/app`. Relative endpoint paths from the OpenAPI document are appended to the server URL to construct the full endpoint URL. |
| Object | Select an object from the drop-down list of linked objects. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

---
