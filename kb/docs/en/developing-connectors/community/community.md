---
url: 'https://docs.workato.com/en/developing-connectors/community/community.md'
description: >-
  Install community connectors built with the Workato connector SDK to get a
  head-start on integrations without building from scratch.
---

# Community connectors

Community connectors are custom connectors built by members of the Workato community and shared on the [community library](/en/community-library). These connectors are designed to help you get a head-start on your integrations by providing pre-built solutions that can be customized to fit your specific requirements. This enables you to start building recipes immediately rather than building a connector from scratch.

The Workato community can build and contribute custom connectors using [Workato's connector SDK](/en/developing-connectors/sdk), and there is no limit to the number of connectors you can install for your workspace.

> **PARTNER CONNECTORS**
> 
> Are you interested in building a connector to your own application? Contact our partnerships team today to join our technology partner program. Partners receive a dedicated developer account as well as the tools and training to get your connector up and running. [Learn more about building with Workato.](/en/developing-connectors/community/community-listing)

> **COMMUNITY ASSETS ARE INTENDED AS EXAMPLES ONLY**
> 
> Platform Assets created and marked public in the community library are intended to serve as a reusable set of templates, best practices and guidelines for different types of solutions. You can learn from, modify, customize and enhance it to meet your specific requirements and business needs. It enables you to expedite the implementation and rollout of integration and orchestration solutions and projects across the organization.

## How to install community connectors

You can install customer connectors uploaded to the community library.

> **REQUIRED PERMISSIONS**
> 
> Installing connectors from the community library requires [full access to the Connector SDK](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#connector-sdk). If you don't have the required permissions, contact your workspace admin to help install the connector.

> **FEATURE AVAILABILITY**
> 
> The Community library isn't accessible to workspaces in the China data center.
> 
> Customers using the China data center must build custom solutions or work with the Professional Services team to develop recipe templates, custom connectors, and best practices. [Recipe lifecycle management (RLCM)](/en/recipe-development-lifecycle#recipe-lifecycle-management) features are supported for the China data center. This means that users can deploy assets to higher environments and import or export `.zip` files to their workspaces. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

Complete the following steps to install the connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Community recipes for community connectors

Community recipes, created by the authors of the corresponding community connectors, serve as guides to help you understand how to use the connector and demonstrate common use cases.

When attempting to clone a community recipe that uses a connector you haven't installed, Workato prompts you to install the community connector before using the recipe.

## Best practices

We recommend using the following best practices when installing platform assets from the community:

- **Evaluate asset metrics**: Assess assets by viewing the metrics on the asset landing page, such as the total number of installations and critical builder statistics.
  
- **Evaluate asset's code or workflow logic**: Evaluate the quality of a connector's code before releasing it to your workspace. Releasing a connector allows anyone in your workspace to use it in recipes, so be sure to test its functionality and safety thoroughly. Similarly, make sure to evaluate the underlying workflow logic of community recipes before using them in your workspace.
  
- **Test the asset**: Test the asset before releasing it or using it widely in your workspace. You can test the functionality and security of community connectors through Workato's [Test code tab](/en/developing-connectors/sdk/guides/debugging#the-test-code-tab), located in **Tools > Connector SDK > Source code**. Similarly, we recommend customizing community recipes and thoroughly testing them before using them in your workspace.
  
- **Use Workato resources**: If you encounter errors in integrations that use assets downloaded from the community, contact [Workato support](https://support.workato.com/) for guidance. Our support team can assess the points of failure, as well as reach out to the asset developer for clarification.
  

## Community connector FAQs

Get answers to frequently asked questions (FAQs) about Community connectors.

### Do I receive updates when the community connector is updated by the connector developer?

View answer

Connectors installed from the community library retain a relationship with their parent connector, which is the connector listed in the community. When the connector author publishes a new version of this connector, you will receive a notification to update your connector. Updating your connector to the latest version doesn't change the version that is released to your workspace. This allows you to test and ensure that the new connector version is stable and suitable for your recipes.

### How do community connectors work with other features in Workato?

View answer

Using connectors from the community is highly complementary to other existing features in Workato.

- **Recipe lifecycle management**: The [recipe lifecycle management (RLCM) feature](/en/recipe-development-lifecycle) enables you to install and test community connectors with recipes in your development workspaces. When you are ready to deploy to production, these connectors are exported along with your recipes. This ensures a stable and seamless integration experience even as you use and test connectors from the community.
  
- **Connector SDK**: [Workato's robust connector SDK](/en/developing-connectors/sdk) gives you the tools to extend these community connectors by adding new triggers, actions, or changing the way you authenticate. This allows you to freely customize your connector to suit your requirements. Additionally, our connector SDK works with various other Workato features such as [on-prem groups](/en/on-prem) to access applications behind firewalls or our [API platform](/en/api-management) to turn your connector into a service API endpoint for your team or customers.
  
- **Governance**: Governance is a key feature of Workato that enables teams to work together securely without compromising company data. Workato imposes restrictions on who can install connectors from the community to ensure that only users with [full Connector SDK privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#connector-sdk) can install connectors from the community library. This ensures that teams have proper processes in place to assess the suitability of connectors installed in their workspace.

---
