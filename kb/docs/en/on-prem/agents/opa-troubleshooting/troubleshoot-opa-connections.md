---
url: >-
  https://docs.workato.com/en/on-prem/agents/opa-troubleshooting/troubleshoot-opa-connections.md
description: >-
  Troubleshoot Workato on-prem connection issues, including SDK extension
  startup and SFTP and Kafka connection errors.
---

# On-prem connection issues

This guide explains issues you may encounter with on-prem connections. This includes issues starting the SDK extension as well as SFTP and Kafka connection errors.

## SFTP - UnknownHostException error

An SFTP on-prem connection fails when there is whitespace in the `Hostname` field in your Workato connection.

You see the following error when you try to establish an SFTP on-prem connection:

```bash
 Error processing SFTP request java.lang.RuntimeException: com.jcraft.jsch.JSchException: java.net.UnknownHostException: XX.XX.XX.XX
```

You may also see the following error in on-prem logs:

```bash
"status":401,..."status_message":"Unauthorized"
```

However, you can connect to SFTP manually using the command line tool.

This happens when there is extra whitespace in the Java logs. For example, there is typically one whitespace between `:` and the IP address. The connection fails if there is more than one space. Review your request and remove extra whitespaces to resolve this error. Refer to [Connections using an on-prem agent](/en/on-prem/agents/connection) for more information.

## Kafka - No profile found error

The OPA displays a **No profile found** error when it can't locate the specified Kafka profile during execution. This issue often results from a configuration mismatch in the `config.yml` file.

![File configuration mismatch](/assets/kafka-profile-error.CCtj4NHb.png)_File configuration mismatch_

Check the following in your `config.yml` to resolve the error:

- The `kafka:` block exists
- The profile name matches exactly, including capitalization
- The profile is properly nested under `kafka:` without indentation errors

For example:

```yaml
kafka:
  myKafkaProfile:
    bootstrap.servers: "localhost:9092"
```

The OPA must recognize the profile exactly as defined. Any mismatch in structure or naming prevents the agent from loading the configuration.

## 520 Connection Failed error

The OPA displays the following **520 Connection Failed** error when it can't start a Java-based extension:

```
Failed to start SDK extension. 520 Connection Failed
```

This error appears during startup and indicates a failure to initialize the SDK handshake between the extension and the Workato platform.

Complete the following steps to resolve the issue:

1. Verify that your system uses **JDK version 8**. Other versions, including more recent versions, may cause compatibility issues during the extension build or runtime.
   
2. Run the `./gradlew jar` command in the root directory of your extension project to build the `.jar` file. For example:
   
   ```bash
   /Users/your-user-name/Downloads/opa-extensions-master/gradlew jar
   ```
   
   This creates the output `.jar` file in the `build/libs/` directory.
   
3. Check both the test and action block in your extension code. The `post()` URLs must use the correct port number, such as `localhost:3000`. For example:
   
   ```js
   post("http://localhost:3000/ext/#{connection['profile']}/computeDigest", { payload: 'test' })
   ```
   
   The OPA uses this port to connect to the extension. The agent may fail to connect and return a 520 error if the port is missing, incorrect, or blocked.
   

## Enable TLS handshake logs

You can add TLS handshake information to [OPA logs](/en/on-prem/agents/logging) to help diagnose SSL/TLS connection issues, such as certificate trust failures and hostname verification failures.

Complete the following steps to enable TLS handshake logs:

1. **Windows**
   
   1. Open the Windows **Start** menu.
      
   2. Go to **All apps > Workato**.
      
   3. Open the **Service Wrapper Configuration** app for the agent you plan to configure.
      
   4. Go to the **Java** tab.
      
   5. Enter the `-Djavax.net.debug=ssl:handshake` parameter in the **Java Options** field.
      
   6. Click **Apply**.
      
   7. Restart the agent for the change to take effect. Refer to [Run an on-prem agent](/en/on-prem/agents/run) for more information.
      
   
   **Linux, Mac, and Docker**
   
   1. Go to the `bin` folder inside your OPA installation.
      
   2. Open `run.sh`.
      
   3. Add the `-Djavax.net.debug=ssl:handshake` parameter to the `JAVA_OPTIONS` variable. For example:
      
      ```bash
      LIBPATH="${WORKATO_AGENT_HOME}/lib_ext"
      LIBPATH="-Djava.library.path="\""${LIBPATH}"\"
      JAVA_OPTIONS="${JAVA_OPTIONS:-} -Djavax.net.debug=ssl:handshake"
      ```
      
   4. Restart the agent for the change to take effect. Refer to [Run an on-prem agent](/en/on-prem/agents/run) for more information.
      
   
2. Open your OPA log file to confirm TLS handshake information is included. The following example shows a failed connection with TLS details visible:
   
   ```
   2025-08-13 09:50:51.206-04 [main] ERROR c.w.agent.net.GatewayCheck - Failed
   gateway check: Connect to https://sg3.workato.com:443
   [sg3.workato.com/52.206.161.203, sg3.workato.com/54.224.75.148,
   sg3.workato.com/52.204.114.159] failed: Connect timed out
   -- HTTP CONTEXT --
       Request: GET /gateway/ping null
        Config: [expectContinueEnabled=false, proxy=null, cookieSpec=null,
   redirectsEnabled=true, maxRedirects=50, circularRedirectsAllowed=false,
   authenticationEnabled=true, targetPreferredAuthSchemes=null,
   proxyPreferredAuthSchemes=null, connectionRequestTimeout=3 MINUTES,
   connectTimeout=null, responseTimeout=null, connectionKeepAlive=3 MINUTES,
   contentCompressionEnabled=true, hardCancellationEnabled=true]
       Route: {s}->https://sg3.workato.com:443
   AuthState: https://sg3.workato.com:443 -> [UNCHALLENGED]
   ------------------------
   -- CLIENT CERTIFICATES --
   -- >>
       Validity: 2025-08-04T20:55:48Z - 2026-08-04T20:56:18Z
        Subject: CN=a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4:10001
   Issuer: CN=Workato opa CA, OU=Devops, O=Workato, L=Mountain View, ST=CA,
   C=US
   -- >>
       Validity: 2024-09-16T08:48:17Z - 2034-05-03T21:10:35Z
        Subject: CN=Workato opa CA, OU=Devops, O=Workato, L=Mountain View, ST=CA,
   C=US
        Issuer: L=Mountain View, CN=Workato onprem Root CA onprem production,
   ST=CA, OU=onprem production, O=Workato onprem Root, C=US
   ------------------------
   -- SERVER CERTIFICATES --
   empty chain: null
   ------------------------
   ```
