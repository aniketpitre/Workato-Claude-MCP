---
url: 'https://docs.workato.com/en/connectors/sap/snc-encryption.md'
description: >-
  Enable Secure Network Communications (SNC) encryption between SAP and the
  Workato on-prem agent using the SAP Cryptographic Library.
---

# SAP Connection - Enabling SNC encryption

The SAP Cryptographic Library is the default security product delivered by SAP for performing encryption functions in SAP Systems. You can use it for providing Secure Network Communications (SNC) between various SAP server components or for using the Secure Sockets Layer (SSL) protocol with the SAP application Server. This guide describes how to enable SNC in your own SAP instance and how to configure your on-prem agent to use SNC for encrypted communication.

This process consists of the following steps:

- [Configure SNC on the Workato OPA server](#configure-snc-on-the-workato-opa-server)
- [Configure SNC on SAP system](#configure-snc-on-sap-system)

## Prerequisites for configuring SNC

- SAP Cryptographic Library installed on your SAP system: This is included as part of the standard SAP NetWeaver AS installation. If the SAP Cryptographic Library is not available on your SAP system, you can install it by using a separate installation package. Refer to the SAP Note [1848999](https://me.sap.com/notes/1848999) for more details.
- SAP system profile parameters configured on the system to enable SNC. Refer to [sample profile parameter settings](https://help.sap.com/docs/SAP_NETWEAVER_750/e73bba71770e4c0ca5fb2a3c17e8e229/7a4ca8d131cb4c479e579b3122b8d947.html).
- SAP BASIS privilege or admin access to the SAP system.
- S-User ID with download rights.
- Download and extract SAP CommonCryptoLib on the OPA server. Refer to the [Configure SNC on the Workato OPA server](#configure-snc-on-the-workato-opa-server) section of our documentation for more details on extraction.
- The SAPCAR utility: This is required to extract the contents from the cryptographic library. If this is not present on your system you must download this utility.
- SAP own certificate under the node `SNC SAPCryptolib`. This is extracted from the transaction code `STRUST`. Refer to the [Export the SAP SNC certificate](#_1-export-the-sap-snc-certificate) section of our documentation for more details.

> **COMMONCRYPTOLIB AND SAPCAR**
> 
> You can download the CommonCryptoLib and SAPCAR Utility from SAP [Software Downloads](https://me.sap.com/softwarecenter). To download these packages, the SAP S-USER ID must have valid software download authorizations assigned to it.

## Configure SNC on the Workato OPA server

### 1\. Unpacking the SAP commoncryptolib using SAPCAR on your OPA's server

On the server running your OPA, you will need to unpack the SAP commoncryptolib.

This example demonstrates how to configure SNC on the Workato OPA server for Mac and Windows operating systems. Commands are similar for Linux operating systems.

1. Make the SAPCAR utility executable.  
     
   **Mac:**
   
   ```
   chmod +x SAPCAR_1200-70007727.EXE
   ```
   
   **Windows:**  
   This step can be ignored.
   
2. Rename SAPCAR file (optional).  
     
   **Mac:**
   
   ```
   mv SAPCAR_1200-70007727.EXE sapcar
   ```
   
   **Windows:**  
   Right click on the file to rename.
   
3. Use SAPCAR utility to unpack **SAPCRYPTOLIB**.  
     
   **Mac:**
   
   ```
   ./sapcar -xf SAPCRYPTOLIBP_8554-70002813.SAR
   ```
   
   Expected output:
   
   ```
   SAPCAR: processing archive SAPCRYPTOLIBP_8554-70002813.SAR (version 2.01)
   SAPCAR: 4 file(s) extracted
   ```
   
   **Windows:**
   
   ```
   sapcar -xf SAPCRYPTOLIBP_8554-20011729.SAR
   ```
   
   Expected output:
   
   ```
   SAPCAR: processing archive SAPCRYPTOLIBP_8554-20011729.SAR (version 2.01)
   SAPCAR: 8 file(s) extracted
   ```
   
4. Create a folder with the name `sec` in your OPA server. This file is used to hold files required for SNC connections. Move the files that were extracted in Step 3 to this folder.
   
   > **LOCATION OF SEC FOLDER**
   > 
   > Place the `sec` folder inside your OPA installation directory.
   

* * *

### 2\. Set the `SECUDIR` and `SNC_LIB` variables

Set the `SECUDIR` and `SNC_LIB` environment variables. These variables tell the server where to look for the certificates required for an SNC encrypted login and which file is used as the SAP cryptographic library.

> **ENVIRONMENT VARIABLES**
> 
> Start OPA from same terminal where you are setting these environment variables. Alternatively, ensure the `echo` command reflects the correct values in the terminal from where you intend to start the OPA. You can set these variables in the `.bashrc` file to save the values permanently.

1. Set the SECUDIR and SNC\_LIB variables.
   
   > **ENVIRONMENT VARIABLE SNC\_LIB**
   > 
   > The value of the environment variable `SNC_LIB` varies based on the operating system you use. For example:
   > 
   > - Mac: `libsapcrypto.dylib`
   > - Windows: `sapcrypto.dll`
   > - Linux:`libsapcrypto.so`
   
   **Mac:**
   
   ```
   export SECUDIR=<directory path for sec folder>
   export SNC_LIB=<OPA installation directory>/sec/libsapcrypto.dylib
   ```
   
   **Windows:**  
   
   1. Right click **This PC**, select **properties** and go to **Advanced system settings**.
      
   2. Under the **Advanced** tab, click **Environment Variables**. ![Env variable](/assets/env-var-win.DEtE4Hwm.png)
      
   3. Add new System variables: `SNC_LIB` and `SECUDIR`.
      
2. Confirm if the environment variables are set correctly.  
     
   **Mac:**
   
   ```
   echo $SECUDIR
   echo $SNC_LIB
   ```
   
   **Windows:**  
   Ensure that `SNC_LIB` and `SECUDIR` are included in the list of **System variables**.
   

* * *

### 3\. Generate client certificate

The steps in this section outline the process to create a client certificate which is imported into your SAP system. Your OPA uses the client certificate to verify its identity. SAP also requires a copy of the certificate to trust your OPA's attempt to connect and this is done using `sapgenpse`.

1. Create a self-signed certificate using `sapgenpse`. You are prompted to provide a PSE PIN and the distinguished name of your PSE. In this example, we have given it the canonical name `workato`.
   
   > **PSE PIN AND DISTINGUISHED NAME**
   > 
   > Avoid using special characters and spaces while setting the canonical name and PSE PIN.
   
   **Mac:**
   
   ```
   ./sapgenpse gen_pse -v -p <OPA installation directory>/sec/workato.pse
   ```
   
   **Windows:**
   
   ```
   sapgenpse gen_pse -v -p <OPA installation directory>\sec\workato.pse
   ```
   
   Expected output:
   
   ```
   Got absolute PSE path "<OPA installation directory>/sec/workato.pse".
   Please enter PSE PIN/Passphrase: ************
   Please reenter PSE PIN/Passphrase: ************
   get_pse: Distinguished name of PSE owner: CN=workato
    Supplied distinguished name: "CN=workato"
    Creating PSE with format v2 (default)
    succeeded.
    certificate creation... ok
    PSE update... ok
    PKRoot... ok
   Generating certificate request... ok.
   Certificate Request:
    Signed Part:
     Subject:                             CN=workato
     Key:                                 rsaEncryption (2048 bits)
     Public key fingerprint (MD5):        80:A7:CE:BC:19:A1:4E:E8:63:1F:77:F9:BC:8F:E8:4B
     Attributes:                          None
    Signature:
     Signature algorithm:                 sha256WithRsaEncryption (1.2.840.113549.1.1.11)
     Signature:                           <Not displayed>
   
   PKCS#10 certificate request for "<OPA installation directory>/sec/workato.pse":
   
   -----BEGIN CERTIFICATE REQUEST-----
   MIICVzCCAT8CAQAwEjEQMA4GA1UEAxMHd29ya2F0bzCCASIwDQYJKoZIhvcNAQEB
   BQADggEPADCCAQoCggEBAM1XnlnelNn28WjlPtDd+a2pkOXcOMGoyuO8VlkPHp/r
   RxzgZO11ac3fYgmr2iuvWwTFh/cNy+9xoXLlS374m103dFJfICBkH0zus4h2DU33
   S+imU57wGyw2YzkptqctA8vYEZFQVnNdjxRcHpsS6RkYeEb8AFs5NOu5ibJpX6gq
   i2+CQkiSzFmTpcEgg5Inr42lZxWMflHbx233M9a9UNF5x+Mrj9VuVTV+r2GaYulq
   8VrjlD9LXtV8ZPzEv/GAi/UILtsAdwaSdB2mawS8MA2R4BICVpk2CZraDOMQpYmw
   YTvkrUV/0+nQ8GWZwMqQ8+fsJUPKjyGCam4J8aSkx4MCAwEAAaAAMA0GCSqGSIb3
   DQEBCwUAA4IBAQCmXXO0MSgWexOTN/3AIRgljnRnz5/VsamVV01KOV460AC3Eh67
   N14u6pjKbJUe29RNEpML8DbmDnsHQYm8WPT5GnTdt08m7M1csswSq4dagIkUgJB5
   LFT/oofJ3V7m/idN9AOb+LI9kEsFh6Z2LBC2umP45qSyWI8QFCsF6a0FB7Xy1Pok
   voOODcA8KTkhN24hkKtHkZNKoFIkniSATvcJmu10iVKuYmeQem5WnfOPmH4Gpf7p
   WMlgnEqEvhmy+MdLWubl6mpiBQfPvj9u9jJ/W2BO7kCfVzfFs9WxEKCibh410ReT
   SREwV95ePEjIZ4H//txpYgDbzc42Zei8odT0
   -----END CERTIFICATE REQUEST-----
   ```
   
   You should now see a `workato.pse` file in your `sec` folder.
   
2. Use this PSE file to create a client certificate `workato.crt` file in your `sec` folder.  
     
   **Mac:**
   
   ```
   ./sapgenpse export_own_cert -v -p <OPA installation directory>/sec/workato.pse -o <OPA installation directory>/sec/workato.crt -x <PSE PIN>
   ```
   
   **Windows:**
   
   ```
   sapgenpse export_own_cert -v -p <OPA installation directory>\sec\workato.pse -o <OPA installation directory>\sec\workato.crt -x <PSE PIN>
   ```
   
   Expected output:
   
   ```
   Opening PSE "<OPA installation directory>/sec/workato.pse"...
    No SSO credentials found for this PSE.
    PSE (v2) open ok.
    Retrieving my certificate... ok.
    Writing to file (PEM-framed base64-encoded)... ok.
   ```
   
3. Assign the credentials of the current OS user to this PSE to add SSO credentials to the PSE.
   
   > **OS USER**
   > 
   > Your OS username can be different from your SAP username. This should be the name of your user in your server, for example, `ec2-user`, or `root`.
   
   **Mac:**
   
   ```
   ./sapgenpse seclogin -p <OPA installation directory>/sec/workato.pse -O [your_os_username]
   ```
   
   **Windows:**
   
   ```
   sapgenpse seclogin -p <OPA installation directory>\sec\workato.pse -O [your_os_username]
   ```
   
   Expected output:
   
   ```
   running seclogin with USER="<OS user>"
   Please enter PSE PIN/Passphrase: ************
   Added SSO-credentials for PSE "<OPA installation directory>/sec/workato.pse"
   ```
   

* * *

### 4\. Import SAP system certificate to the PSE

To import SAP system certificate, we require the following file:

1. The `EH8.crt` certificate file retrieved in step 1 of the [Export the SAP SNC certificate](/en/connectors/sap/snc-encryption#_1-export-the-sap-snc-certificate) section which is the own certificate of your SAP system. This step allows the PSE to know that the SAP system is trusted.  
     
   **Mac:**
   
   ```
   ./sapgenpse maintain_pk -p <OPA installation directory>/sec/workato.pse -a <OPA installation directory>/sec/EH8.crt
   ```
   
   **Windows:**
   
   ```
   sapgenpse maintain_pk -p <OPA installation directory>\sec\workato.pse -a <OPA installation directory>\sec\EH8.crt
   ```
   
   Expected output:
   
   ```
   Please enter PSE PIN/Passphrase: ****
    maintain_pk for PSE "<OPA installation directory>/sec/workato.pse"
   ----------------------------------------------------------------------------
   Subject               :   CN=EH8, OU=I0021153659, OU=SAP Web AS, O=SAP Trust Community, C=DE
   
    PKList updated (1 entries total, 1 newly added)
   ```
   
2. In the `sec` folder, run the following command to check if the `EH8.crt` has been linked successfully. Use `sapgenpse` to check if the certificate from SAP has been linked successfully.  
     
   **Mac:**
   
   ```
   ./sapgenpse maintain_pk -p <OPA installation directory>/sec/workato.pse -l -v
   ```
   
   **Windows:**
   
   ```
   sapgenpse maintain_pk -p <OPA installation directory>\sec\workato.pse -l -v
   ```
   
   Expected output:
   
   ```
   Opening PSE "/Users/sidhantmahajan/Downloads/SNC/sec/workato.pse"...
    PSE (v2) open ok.
    retrieving PKList
   PKList:
    Version:                              1
    Subject:                              CN=EH8, OU=I0021153659, OU=SAP Web AS, O=SAP Trust Community, C=DE
    Issuer:                               CN=EH8, OU=I0021153659, OU=SAP Web AS, O=SAP Trust Community, C=DE
    Serial Number:                        0A:20:23:03:30:09:34:01
    Validity not before:                  Thu Mar 30 15:04:01 2023 (230330093401Z)
    Validity not after:                   Fri Jan  1 05:30:01 2038 (380101000001Z)
    Public key:                           rsaEncryption (2048 bits)
    Public key fingerprint (MD5):         34:BA:58:F3:8D:09:39:07:CF:AF:46:A6:3B:8E:05:C6
    Public key fingerprint (SHA256):      1C:47:70:FA:7C:9D:7A:77:FE:94:3C:D6:65:F5:BE:0D:15:86:01:DA:16:52:43:B0:E6:2D:21:A2:B5:4F:CE:AB
    Signature algorithm:                  sha256WithRsaEncryption (1.2.840.113549.1.1.11)
    Certificate fingerprint (MD5):        6B:74:E9:9C:44:6B:68:CB:34:CF:FE:9F:5D:8C:AB:78
    Certificate fingerprint (SHA1):       E3:D7:DF:21:9C:76:19:AA:C3:1F:CA:3C:97:F1:94:68:50:7F:EA:3D
    Certificate fingerprint (SHA256):     0D:F1:63:43:08:41:B1:B5:6F:F8:A4:95:C8:6D:BE:E3:DD:38:5F:70:03:B8:63:6F:D4:8E:00:25:3C:9A:A2:5D
   ```
   
3. In the `sec` folder, run the following commands to check if credentials are correct by checking the client certificate, key, and SSO mapping.  
     
   **Mac:**
   
   ```
   ./sapgenpse seclogin -p <OPA installation directory>/sec/workato.pse -O [your_os_username] -l
   ./sapgenpse seclogin -p <OPA installation directory>/sec/workato.pse -l
   ```
   
   **Windows:**
   
   ```
   sapgenpse seclogin -p <OPA installation directory>\sec\workato.pse -O [your_os_username] -l
   sapgenpse seclogin -p <OPA installation directory>\sec\workato.pse -l
   ```
   
   Expected output:
   
   ```
    running seclogin with USER="<OS user>"
     0 (LPS:OFF): CN=workato
             (LPS:OFF): <OPA installation directory>/sec/workato.pse
     1 readable SSO-Credentials available
     for PSE-file "<OPA installation directory>/sec/workato.pse"
   ```
   

* * *

## Configure SNC on SAP system

### 1\. Export the SAP SNC certificate

Export the SAP Certificate from the SAP application server. This certificate is then imported to the OPA.

1. Log in to SAP GUI and go to the transaction code `STRUST`.
   
2. Select the SNC SAPCryptolib node and double click the certificate in the `Own Certificate` section. ![Export certificate](/assets/snc-support-nav-7.BBbUxdeh.png)
   
3. Click the **certificate export** icon. Then, select **Base64** format. In our example, we named it `EH8.crt` which is inline with our system ID of the SAP system. ![Export certificate](/assets/snc-support-nav-6.PmqkBest.png)
   

* * *

### 2\. Import the client certificate

This section outlines the steps required to import the client certificate generated on the OPA side into SAP.

1. Go to the transaction code `STRUST` and select the node `SNC SAPCrytolib`.
   
2. Ensure that you are in edit mode and click the **certificate import** icon, located next to the **certificate export** icon as shown in the figure in the previous section.
   
3. Import the client certificate `workato.crt` which was generated on the OPA side.
   
4. Click **Add to certificate list** and **save**.
   
   ![Set password](/assets/snc-support-nav-5.B88pJoSD.png)
   

* * *

### 3\. Mapping client certificate to an integration user in SAP

This section demonstrates how to map the client certificate to an integration user which is used to communicate with Workato.

1. Go to transaction code `SU01`, enter the name of the integration user which is being used to communicate with Workato.
   
2. Go to `SNC` tab, enter in the SNC name and click **save**. The value would be the distinguished name which we defined while generating the client certificate with `p:` prepended (technically referred as **canonical name**). In this example, it means the SNC name is `p:CN=workato`.
   
   ![SNC tab](/assets/snc-tab.CkLD9KBZ.png)
   
3. Go to transaction code `SM30`, enter the table name `VUSREXTID`.
   
4. Maintain the External ID type `DN` and `X` where **External ID** would be the distinguished name of the client certificate with the name of the integration user in the **User** field. ![user mapping](/assets/user-mapping_2.Cd3w-QGy.png)
   

* * *

### 4\. Alter your RFC destination (if you use the new IDoc trigger)

To use the New IDoc trigger through secured communication, you must enable SNC for the RFC destination dedicated to Workato.

1. Go to transaction code `SM59`.
   
2. Navigate to the RFC destination dedicated to Workato.
   
3. Under the `Logon & Security` tab, select the `SNC` button under the `Security Options` section.
   
4. Enter in the quality of protection. In our example, this is set to `3`.
   
5. Enter the canonical name of the client certificate and click **save**. In our example, this is `p:CN=workato`.
   

![SNC enabled on RFC destination](/assets/snc-RFC.b36mQrOk.png)

* * *

### Connection fields

To establish the connection in Workato, configure the [SAP profile](/en/connectors/sap/opa-configure#sap-profile-create) to reflect the SNC properties. The following important properties are additionally required on the Workato connection page to establish a secured connection:

- **Quality of protection**: Enables secured network communication.
- **Sapcrypto library path**: Provide the filesystem path to `libsapcrypto.so` (Linux), `libsapcrypto.dylib` (Mac), `sapcrypto.dll` (Windows).
- **SNC partner name**: Canonical name of the SAP own certificate extracted in step 1 of this [section](/en/connectors/sap/snc-encryption#_1-export-the-sap-snc-certificate).
- **SNC name**: Canonical name of the client certificate.

* * *

### Summary

Congratulations! You have set up encrypted connections between your OPA and your SAP system. This enables end-to-end encryption for all communication between SAP and Workato. This can be verified in transaction code `SMGW`. In the toolbar, navigate to **Goto** and click **Logged on Clients** where on double clicking across your connection with the program ID used for the SNC connection, verify the property **LOCAL** across which you should see port **48XX** reflecting secure communication. Refer to the official SAP documentation on ports for validating the [secure SNC port range](https://help.sap.com/docs/Security/575a9f0e56f34c6e8138439eefc32b16/616a3c0b1cc748238de9c0341b15c63c.html).

![port check](/assets/gateway-monitor.b2xyyxT7.png)

* * *

## Troubleshooting

Use the following sections to resolve issues:

### Unable to load GSS-API shared library

The following error may display when connecting to SAP:

```
SncPDLInit()==SNCERR_INIT
Unable to load GSS-API Shared Library
named "~/sec/libsapcrypto.so"
```

Check your config profile in your OPA. Ensure that the `sapcrypto_library_path` parameter has the **full path** to your `libsapcrypto` library.

### Peer certificate verification failed

You may receive the following error in your OPA logs when connecting to SAP:

```
A2200210 Peer certificate verification failed
```

Check your trust manager configurations under Tcode STRUST. Ensure that your OPA's certificate has been imported **and saved** in your certificate list.

### Could not find a suitable SAP use

You may receive the following error in your OPA logs when connecting to SAP:

```
Could not find a suitable SAP user for the SNC name of the caller
```

Check that your `SECUDIR` environment variable is set. You can verify this with `echo $SECUDIR`. Check the SNC name of your user in SAP under Tcode `SU01` next, if the `SECUDIR` environment variable is set.

### No credentials were supplied

You may receive an error similar to the following example when connecting to SAP:

```
Caused by: com.sap.conn.jco.JCoException: (102) JCO_ERROR_COMMUNICATION: Establishing connection to communication partner failed at CPIC-CALL: CMRCV(coxread) on convId: 45790358 with rc: 20
LOCATION    CPIC (TCP/IP) with Unicode
ERROR       GSS-API(maj): No credentials were supplied
            Unable to establish the security context
```

Complete the following steps to resolve this error:

1. Verify that the `SECUDIR` environment variable is set correctly.
   
2. Verify that the `cred_v2` file is in the directory specified in `SECUDIR`.
   
3. Verify that the `cred_v2` file contains credentials for the PSE to be accessed.
   
4. Verify that the credentials in `cred_v2` for the PSE are readable for the active user.
   
5. Verify that the PSE is available in the location indicated by the credentials.
   
6. Verify that the certificates on the client side and server side are configured properly.

---
