---
url: 'https://docs.workato.com/en/agentic/workato-go/configuration.md'
description: >-
  Configure Workato GO with a custom subdomain and authenticate users with
  Workato Identity or your external identity provider (IdP).
---

# Workato GO configuration

You can configure Workato GO to use a custom subdomain and authenticate users with Workato Identity or your external identity provider (IdP).

## Configure your subdomain

You must have a Workato GO subdomain to provide end users with access to your Workato GO account. A unique, randomly generated subdomain is automatically provided for your Workato GO account. You can change this value to a custom subdomain.

Complete the following steps to configure your subdomain:

1. Sign in to your Workato account.
   
2. Go to **AI Hub** and click the **Workato GO** tab.
   
3. Click **Subdomain** in the sidebar.
   
4. Enter the subdomain you plan to use. For example, if you enter `acme-enhanced`, the URL your end users use to access the Workato GO portal is: `https://acme-enhanced.workato.ai`. Your subdomain must be greater than 3 characters and less than 65 characters. Alternatively, you can note or copy this value if you don't plan to provide a custom subdomain.
   
   ![Subdomain](/assets/subdomain.l6TMIx3t.png)_Subdomain_
   
5. Click **Save**.
   

## Configure your branding

You can use branding properties to add a custom company name and logo to your Workato GO account. Customized branding is optional. Your Workato GO account displays the default branding if you don't configure a custom name and logo.

### Add a custom name

Complete the following steps to add a custom company name to your Workato GO account:

1. Sign in to your Workato GO account.
   
2. Expand the **Admin** menu in the sidebar and click **Advanced**.
   
3. Click **Add Organization Property**.
   
4. Enter `ui.company_name` in the **Name** field.
   
   ![Custom name](/assets/custom-name.B2Ceu3Xf.png)_Custom name property configuration_
   
5. Enter the company name you plan to use in the **Value** field. For example: `Acme Inc.`
   
6. Optional. Enter a description in the **Description** field.
   
7. Click **Submit**.
   

### Add a custom logo

Custom logos must be available through a public URL or deployed within your app. We recommend that you use a transparent `.png` or `.svg`file with dimensions of `210x40px` and a file size under `200 KB`.

Complete the following steps to add a custom logo to your Workato GO account:

1. Sign in to your Workato GO account.
   
2. Expand the **Admin** menu in the sidebar and click **Advanced**.
   
3. Click **Add Organization Property**.
   
4. Enter `ui.branding_logo` in the **Name** field.
   
   ![Custom logo](/assets/custom-logo.BRlQd9v9.png)_Custom logo property configuration_
   
5. Enter the URL to your logo in the **Value** field. For example: `https://cdn.example.com/assets/acme-logo.png`
   
   > **LOGO REQUIREMENTS**
   > 
   > Your logo must be available through a public URL or deployed within your app.
   
6. Optional. Enter a description in the **Description** field.
   
7. Click **Submit**.
   

## User authentication

You can manage user authentication with [Workato Identity](/en/workato-identity). Workato Identity provides [SSO](/en/workato-identity#user-access) and [password](/en/workato-identity#add-a-user-manually) authentication workflows.

---
