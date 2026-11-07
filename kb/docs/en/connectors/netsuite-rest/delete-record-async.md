---
url: 'https://docs.workato.com/en/connectors/netsuite-rest/delete-record-async.md'
description: >-
  The Delete records batch (async) action deletes multiple records
  asynchronously in NetSuite REST.
---

# NetSuite REST - Delete records (async) batch action

The **Delete records batch (async)** action deletes multiple records in NetSuite REST asynchronously. All records submit as a single batch async request, and NetSuite returns one job ID for the entire batch.

Use this action to process large batches without blocking the recipe. The maximum number of records per batch is 100.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record to delete. Only [REST Web Services supported records](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_1558962745.html#Web-Services-Supported-Records) appear in the list. Enable custom records if required. |
| Record data | Provide the list of records to delete from NetSuite. |

Additional fields appear based on the **Record** you select. The structure of **Record data**, **Record data source list**, and **Record data fields** changes dynamically to match the **Record** you select.

## Output

| Output field | Description |
| --- | --- |
| Async job ID | The identifier for the batch async job. Pass this value to the [Get async job result action](/en/connectors/netsuite-rest/get-async-job) to retrieve the job status and per-record results after NetSuite processes the batch. |
| Job enqueued at | The timestamp when NetSuite enqueued the batch job for processing. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/detach-contact-from-record-action.md
description: >-
  The Detach contact from record action detaches a contact from a record in
  NetSuite REST.
---

# NetSuite REST - Detach contact from a record action

The **Detach contact from a record** action detaches a contact from a record in NetSuite REST.

Use this action to remove the association between a contact and a NetSuite record. Refer to [REST Web Services prerequisites and setup](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) for setup requirements.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to detach the contact from. The picklist shows only records supported by NetSuite REST Web Services. Toggle the field to use a custom record. |
| Internal ID | Enter the internal ID of the record to detach the contact from. |
| Contact ID | Enter the internal ID of the contact to detach. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the contact was detached from the record successfully. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/detach-file-from-record-action.md
description: >-
  The Detach file from record action detaches a file from a record in NetSuite
  REST.
---

# NetSuite REST - Detach file from a record action

The **Detach file from a record** action detaches a file from a record in NetSuite REST.

Use this action to remove the association between a file and a NetSuite record. Refer to [REST Web Services prerequisites and setup](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) for setup requirements.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to detach the file from. The picklist shows only records supported by NetSuite REST Web Services. Toggle the field to use a custom record. |
| Internal ID | Enter the internal ID of the record to detach the file from. |
| File ID | Enter the internal ID of the file to detach. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the file was detached from the record successfully. |

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/execute-restlet-script-action.md
description: >-
  The Execute RESTlet script action in the NetSuite REST connector lets you
  import or export data by calling a RESTlet script and deployment ID.
---

# NetSuite REST - Execute RESTlet script action

Use this action to export or import data in NetSuite.

Learn more about [NetSuite RESTlet](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4387799403.html#SuiteScript-2.x-RESTlet-Script-Type).

## Input

| Input field | Description |
| --- | --- |
| Operation | Select a RESTlet operation to perform from the picklist. Available operations include **Import** and **Export**. **Export** operations use **GET** methods and **Import** use **POST** HTTP methods to interact with RESTlet APIs. |
| Script ID | Provide the RESTlet script ID to perform the operation. You can get the script ID from within your NetSuite instance in **Customization > Scripting > Scripts > NetSuite script record**. |
| Deployment ID | Provide the RESTlet script deployment ID to perform the operation. Obtain the deployment ID from your NetSuite instance in **Customization > Scripting > Scripts > NetSuite script record > Deployments**. |
| Request URL parameters | Determine what the URL parameters should be and assign values to them. You can set up these parameters in Workato's graphical UI by clicking **Add URL parameter**. Then, provide a **Label**, **Data type**, and **Hint** (optional) in the **Add new field modal**. Alternatively, you can add the request URL parameters manually by providing a JSON description of your schema. |
| Request body parameters | This input field is only available when you perform an **Import** operation. Click **Use JSON** to describe your request body parameters in JSON, or click **add fields manually** to fill out the **Add new field** modal, determining the **Name**, **Label**, **Data type**, whether the parameter is **Optional**, and the **Hint** for each of your parameters. |
| Response type | Determine a response type. You can choose between JSON and plain text. |
| Output schema | Click **Use JSON** to describe all fields in your response using JSON, or click **add fields manually** to fill out the **Add new field** modal, determining the **Name**, **Label**, **Data type**, whether the parameter is **Optional**, and the **Hint** for each of your parameters. |

## Output

This action does not generate any output data for use in downstream recipe steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/execute-suiteql-query-action.md
description: >-
  The Execute SuiteQL query action in the NetSuite REST connector lets you run a
  custom SELECT query against your database with quota and offset controls.
---

# NetSuite REST - Execute SuiteQL query action

Use the SuiteQL action to execute a custom query against your NetSuite database. This connector only supports the `SELECT` query.

## Input

| Input field | Description |
| --- | --- |
| SuiteQL query | Provide a valid SuiteQL query. |
| Limit | The number of records you plan to fetch. The maximum is 1000 and the default is 100. |
| Offset | The starting position from which records are fetched. The default offset is 0. |
| Output schema | Click **Use SUITEQL** to describe all fields in your response using SuiteQL, or click **add fields manually** to fill out the **Add new field** modal, determining the **Name**, **Label**, **Data type**, whether the parameter is **Optional**, and the **Hint** for each of the fields in your response. |

## Output

This action does not generate any output data for use in downstream recipe steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/get-custom-record-by-id-action.md
description: >-
  The Get custom record by ID action in the NetSuite REST connector lets you
  fetch a custom record by using the internal ID from NetSuite.
---

# NetSuite REST - Get custom record by ID action

The **Get custom record by ID** action allows you to fetch a custom record using the internal ID from NetSuite REST.

Refer to the NetSuite [Prerequisites and Setup for REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) guide for more information.

## Input

| Input field | Description |
| --- | --- |
| Custom record | Select a NetSuite custom record type, or toggle to enter a custom value. The list populates from the custom record types located in your account at **Customization > Records > Record Types**. |
| Internal ID | Provide the internal ID of the record to fetch. |

## Output

The output fields depend on the **Custom record** type you select. Common fields include the following:

| Output field | Description |
| --- | --- |
| Last modified by | The user who last modified the record. |
| Links | The related resource links for the record. |
| Owner | The owner of the record. |
| Reference Name | The reference name of the record. |

Additional fields appear based on the **Custom record** type you select.

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/get-record-by-id-action.md
description: >-
  The Get record by ID action retrieves a record from NetSuite using its
  internal ID.
---

# NetSuite REST - Get record by ID action

The **Get record by ID** action retrieves a record from NetSuite using its internal ID.

## Input

| Input fields | Description |
| --- | --- |
| Record | Select a [NetSuite record](#record-types) to retrieve, or toggle this field to enter a custom record type ID. |
| Internal ID | Enter the internal ID of the record to retrieve. |

### Record types

This action supports the following record types:

- Account
- Accounting period
- Advanced intercompany journal entry
- Assembly item
- Billing account
- Billing schedule
- Bin
- Bin transfer
- Cash refund
- Cash sale
- Change order
- Charge
- Check
- Class
- Commerce category
- Consolidated exchange rate
- Contact
- Contact category
- Contact role
- Cost category
- Credit card charge
- Credit card refund
- Credit memo
- Currency
- Customer
- Customer category
- Customer deposit
- Customer payment
- Customer refund
- Customer subsidiary relationship
- Department
- Deposit
- Deposit application
- Description item
- Discount item
- Email template
- Employee
- Estimate
- Event
- Expense category
- Expense report
- Fulfillment request
- Inbound shipment
- Intercompany journal entry
- Intercompany transfer order
- Inventory adjustment
- Inventory cost revaluation
- Inventory count
- Inventory item
- Inventory number
- Inventory transfer
- Invoice
- Item fulfillment
- Item group
- Item receipt
- Job
- Job status
- Job type
- Journal entry
- Kit item
- Location
- Markup item
- Message
- Nexus
- Non-inventory purchase items
- Non-inventory resale item
- Non-inventory sale item
- Opportunity
- Other charge for purchase item
- Other charge for resale item
- Other name
- Other name category
- Payment item
- Phone call
- Price book
- Price level
- Price plan
- Pricing group
- Project task
- Purchase order
- Requisition
- Return authorization
- Sales order
- Sales tax item
- Service purchase item
- Service resale item
- Service sale item
- Ship item
- Statistical journal entry
- Subscription
- Subscription line
- Subscription plan
- Subscription term
- Subsidiary
- Subtotal item
- Task
- Tax type
- Time bill (track time)
- Transfer order
- Unit of measure
- Usage
- Vendor
- Vendor bill
- Vendor category
- Vendor credit
- Vendor prepayment
- Vendor prepayment application
- Vendor return authorization
- Vendor subsidiary relationship

Refer to the NetSuite [REST Web Services Supported Records](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_1558962745.html) documentation for more information.

## Output

The output fields depend on the record you select. Each record returns a unique set of fields based on its type.

---
