---
url: 'https://docs.workato.com/en/api-mgmt/api-prefix.md'
description: >-
  Learn how API prefixes set unique base paths per Workato account so you can
  separate development, testing, and production endpoints and reuse collection
  paths.
---

# API Prefix

API prefixes are base paths that are unique to each Workato account. You can use it to define your API platform environment. For example, you can use the API prefix to differentiate development, testing, and production endpoints. Doing so allows you to reuse your collection paths.

Having standardized collection names across your company simplifies the [recipe export process](/en/recipe-development-lifecycle). For example, your team can easily export recipes from the development account (`/acme-dev/sales-api/`) to the production account `/acme/sales-api/` without worrying about conflicting collection paths. API Prefix lets your work seamlessly between your environments.

> **WARNING**
> 
> `oauth2` is a reserved namespace. The path prefix `oauth2/*` is not allowed.

## Understanding the Endpoint

Every Workato endpoint consists of several parts. These components together form a unique API endpoint.

![Endpoint components](/assets/url-endpoint-explained.CoImqLqH.png)_Endpoint components_

| Component | Description |
| --- | --- |
| Domain and subdomain | By default, Workato API's are called from `apim.workato.com`. You can customize the domain name with [custom domain configuration](/en/api-mgmt/custom-domain). |
| API prefix | API prefix are higher-level directory paths used to define your API platform environment. |
| Collection path | Collections are logical groups of endpoints whose access pattern has some common features, see [API collection](/en/api-mgmt/api-collections) to find out more. |
| Endpoint path | Endpoint paths can be configured from the [endpoint overview](/en/api-mgmt/configure-recipe-endpoint#step-1-create-the-endpoint). |

## Configuration

Go to **Platform > API Platform > Settings > API path prefix**.

![Customize API prefix](/assets/path-prefix.BS2mZOmf.png)_Customize API prefix_

This API prefix will apply for all API collections and endpoints in this account (individual or team). The default API prefix is set to the initials of your account profile name.

> **WARNING**
> 
> Changes to API prefix will require existing clients of the API to make adjustments on their end.

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

### API Prefix for old API collection

All newly created Workato API collections come preconfigured with an API prefix. However, this does not apply to older API collections. Those will retain their existing URL until you decide to upgrade them.

#### Why upgrade API collection?

This upgrade immediately enables API prefix for this API collection. This includes the benefits of a streamlined recipe export/import. It will also enable custom domain configuration, which allows you to expose API endpoints under your own subdomain. Lastly, future upgrades to API platform will build on this version of API collection. Upgrade this API collection to benefit from new features.

> **WARNING**
> 
> Note that this action cannot be undone. Once your API collection has been upgraded to use API prefix, you will not be able to revert back to the old URLs. You should prepare to inform all existing clients using this API of this change.

#### How to upgrade API collection

For example, this API collection has not activated API prefix. We will run through the process to upgrade your API collection.

Complete the following steps to upgrade your API collection:

1. Go to the **Settings** tab of the API collection.
   
2. Select **Start upgrade**.
   
3. Read the upgrade notes and select **Start upgrade**.
   

The upgrade is complete. All endpoints in this API collection now have API prefixes enabled.

Next, inform the existing users of this API collection, if you have not already done so.

---
