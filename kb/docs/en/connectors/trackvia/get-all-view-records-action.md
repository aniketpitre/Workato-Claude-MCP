---
url: 'https://docs.workato.com/en/connectors/trackvia/get-all-view-records-action.md'
description: >-
  The Get all view records action in the TrackVia connector retrieves records
  matching your search criteria from a view and processes them in batches.
---

# TrackVia - Get all view records action (Batch)

The **Get all view records** batch action retrieves a list of TrackVia records matching the criteria you specify and processes them in batches.

## Input

| Input field | Description |
| --- | --- |
| Application | Select the TrackVia application that contains the view you plan to search. |
| View | Select the TrackVia view you plan to search. A TrackVia view is a set of filters and customizations linked to a data table in TrackVia. |
| Search text | Provide the text to search for in the selected view's records. |

## Output

This action returns the following output fields:

> **MAXIMUM OUTPUT LENGTH**
> 
> The **Get all view records** batch action retrieves a maximum of 1000 records from TrackVia per batch.

| Output field | Description |
| --- | --- |
| Record ID | The TrackVia ID of the record. |
| ID | A numerical identifier indicating the creation order of records. |
| List size | The number of records retrieved. |
| List index | The position of the current record within the index. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> The **Get all view records** batch action generates additional output fields that contain values, metadata, or associated properties for each record element in your selected TrackVia **View**. Refer to TrackVia's [Field Types](https://help.trackvia.com/hc/en-us/articles/8811398834971-Field-Types) guide for more information on the elements of TrackVia records.

---
