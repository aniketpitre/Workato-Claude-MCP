---
url: 'https://docs.workato.com/en/connectors/workato-edi/convert-data-format.md'
description: Use the Convert data action to convert data from JSON to X12 or X12 to JSON.
---

# Workato EDI - Convert data format action

Use the **Convert data format** action to convert JSON data into X12 format or X12 data into JSON format.

## Input

| Input field | Description |
| --- | --- |
| Data | Map in a datapill containing JSON or X12 data. For example, you can obtain a Transaction message from the output of a **Get record (Transaction message)** action. |
| Input data format | Specify the format of your source data. Available options are `JSON` and `EDI-X12`. |

## Output

| Output field | Description |
| --- | --- |
| EDI-X12 data or JSON data | The converted data. The data is in X12 or JSON format depending on the option selected. |

---
