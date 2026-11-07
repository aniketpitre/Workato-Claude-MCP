---
url: 'https://docs.workato.com/en/connectors/ukg-pro/update-record-action.md'
description: >-
  The Update record action in the UKG Pro connector lets you update an existing
  record, such as a pending hire, in a UKG Pro instance.
---

# UKG Pro - Update record action

This action updates a record in your UKG Pro instance.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the UKG Pro object to update: Pending hire |
| Employee identifier | Unique identifiers for the employee, including the **company code** and the **employee number**. |
| Object fields | The input fields for the object you select will be shown. Provide values for the object-specified fields to update the record. |

## Output

| Output field | Description |
| --- | --- |
| Object-specific fields | Record details specific to the object type will be provided as datapills. Refer to the [UKG Pro API documentation](https://connect.ultipro.com/documentation#/api/) for more details on the output fields of each object. |

---
