---
url: 'https://docs.workato.com/en/connectors/soap/execute-operation-action.md'
description: >-
  The Execute operation action runs any web service operation defined in the
  SOAP WSDL document.
---

# SOAP - Execute operation action

The **Execute operation** action runs any web service operation defined in the SOAP WSDL document.

![Example input fields for the SOAP execute operation action](/assets/soap-execute-operation-input.B1w3up51.png)_Example input fields for the SOAP execute operation action_

| Input field | Description |
| --- | --- |
| Binding | Select the binding to define the protocol and message format for a set of operations. |
| Operation | Select the operation to specify methods or functions to call on the remote web service. The operations available vary depending on your selected **Binding**. |
| Response format | Select the format to use for the SOAP response. |
| Enable headers | Select whether to include SOAP headers in the request and response. |
| Header name | The name of the response header to include. Available if you select **Enable headers**. |
| Output field label | The field label in the response. Available if you select **Enable headers**. |
| Remove empty fields | Select `Yes` to automatically remove empty strings, empty arrays, empty objects, and null values from the request payload or `No` to preserve empty fields. |
| Parameters | Enter the parameters to use for the operation. The parameters available vary depending on your selected **Operation**. |

## Output

Output fields load dynamically based on the operation you select. Map the relevant datapill from the datatree to use output fields in downstream steps.

---
