---
url: 'https://docs.workato.com/en/on-prem/agents/logging.md'
description: >-
  Learn how the Workato on-prem agent logs activity, warnings, and traces,
  including the rotation schedule and retention quotas.
---

# On-prem agent logs

The on-prem agent (OPA) logs a variety of events. The log file contains OPA activity, warnings, and traces. The most common use of log files is for troubleshooting, but there are other scenarios, such as audit and compliance.

## Logging schedule

The OPA logger creates a new log file at the start of each day, based to the on-premise system time. It also creates a new log file after the file size exceeds 20 MB. To identify the multiple log files of the same day, the system numbers them sequentially.

You can access the OPA log files in the agent folder. The OPA retains logs for a maximum of 60 days, or at most 20 GB of files.

### Scenario 1: logging up to 20 MB

<dl><dt>Date</dt><dd>01-NOV-2019</dd><dt>Total file size:</dt><dd>15 MB</dd><dt>Log file</dt><dd><code>/agent-2019-11-01.0.log</code><br>A log file starts at the beginning of the day.</dd></dl>

### Scenario 2; logging over 20 MB

<dl><dt>Date</dt><dd>02-NOV-2019</dd><dt>Total file size</dt><dd>25 MB</dd><dt>Log file</dt><dd><code>/agent-2019-11-02.0.log</code><br>A log file is starts at the beginning of the day. The system stores the first 20 MB in this file.<br><br><code>/agent-2019-11-02.1.log</code><br>A new log file starts when the system reaches 20 MB. It contains the remaining 5 MB.</dd></dl>

## OPA log properties

OPA logs contain the following properties:

<dl><dt>Date</dt><dd>OPA dates each log file to improve its findability.</dd><dt>Numbered logs</dt><dd>If there are multiple log files on the same day, OPA numbers them sequentially.</dd><dt>File size limit</dt><dd>The logger enforces a 20 MB size limit to make it easier to query file content.</dd><dt>Storage limit</dt><dd>The folder limit reduces the storage load on the server.</dd></dl>

## Logging OPA activity

At the top level of your `config.yml` file, add the `logging` definition to record the various level of activity logs.

```yml
logging:
  cloud: true
  logger: logging_level
  workato: debug
  sql: trace
```

OPA uses the `cloud` property to send the logs to Workato cloud, to the Workato support team can efficiently access these logs when you require assistance in solving technical issues. This option is enabled by default in the config file. If you don't want to send your agent logs and performance data to Workato, set this value to `false`.

> **TROUBLESHOOT COMMON LOG ERRORS**
> 
> Some log entries point to configuration issues or runtime errors. Refer to the following guides to troubleshoot these errors:
> 
> - [PKIX path building failed error](/en/on-prem/agents/opa-troubleshooting/troubleshoot-setup#pkix-path-building-failed-error)
> - [Java heap space errors](/en/on-prem/agents/opa-troubleshooting/troubleshoot-runtime#java-heap-space-errors)
> - [The agent lost access to the logs folder](/en/on-prem/agents/opa-troubleshooting/troubleshoot-setup#the-agent-lost-access-to-the-logs-folder)

### Workato loggers

These are the loggers that Workato uses:

<dl><dt>workato</dt><dd>This will include logs from all parts of the OPA.</dd><dt>sql</dt><dd>This will only log database-related parts of the OPA.</dd><dt>custom</dt><dd>See <a href="#using-a-custom-logger">Using a custom logger</a> for more information.</dd></dl>

### Workato logging levels

These are the supported logging levels:

<dl><dt>trace</dt><dd>Information for identifying steps that lead to the error. Typically used for diagnosis in the engineering support group.<br>We recommend that you use this *temporarily*, because this exposes a large amount debugging information, including *confidential data*.<br>Example: Starting secure tunnel</dd><dt>debug</dt><dd>Information for troubleshooting or diagnosis, and readable/understandable by users.<br><strong>Example</strong>: Failure due to an unknown exception.</dd><dt>info</dt><dd>Information logged under normal conditions.<br><strong>Example</strong>: agent starting or stopping.</dd><dt>warn</dt><dd>Information about a potential problem that does not require immediate attention from the user.<br><strong>Example</strong>: transient network interruption.</dd><dt>error</dt><dd>Information about an error that needs investigation.<br><strong>Example</strong>: Agent failed to start.</dd></dl>

### Enable TLS handshake logs

You can add TLS handshake information to OPA logs to help diagnose SSL/TLS connection issues, such as certificate trust failures and hostname verification failures.

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
   

## Logging for specific profiles

You can also choose to selectively enable logs for specific profiles. All you have to do is add the `debug: true` definition to the profile:

```yml
database:
  sql:
    adapter: mysql
    database: workato
    username: user
    password: password
    timeout: 30
    debug: true
```

## Using a custom logger

You can also use a custom logger instead of the native Workato loggers. Simply replace the logger name with the name of the class or the package of your custom logger.

```yml
logging:
  "com.workato.agent.file": debug
```

## Where to find OPA logs

The location OPA logs are stored in varies based on your agent configuration and operating system.

Refer to the following sections for more information:

- [Windows](#windows)
- [Linux](#linux)
- [Workato Logging Service](#workato-logging-service)

### Windows

Log files are stored in `%SYSTEMROOT%\System32\LogFiles\Workato` by default for on-prem agents operating as a Windows service. You can navigate to this file manually or use the shortcut in the **Start** menu under **All apps > Workato**.

Complete the following steps to change the log storage location:

1. Open the Windows **Start** menu.
   
2. Go to **All apps > Workato**.
   
3. Open the **Service Wrapper Configuration** app for the agent you plan to configure.
   
4. Go to the **Logging** tab.
   
5. Enter a new log storage location in the **Log path** field. This field locates the Windows service wrapper's lifecycle log (`Agent.<date>.log`), its stdout and stderr capture files (`<service-name>-stdout.<date>.log` and `<service-name>-stderr.<date>.log`), and the service's PID file (`workato.pid`).
   
6. Go to the **Startup** tab.
   
7. Go to the **Arguments** field and update the `--logs=` argument to point to the new log storage location. This argument configures the OPA's application log (`agent.log`).
   
8. Click **Apply**.
   
9. Restart the agent for the change to take effect. Refer to [Run an on-prem agent](/en/on-prem/agents/run) for more information.
   

> **OPA LOG CONTENTS**
> 
> The level of detail included in your OPA logs depends on your agent configuration. Refer to the [Workato logging levels](/en/on-prem/agents/logging#logging-opa-activity) section for more information.

### Linux

Log files are stored in `/var/log/messages` by default for on-prem agents operating as a Linux service through `systemd`. Because this file also contains logs from other Linux services, you must use the `journalctl` command to access OPA specific logs.

```shell
journalctl -u [name of the OPA service].service
```

The `-u` switch filters the logs returned by the service that created them. Replace `[name of the OPA service]` with the name you set for the OPA during installation.

You can further refine your log search using the following commands:

- `> [output-file]`: Exports the result of `journalctl` to a file.
- `--since`: Limits the generated logs to after a specific date and time.
- `--until`: Limits the generated logs to before a specific date and time.

For example:

```shell
journalctl -u workato.service --since "2020-07-26 23:15:00" --until "2020-08-5 23:20:00" > OPALogs.txt
```

Refer to Loggly's [Using journalctl](https://www.loggly.com/ultimate-guide/using-journalctl/) guide for additional journalctl information.

> **OPA LOG CONTENTS**
> 
> The level of detail included in your OPA logs depends on your agent configuration. Refer to the [Workato logging levels](/en/on-prem/agents/logging#logging-opa-activity) section for more information.

> **TROUBLESHOOT MISSING LOGS**
> 
> Refer to the [OPA runtime and performance troubleshooting guide](/en/on-prem/agents/opa-troubleshooting/troubleshoot-runtime) if the OPA stops generating logs when running on Linux. This issue occurs when there is either no free space remaining on the disk or when the logging level settings are incorrect.

### Workato Logging Service

If you are using OPA version 23.0 or newer, you can send your on-prem agent logs to [Workato Logging Service](/en/features/logging-service).

![Enable logging service](/assets/opa-logs.CBhICHxZ.png)_Enable logging service_

In your on-prem group's **Settings** tab, select **Send to Workato logs** to start sending OPA logs to the Workato Logging Service. This allows you to see a more detailed flow of your jobs being processed with Workato on-prem agent usage. By default, this option is disabled.

Note that the Workato Logging Service doesn't include `trace` level OPA logs.

> **ENABLE LOGGING SERVICE**
> 
> If you do not see this option, you do not have the Workato Logging Service enabled in your workspace. Contact your Customer Success representative to enable the Logging Service.

![OPA logs in the Workato Logging Service](/assets/opa-logs-detail.2xSlcLCh.png)_OPA logs in the Workato Logging Service_

You can filter logs by each column on the Logs page. Refer to [Logging service](/en/features/logging-service#filter-log-entries) for instructions.

For example, in the following image, the Logs page only displays entries with log level `ERROR`:

![OPA logs in the Workato Logging Service](/assets/opa-logs-filter-by-error.Bvf9aKUC.png)_OPA logs in the Workato Logging Service_

---
