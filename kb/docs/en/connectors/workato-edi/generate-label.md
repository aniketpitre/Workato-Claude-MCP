---
url: 'https://docs.workato.com/en/connectors/workato-edi/generate-label.md'
description: Use the Generate label action create a custom shipping label.
---

# Workato EDI - Generate label action

Use the **Generate label** action to create a custom label in PDF or ZPL format. You can send the resulting file to a compatible printer to print a shipping label.

## Input

| Input fields | Description |
| --- | --- |
| Payload | Provide the JSON body used to generate a label. See [Orderful’s documentation](https://docs.orderful.com/reference/labelcontroller_generate) for details on the accepted input. |
| Skip validation | Determine whether to validate the JSON data. Select `Yes` to skip validating the JSON data or `No` to validate the provided JSON. |
| Format | Determine the format for the finished label. Available options include `PDF` and `ZPL`. |

## Output

| Output field | Description |
| --- | --- |
| Label | The generated label in hexadecimal-encoded bytes. |

---
