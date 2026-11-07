---
url: 'https://docs.workato.com/en/connectors/smartpm/delete-record-action.md'
description: The Delete record action enables you to delete a record in SmartPM.
---

# SmartPM - Delete record action

The **Delete record** action enables you to delete a record in SmartPM.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type for the record you plan to delete. Fields load dynamically based on your selection. |
| SmartPM ID | Enter the unique identifier of the record to delete. |

## Output

This action doesn't have any output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/smartpm/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action enables you to retrieve details of a
  specific record in SmartPM.
---

# SmartPM - Get record details by ID action

The **Get record details by ID** action enables you to retrieve details of a specific record in SmartPM.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve the details of a record. Fields load dynamically based on the object you select. |

For example, if you select the **Project** object, fields such as **Project ID** appear.

## Output

Output fields depend on the selected object. Use these fields to map datapills in downstream steps.

For example, if you select the **Project** object, the output includes fields such as the following:

| Output field | Description |
| --- | --- |
| ID | The unique identifier for the project. |
| Name | The name of the project. |
| Start date | The start date of the project. |
| Country | The country where the project is located. |
| City | The city where the project is located. |
| State | The state where the project is located. |
| Zip code | The zip code of the project's location. |
| Latitude | The latitude of the project's location. |
| Longitude | The longitude of the project's location. |
| Original scenario ID | The ID for the original scenario related to the project. |
| Default scenario ID | The ID for the default scenario related to the project. |
| Under construction | A flag indicating whether the project is currently under construction (`true` or `false`). |
| Project plan ID | The ID of the project plan associated with the project. |
| Project plan slot count | The number of slots in the project plan. |
| Weather station ID | The ID of the weather station associated with the project. |
| Company ID | The ID of the company associated with the project. |
| Source | The source from which the project data was obtained. |
| Data date | The date associated with the project data. |
| Metadata | Additional metadata related to the project. |

---
