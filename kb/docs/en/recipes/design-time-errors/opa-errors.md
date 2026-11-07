---
url: 'https://docs.workato.com/en/recipes/design-time-errors/opa-errors.md'
description: >-
  Troubleshoot common Workato on-prem agent (OPA) errors covering setup,
  upgrades, runtime behavior, connections, and how to locate and read OPA logs.
---

# On-prem agent (OPA) error troubleshooting

Use this guide to troubleshoot common issues with the Workato on-prem agent (OPA). These guides cover setup, upgrades, runtime behavior, and extensions.

> **REVIEW LOGS**
> 
> Refer to the following sections to locate and investigate errors in OPA logs:
> 
> - [OPA log generation and retention](#understanding-opa-logs): Learn where to find logs and how to interpret them.
> - [Job-level troubleshooting](#job-specific-troubleshooting): Use job IDs to trace failures in logs.

Choose a guide based on the issue you plan to troubleshoot:

- [Setup and installation issues](/en/on-prem/agents/opa-troubleshooting/troubleshoot-setup): Agent startup failures, permission errors, directory creation problems, and proxy-related SSL errors.
- [Upgrade and configuration issues](/en/on-prem/agents/opa-troubleshooting/troubleshoot-upgrade): Post-upgrade failures, service account resets, and connection profile changes.
- [Runtime and performance issues](/en/on-prem/agents/opa-troubleshooting/troubleshoot-runtime): Heap space errors, logging errors, long query errors, and stuck jobs.
- [Connection issues](/en/on-prem/agents/opa-troubleshooting/troubleshoot-opa-connections): Java extension errors and connection errors for SFTP and Kafka.

## OPA log generation and retention

You can use OPA logs to identify agent behavior and system issues during execution. The OPA generates a new log file daily based on the on-premise system time. If a log file exceeds 20 MB within a day, a new one is created and numbered sequentially. For example, if `/agent-2019-11-01.0.log` is the first log of the day, additional logs for the same day are `/agent-2019-11-01.1.log` and `/agent-2019-11-01.2.log`. The OPA retains the latest 60 log files or a maximum of 20 GB of logs.

### Locate OPA logs

You must locate the log files to troubleshoot OPA issues. Depending on your operating system, complete the following instructions for Windows or Linux:

**Windows**

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

**Linux**

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

## Job-specific troubleshooting

Use the job ID to search OPA logs and trace job execution across all stages. This allows you to isolate OPA-specific operations within a single job. For example: `j-AHd9XdsW-JppW`.

![Locate jobs](/assets/find-job-id.DR5Ju-uo.png)_Locate jobs_

---

---
url: >-
  https://docs.workato.com/en/on-prem/agents/opa-troubleshooting/troubleshoot-setup.md
description: >-
  Troubleshoot Workato on-prem agent setup and installation issues caused by
  permissions, invalid config files, or environment restrictions.
---

# On-prem setup and installation issues

This guide covers common issues that occur when you install or initialize the on-prem agent (OPA). These errors result from permission problems, invalid configuration files, or environment-level restrictions.

## Configuration file issues

The `config.yml` file in `<INSTALL_HOME>/conf/config.yml` controls how the agent authenticates and connects to Workato. Errors in this file prevent the agent from starting at first activation or after a later edit.

### Incorrect connection details in `config.yml`

Incorrect authentication entries in the `config.yml` file can cause the agent to fail at startup. Ensure your authentication details are accurate.

### Invalid `config.yml` formatting

The `config.yml` file requires strict indentation and spacing. A misplaced space or newline causes YAML parsing failures. Use an online validator to check the format before you start the agent and remove sensitive information before you use any external tools.

## Permission and account issues

The OPA may encounter errors due to insufficient permissions. Most permission errors occur during activation, first startup, or after changes to permissions.

### Windows Certificate Store access

You may encounter a `Certificate not found` error when activating the agent with **Windows Certificate Store** selected. This is typically caused by insufficient permissions to access the certificate store. You can resolve this issue by storing the key and certificate in the file system or updating your permissions.

Refer to the [Install an on-prem agent on Windows](/en/on-prem/groups/add-agent/windows) guide to store the key and certificate in the file system.

### Windows service account permissions

The agent may fail to start if the assigned service account lacks required permissions. Assign a user with higher privileges to resolve the issue. For example, in Windows:

1. Press `Win + R`, type `services.msc`, and press `Enter`.
   
2. Go to the **Services** window and locate the agent.
   
3. Right-click on the agent and select **Properties**.
   
4. Switch to the **Log on** tab.
   
5. Change the account used to run the agent to one with higher privileges.
   
   ![Change your account](/assets/change-account.Dq_QeFei.png)_Change your account_
   

Refer to [Install an on-prem agent on Windows](/en/on-prem/groups/add-agent/windows) for more information.

### Linux permissions

The OPA installer automatically creates a `workato` system user. Workato strongly recommends running set up commands as this system user to avoid permission errors during activation.

Complete the following steps to create a `workato` system user if it doesn't already exist after agent installation:

1. Run the following commands to create a system group and user with no login shell:
   
   ```shell
   sudo groupadd -r workato
   sudo useradd --comment "Workato Agent" \
               --no-create-home \
               --home /nonexistent \
               --gid workato \
               --system \
               --shell /usr/sbin/nologin \
               workato
   ```
   
2. Run the following commands to set ownership of the Workato agent directories:
   
   ```shell
   sudo chown -R workato:workato /etc/workato-agent/
   sudo chown -R workato:workato /usr/lib/workato-agent/
   ```
   
3. Complete the remaining steps in the [Linux DEB package](/en/on-prem/groups/add-agent/linux-deb) or [Linux RPM package](/en/on-prem/groups/add-agent/linux-rpm) set up instructions as the `workato` system user.
   

### Unable to create directory \[work\] to use as the base directory error

The agent may fail at startup with an `Unable to create directory [work] to use as the base directory` error when it lacks permission to create the `work` directory. This issue often occurs when the agent runs under a limited-privilege account.

![Initialization error](/assets/initialization-error.Bb13Js7J.png)_Initialization error_

Run the agent with an administrator account to avoid this error. If the agent runs as a service, confirm that the assigned service user has full access to the install path.

### The agent lost access to the logs folder

Cleanup jobs or automated server processes may delete the logs folder. The agent can't launch without access to this folder.

![OPA error](/assets/opa-launch-error.C8AdL3Na.png)_OPA error_

Recreate the logs folder to restore access. Note that certain server applications or rules may repeatedly delete the OPA logs folder. Reinstall the OPA using an account with higher privileges if this issue continues.

## Network and certificate issues

The agent must reach Workato gateways (`sg3.workato.com`, `sg4.workato.com`) over port 443 and validate the SSL certificate chain. Improperly configured proxies, firewalls, SSL inspection tools, and missing intermediate certificates can break this connection.

### Unable to load folder structure error

The on-prem files connector may fail with an `Unable to load folder structure` error when it tries to access a network folder.

This error occurs when the OPA host can't reliably connect to the target folder.

Complete the following steps to resolve the issue:

1. Remove any duplicate OPA instances running in your environment.
   
2. Verify the network connection between the OPA host and the folder's location.
   
3. Confirm that the account running the OPA service has permission to access the folder.
   

### PKIX path building failed error

You may see the following error in logs when the agent starts:

```
javax.net.ssl.SSLHandshakeException: PKIX path building failed:
sun.security.provider.certpath.SunCertPathBuilderException:
unable to find valid certification path to requested target
```

This error appears when the on-prem agent (OPA) can't validate the SSL certificate chain for the target service.

This error typically occurs due to one of the following issues:

- Intermediate or root certificates are missing from the trust chain.
- SSL inspection or DLP tools modify or replace certificates.
- A proxy or firewall intercepts HTTPS traffic between the OPA host and the service.

Complete the troubleshooting steps relevant to your OPA configuration to resolve the error:

- Trust required intermediate and root certificates if the error involves an internal service. You can add certificates in the connection configuration, in the `config.yml`, or to the OPA trust store.
  
- Create exceptions for [Workato gateways](/en/security/ip-allowlists#on-premise-agent) if the environment includes a firewall, outbound proxy, or SSL inspection layer, such as DLP tools. You must bypass SSL inspection for Workato's FQDNs because the gateway connection only trusts Workato's private CA. Adding the inspection tool's CA to the OPA trust store doesn't resolve gateway errors. Refer to [Configure SSL/TLS inspection](/en/on-prem#ssl-tls-inspection) for more information.
  
- Configure the `proxy:` section in the `config.yml` file to connect through a proxy. Refer to the [Set up proxy access for your on-prem agent](/en/on-prem/agents/proxy) guide for more information.
  

## Review logs for startup failures

Check the [OPA logs](/en/on-prem/agents/logging) when the agent doesn't start or connect. Repeated "agent connected" and "disconnected" entries often indicate unstable network connectivity. You can expose a [Prometheus metrics endpoint](/en/on-prem/agents/monitoring) (OPA 32.0 and newer) to gather real-time information about agent performance.

SSL errors like `PKIX path building failed` or full exceptions such as `com.workato.agent.net.AgentNonRecoverableException: Error connecting to the gateway sg3.workato.com:443 javax.net.ssl.SSLHandshakeException: PKIX path building failed` indicate that the agent can't validate the SSL certificate chain for the target service. This can happen if intermediate or root certificates are missing, if SSL inspection tools replace or modify certificates, or if a proxy or firewall intercepts the connection between the OPA host and the service.

These patterns can help confirm whether the issue comes from configuration, permissions, or network restrictions.

## Installation best practices

Workato recommends the following practices to ensure the agent starts reliably and runs without interruption.

### Confirm access to Workato's gateway

Ensure the machine running the OPA can reach `sg3.workato.com` and `sg4.workato.com` over port 443. Firewalls or proxies that block outbound HTTPS traffic can prevent the agent from connecting. Refer to [Resolve gateway names on servers with OPA installed](/en/on-prem/agents/opa-troubleshooting/troubleshoot-runtime#resolve-gateway-names-on-servers-with-opa-installed) for more information.

### Use consistent configuration management

Validate the `config.yml` file in a test environment before production deployment. Store validated versions of the file for rollback and configuration tracking.

### Isolate agent instances

Install each agent in a separate path with its own configuration and certificate set. Don't share folders or service accounts across agents.

### Optimize data efficiency

Deploy the agent in the Workato data center nearest to the on-prem system. This setup reduces latency and supports large-volume or high-throughput data.

### Handle credentials securely

Use a secrets manager to store credentials. Don't embed credentials directly in the YAML file or store them in plaintext. For setups that rely on a legacy YAML configuration, protect the file and restrict access.

### Windows installation

Use **Local Service** as the default account for the OPA service. This account provides restricted access. Most teams configure a domain-specific service account to manage permissions and ensure proper access to required resources.

### Linux installation

Workato recommends the following practices when installing OPA on Linux:

- Configure OPA as a service to enable automatic restarts after server reboots.
- Run set up commands as the `workato` system user to avoid permission errors during activation. Refer to the [Linux permissions](#linux-permissions) section for more information.

---

---
url: >-
  https://docs.workato.com/en/on-prem/agents/opa-troubleshooting/troubleshoot-upgrade.md
description: >-
  Troubleshoot Workato on-prem agent upgrade and configuration issues, including
  service accounts, keys, and connection profiles.
---

# On-prem upgrade and configuration issues

This guide explains common issues you may encounter when you upgrade the on-prem agent (OPA) or reconfigure its settings. These problems often result from changes to service behavior, configuration paths, or connection logic across OPA versions.

## Back up `config.yml` before the upgrade

Create a copy of your current `config.yml` file before you start the upgrade. This ensures you can restore your authentication and connection settings if the upgrade overwrites the configuration. If your file includes encrypted passwords, you must re-encrypt them after the upgrade. Encrypted values are tied to the agent's private key and don't transfer between agents.

## Activate firewall ports

Open outbound TCP port 443 to `sg3.workato.com` and `sg4.workato.com` before you upgrade from OPA version 2.10.0 or earlier.

## Restore the original service account if the upgrade resets it

Upgrades may reset the OPA service to use a local account instead of the previously configured user account. This change can disrupt existing connections, such as SQL server connections with `integrated security=true` or file connections to shared drives.

![Connection error](/assets/opa-connection-error.CLWfGPGi.png)_Connection error_

You can change the Windows service configuration back to the previously configured user account to resolve the issue.

## Use separate keys for each agent

Assign a unique set of key files to each agent on the same server. Sharing files like `cert`, `key`, or `cert.pem` can cause authentication failures.

## Reconnect HA agents after the upgrade

Re-establish configuration between upgraded agents in high-availability (HA) setups. Copy the `config.yml` file to each new or restored agent, and confirm the service account can access all mounted paths. If the file contains encrypted passwords, you must re-encrypt them for each agent. Encrypted values rely on agent-specific keys and don't work across different agents.

## Connection profiles with new versions

Create a new on-prem group when you use OPA version 2.15.0 or higher and avoid assigning cloud connection profiles to the same group used by older agents. You can use the **Directly in Workato** option to create the group, then add a new agent to manage those profiles.

![Set up connections](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAqUAAACLCAMAAABvPxBvAAACmlBMVEUAYWsAZm8YRFAcRlIeSFQiS1cjS1cjTFckTFglTlkmTlomT1onT1oqUVwrUl0sU14tVF8uVF8uVWAvVWAwVmExV2IzWWQ0WmQ2WmU3W2Y4XGc5XWg7X2k9YGo+Ymw/YWxBY21DZW9EZm9GZ3FHaHJIaXNKanRKa3VMbXZNbXdObndPb3hQkpxRcHlScXpTcntUcntVdH1WdH1Zdn9Zd4BaeIFdeoJde4Nde4lee4NhfoZjfodkgYlmgYlmgYpngpBog4tqhIxqhY1rhY1sho5uiJBviZBxi5Jxi5Z0jZR0jZV1jpV2j5Z4j5Z5kJd7kpl+lZx/lp2Alp2Al52Bl56CmJ+EmqCFm6KGnKKHnaOInaSLoKaMoaeNoqiOoqiQpKqRpauSpqyTv8OXqK+Yqa+YqbCZqrGaq7KbrLKdrrSerrSer7Wfr7agsLaisriks7mmtruntrypuL2qub+rur+susCtvMGvvcOwvsOxv8Szv8W1wca3w8a3w8i4xMm4xM26xsm7xsu8yMu9yM2+yc6/ys3By9DBzM/CzdDEztHFz9LG0NPH0dTI0tXK09jK1NbL1NfM1djO19rP2NrQ2dvT2tzT2t3V3N7W3d/W3eDX3uDY6enZ3+La4OLb4eTc4uTd4uTe5Obf5Obg5ujh5ujj6Orj6Ovk6erk6evl6uvm6uzn6+zo7e7p7e7q7O3q7u/q7vDr7e7r7e/r7/Ds7u/s7vDs8PHtIwDt7/Dt7/Ht8fLt8fPu8PHu8PLu8PPu8vPvOhrvRCbvRinv8fLv8fPv8/Tw8vPw9PXxUjfx8/Tx8/XyZU7y8fHy9PXzdmTz9fb0g3P0jHz0nJD0o5b06+v1vLP2+Pj6+/v8/f39/f39/f7+/v7+/v////9l4A0GAAAK90lEQVR42u3d/39T1R3H8XLuNVabNhek2pZGN8JXtZVpyyg6FLpSHXXgGNkMLRBRNsJsgWVSKEMz0YFliIDrRBiOkhVasWJrV2Ir22Jvd7d1d19zN7fP/7Jz7k1KE/olLS23D3y/fHhDb25uHo+c5+N+SX44GTpC070MfAQIShGCUgSlCEEpQlCKoBQhKEUIShGUIgSlCEoRglKEoBRBKUJQitAYSs/uODsVb/XdO46O/OTvMRRoHEojCxlj9zQn/ty4YBLe5YTrxKhK//aX3/7pHxgMlLbSarbpfOiRSOLPFfmT8C772NHRN/jrb/6OsUDpK13HjljH1FUSeyCyUpZcK8Wfro26vmABPyr6ZiaOtC/exrJ/qj8rs5mHdH3l0mcl9k2+3daFTP6Jrv9yDpOrdb35Aca+9qM7WLZL38gPqHyttCrC9/LDe1h2k35kJpPX8T3983f/+gPGAqWv9Igkr3qHP1ZKew5nrXrlSzk7XhGrGdeUn68fZVk7t0vzxJrd7CuhVc1b2ROhQqlZL2XzdhSyMzpja/zSXD0yq/C4n/1YL5S376z+xWr2nR2c/9HIrKy9PlbJ9yL5vsVW6HNnHd/5PbGvP/P/EEr/7unAHMZKIvrtlbq+Nl8vjZ/xB5Xyx1J2ga+ZmxMxl7r+KtvA1+n6Vn5iZ6W6vjifn+Nf1fW71+1jfvHiOnHG50r3sa38WcnaS06pXpQVwhCgCd3j6z+bx6p/xUTDK11nXmZmleqJJacplNbFlfLXbDZfvm6zdUGaULo5/mjuJb9Ub57DbnsJg4DGf4/Pj5Dt3JpUaf45qLRy6LFUHEULc8T6wrt1vnJDqtLd4lgqrgq2DlW6m73In40fS/OF73fmShcwCmi8Skuzt59+gn1fXyHtaQ8d1b/KDp8Xq2/PP76GCaVzj++RzKPoBlZ52t9Uzfyni6SmVKWRrMKfX9yuX8jKOny8mmP99mnzujSrkL96xaDSbxzWv86gFI1b6SF+WSqtsb43lf36EZkttkyyhaVCaa7E7mu2vgTgG/xAF8uX9FSl+pFsxmYe1w/xhy+/H7mPsQviOkGsXRhJKH3/Ef5W1RgENIHr0ounI/FHE2PiL/OQyn21D/4y1X762vL6zp63Hi5eWw79R3wPEYwBmtDd0yiZR0GEprXSE+LbfYSmtVKEoBQhKEVQihCUIihFCEoRglIEpQhBKULpK31uRgZCN70Zz41D6cCMdwmhm967MwbSVjowkIEPDNlRxsBA2ko1KEX2KNXSVToApcg+pQPpKu2DUmSP0r60lfarUIrsUar+MV2lGpQiu5RqUIqgFCEoRVAKpQhKEYJSBKUIQSlCUIqgFKFpotQIh8OG+EdFaKQ38ZYN+SNpsy6NL8TLta6kVwQLMDRoEpU2MUWRHuPQ5tcP97SSqjRps/VlYgeNROXrR1G6ZQsGCkpvUClRzL18pDdgqUqTqs8j8s/2EnnqR1Hq9WKgoPSGldI51kKLGqihwic1kFeWV/N1NQ5W/FY2UxYJpfP5ed5QLvHV5mY1slwrXtzCDCrZ5CGSWqijWHK8QNY+hFLfo3SqWJafoQrZoTTQe/eyu/ZiwKB04kopL0gFQQo6q2KGzx0zSmrJ7zxPB4yDLNwmlNbww2nQI7YUm0k1Rl2m+WpXIzljstHkInJXGa3OgLUPrjToNqj+ALVKb3Y9/HQ4pjq30TGpESP2BejDD6dIaYGl1GXBo2AZuWoHn+VKVUmlskBCKT9SGvzoyyvxN3rIE9pVQo0Sv7YNuK19BAtO5nRY92bcfxk/4wfENUDVcgzhrV/z4483T41SV32CH7FsRVEqiDUNVUpLAgaHek1p/HlfuX89eX1VPmtlUIo/unLkc0StxbkVLkupeW3rdWMMvwBIly1LYTpJShu5wAS/TOu0nBlKUrrfE1pC1ysNuZeHKFRUxBfiEmBXQVwpC/qK+D3VNnN7odTviX8lgG59pKlMJ0fp207vNX7lJQbFDCqfZ9Apo4Wp8ePg7Ptrh1GqSnkGGU6Xyhd1ZLi9caUFZBTsoszXqTUzSOVV/P5MOkYdziBG8VbvyWVmT062UsZy64bwMxY7lDsPmg85Z+ghRy7Vyq/xW37rhJ+ilPLEMdKTxxcnc7IdS41BpRRydvhkpbgoSG9IyvO0X1YcazGIuMefrF9ItbD10CaWbTHr/8DYZ+s27bo9WT9Jxcw9hWMYLyidyt/xjVYnvkVC01zpU44APmw0zZUiBKUISqEUQSlCUIqgFCEoRVAKpeiWVfo/hKa0G1HKX/5fhG5SltZxKsXHhm5+41SKDwzZ0TiUqlFL6ef/Qegm9bmlNKqmqVQzlQ4S/TdCU9oQqFyplpZSfsKPPvgyQjb0YHTEU35Gysx5fVF8X4rs+b402jfS7HkZSUgHNA1KkV1KNa50IA2l4u4JnxeyR6k6MLZSsYmm4hdSZNcvpKo2AtOMJKT9OOMjO8/4/cMzTVaqaZ9BKbJL6WealobSfu1qNAKlyB6lkehV82A6ilLrqjQa7YFSZI/Snmh0hCvTJKWqGu2FUmSX0t6oqo6ptE+9Gu25AqXIHqVXeqJX1b6xlKrihN8BpcgepR3ilK+OoVTjSiNdnVCK7FHa2RWJmt+ZjqW0t6MdSpE9Sts7esdU2i+UXvkYSpFdSj++IpT2j6xUfKPPb566Oy9DKbJH6eXObn77pA1zME1W2tvdeQlKkT1KL3V296ajtKe78wMoRfYo/aCzu2cMpf1QiqaH0v6RlWqW0nYoRXYpbbeUaqMr/aSn+yMoRXYp/ai755OxlX7a0335OqVGOCzmtk+Z8z6ppOmckzbrEhOSiJfH5yFJlDydM0JC6eXunk/HVto7nNImpijSY0bKnPeDKalKkzYT8+A1sUai8vWjKN2yBWOETKW9E1ZKFHOPOIMtS1WaVH0ekX+2l8hTP4pSrxdjhG5YKZ1jLdac9z6pgbyyvJqvq3Gw4reymbJIKJ3Pz/OGcomvNjerkWVzqscWZlDJJg+R1EIdxZLjBbL2IZT6HqVTxbL8DFXIDqWB3ruX3bUXYwWlE1dKedak42Jae587ZpTUkt95ng4YB1m4TSit4YfToJjH0dxMqjHqMs1XuxrJGZONJheRu8podQasfXClQbdB9QeoVXqz6+GnwzHVuY2OSZjUDEpvQGmBpdRlwaNgGblqB5/lSlVJpbJAQik/Uhr86Msr8Td6yBPaVUKNEr+2DbitfQQLTuZ0WPdmedZ0zgFxDVC1HIMFpRNX6qq/NgNutqIoFfGJcAcnHV8SMKyZcpMnyvWV+9eT11fli0+QK8UfXTnyOaLW4twKl6XUvLb1ujFYUDphpY1cYIJfpnVazgwlKd3vCS2h65WG3MtDFCoq4gtxCbCrIK6UBX1F/J5qm7m9UOr3xL8SQFA6MaVvO73X+JWXGBQzqHyeQaeMFqbGj4Oz768dRqkq5RlkOF0qX9SR4fYOTjpuFOyizNepNTNI5VX8/kw6Rh3OIAYLSiemlLHcuiH8jMUO5c6D5kPOGXrIkUu18mv8lt864acopTxxjPTk8cXJnGzHUmNQKYWcHT5ZKS4K0huS8jztlxXHWowVlE5I6TBpYevBnNC+LWb9Hxj7bN2mXbcn6yepmLmncAxDBaWTpnSYjFYnvkVC01zpU44APmc0zZUiBKUISqEUQSlCUIqgFCEoRQhKEZQiBKUISqEUQSlCUIqgFCEoRQhKEZQiZJvSXyNkQziWIpzxEZpSpf8HKGhz/YMvmSUAAAAASUVORK5CYII=)_Set up connections_

---

---
url: >-
  https://docs.workato.com/en/on-prem/agents/opa-troubleshooting/troubleshoot-runtime.md
description: >-
  Troubleshoot Workato on-prem agent runtime issues, including heap space
  errors, logging errors, long query errors, and stuck jobs.
---

# On-prem runtime and performance issues

This guide covers issues that can occur during the on-prem agent (OPA) runtime. These include heap space errors, logging errors, long query errors, and jobs stuck due to dropped database connections.

## Java heap space errors

The following error log indicates the agent has reached its memory quota:

```
java.lang.OutOfMemoryError: Java heap space
```

This error indicates that OPA doesn't have enough memory to process large jobs or payloads. By default, the heap size is set to a fraction of available system memory.

**Windows**

1. Open the Windows **Start** menu.
   
2. Go to **All apps > Workato**.
   
3. Open the **Service Wrapper Configuration** app for the agent you plan to configure.
   
4. Go to the **Java** tab.
   
5. Enter the `-Xmx` parameter in the **Java Options** field. For example, enter `-Xmx10G` to allocate 10 GB of heap memory.
   
6. Click **Apply**.
   
7. Restart the agent for the change to take effect. Refer to [Run an on-prem agent](/en/on-prem/agents/run) for more information.
   

**Linux, Mac, and Docker**

Open `run.sh` and add the `-Xmx` flag to the `JAVA_OPTIONS` variable to adjust heap memory on Linux, Mac, or Docker. For example, the following line allocates 10 GB:

```bash
JAVA_OPTIONS="${JAVA_OPTIONS:-} -Xmx10G"
```

Restart the agent for the change to take effect. Refer to [Run an on-prem agent](/en/on-prem/agents/run) for more information.

## Resolve gateway names on servers with OPA installed

You may encounter the following errors when resolving Workato gateway names on servers with OPA installed:

- `sg3.workato.com`
- `sg4.workato.com`

Complete the following troubleshooting steps to resolve gateway names:

1. Connect to the server where your OPA instance runs.
   
2. Open your server's console.
   
3. Run the following commands to verify if the gateway names can be resolved from your Windows, Linux, and Mac server:
   
   `nslookup sg3.workato.com`
   
4. Run the following command on Linux and Mac servers to verify if the gateway names can be resolved:
   
   `dig sg3.workato.com`
   
   Your output is similar to the following:
   
   ```bash
   sg3.workato.com	canonical name = public-v10-awsprod-opg3-nlb-d6da47859547995a.elb.us-east-1.amazonaws.com.
   Name:	public-v10-awsprod-opg3-nlb-d6da47859547995a.elb.us-east-1.amazonaws.com
   Address: 54.224.75.148
   Name:	public-v10-awsprod-opg3-nlb-d6da47859547995a.elb.us-east-1.amazonaws.com
   Address: 52.206.161.203
   Name:	public-v10-awsprod-opg3-nlb-d6da47859547995a.elb.us-east-1.amazonaws.com
   Address: 52.204.114.159
   ```
   
   This successful output indicates that it is possible to resolve the domain name.
   

## Check gateway connectivity

You may encounter issues with establishing gateway connectivity on servers with OPA installed.

Complete the following troubleshooting steps to check gateway connectivity:

1. Connect to the server where your OPA instance runs.
   
2. Open your server's console.
   
3. Run the following commands to verify if the gateway names can be resolved from your Windows, Linux, and Mac server:
   
   ```bash
   curl -k -vvv -GET --no-alpn --key conf/cert.key --cert conf/cert.pem https://sg3.workato.com/gateway/ping
   ```
   
   Your output is similar to the following:
   
   ```bash
   * TLSv1.2 (IN), TLS handshake, Finished (20):
   * SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
   *
   (LINES SKIPPED)
   >
   < HTTP/1.1 200 OK
   < Content-Type: application/json
   < Date: Mon, 25 Jul 2022 21:33:42 GMT
   < Content-Length: 81
   <
   {"gateway_version":"1.0.1","os_platform":"linux","os_release":"4.19.0-10-amd64"}
   ```
   

## Verify the server certificate chain

You may encounter issues verifying the server certificate chain on servers with OPA installed.

Complete the following troubleshooting steps to verify the server certificate chain:

1. Go to your OPA installation folder. Refer to the [Accessing on-prem](/en/on-prem) documentation for more information about installation.
   
2. Download the Workato root certificate and save it in your OPA installation folder. Refer to the [HTTP SSL](/en/on-prem/agents/opa-troubleshooting/troubleshoot-runtime#download-the-certificate-chain) documentation for instructions.
   
3. Run the following command for Linux and Mac:
   
   ```bash
   curl -vvv -GET --no-alpn --cacert root_ca_cert.pem --key conf/cert.key --cert conf/cert.pem https://sg3.workato.com/gateway/ping
   ```
   
   The expected output contains the following:
   
   `SSL certificate verify ok`
   
   This indicates that the server certificate chain was successfully verified.
   

## OPA stopped creating logs

You may encounter an issue where OPA stops generating logs when running on Linux. This issue occurs when there is either no free space remaining on the disk or when the logging level settings are incorrect. Complete the following troubleshooting procedure to resolve this issue:

1. Run the following command to determine if there is free space left on the disk:
   
   ```bash
   df -h
   cat /etc/fstab
   parted -l
   ```
   
   This determines if the issue is related to disk space.
   
2. Verify that the logging permissions are correct.
   
   1. Run `ls -lah /var/log/workato-agent` to view log permissions.
      
   2. Run the following command if a user or group does not have permissions set to `workato`:
      
      ```bash
      chown -R workato:workato /var/log/workato-agent
      ```
      
3. Check that the logging level is set to debug in the config file. For example:
   
   `logger: debug`
   

## Jobs stuck indefinitely due to dropped TCP connections

Jobs that hang without producing an error or timeout are often caused by a firewall or NAT device silently dropping an idle TCP connection between OPA and the database. The JVM thread holding the socket receives no notification and waits indefinitely for a response.

You can configure TCP keepalive at the OS level to periodically probe idle connections and detect when they drop, allowing the stuck thread to fail and recover.

> **GLOBAL SETTINGS**
> 
> Keepalive settings typically affect all applications on the host, not just the Workato OPA.

**Windows**

Complete the following steps to configure keepalive settings on Windows:

1. Open the Windows registry editor (Regedit).
   
2. Go to the following path:
   
   ```text
   HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters
   ```
   
3. Create or update the following two **DWORD** values under the `Parameters` key:
   
   | Registry value | Description |
   | --- | --- |
   | `KeepAliveTime` | Milliseconds of inactivity before the first probe is sent. |
   | `KeepAliveInterval` | Milliseconds between subsequent probes. |
   
   For example, set `KeepAliveTime` to `300000` and `KeepAliveInterval` to `5000` to begin detection after 5 minutes of inactivity, and send probes every 5 seconds until the connection is confirmed dead.
   
4. Save your changes, then restart your machine for the changes to take effect.
   

**Linux**

Complete the following steps to configure keepalive settings on Linux:

1. Add the following lines to `/etc/sysctl.conf` to configure keepalive settings that persist across reboots:
   
   ```text
   net.ipv4.tcp_keepalive_time = INITIAL_WAIT
   net.ipv4.tcp_keepalive_intvl = INTERVAL
   net.ipv4.tcp_keepalive_probes = NUMBER_OF_PROBES
   ```
   
   Replace the placeholders with values suited to your network environment:
   
   | Parameter | Description |
   | --- | --- |
   | `INITIAL_WAIT` | Seconds of inactivity before the first probe is sent. |
   | `INTERVAL` | Seconds between subsequent probes. |
   | `NUMBER_OF_PROBES` | Number of unanswered probes before the connection is considered dead. |
   
   For example, the following configuration detects a dead connection in a maximum of 5 minutes and 15 seconds:
   
   ```text
   net.ipv4.tcp_keepalive_time = 300
   net.ipv4.tcp_keepalive_intvl = 5
   net.ipv4.tcp_keepalive_probes = 3
   ```
   
2. Save your changes, then run the following command to apply them without rebooting:
   
   ```bash
   sudo sysctl -p
   ```
   

## Long query error

You may encounter the following error when using the **On-prem files** connector with a database connector, such as **MySQL**:

```
Long query error: java.lang.IllegalArgumentException: Missing files profile laws rds cx
```

This error occurs when the **On-prem files** connector and a database connector use different on-prem groups. Set both connections to use agents in the same on-prem group to resolve this error.

---

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

---
