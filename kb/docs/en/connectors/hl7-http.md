---
url: 'https://docs.workato.com/en/connectors/hl7-http.md'
description: >-
  HL7 HTTP, or Health Level Seven HTTP, is a set of international standards for
  the exchange, integration, sharing, and retrieval of electronic health
  information. This connector is the HTTP-based variant of the HL7 connector.
  This connector sends HL7 messages using HTTP.
---

# HL7 HTTP

[HL7 HTTP](https://www.hl7.org/), or Health Level Seven HTTP, is a set of international standards for the exchange, integration, sharing, and retrieval of electronic health information. This connector is the HTTP-based variant of the [HL7 connector](/en/connectors/hl7). This connector sends HL7 messages using HTTP.

## Install HL7 from the community library

Complete the following steps to install the HL7 HTTP connector from the [community library](https://www.workato.com/browse/connectors):

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

The HL7 HTTP connector uses HTTP authentication.

### HL7 HTTP setup

1. Download the [HL7 extension](https://workato-opa-extensions.s3.amazonaws.com/hl7-extensions/hl7-extension-latest.zip).
   
2. Extract the downloaded package to `$OPA/ext`, where `$OPA` refers to your OPA installation directory.
   
3. Configure where outbound HL7 HTTP traffic goes for the HL7 HTTP connection. The connector configuration takes precedence when set.
   

### Connect to HL7 in Workato using HTTP

Complete the following steps to connect to HL7 HTTP in Workato:

1. Click **Create > Connection**.
   
2. Search for and select **HL7 HTTP** on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![HL7 HTTP connection](/assets/hl7-http-connection-setup.D_8LHWRp.png)_Set up your HL7 HTTP connection._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select the [on-prem group](/en/on-prem/groups) where your HL7 extension is configured.
   
6. Use the **Processing mode** drop-down menu to select the HL7 processing ID you plan to use. Options include: `Debugging`, `Production`, and `Training`.
   
7. Provide your **Profile name**. The OPA profile must have a running HL7 listener to receive HL7 messages.
   
8. Enter the **Remote HL7 HTTP base URL** for send actions. Overrides `remoteUrl` in OPA `config.yml` if set. Leave blank to use OPA only.
   
9. Enter the **Send path** for HTTP POST. Overrides `sendPath` in OPA `config.yml` if set. Leave blank to use OPA only.
   
10. Enter custom HTTP **Connection headers** to send with every request.
    
11. Select **Apply connection headers to all actions** to include connection headers in every action request.
    
12. Click **Connect**.

---
