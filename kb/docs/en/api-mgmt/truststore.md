---
url: 'https://docs.workato.com/en/api-mgmt/truststore.md'
description: >-
  Manage certificate bundles in the Workato Truststore to define trusted CA
  chains that validate client certificates during mTLS authentication.
---

# Truststore

The Truststore lets you manage certificate bundles that Workato uses to validate client certificates during [mutual TLS (mTLS) authentication](/en/api-mgmt/mtls). These bundles define trusted certificate authority (CA) chains that Workato uses to validate client certificates during the TLS handshake. You must upload at least one certificate bundle to enforce mTLS.

> **CUSTOM DOMAIN REQUIRED**
> 
> Your workspace must use a custom domain with self-managed certificates to enforce mTLS. Workato disables mTLS authentication and displays an alert in the Truststore if your custom domain is inactive or misconfigured.
> 
> Refer to the [Custom domain status and mTLS availability](#custom-domain-status-and-mtls-availability) section for more information.

## Upload a certificate bundle

Complete the following steps to upload a certificate bundle:

1. Click **Add bundle**.
   
   ![Add certificate bundle](/assets/add-bundle.ktKxpVhF.png)_Add certificate bundle_
   
2. Upload a valid `.pem` file that includes a root and intermediate CA certificates.
   
   ![Add certificate bundle](/assets/add-bundle-modal.CTnKwHAy.png)_Add certificate bundle_
   
3. Enter a **Name** to identify your bundle. Workato uses the file name as the bundle name if left blank.
   
4. Click **Add bundle**.
   
   > **FORMAT AND LIMITS**
   > 
   > Each upload must be a single `.pem` file with root and intermediate certificates. The maximum file size is 1 MB, and the Truststore supports up to 50 bundles per workspace.
   
5. Confirm that the bundle appears in the Truststore with one of the following statuses:
   
   - **Valid**: All certificates are valid.
   - **Expiring soon**: One or more certificates expire within 14 days.
   - **Expired**: One or more certificates have expired.

## Manage certificate bundles

Use the **•••** (ellipsis) menu in the Truststore to manage certificate bundles. You can **Rename** a bundle, **Download** it, [replace it with a new PEM file](#replace-an-existing-certificate-bundle), or delete it if it's no longer in use.

![Manage certificate bundle](/assets/manage-bundles.BhKhtkCp.png)_Manage certificate bundles_

When you replace a bundle, Workato updates all clients that use it. The new certificates take effect immediately without downtime.

Workato logs all changes in the activity audit log for traceability.

### Replace an existing certificate bundle

Workato displays a warning if a bundle expires within 14 days or within 24 hours. Replace the bundle before it expires to avoid mTLS handshake failures.

1. Locate the expiring bundle in the Truststore.
   
2. Click **Replace** next to the expiration badge, or click **•••** (ellipses) and select **Replace bundle**.
   
   ![Replace certificate bundle](/assets/replace-bundle.C9GfD9VH.png)_Replace certificate bundle_
   
3. Upload a new `.pem` file in the **File upload** field with a valid root and intermediate CA certificates.
   
   ![Replace certificate bundle](/assets/replace-bundle-2.Bi30S92U.png)_Replace certificate bundle_
   
4. Optional. Enter a new **Name**.
   
5. Click **Replace bundle**.
   

Workato replaces the bundle immediately and uses the new certificates for client validation. After replacement, the expiration date and status reflect the updated bundle. This update affects all clients that use the replaced bundle.

## Expiring certificate bundles

Workato tracks certificate expiration dates and flags issues before they affect your API traffic.

The Truststore displays a visual warning when a certificate in a bundle nears expiry. Workato also sends email alerts 14 days, 7 days, and 1 day before expiration. These alerts help you replace expiring bundles before they cause authentication failures.

## Custom domain status and mTLS availability

Workato enforces mTLS only when your workspace has a valid custom domain. The Truststore disables mTLS certificate validation if the domain is inactive or misconfigured.

The Truststore displays a warning when mTLS enforcement becomes unavailable due to domain issues.

![mTLS enforcement warning](/assets/enforcement-warning.DEMK0PxZ.png)_mTLS enforcement warning_

Click **Check custom domain settings** to update your configuration. Contact your workspace administrator if you don't have access to API settings. Workato doesn't enforce mTLS until the custom domain becomes active, even if certificate bundles are present.

---
