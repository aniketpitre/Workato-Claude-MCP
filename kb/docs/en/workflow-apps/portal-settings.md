---
url: 'https://docs.workato.com/en/workflow-apps/portal-settings.md'
description: >-
  Configure the Workflow apps portal name, URL prefix, branding, custom domain,
  email server, and security settings in Workato.
---

# Portal settings

Go to **Platform > Workflow apps portal > Portal settings** to configure the Workflow apps portal. The **Portal settings** tab includes the following sections:

- [General](#general)
- [Branding](#branding)
- [Custom domain and email server](#custom-domain-email-server)
- [Security](#security)

* * *

## General

This section enables you to set up the **Portal name** and customize the **Portal URL** by choosing a unique URL prefix.

- Portal name
  
- Business name of your Workflow apps portal. Workato displays the portal name in the App portal and email notifications.
  
- Portal URL
  
- Customize the URL prefix. The data center you use determines where the Workflow apps portal is hosted. Example: `https://acme.workato.app`
  

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

### Workato Enterprise customers

- US data center: `workato.app`
- EU data center: `eu.workato.app`
- SG data center: `sg.workato.app`
- JP data center: `jp.workato.app`
- AU data center: `au.workato.app`
- IL data center: `il.workato.app`
- KR data center: `kr.workato.app`
- UK data center: `uk.workato.app`

### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users

- Self-service data center: `trial.workato.app`

* * *

## Branding

This section enables you to customize the **Workflow apps portal** to include your brand logo, change branding colors to match your organization, and configure a custom font.

- Brand logo
  
- Supports PNG and SVG file types.
  
  - Maximum file size:
  - 10 MB
  - Display area:
  - The portal scales your logo to fit a set area and preserves its proportions. The sign-in page displays logos up to 360 px wide and 80 px tall. The portal header displays logos up to 28 px tall, with no width limit.
  - Recommended aspect ratio:
  - Use an image with a width-to-height ratio of about 4.5:1 or narrower to display at the full 80 px height. For example, an image with the dimensions of 720 × 160 px (2× the display area) stays sharp on high-resolution screens. Logos wider than 4.5:1 display shorter than 80 px tall.
- Brand color
  
- Choose a color for the headers, buttons, and navigational elements. You can enter a hex color code or use the color picker.
  
  - Sample value:
  - `#739ad9`
- Complementary text color
  
- Pair a complementary color with the brand color to optimize contrast. You can enter a hex color code or use the color picker.
  
  - Sample value:
  - `#d3ce31`
- Google Fonts URL
  
- Enter a Google Fonts URL to apply a custom font to the Workflow apps portal. Custom fonts don't apply to Workflow apps email notifications.
  

* * *

### Preview

The Preview feature enables you to preview how the **Brand color**, **Complementary text color**, and **Brand logo** work together before implementing them in your Workflow apps portal.

The preview is static and contained within the **Settings** interface.

![Preview your branding choices](/assets/branding.V9s5wjlj.png)_Preview your branding choices for the Workflow apps portal_

* * *

## Custom domain and email server

You can set up a custom domain and email server for your Workflow apps portal. Refer to the [Custom domain and email server](/en/workflow-apps/custom-domain-email-server) documentation for more information.

* * *

## Security

The security section enables you to set up authentication for the portal and control whether portal pages can be embedded in external websites.

### Authentication

Workato supports the following authentication schemes:

- Password authentication
- [SAML-based SSO](/en/workflow-apps/saml)

![Security settings](/assets/settings-security.DRVEiKYd.png)_Set up security settings for the Workflow apps portal_

### Embedding

You can embed portal pages into your organization's internal portals, Salesforce, and more.

Toggle **Enable iframe embedding** to allow embedding your portal pages in an `iframe`. From here, you can enable embedding your portal pages in any `iframe`, or only within domains you specify.

If you plan to limit embedding your portal pages only to specific domains, you can specify one or more URLs in the **Specify frame ancestors** field. These URLs are used in the Content-Security-Policy HTTP header to allow rendering of Workflow apps in an `iframe`.

Alternatively, leave this field blank to allow embedding pages in any `iframe`.

![Specify domains](/assets/settings-security-embedding.OesX5nZo.png)_Enable embedding_

#### Customize portal for embedding

When you embed portal pages within external sites, you can customize the portal's appearance by hiding the top banner and customizing the padding on all sides by appending specific query parameters to your [portal URL](#portal-url).

These parameters are URL-encoded JSON in the following format:

Example:

```
{"showHeader": false, "layoutPadding": "0 10px 10px 0"}
```

  

- showHeader
  
- Boolean (true/false) value. Set to `false` to hide the top header of the portal.
  
- layoutPadding
  
- Determine the padding of the portal on all sides. In the preceding example, the top padding is `0`, the right is `10px`, the bottom is `10px`, and the left is `0`.
  

The following demonstrates how to generate the parameter value in your browser console:

```
encodeURIComponent(JSON.stringify({"showHeader": false, "layoutPadding": "0 10px 10px 0"}))
```

Which results in the following parameter. Append this to your portal URL:

```
?embedding_params=%7B%22showHeader%22%3Afalse%2C%22layoutPadding%22%3A%220%200%200%200%22%7D
```

Altogether, it looks something like this:

```

<iframe src="https://mycompany.workato.app/app-name/?embedding_params=%7B%22showHeader%22%3Afalse%2C%22layoutPadding%22%3A%220%200%200%200%22%7D"></iframe>
```

---
