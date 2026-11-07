---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-update-action.md
description: >-
  The Update record action in the SAP SuccessFactors connector updates a record
  with specified values, reverting omitted fields to their default values.
---

# SAP SuccessFactors - Update record action

Updates a record with specified values. If you do not provide a value for a field, that field reverts to its default value.

Contrast this with the [Merge action](/en/connectors/successfactors/successfactors-merge-action), that does not change the value of the field if you do not provide a new value.

## Input

- Object
  
- Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names.
  
- Object unique key
  
- Select the column that contains the object ID.
  
- Additional attributes
  
- Depending on the object you select and your SuccessFactors configuration, subsequent fields appear where you define additional attributes for the record, such as ID, start date, and status.
  
- You may also select additional optional attributes to update.
  
- A common attribute is a navigation field, which associates this record with other records through a URI, such as a user to their manager. See [Using navigation fields](/en/connectors/successfactors/successfactors-nav-fields.html).
  

## Output

The output fields vary depending on the object you select. To view the available datapills, review the output datatree.

> **DateTime fields**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).
