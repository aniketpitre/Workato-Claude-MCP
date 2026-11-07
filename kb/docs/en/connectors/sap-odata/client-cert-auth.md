---
url: 'https://docs.workato.com/en/connectors/sap-odata/client-cert-auth.md'
description: >-
  Set up and connect SAP S/4HANA Cloud to Workato using client certificate
  (x509) authentication, including OData service and communication setup.
---

# How to connect to SAP S/4HANA Cloud through Client Certification Authentication on Workato

Complete the following steps to set up OData services for your SAP S/4HANA Cloud instance.

1. Find the OData API for your automation requirements in the [SAP API Business Hub explorer](https://api.sap.com/package/SAPS4HANACloud?section=Artifacts).
   
   ![SAP API explorer](/assets/api_explorer.BOhdewup.png)_SAP API explorer_
   
2. Once you've found a suitable API, click to open it, and find the communication scenario ID. Store this ID for use later on.
   
   ![API communication scenario](/assets/details_communication_scenario.DoubNr09.png)_API details communication_
   
3. Prepare your CA-signed x509 certificate. This certificate must be signed by a CA known to your S/4HANA Cloud backend system. You can verify known CAs by checking the Certificate Trust List in your S/4HANA Cloud system. Find out more about this in this [SAP Blog article](https://blogs.sap.com/2021/12/01/s-4hana-cloud-apis-with-clientcertificateauthentication./) or check out the following guide on how to use SAP Passport as a simple way to create certificates.
   
4. Follow the steps in [Setting up Communication Management](https://blogs.sap.com/2017/11/09/setting-up-communication-management-in-sap-s4hana-cloud/) to complete the following required tasks:
   
   - **Create a Communication User**: Create your communication user using the certificate created in step 3.
   - **Create a Communication System**: Tied to the communication User and set authentication method to SSL Client Certificate.
   - **Create a Communication Arrangement**: tied the communication system and user to the communication scenario.
5. Return to Workato to fill in the [connection fields](#connection-fields).
   

## Sample guide: Use SAP Passport to create certificates for Client Certificate authentication with S/4HANA Cloud

Preparing a CA-signed x509 certificate requires a certificate signed by a trusted CA. SAP passport provides a fast and simple way to generate x509 certificates that are signed by SAP's Cloud Root CA. This guide provides steps to achieve connectivity through this method. However, the certificates you use in production must adhere to your organization's preferred and/or existing vendors which may include SAP.

1. Apply for a [SAP passport](https://support.sap.com/en/my-support/single-sign-on-passports.html?anchorId=section).
   
2. Download the certificate `.pfx` file.
   
3. Convert the `.pfx` file into `.pem` format using OpenSSL. You must have OpenSSL downloaded on your local machine.
   
   - You can use the following command `openssl pkcs12 -in input-cert.pfx -out output-cert.pem -legacy` to create an opaque password and save it for use later on. This command prompts you for your PEM pass phrase.
4. Open the `.pem` file with any plain text editor to inspect the contents. The structure should be similar to the following example:
   
   ```
   Bag Attributes
       localKeyID: 01 00 00 00
       friendlyName: SXXXXXXXXXX
   Key Attributes: <No Attributes>
   -----BEGIN ENCRYPTED PRIVATE KEY-----
   MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w
   ...<redacted>...
   jTG6eYRIAnHR2+4Vto+QxA==
   -----END ENCRYPTED PRIVATE KEY-----
   Bag Attributes
       localKeyID: 01 00 00 00
       friendlyName: S0023610052
   subject=C = DE, O = SAP Trust Community, OU = SAP Service Marketplace, CN = SXXXXXXXXXX
   issuer=C = DE, O = SAP Trust Community, CN = SAP Passport CA G2
   -----BEGIN CERTIFICATE-----
   MIIDjzCCAnegAwIBAgINY3nCYsU77LIAABBWgj
   ...<redacted>...
   NSo4ezWlQtb/44Swg0NFaLpwmn
   -----END CERTIFICATE-----
   Bag Attributes: <No Attributes>
   subject=C = DE, O = SAP Trust Community, CN = SAP Passport CA G2
   issuer=C = DE, L = Walldorf, O = SAP SE, CN = SAP Cloud Root CA
   -----BEGIN CERTIFICATE-----
   MIIFLzCCAxegAwIBAddfzANBgkqhkiG9w0BAQsF
   ...<redacted>...
   hmZooggAg+fCd5ZE4NgC7bAdwj/QYjPmXsolDjABgYUxtGQ=
   -----END CERTIFICATE-----
   Bag Attributes: <No Attributes>
   subject=C = DE, L = Walldorf, O = SAP SE, CN = SAP Cloud Root CA
   issuer=C = DE, L = Walldorf, O = SAP SE, CN = SAP Cloud Root CA
   -----BEGIN CERTIFICATE-----
   MIIFZjCCA06gAwIBAgIQGHcPvmUGa79M6pM42bGdfdsfasdf
   ...<redacted>...
   LvHPhNDM3rMsLu06agF4JTbO8ANYtWQTx0PVrZKJu+8fcIaUp
   -----END CERTIFICATE-----
   ```
   
5. Create a new `.pem` file from the preceding file and save it as `communication_user.pem`. This `.pem` file should only include the certificates without the private key. Based on the preceding example, your new `.pem` file should look like the following example:
   
   ```
   -----BEGIN CERTIFICATE-----
   MIIDjzCCAnegAwIBAgINY3nCYsU77LIAABBWgj
   ...<redacted>...
   NSo4ezWlQtb/44Swg0NFaLpwmn
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   MIIFLzCCAxegAwIBAddfzANBgkqhkiG9w0BAQsF
   ...<redacted>...
   hmZooggAg+fCd5ZE4NgC7bAdwj/QYjPmXsolDjABgYUxtGQ=
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   MIIFZjCCA06gAwIBAgIQGHcPvmUGa79M6pM42bGdfdsfasdf
   ...<redacted>...
   LvHPhNDM3rMsLu06agF4JTbO8ANYtWQTx0PVrZKJu+8fcIaUp
   -----END CERTIFICATE-----
   ```
   
6. Upload the `communication_user.pem` file in the certificate section when creating your communication user.
   
   ![API communication scenario](/assets/cert_upload_comunication_user.WV--pjZq.png)_Certificate upload_
   
7. Set up the rest of your configurations for Communication System and Communication Arrangement on your SAP S/4HANA Cloud instance as you normally do. Ensure that the authentication method for Inbound communication in your Communication system is set to **SSL Client Certificate**.
   
   ![API communication scenario](/assets/cert_communication_system.wufkfUvR.png)_Certificate communication system_
   
8. Return to Workato and fill in the following connection fields:
   
   - Authentication type - `Client certificate(x509)`
   - Client certificate - This is the first certificate in your `.pem` file from step 4. Based on the preceding example it should be similar to following output:
   
   ```
   -----BEGIN CERTIFICATE-----
   MIIDjzCCAnegAwIBAgINY3nCYsU77LIAABBWgj
   ...<redacted>...
   NSo4ezWlQtb/44Swg0NFaLpwmn
   -----END CERTIFICATE-----
   ```
   
   - Private key - This is the private key in your `.pem` file from step 4 Based on the preceding example it should be similar to the following output:
   
   ```
   -----BEGIN ENCRYPTED PRIVATE KEY-----
   MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w
   ...<redacted>...
   jTG6eYRIAnHR2+4Vto+QxA==
   -----END ENCRYPTED PRIVATE KEY-----
   ```
   
   - Passphrase - This is the private PEM pass phrase you created in step 3.
   - CA certificate - This should include the remaining two certificates in your `.pem` file from step 4. You must include both certificates with a blank line in between because it is a chain.
   
   ```
   -----BEGIN CERTIFICATE-----
   MIIFLzCCAxegAwIBAddfzANBgkqhkiG9w0BAQsF
   ...<redacted>...
   hmZooggAg+fCd5ZE4NgC7bAdwj/QYjPmXsolDjABgYUxtGQ=
   -----END CERTIFICATE-----
   
   -----BEGIN CERTIFICATE-----
   MIIFZjCCA06gAwIBAgIQGHcPvmUGa79M6pM42bGdfdsfasdf
   ...<redacted>...
   LvHPhNDM3rMsLu06agF4JTbO8ANYtWQTx0PVrZKJu+8fcIaUp
   -----END CERTIFICATE-----
   ```
   
   - Host, Service, SAP Client - Fill in the required fields. Required fields vary depending on your SAP instance details.

## Connection fields

Complete the following fields in Workato to finish establishing your connection:

> **ODATA VERSIONS**
> 
> We recommend that you create dedicated connections for V2 and V4 APIs.

| Field | Description |
| --- | --- |
| Connection name | Give this connection a descriptive name so you can reuse it in other recipes. |
| Connection type | Choose an on-prem agent if your SAP instance is running in a network that does not allow direct connection. Before attempting to connect, make sure you have an active on-prem agent. Refer to the [On-premise connectivity](/en/on-prem) guide for more information. If you choose to use `Client certificate (x509)` as your authentication type, you must select the option `Cloud`. If `Cloud` is selected, requests are sent directly from Workato's servers. |
| Authentication type | Select either `Basic` or `Client certificate(x509)`. |
| OData version | Select the OData version for the API you plan to use in this connection - `v2` or `v4`. |
| Username | _applicable for authentication type as `Basic`._ The username of the Communication User you created in the preceding steps. |
| Password | _applicable for authentication type as `Basic`._ The password of the Communication User you created in the preceding steps. |
| Client certificate | _applicable for authentication type as `Client certificate(x509)`._ The username of the Communication User you created in the preceding steps. |
| Private key | _applicable for authentication type as `Client certificate(x509)`._ The private key for your Client certificate. |
| Passphrase | _applicable for authentication type as `Client certificate(x509)`._ The passphrase for the private key - if applicable. |
| CA certificate | _applicable for authentication type as `Client certificate(x509)`._ If you used a custom CA to sign your x509 certificate, you must add the CA's certificates here. If there are multiple certificates in a chain, leave a blank line between each certificate. |
| Host | The base path to your SAP OData services. For SAP S/4HANA Cloud, this is found in the Communication Arrangement URL. For example, if the service URL is `https://www.myS4HanaSystem.com/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV`, then your host is `https://www.myS4HanaSystem.com/sap/opu/odata/sap/`. |
| Service | A sample service that you can use to test authentication. This can be the first service that you have configured. For SAP S/4HANA Cloud, the service name can be found in your Communication Arrangement. |
| SAP client | The SAP client to reference. For example, if `https://www.myS4HanaSystem.com/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV?sap-client=800` is the service URL, your SAP client is 800. |

---
