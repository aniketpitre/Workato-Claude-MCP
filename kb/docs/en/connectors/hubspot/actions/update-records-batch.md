---
url: 'https://docs.workato.com/en/connectors/hubspot/actions/update-records-batch.md'
description: >-
  The Update records batch action in the HubSpot connector lets you update
  existing records such as contacts, companies, and deals in batches.
---

# HubSpot - Update records action (batch)

The **Update records** batch action enables you to update existing records in your HubSpot instance in batches.

This action supports the following objects:

- Contacts
- Companies
- Deals
- Ticket
- Products
- Line items

> **CONTACT BATCH UPDATE OPERATION**
> 
> Batch operations for contacts are limited to batches of 10. [Learn more](https://developers.hubspot.com/docs/guides/api/crm/objects/contacts).

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to update in batches. |

Additional input fields are available based on the object you select.

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the batch update operation. |
| Requested at | Timestamp indicating when the batch update request was submitted. |
| Started at | Timestamp indicating when the batch update processing began. |
| Completed at | Timestamp indicating when the batch update processing finished. |
| Links | A set of URLs for checking the batch status or retrieving results. |
| Results | A list of updated records returned from the batch operation. |
| ID (results) | The unique identifier of the updated record. |
| Created at (results) | Timestamp indicating when the record was originally created. |
| Updated at (results) | Timestamp indicating when the record was last updated. |
| Archived (results) | Indicates whether the record is archived. |
| Archived at (results) | Timestamp indicating when the record was archived, if applicable. |
| Properties (results) | A collection of updated property values for the record, based on the object schema. |

---

---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/get-associations-batch.md
description: >-
  The Get associations batch action in the HubSpot connector lets you retrieve
  all associations of an object by object type.
---

# HubSpot - Get associations action (batch)

The **Get associations** batch action allows you to retrieve all associations of an object by object-type.

## Input

| Input field | Description |
| --- | --- |
| From object | This is the object you're associating. Use the drop-down menu to choose **Select from list** or **Use custom value**. |
| To object | This is the object you're associating the record to. Use the drop-down menu to choose **Select from list** or **Use custom value**. |
| From object ID | The ID of the record to associate. |

## Output

If the request is successful, Workato returns a list of records associated with the selected records. You can use these datapills in subsequent recipe steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/get-contacts-associated-with-company-batch.md
description: >-
  The Get contacts associated with a company batch action in the HubSpot
  connector retrieves all contacts associated with a company by company ID.
---

# HubSpot - Get contacts associated with a company action (batch)

The **Get contacts associated with a company** batch action retrieves all contacts associated with a company in HubSpot in descending order when you provide the company ID.

## Input

| Input field | Description |
| --- | --- |
| Company ID | The ID of the company from which you plan to get associated contacts. You can find the company ID at the end of the URL of the company's page. |
| Count | Specify the number of contacts to return in the response. 20 contacts are returned if no limit is set. |
| Properties | Only contact properties you select are returned. Leave this field blank if you plan to retrieve all properties. |
| Property mode | Select the value and version history to retrieve the entire version history of the contact properties. |

## Output

If the request is successful, Workato returns a list of records that the company contact is associated with. You can use these datapills in subsequent recipe steps.

This action retrieves all contacts associated with a company in HubSpot in descending order when you provide the company ID. Additionally, you can select whether to retrieve the version history of fields and/or the list memberships of the contact.

---

---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/list-associations-batch.md
description: >-
  The List associations batch action in the HubSpot connector retrieves all
  associations for the specified object IDs, up to 2000 records.
---

# HubSpot - List associations action (batch)

The **List associations** batch action retrieves all associations for the specified object IDs. It accepts a list of maximum 2000 records. The action fails if you provide more than 2000 records.

## Input

| Input field | Description |
| --- | --- |
| From object | Select the source object type for the associations. |
| To object | Select the target object type to which the source object may be associated. |
| Input parameters | Expand this section to configure the list of source object IDs. |
| Input parameters source list | Input a list datapill representing the object IDs to use for the batch request. The maximum is 2000 records. |
| From object ID | Specify the object ID to list associations from. |
| After | Map the pagination token to retrieve the next page of results. |

## Output

| Output field | Description |
| --- | --- |
| Results | A list of association results returned by the action. Each result includes the associated records for a given object ID. |
| From | The source object in the association, including its ID. |
| Paging | Contains pagination details for retrieving the next set of results. |
| To | A list of associated objects linked to the source object. |
| Errors | A list of any errors that occurred during processing. |
| Status (errors) | The error status code, if applicable. |
| Category (errors) | The category or type of the error. |
| Sub category (errors) | A more specific classification of the error. |
| Message (errors) | A message describing the error. |

---
