---
url: 'https://docs.workato.com/en/connectors/trackvia/new-record-trigger.md'
description: >-
  The New record trigger in the TrackVia connector fires in real time when new
  records are created in a selected TrackVia application and view.
---

# TrackVia - New record trigger

The **New record** trigger monitors TrackVia in real-time for newly created records.

## Input

| Input field | Description |
| --- | --- |
| Application | Select the TrackVia application that contains the view you plan to monitor. |
| View | Select the TrackVia view you plan to monitor for newly created records. A TrackVia view is a set of filters and customizations linked to a data table in TrackVia. |

## Output

| Output field | Description |
| --- | --- |
| Record ID | The TrackVia ID of the record. |
| ID | A numerical identifier indicating the creation order of records. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> The **New record** trigger generates additional output fields that contain values, metadata, or associated properties for each record element in your selected TrackVia **View**. Refer to TrackVia's [Field Types](https://help.trackvia.com/hc/en-us/articles/8811398834971-Field-Types) guide for more information on the elements of TrackVia records.

---
