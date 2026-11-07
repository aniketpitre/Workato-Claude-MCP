---
url: 'https://docs.workato.com/en/connectors/gainsight-nxt.md'
description: >-
  Connect Gainsight NXT to Workato to automate customer success workflows across
  your company and person records.
---

# Gainsight NXT

[Gainsight NXT](https://www.gainsight.com/) is a customer success platform that helps organizations manage their customer relationships, monitor customer health, and drive retention and growth. The `Gainsight NXT` connector enables you to search, retrieve, create, update, and upsert Company and Person records, and trigger recipes when records are created or updated.

## Prerequisites

You must provide an access key and your `Gainsight NXT` domain to establish a connection to `Gainsight NXT`.

### Obtain an access key from Gainsight NXT

The connector authenticates using an API access key generated from your `Gainsight NXT` tenant.

1. Contact your `Gainsight NXT` admin to obtain an access key for your `Gainsight NXT` tenant, or to generate a new access key.
   
2. Refer to the [Generate API Access Key](https://support.gainsight.com/SFDC_Edition/Connectors/04API_Integration/Generate_API_Access_Key) article in the `Gainsight NXT` documentation for more details.
   
3. Copy and securely store the access key for use in Workato.
   

## Connection setup

Establishing a connection to Gainsight NXT involves the following configuration:

- [Install the Gainsight NXT connector from the community library](#community-install)
- [Complete setup in Workato](#workato-setup)

### Install the Gainsight NXT connector from the community library

Complete the following steps to install the Gainsight NXT connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### Complete setup in Workato

Complete the following steps to establish a connection to Gainsight NXT.

1. Click **Create > Connection** or press C twice.
   
2. Search for `Gainsight NXT` and select it as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your access key in the **Access key** field.
   
6. Enter your application domain in the **Domain** field, for example, `demoworks.gainsightcloud.com`.
   
7. Click **Connect**.

---
