---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/action-transfer-data.md
description: >-
  Transfer data action allows you to transfer data from one user ID to another
  in the Google Workspace.
---

# Google Workspace - Transfer data action

The **Transfer data** action transfers data from one user ID to another in Google Workspace. You must select the **Object** type you plan to add before you can configure the action. The recipe editor generates additional fields based on your selection. You can use this action to transfer ownership from one user to another when off-boarding a user.

### Input

| Input field | Description |
| --- | --- |
| Old owner user ID | Enter the old owner user ID. |
| New owner user ID | Enter the new owner user ID. |
| Application data transfers source list | Select the source list for the transfer. Accepts list datapill as input. This list contains data transfer details of the applications associated with this transfer resource. |
| Application ID | Select the data transfer application. |
| Application transfer params source list | Select the parameters list for the transfer. Accepts list datapill as input. These parameters are used to select the data that gets transferred in context of this application. |
| Transfer parameter values | Select the parameter values to transfer. |
| Application transfer status | Select the application transfer status. |

### Output

The **Transfer data** action generates output fields relevant to the newly added group object.
