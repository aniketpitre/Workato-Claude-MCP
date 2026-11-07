---
url: 'https://docs.workato.com/en/connectors/linkedin.md'
description: >-
  The LinkedIn connector enables you to automate B2B marketing workflows,
  syncing campaign performance and leads from LinkedIn Campaign Manager to your
  CRM.
---

# LinkedIn

[Video](https://www.youtube.com/embed/DLhhwVWXs7w?rel=0&rel=0)

[LinkedIn](https://www.linkedin.com/) is a social networking site built for professional networking and businesses. LinkedIn allows business professionals to keep up to date in their professional circles. Marketers also use LinkedIn to run a variety of different ads to garner new leads and build awareness about the B2B products that they sell.

The LinkedIn connector allows you to automate your marketing processes, ensuring campaign performance and leads flow seamlessly from LinkedIn Campaign Manager to your marketing automation platform or CRM. This helps you maximize the value of your marketing spend.

> **FEATURE AVAILABILITY**
> 
> The LinkedIn connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The LinkedIn connector uses the [202607 version](https://learn.microsoft.com/en-us/linkedin/marketing/versioning?view=li-lms-2026-07) of the LinkedIn REST API.

### Overriding API version in custom actions

You can use a different API version by creating a custom action and adding the `Linkedin-Version` request header to override the default API version. Refer to LinkedIn's [version header](https://learn.microsoft.com/en-us/linkedin/marketing/versioning?view=li-lms-2026-07#version-headers) documentation to learn more.

## How to connect to LinkedIn on Workato

The LinkedIn connector uses OAuth 2.0 to connect to LinkedIn. To fully utilize all triggers and actions on the LinkedIn connector, you must to be an admin in both your company's LinkedIn page, as well as an account manager in your LinkedIn Advertising account.

Complete the following steps to establish a LinkedIn connection in Workato:

> **LINKEDIN REFRESH TOKEN LIMITS**
> 
> When using the LinkedIn connector, be aware that LinkedIn limits the number of refresh tokens per account, which can lead to disconnections. This issue often arises when multiple connections use the same credentials, causing older connections to lose their refresh token upon the establishment of new ones. To maintain stable connectivity, limit simultaneous connections with the same credentials and consider using separate credentials for different environments.

### Step 1: Become an admin in your LinkedIn company page

All advertising accounts are tied to a specific business in LinkedIn. Therefore, you must have a LinkedIn company page to direct people who interact with your ads. This should have been set up when you first started running ads through Campaign Manager.

Before creating your connection on Workato, ensure you are an admin on your LinkedIn company page. Only existing admins can grant you admin access. To verify your admin status, navigate to your LinkedIn company page and look for the **Super admin view** label:

![LinkedIn Super admin view](/assets/company-page.CO0k601f.png)_LinkedIn Super admin view_

If you do not see this label, contact the current admins of your LinkedIn company page to make you an admin.

### Step 2: Become an account manager in your LinkedIn advertising account

Advertising accounts also house the billing information for all campaigns. You must be an account manager for each advertising account you want to build Workato recipes for.

To become an account manager, an existing manager in your advertising account must grant you admin access. This can be done through LinkedIn's Campaign Manager.

![LinkedIn ad account access view](/assets/add-access-page.f2t_NtSQ.png)_Click "Edit" and you can add managers to this advertising account_

### Step 3: Authenticate on Workato

After receiving admin roles for your company page and advertising account, you can create a connection on Workato.

![Configuring LinkedIn connection](/assets/connection.Rg3r1MMX.png)

| Field | Description |
| --- | --- |
| Connection name | Give this LinkedIn connection a unique name that identifies the authenticated user. |
| Location | Select the project or folder in which you plan to store this connection. |
| Advanced settings (Scopes) | Select the LinkedIn scopes this connection can access. |

#### Default scopes

Workato requests the following scopes by default:

- **Manage your advertising accounts**
- **Retrieve reporting for your advertising accounts**
- **Create, modify and delete posts, comments and reactions on your behalf**
- **Access your Lead Gen forms and retrieve leads**
- **Read your basic profile**

#### Minimum scopes

The **Read your basic profile** scope is required to establish a connection.

## Connection expiry

LinkedIn's API allows Workato to maintain a valid connection for 365 days from the initial connection. This ensures long-term security for your connections. After 365 days, you must manually re-authenticate to extend the connection for another year.

Refer to the [LinkedIn documentation](https://docs.microsoft.com/en-us/linkedin/shared/authentication/programmatic-refresh-tokens?context=linkedin/marketing/context) for more information.

---
