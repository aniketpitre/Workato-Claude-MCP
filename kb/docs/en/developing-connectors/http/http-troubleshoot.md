---
url: 'https://docs.workato.com/en/developing-connectors/http/http-troubleshoot.md'
description: >-
  Troubleshoot the Workato HTTP connector to resolve connection failures, SSL
  validation errors, and token expiration with external APIs.
---

# HTTP connector troubleshooting

Use this page to troubleshoot issues when using the HTTP connector in Workato. These guides help you resolve connection failures, SSL validation errors, and token expiration issues with external APIs.

## SSL certificate verification failed

The HTTP connector fails to connect when the target server uses a self-signed or invalid certificate. You can export the certificate chain from the server and upload it in the HTTP connection setup to restore trust.

Refer to the [HTTP SSL certificate verify failed](/en/troubleshooting/http-ssl-certificate-verify-failed-error) guide for more information.

## Microsoft Graph API disconnects after one hour

The connector disconnects from Microsoft Graph after one hour when the access token expires. Include the `offline_access` scope in the connection settings to enable automatic token refresh.

Refer to the [Microsoft Graph API disconnects after one hour](/en/developing-connectors/http/troubleshoot-graph) guide for more information.

## Validate API behavior with Postman

Use Postman to test your request structure and headers before you build the request in Workato. This ensures that the API responds as expected and that the authentication and payload formatting are correctly configured.

---

---
url: >-
  https://docs.workato.com/en/troubleshooting/http-ssl-certificate-verify-failed-error.md
description: >-
  Troubleshoot the SSL certificate verify failed error on the Workato HTTP
  connector by downloading and uploading the full certificate chain.
---

# HTTP SSL certificate verify failed

The **Certificate verify failed** error occurs when you attempt to connect to the [HTTP connector](/en/developing-connectors/http-v2) in Workato without a valid certificate.

```text
Workato::Adapters::OnException::Exception: SSL_connect returned=1 errno=0 state=error: certificate verify failed
```

This error may occur for the following reasons:

- **Certificate is self-signed**: The certificate wasn't issued by a trusted certificate authority.
- **Certificate chain is incomplete**: The target server doesn't return all intermediate certificates required for validation.
- **Certificate is invalid or mismatched**: The certificate is expired or doesn't match the expected domain.

## How the HTTP connector handles certificate errors

The HTTP connector returns a certificate verification error when it can't validate the server's SSL certificate. This occurs when the certificate is self-signed, expired, or missing a complete trust chain.

Most SSL clients, including browsers, Postman, and Workato, reject self-signed or incomplete certificates by default. You must upload the full certificate chain during connection setup to establish trust.

The connector accepts a self-signed certificate only if the full certificate chain is uploaded. If the certificate is expired or doesn't match the server domain, the connector still rejects the connection. You must replace the certificate in these cases to restore secure communication.

## How to troubleshoot

You can [download the certificate chain](#download-the-certificate-chain) from the target server and upload it to the [HTTP connection configuration](#configure-the-http-connection) to establish trust with a self-signed certificate. This lets Workato validate the SSL handshake even when the certificate isn't signed by a public authority.

### Download the certificate chain

Complete the following steps to export the certificate chain from the target server:

1. Open a browser like Firefox and go to a secure page that uses a self-signed SSL certificate. For example: `https://self-signed.badssl.com/`.
   
2. Click **Advanced… > View Certificate** to display the certificate details.
   
   ![Obtain the certificates](/assets/view-certificate.D20nuDoj.png)_Obtain the certificates_
   
3. Click **PEM (chain)** to download the full certificate chain as a `.pem` file.
   
   ![Download the certificate chain](/assets/download-pem-chain.CNNRi6CX.png)_Download the certificate chain_
   
   > **WHY THE FULL CERTIFICATE CHAIN MATTERS**
   > 
   > A certificate chain contains multiple certificates, such as the server certificate, intermediate certificates, and the root certificate. Each certificate must validate the preceding one to establish trust.
   > 
   > Workato can't verify the target server without the complete chain. You must include all certificates to avoid connection errors.
   
4. Open the downloaded file in a text editor. Confirm that it includes one or more certificates, each wrapped in `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.
   
   ![Open the downloaded certificate using a text editor](/assets/open-certificate-in-text-editor.BVnTCCOD.png)_Open the downloaded certificate using a text editor_
   
5. Copy the full certificate content, including all `BEGIN/END` blocks.
   

After you copy the certificate chain, you can [configure the HTTP connection](#configure-the-http-connection) in Workato to complete the setup.

## Configure the HTTP connection

Complete the following steps to configure the HTTP connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `HTTP` on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Complete the required fields. Refer to the [HTTP connection setup](/en/developing-connectors/http/connection-setup) documentation for more information.
   
5. Set the **Use custom TLS/SSL certificate settings** field to **Yes**.
   
6. Paste the downloaded certificate chain in the **TLS server custom CA certificate** field.
   
   > **SEPARATE MULTIPLE CERTIFICATES**
   > 
   > Separate each certificate with a blank line if the chain includes more than one.
   
   ![Paste the downloaded certificate contents](/assets/configure-http-connection.-iDGtn4A.png)_Paste the downloaded certificate contents_
   
7. Click **Connect**.
   

The connector should succeed if the certificate chain is valid and complete.

## Troubleshoot certificate errors

The HTTP connector may return the following error when the certificate chain is incomplete:

```text
SSL_connect returned=1 errno=0 state=error: certificate verify failed (unable to get issuer certificate)
```

The error usually indicates a missing or misconfigured certificate in the chain when the connection already uses custom CA certificates.

Complete the following steps to resolve this error:

1. Ensure that you provide the full certificate chain in the **TLS server custom CA certificate** field. Include the following in order, and separate each certificate with a blank line:
   
   - The server certificate
   - Any intermediate certificates
   - The root certificate
2. Verify the certificate chain configuration. A complete and correctly ordered chain should work with the connector and with external tools such as Postman or cURL.
   
3. Check the certificate chain with a tool such as [KeyCDN SSL Checker](https://tools.keycdn.com/ssl) to confirm that the target server returns a valid and complete chain.
   
   ![Example of a certificate chain check for https://www.google.com](/assets/example-certificate-chain-check.GxkWlvEN.png)_Example of a certificate chain check for `https://www.google.com`_

---
