---
url: 'https://docs.workato.com/en/connectors/outsystems/get-entity-by-id-action.md'
description: >-
  The Get entity by ID action in the OutSystems connector fetches a record from
  a module using the entity ID and record ID you provide.
---

# OutSystems - Get entity by ID action

The Get entity by ID action fetches entities based on the values you select for the action.

![Get entity by ID action](/assets/get-entity-by-id-action.2mNImCEe.png)_Get entity by ID action_

## Input

| Input field | Description |
| --- | --- |
| Module | Select the module where the record you plan to fetch is located. |
| Entity ID | Select the entity ID of the module. |
| Record ID | The ID of the record you plan to fetch. You can find the record ID in the OutSystems URL. |

## Output

| Output field | Description |
| --- | --- |
| Record | This entry contains information specific to the record attributes and other configurations you selected for the OutSystems object. This value is `null` if the record is blank. |

---
