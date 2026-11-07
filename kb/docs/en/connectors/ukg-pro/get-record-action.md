---
url: 'https://docs.workato.com/en/connectors/ukg-pro/get-record-action.md'
description: >-
  The Get record action in the UKG Pro connector retrieves a record, such as a
  person, employment, or job, from a UKG Pro instance.
---

# UKG Pro - Get record action

This action retrieves a record in your UKG Pro instance.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the UKG Pro object to retrieve: Person, Employment, Job, Contact, Compensation, PTO plan, Employee job history, Employee custom fields, General ledger, Pending hire |
| Employee identifier | Unique identifiers for the employee, including the **company code** and the **employee number**. |

## Output

| Output field | Description |
| --- | --- |
| Object-specific fields | Record details specific to the object type will be provided as datapills. Refer to the [UKG Pro API documentation](https://connect.ultipro.com/documentation#/api/) for more details on the output fields of each object. |

---
