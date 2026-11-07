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
