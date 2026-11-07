---
url: 'https://docs.workato.com/en/connectors/ukg-pro/search-record-action.md'
description: >-
  The Search record action in the UKG Pro connector searches a UKG Pro instance
  and retrieves records that match your specified search criteria.
---

# UKG Pro - Search record action

This action searches your UKG Pro instance and retrieves records that match the search criteria.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the UKG Pro object to retrieve: Person details, Employment details, Employee contract details, Employee deductions, Beneficiaries, Compensation details, Contacts, Dependents, Employee changes, Company details, Code tables, Locations, Organization levels, Jobs, Deductions, Employee national documents, Global employee localization, Employee education, PTO plans, Employee job history details, Employee pay deduction details, International employees, Employee direct deposits, Pending hires |
| Object fields | Input fields for the object you selected will be shown. Provide values for the object-specified fields as the search criteria. |

## Output

The output to this action is a list of object records, including the **List size** and **List index**. The output datapills will be according the object specified in the input configuration.

| Output field | Description |
| --- | --- |
| Object-specific fields | Record details specific to the object type will be provided as datapills. Refer to the [UKG Pro API documentation](https://connect.ultipro.com/documentation#/api/) for more details on the output fields of each object. |

---
