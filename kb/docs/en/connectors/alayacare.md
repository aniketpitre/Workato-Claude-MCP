---
url: 'https://docs.workato.com/en/connectors/alayacare.md'
description: >-
  The AlayaCare connector lets you automate home and community care workflows by
  searching for and retrieving care records.
---

# AlayaCare

AlayaCare is a cloud platform that helps home and community-based care agencies manage client referrals, intake, scheduling, documentation, billing, and payroll. This connector supports client and schedule objects.

This connector lets you perform the following actions:

- Search and filter lists of clients or schedules
- Retrieve information for a specific client or schedule using a unique identifier
- Create and configure your own actions

## API version

The AlayaCare connector uses the [AlayaCare API](https://alayacare.github.io/external-integration-docs/external-api-guide.html).

## Prerequisites

To establish a connection to AlayaCare you must have the following:

- Public key
- Private key
- AlayaCare domain

### Obtain AlayaCare keys and domain

The AlayaCare connector uses basic authentication for your domain, with a public and private keys.

#### Public and private keys

AlayaCare provides your team with the required private and public keys directly by using a password manager, such as LastPass. Contact AlayaCare if you haven't received your keys.

#### Domain name

Complete the following steps to obtain your AlayaCare domain:

1. Replace `example` in the following base URL with your tenant name and environment: `https://example.alayacare.ca/ext/api/v2/clinical/`
   
   For example, `https://.uat.alayacare.ca/ext/api/v2/clinical/` or `https://staging.alayacare.ca/ext/api/v2/clinical/`.
   
2. If your updated base URL is `https://staging.alayacare.ca/ext/api/v2/clinical/`, your domain name is `staging.alayacare`.
   
3. Record your domain name to use when completing setup in Workato.
   

## How to connect to AlayaCare

You must complete the steps in each of the following sections to connect to AlayaCare:

### Download AlayaCare from the community

Complete the following steps to install the AlayaCare connector from the [community library](https://www.workato.com/browse/connectors):

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

Complete the following steps to establish a connection to AlayaCare in Workato:

1. Provide a **Connection name** that identifies which AlayaCare instance Workato is connected to.
   
   ![AlayaCare Connection](/assets/alayacare-connection-setup.N0tyob6D.png)_Create your connection_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Enter your AlayaCare **Public key**.
   
4. Enter your AlayaCare **Private key**.
   
5. Enter your **AlayaCare domain**. For example, if your instance URL is `https://homecare.alayacare.com`, your domain name is `homecare.alayacare.com`.
   
6. Click **Connect**.

---
