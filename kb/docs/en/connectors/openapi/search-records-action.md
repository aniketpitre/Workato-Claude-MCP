---
url: 'https://docs.workato.com/en/connectors/openapi/search-records-action.md'
description: Search records via OpenAPI.
---

# OpenAPI - Search records action

The **Search records** action searches records using OpenAPI. The list of objects is dynamically generated based on the API endpoints found in the [OpenAPI document](https://restfulapi.net/).

![Search records action](/assets/openapi-search-record-action.Cd3gdICy.png)_Search records action_

## Input

| Input fields | Description |
| --- | --- |
| OpenAPI document source | Define how to provide the OpenAPI document to the connector. Workato recommends loading it from a URL. Alternatively, you can copy and paste the contents of the file. |
| Server URL | Provide a URL to the target host or service, for example, `https://app.example.com` or `https://example.com/app`. Relative endpoint paths from the OpenAPI document are appended to the server URL to construct the full endpoint URL. |
| Object | Select an object from the drop-down list of linked objects. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

---
