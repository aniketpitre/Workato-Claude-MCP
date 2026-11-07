---
url: 'https://docs.workato.com/en/oem/workato-embedded.md'
description: >-
  Workato Fully Embedded lets you build and manage customer integrations inside
  your product using full page or widget iframes in the UI.
---

# Workato Fully Embedded

Workato Fully Embedded allows you to build and manage customer integrations directly within your product by embedding a full page `iframe` or individual widget `iframes` in the UI.

![Embedded](/assets/workato-embedded.DsCmtPzc.png)_Embedded in an `iframe` in ACME ERP_

Embedded provides an alternative to building an in-house integration or automation solution. Embedding the Workato platform or its widgets into your product UI enables you and your customers to build, run, and maintain integrations using Workato’s tools.

## Embedded options

Workato Fully Embedded supports two embedding options, allowing you to tailor the automation experience to your product and customer needs:

### Full page embedding

Embed the full Workato platform as an `iframe` to give customers access to features such as the recipe editor, dashboards, and app connections within your product’s interface. This approach provides a seamless integration that allows your users to perform a wide range of automation tasks without leaving your application.

For details on implementing fully embedded, refer to the [Embedding Workato implementation guide](/en/oem/workato-embedded-implementation#full-page-iframes).

### Widget embedding

You can use Workato widgets to embed specific, function-focused automation tools directly in your application. Widgets enable you to integrate Workato’s capabilities while keeping your product’s interface focused and intuitive.

For details on implementing widgets such as the connection widget, recipe widget, or dynamic field mapping widget, refer to the [Embedding Workato implementation guide](/en/oem/workato-embedded-implementation#widget-iframes).

## Supported features

Workato’s embedded options include several features to enhance the user experience, providing flexibility to tailor navigation, enable deep linking, and ensure seamless communication between your product and embedded content. The following features help you deliver a smooth and integrated experience for your customers.

### Navigation

Full page embedding allows you to tailor the navigation experience in your UI to meet your customers’ needs by providing a full page `iframe` without the Workato-specific navigation bar. You can define which Workato features to include by specifying the appropriate Workato paths for each page, such as `/recipes`, and building your own navigation links between them. Full-page embedding can reference any unique Workato URL.

For example, you can include the following features:

- **Dashboard**
- **Recipes**
- **App connections**
- **Community pages**

![Navigation](/assets/embedded-iframe.m9A10y2T.png)_Navigation and the Workato `iframe`_

You can also provide links to **Tools**, such as **Lookup tables** and **Environment properties**, to offer additional functionality.

> **SYSTEM ACCESS**
> 
> The customer's plan or role determines the pages they can access. Refer to the [Role-based access control](/en/user-accounts-and-teams/role-based-access/) documentation for more information.

### Browser navigation and deep linking

Embedded supports seamless browser navigation and deep linking to provide a smooth user experience. Whether embedding full-page iframes or widgets, users can navigate using the browser’s **back** and **forward** buttons or open new tabs. The correct Workato pages or widgets load automatically based on your URL and path configuration.

![Embedded URL](/assets/embedded-url.CFngeQX_.png)_Embedded Partner URL and Workato path_

Deep linking maps your product URLs to the corresponding Workato URLs for both full-page iframes and widgets. This ensures that when users launch your URLs, the correct iframe or widget loads, making browser links shareable and accessible for later use.

In the following example, the vendor URL is `https://acme-erp.com/integration`, followed by the Workato path `/dashboard` to direct users to the correct page.

![Embedded URL](/assets/embedded-url.CFngeQX_.png)_Embedded Partner URL and Workato path_

### Redirection

When users visit `https://www.workato.com/` while logged into your app, Embedded redirects them to your provided URL. For example, Workato redirects customers to `https://acme-erp.com/integration`.

### Browser support and configuration

Embedded supports all modern and up-to-date browsers, including the following:

- Google Chrome
- Apple Safari
- Microsoft Edge
- Mozilla Firefox

> **EMBEDDED AVAILABILITY**
> 
> Internet Explorer is not supported. You must switch to Microsoft Edge or another browser to use Embedded functionality.

To ensure proper loading of Workato iframe content, update your browser settings using the following instructions:

#### Google Chrome

By default, Chrome blocks third-party cookies in incognito mode. Complete the following steps to allow them:

1. Go to **Settings > Privacy and security > Third-party cookies**.
   
2. Select **Allow third-party cookies**.
   
   ![Chrome cookies](/assets/google-cookies.Dn1QPl_W.png)_Select **Allow all cookies** to enable the Workato `iframe` to load_
   

#### Apple Safari

Adjust the privacy settings to allow `iframe` content to load:

1. Go to **Settings > Privacy**.
   
2. Disable **Prevent cross-site tracking** to enable third-party cookies.
   

#### Mozilla Firefox

Embedded customers may be redirected to the Workato login page when attempting to establish a connection. Embedded customers should add your origin URL(s) to Firefox's Enhanced Tracking Protection exceptions to resolve this:

1. Go to **Settings > Privacy & Security > Enhanced Tracking Protection**.
   
   ![Firefox Enhanced Tracking Protection settings page](/assets/firefox-enhanced-tracking-protection.BfjqHIgk.png)_Firefox Enhanced Tracking Protection settings page_
   
2. Click **Manage Exceptions** and add your origin URL(s).
   
   ![Firefox Manage Exceptions dialog for adding allowed sites](/assets/firefox-manage-exceptions.DsitWh-v.png)_Firefox Manage Exceptions dialog for adding allowed sites_
   

When you configure multiple origin URLs (such as regional domains), Embedded customers must add exceptions for each domain. Embedded customers can also switch to Chrome or another supported browser.

---
