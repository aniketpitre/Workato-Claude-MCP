---
url: 'https://docs.workato.com/en/connectors/sap/sap-troubleshooting.md'
description: >-
  Troubleshoot common SAP connector setup and connection issues, including agent
  startup errors, JCo failures, and missing IDocs, plus debug logging.
---

# SAP troubleshooting guide

Use this guide to troubleshoot issues when you set up the SAP connector.

## Enable debug logging

We recommend that you enable debug logging in your `config.yml` file if you experience issues when you set up the SAP RFC connector. This enables you to capture detailed error information during connection attempts. For example:

```yaml
logging:
  com.workato.agent.sap: DEBUG
```

Refer to the [Common issues](#common-issues) and [Error messages](#error-codes) sections to identify and resolve problems.

## Common issues

You may encounter the following issues when setting up or connecting to SAP with a Workato on-prem agent:

### Agent fails to start

The agent may display the following error during startup:

```text
JCo initialization failed with java.lang.UnsatisfiedLinkError: C:\Program Files\Workato Agent PROD\lib_ext\sapjco3.dll: Can't find dependent libraries
```

On Windows platforms, JCo 3.1 requires you to install the Microsoft Visual Studio 2015-2022 C/C++ runtime libraries on your agent server. If these libraries aren't present, you must download and install the latest `Microsoft Visual C++ 2015-2022 Redistributable Package` from the [Microsoft knowledge base article](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022). Select the package that matches your locale and JVM bit-width (x64 for 64-bit operating systems or x86 for 32-bit operating systems).

### Agent fails to connect to SAP

Check the OPA logs to find the specific error. Learn how to [enable debug logging](#debug-logging-enable).

### IDocs missing from dropdown list

You must [configure the required IDoc in your SAP system](/en/connectors/sap/configure-idoc-sap) before Workato can display them in a drop-down list.

By default, Workato refreshes IDoc metadata every 24 hours. To change this interval, set `metadata_refresh_interval` in the [SAP connection profile](/en/on-prem/agents/connection/profile#sap-profile).

[Contact Customer Success](https://support.workato.com) if the issues continue.

### SAP RFC fails to call Workato APIs

Your SAP system configuration may not support TLS 1.2, which is required for incoming connections to Workato. Enable TLS 1.2 support in your SAP environment to complete the connection. Refer to the [Configure SAP to interact with the Workato API platform](/en/connectors/sap/tls1.2) guide for setup instructions.

## Error messages

You may encounter the following errors when establishing a SAP connection. Use this section to identify the cause and resolve the issue.

### java.lang.UnsatisfiedLinkError: no sapjco3 in java.library.path

This error occurs when the agent uses a Java connector package that doesn't match the host operating system. Ensure that you download and install the correct SDK version.

On Mac, the agent raises this error if `libsapjco3.dylib` doesn't exist in the `lib_ext` folder.

### Classpath entry lib/sap-connector-X.X.X.jar not found, skipped.

This error appears on Mac when the `sap-connector-X.X.X.jar` file is moved to the `lib_ext` folder. To avoid classpath issues, keep the file in its default location.

### Registration of tp <Program's name> from host ??? not allowed

This error may indicate issues in the `reg_info` or `sec_info` files. Follow [SAP note 1850230](https://userapps.support.sap.com/sap/support/knowledge/en/1850230) and complete the following steps to disable all checks, otherwise maintain the ACL entries in `reginfo` and `secinfo` files:

1. Move or rename the `reginfo` and `secinfo` files.
   
2. Confirm the OS-level path matches the values `gw/reg_info` and `gw/sec_info` in RZ11.
   
3. Set the value of the `gw/reg_no_conn_info` parameter to `0`.
   
4. Set the value of the `gw/acl_mode` parameter to `0`.
   
5. Ensure the SAP server (`gwhost`) is accessible from the agent host. Ping the server's IP address from Terminal or Command Prompt to verify connectivity.
   

### java.lang.NoClassDefFoundError: com/sap/conn/jco/JCoException

This error occurs when the SAP Java Connector (JCo) library is missing or not correctly referenced in the agent classpath. Complete the following steps to resolve this:

1. Download the SAP JCo libraries that match your operating system. For example, download the Windows version if the agent runs on Windows. Refer to the [SAP Java Connector](https://support.sap.com/en/product/connectors/jco.html) page for more information.
   
2. Add the following files to the `lib_ext` folder in the Workato agent's home directory:
   
   - `sapjco3.jar`
   - `sapjco3.dll` (Windows), `libsapjco3.so` (Linux), or `libsapjco3.dylib` (Mac)
   - `sap-connector-impl-<version>.jar`
3. Verify that the `config.yml` file includes `lib_ext` in the classpath. For example:
   
   ```yaml
   server:
     classpath:
       - lib_ext
   ```
   
4. Ensure proper indentation and formatting in your `config.yml`. Check the YAML indentation in your config.yml. If the formatting is incorrect, the agent may fail to load the SAP profile. For example:
   
   ![Proper file indentation](/assets/lib-ext-indent.DIRJeZNG.png)_Proper file indentation_
   

### java.lang.NoClassDefFoundError: com/sap/conn/idoc/jco/JCoIDoc

This error occurs when the SAP Java IDoc Library is missing. Complete the following steps to resolve this:

1. Download the SAP Java IDoc Library (SAP JIDocLib). Refer to the [SAP Java Connector](https://support.sap.com/en/product/connectors/jco.html) page for more information.
   
2. Add the following files to the `lib_ext` folder in the Workato agent's home directory:
   
   - `sapidoc3.jar`

### Cannot invoke "com.workato.agent.sap.impl.json.IDocTypeBean.getSegMap()" because "selected" is null

This error occurs when the agent creates a trigger before it completes metadata retrieval from SAP. Wait 90 seconds for the OPA to retrieve the metadata.

## Contact support

If the issue you encounter isn't listed here and you need help, check the `agent.log` file or contact [Workato Support](https://support.workato.com/en/support/home). Ensure that you provide the support TRACE level OPA logs for further analysis. Verify that you can reproduce the error by stopping the OPA and renaming the existing `agent.log` file to generate fresh logs. The following configuration settings must be applied in the `config.yml` file located in the **"conf"** folder in the OPA installation directory:

```yaml
logging:
  com.workato.agent.sap: TRACE
```

---
