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
