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
