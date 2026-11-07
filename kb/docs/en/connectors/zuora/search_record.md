---
url: 'https://docs.workato.com/en/connectors/zuora/search_record.md'
description: >-
  The Search record action in the Zuora connector lets you search records by
  object type using dynamically generated search parameters.
---

# Zuora - Search record action

## Search record action

This action searches for records in Zuora. First, select the object type in Zuora after which Workato will generate the possible search parameters. Ensure that the Zuora connector is configured to the latest WSDL SOAP API version. Earlier WSDL versions may not be compatible.

![Search record action](/assets/search_record_action.DwNIxAbl.gif)_Search parameters are dynamically generated based on the object selected._

### Input

| Field | Description |
| --- | --- |
| Object | Select the object type in Zuora you hope to create. |
| Object-level Search parameters fields | All relevant object input fields. Required input fields will be highlighted. Take note that the ID in the response from the [create record action](/en/connectors/zuora/create_record.html) or the [update record action](/en/connectors/zuora/update_record.html) should be matched to the ID search parameter. |

### Output

| Field | Description |
| --- | --- |
| Array of records | An array of records where the attributes returned for each record change dynamically based on the object you have selected. |

---
