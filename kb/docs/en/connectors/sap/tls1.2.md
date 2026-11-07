---
url: 'https://docs.workato.com/en/connectors/sap/tls1.2.md'
description: >-
  Configure SAP to interact with the Workato API platform by enabling TLS 1.2,
  importing Workato SSL certificates, and creating an RFC destination.
---

# Configure SAP to interact with the Workato API platform

This article outlines the steps required to enable TLS 1.2 for SAP instances to interact with Workato's API platform.

## What is TLS 1.2

TLS 1.2 is currently the most widely used version of TLS and has several improvements in security compared to TLS 1.1. TLS 1.2 encryption enhancements allow more secure hash algorithms such as SHA-256 as well as advanced cipher suites that support authenticated encryption for other data modes. In 2016, a number of TLS servers were reconfigured to abort/reject TLSv1.0 handshakes, or to require forward secrecy (PFS) cipher suites for access. Workato blocks all incoming web traffic that is not encrypted using TLS 1.2 to ensure your data is kept secure.

## 1\. Recommended configuration required for enabling TLSv1.2

Complete the following steps to enable TLS 1.2 in your SAP instance:

1. Edit your profile through the SAP GUI using the transaction code `RZ10`.
   
2. Navigate to section 7 in the SAP Note [510007](https://me.sap.com/notes/510007) for an updated list of SAP system parameters that must be configured in the `DEFAULT` profile.
   
3. Add the listed parameters and then save and activate the profile.
   
   > **ADD PARAMETERS TO DEFAULT PROFILE**
   > 
   > Ensure that you add these parameters to your `DEFAULT.PFL` through transaction code RZ10, and then save and activate the profile. Ignore the warnings in Netweaver 70x/71x/72x/73x/74x about profile parameters that unknown in transaction codes RZ10 and RZ11. Parameter value assignments in the instance profile take precedence over assignments in `DEFAULT.PFL`. You must remove value assignments for the parameters from all instance profiles in your system for the new value assignments in `DEFAULT.PFL` to take effect.
   

> **CHECK YOUR CONFIGURATION**
> 
> TLS 1.2 might be the configured out-of-the-box in your SAP instance depending on the release version. Check if your SAP instance already has the cipher suites configured as required. If so, you can skip this step.

## 2\. Adding Workato SSL certificates to trust manager

1. Log in to SAP and go to transaction code `STRUST`.
   
2. Select the `SSL client SSL Client (Standard)` option in the sidebar.
   
3. Click the **Import certificate** button.
   
4. Import the following certificate for standard APIM endpoint: [Amazon Root CA 1 cert](https://www.amazontrust.com/repository/). Refer to the [Amazon documentation](https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-pinning) for more information. If you are using a custom APIM domain, you can import the `ISRG root X1` certificate from [Let's Encrypt](https://letsencrypt.org/certificates/).
   
5. Click **Add to Certificate List**.
   

![Import certificates in trust manager](/assets/import_certificates.D9K66dlS.png)_Certificate import process_

## 3\. Create an RFC Destination

RFC destinations enable you to define the domains in which SAP can call RFCs to communicate with Workato. You can configure this to use Workato's API platform or webhook triggers in recipes. Refer to the following steps for information on how to connect to Workato's API management platform.

1. Go to transaction code `SM59` and create an RFC destination of type `G` (HTTP Connections to External Server).
   
2. Complete the following fields:
   
   | Input field name | Recommended Value |
   | --- | --- |
   | RFC Destination | This is the name of your RFC destination which will be called in your RFCs. Remember this title for further steps. |
   | Connection Type | G - HTTP Connection to External Server |
   | Description | Give an accurate description of the RFC destination. Below we named it "Workato API Platform REST endpoints" and gave a link to the API management documentation. |
   | Target Host | For API management, the target Host should be "apim.workato.com" |
   | Service No. | The port for communication. This should be "443". |
   | Path Prefix | This is appended to your target host. The exact path of the endpoint should be configured in an RFC. In this example, we have just entered a single "/" |
   | Security Options (under the Logon & security tab) | SSL should be toggled to Active and SSL certificate toggled to Default SSL Client (Standard) |
   
   ![RFC destination](/assets/RFC_destination.97cajgbl.png)_Sample RFC destination of type G_
   
   ![Logon and security](/assets/logon_and_security.Dor4n1ry.png)_Security options to enable SSL_
   

## 4\. Create an APIM endpoint

API collections are collections of endpoints which correspond to a folder which contains [API recipes](/en/api-mgmt/api-recipes/). API collections allows RFCs in SAP to call and trigger recipes in Workato directly. Refer to [API collection management](/en/api-mgmt/api-collections) for steps on how to create your API collection.

![API collection](/assets/api_collection.D_IqAdb6.png)_API collection_

In this example, the collection is named `sap-connection-demo` with a version `A0001`. The collection is linked it to a folder with a single recipe with the name `Hello, Workato!`. This results in a collection with a single endpoint `https://apim.workato.com/sap-connection-demo-va0001/hello-workato` that has been edited to accept `POST` requests.

---
