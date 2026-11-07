---
url: 'https://docs.workato.com/en/connectors/netsuite/netsuite-common-fields.md'
description: >-
  Reference for common NetSuite fields such as internal ID, external ID, and
  IDs, and how to select standard and custom fields when configuring the
  connector.
---

# Common NetSuite fields

The NetSuite connector can retrieve your standard or custom NetSuite objects and the associated set of standard and custom fields. When you configure your trigger or action, you must first select the specific object for interaction.

> **Renamed objects; possible disparity**
> 
> Objects in your NetSuite instance may be renamed. However, they appear in Workato with the original name instead of the new name. Check these with your NetSuite admin, or reach out to us if you cannot find your object on Workato.

When configuring an action, you can see the fields selector with a list of standard and custom fields that belong to the selected object. Simply select the fields for interaction.

![NetSuite fields selector](/assets/netsuite-fields-selector.CoVQPnea.png)_NetSuite fields selector_

Some of these fields display their internal API names instead of their labels in NetSuite. See the list of [Common NetSuite fields](/en/connectors/netsuite/netsuite-common-fields). Some of these have a different name in Workato.

- Internal ID
  
- Every NetSuite record has a unique internal ID, which you can find in the URL when viewing the specific NetSuite record. Internal IDs are usually used to specify the exact record to update for update object actions. Obtain them from the datatree of create object actions or search object actions.
  
  ![NetSuite Internal ID](/assets/internal-id-in-netsuite-url.BDsHlj4b.png)_Internal ID of a specific sales order as seen in the URL_
  
- External ID
  
- Every NetSuite record has an external ID field to store the IDs of corresponding objects in other systems - for example, you can store the corresponding Salesforce ID of a NetSuite customer in that customer's external ID field.
  
  This field is a standard field in NetSuite, but typically not visible by default in NetSuite.
  
- ID
  
- When you link an object to another object in Workato, NetSuite usually asks for the object's IDs to which you plan to link. For example, when you create a transaction and try to link this transaction to a class, department, or subsidiary, Netsuite requests the object's IDs. To find these IDs, you typically must search for these objects. Following the preceding example, in this situation, you must search for your class, department, or subsidiary. Alternatively, you can store these values in a [lookup table](/en/features/lookup-tables) for easy reference without having to execute a search in your NetSuite instance.
  
- Custom fields
  
- The recipe is able to retrieve the custom fields of your selected NetSuite object for you to read from or write to. All custom fields are grouped together under the parent `Custom fields`.
  
  When working with custom fields that reference other objects in NetSuite, you can now reference these objects using their internal or external IDs. To reference another object using its external ID, you must add a prefix to the value specified.
  
  > **19/5/2020 Enhancement**
  > 
  > As of 19/5/2020, we have made a significant enhancement to the migration of NetSuite recipes from Sandbox to Production environments. This requires you to take certain steps for any NetSuite recipes created on or before 19/5/2020. Learn more in [Migrating NetSuite recipes across environments](/en/connectors/netsuite/netsuite-recipe-migration)
  
  ![NetSuite custom fields](/assets/netsuite-custom-fields.Ci7tveaV.png)_Custom fields Tax Receipt No. and External ID_
  
- Item list
  
- For transaction objects that contains line items, you can find the available fields within each line item grouped within the item list field.
  
  ![NetSuite item list](/assets/netsuite-item-list.BE4frzCa.png)_Item list displayed in the create sales order action_

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-unsupported-records.md
description: >-
  Reference for NetSuite records that triggers and search actions do not support
  because they cannot be queried through the NetSuite API.
---

# Unsupported records in NetSuite

Triggers and search actions do not support certain records because they cannot be queried through the NetSuite API.

## Unsupported objects in search record action and trigger

You can use the **Get all standard records** action to retrieve objects that do not appear in search actions:

- Budget category
- Campaign audience
- Campaign category
- Campaign channel
- Campaign family
- Campaign response
- Campaign offer
- Campaign search engine
- Campaign subscription
- Campaign vertical
- Currency
- Landed cost
- Lead source
- Sales tax item
- State
- Support case issue
- Support case origin
- Support case priority
- Support case status
- Support case type
- Tax account
- Tax group
- Tax type

## Unsupported objects in trigger

We do not support new and new/updated triggers for the following objects:

- Accounting period
- Billing account
- Billing schedule
- Bin
- Budget
- Campaign response
- Contact category
- Contact role
- Cost category
- Coupon code
- Custom list
- Customer category
- Customer message
- Customer status
- Entity group (new trigger not supported)
- Expense category
- Fair value price
- Folder (new trigger not supported)
- Gift certificate (new/updated trigger not supported)
- Global account mapping
- Inventory number
- Item account mapping
- Item revision
- Job status
- Job type
- Landed cost
- Manufacturing cost template
- Manufacturing operation task
- Manufacturing routing
- Nexus
- Other name category
- Partner category
- Payment method
- Payroll item
- Phone call
- Price level
- Pricing group
- Promotion code
- Rev rec schedule
- Rev rec template
- Sales role
- Sales tax item
- Site category
- Solution
- Tax group
- Tax type
- Term
- TimeSheet
- Topic
- Units type
- Vendor category
- Win loss reason

---
