---
url: 'https://docs.workato.com/en/connectors/eloqua/search-record.md'
description: >-
  The Search records action in the Eloqua connector lets you search standard or
  custom records using your own search criteria in Eloqua.
---

# Eloqua - Search records action

The action `Search records` allows you to search standard records or custom records in Eloqua. To begin, you will first need to select the object type of the record you want to search.

![Select Eloqua record](/assets/record-select-record.Cz5MWZNN.png)_You can select standard or custom objects_

## Input

When you select the object you want to search, you'll be able to build your own search criteria to search on standard or custom fields in any object.

![Search Eloqua records](/assets/search-record-field.CvVhXVS2.png)

| Input field | Description |
| --- | --- |
| Object | The object type. This can be standard or custom objects. |
| Search criteria | Build your own search query. Refer to the Eloqua [Using the search URL parameter](https://docs.oracle.com/en/cloud/saas/marketing/eloqua-develop/Developers/RESTAPI/Tutorials/search_parameter.htm?cshid=SearchParam) documentation for more information on building a search criteria. |
| Depth | Controls how much data is returned from Eloqua. Refer to the Eloqua [Request depth](https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/APIRequests_RequestDepth.html) documentation for more information. |
| Order by | Specifies how the records are ordered in the output. |
| Count | The number of records to be returned. Maximum is 1000. |
| Page | Used to paginate through large batches of records. |

## Output

When you select the object you want to search, output fields relevant to the object you have selected are displayed. This includes any custom fields you may have attached to any standard or custom object. The datapills correspond to the data of the records that have matched your search records.

![Eloqua record](/assets/search-record-output-field.CukIxXUD.png)

---
