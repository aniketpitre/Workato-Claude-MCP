---
url: 'https://docs.workato.com/en/connectors/smartpm/search-records-action.md'
description: >-
  The Search records action enables you to retrieve a list of records that match
  your search criteria from SmartPM.
---

# SmartPM - Search records action

The **Search records** action enables you to retrieve a list of SmartPM records that match your search criteria.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve a list of records. Fields load dynamically based on the object you select. |

For example, if you select the **Project** object, input fields such as **As of** and **Filters** appear.

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
