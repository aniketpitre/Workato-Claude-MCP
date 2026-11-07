---
url: 'https://docs.workato.com/en/connectors/oracle-fusion-cloud.md'
description: >-
  The Oracle Fusion Cloud connector lets you create, update, get, and search
  records, run bulk imports and ESS jobs, and trigger on new or updated records.
---

# Oracle Fusion Cloud

[Oracle Fusion Cloud](https://docs.oracle.com/en/cloud/saas/index.html) is a suite of cloud-hosted applications from Oracle that provides important business functions, including:

- Enterprise resource planning
- Supply chain management
- Sales
- Human capital management

The Oracle Fusion Cloud connector serves as a single point of connectivity for these business functions. You can use this connector for core financial use cases, including:

- Order-to-cash
- Procure-to-pay
- Record-to-report
- Invoicing
- Month-end-reconciliations

## API version

The Oracle Fusion Cloud connector uses the [Oracle Fusion Cloud API v11.13.18.05](https://docs.oracle.com/en/cloud/saas/applications-common/24a/farca/api-set-id-sets-set-id-sets-11.13.18.05.html) and [SOAP Web Services for Financials](https://docs.oracle.com/en/cloud/saas/financials/25c/oeswf/erpintegrationservice-d16510e420.html#Relationships) (no versioning).

## How to connect to Oracle Fusion Cloud

The Oracle Fusion Cloud connector supports the following authentication methods:

- [Basic](#basic)
- [JWT token](#jwt-token)

### Basic

Complete the following steps to connect to Oracle Fusion Cloud using basic authentication:

1. Sign in to Workato.
   
2. Select the project where you plan to store the connection.
   
3. Click **Create > Connection** or press C twice.
   
4. Search for `Oracle Fusion Cloud` and select it as your app.
   
5. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Oracle Fusion Cloud (basic authentication)](/assets/basic.C_sNovQ1.png)_Connect to Oracle Fusion Cloud (basic authentication)_
   
6. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
7. Use the **Auth type** drop-down menu to select **Basic**.
   
8. Enter the username for your Oracle Fusion Cloud account in the **Username** field.
   
9. Enter the password for your Oracle Fusion Cloud account in the **Password** field.
   
10. Enter the subdomain of your specific Oracle Fusion Cloud instance in the **Subdomain** field. For example, `servername.fa.us2.oraclecloud.com`.
    
11. Click **Connect**.
    

### JWT token

The following steps are required to connect to Oracle Fusion Cloud using JWT token authentication:

1. [Generate a X.509 key pair](#generate-a-x-509-key-pair)
2. [Retrieve the certificate fingerprint](#retrieve-the-certificate-fingerprint)
3. [Configure token-based authentication in Oracle Fusion Cloud](#configure-token-based-authentication-in-oracle-fusion-cloud)
4. [Complete setup in Workato](#complete-setup-in-workato)

You can also refer to the Oracle [Configure JWT Authentication Provider](https://www.oracle.com/webfolder/technetwork/tutorials/obe/fusionapps/HCM/JWT_API_Authentication_OBE/html/index.html#GenerateaX.509KeyPair) tutorial for more information about this process.

#### Generate a X.509 key pair

X.509 key pairs are used to establish secure communication by verifying the authenticity of the public certificate.

Complete the following steps to generate a X.509 key pair:

1. Open a new terminal window.
   
2. Run the following command to generate a private key:
   
   ```shell
   openssl genrsa -out private.key 2048
   ```
   
   This command creates a 2048-bit RSA private key and saves it to `private.key`.
   
3. Run the following command to generate an X.509 certificate containing the public key:
   
   ```shell
   openssl req -new -x509 -key private.key -out publickey.cer -days 365
   ```
   
   This command generates a self-signed X.509 certificate (`publickey.cer`) valid for 365 days.
   
4. Open the `private.key` file in a text editor and copy the contents, starting from `-----BEGIN RSA PRIVATE KEY-----` and ending with `-----END RSA PRIVATE KEY-----`.
   
   Store this key securely, as it is required to [complete setup in Workato](#complete-setup-in-workato).
   

#### Retrieve the certificate fingerprint

The certificate fingerprint is a unique identifier used to verify the authenticity of a certificate.

Complete the following steps to retrieve the certificate fingerprint:

1. Run the following `openssl` command to generate the x5t value from the `publickey.cer` file:
   
   ```shell
   openssl x509 -sha1 -in publickey.cer -noout -fingerprint
   ```
   
   The fingerprint output is in hexadecimal format:
   
   ```plaintext
   Fingerprint=00:6D:6F:4A:5F:36:71:10:24:F8:F0:FD:33:89:6D:C5:EB:92:00:0F
   ```
   
2. Convert the fingerprint to base64 format. Replace the string with your actual certificate fingerprint:
   
   ```shell
   echo "00:6D:6F:4A:5F:36:71:10:24:F8:F0:FD:33:89:6D:C5:EB:92:00:0F" | xxd -r -p | base64
   ```
   
   The fingerprint output is in base64 format:
   
   ```plaintext
   AG1vSl82cRAk+PD9M4ltxeuSAA8=
   ```
   
3. Copy the base64-encoded certificate fingerprint and store it securely. This value is required to [complete setup in Workato](#complete-setup-in-workato).
   
   > **REMOVE TRAILING CHARACTERS OR SYMBOLS**
   > 
   > Remove any trailing `=` when you store the fingerprint.
   

#### Configure token-based authentication in Oracle Fusion Cloud

Complete the following steps to configure token-based authentication in Oracle Fusion Cloud:

1. Sign in to Oracle Fusion Cloud.
   
2. Click the **☰ Navigator** icon to expand the sidebar and go to **Tools > Security**.
   
3. Click **API Authentication**.
   
4. Click **\+ Create Oracle API Authentication Provider**.
   
5. Click **Edit**.
   
6. Enter the name of the calling provider in the **Trusted Issuer** field. For example, `Workato`.
   
7. Select the **JWT** checkbox as the **Token Type**.
   
   ![Configure token-based authentication in Oracle Fusion Cloud](/assets/jwt-config.DQfXPdwp.png)_Configure token-based authentication in Oracle Fusion Cloud_
   
8. Click **Save and Close**.
   
9. Click **Inbound API Authentication Public Certificates**.
   
10. Click **\+ Add New Certificate**.
    
11. Enter a name in the **Certificate Alias** field.
    
12. Click **Choose File** and select the public certificate (`publickey.cer`) generated in the [Generate a X.509 key pair](#generate-a-x-509-key-pair) step.
    
13. Click **Save**.
    

#### Complete setup in Workato

Complete the following steps to connect to Oracle Fusion Cloud using JWT token authentication:

1. Sign in to Workato.
   
2. Select the project where you plan to store the connection.
   
3. Click **Create > Connection** or press C twice.
   
4. Search for `Oracle Fusion Cloud` and select it as your app.
   
5. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Oracle Fusion Cloud (JWT token authentication)](/assets/jwt-token.BfN6UZkC.png)_Connect to Oracle Fusion Cloud (JWT token authentication)_
   
6. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
7. Use the **Auth type** drop-down menu to select **JWT token**.
   
8. Enter the [trusted issuer name](#configure-token-based-authentication-in-oracle-fusion-cloud) for your Oracle API authentication in the **Issuer** field.
   
9. Enter the username for your Oracle Fusion Cloud account in the **Username** field.
   
10. Enter the [private key](#generate-a-x-509-key-pair) associated with your public certificate in the **Private key** field.
    
11. Enter your [base64-encoded certificate fingerprint](#retrieve-the-certificate-fingerprint) in the **Certificate fingerprint** field.
    
12. Enter the subdomain of your specific Oracle Fusion Cloud instance in the **Subdomain** field. For example, `servername.fa.us2.oraclecloud.com`.
    
13. Click **Connect**.
    

## Business modules

The Oracle Fusion Cloud connector uses various API endpoints within a single connector to offer connectivity to all business modules in one place. The connector supports the following modules:

- Financials
- Project Management
- Accounting Hub
- Procurement
- Risk Management and Compliance
- Supply Chain Planning
- Inventory Management
- Manufacturing
- Maintenance
- Order Management
- Procurement
- Service Logistics
- Product Lifecycle Management
- Sales Automation
- Customer Data Management
- Subscription Management
- Partner Relationship Management
- Loyalty
- Fusion Service
- Human Resources

Refer to the following Oracle documentation for more information:

- [Oracle Fusion Cloud Applications Suite](https://docs.oracle.com/en/cloud/saas/index.html)
- [REST Framework versions](https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Setting_the_REST_Framework_Version.html)

---
