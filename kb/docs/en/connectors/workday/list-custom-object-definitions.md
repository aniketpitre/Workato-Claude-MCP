---
url: >-
  https://docs.workato.com/en/connectors/workday/list-custom-object-definitions.md
description: >-
  The List custom object definitions action in the Workday connector lets you
  retrieve the custom object definitions available to your security profile.
---

# Workday - List custom object definitions action

This action lists all available custom object definitions in Workday. The list retrieved will be subject to the security profile assigned to the credentials used when setting up the connection.

## Inputs

![List custom object definitions action](/assets/list-custom-object-definitions.C8NYfDbS.png)_List custom object definitions action_

| Input field | Description |
| --- | --- |
| Count | Sets the count of the objects to be retrieved in a single response, up to 100. If left blank, defaults to 20. |
| Page | Sets the page offset of the response. If left blank, defaults to 1. |

## Outputs

The outputs of this action are the total count of existing records and a paginated list of custom object definitions.
