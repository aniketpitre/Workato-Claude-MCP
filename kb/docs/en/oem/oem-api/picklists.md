---
url: 'https://docs.workato.com/en/oem/oem-api/picklists.md'
description: >-
  Reference for the Embedded API endpoint that retrieves picklist values for a
  connection in a customer workspace.
---

# Embedded API - Picklists

Use the following endpoint to get picklist values of an Embedded customer. Refer to this [document](/en/oem/oem-api/picklist-parameters#picklist-names-parameters-by-adapter) to obtain picklist names and parameters for each connector.

## Rate limits

The picklist resource has the following rate limit:

| Type | Resource | Quota |
| --- | --- | --- |
| All | All [Picklists](/en/oem/oem-api/picklists.html) endpoints | 60 requests per minute |

## Get picklist values

Obtains a list of picklist values for a specified connection in an Embedded customer workspace.

<api-code no-copy-method>

```
POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections/:connection_id/pick_list
```

</api-code>

### URL Parameters

| Name | Type | Description |
| --- | --- | --- |
| managed\_user\_id | **string** _required_ | Embedded customer ID/external ID. External ID must be prefixed with an `E` (for example, `EA2300`) and the resulting ID should be URL encoded. |
| connection\_id | **string** _required_ | ID of the connection. This can be found in the URL of the app connection or is the result of the [List connections](/en/oem/oem-api/connections#list-connections) endpoint. |

### Body

| Name | Type | Description |
| --- | --- | --- |
| pick\_list\_name | **string** _required_ | Name of the pick list. Obtain from this [document](/en/oem/oem-api/picklist-parameters). |
| pick\_list\_params | **Object** _optional_ | Picklist parameters, required in some picklists. For more information view this [document](/en/oem/oem-api/picklist-parameters). |

#### Sample request

This example curl request obtains a list of Salesforce picklist values from the picklist `sobject_fields` from the `Invoice__c` custom object in Salesforce.

<api-code>

```shell
curl  -X POST https://YOUR_DATA_CENTER/api/managed_users/:managed_user_id/connections/:connection_id/pick_list \
      -H 'Authorization: Bearer <api_token>' \
      -H 'Content-Type: application/json' \
      -d '{ "pick_list_name": ":pick_list_name", "pick_list_params": {"sobject_name": ":sobject_name"}}'

```

</api-code>

### Response

```json
{
    "result": [
        [
            "Record ID",
            "Id"
        ],
        [
            "Owner ID",
            "OwnerId"
        ],
        [
            "Deleted",
            "IsDeleted"
        ],
        [
            "Invoice Name",
            "Name"
        ],
        [
            "Created Date",
            "CreatedDate"
        ],
        [
            "Created By ID",
            "CreatedById"
        ],
        [
            "Last Modified Date",
            "LastModifiedDate"
        ],
        [
            "Last Modified By ID",
            "LastModifiedById"
        ],
        [
            "System Modstamp",
            "SystemModstamp"
        ],
        [
            "Last Viewed Date",
            "LastViewedDate"
        ],
        [
            "Last Referenced Date",
            "LastReferencedDate"
        ],
        [
            "External ID",
            "External_ID__c"
        ],
        [
            "Status",
            "Status__c"
        ],
        [
            "Contact",
            "Contact__c"
        ],
        [
            "Intacct Invoice ID",
            "Intacct_Invoice_ID__c"
        ],
        [
            "Multi-select",
            "Multi_select__c"
        ],
        [
            "Invoiced",
            "Invoiced__c"
        ],
        [
            "Number field",
            "Number_field__c"
        ]
    ]
}
```

---
