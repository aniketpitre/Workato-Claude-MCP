# On-prem

42 pages. Paths are relative to the repository root.


## On-prem

- **On-prem connectivity** - `kb/docs/en/on-prem.md` - Learn how the Workato on-prem agent creates a secure tunnel from your private network to Workato cloud to access databases, files, and apps behind firewalls.
- **On-prem agent** - `kb/docs/en/on-prem/agents.md` - The Workato on-prem agent securely connects recipes to on-prem apps, databases, and folders without opening ports in your firewall.
- **On-prem agent - Connections using an on-prem agent** - `kb/docs/en/on-prem/agents/connection.md` - Learn how on-prem agent connections route requests from your private environment using cloud profiles or connection profiles.
- **On-prem agent - OPA Smart Shunt** - `kb/docs/en/on-prem/agents/opa-smart-shunt.md` - Learn how OPA Smart Shunt moves data directly between on-premise systems to stay compliant and avoid network latency and transfer quotas.
- **On-prem group** - `kb/docs/en/on-prem/groups.md` - Learn how on-prem groups pool Workato on-prem agents for high availability through fault tolerance and load balancing.
- **On-prem quotas** - `kb/docs/en/on-prem/limits.md` - Reference for Workato on-prem connectivity quotas, including default values and notes for on-prem agents and groups.
- **On-prem agent (OPA) error troubleshooting** - `kb/docs/en/recipes/design-time-errors/opa-errors.md` - Troubleshoot common Workato on-prem agent (OPA) errors covering setup, upgrades, runtime behavior, connections, and how to locate and read OPA logs.

## On-prem agent

- **On-prem agent - Automatic alerts** - `kb/docs/en/on-prem/agents/alert.md` - Configure automatic email alerts for an on-prem group to get notified when an agent disconnects or a certificate nears expiration.
- **On-prem agent version deprecation** - `kb/docs/en/on-prem/agents/deprecation.md` - Reference for Workato on-prem agent version deprecation and sunset dates, with the upgrade schedule to avoid recipe disruptions.
- **On-prem agent - Extensions** - `kb/docs/en/on-prem/agents/extension.md` - Connect legacy on-prem applications to Workato recipes by registering Java extensions as REST endpoints in the on-prem agent.
- **On-prem agent - Key management** - `kb/docs/en/on-prem/agents/key.md` - Create and renew the cert.key and cert.pem files that connect a Workato on-prem agent to the cloud through a gateway.
- **On-prem agent - Logging** - `kb/docs/en/on-prem/agents/logging.md` - Learn how the Workato on-prem agent logs activity, warnings, and traces, including the rotation schedule and retention quotas.
- **On-prem agent - Monitoring** - `kb/docs/en/on-prem/agents/monitoring.md` - Enable the Prometheus-compatible metrics endpoint and health checks on the Workato on-prem agent to monitor CPU, memory, JVM, and connector activity.
- **On-prem agent - Password Encryption** - `kb/docs/en/on-prem/agents/password-encryption.md` - Encrypt passwords and private keys in the on-prem agent config file using the OPA encryptor tool to secure sensitive data.
- **On-prem agent - Proxy Server Support** - `kb/docs/en/on-prem/agents/proxy.md` - Set up proxy server access for a Workato on-prem agent operating in an environment with limited internet connectivity.
- **On-prem agent - Run an on-prem agent** - `kb/docs/en/on-prem/agents/run.md` - Start an existing Workato on-prem agent on Windows, Linux, Mac, or Docker, and reconnect an agent to Workato.
- **On-prem agent - Secrets Manager** - `kb/docs/en/on-prem/agents/secrets-manager.md` - Use an external secrets manager with the Workato on-prem agent to manage passwords without storing them in config files.
- **Configuring AWS Secrets Manager for on-prem agent** - `kb/docs/en/on-prem/agents/secrets-manager/amazon-web-services-secret-manager.md` - Configure AWS Secrets Manager with the Workato on-prem agent to store secrets using cloud profiles or connection profiles.
- **Configuring Google Secret Manager for on-prem agent** - `kb/docs/en/on-prem/agents/secrets-manager/google-secret-manager.md` - Configure Google Secret Manager with the Workato on-prem agent to store database credentials for cloud profiles and connection profiles.
- **Configuring HashiCorp Vault For on-prem agent** - `kb/docs/en/on-prem/agents/secrets-manager/hashicorp-vault.md` - Configure HashiCorp Vault as a secrets engine for Workato on-prem agent cloud profiles, without manually editing the config.yml file.
- **Configuring Microsoft Azure Key Vault for on-prem agent** - `kb/docs/en/on-prem/agents/secrets-manager/microsoft-azure-key-vault.md` - Configure Microsoft Azure Key Vault with the Workato on-prem agent to securely store and access secrets for cloud and connection profiles.
- **On-prem group - Settings** - `kb/docs/en/on-prem/agents/settings.md` - Configure logging, IP allowlists, and email alerts for your Workato on-prem agents from the on-prem group Settings page.
- **On-prem agent - Stop an on-prem agent** - `kb/docs/en/on-prem/agents/shutdown.md` - Stop a Workato on-prem agent safely using the shutdown script or SIGTERM, and disable it in Workato to reroute actions before restarting.
- **On-prem agent - Upgrade an agent** - `kb/docs/en/on-prem/agents/upgrade.md` - Upgrade your Workato on-prem agent to a new version with zero downtime or by replacing the existing agent.
- **On-prem agent version notes** - `kb/docs/en/on-prem/agents/versions.md` - Release notes for Workato on-prem agent versions, including new features, fixes, and version deprecation details.
- **On-prem add agent FAQs** - `kb/docs/en/on-prem/groups/add-agent/add-agent-faqs.md` - Answers to common questions about adding Workato on-prem agents, including supported operating systems and activation codes.
- **Deploy an on-prem agent using a Docker image** - `kb/docs/en/on-prem/groups/add-agent/docker.md` - Deploy a Workato on-prem agent using a Docker image, from retrieving the agent to running it in your on-prem group.
- **Install an on-prem agent using the DEB Linux package** - `kb/docs/en/on-prem/groups/add-agent/linux-deb.md` - Install a Workato on-prem agent on Debian or Ubuntu using the DEB Linux package, run as the workato system user.
- **Install an on-prem agent using the RPM Linux package** - `kb/docs/en/on-prem/groups/add-agent/linux-rpm.md` - Install a Workato on-prem agent on Red Hat, Fedora, or CentOS using the RPM Linux package, run as the workato system user.
- **Install an on-prem agent on Mac** - `kb/docs/en/on-prem/groups/add-agent/macos.md` - Install a Workato on-prem agent (OPA) on Mac to connect on-premises apps and databases to your recipes.
- **Install an on-prem agent on Windows** - `kb/docs/en/on-prem/groups/add-agent/windows.md` - Install a Workato on-prem agent (OPA) on Windows to connect on-premises apps and databases to your recipes.

## On-prem connections

- **On-prem agent - Cloud Profiles** - `kb/docs/en/on-prem/agents/connection/cloud.md` - Set up on-prem agent connections directly in Workato with cloud profiles, without editing a config file on the agent's machine.
- **On-prem agent connections - FAQS** - `kb/docs/en/on-prem/agents/connection/on-prem-faq.md` - Answers to common questions about on-prem agent connections, cloud profiles, and connection profiles in Workato.
- **On-prem agent - Connection Profiles** - `kb/docs/en/on-prem/agents/connection/profile.md` - Set up on-prem agent connection profiles in the config.yml file to identify and connect to each on-prem application.

## On-prem group

- **On-prem agent - Add an agent to an on-prem group** - `kb/docs/en/on-prem/groups/add-agent.md` - Add an on-prem agent to a Workato on-prem group, set the agent name, and select the operating system where you install it.
- **On-prem group - Configuration file** - `kb/docs/en/on-prem/groups/common-config.md` - Learn how the on-prem agent config.yml file stores connection profiles and why agents in a group must share identical configuration.
- **On-prem group - Create group** - `kb/docs/en/on-prem/groups/create-group.md` - Create an on-prem group in Workato to organize on-prem agents and set the connection type used to reach on-premises resources.
- **On-prem group - Status** - `kb/docs/en/on-prem/groups/group-status.md` - Learn how on-prem group and agent statuses work in Workato, including agent states, certificate expiration, and agent details.

## On-prem troubleshooting

- **On-prem connection issues** - `kb/docs/en/on-prem/agents/opa-troubleshooting/troubleshoot-opa-connections.md` - Troubleshoot Workato on-prem connection issues, including SDK extension startup and SFTP and Kafka connection errors.
- **On-prem runtime and performance issues** - `kb/docs/en/on-prem/agents/opa-troubleshooting/troubleshoot-runtime.md` - Troubleshoot Workato on-prem agent runtime issues, including heap space errors, logging errors, long query errors, and stuck jobs.
- **On-prem setup and installation issues** - `kb/docs/en/on-prem/agents/opa-troubleshooting/troubleshoot-setup.md` - Troubleshoot Workato on-prem agent setup and installation issues caused by permissions, invalid config files, or environment restrictions.
- **On-prem upgrade and configuration issues** - `kb/docs/en/on-prem/agents/opa-troubleshooting/troubleshoot-upgrade.md` - Troubleshoot Workato on-prem agent upgrade and configuration issues, including service accounts, keys, and connection profiles.
