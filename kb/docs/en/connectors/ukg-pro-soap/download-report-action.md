---
url: 'https://docs.workato.com/en/connectors/ukg-pro-soap/download-report-action.md'
description: >-
  The Download report action downloads a preconfigured report from your UKG Pro
  instance.
---

# UKG Pro (SOAP) - Download report action

The **Download report** action downloads a preconfigured report from your UKG Pro instance.

## Input

Input fields load dynamically based on the selected report.

| Input field | Description |
| --- | --- |
| Report path | Select the report to retrieve. |
| Delimiter | Select the delimiter for the report from the drop-down menu. Options include `XML`, `Comma-separated values`, `Tab-separated values`, and `Space-separated values`. |

## Output

| Output field | Description |
| --- | --- |
| Report | The report object. The report is formatted according to the delimiter specified in the action configuration. Use the corresponding [Workato tool](/en/handling-files-and-attachments) to parse the report. |

---
