---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/new-updated-record.md
description: >-
  This trigger checks Salesforce for newly created or updated objects at an
  interval you specify.
---

# Salesforce - New/updated record trigger

This trigger checks Salesforce for newly created or updated objects at an interval you specify.

## Input

| Input fields | Description |
| --- | --- |
| Trigger poll interval | Optional. Specify how frequently to check Salesforce for new or updated records. Defaults to every five minutes. |
| Object | Select the object type to monitor. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |

![New/updated record trigger](/assets/trigger-new-updated-lead.BVGS-Oqy.png)_Configured **New/updated record** fields_

## Output

The output of this action varies based on your selected **Object** and **Fields to retrieve**. Refer to Salesforce's [Overview of Salesforce Objects and Fields](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_concepts.htm) guide for more information on available objects and fields.
