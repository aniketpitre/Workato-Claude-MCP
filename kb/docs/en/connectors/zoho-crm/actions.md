---
url: 'https://docs.workato.com/en/connectors/zoho-crm/actions.md'
description: >-
  Browse the actions supported by the Zoho CRM connector in Workato to create,
  update, and manage records in your Zoho CRM account.
---

# Zoho CRM - Actions

The Zoho CRM connector supports the following actions:

- [Batch create custom objects action](/en/connectors/zoho-crm/actions/batch-create-custom-objects)
- [Batch create standard objects action](/en/connectors/zoho-crm/actions/batch-create-standard-objects)
- [Batch update custom objects action](/en/connectors/zoho-crm/actions/batch-update-custom-objects)
- [Batch update standard objects action](/en/connectors/zoho-crm/actions/batch-update-standard-objects)
- [Batch upsert custom objects action](/en/connectors/zoho-crm/actions/batch-upsert-custom-objects)
- [Batch upsert standard objects action](/en/connectors/zoho-crm/actions/batch-upsert-standard-objects)
- [Bulk create custom objects action](/en/connectors/zoho-crm/actions/bulk-create-custom-objects)
- [Bulk create standard objects action](/en/connectors/zoho-crm/actions/bulk-create-standard-objects)
- [Bulk update custom objects action](/en/connectors/zoho-crm/actions/bulk-update-custom-objects)
- [Bulk update standard objects action](/en/connectors/zoho-crm/actions/bulk-update-standard-objects)
- [Bulk upsert custom objects action](/en/connectors/zoho-crm/actions/bulk-upsert-custom-objects)
- [Bulk upsert standard objects action](/en/connectors/zoho-crm/actions/bulk-upsert-standard-objects)
- [Create account action](/en/connectors/zoho-crm/actions/create-account)
- [Create campaign action](/en/connectors/zoho-crm/actions/create-campaign)
- [Create contact action](/en/connectors/zoho-crm/actions/create-contact)
- [Create deal action](/en/connectors/zoho-crm/actions/create-deal)
- [Create invoice action](/en/connectors/zoho-crm/actions/create-invoice)
- [Create lead action](/en/connectors/zoho-crm/actions/create-lead)
- [Create vendor action](/en/connectors/zoho-crm/actions/create-vendor)
- [Delete custom object action](/en/connectors/zoho-crm/actions/delete-custom-object)
- [Delete standard object action](/en/connectors/zoho-crm/actions/delete-standard-object)
- [Get lead by ID action](/en/connectors/zoho-crm/actions/get-lead-by-id)
- [Get object by ID action](/en/connectors/zoho-crm/actions/get-object-by-id)
- [Relate a member to a campaign action](/en/connectors/zoho-crm/actions/relate-member-to-campaign)
- [Search accounts action (batch)](/en/connectors/zoho-crm/actions/search-accounts-batch)
- [Search campaigns action (batch)](/en/connectors/zoho-crm/actions/search-campaigns-batch)
- [Search contacts action (batch)](/en/connectors/zoho-crm/actions/search-contacts-batch)
- [Search custom objects action](/en/connectors/zoho-crm/actions/search-custom-objects)
- [Search deals action (batch)](/en/connectors/zoho-crm/actions/search-deals-batch)
- [Search invoice action](/en/connectors/zoho-crm/actions/search-invoice)
- [Search leads action (batch)](/en/connectors/zoho-crm/actions/search-leads-batch)
- [Search products action (batch)](/en/connectors/zoho-crm/actions/search-products-batch)
- [Search records using COQL query action](/en/connectors/zoho-crm/actions/search-records-using-coql-query)
- [Search standard objects action](/en/connectors/zoho-crm/actions/search-standard-objects)
- [Search vendors action (batch)](/en/connectors/zoho-crm/actions/search-vendors-batch)
- [Update account action](/en/connectors/zoho-crm/actions/update-account)
- [Update campaign action](/en/connectors/zoho-crm/actions/update-campaign)
- [Update contact action](/en/connectors/zoho-crm/actions/update-contact)
- [Update deal action](/en/connectors/zoho-crm/actions/update-deal)
- [Update invoice action](/en/connectors/zoho-crm/actions/update-invoice)
- [Update lead action](/en/connectors/zoho-crm/actions/update-lead)
- [Update vendor action](/en/connectors/zoho-crm/actions/update-vendor)
- [Upsert custom object action](/en/connectors/zoho-crm/actions/upsert-custom-object)
- [Upsert standard object action](/en/connectors/zoho-crm/actions/upsert-standard-object)

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/batch-create-custom-objects.md
description: >-
  The Batch create custom objects action creates custom objects in batches in
  Zoho CRM.
---

# Zoho CRM - Batch create custom objects action

The **Batch create custom objects** action creates custom objects in batches in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the custom module for the objects. |

## Output

| Output field | Description |
| --- | --- |
| {Objects} | The list of objects that were created. |
| {Object} ID | The unique identifier of the object. |
| Created time | The timestamp when the object was created. |
| Modified time | The timestamp when the object was modified. |
| Created by | The user who created the object. |
| Modified by | The user who last modified the object. |
| ID | The unique identifier of the object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/batch-create-standard-objects.md
description: >-
  The Batch create standard objects action creates standard objects in batches
  in Zoho CRM.
---

# Zoho CRM - Batch create standard objects action

The **Batch create standard objects** action creates standard objects in batches in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the standard module for the objects. |
| Data | Provide the data for the objects to create. |
| Data source list (Data) | Provide the source list for the data. |

Additional fields appear based on the module you select.

## Output

The output is a list of the objects that were created in Zoho CRM.

| Output field | Description |
| --- | --- |
| {Objects} | A list of objects that were created in Zoho CRM. |
| {Object} ID | The unique identifier of the object. |
| Created time | The timestamp when the object was created. |
| Modified time | The timestamp when the object was modified. |
| Created by | The user who created the object. |
| Modified by | The user who last modified the object. |
| ID | The unique identifier of the object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/batch-update-custom-objects.md
description: >-
  The Batch update custom objects action updates custom objects in batches in
  Zoho CRM.
---

# Zoho CRM - Batch update custom objects action

The **Batch update custom objects** action updates custom objects in batches in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the custom module for the objects. |

## Output

| Output field | Description |
| --- | --- |
| {Objects} | The list of objects that were updated. |
| {Object} ID | The unique identifier of the object. |
| Created time | The timestamp when the object was created. |
| Modified time | The timestamp when the object was modified. |
| Created by | The user who created the object. |
| Modified by | The user who last modified the object. |
| ID | The unique identifier of the object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/batch-update-standard-objects.md
description: >-
  The Batch update standard objects action updates standard objects in batches
  in Zoho CRM.
---

# Zoho CRM - Batch update standard objects action

The **Batch update standard objects** action updates standard objects in batches in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the standard module for the objects. |
| Data | Provide the data for the objects to update. |
| Data source list (Data) | Provide the source list for the data. |

Additional fields appear based on the module you select.

## Output

The output is a list of the objects that were updated in Zoho CRM.

| Output field | Description |
| --- | --- |
| {Objects} | A list of objects that were updated in Zoho CRM. |
| {Object} ID | The unique identifier of the object. |
| Created time | The timestamp when the object was created. |
| Modified time | The timestamp when the object was modified. |
| Created by | The user who created the object. |
| Modified by | The user who last modified the object. |
| ID | The unique identifier of the object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/batch-upsert-custom-objects.md
description: The Batch upsert custom objects action upserts objects in batches in Zoho CRM.
---

# Zoho CRM - Batch upsert custom objects action

The **Batch upsert custom objects** action upserts objects in batches in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the custom module for the objects. |

## Output

| Output field | Description |
| --- | --- |
| {Objects} | The list of objects that were upserted. |
| {Object} ID | The unique identifier of the object. |
| Created time | The timestamp when the object was created. |
| Modified time | The timestamp when the object was modified. |
| Created by | The user who created the object. |
| Modified by | The user who last modified the object. |
| ID | The unique identifier of the object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/batch-upsert-standard-objects.md
description: >-
  The Batch upsert standard objects action upserts standard objects in batches
  in Zoho CRM.
---

# Zoho CRM - Batch upsert standard objects action

The **Batch upsert standard objects** action upserts standard objects in batches in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the standard module for the objects. |
| Data | Provide the data for the objects to upsert. |
| Data source list (Data) | Provide the source list for the data. |
| Duplicate check fields (Data) | Select the fields to check for duplicates. |

Additional fields appear based on the module you select.

## Output

The output is a list of the objects that were upserted in Zoho CRM.

| Output field | Description |
| --- | --- |
| {Objects} | A list of objects that were upserted in Zoho CRM. |
| {Object} ID | The unique identifier of the object. |
| Created time | The timestamp when the object was created. |
| Modified time | The timestamp when the object was modified. |
| Created by | The user who created the object. |
| Modified by | The user who last modified the object. |
| ID | The unique identifier of the object. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/bulk-create-custom-objects.md
description: >-
  The Bulk create custom objects action creates custom objects in bulk in Zoho
  CRM.
---

# Zoho CRM - Bulk create custom objects action

The **Bulk create custom objects** action creates custom objects in bulk in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the custom module for the objects. |
| Ignore empty | Specify whether to ignore empty rows. |
| File content | Provide the file content. The file must be in zip format. The maximum file size is 25 MB. |
| Csv header | Enter the CSV header as comma separated values. |
| Field mapping | Provide the field mapping configuration. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the bulk operation. |
| Resource | The resource details for the bulk operation. |
| Status (Resource) | The status of the resource. |
| Code (Resource) | The code for the resource. |
| Type (Resource) | The type of resource. |
| File (Resource) | The file details for the resource. |
| Status (File) | The status of the file. |
| Name (File) | The name of the file. |
| Added count (File) | The number of records added from the file. |
| Skipped count (File) | The number of records skipped from the file. |
| Updated count (File) | The number of records updated from the file. |
| Total count (File) | The total number of records in the file. |
| Field mappings (Resource) | The field mapping configuration for the resource. |
| Api name (Field mappings) | The API name of the mapped field. |
| Index (Field mappings) | The index position of the mapped field. |
| Format (Field mappings) | The format of the mapped field. |
| Find by (Field mappings) | The field to use for finding records. |
| Module (Field mappings) | The module for the mapped field. |
| Default value (Field mappings) | The default value for the mapped field. |
| ID | The unique identifier of the bulk operation. |
| Result | The result details of the bulk operation. |
| Download URL (Result) | The URL to download the result file. |
| Created by | The user who created the bulk operation. |
| ID (Created by) | The unique identifier of the creator. |
| Name (Created by) | The name of the user who created the operation. |
| Operation | The type of operation performed. |
| Created time | The timestamp when the operation was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/bulk-create-standard-objects.md
description: >-
  The Bulk create standard objects action creates standard objects in bulk in
  Zoho CRM.
---

# Zoho CRM - Bulk create standard objects action

The **Bulk create standard objects** action creates standard objects in bulk in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the standard module for the objects. |
| Ignore empty | Specify whether to ignore empty rows. |
| File content | Provide the file content. The file must be in zip format. The maximum file size is 25 MB. |
| Csv header | Enter the CSV header as comma separated values. |
| Field mapping | Provide the field mapping configuration. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the bulk operation. |
| Resource | The resource details for the bulk operation. |
| Status (Resource) | The status of the resource. |
| Code (Resource) | The code for the resource. |
| Type (Resource) | The type of resource. |
| File (Resource) | The file details for the resource. |
| Status (File) | The status of the file. |
| Name (File) | The name of the file. |
| Added count (File) | The number of records added from the file. |
| Skipped count (File) | The number of records skipped from the file. |
| Updated count (File) | The number of records updated from the file. |
| Total count (File) | The total number of records in the file. |
| Field mappings (Resource) | The field mapping configuration for the resource. |
| Api name (Field mappings) | The API name of the mapped field. |
| Index (Field mappings) | The index position of the mapped field. |
| Format (Field mappings) | The format of the mapped field. |
| Find by (Field mappings) | The field to use for finding records. |
| Module (Field mappings) | The module for the mapped field. |
| Default value (Field mappings) | The default value for the mapped field. |
| ID | The unique identifier of the bulk operation. |
| Result | The result details of the bulk operation. |
| Download URL (Result) | The URL to download the result file. |
| Created by | The user who created the bulk operation. |
| ID (Created by) | The unique identifier of the creator. |
| Name (Created by) | The name of the user who created the operation. |
| Operation | The type of operation performed. |
| Created time | The timestamp when the operation was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/bulk-update-custom-objects.md
description: >-
  The Bulk update custom objects action updates custom objects in bulk in Zoho
  CRM.
---

# Zoho CRM - Bulk update custom objects action

The **Bulk update custom objects** action updates custom objects in bulk in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the custom module for the objects. |
| Ignore empty | Specify whether to ignore empty rows. |
| File content | Provide the file content. The file must be in zip format. The maximum file size is 25 MB. |
| Csv header | Enter the CSV header as comma separated values. |
| Find by | Enter the API name of a unique field. The system uses the value you provide in this field to find the existing records in the CRM. The default value is ID. |
| Field mapping | Provide the field mapping configuration. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the bulk operation. |
| Resource | The resource details for the bulk operation. |
| Status (Resource) | The status of the resource. |
| Code (Resource) | The code for the resource. |
| Type (Resource) | The type of resource. |
| File (Resource) | The file details for the resource. |
| Status (File) | The status of the file. |
| Name (File) | The name of the file. |
| Added count (File) | The number of records added from the file. |
| Skipped count (File) | The number of records skipped from the file. |
| Updated count (File) | The number of records updated from the file. |
| Total count (File) | The total number of records in the file. |
| Field mappings (Resource) | The field mapping configuration for the resource. |
| Api name (Field mappings) | The API name of the mapped field. |
| Index (Field mappings) | The index position of the mapped field. |
| Format (Field mappings) | The format of the mapped field. |
| Find by (Field mappings) | The field to use for finding records. |
| Module (Field mappings) | The module for the mapped field. |
| Default value (Field mappings) | The default value for the mapped field. |
| ID | The unique identifier of the bulk operation. |
| Result | The result details of the bulk operation. |
| Download URL (Result) | The URL to download the result file. |
| Created by | The user who created the bulk operation. |
| ID (Created by) | The unique identifier of the creator. |
| Name (Created by) | The name of the user who created the operation. |
| Operation | The type of operation performed. |
| Created time | The timestamp when the operation was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/bulk-update-standard-objects.md
description: >-
  The Bulk update standard objects action updates standard objects in bulk in
  Zoho CRM.
---

# Zoho CRM - Bulk update standard objects action

The **Bulk update standard objects** action updates standard objects in bulk in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the standard module for the objects. |
| Ignore empty | Specify whether to ignore empty rows. |
| File content | Provide the file content. The file must be in zip format. The maximum file size is 25 MB. |
| Csv header | Enter the CSV header as comma separated values. |
| Find by | Enter the API name of a unique field. The system uses the value you provide in this field to find the existing records in the CRM. The default value is ID. |
| Field mapping | Provide the field mapping configuration. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the bulk operation. |
| Resource | The resource details for the bulk operation. |
| Status (Resource) | The status of the resource. |
| Code (Resource) | The code for the resource. |
| Type (Resource) | The type of resource. |
| File (Resource) | The file details for the resource. |
| Status (File) | The status of the file. |
| Name (File) | The name of the file. |
| Added count (File) | The number of records added from the file. |
| Skipped count (File) | The number of records skipped from the file. |
| Updated count (File) | The number of records updated from the file. |
| Total count (File) | The total number of records in the file. |
| Field mappings (Resource) | The field mapping configuration for the resource. |
| Api name (Field mappings) | The API name of the mapped field. |
| Index (Field mappings) | The index position of the mapped field. |
| Format (Field mappings) | The format of the mapped field. |
| Find by (Field mappings) | The field to use for finding records. |
| Module (Field mappings) | The module for the mapped field. |
| Default value (Field mappings) | The default value for the mapped field. |
| ID | The unique identifier of the bulk operation. |
| Result | The result details of the bulk operation. |
| Download URL (Result) | The URL to download the result file. |
| Created by | The user who created the bulk operation. |
| ID (Created by) | The unique identifier of the creator. |
| Name (Created by) | The name of the user who created the operation. |
| Operation | The type of operation performed. |
| Created time | The timestamp when the operation was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/bulk-upsert-custom-objects.md
description: >-
  The Bulk upsert custom objects action upserts custom objects in bulk in Zoho
  CRM.
---

# Zoho CRM - Bulk upsert custom objects action

The **Bulk upsert custom objects** action upserts custom objects in bulk in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the custom module for the objects. |
| Ignore empty | Specify whether to ignore empty rows. |
| File content | Provide the file content. The file must be in zip format. The maximum file size is 25 MB. |
| Csv header | Enter the CSV header as comma separated values. |
| Find by | Enter the API name of a unique field. The system uses the value you provide in this field to find the existing records in the CRM. The default value is ID. |
| Field mapping | Provide the field mapping configuration. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the bulk operation. |
| Resource | The resource details for the bulk operation. |
| Status (Resource) | The status of the resource. |
| Code (Resource) | The code for the resource. |
| Type (Resource) | The type of resource. |
| File (Resource) | The file details for the resource. |
| Status (File) | The status of the file. |
| Name (File) | The name of the file. |
| Added count (File) | The number of records added from the file. |
| Skipped count (File) | The number of records skipped from the file. |
| Updated count (File) | The number of records updated from the file. |
| Total count (File) | The total number of records in the file. |
| Field mappings (Resource) | The field mapping configuration for the resource. |
| Api name (Field mappings) | The API name of the mapped field. |
| Index (Field mappings) | The index position of the mapped field. |
| Format (Field mappings) | The format of the mapped field. |
| Find by (Field mappings) | The field to use for finding records. |
| Module (Field mappings) | The module for the mapped field. |
| Default value (Field mappings) | The default value for the mapped field. |
| ID | The unique identifier of the bulk operation. |
| Result | The result details of the bulk operation. |
| Download URL (Result) | The URL to download the result file. |
| Created by | The user who created the bulk operation. |
| ID (Created by) | The unique identifier of the creator. |
| Name (Created by) | The name of the user who created the operation. |
| Operation | The type of operation performed. |
| Created time | The timestamp when the operation was created. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/bulk-upsert-standard-objects.md
description: >-
  The Bulk upsert standard objects action upserts standard objects in bulk in
  Zoho CRM.
---

# Zoho CRM - Bulk upsert standard objects action

The **Bulk upsert standard objects** action upserts standard objects in bulk in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the standard module for the objects. |
| Ignore empty | Specify whether to ignore empty rows. |
| File content | Provide the file content. The file must be in zip format. The maximum file size is 25 MB. |
| Csv header | Enter the CSV header as comma separated values. |
| Find by | Enter the API name of a unique field. The system uses the value you provide in this field to find the existing records in the CRM. The default value is ID. |
| Field mapping | Provide the field mapping configuration. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the bulk operation. |
| Resource | The resource details for the bulk operation. |
| Status (Resource) | The status of the resource. |
| Code (Resource) | The code for the resource. |
| Type (Resource) | The type of resource. |
| File (Resource) | The file details for the resource. |
| Status (File) | The status of the file. |
| Name (File) | The name of the file. |
| Added count (File) | The number of records added from the file. |
| Skipped count (File) | The number of records skipped from the file. |
| Updated count (File) | The number of records updated from the file. |
| Total count (File) | The total number of records in the file. |
| Field mappings (Resource) | The field mapping configuration for the resource. |
| Api name (Field mappings) | The API name of the mapped field. |
| Index (Field mappings) | The index position of the mapped field. |
| Format (Field mappings) | The format of the mapped field. |
| Find by (Field mappings) | The field to use for finding records. |
| Module (Field mappings) | The module for the mapped field. |
| Default value (Field mappings) | The default value for the mapped field. |
| ID | The unique identifier of the bulk operation. |
| Result | The result details of the bulk operation. |
| Download URL (Result) | The URL to download the result file. |
| Created by | The user who created the bulk operation. |
| ID (Created by) | The unique identifier of the creator. |
| Name (Created by) | The name of the user who created the operation. |
| Operation | The type of operation performed. |
| Created time | The timestamp when the operation was created. |

---
