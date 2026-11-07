---
url: 'https://docs.workato.com/en/connectors/eloqua/update-record.md'
description: >-
  The Update record action in the Eloqua connector lets you update standard or
  custom records by their internal ID in Eloqua.
---

# Eloqua - Update record action

The action `Update record` allows you to update standard records or custom records in Eloqua. To begin, you will first need to select the object type of the record you want to update.

![Select Eloqua record](/assets/record-select-record.Cz5MWZNN.png)_You can select standard or custom objects_

## Input

When you select the object you want to update, input fields relevant to the object you have selected are displayed. This includes any custom fields you may have attached to any standard or custom object.

> **Note**
> 
> To update a record in Eloqua, you will need the Eloqua internal ID of the record. This can be found via the search record action or via external IDs you might find in upstream systems.

![Eloqua record](/assets/update-record-field.DeEtAuvI.png)_A contact object will require a contact ID_

## Output

When you select the object you want to update, output fields relevant to the object you have selected are displayed. This includes any custom fields you may have attached to any standard or custom object. The datapills correspond to the data of the record in Eloqua you have just updated.

![Eloqua record](/assets/update-record-output-field.LwTEnjVD.png)

---
