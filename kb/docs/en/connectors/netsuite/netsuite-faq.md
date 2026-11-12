---
url: 'https://docs.workato.com/en/connectors/netsuite/netsuite-faq.md'
description: >-
  Answers to frequently asked questions about the NetSuite connector, including
  creating invoices from CSV files and missing custom search fields.
---

# NetSuite FAQ

Get answers to frequently asked questions (FAQs) about the NetSuite connector. Contact [Workato Support](https://support.workato.com/support/tickets) to report bugs or troubleshoot issues with this connector.

## How to create a NetSuite invoice from CSV file

View answer

To set up a workflow that takes in a CSV import to create NetSuite invoices, first configure your CSV file. You can set up your recipe to trigger off new files in [Google Drive](/en/connectors/google-drive/trigger-new-file).

Next, use [Workato CSV parser](/en/features/handling-csv-files#csv-by-workato) to parse the CSV lines. Lastly, you can use the [Create records](/en/connectors/netsuite/action-batch-create) action to create invoices from the lines datapill.

![Example recipe: Create invoice from CSV](/assets/faq-create-invoice-from-csv.BnNTei4y.png)_Example recipe: Create invoice from CSV_

## Missing fields from Search custom record type

View answer

The custom action **created** and **lastModified** fields are not available by default. To enable these fields for use as datapills, you must enable them on the NetSuite UI. Ensure that the following options are checked.

![Custom record type: Show created date and lastModified](/assets/faq-show-create-and-lastmodified-date.n-sotVCV.png)_Custom record type: Show created date and lastModified_

## OAuth authentication for NetSuite connector

View answer

The NetSuite connector and [HTTP](/en/developing-connectors/http-v2) only supports OAuth2. Workato does not support OAuth1.0.

## Error `invalid subsidiary reference netsuite`

View answer

In NetSuite, a subsidiary object may itself contain child subsidiaries. The permission sets for each subsidiary is unique and distinct. If the Workato connection does not have the necessary permissions, it will cause an **invalid subsidiary reference** error.

Using any CREATE, UPDATE, or UPSERT actions with a record that has a subsidiary inaccessible to the integration role results in an invalid subsidiary reference error. This causes the action to fail.

When using the SEARCH action, the action will not be able to retrieve any records. Although the action will be fail and your will not have any indicative errors, this is not the desired behavior.

To resolve this, ensure that the credentials provided have the necessary permissions to work with the subsidiary objects.

## Error `The restrictions on your role deny you access to this record`

View answer

If the NetSuite credentials do not have the appropriate permissions, the recipe cannot access cross-subsidiary records. To resolve this, update the permissions for the connection credentials and set **Allow Cross-Subsidiary Record Viewing** to True.

- Go to Setup> Users/Roles > Manage Roles
- Customize or Edit the Role
- Make sure that the Allow Cross-Subsidiary Record Viewing is checked
- Click Save

## Does NetSuite API support dynamic fields in saved search?

View answer

NetSuite API does not support custom fields from saved search. It is not possible to fetch formula fields with the NetSuite connector.

---
