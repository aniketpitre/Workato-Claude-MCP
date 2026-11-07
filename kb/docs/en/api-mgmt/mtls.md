---
url: 'https://docs.workato.com/en/api-mgmt/mtls.md'
description: >-
  Configure mutual TLS (mTLS) for an API platform client to require valid client
  certificates verified against your workspace truststore.
---

# Mutual TLS authentication

Mutual TLS (mTLS) provides an added layer of security for your APIs. It requires both the client and server to present valid certificates during the SSL handshake, allowing each party to verify the other's identity.

Workato checks client certificates against trusted certificate authority (CA) chains defined in your workspace's [Truststore](/en/api-mgmt/truststore).

mTLS works with your configured authentication method. Workato validates both the access token and the client certificate for each request. This ensures that only trusted and authenticated clients can access your APIs.

> **CUSTOM DOMAIN REQUIRED**
> 
> Your workspace must have an active custom domain to enable mTLS.

## Configure mTLS for an API client

Complete the following steps to enable mTLS enforcement for an API client. This requires each request to present a valid client certificate:

1. Go to **API platform > Clients**, then click **\+ Add new client**.
   
2. Enter client details such as the **Name** and **Description**. You can optionally upload a **Client logo** and enable **Grant client access to portal**.
   
3. Click **Next**.
   
4. Choose an **Authentication method** for the client.
   
5. Toggle **Enforce mutual TLS (mTLS)**.
   
   ![Edit Mutual TLS](/assets/enforce-tls.CPGnQ8U4.png)_Edit Mutual TLS_
   
6. Select up to 5 **Certificate bundles** from your Truststore. Workato uses these bundles to validate client certificates against trusted certificate authorities.
   
7. Add **Certificate validation** rules. Refer to the [Add certificate validation rules](#add-certificate-validation-rules) section for more information.
   
8. Configure the remaining access settings, such as **API collections to include** and optional policies.
   
9. Click **Next** to complete the client creation.
   

Workato checks both the access token and the client certificate for each request. It uses the selected bundles to build trust chains during certificate validation.

### Add certificate validation rules

Use the **Certificate validation** field to enforce identity checks against metadata in the client certificate. You can enter an expression that evaluates fields, such as Common Name (CN), Subject Alternative Name (SAN), or Distinguished Name (DN).

Workato runs this expression at runtime and rejects the request if the certificate fails validation.

> **EXAMPLE USE CASE**
> 
> Use a formula that checks whether the SAN includes the string `"test"` to restrict access to test environments. For example:
> 
> ```ruby
> 
> SAN.include?("test")
> ```
> 
> This expression passes only certificates that include `"test"` in the SAN field.

#### How Workato interprets SAN and DN fields

Workato applies specific formatting rules when it evaluates SAN and DN fields during certificate validation.

The SAN (Subject Alternative Name) field contains an array of strings. Each entry starts with a type prefix, such as `DNS:`, `IP:`, `URI:`, or `Email:`. The formula must include the full value with the correct prefix. For example, to validate an email:

```ruby
SAN.include?("Email:client@example.com")
```

Even if the certificate shows the displays in lowercase, the formula must use an uppercase `"Email"` prefix. Other SAN values, such as DNS, IP, and URI, appear in uppercase and don't require transformation.

For Distinguished Name (DN) values, the format in the formula editor differs from the certificate. A certificate may display the DN in the following X.509 format:

`/C=US/O=Org/CN=RootCA`

The formula editor lists the DN components in reverse order, following the RFC 4514 format:

`CN=RootCA,O=Org,C=US`

Use the RFC 4514 format when you write DN-based validation rules.

## Manage your Truststore

The Truststore lets you upload and manage certificate bundles that Workato uses to validate client certificates during mTLS authentication. Each bundle defines trusted certificate authority (CA) chains to verify client identities during the SSL handshake.

Refer to the [Truststore](/en/api-mgmt/truststore) documentation for more information on how to upload and manage certificate bundles.

### SSL handshake error codes

Workato rejects requests that fail mTLS certificate validation. The following error codes indicate the reason for the failure:

| Error code | Description |
| --- | --- |
| `4016` | Certificate bundle is missing from the client configuration. |
| `4017` | Client certificate is missing from the request. |
| `4018` | Client certificate is invalid. |
| `4019` | Certificate failed the formula validation rule. |
| `4020` | API client doesn't exist or isn't configured. |

---
