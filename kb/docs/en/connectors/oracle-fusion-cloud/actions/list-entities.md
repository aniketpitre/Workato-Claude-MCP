---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/list-entities.md
description: >-
  The List entities action retrieves the list of service data objects associated
  with the ERP Integration Service.
---

# Oracle Fusion Cloud - List entities action

The **List entities** action retrieves the list of service data objects associated with the ERP Integration Service.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

This action doesn't require any input.

## Output

| Output field | Description |
| --- | --- |
| Entities | An array of entity objects containing information about available business entities in Oracle Fusion Cloud. |
| Name (Entities) | The name of the entity or business object. |
| Type name (Entities) | The technical type name or classification of the entity. |
| Can create (Entities) | Indicates whether the entity supports create operations. |
| Can update (Entities) | Indicates whether the entity supports update operations. |
| Can merge (Entities) | Indicates whether the entity supports merge operations. |
| Can delete (Entities) | Indicates whether the entity supports delete operations. |
