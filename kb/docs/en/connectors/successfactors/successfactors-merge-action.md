---
url: >-
  https://docs.workato.com/en/connectors/successfactors/successfactors-merge-action.md
description: >-
  The Merge record action in the SAP SuccessFactors connector updates specific
  properties in a record, leaving fields unchanged when no new value is given.
---

# SAP SuccessFactors - Merge record action

Update specific properties in a record.

If you do not provide a new value, the field value does not change.

Contrast this with the [Update action](/en/connectors/successfactors/successfactors-update-action); it sets the field to its default value if you do not provide a value.

## Input

- Object
  
- Select the SuccessFactors object. Because objects can have similar names, the list includes their internal names.
  
- Additional attributes
  
- Depending on the object you select and your SuccessFactors configuration, subsequent fields appear where you define additional attributes for the record, such as ID, start date, and status.
  

## Output

The output fields vary depending on the object you select. To view the available datapills, review the output datatree.

> **DateTime fields**
> 
> The system converts `DateTime` fields to UTC time. It infers the origin time zone from the instance's [environment time zone](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/2abbb39286994389bb0f1f4418773a7c/2f7f2877485d4b598cda2e00c5887fc4.html?locale=en-US), unless otherwise stated. Learn more about [Datatree and datapills](/en/workato-concepts#datatree-and-datapills).
