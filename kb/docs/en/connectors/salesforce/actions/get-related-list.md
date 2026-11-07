---
url: 'https://docs.workato.com/en/connectors/salesforce/actions/get-related-list.md'
description: >-
  This action retrieves a related list of a Salesforce record in batches using a
  parent record's ID.
---

# Salesforce - Get related list by parent record ID action (batch)

This action retrieves a related list of a Salesforce record in batches using a parent record's ID. In Salesforce, a related list is usually a child object that has a lookup or master-detail relationship to a parent record. Refer to the [Salesforce object relationships](/en/connectors/salesforce/related-objects) guide for more information about object relationships.

## Input

| Input fields | Description |
| --- | --- |
| Related list object | Select the type of object to retrieve. |
| Related objects | Select related objects. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

Additional fields load dynamically based on the selected **Related list object**.

## Output

The output of this action varies based on your selected **Related list object** and **Fields to retrieve**. Refer to Salesforce's [Overview of Salesforce Objects and Fields](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_concepts.htm) guide for more information on available objects and fields.

---
