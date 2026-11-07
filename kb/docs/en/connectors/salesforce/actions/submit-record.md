---
url: 'https://docs.workato.com/en/connectors/salesforce/actions/submit-record.md'
description: This action submits a record for approval in Salesforce.
---

# Salesforce - Submit record for approval action

This action submits a record for approval in Salesforce. This action is equivalent to clicking `Submit for approval` on a record in Salesforce.

![Submitted for approval](/assets/approval-submitted.CW3hUSC6.png)_An Invoice record submitted for approval_

## Input

| Input fields | Description |
| --- | --- |
| Approval process | Select an approval process from the drop-down. Alternatively, use the drop-down menu to select **Use process definition unique name or ID** and enter the unique name (for example, `Invoice_discount_approval`) or ID (for example, `04a1K000000PnvP`) of the process. The unique name and ID are available on the Salesforce **Approval process** page. |
| Record ID | Enter the ID of the record to submit for approval. You can use a datapill from a previous step where a Salesforce record is created or updated. |
| Approver ID | Enter the Salesforce ID of an approver. This is required if the process is not auto-approved and if an approver is not selected by default. |
| Submitter ID | Enter the ID of the user to associate with the submission. |
| Comments | Enter comments to include with the submission. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

![Submit record for approval input](/assets/submit-record-input.B3GgaBmH.png)_The Submit record for approval action_

## Output

| Output fields | Description |
| --- | --- |
| Record ID | The Salesforce ID of the record. |
| Status | The status of the record's approval. |
| Approval request ID | The Salesforce ID of the approval request. |
| Success | Indicates whether the record was processed successfully. |
| Errors | An object containing any errors that occurred. |

After Workato submits the record, its approval status in the Salesforce Approval History becomes `Pending`.

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/update-records-in-batches.md
description: This action updates Salesforce records in batches.
---

# Salesforce - Update records in batches action (batch)

This action updates Salesforce records in batches. Each batch can update up to 2,000 records in 10 batches of 200.

![Update record in batch](/assets/batch-update-action.r3XJnxX0.png)_Update records in batches action_

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the standard or custom object type to update. |
| Batch size | Enter the number of records to process in each batch. The minimum value is `1`, the maximum and default is `200`. |
| Advanced configuration | Select whether to roll back records if an operation fails. Refer to the [Advanced configuration](#advanced-configuration) section for more information. |

Additional fields load dynamically based on the selected object. Use these fields to enter a source list and configure the updated records.

You can obtain a source list from various locations, such as a new CSV file in a file storage app, including Box, Amazon S3, and On-prem files. Refer to the [List management](/en/features/list-management) documentation for more information about list inputs.

![Select object](/assets/salesforce-batch-select-object-pill.BVXFqMoT.png)_Select the list input datapill_

### Advanced configuration

![Advanced configuration](/assets/batch-advanced-config.BZcKXtba.png)_Advanced configuration_

The **Advanced configuration** settings configure whether batch operations roll back when a record fails.

Workato processes records in batches of up to 200 records each. If a single record in a batch fails, the entire batch rolls back, while other batches remain unaffected.

For example, when processing 1,000 records, they are divided into 5 batches of 200 records each. If any record in the first batch fails, the entire first batch of 200 records rolls back. The remaining four batches proceed as normal.

The default and recommended setting is `No`. This allows successful records to remain processed. You can use additional logic in subsequent recipe steps to handle the failed records.

## Output

This action outputs two objects:

- **Successful records** contains information about records successfully updated in Salesforce.
- **Failed records** contains information about records that encountered issues and were not updated in Salesforce.

#### Successful records

| Output fields | Description |
| --- | --- |
| Salesforce ID | The internal Salesforce ID of the updated record. |
| Success | Indicates whether a record was successfully updated in Salesforce. |
| List size | The number of successfully updated records. |
| List index | The position of each successfully processed record within a batch. |

Additional outputs load dynamically based on the selected object type.

#### Failed records

| Output fields | Description |
| --- | --- |
| Success | Indicates whether a record was successfully updated in Salesforce. |
| Errors | An array containing the `Status code`, `Error message` and `Fields`. Use the information here to determine why the records failed. |
| List size | The number of records that failed and were not updated. |
| List index | The position of each failed record within a batch. |

Additional outputs load dynamically based on the selected object type.

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/update-records-csv.md
description: >-
  This action updates Salesforce records in bulk from a CSV file using the
  Salesforce bulk API.
---

# Salesforce - Update records in bulk from CSV file action

This action updates Salesforce records in bulk from a CSV file using the Salesforce bulk API.

> **POLLING BEHAVIOR**
> 
> The recipe that contains this action must be in a running state for asynchronous polling to function as expected.

Refer to the [Salesforce bulk operations](/en/connectors/salesforce/salesforce-bulk) guide for more information about bulk operations.

> **API VERSIONS**
> 
> This action exists in both API v1.0 and API v2.0 versions. Workato recommends using the bulk API v2.0 for optimal performance. This version reduces the impact on Salesforce API quotas by batching records more efficiently.

> **RETRY FAILED RECORDS**
> 
> You can use the [Retry bulk job for failed records from CSV file](/en/connectors/salesforce/actions/retry-job-csv) action to resubmit failed records to Salesforce as a new bulk job.

## Input

| Input fields | Description |
| --- | --- |
| Salesforce object to update | Select the standard or custom object type to update. |
| Relationship fields | Optional. Select how to map the CSV data columns into Salesforce object fields. Relationship fields are required for polymorphic columns. Refer to the [Relationship fields](#relationship-fields) section for more information about this input or the [Salesforce API documentation](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/relationship_fields_in_a_header_row__2_0.htm) for more information about polymorphic fields. |
| CSV file input | Define the schema of the CSV files containing Salesforce bulk load data. Refer to the [CSV file](#csv-file) section for an example. |
| File contents (CSV file input) | Enter the contents of the file. You can obtain a File datapill from the [Download file](/en/connectors/salesforce/actions/download-file) action. |
| Column separator (CSV file input) | Use the drop-down menu to select the column separator to use. For example, comma (`,`) or pipe (`|`). |
| Contains header line? (CSV file input) | Select whether the CSV file content contains a header line. This tells Workato whether to skip the first line to avoid processing it as data. |
| Column names (CSV file input) | Enter information about the data columns in your CSV file. The columns you enter become available in the **CSV to Salesforce object field mapping** section. |
| Use CSV column names as Salesforce field names (CSV file input) | Select whether to map CSV columns to Salesforce object fields automatically. This requires the CSV file to have a header line with column names matching the object fields. |
| CSV to Salesforce object field mapping | Enter CSV column names and the Salesforce object to update in bulk. |
| Advanced configuration | Configure advanced settings for the action. |
| Wait for Salesforce to process all CSV rows? (Advanced configuration) | Select whether to run the action synchronously. Select `Yes` to wait until Salesforce processes all rows in the CSV file before starting the next action. Select `No` to start the next action after the CSV file is uploaded to Salesforce. Bulk operations are asynchronous by default. |
| CSV chunk size for each Salesforce bulk job (in MB) (Advanced configuration) | Enter the CSV chunk size in megabytes for each Salesforce bulk job. If the CSV file is larger than the chunk size, the action automatically creates multiple Salesforce bulk jobs. This field defaults to 100 MB. |
| Return success report without header line (Advanced configuration) | Select whether to exclude header lines from returned success reports. |
| Return failed rows report without header line (Advanced configuration) | Select whether to exclude header lines from returned failed rows reports. |

### Relationship fields

Salesforce uses relationships and relationship fields to associate data between two objects. For example, the `Account` and `Contact` objects have a relationship where each contact stores a reference to one account, while each account can link to many contacts. You can view all contacts associated with an account directly from the account record. Some objects have relationships to other objects of the same type. For example, the `Reports To` field for a contact is a reference to a different contact.

Relationship fields also allow polymorphic column mapping. Workato cannot infer this mapping automatically, so you must specify it manually. If you don't configure the **Relationship fields** input, no data maps into Salesforce.

To configure this field, select which column of the CSV file to pull data from for each field that you plan to write to in Salesforce. This action doesn't allow datapills or data transformation using formula mode as it streams the CSV file data directly into Salesforce. Refer to the [Salesforce object relationships](/en/connectors/salesforce/related-objects) guide for more information about object relationships or the Salesforce [CSV field header documentation](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/datafiles_csv_rel_field_header_row.htm) for information about relationship fields in CSV headers.

![Salesforce bulk upsert action - configured fields mapping section](/assets/bulk-action-configured-fields-mapping.B0TgIjKb.png)_Salesforce bulk upsert action - field mapping section_

### CSV file

The following example shows how to format the **CSV file input** for a CSV:

```
external_id,last_name,value
"a0K1h000003fXSS","Minnes","54"
"a0K1h000003fehx","Lecompte","12"
"a0K1h000003fjnv","Fester","28"
```

![Salesforce bulk action - configured CSV file input section](/assets/bulk-action-csv-file-input-section.70nqd1LC.png)_Salesforce bulk action - configured CSV file input section_

## Output

| Output fields | Description |
| --- | --- |
| All records successfully processed? | Indicates whether all CSV rows across Salesforce bulk jobs processed successfully. |
| Number of records succeeded | The total number of CSV rows that were successfully processed in Salesforce. |
| Number of records failed | The total number of CSV rows that encountered issues and were not processed in Salesforce. |
| Number of retried records | The total number of CSV rows that retried processing in Salesforce. This field is relevant for the [Retry objects bulk job in Salesforce from CSV file](/en/connectors/salesforce/actions/retry-job-csv) action. |
| Number of records processed | The total number of CSV rows processed in Salesforce, excluding the header row. |
| CSV contents with failed records | CSV file content containing CSV rows that encountered issues and were not processed. Two additional columns are added to this CSV file: `sf__Error` and `sf__Id`. Refer to the [Salesforce documentation](https://developer.salesforce.com/docs/atlas.en-us.api_bulk_v2.meta/api_bulk_v2/get_job_failed_results.htm) for more information. |
| CSV content with success records | CSV file content containing CSV rows that were successfully processed in Salesforce. Two additional columns are added to this CSV file: `sf__Created` and `sf__Id`. Refer to the [Salesforce documentation](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/get_job_successful_results.htm) for more information. |
| Failed records report header | Header information of failed record reports. |
| Success records report header | Header information of successful record reports. |
| Salesforce bulk jobs | An object containing information about each Salesforce bulk job. Refer to the [Salesforce bulk jobs](#salesforce-bulk-jobs) section for more information. |

### Salesforce bulk jobs

Workato splits large CSV files into chunks and processes them as separate Salesforce bulk jobs to comply with Salesforce API size limits. Bulk operations output a `Salesforce bulk jobs` datatree that contains information about each chunk processed.

![Salesforce bulk operation output datatree - list of bulk jobs](/assets/bulk-operation-datatree-array-of-jobs.CZCluW4m.png)_Salesforce bulk operation output datatree - list of bulk jobs_

Workato includes the aggregated results across all bulk jobs at the top of the output, outside of the `Salesforce bulk jobs` datatree.

![Salesforce bulk operation output datatree - aggregated results across bulk jobs](/assets/bulk-operation-datatree-aggregate-numbers.Cn8qzyPE.png)_Salesforce bulk operation output datatree - aggregated results across bulk jobs_

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/upsert-records-batch.md
description: This action upserts Salesforce records in batches.
---

# Salesforce - Upsert records in batches action (batch)

This action upserts Salesforce records in batches. Each batch can upsert up to 2,000 records in 10 batches of 200. If matching records are found, they are updated. If matching records aren't found, they are created.

![Upsert records in batches action](/assets/batch-upsert-action.S5QotxY6.png)_Upsert records in batches action_

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the standard or custom object type to upsert. |
| Batch size | Enter the number of records to process in each batch. The minimum value is `1`, the maximum and default is `200`. |
| Primary key | Select an external ID to use as the primary key. If multiple records match the provided primary key, the action throws an error. Refer to the [Primary key](#primary-key) section for more information. |
| Relationship fields | Optional. Select how to map the CSV data columns into Salesforce object fields. Relationship fields are required for polymorphic columns. Refer to the [Relationship fields](#relationship-fields) section for more information about this input or the [Salesforce API documentation](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/relationship_fields_in_a_header_row__2_0.htm) for more information about polymorphic fields. |
| Advanced configuration | Select whether to roll back records if an operation fails. Refer to the [Advanced configuration](#advanced-configuration) section for more information. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

Additional fields load dynamically based on the selected object. Use these fields to enter a source list and configure the new records.

You can obtain a source list from various locations, such as a new CSV file in a file storage app, including Box, Amazon S3, and On-prem files. Refer to the [List management](/en/features/list-management) documentation for more information about list inputs.

### Primary key

This action requires you to specify an `External ID` field as a primary key to uniquely identify each Salesforce record.

The `External ID` field is a custom field that has the `External ID` attribute. It contains unique record identifiers from a system outside of Salesforce. External ID fields must be custom text, number, or email fields.

If an `External ID` value you provide already exists in a Salesforce record, Workato updates that record. If no matching `External ID` exists in Salesforce, Workato creates a new record. This action throws an error if multiple Salesforce records match the provided `External ID`.

> **MULTIPLE PRIMARY KEYS**
> 
> You can’t use more than one primary key in a single operation. To handle scenarios where multiple fields identify a record, first perform a search action using one of the keys. Then, add a conditional action to check whether the number of results is greater than one.
> 
> If you need to search using two fields (for example, `Full Name` and `Account`), use a search action that includes both fields as filters. Then retrieve the results and use a conditional check to verify the number of matching records before updating or creating records.

> Create a primary key in Salesforce
> 
> Complete the following steps to create an `External ID` field to use as your primary key:
> 
> 1. Go to the Salesforce **Setup** menu and select the **Object Manager** tab.
>    
> 2. Select the object where you plan to add the custom field. For example, **Contact**.
>    
> 3. Go to the **Fields & Relationships** tab and select **New**.
>    
> 4. Select the **Data Type** for the custom field. This example uses **Text**.
>    
> 5. Click **Next**.
>    
> 6. Configure the following fields:
>    
>    - Field Label
>      
>    - Enter a label to use for displays, page layouts, reports, and list views. This example uses `Test id`.
>      
>    - Length
>      
>    - Enter the maximum length for the field. This example uses `25`.
>      
>    - Field Name
>      
>    - The **Field Name** is an internal reference for integration purposes, such as custom links, custom s-controls, and the API. Changing the **Field Name** may affect existing integrations. The **Field Name** can only contain alphanumeric characters. It must begin with a letter, cannot end with an underscore, cannot contain two consecutive underscore characters, and must be unique across all `Contact` fields.
>      
>    - Unique
>      
>    - Select the **Unique** checkbox to disallow duplicate values.
>      
>    - External ID
>      
>    - Select the **External ID** checkbox to set the field as the unique identifier from an external system.
>      
> 7. Click **Next**.
>    
> 8. Select the profiles to provide edit access for this field through field-level security. The field is hidden from all users if you don’t assign it to any profiles.
>    
> 9. Click **Next**.
>    
> 10. Select the page layouts to include this field in. Salesforce adds the field to the end of the first two-column section in each selected layout. The field doesn't appear on any pages if you don't select a layout.
>     
>     You can customize the page layout to change the location of this field on the page.
>     
> 11. Click **Save**. The custom field for the **Contact** object appears as an option in the **Primary key** drop-down menu in the Workato recipe editor.
>     
> 12. Return to Workato and use the **Primary key** field to select the new custom field.
>     
>     ![Primary key](/assets/primary-key.DWszQXAf.png)_Primary key_
>     

### Relationship fields

Salesforce uses relationships and relationship fields to associate data between two objects. For example, the `Account` and `Contact` objects have a relationship where each contact stores a reference to one account, while each account can link to many contacts. You can view all contacts associated with an account directly from the account record. Some objects have relationships to other objects of the same type. For example, the `Reports To` field for a contact is a reference to a different contact.

Relationship fields also allow polymorphic column mapping. Workato cannot infer this mapping automatically, so you must specify it manually. If you don't configure the **Relationship fields** input, no data maps into Salesforce.

To configure this field, select which column of the CSV file to pull data from for each field that you plan to write to in Salesforce. This action doesn't allow datapills or data transformation using formula mode as it streams the CSV file data directly into Salesforce. Refer to the [Salesforce object relationships](/en/connectors/salesforce/related-objects) guide for more information about object relationships or the Salesforce [CSV field header documentation](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/datafiles_csv_rel_field_header_row.htm) for information about relationship fields in CSV headers.

![Salesforce bulk upsert action - configured fields mapping section](/assets/bulk-action-configured-fields-mapping.B0TgIjKb.png)_Salesforce bulk upsert action - field mapping section_

### Advanced configuration

![Advanced configuration](/assets/batch-advanced-config.BZcKXtba.png)_Advanced configuration_

The **Advanced configuration** settings configure whether batch operations roll back when a record fails.

Workato processes records in batches of up to 200 records each. If a single record in a batch fails, the entire batch rolls back, while other batches remain unaffected.

For example, when processing 1,000 records, they are divided into 5 batches of 200 records each. If any record in the first batch fails, the entire first batch of 200 records rolls back. The remaining four batches proceed as normal.

The default and recommended setting is `No`. This allows successful records to remain processed. You can use additional logic in subsequent recipe steps to handle the failed records.

## Output

This action outputs two objects:

- **Successful records** contains information about records successfully upserted in Salesforce.
- **Failed records** contains information about records that encountered issues and were not upserted in Salesforce.

#### Successful records

| Output fields | Description |
| --- | --- |
| Salesforce ID | The internal Salesforce ID of the upserted record. |
| Success | Indicates whether a record was successfully upserted in Salesforce. |
| List size | The number of successfully upserted records. |
| List index | The position of each successfully processed record within a batch. |

Additional outputs load dynamically based on the selected object type.

#### Failed records

| Output fields | Description |
| --- | --- |
| Success | Indicates whether a record was successfully upserted in Salesforce. |
| Errors | An array containing the `Status code`, `Error message` and `Fields`. Use the information here to determine why the records failed. |
| List size | The number of records that failed and were not upserted. |
| List index | The position of each failed record within a batch. |

Additional outputs load dynamically based on the selected object type.

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/upsert-records-in-bulk-from-csv.md
description: >-
  This action upserts Salesforce records in bulk from a CSV file and a primary
  key.
---

# Salesforce - Upsert records in bulk from CSV file action

This action upserts Salesforce records in bulk from a CSV file and a primary key. Matching records are updated and new records are created if matching records aren't found.

> **POLLING BEHAVIOR**
> 
> Recipes that contain an action with polling must be in a running state for asynchronous polling to function as expected.

Refer to the [Salesforce bulk operations](/en/connectors/salesforce/salesforce-bulk) guide for more information about bulk operations.

> **API VERSIONS**
> 
> This action exists in both API v1.0 and API v2.0 versions. Workato recommends using the bulk API v2.0 for optimal performance. This version reduces the impact on Salesforce API quotas by batching records more efficiently.

> **RETRY FAILED RECORDS**
> 
> You can use the [Retry bulk job for failed records from CSV file](/en/connectors/salesforce/actions/retry-job-csv) action to resubmit failed records to Salesforce as a new bulk job.

## Input

| Input fields | Description |
| --- | --- |
| Salesforce object to upsert | Select the standard or custom object type to upsert. |
| Relationship fields | Optional. Select how to map the CSV data columns into Salesforce object fields. Relationship fields are required for polymorphic columns. Refer to the [Relationship fields](#relationship-fields) section for more information about this field or the [Salesforce API documentation](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/relationship_fields_in_a_header_row__2_0.htm) for more information about polymorphic fields. |
| Primary key | Select an external ID to use as the primary key. Alternatively, you can use the drop-down menu to switch this field to **Enter primary key** and enter the API name of an indexed field. If multiple records match the provided primary key, the action throws an error. Refer to the [Primary key](#primary-key) section for more information. |
| CSV file input | Define the schema of the CSV files containing Salesforce bulk load data. Refer to the [CSV file](#csv-file) section for an example. |
| File contents (CSV file input) | Enter the contents of the file. You can obtain a File datapill from the [Download file](/en/connectors/salesforce/actions/download-file) action. |
| Column separator (CSV file input) | Use the drop-down menu to select the column separator to use. For example, comma (`,`) or pipe (`|`). |
| Contains header line? (CSV file input) | Select whether the CSV file content contains a header line. This tells Workato whether to skip the first line to avoid processing it as data. |
| Column names (CSV file input) | Enter information about the data columns in your CSV file. |
| Use CSV column names as Salesforce field names | Select whether to map CSV columns to Salesforce object fields automatically. This option requires a header containing column names matching the Salesforce object fields. |
| CSV to Salesforce object field mapping | Enter CSV column names and the Salesforce object to upsert in bulk. |

### Primary key

This action requires you to specify a primary key to uniquely identify each Salesforce record. The Salesforce bulk API supports both the `External ID` field and indexed fields, for example the internal Record ID, as primary keys.

The `External ID` field is a custom field that has the `External ID` attribute. It contains unique record identifiers from a system outside of Salesforce. External ID fields must be custom text, number, or email fields.

Use the drop-down menu to switch the **Primary key** field to **Enter primary key** and enter the API name of an indexed field to use it as a primary key.

The action's behavior while using an external ID and other indexed fields differ as follows:

| Input value | External ID | Indexed fields |
| --- | --- | --- |
| Match found | Updates record | Updates record |
| No match found | Creates record | `MALFORMED_ID:Id in upsert is not valid` error |
| No value | `MISSING_ARGUMENT:External_ID__c not specified` error | Creates records |

This action throws an error if multiple Salesforce records match the provided primary key.

> **MULTIPLE PRIMARY KEYS**
> 
> You can’t use more than one primary key in a single operation. To handle scenarios where multiple fields identify a record, first perform a search action using one of the keys. Then, add a conditional action to check whether the number of results is greater than one.
> 
> If you need to search using two fields (for example, `Full Name` and `Account`), use a search action that includes both fields as filters. Then retrieve the results and use a conditional check to verify the number of matching records before updating or creating records.

> Create a primary key in Salesforce
> 
> Complete the following steps to create an `External ID` field to use as your primary key:
> 
> 1. Go to the Salesforce **Setup** menu and select the **Object Manager** tab.
>    
> 2. Select the object where you plan to add the custom field. For example, **Contact**.
>    
> 3. Go to the **Fields & Relationships** tab and select **New**.
>    
> 4. Select the **Data Type** for the custom field. This example uses **Text**.
>    
> 5. Click **Next**.
>    
> 6. Configure the following fields:
>    
>    - Field Label
>      
>    - Enter a label to use for displays, page layouts, reports, and list views. This example uses `Test id`.
>      
>    - Length
>      
>    - Enter the maximum length for the field. This example uses `25`.
>      
>    - Field Name
>      
>    - The **Field Name** is an internal reference for integration purposes, such as custom links, custom s-controls, and the API. Changing the **Field Name** may affect existing integrations. The **Field Name** can only contain alphanumeric characters. It must begin with a letter, cannot end with an underscore, cannot contain two consecutive underscore characters, and must be unique across all `Contact` fields.
>      
>    - Unique
>      
>    - Select the **Unique** checkbox to disallow duplicate values.
>      
>    - External ID
>      
>    - Select the **External ID** checkbox to set the field as the unique identifier from an external system.
>      
> 7. Click **Next**.
>    
> 8. Select the profiles to provide edit access for this field through field-level security. The field is hidden from all users if you don’t assign it to any profiles.
>    
> 9. Click **Next**.
>    
> 10. Select the page layouts to include this field in. Salesforce adds the field to the end of the first two-column section in each selected layout. The field doesn't appear on any pages if you don't select a layout.
>     
>     You can customize the page layout to change the location of this field on the page.
>     
> 11. Click **Save**. The custom field for the **Contact** object appears as an option in the **Primary key** drop-down menu in the Workato recipe editor.
>     
> 12. Return to Workato and use the **Primary key** field to select the new custom field.
>     
>     ![Primary key](/assets/primary-key.DWszQXAf.png)_Primary key_
>     

### Relationship fields

Salesforce uses relationships and relationship fields to associate data between two objects. For example, the `Account` and `Contact` objects have a relationship where each contact stores a reference to one account, while each account can link to many contacts. You can view all contacts associated with an account directly from the account record. Some objects have relationships to other objects of the same type. For example, the `Reports To` field for a contact is a reference to a different contact.

Relationship fields also allow polymorphic column mapping. Workato cannot infer this mapping automatically, so you must specify it manually. If you don't configure the **Relationship fields** input, no data maps into Salesforce.

To configure this field, select which column of the CSV file to pull data from for each field that you plan to write to in Salesforce. This action doesn't allow datapills or data transformation using formula mode as it streams the CSV file data directly into Salesforce. Refer to the [Salesforce object relationships](/en/connectors/salesforce/related-objects) guide for more information about object relationships or the Salesforce [CSV field header documentation](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/datafiles_csv_rel_field_header_row.htm) for information about relationship fields in CSV headers.

![Salesforce bulk upsert action - configured fields mapping section](/assets/bulk-action-configured-fields-mapping.B0TgIjKb.png)_Salesforce bulk upsert action - field mapping section_

### CSV file

The following example shows how to format the **CSV file input** for a CSV:

```
external_id,last_name,value
"a0K1h000003fXSS","Minnes","54"
"a0K1h000003fehx","Lecompte","12"
"a0K1h000003fjnv","Fester","28"
```

![Salesforce bulk action - configured CSV file input section](/assets/bulk-action-csv-file-input-section.70nqd1LC.png)_Salesforce bulk action - configured CSV file input section_

## Output

| Output fields | Description |
| --- | --- |
| All records successfully processed? | Indicates whether all CSV rows across Salesforce bulk jobs processed successfully. |
| Number of records succeeded | The total number of CSV rows that were successfully processed in Salesforce. |
| Number of records failed | The total number of CSV rows that encountered issues and were not processed in Salesforce. |
| Number of retried records | The total number of CSV rows that retried processing in Salesforce. This field is relevant for the [Retry objects bulk job in Salesforce from CSV file](/en/connectors/salesforce/actions/retry-job-csv) action. |
| Number of records processed | The total number of CSV rows processed in Salesforce, excluding the header row. |
| CSV contents with failed records | CSV file content containing CSV rows that encountered issues and were not processed. Two additional columns are added to this CSV file: `sf__Error` and `sf__Id`. Refer to the [Salesforce documentation](https://developer.salesforce.com/docs/atlas.en-us.api_bulk_v2.meta/api_bulk_v2/get_job_failed_results.htm) for more information. |
| CSV content with success records | CSV file content containing CSV rows that were successfully processed in Salesforce. Two additional columns are added to this CSV file: `sf__Created` and `sf__Id`. Refer to the [Salesforce documentation](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/get_job_successful_results.htm) for more information. |
| Failed records report header | Header information of failed record reports. |
| Success records report header | Header information of successful record reports. |
| Salesforce bulk jobs | An object containing information about each Salesforce bulk job. Refer to the [Salesforce bulk jobs](#salesforce-bulk-jobs) section for more information. |

### Salesforce bulk jobs

Workato splits large CSV files into chunks and processes them as separate Salesforce bulk jobs to comply with Salesforce API size limits. Bulk operations output a `Salesforce bulk jobs` datatree that contains information about each chunk processed.

![Salesforce bulk operation output datatree - list of bulk jobs](/assets/bulk-operation-datatree-array-of-jobs.CZCluW4m.png)_Salesforce bulk operation output datatree - list of bulk jobs_

Workato includes the aggregated results across all bulk jobs at the top of the output, outside of the `Salesforce bulk jobs` datatree.

![Salesforce bulk operation output datatree - aggregated results across bulk jobs](/assets/bulk-operation-datatree-aggregate-numbers.Cn8qzyPE.png)_Salesforce bulk operation output datatree - aggregated results across bulk jobs_

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/troubleshoot-connection-setup.md
description: >-
  Use this guide to troubleshoot errors when you connect to the Salesforce
  connector in Workato.
---

# Troubleshoot Salesforce connection setup

Use this guide to troubleshoot errors when you connect to the Salesforce connector in Workato.

## Salesforce connection failed: Action failed due to server error

The `action failed due to server error` message displays when you click **Connect** to establish a Salesforce connection and it fails.

![action failed due to server error](/assets/sffailconnect.CL_57-mN.png)_Salesforce connection fails with an `action failed due to server error` message_

Complete the following steps to resolve this error and successfully establish a Salesforce connection:

1. Verify the domain. Use the correct Salesforce domain or custom domain:
   
   - Set the **Sandbox** field to Yes if your Salesforce domain ends with `.sandbox.my.salesforce.com`, or **No** if it ends with `.my.salesforce.com`.
2. If you're using a custom OAuth profile, confirm your external client app's OAuth and security settings match the configuration in [Create a custom OAuth profile for Salesforce](/en/connectors/salesforce/custom-oauth), including the **Flow Enablement** and **Security** settings.
   
3. Add Workato IPs to your allowlist. Refer to [IP allowlists](/en/security/ip-allowlists#traffic-from-workato) for more information.
   
4. Confirm that Salesforce doesn't block Workato. If the Workato connector is blocked, go to **Manage Apps** > **Connected Apps OAuth Usage**, then click **Unblock** next to the app name.
   
   ![Unblock Workato in SFDC](/assets/resolve.GOP1yHKb.png)_Unblock Workato in SFDC_
   

## Salesforce connection disconnects repeatedly

A connection that repeatedly shows **Connection lost** and requires reconnecting usually means Salesforce isn't returning a refresh token. A Refresh Token Policy or IP Relaxation setting can cause the same symptom.

![Connection lost banner on a Salesforce connection's detail page.](/assets/connection-lost.BQSzyd70.png)_Connection lost banner on a Salesforce connection_

Salesforce only issues a refresh token when your Salesforce app's OAuth policies explicitly grant the **Perform requests at any time** scope. **Full access** doesn't include this scope by default. Refer to [Token expiration](/en/connectors/salesforce#token-expiration) for how this works.

Add **Perform requests at any time (refresh\_token, offline\_access)** to your external client app's Selected OAuth Scopes if you're using a [custom OAuth profile](/en/connectors/salesforce/custom-oauth).

Complete the following steps for the default OAuth 2.0 connection:

1. Sign in to Salesforce and go to **Setup > Apps > App Manager**.
   
2. Open the Connected App named `Workato connector`. Salesforce creates it automatically, or an admin installs it, the first time your org connects. Refer to [OAuth restrictions](/en/connectors/salesforce#oauth-restrictions) if you don't see the Connected App.
   
3. Select **Manage**.
   
4. Check the **OAuth Policies > Application Permissions** list for the **Perform requests at any time** scope.
   

Check the following settings on the same app if disconnections continue:

- **Refresh Token Policy (Idle Expiration Time Limit Enforced)**: avoid **Immediately expire refresh token**, and set any idle-expiration window longer than how often your recipes actually use the connection.
- **IP Relaxation**: set to **Relax IP restrictions**, or [add Workato's IPs](/en/security/ip-allowlists#traffic-from-workato) to **Setup > Security > Network Access** or the integration user's **Login IP Ranges** instead if you need to keep **Enforce IP restrictions**. Workato connects from a rotating range of IPs, so an enforced policy without an allowlist can revoke the session in a way that looks like a disconnect.
- **Lock sessions to the IP address from which they originated** (**Setup > Security > Session Settings**) can cause the same symptom if set too strictly alongside IP Relaxation.

Refer to Salesforce's [Manage OAuth Access Policies for a Connected App](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_manage_oauth.htm&type=5) and [OAuth Tokens and Scopes](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_tokens_scopes.htm&type=5) for additional token expiration options and configuration steps.

---
