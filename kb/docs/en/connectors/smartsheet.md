---
url: 'https://docs.workato.com/en/connectors/smartsheet.md'
description: >-
  The Smartsheet connector lets you automate work management: create, update,
  search, and get rows, and trigger recipes on new or updated rows.
---

# Smartsheet

[Smartsheet](https://www.smartsheet.com) enables you to collaborate and manage workflows effectively. You can plan, capture, manage, automate, and report on work across your organizations.

## API version

Smartsheet's connector uses Smartsheet's API 2.0 for integration. For more information, refer to [Smartsheet's API documentation](https://smartsheet.redoc.ly/).

## Connection setup

Follow these steps to set up a Smartsheet connection in Workato:

1. Enter a unique **Connection name** to identify your Smartsheet account within Workato.
   
   ![Smartsheet connection](/assets/smartsheet-connection-setup.SK4twxT2.png)_Name your connection_
   
2. Click **Advanced settings** to show or hide additional options depending on your requirements.
   
3. Select the necessary **Requested permissions (OAuth scopes)** for the connection. If you leave this field blank, the connection defaults to the minimum required permissions, which are `READ_SHEETS`, `WRITE_SHEETS`, and `ADMIN_WEBHOOKS`.
   
4. Review all information you entered to ensure it is correct, including the connection name and selected permissions.
   
5. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
6. Click **Connect** to authorize a connection between Workato and your Smartsheet account. This action opens a Smartsheet login window to complete the authorization.
   
   ![Smartsheet connection](/assets/smartsheet-authorize.D3U4mjNY.png)_Authorize your connection_

---
