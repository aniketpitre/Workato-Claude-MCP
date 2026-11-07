---
url: 'https://docs.workato.com/en/connectors/facebook-ads.md'
description: >-
  The Facebook Lead Ads connector lets you trigger on new leads, list campaigns,
  and retrieve campaign and ad set insights for your ad workflows.
---

# Facebook Lead Ads

[Facebook Lead Ads](https://www.facebook.com/business/ads/lead-ads) is a targeted advertising tool that allows businesses to collect lead information directly through ads, using forms that auto-populate with a user's Facebook contact details. You can use Facebook Lead Ads to efficiently capture leads, enhance your marketing campaigns, and drive customer engagement.

> **FEATURE AVAILABILITY**
> 
> The Facebook Lead Ads connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The Facebook Lead Ads connector uses the [Facebook Marketing API v24.0](https://developers.facebook.com/docs/marketing-apis/).

## Connection setup

Complete the following steps to create a Facebook Lead Ads connection in Workato.

1. Enter a **Connection name** to label your Facebook Lead Ads account within Workato.
   
   ![Facebook Lead Ads connection](/assets/connection-setup.DyEbLy1p.png)_Label your connection_
   
2. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
3. Click **Connect** to open Facebook's login window.
   
4. Enter your credentials in the Facebook login window to authenticate your account.
   
   ![Facebook login](/assets/facebook-login.CqbZIODs.png)_Facebook login window_
   
5. Review the permissions that Workato requests to manage your Lead Ads.
   
   ![Facebook permissions](/assets/review-permissions.B1xv0g8X.png)_Review permissions_
   
6. Click **Continue** to approve the connection permissions and complete the setup.
   

## Troubleshooting

If you have connected your Facebook account, given the relevant pages access and still can't trigger the recipe despite new leads being added -- utilize [this tool](https://developers.facebook.com/tools/lead-ads-testing) to help with debugging the setup. You can select the relevant page and form and see if the Workato App has been successfully subscribed and even send a test webhook lead to check.

If the Workato application isn't subscribed correctly, the likely issue is that it needs be explicitly provided [CRM access](https://www.facebook.com/business/help/540596413257598?id=735435806665862) within Meta business manager.

We provide a step by step guide to the same as follows:

1. Set up a New leads trigger, start the recipe.
   
2. Sign in to [Meta Business Suite](https://business.facebook.com)
   
3. Select your business in the drop-down menu.
   
4. Go to **Settings > Integrations > Leads access**.
   
5. Go to the **CRMs** tab and click **Assign CRMs**. Once you have started the recipe, Workato's OAuth app should be listed in the select options.
   
   ![Assign Workato's App to CRM](/assets/assign-crm.Dgue09y5.png)_Assign CRM access to Workato's App_
   
6. Now the OAuth app should be listed in the [Facebook leads testing tool](https://developers.facebook.com/tools/lead-ads-testing), and the recipe should receive events when leads are created.
   
   ![Lead Ads testing tool](/assets/lead-ads-testing-tool.DWXo8s1M.png)_Verify the configuration in the lead ads testing tool_

---
