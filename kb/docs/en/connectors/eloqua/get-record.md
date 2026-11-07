---
url: 'https://docs.workato.com/en/connectors/eloqua/get-record.md'
description: >-
  The Get records action in the Eloqua connector lets you retrieve the details
  of a standard or custom record by ID in Eloqua.
---

# Eloqua - Get records action

The action `Get record details` allows you to retrieve the details of a standard record or custom record in Eloqua. To begin, you will first need to select the object type of the record you want to retrieve.

![Select Eloqua record](/assets/record-select-record.Cz5MWZNN.png)_You can select standard or custom objects_

## Input

When you select the object you want to retrieve, you'll be prompted to provide the ID of the record in question.

![Get Eloqua records](/assets/get-record-field.uG7S1nS3.png)

| Input field | Description |
| --- | --- |
| Object | The object type. This can be standard or custom objects. |
| ID | The ID of the record. |
| Depth | Controls how much data is returned from Eloqua. Refer to the Eloqua [Request depth](https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/APIRequests_RequestDepth.html) documentation for more information. |

## Output

When you select the object you want to retrieve, output fields relevant to the object you have selected are displayed. This includes any custom fields you may have attached to any standard or custom object. The datapills correspond to the data of the records that have matches the ID you have provided.

![Eloqua record](/assets/get-record-output-field.hGxaNXWi.png)

---
