---
url: 'https://docs.workato.com/en/workflow-apps/custom-domain-email-server.md'
description: >-
  Configure a custom domain and email server for Workflow apps to deliver a
  branded experience using CNAME and SPF DNS records.
---

# Custom domain and email server

The custom domain and email server features work together to provide a personalized and branded experience for Workflow app users. This ensures a seamless experience between your application and Workflow apps.

> **CNAME AND SPF RECORD SETUP**
> 
> Configuring a custom domain and email server involves adding a CNAME and an SPF record to your DNS settings. A CNAME aliases one domain to another and is required for a custom domain setup, while an SPF record specifies authorized mail servers. Although both can be used in the same registered domain, they can't coexist on the same domain or subdomain. For example, you can use a CNAME for a subdomain like `www.example.com` and an SPF record for the root domain, `example.com`.

## Custom domain

A custom domain enables you to use your own domain name instead of the default Workato domain (`{customer_subdomain}.workato.app`) for your Workflow apps. This means that you can set up your DNS (Domain Name System) domain to access the [Workflow apps portal](/en/workflow-apps/portal-settings), pages, tasks, links, and email communications using a custom domain.

Custom domains follow the `{custom_subdomain}.{customer_domain}/portal` format. For example:

```html
https://apps.idea-lifestyle.net/portal
```

### Certificate for TLS

New certificates are created automatically when you add a custom domain. Workato manages certificates to enable HTTPS on the custom domains that you add.

#### Certificate renewals

Custom domain certificates automatically renew one month before the set expiration date. Workato manages the renewal process with [Let's Encrypt](https://letsencrypt.org/). The new certificate request for the custom domain includes validating domain ownership through DNS records or other verification methods specified by Let's Encrypt. Workato automatically deploys the new certificate after Let's Encrypt issues it. This seamless transition ensures that your custom domain continues to operate over HTTPS without interruption or manual intervention required on your end.

> **CERTIFICATE AUTHORITY AUTHORIZATION (CAA) RECORD**
> 
> If you restrict the Certificate Authorities (CAs) that are allowed to issue certificates for your site, the custom domain workflow fails when trying to issue a certificate for your custom domain. [Add a CAA record](https://letsencrypt.org/docs/caa) for Let's Encrypt's domain name `letsencrypt.org` to resolve this.

### Set up a custom domain

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

Complete the following steps to set up a custom domain:

1. Sign in to your Workato account.
   
2. Use the sidebar navigation to go to **Platform > Workflow apps portal > Portal settings > Custom domain and email server**.
   
3. Click **Add domain**.
   
   ![Add domain](/assets/domain-add.d7DfDtRi.png)_Add a domain_
   
4. Enter your full domain name, including the subdomain, and click **Add domain**. For example, `apps.idea-lifestyle.net`.
   
   ![Register a domain](/assets/apps-register-domain.qExu_-7z.png)_Register a domain_
   
5. Verify your domain by configuring the CNAME record in your DNS settings
   
   1. In your DNS manager, go to **Websites** and select your domain. This example uses [Cloudflare](https://dash.cloudflare.com/login).
      
   2. Open **DNS > Records** and click **\+ Add record**.
      
   3. Select `CNAME` as the **Type** and supply your subdomain name in the **Name** field. For example, `apps`.
      
   4. Provide the **Target**. Copy and paste the **Value** from Workato. For example:
      
      ```
      apps-custom.workato.app
      ```
      
      The **Value**/**Target** varies based on the [data center](/en/datacenter/datacenter-overview) that serves your Workato workspace. Use the URL that matches your data center.
      
      > **PREREQUISITES**
      > 
      > To set up a custom domain for your Workflow apps, you must have the following:
      > 
      > - A domain to which you have permissions to manage DNS records. You can prepare a registered domain name or use an existing domain for this purpose. For more information on domain names, see the [ICANN documentation](https://www.icann.org/resources/pages/register-domain-name-2017-06-20-en).
      
      ### Workato Enterprise customers
      
      - US Data Center: `apps-custom.workato.app`
      - EU Data Center: `apps-custom.eu.workato.app`
      - SG Data Center: `apps-custom.sg.workato.app`
      - JP Data Center: `apps-custom.jp.workato.app`
      - AU Data Center: `apps-custom.au.workato.app`
      - IL Data Center: `apps-custom.il.workato.app`
      - KR Data Center: `apps-custom.kr.workato.app`
      - UK Data Center: `apps-custom.uk.workato.app`
      
      ### Self-service (Workato Free, Workato Pro, or Developer Sandbox) users
      
      - Self-service Data Center: `apps-custom.trial.workato.app`
   5. Set the **Proxy status** to `DNS only`.
      
   6. Click **Save**.
      
      ![Add CNAME to DNS](/assets/dns-record-add.Cp18Zp0S.png)_Add a CNAME record to your DNS settings_
      
   
6. Depending on your domain host, it can take up to 24 hours for the new CNAME record to propagate through the global domain name system. After verifying your custom domain's DNS, Workato generates an SSL certificate. It can take up to an hour for the certificate to be issued and ready for use. Refresh the **Custom domain and email server** page to check on the status.
   
   **Verification pending**
   
   ![Domain verification pending](/assets/domain-pending.CngyZvyX.png)_Domain verification pending_
   
   **Domain verified**
   
   ![Domain verified](/assets/domain-verified.B-WkmqcZ.png)_Domain verified_
   

## Custom email server

Workato allows you to send emails from your Workflow apps using SMTP (Simple Mail Transfer Protocol). This feature enables you to send emails from addresses like `{username}@{customerdomain}.com` instead of the default `admin@workato.app`. By using your organization's email server, such as Exchange Online or Gmail, you can maintain consistency in your communications.

### Set up a custom email server in Workato

Complete the following steps to set up your custom email server in Workato. This process involves obtaining values from your SMTP email server.

1. Sign in to your Workato account.
   
2. Use the sidebar navigation to go to **Platform > Workflow apps portal > Portal settings > Custom domain and email server**.
   
3. Click **Add email server**.
   
   ![Add email server](/assets/custom-email-server-add.CPCM4VCS.png)_Add email server_
   
4. Configure your email server
   
   1. In the **Server** field, add your SMTP email server value. For example, `smtp.gmail.com`.
      
   2. In the **From email address** field, provide an email address from which you plan to send Workflow apps communications. Users will see this email address in all correspondence. For example, `noreply@apps.idea-lifestyle.com`.
      
   3. In the **User name** field, add your SMTP email server username.
      
   4. In the **Password** field, enter your SMTP email server password.
      
   5. Enter `587` in the **Port** field. Workato only supports port `587` for secure email transfer.  
      **Port 25 isn't supported and connections using it fail**.
      
   6. Click **Next**.
      
      ![Email server setup](/assets/email-server-setup.oxm-1XrM.png)_Email server setup_
      
   
5. In the **Send to email address** field, provide your email address and click **Send test email**. Workato sends a test email to this address to verify the email server is working.
   
6. Check your inbox and spam folder to confirm the email was sent successfully.
   
   ![Verification email](/assets/email-server-verification.Waaf8hny.png)_Email verification sent_
   
7. Click **Add email server**.
   

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

---
