---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/retrieve-category-group-hierarchy.md
description: >-
  This action retrieves a data category group hierarchy from Salesforce using a
  source list.
---

# Salesforce - Retrieve data category group hierarchy action (batch)

This action retrieves a data category group hierarchy from Salesforce using a source list.

## Input

| Input fields | Description |
| --- | --- |
| Full names source list | Input a list datapill to use as the source. Refer to the [List management](/en/features/list-management) documentation for more information about list inputs. |
| Full name | Enter the full name of the data category group to retrieve. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

| Output fields | Description |
| --- | --- |
| Full name | The full name of the group. |
| Label | The display name of the group. |
| Active? | Indicates whether the group is active. |
| Data categories | An object containing information about the retrieved data category. For example: the `Name`, `label`, and an object containing `Child data categories`. |
| List size | The total number of category group records returned. |
| List index | The position of the current category group record in the list. |
