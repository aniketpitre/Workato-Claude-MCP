---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/export-object-data-file.md
description: >-
  The Export object data (file) action in the HubSpot connector lets you bulk
  export object data and use the file in later recipe steps.
---

# HubSpot - Export object data action (file)

The **Export object data** action allows you to export data from HubSpot in bulk. You can use the downloaded file contents in subsequent recipe steps to upload the file into other applications.

## Input

| Input field | Description |
| --- | --- |
| Export type | Use the drop-down menu to select **VIEW** or **LIST** as the export type. |
| Export name | Provide a name for your export. |
| Language | Use the drop-down menu to choose **Select a language** (this option provides a list of languages for you to choose from) or **Enter a language** (this option allows you to manually enter the language you plan to use). |
| Object | Use the drop-down menu to choose **Select an object** or **Enter object ID**. You can select any standard HubSpot object, including contacts, companies, deals, and more. |

## Output

Workato returns a record representing each imported record. You can use these datapills in subsequent recipe steps.
