---
url: 'https://docs.workato.com/en/connectors/workday/get-business-object.md'
description: >-
  The Get business object details batch action retrieves records from a Workday
  custom object using batch queries.
---

# Workday - Get business object details (batch) action

The **Get business object details** batch action retrieves data from a Workday custom object. This action supports batch queries and adjusts input and output fields based on the selected **Business object**.

## Input

| Input field | Description |
| --- | --- |
| Business object | Choose the Workday custom object to query. For example, select **Applicants** to retrieve applicant records. |
| Fields with attributes | Select additional fields with custom attributes to include in the response. Available fields vary based on the selected **Business object**. |
| Fields with multiple values | Select fields that support multiple values (arrays or lists). Additional fields vary based on the selected **Business object**. |

Additional input fields appear based on the selected **Business object**.

## Output

| Output field | Description |
| --- | --- |
| Data | Contains the records returned from Workday based on the selected criteria. |
| Results | Contains metadata about the request, such as processing status or messages. |

The structure of **Data** varies depending on the selected **Business object** and selected fields.

---
