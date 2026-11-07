---
url: 'https://docs.workato.com/en/connectors/email-custom-opa.md'
description: >-
  Connect Email (Custom) OPA to Workato to send and receive email over SMTP,
  IMAP, and POP3 through an on-prem agent extension.
---

# Email (Custom) OPA

[Email (Custom) OPA](https://app.workato.com/custom_adapters/1361680/details?community=true) is a utility connector that sends and receives email over SMTP, IMAP, and POP3 through a Java extension on your [on-prem agent](/en/on-prem/agents). It provides the same actions and triggers as the [Email (Custom)](/en/connectors/email-custom) connector, for deployments that need to route email traffic through an on-prem agent instead of connecting directly.

## Install Email (Custom) OPA from the community library

Complete the following steps to install the Email (Custom) OPA connector from the [community library](https://www.workato.com/browse/connectors):

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

Install the extension on your on-prem agent and have your email account's username, password, and SMTP, IMAP, or POP3 server details ready before you connect Email (Custom) OPA in Workato.

### Install the Email (Custom) OPA extension

Complete the following steps to install the extension on your on-prem agent:

1. Install an [on-prem agent](/en/on-prem/agents) and connect it to your Workato workspace.
   
2. Download the [Email (Custom) OPA extension](https://workato-opa-extensions.s3.us-east-1.amazonaws.com/email-opa-extensions/email_opa-extension-latest.zip), extract the JAR file, and place it in your on-prem agent's extension folder, for example `ext/`.
   
3. Add the extension's classpath and profile name to your on-prem agent's `conf/config.yml` file:
   
   ```yaml
   server:
     classpath: /path/to/workato-opa/ext
   extensions:
     email_custom:
       controllerClass: com.workato.extension.email.ExtensionController
   ```
   
   `email_custom` is the profile name. Use the same value in the connection's **OPA profile** field.
   
4. Restart the on-prem agent to apply the extension and configuration changes.
   

### Connect to Email (Custom) OPA

Complete the following steps to set up an Email (Custom) OPA connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Email (Custom) OPA` as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Email (Custom) OPA connection setup](/assets/email-custom-opa-connection-setup.BRWDNOJz.png)_Email (Custom) OPA connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select the on-prem group running your extension. This connector requires an on-prem agent and doesn't support a direct cloud connection. Refer to [On-prem group](/en/on-prem/groups) for more information.
   
6. Enter the **OPA profile** name you configured in `config.yml`, for example `email_custom`.
   
7. Enter your email account's **Username** and **Password**.
   
8. Enter the **SMTP Server** and **SMTP Port**, for example `smtp.example.com` and `587`.
   
9. Use the **STARTTLS for SMTP?** drop-down menu to select whether your mail server uses STARTTLS for SMTP.
   
10. Optional. Use the **Receiving protocol** drop-down menu to select **IMAP** or **POP3**, then enter the matching server, port, and SSL/TLS fields:
    
    - For IMAP, enter the **IMAP Server** and **IMAP Port**, and use the **Enable SSL/TLS for IMAP?** drop-down menu to select whether your server uses SSL/TLS.
    - For POP3, enter the **POP3 Server** and **POP3 Port**, and use the **Enable SSL/TLS for POP3?** drop-down menu to select whether your server uses SSL/TLS.
11. Optional. Expand **Advanced settings** and enter a **Max connections per mailbox** value between `4` and `20`. Defaults to `10` if left blank.
    
12. Click **Connect**.

---
