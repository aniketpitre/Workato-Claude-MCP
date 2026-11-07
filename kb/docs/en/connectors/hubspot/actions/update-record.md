---
url: 'https://docs.workato.com/en/connectors/hubspot/actions/update-record.md'
description: >-
  The Update record action in the HubSpot connector lets you update an existing
  record with given properties and returns the updated record details.
---

# HubSpot - Update record action

The **Update record** action enables you to update existing records in your HubSpot instance with the given properties and receives the details of the updated record, including the ID.

This action supports the following objects:

- Contact
- Company
- Deal
- Product
- Ticket
- Line item
- Quote
- Custom objects

> **AUTOMATICALLY POPULATE PROPERTIES WITH HUBSPOT INSIGHTS**
> 
> HubSpot automatically attempts to populate some properties with [HubSpot Insights](https://knowledge.hubspot.com/articles/kcs_article/companies/what-is-hubspot-insights) if you provide a company's website domain name. Refer to the HubSpot documentation to learn how to [disable HubSpot Insights](https://knowledge.hubspot.com/articles/kcs_article/companies/hubspot-insights-on-company-records).

## Input

You must select the object you plan to update before you can configure this action. Workato populates the object's associated properties after you select it. Specify the ID of the record you plan to update. Enter `clear` in formula mode to delete the value of a specific field.

> **CONTACT OWNER**
> 
> If you select the **Contact** object as your record to update, ensure that you also select the `crm.objects.owners.read` scope during connection setup. This enables you to access the values in the **Contact owner** list input field.

## Output

Workato returns an object representing the updated record. You can use these datapills in subsequent recipe steps. The ID, Created at, Updated at and Archived datapills contain a value automatically. The remaining datapills contain information if the corresponding field contained information when created. Some fields may pass in default values, which are also returned.

---
