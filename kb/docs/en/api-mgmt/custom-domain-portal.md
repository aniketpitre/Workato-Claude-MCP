---
url: 'https://docs.workato.com/en/api-mgmt/custom-domain-portal.md'
description: >-
  Configure a custom domain to serve the Workato API developer portal under your
  own branded URL with automatic TLS certificates.
---

# Custom domain

You can personalize the API developer portal experience by configuring a custom domain. This lets you serve the portal under your branded URL and enhances trust and consistency when developers access documentation and test endpoints.

> **CNAME RECORD SETUP**
> 
> You must add a CNAME record in your DNS settings to configure a custom domain. These records must apply to different DNS names. For example, use a CNAME for `portal.example.com` and reserve other DNS records for the root domain, such as `example.com`. Most DNS providers don't allow a CNAME and other record types on the same subdomain.

> **FEATURE AVAILABILITY**
> 
> API platform custom domains aren't supported in the China data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## Custom domain

Custom domains allow you to host your API Developer Portal under your organization’s domain. This replaces the default Workato-hosted URL with a branded one like `https://portal.example.com`.

You can configure your DNS settings so that developers access the portal and API documentation from a branded domain instead of the default Workato domain (`{customer_subdomain}.portal.app.workato.com`).

Custom domains follow the `{subdomain}.{your_domain}` format. For example:

```html
https://portal.idea-lifestyle.net
```

### Certificate for TLS

Workato issues and manages HTTPS certificates through [Let’s Encrypt](https://letsencrypt.org/) for custom domains. Certificates renew automatically one month before the expiration date.

> **CERTIFICATE AUTHORITY AUTHORIZATION (CAA) RECORD**
> 
> Add a CAA record for `letsencrypt.org` if your DNS restricts which certificate authorities can issue certificates for your domain.

### Configure a custom domain

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

Complete the following steps to set up a custom domain for your API Developer Portal:

1. Sign in to your Workato account.
   
2. Go to **Platform > API platform > Settings > Developer Portal > Custom domain**.
   
3. Click **Add domain**.
   
   ![Add custom domain](/assets/add-custom-domain-portal.QUgIMmM3.png)_Add custom domain_
   
4. Enter your full subdomain and click **Add domain**. For example, `portal.example.com`.
   
   ![Add full subdomain](/assets/enter-full-subdomain.Cja4XZqa.png)_Enter full subdomain_
   
   > **DOMAIN NAME IN USE**
   > 
   > You can't use the same subdomain across different Workato environments or features. Use a distinct subdomain to avoid conflicts.
   
5. Verify your domain by creating a CNAME record in your DNS provider’s admin console.
   
6. Open your DNS provider’s DNS management console.
   
7. Add a new CNAME record for your subdomain and point it to the target **Value** provided in your **Custom domain** settings in Workato. For example, `abcde123456.apim-portal-custom.workato.com`.
   
8. Save the DNS record.
   
9. Click **Save**.
   

It can take up to 24 hours for the CNAME record to propagate. After DNS verification, Workato issues and applies an SSL certificate for your domain. Certificate generation may take up to an hour. Refresh the **Custom domain** page to check the status.

> **PREREQUISITES**
> 
> Ensure you have the following before you configure a custom domain:
> 
> - Access to your DNS host
> - A registered domain and subdomain name. Refer to the [ICANN documentation](https://www.icann.org/resources/pages/register-domain-name-2017-06-20-en) for more information on domain names. For example, `portal.boltcompany.com`.

### Remove a custom domain

Complete the following steps to remove a custom domain:

1. Click **Remove** next to the custom domain entry.
   
2. Confirm the action in the modal dialog to revert to the default Workato domain.
   
   ![Remove custom domain](/assets/remove-custom-domain-portal.E2SQpPOf.png)_Remove custom domain_
   

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

---
