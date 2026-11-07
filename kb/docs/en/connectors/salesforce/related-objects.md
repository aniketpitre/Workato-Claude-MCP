---
url: 'https://docs.workato.com/en/connectors/salesforce/related-objects.md'
description: >-
  Learn how Salesforce object relationships work in Workato and how to use the
  Related objects and Fields inputs to retrieve data from related objects.
---

# Salesforce object relationships

Salesforce uses object relationships to associate data between two objects. These relationships use custom relationship fields and allow users to access related data directly from a record.

For example, the `Account` and `Contact` objects have a relationship where each contact stores a reference to one account, while each account can link to many contacts. This setup lets you view all contacts associated with an account directly from the account record.

Salesforce supports several types of object relationships, such as:

- Master-detail
- Lookup
- Hierarchical

Refer to the Salesforce documentation for more information on [object relationships](https://help.salesforce.com/articleView?id=overview_of_custom_object_relationships.htm&type=5).

## Related objects field

In Workato, all [Salesforce triggers and SOQL search actions](https://www.workato.com/integrations/salesforce) support the **Related objects** and **Fields** inputs. These inputs appear when you select **Show optional fields** and let you retrieve data from related objects, such as lookup relationships.

> **POLYMORPHIC RELATIONSHIPS**
> 
> You must use the **Relationships fields** input to specify polymorphic relationships when configuring bulk actions. Refer to Salesforce's [Relationship Fields in a Header Row](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/relationship_fields_in_a_header_row__2_0.htm) guide for more information on polymorphic fields.

![Related objects field](/assets/related-objs-fields.w3zX-atg.png)_'Related objects' and 'Fields' inputs on triggers and actions_

## Access fields in parent objects

The following example demonstrates how to trigger a recipe on new or updated **Opportunity** records and access fields from its related **Account**.

To do this, you will:

- Use the **New/updated record** trigger on the **Opportunity** object.
- Select fields from the related **Account** object to include in the trigger data.

Complete the following steps to configure the trigger and access the related **Account** fields:

1. Select **Opportunity** from the **Object** drop-down menu.
   
2. Open the **Related objects** drop-down menu and select **Account** to include fields from the parent object.
   
   ![Select related object](/assets/parent-field-dropdown.Cl-YgQKc.png)_Only parent objects appear in the drop-down menu_
   
3. Use the **Fields** input to select the required fields from both **Opportunity** and **Account**. Fields from related objects are listed with dot notation. For example, `Account.Account ID` and `Account.Deleted`.
   
   Use the search bar to find fields quickly. If you leave this input field blank, the trigger retrieves only the fields from the **Opportunity** object.
   
   ![Fields field](/assets/fields-field-1.BcNza8EG.png)_Fields from **Opportunity** and its related **Account** object_
   
   To include fields like mailing address and business phone from **Account**, select them in the **Fields** input. These fields then appear in the datatree for use in subsequent recipe steps.
   

## Access fields in grandparent objects

In this example, **Opportunities** relate to **Contacts** or **Accounts**, and those objects relate to **Users**.

> **GRANDPARENT RELATIONSHIPS**
> 
> You must know the relationship field names in your Salesforce schema to access grandparent relationships.

![Grandparent hierarchy](/assets/grandparent-hierarchy.C96H8T7_.png)_Example of child-parent-grandparent relationship structure_

Complete the following steps to retrieve data from a grandparent object:

1. Toggle the **Related objects** field to enable text input.
   
2. Enter the relationship path using comma-separated values. For example:
   
   ```text
   Primary_Contact__r,Primary_Contact__r.User__r
   ```
   
     
   - Use `__r` to denote a relationship.
   - For custom objects that end in `__c`, replace it with `__r`. For example, `Invoice__c` becomes `Invoice__r`.
3. Ensure the relationship names are case-sensitive and match exactly. For example, `Primary_contact__r` fails if the correct name is `Primary_Contact__r`.
   
4. Select fields from both parent and grandparent objects in the **Fields** input.
   
   ![Fields field 2](/assets/grandparent-relationship-selected.D_k0Vpdv.png)_Fields from parent and grandparent objects selected_

---
