---
url: 'https://docs.workato.com/en/connectors/zscaler-digital-experience.md'
description: >-
  Zscaler Digital Experience (ZDX) is a cloud-native service that monitors
  application, device, and network performance.
---

# Zscaler Digital Experience (ZDX)

[Zscaler Digital Experience (ZDX)](https://www.zscaler.com/products-and-solutions/zscaler-digital-experience-zdx) is a cloud-native service that monitors application, device, and network performance. Use the Zscaler Digital Experience (ZDX) connector to retrieve and search application, user, device, software inventory, department, and location records.

## Install Zscaler Digital Experience (ZDX) from the community library

Complete the following steps to install the Zscaler Digital Experience (ZDX) connector from the [community library](https://www.workato.com/browse/connectors):

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

The Zscaler Digital Experience (ZDX) connector supports the following authentication types:

- [OneAPI (Zidentity client credentials)](#oneapi-authentication)
- [Legacy ZDX API key](#legacy-authentication)

### OneAPI authentication

Use OneAPI if your Zscaler tenant issues Zidentity client credentials.

#### Obtain OneAPI credentials

Complete the following steps to obtain OneAPI credentials in Zscaler Digital Experience (ZDX):

1. Sign in to the [Zidentity Admin Portal](https://console.zscaler.com).
   
2. Go to **Administration > API Configuration > OneAPI > API Clients**.
   
3. Click **Add API client**.
   
4. Enter a **Name**, **Description**, **Status**, and **ZDX API resource/role scope** to configure the API client.
   
5. Copy the **Client ID** and **Client Secret**.
   
6. Copy your Zidentity vanity domain. The vanity domain is the subdomain of your login URL. For example, if your login URL is `https://acme.zslogin.net`, your vanity domain is `acme`.
   

#### Connect to Zscaler Digital Experience using OneAPI

Complete the following steps to set up a OneAPI connection to Zscaler Digital Experience (ZDX) in Workato:

1. Click **Create > Connection**.
   
2. Search for and select Zscaler Digital Experience (ZDX) as your connection.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Set up a ZDX connection.](/assets/zdx-connection-setup.DPZ4NcaO.png)_Set up a ZDX connection._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OneAPI (Zidentity client credentials)**.
   
6. Enter your **Client ID** and **Client secret**.
   
7. Enter your **Vanity domain**.
   
8. Optionally, enter your **Zidentity cloud** if your tenant uses a non-production Zidentity environment, such as `beta`, or a FedRAMP cloud (`gov` or `govus`). Leave this field blank for production.
   
9. Click **Connect**.
   

### Legacy ZDX API key authentication

Use legacy API key authentication if your tenant has an API Key ID and Secret pair generated from the ZDX Admin Portal.

#### Obtain a legacy API key

Complete the following steps to obtain a legacy API key:

1. Sign in to the [Zidentity Admin Portal](https://console.zscaler.com).
   
2. Go to **Administration > Authentication > API Keys** and generate an API key pair.
   
3. Click **Create new API key**.
   
4. Enter a **Name** and select a **Role** to configure the API key.
   
5. Click **Create key**.
   
6. Copy the **Key ID** and **Key Secret**. The key secret is shown only once. [Learn more](https://help.zscaler.com/zdx/about-api-keys).
   

#### Connect to Zscaler Digital Experience using a legacy API key

Complete the following steps to set up a legacy API key connection to Zscaler Digital Experience (ZDX) in Workato:

1. Click **Create > Connection**.
   
2. Search for and select Zscaler Digital Experience (ZDX) as your connection.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Set up a ZDX connection.](/assets/zdx-connection-setup.DPZ4NcaO.png)_Set up a ZDX connection._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Legacy ZDX API key**.
   
6. Enter your **API key ID** and **API key secret**.
   
7. Optionally, enter your **ZDX cloud** name if your tenant is on a different cloud than the default `zdxcloud`.
   
8. Optionally, enter your tenant's **API version**. Defaults to `v1`.
   
9. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/zscaler-digital-experience/get-record-action.md
description: >-
  The Get record action retrieves a single application, user, or device from
  Zscaler Digital Experience (ZDX) by its unique ZDX ID.
---

# Zscaler Digital Experience (ZDX) - Get record action

The **Get record** action retrieves a single application, user, or device from Zscaler Digital Experience (ZDX) by its unique ZDX ID.

## Input

Input fields dynamically generate based on the object you select. The following input field is common to all objects.

| Input field | Description |
| --- | --- |
| Object | Select the object type to retrieve. Options include `Application`, `User`, and `Device`. |

## Output

Output fields dynamically generate based on the object you select.

---

---
url: >-
  https://docs.workato.com/en/connectors/zscaler-digital-experience/search-records-action.md
description: >-
  The Search records action searches Zscaler Digital Experience (ZDX) for
  records that match the filters you specify.
---

# Zscaler Digital Experience (ZDX) - Search records action

The **Search records** action searches Zscaler Digital Experience (ZDX) for records that match the filters you specify. Results use cursor pagination.

## Input

Input fields dynamically generate based on the object you select. The following input field is common to all objects.

| Input field | Description |
| --- | --- |
| Object | Select the object type to search. Options include `Applications`, `Users`, `Devices`, `Software`, `Departments`, and `Locations`. |

## Output

Output fields dynamically generate based on the object you select.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/community/community-listing.md
description: >-
  Contribute your custom connector to the Workato community library to share
  open-source or closed-source connectors with users.
---

# Contributing your connector to Workato

Join thousands of customers and partners on the Workato platform who use our robust [connector SDK](/en/developing-connectors/sdk) by sharing your connectors with the community. We've created the Workato community as a way for all our users to come together and solve the problem of integrations together, and also allowing ISV partners to get their applications discovered by Workato's ecosystem of engaged IT administrators and automation builders.

There is one supported way to publish your connector to Workato:

- [Publishing your connector to the community library](#publishing-your-connector-on-the-community)
  - This approach allows you to share either open-source or closed-source connectors. Closed-source connectors let you hide your source code while still distributing it privately or publishing it to the Workato Community.

> **TIP**
> 
> If you're an app developer looking to build a connector but don't have access to Workato, join us as a Workato technology partner today. Workato's low code platform can make integrations a breeze for your customers, thereby driving engagement and reducing churn. As a technology partner, you'll get priority access to support and training to build on the Workato platform so you can get your connector up and running quickly. [Sign up here today](https://resources.workato.com/application-partner-inquiry/)

## The community library

Workato's [community library](/en/community-library) allows you to share assets, such as recipes and community connectors, with the Workato community.

### Benefits

- Gain exposure on the Workato platform as an experienced Workato systems integrator by listing connectors you have built. Our active community of integrators are on the lookout for consultants with in-depth knowledge of specific apps and integrations to help them with them. You can share your connectors and also direct interested users to your website to learn more about your app or services!
- List a connector to your own app on Workato and allow your customers a way to easily implement integrations from your app to the thousands of other applications on Workato. Drive engagement and reduce churn for your app when your customers can integrate it with their tech stack easily using Workato.

### Upload your connector to the community library

You can upload custom connectors to the community library.

> **REQUIRED PERMISSIONS**
> 
> Uploading connectors to the community library requires [full access to the Connector SDK](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#connector-sdk). If you don't have the required permissions, contact your workspace admin to help you upload the connector.

Complete the following steps to share a connector to the community library:

1. Go to **Tools > Connector SDK**.
   
2. Select the connector you plan to share.
   
   ![Click the connector](/assets/select-connector.D5e_JOdb.png)_Click the connector you plan to upload_
   
3. Go to the **Share** tab, then click **Share version**.
   
   ![Click Share version](/assets/share-connector.DGSlq1R0.png)_Click **Share version**_
   
4. Optional. Click the **Make source code hidden** button if you plan to publish a closed-source connector. This ensures your connector code isn't visible or editable by others. You can't change this setting after publishing unless you unpublish the connector.
   
   ![Choose to hide your source code](/assets/change-source-code-hidden.BY45Q0of.png)_Choose to hide your source code_
   
5. Click **Edit** in the connector description and ensure the description includes a clear way for users to contact support, such as a support email, documentation link, or help center. Submissions without support contact information may be rejected during review.
   
   ![Edit connector description](/assets/edit-connector-description.BeXXOJO_.png)_Edit connector description_
   
6. Click **Publish connector** to open the **List on community library** dialog.
   
   ![Click Publish connector](/assets/publish-connector.DwV2kuQB.png)_Click **Publish connector**_
   
7. Enter the **App** name. This field is case-sensitive.
   
   ![The Add details section](/assets/add-details.mficMB8r.png)_The **Add details** section_
   
8. Select any relevant tags in the **Category tags** drop-down menu.
   
9. Enter up to three **Search keywords**, separated by commas.
   
10. Optional. Click the **Prevent direct installation** toggle if you plan to redirect visitors to a landing page to request access.
    
    The following occurs when this option is enabled:
    
    - End users can't install the connector directly from the community listing.
    - Users can install the connector only through your private sharing link. Go to the **Sharing privately using a link** section of your connector's **Share** tab to obtain the link. Refer to [Share a connector with a link](/en/developing-connectors/sdk/quickstart/sharing#closed-source-code) to learn how to grant access to users.
    - You must provide a **Landing Page URL** and a clear path.
    
    Any workspace can install the connector directly from the community listing if you don't enable this toggle. Closed-source connectors hide the source code but don't restrict installation.
    
11. Provide a **Landing Page URL** if you enabled **Prevent direct installation**. The page you link to should showcase the connector and provide a clear path on how to obtain the private sharing link of the connector.
    
12. Read the Workato developer agreement and click the checkbox to accept the terms and conditions.
    
    ![Read the Workato developer agreement](/assets/developer-agreement.E84uhr_m.png)_Read the Workato developer agreement_
    
13. Click **List connector** to submit your connector for review.
    
14. Workato notifies you through your community profile's email when your connector has been reviewed.
    
    ![Monitor your connector's status](/assets/connector-approval.B9nNC6ka.png)_Monitor your connector's status_
    

### Creating community recipes for your connector

Community recipes allow you to showcase the functionality of your connector through recipes that anyone can find and install for use immediately. They drive usage and improve how fast people understand how to use your connector.

When designing community recipes for your connector, be sure to keep the recipe simple and understandable - these are templates that users can extend further, rather than full fledged production recipes. When users choose to install your community recipes, we will prompt them to install your community connector as part of the process.

To publish a community recipe utilizing community connectors, you will need to ensure that all custom connectors in the recipe are published to the community by you and that the recipe has at least 1 successful job. To share a recipe to the community, go to that recipe's page => settings => sharing.

![sharing a recipe](/assets/recipe-sharing.BBbHVBAP.png)

After sharing community recipes, users will be able to find your recipes when browsing either community recipes or community connectors.

### Best practices - Listing a community connector

We recommend using the following best practices when sharing assets with the community:

- **Scrub sensitive information from your source code**: You must remove hardcoded credentials, such as OAuth client IDs, secrets, or API keys, if you're listing an open-source connector. These values are exposed when users install and view your connector's code. Use input fields to collect sensitive data from users for all connector types rather than hardcoding values.
  
- **Customize your asset listing**: Use a clear logo, description, and tags to accurately convey your asset's purpose and functionality.
  
- **Prepare informational content**: Set users up for success by providing them with informational content about your asset. You can place links to documentation in the actions and triggers of your connector. Additionally, if you enabled **Prevent direct installation** when listing your connector, the landing page you link to should showcase the connector, highlight how users can reach out, and provide a clear path to your private sharing link.
  
- **Provide contact information**: Ensure your community profile includes a contact email or website so users can reach out with questions about your asset. You can update this information on the **Workspace admin** page.
  
- **Provide community recipes**: Upload recipes for your community connectors to help users get started.
  
- **Confirm your source code visibility setting**: Ensure you've set the source code to hidden before publishing if you're publishing a closed-source connector. This setting is locked after the connector is listed in the community.

---
