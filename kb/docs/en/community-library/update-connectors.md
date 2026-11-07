---
url: 'https://docs.workato.com/en/community-library/update-connectors.md'
description: >-
  Update a connector installed from the community library, either by applying
  the update banner or copying the latest source code into the connector.
---

# Update a community connector

There are two ways to update a connector installed from the community library:

- If an update banner appears in the Connector SDK, [use it to apply the update directly](#apply-update-from-banner).
- If no banner appears, [copy the latest source code from the community library into your existing connector](#copy-the-latest-code-from-the-community-library).

> **REQUIRED PERMISSIONS**
> 
> Updating community connectors requires [full access to the Connector SDK](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#connector-sdk). If you don’t have the required permissions, contact your workspace admin.

## Apply update from banner

When a new version is available, a banner appears on the connector in the Connector SDK. Complete the following steps to apply the update from the banner:

1. Go to **Tools > Connector SDK**.
   
2. Select a connector that displays the update banner.
   
   ![Update connector](/assets/update-connector.PrsZySvw.png)_Update connector_
   
3. Click **Update connector**.
   
4. Review and test the updated code.
   
5. Click **Release latest version**.
   

## Copy the latest code from the community library

If the banner doesn't appear, complete the following steps to update the connector by copying the latest source code:

1. Go to **Community library > Custom connectors** and select the connector you plan to update.
   
2. Select the **Source code** tab and copy the connector's source code.
   
3. Go to **Tools > Connector SDK** and select your original connector.
   
4. Paste the updated connector code into the **Source code** tab.
   
5. Save the changes to your connector.
   
6. Review and test the updated code.
   
7. Click **Release latest version**.

---
