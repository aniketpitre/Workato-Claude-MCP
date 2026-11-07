---
url: 'https://docs.workato.com/en/connectors/hl7.md'
description: >-
  The HL7 connector enables you to send and receive HL7 messages to automate
  healthcare data exchange between clinical and administrative systems.
---

# HL7

[HL7](https://www.hl7.org/), or Health Level Seven, is a set of international standards for the exchange, integration, sharing, and retrieval of electronic health information. HL7 messages are a key component of this standard, and serve as the format for exchanging information between healthcare applications. These messages are structured in a way that allows different systems to understand and interpret the data consistently. You can use HL7 messages for various purposes, including transmitting patient demographic information, laboratory results, clinical observations, and administrative data.

The HL7 Workato connector allows you to send and receive HL7 messages in different versions, and includes a corresponding OPA extension.

## Prerequisites

You must have the following prerequisites to set up an HL7 connection in Workato:

- An on-prem agent (OPA) that uses a [connection profile](/en/on-prem/agents/connection/profile). [Cloud profiles](/en/on-prem/agents/connection/cloud) don't support extensions. Refer to the [Add an agent](/en/on-prem/groups/add-agent) guide for setup instructions.
- Version 17 or higher of the [Java Development Kit (JDK)](#install-the-java-development-kit-jdk), if you're using an OPA version lower than [23.0](/en/on-prem/agents/versions#v23-0).
- The [HL7 extension installed on your OPA](#install-the-hl7-extension).
- The [HL7 connector installed from the community library](#install-the-hl7-connector).

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
   

### Install the HL7 extension

The HL7 extension enables an on-prem agent (OPA) that uses a [connection profile](/en/on-prem/agents/connection/profile) to send and receive HL7 messages. Complete the following steps to install and configure the extension on your OPA:

> **OPA\_DIRECTORY PLACEHOLDER**
> 
> The remainder of this guide uses `[OPA_DIRECTORY]` as a placeholder for the path to your OPA installation directory. The following are common directory locations:
> 
> - **Unix-like operating systems**: `/opt/workato`
> - **Windows**: `C:\Program Files\Workato Agent`
> - **Mac**: Location varies.

1. Complete the following steps to download and extract the HL7 extension package into the `[OPA_DIRECTORY]/ext` folder:
   
   **Windows**
   
   1. Open PowerShell and run the following commands to download and extract the HL7 extension package:
      
      ```shell
      Invoke-WebRequest -Uri "https://workato-opa-extensions.s3.amazonaws.com/hl7-extensions/hl7-extension-latest.zip" -OutFile hl7-extension.zip
      Expand-Archive -Path hl7-extension.zip -DestinationPath "[OPA_DIRECTORY]\ext"
      ```
      
   2. Run the following command to confirm the extraction succeeded:
      
      ```shell
      Get-ChildItem "[OPA_DIRECTORY]\ext" -Filter "hl7-extension.jar"
      ```
      
      The command lists `hl7-extension.jar` if the install completed correctly.
      
   
   **Linux and Mac**
   
   1. Open your CLI and run the following commands to download and extract the HL7 extension package:
      
      ```shell
      $ curl -o hl7-extension.zip https://workato-opa-extensions.s3.amazonaws.com/hl7-extensions/hl7-extension-latest.zip
      $ unzip hl7-extension.zip -d [OPA_DIRECTORY]/ext
      ```
      
   2. Run the following command to confirm the extraction succeeded:
      
      ```shell
      $ ls [OPA_DIRECTORY]/ext | grep hl7-extension.jar
      ```
      
      The command lists `hl7-extension.jar` if the install completed correctly.
      
   
2. Update the `[OPA_DIRECTORY]/conf/config.yml` OPA configuration file with the following information:
   
   ```yml
   server:
     classpath: ext # Set the classpath to the path of the folder where the HL7 extension JAR files are located
   
   extensions:
     # HL7-Profile including a listener to receive messages
     hl7: # Name of the connection profile to be used, when creating a connection
       controllerClass: com.workato.extension.hl7.ExtensionController
       localPort: 1011 # Listening port to receive messages
       webhookURL: https://webhooks.workato.com/users/... # The webhook URL to receive the HL7 message
       remotePort: 1011 # Port to send messages
       remoteHost: localhost # Hostname to send messages
       tls: false
       # Encoding used for sending and receiving messages. Possible values UTF-8, ISO-8859-1, UTF-16, ...
       # encoding: ISO-8859-1
   
   # HL7-Profile WITHOUT a listener, which allows you to send messages only
     hl7_no_listener:
       controllerClass: com.workato.extension.hl7.ExtensionController
       remotePort: 1011
       remoteHost: localhost
       tls: false
       # Encoding used for sending and receiving messages. Possible values UTF-8, ISO-8859-1, UTF-16, ...
       # encoding: ISO-8859-1
   ```
   
3. [Stop](/en/on-prem/agents/shutdown) and [restart](/en/on-prem/agents/run#reconnect-an-agent-to-workato) the OPA for the changes to take effect.
   

### Install the HL7 connector

Complete the following steps to install the HL7 connector from the [community library](https://www.workato.com/browse/connectors):

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

Complete the following steps to create an HL7 connection in Workato:

1. Provide a **Connection name** that identifies which HL7 instance Workato is connected to. ![Connect HL7 on Workato](/assets/hl7-connection.CHhvbPq2.png)_HL7 connection configuration_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Connection type** drop-down menu to select an [on-prem group](/en/on-prem/groups) that contains the HL7 extension.
   
4. Use the **Processing mode** drop-down menu to select the HL7 processing ID you plan to use. Options are: Debugging, Production, and Training.
   
5. Provide your **Profile name**. To receive HL7 messages, the OPA profile **MUST** have a running HL7 listener.
   
6. Click **Connect**.

---
