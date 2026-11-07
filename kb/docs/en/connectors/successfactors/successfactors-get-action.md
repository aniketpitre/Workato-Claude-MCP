---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-get-action.md
description: >-
  Use the Get record details action to retrieve a specific record by searching
  with its key columns in SAP SuccessFactors.
---

# SAP SuccessFactors - Get record details action

Retrieve the details of a specific record by searching using the key columns.

## Input

| Field | Description |
| --- | --- |
| Object | Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names. |
| Record key properties | The required inputs that identify a specific record. The fields shown depend on the selected object. Refer to [Record key properties](#record-key-properties) for more information. |
| Navigation fields | Select the related records to include in the output. Navigation fields appear only on objects with navigation properties. Refer to [Use navigation fields](/en/connectors/successfactors/successfactors-nav-fields) for more information. |
| Output fields | Workato fetches all available fields in the selected record by default. Use this input to filter for only the output fields you need. Optional field. |

### Record key properties

The record key properties are the required inputs that identify a specific record. The fields shown depend on the selected object's key definition:

- Single-key objects, such as **User**, display one input matching the key name. For example, **User ID** (`userId`).
- Composite-key objects, such as **Position**, display multiple required inputs. For example, **Code** (`code`) and **Effective start date** (`effectiveStartDate`).

Provide a value for all key inputs. The action returns an error if the record isn't found.

## Output

The output fields vary depending on the object you select. To view the available datapills, review the output datatree.

> **DateTime fields**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).
