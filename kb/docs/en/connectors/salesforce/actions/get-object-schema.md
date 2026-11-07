---
url: 'https://docs.workato.com/en/connectors/salesforce/actions/get-object-schema.md'
description: This action retrieves the schema of a standard or custom object in Salesforce.
---

# Salesforce - Get object schema action

This action retrieves the schema of a standard or custom object in Salesforce. Use this action when you need to replicate a Salesforce object's fields in a data warehouse.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the standard or custom object type to retrieve a schema from. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

| Output fields | Description |
| --- | --- |
| Object name | The name of the object. |
| Object label | The object's label. |
| Custom object? | Indicates whether the object is custom. |
| Fields | Contains information about the object's fields, such as the `Field name`, `Field label`, and `Type`. This contains only the fields that the connected account can view, as defined by their field-level security settings. |

Refer to the [Salesforce API documentation](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm) for more details on the fields returned.

The following example shows the output of retrieving the schema of a custom sObject named `Commission__c`:

Commission\_\_c custom sObject output

```json
{
   "name":"Commission__c",
   "label":"Commission",
   "custom":true,
   "fields":[
      {
         "name":"Id",
         "label":"Record ID",
         "custom":false,
         "length":18,
         "scale":0,
         "precision":0,
         "type":"string"
      },
      {
         "name":"OwnerId",
         "label":"Owner ID",
         "custom":false,
         "length":18,
         "scale":0,
         "precision":0,
         "type":"string"
      },
      {
         "name":"IsDeleted",
         "label":"Deleted",
         "custom":false,
         "length":0,
         "scale":0,
         "precision":0,
         "type":"boolean"
      },
      {
         "name":"Name",
         "label":"Commission Name",
         "custom":false,
         "length":80,
         "scale":0,
         "precision":0,
         "type":"string"
      },
      {
         "name":"CreatedDate",
         "label":"Created Date",
         "custom":false,
         "length":0,
         "scale":0,
         "precision":0,
         "type":"string"
      },
      {
         "name":"CreatedById",
         "label":"Created By ID",
         "custom":false,
         "length":18,
         "scale":0,
         "precision":0,
         "type":"string"
      },
      {
         "name":"LastModifiedDate",
         "label":"Last Modified Date",
         "custom":false,
         "length":0,
         "scale":0,
         "precision":0,
         "type":"string"
      },
      {
         "name":"LastModifiedById",
         "label":"Last Modified By ID",
         "custom":false,
         "length":18,
         "scale":0,
         "precision":0,
         "type":"string"
      },
      {
         "name":"SystemModstamp",
         "label":"System Modstamp",
         "custom":false,
         "length":0,
         "scale":0,
         "precision":0,
         "type":"string"
      },
      {
         "name":"Rate__c",
         "label":"Rate",
         "custom":true,
         "length":0,
         "scale":0,
         "precision":18,
         "type":"string"
      },
      {
         "name":"Name__c",
         "label":"Name",
         "custom":true,
         "length":0,
         "scale":0,
         "precision":18,
         "type":"double"
      },
      {
         "name":"User__c",
         "label":"User",
         "custom":true,
         "length":18,
         "scale":0,
         "precision":0,
         "type":"string"
      }
   ]
}
```

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/get-record-details.md
description: This action retrieves the details of a Salesforce record by its ID.
---

# Salesforce - Get record details by ID action

This action retrieves the details of a Salesforce record by its ID.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the standard or custom object type to retrieve. |
| Object ID | Enter the Salesforce ID of the object to retrieve. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

The output of this action varies based on the type of object you select.

---
