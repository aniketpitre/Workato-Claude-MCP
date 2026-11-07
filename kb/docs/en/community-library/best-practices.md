---
url: 'https://docs.workato.com/en/community-library/best-practices.md'
description: >-
  Learn best practices for installing, uploading, and sharing community library
  connectors and recipes safely and effectively in your workflows.
---

# Community library best practices

Follow these best practices to use and share community assets in your workflows effectively.

## Installing assets

We recommend using the following best practices when installing platform assets from the community:

- **Evaluate asset metrics**: Assess assets by viewing the metrics on the asset landing page, such as the total number of installations and critical builder statistics.
  
- **Evaluate asset's code or workflow logic**: Evaluate the quality of a connector's code before releasing it to your workspace. Releasing a connector allows anyone in your workspace to use it in recipes, so be sure to test its functionality and safety thoroughly. Similarly, make sure to evaluate the underlying workflow logic of community recipes before using them in your workspace.
  
- **Test the asset**: Test the asset before releasing it or using it widely in your workspace. You can test the functionality and security of community connectors through Workato's [Test code tab](/en/developing-connectors/sdk/guides/debugging#the-test-code-tab), located in **Tools > Connector SDK > Source code**. Similarly, we recommend customizing community recipes and thoroughly testing them before using them in your workspace.
  
- **Use Workato resources**: If you encounter errors in integrations that use assets downloaded from the community, contact [Workato support](https://support.workato.com/) for guidance. Our support team can assess the points of failure, as well as reach out to the asset developer for clarification.
  

## Uploading assets

We recommend using the following best practices when sharing assets with the community:

- **Scrub sensitive information from your source code**: You must remove hardcoded credentials, such as OAuth client IDs, secrets, or API keys, if you're listing an open-source connector. These values are exposed when users install and view your connector's code. Use input fields to collect sensitive data from users for all connector types rather than hardcoding values.
  
- **Customize your asset listing**: Use a clear logo, description, and tags to accurately convey your asset's purpose and functionality.
  
- **Prepare informational content**: Set users up for success by providing them with informational content about your asset. You can place links to documentation in the actions and triggers of your connector. Additionally, if you enabled **Prevent direct installation** when listing your connector, the landing page you link to should showcase the connector, highlight how users can reach out, and provide a clear path to your private sharing link.
  
- **Provide contact information**: Ensure your community profile includes a contact email or website so users can reach out with questions about your asset. You can update this information on the **Workspace admin** page.
  
- **Provide community recipes**: Upload recipes for your community connectors to help users get started.
  
- **Confirm your source code visibility setting**: Ensure you've set the source code to hidden before publishing if you're publishing a closed-source connector. This setting is locked after the connector is listed in the community.

---
