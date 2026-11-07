---
url: 'https://docs.workato.com/en/connectors/opa-webhook.md'
description: >-
  OPA Webhook is a webhook HTTP request forwarder. OPA Webhook runs on a Workato
  On‑Premise Agent (OPA). This connector lets internal services send webhook
  events to Workato.
---

# OPA Webhook

[OPA Webhook](https://www.workato.com/) is a webhook HTTP request forwarder. OPA Webhook runs on a Workato On‑Premise Agent (OPA). This connector lets internal services send webhook events to Workato.

Example OPA Webhook workflow:

1. Workato calls the connector trigger `webhook_subscribe` when a recipe starts.
2. The connector registers the recipe’s Workato webhook URL with the OPA extension for a specified routing key.
3. Your internal service sends HTTP requests to `http://<opa-host>:<listenPort>/<routing_key>`.
4. The OPA extension forwards the request body to all running recipes with that routing key.

## Install OPA Webhook from the community library

Complete the following steps to install the OPA Webhook connector from the [community library](https://www.workato.com/browse/connectors):

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

The OPA Webhook connector uses an external secrets manager for authentication.

Secure your data in the OPA Webhook connector by using an external secrets manager. Refer to [Secret management for connection credentials](/en/security/data-protection/secrets-management/secrets-management) for more information about using an external secrets manager.

### On-premise agent setup

Complete the following steps to set up OPA Webhook for external secrets manager authentication:

1. Install an on-prem agent and connect it to the workspace where you plan to use OPA webhooks. Refer to [On-prem agent](https://docs.workato.com/en/on-prem/agents) for detailed instructions.
   
2. Download the OPA Webhook extension ZIP file.
   
3. Extract the JAR file from the OPA Webhook extension ZIP file.
   
4. Save the JAR file in your OPA extension folder, such as `lib_ext/`.
   
5. Update your OPA `config.yml` to include the following:
   
   ```yml
   extensions:
     webhook:
       controllerClass: com.workato.extension.webhook.ExtensionController
       listenPort: 8081
       maxRetries: 3
       retryDelayMs: 2000
       connectionTimeout: 30000
       readTimeout: 30000
   ```
   

### Connect to OPA Webhook with external secrets manager authentication

Complete the following steps to connect to OPA Webhook in Workato:

1. Click **Create > Connection**.
   
2. Search for `OPA Webhook` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![OPA Webhook connection](/assets/opa-webhook-connection-setup.BxYqnbo_.png)_Set up an OPA Webhook connection._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select the **Connection type**. Options include `Cloud` or an on-prem group.
   
6. Enter a webhook extension **Profile**. This must match the profile name configured in your OPA `config.yml` file.
   
7. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/opa-webhook/new-webhook-event-trigger.md
description: The New webhook event trigger monitors OPA Webhook for new webhook requests.
---

# OPA Webhook - New webhook event trigger

The **New webhook event** trigger monitors OPA Webhook for new webhook requests.

## Input

| Input field | Description |
| --- | --- |
| Webhook routing key | Enter a routing key. All webhooks are routed to recipes associated with this key. |
| Custom payload schema | Enter fields to define the schema for the webhook payload. |

## Output

Output fields load dynamically based on the custom payload schema you define.

---
