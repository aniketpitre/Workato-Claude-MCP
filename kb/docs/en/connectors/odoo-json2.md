---
url: 'https://docs.workato.com/en/connectors/odoo-json2.md'
description: >-
  Connect Workato to Odoo's JSON-2 API to create, update, search, and sync
  records across any Odoo object, run object functions, and complete guided
  wizards.
---

# Odoo (JSON-2)

[Odoo](https://www.odoo.com/) provides a comprehensive suite of business applications that enables businesses to manage and automate key processes across departments such as sales, CRM, inventory, and accounting. You can use this connector to interact with Odoo (JSON-2) modules, enabling efficient data management and automation.

The Odoo (JSON-2) connector uses the JSON-2 API and builds input and output schemas dynamically. The connector retrieves fields directly from your Odoo (JSON-2) environment when you select an object. Use the Odoo (JSON-2) connector to create, update, and retrieve records for any object, search records by custom criteria, run object functions and guided wizards, retrieve quotations by validity date, and trigger recipes when an object is created or updated.

## Prerequisites

You must have the following prerequisites to use the Odoo (JSON-2) connector:

- An Odoo v19.0 or later environment. The Odoo (JSON-2) connector uses the [JSON-2 API](https://www.odoo.com/documentation/19.0/developer/reference/external_api.html), introduced in Odoo v19.0. Earlier Odoo versions, which rely on the XML-RPC or JSON-RPC APIs, aren't supported.

## Install Odoo (JSON-2) from the community library

Complete the following steps to install the Odoo (JSON-2) connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The Odoo (JSON-2) connector uses Bearer token authentication.

### Odoo setup

Complete the following steps to create an API key to connect to Odoo (JSON-2) in Workato:

1. Sign in to your [Odoo](https://www.odoo.com/) account.
   
2. Click your profile icon.
   
3. Go to **My Preferences**.
   
4. Click **Account Security**.
   
5. Click **New API Key** and follow the prompts to generate a key.
   
6. Copy and securely store the API key to use in Workato.
   

### Complete setup in Workato

Complete the following steps to establish a connection to Odoo (JSON-2).

1. Click **Create > Connection** or press C twice.
   
2. Search for `Odoo (JSON-2)` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Odoo connection setup dialog with the connection name, location, environment URL, API key, and database fields.](/assets/odoo-connection-setup.BDv2TLck.png)_Create an Odoo connection in Workato._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Odoo environment URL in the **Environment URL** field. For example, if your environment is `https://workato.odoo.com`, enter `workato`.
   
6. Enter your personal API key in the **API key** field.
   
7. Enter your database name in the **Database** field. This is only required when your Odoo server hosts multiple databases.
   
8. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/odoo-json2/new-updated-object-trigger.md
description: >-
  Triggers when a record of the selected Odoo object is created or updated in
  Odoo.
---

# Odoo (JSON-2) - New/updated object trigger

The **New/updated object** trigger runs when a record of the selected object is created or updated in Odoo (JSON-2). Each poll returns up to 100 new or updated records, ordered by their last-modified date.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the object you plan to monitor, such as **Contact** or **Sales order**. The list of objects is populated dynamically from your environment. |
| Trigger poll interval | Select the frequency at which trigger checks for new events, from the drop-down menu. Defaults to minutes if left blank. The minimum value allowed is 5 minutes. Refer to [Polling intervals](/en/recipes/polling-intervals) for more information. |

## Output

Output fields are dynamically generated based on the object you select. Refer to the [Odoo](https://www.odoo.com/documentation/19.0/developer/reference/external_api.html) documentation for a complete list of output fields.

---
