---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/action-mobile-device.md
description: >-
  The Mobile device action performs certain action on the mobile device resource
  enlisted in the Google Workspace.
---

# Google Workspace - Mobile device action

The **Mobile device** action performs certain action on the mobile device resource enlisted in Google Workspace. You must select the **Object** type you plan to add before you can configure the action. The recipe editor generates additional fields based on your selection. Refer to the [Google Workspace Directory API](https://developers.google.com/admin-sdk/directory/v1/guides/manage-mobile-devices) for more information about the configuration.

### Input

| Input field | Description |
| --- | --- |
| Resource ID | Enter the mobile device Google Workspace ID. |
| Action | Select the action you plan to perform on the device. |

### Output

| Output field | Description |
| --- | --- |
| Success | A boolean (`true` or `false`) value indicating whether the action was successful or not. |
| Error message | Displays an error message if the action was not successful. |
