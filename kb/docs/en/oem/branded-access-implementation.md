---
url: 'https://docs.workato.com/en/oem/branded-access-implementation.md'
description: >-
  Set up branded access SSO for Embedded by redirecting customers to Workato
  through a JWT-authenticated direct link URL.
---

# Branded access SSO - JWT direct linking implementation guide

You can use the branded SSO implementation model to securely redirect your customers from your application to Workato. This limits login access to Workato to the partner application.

This implementation model works by redirecting customers from your application to a Workato URL that is authenticated using a JWT (JSON Web Token) that is sent as a URL parameter.

Within Workato, you can offer customers pre-built integrations and allow your customers to modify or build their own automations. You can use [role-based access control](/en/user-accounts-and-teams/role-based-access/) to assign roles to your customers, defining their access to specific [projects](/en/projects), tools, and features within Workato, including [recipe lifecycle management](/en/recipe-development-lifecycle), the [activity audit log](/en/features/activity-audit-log), and more.

Additionally, you can use the [theme editor](/en/oem/branding) to customize the Workato app to match your own branding.

This guide consists of the following sections:

- [Prerequisites](#prerequisites)
- [Construct a direct link URL](#direct-link-url)
- [Log out of a Workato session](#log-out)

## Prerequisites

- JSON Web Token (JWT)
- **_Required._** Generate a JWT to facilitate secure access to Workato. JWTs authenticate users and provide verified access to applications and resources. As a reminder, the following information is required to generate a JWT. Learn more in our [JWT direct linking](/en/oem/jwt-direct-linking#step3) guide.
  - Private and public key pair
  - **_Required._** The JWT token must be signed using a private key generated with the RS256 algorithm. Workato uses the public key to verify the generated JWT tokens. Use the [Update JWT signing key API](/en/oem/oem-api/jwt-direct-link-configurations#update-jwt-signature-verification-key) to set the public key or provide the public key to your Workato Success Representative.
  - Embedded vendor ID
  - **_Required._** The Embedded vendor ID is required to generate the JWT. Use the vendor ID returned by [Update JWT signing key API](/en/oem/oem-api/jwt-direct-link-configurations#update-jwt-signature-verification-key) or ask your Workato Success Representative to provide the value for this ID after you provide your public key.
  - Customer workspace ID
  - **_Required._** The customer workspace ID is the unique ID of the Embedded customer workspace in Workato. You can obtain this value from the Workato UI or programmatically. From the UI, obtain the customer workspace ID by navigating to the **Admin console > Customers** and selecting the specific customer. When selected, the customer workspace ID is present in the URL. Alternatively, fetch the customer workspace ID by calling our [get customer API](/en/oem/oem-api/managed-users#get-customer-account). If the external ID is used instead of the Workato ID, the segment should start with the prefix `E`.
  - Customer user ID
  - **_Optional._** The customer user ID is the unique ID of an individual workspace member in the customer workspace. Include the customer user ID when the user's specific role must apply to the Workato session created. Fetch the customer user ID by calling our [get customer workspace member API](/en/oem/oem-api/managed-users#get-list-of-customer-account-members). If the external ID is used instead of the Workato ID, the segment should start with the prefix `E`.

## Construct a direct link URL

To provide access to Workato for your customers from your application, construct a direct link URL and redirect them to this URL. The JWT generated in the previous step is sent as a URL parameter in this direct link URL. Workato validates the JWT to ensure its integrity and authenticity, using it to establish an authenticated session and provide verified access to Workato for your customer.

Use the following direct link URL formats for branded access SSO implementations based on your data center:

**Workato accounts hosted in the US Data Center**

```html
https://app.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Europe Data Center**

```html
https://app.eu.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Singapore Data Center**

```html
https://app.sg.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Japan Data Center**

```html
https://app.jp.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Australia Data Center**

```html
https://app.au.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the Israel Data Center**

```html
https://app.il.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the China Data Center**

```html
https://app.workatoapp.cn/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the South Korea Data Center**

```html
https://app.kr.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

**Workato accounts hosted in the United Kingdom Data Center**

```html
https://app.uk.workato.com/direct_link/recipes?workato_dl_token=<jwt_token>
```

## Log out of a Workato session

When a customer is redirected to Workato, a secure Workato session is created for the customer. If the customer logs out of your application, you can also configure this implementation to log them out of the active Workato session by redirecting the customer to Workato’s sign out URL. The sign out URL varies depending on the data center you use. Refer to the following list to determine which sign out URL you should use.

**Sign out URL for accounts hosted in the US Data Center**

```html
https://app.workato.com/users/sign_out
```

**Sign out URL for accounts hosted in the Europe Data Center**

```html
https://app.eu.workato.com/users/sign_out
```

**Sign out URL for accounts hosted in the Singapore Data Center**

```html
https://app.sg.workato.com/users/sign_out
```

**Sign out URL for accounts hosted in the Japan Data Center**

```html
https://app.jp.workato.com/users/sign_out
```

**Sign out URL for accounts hosted in the Australia Data Center**

```html
https://app.au.workato.com/users/sign_out
```

**Sign out URL for accounts hosted in the Israel Data Center**

```html
https://app.il.workato.com/users/sign_out
```

**Sign out URL for accounts hosted in the China Data Center**

```html
https://app.workatoapp.cn/users/sign_out
```

**Sign out URL for accounts hosted in the South Korea Data Center**

```html
https://app.kr.workato.com/users/sign_out
```

**Sign out URL for accounts hosted in the United Kingdom Data Center**

```html
https://app.uk.workato.com/users/sign_out
```

### Sample sign out URL

```html
<a href="https://app.workato.com/users/sign_out" @click="opened = false">Sign out</a>
```

---
