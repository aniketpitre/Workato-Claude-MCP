---
url: 'https://docs.workato.com/en/oem/cx-options.md'
description: >-
  Compare Workato Embedded customer experience options, from managed services to
  self-service models, and choose the right fit.
---

# Customer experience options

Workato's customer experience (CX) options offer embedded partners a seamless and integrated experience that scales with your business needs, whether through a [managed service](#managed-services) or [self-service](#self-service) model.

## Managed services

Workato's managed services option provides a behind-the-scenes automation platform that empowers your service team to create and manage complex integrations seamlessly. This approach offers a hands-off experience for your customers, ensuring they benefit from automation without the need for direct involvement or understanding of the integration details.

This service enables tailored integrations that enhance your product's value and customer experience, aligning with specific business needs while minimizing complexity for your end users.

### Authenticate connections

To offer integrations as a managed service, securely collecting your customers’ connector credentials within their workspaces is critical before activating recipes. Workato supports the following methods for authenticating these connections:

- Embedded connection widget
  
- Embed Workato's [connection widget](/en/oem/workato-embedded-implementation#connection-widget) within your application, enabling your customers to seamlessly authenticate to their app connections from your application. We recommend using this method as it ensures a reliable connection process for your customers.
  
- Invite customers as collaborators with limited permissions
  
- Create [roles](/en/user-accounts-and-teams/role-based-access/#creating-custom-roles) with limited permissions in your Workato environment and invite your customers as collaborators, assigning them these roles. This method allows your customers to authenticate their connections securely while you control their access and actions.
  
- Collecting credentials offline
  
- Collect credentials from your customers and authenticate on their behalf. We do not recommend this method due to the risks associated with handling sensitive information offline.
  

![Connection widget](/assets/connection-widget.BeW06vHh.png)_Workato's embedded connection widget_

## Self-service

Workato's self-service options enable your customers to autonomously create their own automations. This approach allows your customers to take charge of their automation needs, while your team remains available to assist, support, and scale their efforts as necessary. Integrating your product with Workato encourages customer independence and offers customized automation solutions that directly meet their specific business requirements.

### Branded access

Workato's branded access option allows you to seamlessly integrate the automation experience under your company's brand. This approach lets your customers access and manage integrations within an environment that mirrors your brand identity.

![Branded access](/assets/white-label-updated.CHMCZ-fG.png)_Workato's branded access integration_

You can offer Workato's branded access option to your customers in two ways:

#### Invite customers as collaborators

Invite your customers to join your branded Workato environment as collaborators. They can register with a username and password, and then log in to Workato. This provides them with direct access tailored to their needs. You can grant a variety of [roles and permissions](/en/user-accounts-and-teams/role-based-access/#how-role-based-access-control-works), from basic access to more advanced controls, depending on their role and your discretion.

#### SSO with JWT Direct Linking

Securely redirect your customers from your application to Workato and authenticate them programmatically using [JWT direct linking](/en/oem/jwt-direct-linking). This streamlines access within a secure framework.

After setting up your authentication method, you can also enhance your branded access experience with Workato's [theme editor](/en/oem/branding). This tool enables you to customize the Workato platform's interface, ensuring it matches your brand’s visual identity and offers a consistent brand experience throughout the customer journey.

For more information on implementing Workato's branded access SSO option, refer to our [Branded access SSO implementation](/en/oem/branded-access-implementation) guide.

### Fully Embedded

Embed Workato fully within your product to offer your customers comprehensive access to all Workato features, such as the recipe editor and dashboards, directly in your app's interface.

![Fully Embedded](/assets/fully-embedded-updated.DbhcgboC.png)_Workato embedded in an `iframe` in Acme ERP_

Workato's Fully Embedded option allows your customers to build and manage integrations within your product. Setting up Fully Embedded involves embedding an `iframe` in your application's UI, delivering a deep integration that maintains a seamless user experience. This enables your customers to interact with a complete suite of Workato features without leaving your application, ensuring they stay engaged in your product environment while accessing Workato's automation tools.

For more information on implementing fully embedded, refer to our [fully embedded](/en/oem/workato-embedded#workato-fully-embedded) guide.

---
