---
url: 'https://docs.workato.com/en/connectors/ukg-pro-rest/import-data-action.md'
description: >-
  The Import data action submits an encoded XML transaction to UKG Pro's Import
  Tool.
---

# UKG Pro - Import data action

The **Import data** action submits an encoded XML transaction to UKG Pro's Import Tool.

## Input

| Input field | Description |
| --- | --- |
| Schema | Provide the XML schema. You can retrieve the XML schema from **Menu > Administration > Integration Studio > Import Tool > Configurations > Validate > Show Schema Options** in UKG Pro. |
| Transaction | Provide the XML transaction. |
| Unique file name | Enter the name of the file. |
| Time limit | Enter the maximum length in minutes the action can run. |

## Output

| Output field | Description |
| --- | --- |
| Is complete? | Indicates whether the import process is complete. |
| Status | The status of the **Import data** action within UKG Pro. |
| Staging ID | A unique identifier for the record in the staging system before final processing. |
| Data | Contains the raw or processed data related to the import. |
| File process date | The date when the file containing data was processed. |
| Service submittal date | The date when the data was submitted to the UKG Pro service. |
| Last repost date | The most recent date the data was resubmitted or reposted in the system. |
| Employee name | The full name of the employee. |
| Employee number | A unique employee identifier. |
| Transaction | The type of transaction. |
| File name | The name of the file. |
| Messages | Any system-generated messages related to the processing of the imported data, including errors or confirmations. |
| Child transaction statuses | The statuses of any sub-transactions related to the main transaction. |
| Error | Describes any errors encountered during the processing or importing. |

---
