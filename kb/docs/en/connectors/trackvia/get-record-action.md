---
url: 'https://docs.workato.com/en/connectors/trackvia/get-record-action.md'
description: >-
  The Get record action in the TrackVia connector retrieves a single record by
  its ID from a selected application and view.
---

# TrackVia - Get record action

The **Get record** action retrieves a TrackVia record by its ID.

## Input

| Input field | Description |
| --- | --- |
| Application | Select the TrackVia application that contains the record you plan to retrieve. |
| View | Select the TrackVia view that contains the record you plan to retrieve. A TrackVia view is a set of filters and customizations linked to a data table in TrackVia. |
| ID | Specify the TrackVia ID of the record you plan to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| Record ID | The TrackVia ID of the record. |
| ID | A numerical identifier indicating the creation order of records. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> The **Get record** action generates additional output fields that contain values, metadata, or associated properties for each record element in your selected TrackVia **View**. Refer to TrackVia's [Field Types](https://help.trackvia.com/hc/en-us/articles/8811398834971-Field-Types) guide for more information on the elements of TrackVia records.

---
