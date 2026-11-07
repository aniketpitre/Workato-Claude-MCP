---
url: 'https://docs.workato.com/en/connectors/hubspot/actions/create-record.md'
description: >-
  The Create record action in the HubSpot connector lets you create a record or
  batch of records and set the values of relevant properties.
---

# HubSpot - Create record action

The **Create record** action allows you to create a record or a batch of records in HubSpot. You can specify the values of relevant properties during creation. Workato supports the following objects:

- Contact
- Company
- Deal
- Ticket
- Product
- Line item
- Quote
- Custom objects

> **AUTOMATICALLY POPULATE PROPERTIES WITH HUBSPOT INSIGHTS**
> 
> HubSpot attempts to automatically populate some properties with [HubSpot Insights](https://knowledge.hubspot.com/articles/kcs_article/companies/what-is-hubspot-insights) if you provide a company's website domain name. Refer to the HubSpot documentation to learn how to [disable HubSpot Insights](https://knowledge.hubspot.com/articles/kcs_article/companies/hubspot-insights-on-company-records).

## Input

You must select the object you plan to create before you can configure this action. Workato populates the object's associated properties automatically after you select it. Fill in required fields to prevent errors when attempting to create the record.

> **CONTACT OWNER**
> 
> If you select the **Contact** object as your record to create, ensure that you also select the `crm.objects.owners.read` scope during connection setup. This enables you to access the values in the **Contact owner** list input field.

## Output

Workato returns an object representing the record. You can use these datapills in subsequent recipe steps. The ID, Created at, Updated at and Archived datapills contain a value automatically. The remaining datapills contain information if the corresponding field contained information when created. Some fields may pass in default values, which are also returned.

---
