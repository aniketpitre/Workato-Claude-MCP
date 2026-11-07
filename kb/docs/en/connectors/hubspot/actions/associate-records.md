---
url: 'https://docs.workato.com/en/connectors/hubspot/actions/associate-records.md'
description: >-
  The Associate records action in the HubSpot connector lets you create an
  association between two records in your HubSpot instance.
---

# HubSpot - Associate records action

The **Associate records** action allows you to create an association between two records.

## Input

| Input field | Description |
| --- | --- |
| From | Expand the From section and use the **Object** menu to choose **Select from list** or **Use custom value**. This is the object you're associating. |
| Object ID | The ID of the record to associate. |
| Association types | Use the drop-down menu to choose **Select from list** or **Enter custom value**. Leave this field blank to create a default (most generic) association. |

## Output

If the request is successful, Workato returns a list of records associated with the selected records. You can use these datapills in subsequent recipe steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/associate-records-batch.md
description: >-
  The Associate records batch action in the HubSpot connector creates
  associations between records, accepting up to 2000 records per request.
---

# HubSpot - Associate records action (batch)

The **Associate records** batch action creates associations between records in HubSpot. If association types are left blank, it creates the default (most generic) association type between two object types. Note that the default association is available only for HubSpot main objects.

If you plan to use custom object associations, you must create a user-defined association definition and use it in association types. This action accepts a maximum of 2000 records and fails if more than 2000 records are provided.

## Input

| Input field | Description |
| --- | --- |
| From object | This is the object you're associating. Use the drop-down menu to choose **Select from list** or **Use custom value**. |
| To object | This is the object you're associating the record to. Use the drop-down menu to choose **Select from list** or **Use custom value**. |
| Input parameters source list | This field is optional. Input a list datapill. |
| From object ID | The ID of the record to associate. |
| To object ID | The ID of the record to associate to. |
| Association types | This allows you to select the type of association you plan to create. Use the drop-down menu to choose **Select from list** or **Enter custom value**. Leave this field blank to create the default (most generic) association. |

## Output

If the request is successful, Workato returns a list of records associated with the selected records. You can use these datapills in subsequent recipe steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/delete-associations-batch.md
description: >-
  The Delete associations batch action in the HubSpot connector deletes all
  associations for the record objects you specify, up to 100 records.
---

# HubSpot - Delete associations action (batch)

The **Delete associations** batch action deletes all associations for the record objects you specify. You can submit a maximum of 100 records. The action fails if more than 100 records are submitted.

## Input

| Input field | Description |
| --- | --- |
| From object | This is the object you're associating. Use the drop-down menu to choose **Select from list** or **Use custom value**. |
| To object | This is the object you're associating the record to. Use the drop-down menu to choose **Select from list** or **Use custom value**. |
| Input parameters source list | This field is optional. Input a list datapill. |
| From object ID | The ID of the record to associate. |
| To object ID | The ID of the record to associate to. |

## Output

This action doesn't return any output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/hubspot/actions/export-object-data-file.md
description: >-
  The Export object data (file) action in the HubSpot connector lets you bulk
  export object data and use the file in later recipe steps.
---

# HubSpot - Export object data action (file)

The **Export object data** action allows you to export data from HubSpot in bulk. You can use the downloaded file contents in subsequent recipe steps to upload the file into other applications.

## Input

| Input field | Description |
| --- | --- |
| Export type | Use the drop-down menu to select **VIEW** or **LIST** as the export type. |
| Export name | Provide a name for your export. |
| Language | Use the drop-down menu to choose **Select a language** (this option provides a list of languages for you to choose from) or **Enter a language** (this option allows you to manually enter the language you plan to use). |
| Object | Use the drop-down menu to choose **Select an object** or **Enter object ID**. You can select any standard HubSpot object, including contacts, companies, deals, and more. |

## Output

Workato returns a record representing each imported record. You can use these datapills in subsequent recipe steps.

---
