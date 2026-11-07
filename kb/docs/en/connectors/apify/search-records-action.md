---
url: 'https://docs.workato.com/en/connectors/apify/search-records-action.md'
description: >-
  The Search records action retrieves public store Actors or the dataset items
  from a finished run in Apify.
---

# Apify - Search records action

The **Search records** action retrieves public store Actors or the dataset items from a finished run in Apify.

To run a public Actor with another action, enter the ID from the search results as a custom value in the **Actor** field.

## Input

Input fields are dynamically generated based on the object you select. The following input field is common to all objects. Refer to the [Apify API documentation](https://docs.apify.com/api/v2) for more information on available input fields.

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to search, such as **Actor** or **Dataset item**. |

## Output

Refer to the [Apify API documentation](https://docs.apify.com/api/v2) for more information on available objects and fields. The following output fields are common to all objects.

| Output field | Description |
| --- | --- |
| Records | The Actors or dataset items that match your search. |
| Total | Total number of records available. |
| Offset | Number of records skipped. |
| Limit | Maximum number of records returned. |
| Count | Number of records in this response. |
| Descending | Whether the results are in descending order. |

---
