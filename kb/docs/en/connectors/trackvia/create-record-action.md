---
url: 'https://docs.workato.com/en/connectors/trackvia/create-record-action.md'
description: >-
  The Create record action in the TrackVia connector creates a new record in a
  selected TrackVia application and view.
---

# TrackVia - Create record action

The **Create record** action creates a new object in TrackVia.

## Input

| Input field | Description |
| --- | --- |
| Application | Select the TrackVia application where you plan to create the new object. |
| View | Select the TrackVia view where you plan to create the new object. A TrackVia view is a set of filters and customizations linked to a data table in TrackVia. |
| Record | Optional. Enter details for the new object. This field contains a sub-field for each TrackVia element in your selected **View**. |

## Output

| Output field | Description |
| --- | --- |
| Record ID | The TrackVia ID of the record. |
| ID | A numerical identifier indicating the creation order of records. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> The **Create record** action generates additional output fields that contain values, metadata, or associated properties for each record element in your selected TrackVia **View**. Refer to TrackVia's [Field Types](https://help.trackvia.com/hc/en-us/articles/8811398834971-Field-Types) guide for more information on the elements of TrackVia records.

---
