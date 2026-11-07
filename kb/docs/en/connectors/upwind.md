---
url: 'https://docs.workato.com/en/connectors/upwind.md'
description: Upwind is a cloud security platform that provides runtime-powered protection.
---

# Upwind

[Upwind](https://www.upwind.io/) is a cloud security platform that provides runtime-powered protection. This connector allows you to automate security workflows by integrating Upwind's threat detection, vulnerability management, and configuration compliance data with the rest of your organization's systems.

This connector has the following capabilities:

- Create tickets in a service management application when new threat events are detected in a cloud security platform
- Sync new and updated configuration compliance findings to a governance, risk, and compliance application for audit tracking
- Enrich incident records in a SIEM application with vulnerability finding and SBOM package details to accelerate security triage
- Register image build and deployment events from a CI/CD pipeline tool in a cloud security platform to enable runtime-to-code traceability
- Trigger automated notifications in a messaging application when high-severity configuration findings or threat events are identified

## Install Upwind from the community library

Complete the following steps to install the Upwind connector from the [community library](https://www.workato.com/browse/connectors):

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

The Upwind connector uses OAuth 2.0 authentication.

### Upwind setup

1. Sign in to your Upwind account.
   
2. Select your profile icon and click **Settings**.
   
3. Click **Generate credential**.
   
4. Select credential type you plan to use. Options are: `Cloud account`, `Sensor`, `third-party integration` or `API`.
   
5. Provide a **Name** for your credential, or use the auto-generated name.
   
6. Click **Generate > Save**. You must use these credentials to create a connection in Workato in later steps.
   

### Connect to Upwind using OAuth 2.0

Complete the following steps to connect to Upwind in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Upwind` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Upwind connection setup](/assets/upwind-connection-setup.DY5Tn7fL.png)_Upwind connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client ID** for your Upwind account.
   
6. Enter the **Organization ID** for your Upwind account.
   
7. Select the **Region** where your Upwind account is hosted.
   
8. Click **Connect**.

---
