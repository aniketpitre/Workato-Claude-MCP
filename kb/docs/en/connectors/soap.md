---
url: 'https://docs.workato.com/en/connectors/soap.md'
description: >-
  The SOAP connector is a universal connector that lets you connect to any web
  service described by a WSDL, with fields generated automatically.
---

# SOAP universal connector

Workato's [SOAP connector](https://app.workato.com/custom_adapters/424195/details?community=true) is a universal connector that lets you connect to any web service using WSDL descriptions. Use the SOAP connector if there isn't a web service-specific connector available and the web service provides a WSDL description.

Supported web service standards include:

- SOAP protocol bindings versions 1.1 and 1.2
- WSDL version 1.1 and XML Schema/XSD
- HTTP transport version 1.1 and 2.0

![Example SOAP recipe](/assets/soap-recipe.CglyCqfK.png)_Example SOAP recipe_

## How the SOAP connector works

The SOAP connector uses an on-prem agent to access web services in both private networks and in the cloud. The agent's SOAP extension uses [Apache CXF](https://cxf.apache.org/), which requires a JDK (Java Development Kit).

![SOAP architecture](/assets/soap-architecture.Clsp94eN.png)_SOAP architecture_

## Prerequisites

You must have the following prerequisites to set up a SOAP connection in Workato:

- An on-prem agent (OPA) that uses a [connection profile](/en/on-prem/agents/connection/profile). [Cloud profiles](/en/on-prem/agents/connection/cloud) don't support extensions. Refer to the [Add an agent](/en/on-prem/groups/add-agent) guide for setup instructions.
- Version 17 or higher of the [Java Development Kit (JDK)](#install-the-java-development-kit-jdk), if you're using an OPA version lower than [23.0](/en/on-prem/agents/versions#v23-0).
- The [SOAP extension installed on your OPA](#install-opa-extension).
- The [SOAP connector installed from the community library](#install-soap-connector).

### Install the Java Development Kit (JDK)

OPA versions lower than 23.0 require version 17 or higher of the [Java Development Kit (JDK)](https://adoptium.net).

Refer to [JDK distributions](https://whichjdk.com/#distributions) to install the JDK, or complete the following steps to validate an existing JDK installation:

> **JDK\_DIRECTORY PLACEHOLDER**
> 
> The remainder of this guide uses `[JDK_DIRECTORY]` as a placeholder for the path to your JDK installation directory. The JDK installs in the following locations by default:
> 
> - **Linux**: `/usr/lib/java`
> - **Ubuntu**: `/usr/share/java/`
> - **Windows**: `C:\Program Files\Java\jdk-<release>`
> - **Mac**: Location varies based on distribution. For example: `/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home`

1. Confirm the installation succeeded by listing the JDK folder contents.
   
   **Windows**
   
   Run the following command in PowerShell:
   
   ```shell
   Get-ChildItem "[JDK_DIRECTORY]"
   ```
   
   **Linux and Mac**
   
   Run the following command:
   
   ```shell
   $ ls [JDK_DIRECTORY]
   bin  conf  include  jmods  legal  lib  release
   ```
   
2. Check for the `javac` binary to confirm that the installation is a JDK and not a JRE.
   
   **Windows**
   
   Run the following command in PowerShell:
   
   ```shell
   Get-ChildItem "[JDK_DIRECTORY]\bin" -Filter "javac*"
   ```
   
   **Linux and Mac**
   
   Run the following command:
   
   ```shell
   $ ls [JDK_DIRECTORY]/bin/java*
   bin/java  bin/javac  bin/javadoc  bin/javap
   ```
   
3. Confirm the JDK is version 17 or higher.
   
   **Windows**
   
   Run the following command in PowerShell:
   
   ```shell
   & "[JDK_DIRECTORY]\bin\javac.exe" -version
   ```
   
   **Linux and Mac**
   
   Run the following command:
   
   ```shell
   $ [JDK_DIRECTORY]/bin/javac -version
   javac 17.0.11
   ```
   

### Install the OPA extension

The SOAP extension enables an OPA that uses a [connection profile](/en/on-prem/agents/connection/profile) to communicate with SOAP web services. Complete the following steps to install and configure the extension on your OPA:

> **OPA\_DIRECTORY PLACEHOLDER**
> 
> The remainder of this guide uses `[OPA_DIRECTORY]` as a placeholder for the path to your OPA installation directory. The following are common directory locations:
> 
> - **Unix-like operating systems**: `/opt/workato`
> - **Windows**: `C:\Program Files\Workato Agent`
> - **Mac**: Location varies.

1. Complete the following steps to download and extract the latest SOAP extension package into the `[OPA_DIRECTORY]/ext` folder:
   
   Download the SOAP extension package
   
   **Windows**
   
   1. Open PowerShell and run the following commands to download and extract the SOAP extension package:
      
      ```shell
      Invoke-WebRequest -Uri "https://workato-opa-extensions.s3.amazonaws.com/soap-extensions/soap-extension-latest.zip" -OutFile soap-extension.zip
      Expand-Archive -Path soap-extension.zip -DestinationPath "[OPA_DIRECTORY]\ext"
      ```
      
   2. Run the following command to list the SOAP extension files in `[OPA_DIRECTORY]\ext`:
      
      ```shell
      Get-ChildItem "[OPA_DIRECTORY]\ext" -Filter "*soap_extension*"
      ```
      
      The command lists both JAR files if the install completed correctly:
      
      ```text
      soap_extension.jar
      soap_extension_client.jar
      ```
      
   
   **Linux and Mac**
   
   1. Open your CLI and run the following commands to download and extract the SOAP extension package:
      
      ```shell
      $ curl -o soap-extension.zip https://workato-opa-extensions.s3.amazonaws.com/soap-extensions/soap-extension-latest.zip
      $ unzip soap-extension.zip -d [OPA_DIRECTORY]/ext
      ```
      
   2. Run the following command to list the SOAP extension files in `[OPA_DIRECTORY]/ext`:
      
      ```shell
      $ ls [OPA_DIRECTORY]/ext | grep soap_extension
      ```
      
      The command lists both JAR files if the install completed correctly:
      
      ```text
      soap_extension.jar
      soap_extension_client.jar
      ```
      
   
   > **INSTALLATION ALTERNATIVES**
   > 
   > Alternatively, you can [download and install the package manually](https://workato-opa-extensions.s3.amazonaws.com/soap-extensions/soap-extension-latest.zip), or refer to the [soap extension library](https://workato-opa-extensions.s3.amazonaws.com/index.html?prefix=soap-extensions/) to install older versions.
   
2. Complete the following steps to update the `[OPA_DIRECTORY]/conf/config.yml` configuration file:
   
   Configure the OPA and the extension
   
   1. Open `[OPA_DIRECTORY]/conf/config.yml` and set the `classpath` to the folder that contains the SOAP extension JAR files. For example, the following edit sets a relative path to the `ext` folder:
      
      ```yaml
      server:
         classpath: ext
      ```
      
   2. Add the following to register the SOAP extension:
      
      ```yaml
      extensions:
         soap:
            controllerClass: com.workato.extension.soap.ExtensionController
      ```
      
   3. Add the following to set the JDK path explicitly if it's stored somewhere other than the `JDK_HOME` environment variable or the `jdk.home` system property, which the extension checks by default:
      
      ```yaml
      extensions:
         soap:
            controllerClass: com.workato.extension.soap.ExtensionController
            jdkHome: [JDK_DIRECTORY]
      ```
      
   
3. [Stop](/en/on-prem/agents/shutdown) and [restart](/en/on-prem/agents/run#reconnect-an-agent-to-workato) the OPA for the changes to take effect.
   

### Install the SOAP connector

Complete the following steps to install the SOAP connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

Complete the following steps to create a SOAP connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `SOAP` on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Setting up a SOAP connection](/assets/soap-new-connection.2K9LNX7J.png)_Setting up a SOAP connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select an [on-prem group](/en/on-prem/groups) that contains the SOAP extension.
   
6. Use the **WSDL source type** drop-down menu to select how to provide the WSDL file. The WSDL file defines the web service's interfaces, operations, and data types. Options include the following:
   
   - **WSDL URL**: The OPA loads the WSDL file from the URL. Typically, the URL is the SOAP web service with `WSDL` as a query string. For example: `https://<hostname>/<path>?WSDL`
     
   - **File content**: Enter the content of the WSDL file directly. This must be a valid XML document that defines the SOAP web service.
     
   - **File path**: Enter the absolute or relative path of the WSDL file on the OPA. If it's relative, specify the absolute path of the directory containing the WSDL file in the `extensions.soap.wsdlBase` section of the `config.yml` [OPA configuration file](/en/on-prem/agents/connection/profile#basics). For example:
     
     ```yaml
     extensions:
       soap:
         wsdlBase: /opt/workato/ext/wsdl
     ```
     
7. Optional. Use the **Require dedicated login operation** drop-down menu to select whether the service requires a separate login call for subsequent operations. This typically isn't required. Defaults to `No`. Refer to [Dedicated login operation](/en/connectors/soap/authentication#login-operation) for more information.
   
8. Use the **Authentication type** drop-down menu to select an authentication method. Refer to the SOAP [authentication types](/en/connectors/soap/authentication#authentication-types) guide for more information.
   
9. Optional. Expand the **Advanced options** section and complete the following steps to configure the optional fields:
   
   Configure advanced options
   
   1. Enter an address to send SOAP messages to in the **Web service address** field. Use this field if the WSDL file doesn't define the service address, or to override it.
      
   2. Enter the maximum depth of input and output fields in the **Max schema depth** field. This determines how deep the connector traverses the schema tree and prevents overly expansive schema structures. Some fields may not be shown if the actual depth exceeds this value. Defaults to 15.
      
   3. Enter the maximum number of recursions for a particular type within the schema structure in the **Max type recursion** field. This prevents infinite loops when a type is nested within itself. Defaults to 3.
      
   4. Use the **Record SOAP envelopes** drop-down menu to select whether to record request and response SOAP envelopes and make them available in the job logs. Use this option for debugging.
      
   5. Use the **Trust all certificates** drop-down menu to select whether to skip verification of the certificate the server presents. We recommend leaving this disabled in production environments.
      
   6. Use the **Trust all hostnames** drop-down menu to select whether to skip verification of the hostname of the certificate the server presents. We recommend leaving this disabled in production environments.
      
   7. Enter a pattern in the **Datetime format** field if the service requires a custom datetime format. Defaults to `yyyy-MM-dd'T'HH:mm:ss'Z'` (ISO 8601 in UTC). For example, `2023-07-04T22:00:00.000Z`. Refer to the [Java](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#patterns) documentation for datetime pattern examples.
      
   8. Enter the length of the connection timeout to use in seconds in the **Connect timeout** field. Defaults to 10 seconds.
      
   
10. Click **Connect**.
    

> **FURTHER READING**
> 
> - [SOAP authentication](/en/connectors/soap/authentication)
> - [Execute operation action](/en/connectors/soap/execute-operation-action)

---
