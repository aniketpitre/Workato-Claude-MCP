---
url: 'https://docs.workato.com/en/connectors/trackvia/update-record-action.md'
description: >-
  The Update record action in the TrackVia connector updates a record you
  specify by its ID in a selected application and view.
---

# TrackVia - Update record action

The **Update record** action updates a record you specify in TrackVia.

## Input

| Input field | Description |
| --- | --- |
| Application | Select the TrackVia application that contains the record you plan to update. |
| View | Select the TrackVia view that contains the record you plan to update. A TrackVia view is a set of filters and customizations linked to a data table in TrackVia. |
| ID | Specify the TrackVia ID of the record you plan to update. |
| Record | Optional. Enter new details for the object. This field contains a sub-field for each record element in your selected TrackVia **View**. |

## Output

| Output field | Description |
| --- | --- |
| Record ID | The TrackVia ID of the record. |
| ID | A numerical identifier indicating the creation order of records. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> The **Update record** action generates additional output fields that contain values, metadata, or associated properties for each record element in your selected TrackVia **View**. Refer to TrackVia's [Field Types](https://help.trackvia.com/hc/en-us/articles/8811398834971-Field-Types) guide for more information on the elements of TrackVia records.

---

---
url: >-
  https://docs.workato.com/en/connectors/trackvia/upload-file-to-a-record-action.md
description: >-
  The Upload file to a record action in the TrackVia connector uploads a file to
  a specified field in a record you select.
---

# TrackVia - Upload file to a record action (File)

The **Upload file to a record** action uploads a file to a record you specify in TrackVia.

## Input

| Input field | Description |
| --- | --- |
| Application | Select the TrackVia application that contains the record you plan to upload a file to. |
| View | Select the TrackVia view that contains the record you plan to upload a file to. A TrackVia view is a set of filters and customizations linked to a data table in TrackVia. |
| Field name | Select the specific field in the record you plan to upload a file to. |
| ID | Specify the TrackVia ID of the record you plan to upload a file to. |
| Content | Provide the content of the file you plan to upload. |
| Content type | Select the file type you plan to upload. |
| File name | Provide a name for the file. |

## Output

| Output field | Description |
| --- | --- |
| Record ID | The TrackVia ID of the record. |
| ID | A numerical identifier indicating the creation order of records. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> The **Upload file to a record** action generates additional output fields that contain values, metadata, or associated properties for each record element in your selected TrackVia **View**. Refer to TrackVia's [Field Types](https://help.trackvia.com/hc/en-us/articles/8811398834971-Field-Types) guide for more information on the elements of TrackVia records.

---
