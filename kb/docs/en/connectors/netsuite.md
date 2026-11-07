---
url: 'https://docs.workato.com/en/connectors/netsuite.md'
description: >-
  The NetSuite connector lets you automate ERP and CRM workflows: create,
  update, upsert, delete, and search standard and custom records, plus record
  triggers.
---

# NetSuite

[NetSuite](http://www.netsuite.com/) is a cloud business management suite that offers comprehensive software solutions for organizations, including support for ERP/Financials, CRM, and e-commerce.

> **NETSUITE SOAP WEB SERVICES SUPPORT POLICY CHANGES**
> 
> According to the official press [release](https://community.oracle.com/netsuite/english/discussion/4508412/soap-web-services-endpoint-release-and-support-policy-changes), NetSuite is beginning to phase out SOAP support and want everyone to build new integrations using REST APIs. NetSuite is continuously adding new operations and exposing additional record types into REST to achieve parity with SOAP.
> 
> Starting with the 2026.1 release, NetSuite will stop releasing SOAP endpoints by default, unless NetSuite explicitly announces a new one for critical reasons where 2025.2 is expected to be the last routine SOAP endpoint.
> 
> Existing SOAP integrations will continue to work and be supported as long as the specific SOAP endpoint version you are using remains within its 3-year support window. As part of our long-term integration strategy for NetSuite, we recommend using the [NetSuite REST connector](/en/connectors/netsuite-rest) for all new integrations, and also begin planning the migration of existing SOAP-based integrations to REST Web Services.
> 
> Workato actively monitors NetSuite API changes to deliver updates to the Workato NetSuite SOAP and NetSuite REST connectors. The NetSuite REST connector doesn't offer full-feature parity with the NetSuite SOAP connector. Review your use case to determine whether the NetSuite REST connector meets your requirements before you begin your implementation.
> 
> Workato recommends that you monitor NetSuite’s API changes when planning your integration strategies.

## API version

The NetSuite connector uses the WSDL from the [SuiteTalk 2025\_2 API](https://www.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2025_2/schema/record/account.html). This gives you access to objects introduced in past API versions and all records in the **Schema Browser** tab of the API reference documentation.

## Connect to NetSuite on Workato

You can connect to NetSuite through token-based authentication. You must first generate an application ID, a consumer key, a consumer secret, a token ID, and a token secret.

We recommend that you reference our video channel for instructions on "How to connect to NetSuite":

[Video](https://www.youtube.com/embed/F29lbb9jN74)

See [Connect to NetSuite on Workato](/en/connectors/netsuite/netsuite-connect) for detailed steps on how to connect to Netsuite through token-based authentication.

## Common NetSuite fields

The NetSuite connector can retrieve your standard or custom NetSuite objects and the associated set of standard and custom fields. When you configure your trigger or action, you must first select the specific object for interaction.

See [Common NetSuite fields](/en/connectors/netsuite/netsuite-common-fields) for details.

## Triggers

Workato has the following triggers for NetSuite:

- [Export new and updated standard or custom records trigger (bulk)](/en/connectors/netsuite/export-new-updated-record-bulk-trigger)
  
- [New classification object trigger](/en/connectors/netsuite/netsuite-classification-object-trigger)
  
- [New standard object and new custom object trigger](/en/connectors/netsuite/netsuite-new-records-trigger)
  
- [Updated standard object and updated custom object trigger](/en/connectors/netsuite/netsuite-updated-records-trigger)
  
- [New standard object and new custom object batch trigger](/en/connectors/netsuite/netsuite-new-records-batch-trigger)
  
- [New saved search result for object trigger](/en/connectors/netsuite/netsuite-new-saved-search-trigger)
  
- [New/updated saved search result for object trigger](/en/connectors/netsuite/netsuite-update-saved-search-trigger)
  
- [Export new standard records](/en/connectors/netsuite/netsuite-export-new-standard-records)
  
- [Export new custom records](/en/connectors/netsuite/netsuite-export-new-custom-records)
  
- [Export new/updated standard records](/en/connectors/netsuite/netsuite-export-new-updated-standard-records)
  
- [Export new/updated custom records](/en/connectors/netsuite/netsuite-export-new-updated-custom-records)
  
- [Deleted standard record](/en/connectors/netsuite/deleted-standard-record-trigger)
  

DEPRECATION OF TRIGGER CONDITIONS IN BATCH TRIGGERS

Trigger conditions are deprecated and will be removed from NetSuite SOAP batch triggers on **October 23, 2025**.

This change improves accuracy and consistency when filtering records. Trigger conditions only evaluate the **first record** in each batch. This means that even if the first record matches the condition, the batch may still include records that don't, which leads to inconsistent batch sizes. In contrast, the **Search settings** field filters records in NetSuite before Workato retrieves them. This ensures that each batch contains only records that meet the criteria.

This update removes trigger conditions from the following NetSuite SOAP batch triggers:

- [New classification records](/en/connectors/netsuite/netsuite-classification-object-trigger)
- [New custom records](/en/connectors/netsuite/new-custom-records-saved-search-batch)
- [New standard records](/en/connectors/netsuite/new-standard-records-saved-search-batch)
- [New/updated custom records](/en/connectors/netsuite/new-updated-custom-records-saved-search-batch)
- [New/updated standard records](/en/connectors/netsuite/new-updated-standard-records-saved-search-batch)

To avoid any disruptions, we recommend updating your recipes to use the **Search settings** field before **October 23, 2025**. This approach improves performance and gives you more control over data retrieval.

Complete the following steps to update your batch trigger:

1. Open the trigger configuration in your NetSuite SOAP recipe.
   
2. Ensure the **Set trigger condition** toggle is disabled.
   
   ![Disable the Set trigger condition toggle](/assets/disable-trigger-toggle.DUoe25ye.png)_Disable the **Set trigger condition** toggle_
   
3. Expand the **Search settings** section.
   
4. Choose an operator for each field type to define how values should be matched.
   
   ![Configure Search settings by selecting operators for each field type](/assets/configure-search-settings.Cht2SSZn.png)_Configure **Search settings** by selecting operators for each field type_
   
5. Add the fields you plan to filter from the optional fields list, set their values, and save the trigger configuration.
   
6. Test your recipe to confirm that batches include only matching records.
   

If you have questions or need help updating your recipes, reach out to your Customer Success Manager.

### Example: Filtering sales orders by status

This example shows how results can differ depending on which method you use to filter sales orders by status.

Trigger conditions check only the first record in the batch. The platform processes the entire batch if that record matches, even when other records don't.

![Trigger condition for batch trigger](/assets/trigger-cond-batch1.CaPhAgSO.png)_Trigger condition evaluates only the first record_

As a result, the batch may include records with different statuses:

![Trigger condition job result](/assets/trigger-cond-jobs.TszQocVH.png)_Batch includes records that don't meet the condition_

**Search settings** apply the filter within NetSuite before the batch is retrieved, so only matching records are included:

![Search settings job result](/assets/search-settings-jobs.CNSXd9_R.png)_Batch includes only records that match the condition_

## Actions

Workato has the following actions for Netsuite:

- [Create standard object and create custom object action](/en/connectors/netsuite/netsuite-add-object-action)
  
- [Create standard object and create custom object in bulk action](/en/connectors/netsuite/netsuite-create-object-batch-action)
  
- [Create standard record and create custom record in batch action](/en/connectors/netsuite/action-batch-create)
  
- [Get all standard objects action](/en/connectors/netsuite/netsuite-get-standard-objects-action)
  
- [Get case comments action](/en/connectors/netsuite/netsuite-get-case-comments-action)
  
- [Search standard objects action](/en/connectors/netsuite/netsuite-search-standard-object-action)
  
- [Search custom objects action](/en/connectors/netsuite/netsuite-search-custom-object-action)
  
- [Update standard object and update custom object action](/en/connectors/netsuite/netsuite-update-object-action)
  
- [Update records in batch](/en/connectors/netsuite/action-batch-update)
  
- [Update records in bulk](/en/connectors/netsuite/netsuite-update-batch-action)
  
- [Upsert records in batch](/en/connectors/netsuite/action-batch-upsert)
  
- [Upsert records in bulk](/en/connectors/netsuite/netsuite-upsert-batch-action)
  
- [Get case comments action](/en/connectors/netsuite/netsuite-get-case-comments-action)
  
- [Delete standard record action](/en/connectors/netsuite/delete-standard-record)
  
- [Delete standard records action (batch)](/en/connectors/netsuite/delete-standard-records)
  
- [Delete custom record action](/en/connectors/netsuite/delete-custom-record)
  
- [Delete custom records action (batch)](/en/connectors/netsuite/delete-custom-records)
  
- [Initialize record action](/en/connectors/netsuite/initialize-record)
  

## Unsupported records

There are certain records that triggers and search actions do not support, as they cannot be queried via the NetSuite API.

Users can use the `Get all standard records` action to retrieve these objects not found in search actions or triggers:

- Budget category
- Campaign audience
- Campaign category
- Campaign channel
- Campaign family
- Campaign offer
- Campaign search engine
- Campaign subscription
- Campaign vertical
- Currency
- Lead source
- State
- Support case issue
- Support case origin
- Support case priority
- Support case status
- Support case type
- Tax account

The following records are not supported:

- Campaign response
- Item revision
- Landed cost
- Sales tax item
- Tax group
- Tax type
- Currency revaluation
- Payroll adjustment
- Inventory worksheet

---
