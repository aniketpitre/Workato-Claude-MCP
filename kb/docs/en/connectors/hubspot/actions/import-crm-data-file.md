---
url: 'https://docs.workato.com/en/connectors/hubspot/actions/import-crm-data-file.md'
description: >-
  The Import CRM data action in the HubSpot connector lets you bulk import data
  from a CSV file into a HubSpot object such as contacts or deals.
---

# HubSpot - Import CRM data action

The **Import CRM data** action allows you to import data in HubSpot in bulk. Your file size must be less than 512 MB and must have less than 1,048,576 rows.

## Input

| Input field | Description |
| --- | --- |
| File name | Provide a unique name for the file. |
| Object | Use the drop-down menu to choose **Select an object** or **Enter object ID**. You can select any standard HubSpot object, including contacts, companies, deals, and more. |
| Operation | Use the drop-down menu to choose **Select operation** or **Enter operation**. This sets the operation used for the import. |
| Import name | Enter a unique name for the import. This is used to identify the import. |
| CSV file input | Describe your CSV file and column names. |
| File contents | CSV file contents are used to bulk upload records in HubSpot. Ensure that the CSV contains unique column names for all fields. The import file must contain at least two rows. |
| Column separator | Use the drop-down menu to select the column separator you plan to use. For example, comma (`,`) or pipe (`|`). |
| Column names | Click **Use a sample file** to use a sample file to input all column names at the same time. If you do not have a sample file, click **Add column name** to manually enter your column names. |
| Use CSV column names as HubSpot field names | This field is optional. Select **Yes** if you plant to map CSV columns to HubSpot object fields automatically. The CSV file must have a header line with column names matching the object fields. |
| Association | This field is optional. Select the objects for association. If you have multiple associations, ensure that the CSV column names are unique and mapped to the correct object. |
| Wait for HubSpot to process all records? | Select **Yes** or **No** from the drop-down menu. If **Yes** is selected, the action returns when HubSpot processes all the rows in the CSV file. If **No** is selected, the action moves to the next recipe action after the CSV file is uploaded to HubSpot. |

## Output

Workato returns a record representing each imported record. You can use these datapills in subsequent recipe steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/get-contacts-in-list-batch.md
description: >-
  The Get contacts in list batch action in the HubSpot connector retrieves all
  details about contacts in a specific contact list.
---

# HubSpot - Get contacts in list action (batch)

The **Get contacts in list** batch action retrieves all details about contacts in a specific contact list in HubSpot.

## Input

| Input field | Description |
| --- | --- |
| List | List from which you plan to retrieve contacts. |
| Properties | The property of the contact that's returned in the response. For example, city, street address, and more. See the [Hubspot API Reference](https://developers.hubspot.com/docs/guides/api/crm/search) for a list of returned properties. |

## Output

| Output field | Description |
| --- | --- |
| ID | The HubSpot ID of the contact. |
| Created at | The timestamp when the contact was created. |
| Updated at | The most recent date that any property on a contact record was updated. |
| Archived | Indicates if the contact has been archived. |
| Last Modified Date | The most recent date that any property on a contact record was updated. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> This trigger also provides a datatree with the contact's attributes and values. Additional fields depend on the **Properties** you select. Refer to HubSpot's [Properties](https://knowledge.HubSpot.com/properties/hubspots-default-contact-properties) guide for more information about retrievable properties.

---

---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/add-contact-to-list-batch.md
description: >-
  The Add contact to list batch action adds existing contact records to a
  contact list in HubSpot.
---

# HubSpot - Add contact to list action (batch)

The **Add contact to list** batch action adds existing contact records to a contact list. You can only add contacts to a static HubSpot list, not to a dynamic list.

## Input

| Input field | Description |
| --- | --- |
| List | The ID of the target contact list you plan to add contacts to. |
| Contact IDs | Contact IDs source list | The array of contacts to be added to the list. |
| ID | The ID of the contact to be added to the list. |

## Output

| Output field | Description |
| --- | --- |
| Record IDs removed | Record IDs of contacts that have been removed from the list. |
| Record IDs added | Record IDs of contacts successfully added to the list. |
| Record IDs missing | Record IDs of contacts not found in your HubSpot instance. |

---

---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/add-contact-to-workflow.md
description: >-
  The Add contact to workflow action adds contacts into a workflow in the event
  that the contact meets a set of criteria.
---

# HubSpot - Add contact to workflow action

The **Add contact to workflow** action adds contacts into a workflow if that contact meets a set of criteria.

For example, a contact who downloads a whitepaper can be added to a workflow that sends follow-up emails based on the whitepaper's content.

## Input

| Input field | Description |
| --- | --- |
| Workflow | The workflow you plan to enroll the contact into. |
| Contact email | The email that corresponds to the contact to add to the workflow |

## Output

This action doesn't return any output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/remove-contact-from-list-batch.md
description: >-
  The Remove contact from list batch action in the HubSpot connector removes
  contacts from a specified static list in your HubSpot instance.
---

# HubSpot - Remove contact from list action (batch)

The **Remove contact from list** batch action removes contacts from a specified contact list. You can only remove a contact from a static HubSpot list, not from a dynamic list.

## Input

| Input field | Description |
| --- | --- |
| List | The ID of the target contact list where you plan to remove contacts. |
| Contact IDs | Contact IDs source list | The array of contacts to be removed from the list. |
| ID | The ID of the contact you plan to remove from the list. |

## Output

| Output field | Description |
| --- | --- |
| Record IDs removed | Record IDs of contacts removed from the list. |
| Record IDs added | Record IDs of contacts successfully added to the list. |
| Record IDs missing | Record IDs of contacts not found in your HubSpot instance. |

---
