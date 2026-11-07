---
url: >-
  https://docs.workato.com/en/connectors/odata/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action enables you to get record details by
  searching by ID.
---

# OData - Get record details by ID action

The **Get record details by ID** action enables you to get record details by searching by ID. The list of objects is dynamically generated based on the API endpoints found in the OData document.

## Input

Additional input fields load dynamically based on the OData document source you select.

| Input fields | Description |
| --- | --- |
| OData document source | Select the type of OData document source. |
| Document URL | The publicly accessible URL for the OData document to use. |
| Server URL | Enter the URL to the target host or service. Relative endpoint paths from the OData document are appended to the Server URL to construct the full endpoint URL. |
| Object | Select the object to get record details for. |
| Custom headers | Add any required customer headers. |
| Select | Select or enter properties to return in the output. |
| Expand | Select or enter a value to expand related entities. |

## Output

Output fields load dynamically based on the document source you select.
