---
url: 'https://docs.workato.com/en/api-mgmt/custom-domain.md'
description: >-
  Configure a custom domain to route Workato API platform endpoints through your
  own subdomain instead of the default apim.workato.com URL.
---

# Custom Domain

Route Workato API endpoints through your own domain to expose Workato API endpoints under your own subdomain. For example, modify the endpoint to reflect your company's subdomain.

**Original API URL:** `https://apim.workato.com/boltco/sales-api/get-invoice`

**Custom domain URL:** `https://api.boltcompany.com/sales-api/get-invoice`

Custom domain names in Workato aren't case sensitive.

> **FEATURE AVAILABILITY**
> 
> API platform custom domains aren't supported in the China data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## Configure a custom domain

1. Prepare a registered domain and subdomain name. For more information on domain names, see the [ICANN documentation](https://www.icann.org/resources/pages/register-domain-name-2017-06-20-en). For example, `blog.boltcompany.com`.
   
2. Go to **Platform > API Platform > Settings > Custom domain** and click **Add domain**.
   
   ![Register custom domain](/assets/add-custom-domain-blank.CplK-Qn7.png)_Register custom domain_
   
3. Enter your subdomain name and click **Add domain**.
   
   ![Register a domain](/assets/add-custom-domain.DpADdTPh.png)_Register a domain_
   
4. Verify your custom domain by configuring the CNAME record with your domain host. The following steps use Cloudflare as an example.
   
5. Click **Add record**, select `CNAME` as the type, and provide the subdomain name, for example: `api` for domain `boltcompany.com`.
   
   ![Create CNAME record with Cloudflare](/assets/add-cname-record-cloudflare.C8XsZwmr.png)_Create CNAME record with Cloudflare_
   
6. Copy and paste the unique target value from your **Custom domain** settings. Use this value for your CNAME record. For example, `abcde123456.apim-custom.workato.com`.
   
   ![Copy the unique CNAME target from your Custom domain settings](/assets/copy-domain-value.UCKxbbgz.png)_Copy the unique CNAME target from your **Custom domain** settings_
   
7. Click **Save**.
   
   It might take up to an hour for the new CNAME record to propagate through the global domain name system depending on the domain host. Workato starts generating a TLS certificate after verifying your custom domain's DNS. It can take up to an hour for the certificate to be issued and ready for use. Refresh the **Custom domains** page to check on the status.
   
   > **CAN THE ORIGINAL ENDPOINT NAME BE USED?**
   > 
   > - The original API endpoint continues to work in parallel with your custom domain.
   > - Requests to custom domains are routed to a [specific set of IP addresses](/en/security/ip-allowlists#custom-apim-domains).
   

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

## Certificate for TLS

The default domain is `workato.com` when you use Workato’s API platform. Custom domains are supported. New certificates are created automatically when you add a custom domain. Workato manages API certificates to enable HTTPS on the custom domains that you add.

### Certificate renewals

Custom domain certificates automatically renew one month before the set expiration date. Workato manages the renewal process with [Let’s Encrypt](https://letsencrypt.org/). The new certificate request for the custom domain includes validating domain ownership through DNS records or other verification methods specified by Let’s Encrypt. Workato automatically deploys the new certificate after it is issued by Let's Encrypt. This seamless transition ensures that your custom domain continues to operate over HTTPS without interruption or manual intervention required on your end.

> **CERTIFICATE AUTHORITY AUTHORIZATION (CAA) RECORD**
> 
> If you restrict the Certificate Authorities (CAs) that are allowed to issue certificates for your site, the custom domain workflow fails when trying to issue a certificate for your custom domain. Add a CAA record for Let's Encrypt's domain name `letsencrypt.org` to resolve this. [Find out more](https://letsencrypt.org/docs/caa).

## Remove custom domain configuration

You may have to remove the current custom domain configuration if you would like to reconfigure your API platform to a different custom domain.

1. Click **Remove** on the top-right of the screen.  
   ![Custom domain page](/assets/copy-domain-value.UCKxbbgz.png)_Custom domain page_
   
2. Read the notes on the remove custom domain wizard. Tick the checkbox and select **Remove Domain**.  
   ![Remove custom domain](/assets/remove-custom-domain.w3tNnE2P.png)_Remove custom domain_
   

Your APIs default to `apim.workato.com`. Inform the existing users of this API collection about the new domain if you haven't done so already.

## Custom domain APIM IP addresses

Workato routes client traffic to data center-specific IP addresses when using custom domains for API recipes. Refer to the [Custom APIM domains and IP addresses](/en/security/ip-allowlists#custom-apim-domains) documentation for more information.

---
