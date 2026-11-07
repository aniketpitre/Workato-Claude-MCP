---
url: 'https://docs.workato.com/en/on-prem/agents/versions.md'
description: >-
  Release notes for Workato on-prem agent versions, including new features,
  fixes, and version deprecation details.
---

# On-prem agent version notes

The latest version of the Workato on-prem agent (OPA) is `v34.0`.

Learn more about how to [upgrade your OPA version](/en/on-prem/agents/upgrade).

* * *

> **VERSION DEPRECATION**
> 
> On-prem agent versions older than 2.19.0 were sunset on January 8, 2026.
> 
> Refer to the [On-prem agent version deprecation](/en/on-prem/agents/deprecation) guide for more information.

## v34

### v34.0

_Released October 30, 2026_

- **Solace**: New Message batch trigger, added manual ACK for Receive Messages Batch action.
- **MCP**: Added MCP access via OPA.
- **SQL Server**: Added partial load support for Bulk Load action.
- **SQL Server**: Added name-based column mapping for Bulk Load action.
- **SQL Server**: Added support for `DateTimeOffset` type as a date-time in a Run Custom SQL action.
- **Modules**: Added support for OPA modular build.
- **SAP**: Fixed agent failure on large batches.
- **Security**: Updated Java Runtime to version `21.0.13+9`, updated libraries according to the OWASP scanner recommendations.

## v33

### v33.1

_Released October 14, 2026_

- **SAP**: Updated the SAP JCo libraries to version `3.1.14`.
- **SAP**: Optimized the retrieval of ALE and `IDoc` configuration for `IDoc` triggers by filtering by program ID on the SAP side. Unrelated or misconfigured ALE entries are no longer fetched.
- **SAP**: Fixed an issue where one SAP connection failing to start its `IDoc` listener prevented other SAP subscriptions on the same on-prem agent from starting.
- **PostgreSQL**: Added support for the `BIT` data type.
- **Kafka**: Fixed a bug for transactional message handling.
- **Security**: Updated libraries according to the OWASP scanner recommendations, including Spring upgrade to version `7.0.9`.

### v33.0

_Released August 17, 2026_

- **Solace**: Added a [Solace](/en/connectors/solace) connector based on the Solace JCSMP API.
- **SQL Server**: Increased the CSV character limit to 100,000,000 for the [Bulk load from on-prem file](/en/connectors/mssql/bulk-load-from-on-prem-file) action.

## v32

### v32.2

_Released July 31, 2026_

- **SAP**: SAP connection profile YAML config property `quality_of_protection` now accepts both integer and string values.
- **SAP**: Fixed an issue introduced in OPA v32.1 where the `IDoc` parser failed to support `IDocs` with multiple top-level segments.
- **Database**: `NULL` and empty strings are now distinct for CSV export and import. SQL `NULL` corresponds to an unquoted empty value `(,,)` and an empty string corresponds to a quoted empty value `(,"",)`.
- **Database**: CSV export of `TIMESTAMP WITHOUT TIME ZONE` (Postgres, Redshift) and `DATETIME` (MySQL) columns now conforms to ISO 8601 and uses `T` as the separator between date and time.
- **Security**: Updated libraries according to the OWASP scanner recommendations.

### v32.1

_Released Jun 26, 2026_

- **SAP**: Optimized `IDoc` processing in non-Unicode SAP systems and introduced support for multibyte character encodings.
- **Security**: Updated libraries according to the OWASP scanner recommendations.

### v32.0

_Released May 21, 2026_

- **SAP**: Made the `IDoc` schema cache invalidation interval configurable at the SAP connection level.
- **Kafka**: Fixed timeout setting.
- **Database**: Bulk insert improvements.
- **Oracle**: Fixed handling of `NULL` values in `REF_CURSOR` stored procedure parameters.
- **Hardening**: Improved OPA connectivity for slow networks.
- **Monitoring**: Added a [Prometheus endpoint](/en/on-prem/agents/monitoring) for OPA service monitoring.
- **Security**: Updated libraries according to the OWASP scanner recommendations.

## v31

### v31.1

_Released March 24, 2026_

- **Database**: Improved asynchronous tasks management.
- **Database**: Fixed `Hikari Connection Pool` error when using secrets.
- **Oracle**: Increased maximum BLOB size to 50MB.
- **On-prem files**: Improved handling of timeouts for list file operations.
- **Kafka**: Fixed bug for `OAUTHBEARER SASL` mechanism (affected OPA 31.0).

### v31.0

_Released February 10, 2026_

- **JMS**: New `Receive message from queue` action.
- **Kafka**: New `Publish messages` batch action.
- **SAP**: Added compatibility with SAP `JCo 3.1.13`.
- **SAP**: Improved scalability scenarios and correct suspension of `IDoc` handlers when OPA is disabled.
- **SAP**: Corrected formatting of `IDoc` Status messages to include parameter substitution from `EDIDS`.
- **SQL**: Upgraded SQL Server JDBC driver.
- **Security**: Updated libraries according to the OWASP scanner recommendations.
- **Monitoring**: Removed the [`manual monitoring`](/en/on-prem/agents/monitoring) feature along with related dependencies.

## v30

### v30.0

_Released December 3, 2025_

When installing OPA on Windows, you can choose to store the certificate and private key in Windows Certificate Store (default option) or in the OPA `conf` folder (previous functionality). Refer to the [Windows OPA](/en/on-prem/groups/add-agent/windows#security) guide for more information.

- **Security**: Windows Certificate Store can now store the certificate and private key.
- **JMS**: Added support for JMS message properties and headers.
- **JMS**: Added support for Solace along with OAuth2 authentication.
- **Oracle**: Extended Execute Stored Procedure action with support for long queries (up to 24 hours).
- **FTP**: Fixed issue with character encoding.
- **Security**: Updated libraries according to the OWASP scanner recommendations.

## v29

### v29.1

_Released October 31, 2025_

- **Data pipelines**: Added support for SQL Server as a data destination.
- **Security**: Updated Spring LDAP to version `3.2.14`.

### v29.0

_Released October 08, 2025_

- **SAP**: Enhanced stability in SAP `IDoc` listener initialization and connection management.
- **Configuration**: Fixed bug for creating duplicate connections, e.g., in case of connection pooling.
- **Kafka**: Improved support for Protobuf and schema registry.
- **Logging**: Added support for json output format.

## v28

### v28.1

_Released July 31, 2025_

- **SAP**: New [`Send IDoc (Advanced)`](/en/connectors/sap/action-send-idoc-advanced) action that includes re-designed logic to fetch the schema.

### v28.0

_Released July 10, 2025_

- **Oracle**: Added support for `REF CURSOR` as an OUT parameter type for stored procedures.
- **SAP**: Restricted schema fetching to only remotely enabled functions (FMs).
- **SAP**: Upgraded SAP IDoc to version `3.1.4`.
- **SAP**: Upgraded SAP JCo to version `3.1.12`.
- **SMB**: Extended SMB download file support up to 100GB.
- **Hardening**: Improved OPA connectivity for not stable network conditions.
- **Security**: Fixed [encryptor](/en/on-prem/agents/password-encryption) tool.
- **Security**: Updated libraries according to the OWASP scanner recommendations.

## v27

### v27.1

_Released May 21, 2025_

- **SAP**: Improved performance of segment loading in IDoc batch processing.
- **SAP**: In `Send IDoc` action, refactored the logic to include all Custom IDocs in the picklist.
- **SAP**: In `New IDocs` trigger, added display of partner type and number (`RCVPRT`, `RCVPRN`) alongside the IDoc type they belong to.
- **JDBC**: Simplified connection check.

### v27.0

_Released March 25, 2025_

- **SMB**: Added support for on-premise [SMB](/en/connectors/smb).
- **Kafka**: Added support for JSON format in schema registry.
- **SAP**: Upgraded to SAP JCo `3.1.11`.
- **SAP**: Added compatibility with legacy SAP JCo versions (`3.0.*`).
- **SAP**: Added detailed error messages in `Check IDoc Status`.
- **FTPS**: Fixed a connectivity error for some of FTP servers.
- **Configuration**: The `config.yml` file is no longer required to run the OPA when using cloud profiles. The default permissions in the Linux and Docker config directory are set to be accessible by the Workato dedicated user only.
- **Other**: The `JAVA_OPTIONS` environment variable may be used to pass additional parameters directly to the Java Runtime running OPA on all platforms, including Docker.

## v26

### v26.0

_Released January 17, 2025_

From this version onward, the on-prem agent is available as a single package for all data centers. While the packages with the suffixes `-eu`, `-sg`, `-jp`, and `-au` will still work, they are no longer supported.

- **Configuration**: Introduced a unified package for all data centers.
- **FTP**: Fixed bugs affecting Windows-based FTP servers.

## v25

### v25.1

_Released December 18, 2024_

- **Kafka**: Improved trigger throughput.
- **FTPS**: Added session resumption support for TLS 1.2.
- **SAP**: Fixed duplication of IDoc types with custom extensions.
- **SAP**: Enhanced recognition of IDoc statuses for the `Send IDoc` action.
- **Security**: Updated libraries according to the OWASP scanner recommendations.

### v25.0

_Released October 29, 2024_

- **FTP**: Added support for on-premise [FTP](/en/connectors/ftp).
- **SAP**: Provided detailed error messages for known SAP JCo failures.
- **SAP**: Use the latest schema for RFC, BAPI and IDoc without restarting OPA.
- **SAP**: Extended timeout for updating outbound IDoc status to ensure stability on poor network connections.
- **SFTP**: Improved logging for troubleshooting purposes.
- **MSSQL**: Fixed issue when connecting to SQL Server with Windows Authentication.
- **Logging**: Fixed repetitive `request has been canceled` errors in logs.
- **Security**: Updated JRE to `21.0.5+11`, Jetty to `12.0.14`, Spring to `6.1.14`, and other libraries according to OWASP recommendations.

## v24

### v24.3

_Released August 23, 2024_

- **SAP**: Aligned order of fields in `RFC_READ_TABLE` requests for compatibility with legacy SAP systems.
- **Security**: Updated libraries according to the OWASP scanner recommendations.

### v24.2

_Released July 8, 2024_

- **Kafka**: Fixed "Consumer is not ready" occasional error when restarting a recipe with real-time trigger.
- **SAP**: Added metadata for a table queried by "Call RFC" action.
- **Server**: Avoid unexpected timeouts when accessing a slow database.

### v24.1

_Released June 27, 2024_

- **SAP**: Improved `Call BAPI` action, allowing easier navigation in the catalog of available BAPI methods.
- **SAP**: Fixed loading of IDoc segments. Added support for segment nesting levels up to 128.

### v24.0

_Released June 10, 2024_

- **SFTP**: Added support for on-premise [SFTP](/en/connectors/sftp).
- **SAP**: Removed the metadata cache for IDoc types. All required data is now retrieved on-demand from the SAP server. This change saves agent memory and improves operational consistency.
- **SAP**: Added support for SAP JCo version `3.1.9 (2024-03-19)`, including the `sapjco3.jar` and corresponding native binary libraries. Workato recommends that you use the latest version of SAP JCo with OPA, however, Workato still provides support for JCo versions with the major release `3.0.x` in partial compatibility mode.
- **SAP**: Added support for more precise identification of the Distribution Model for Inbound IDocs.
- **Security**: Updated libraries according to the OWASP scanner recommendations.
- **Cloud logging**: Fixed a bug that caused log spamming when debugging was enabled.

## v23

### v23.2

_Released May 17, 2024_

- **Security**: updated Java runtime and libraries according to OWASP scanner recommendations.
- **Database**: fixed bug when agent becomes unresponsive when database request is canceled.
- **Cloud logging**: improved data transfer algorithm to reduce losses when a lot of messages appear.
- **Linux**: fixed bug where logs were not produced after package upgrade.

### v23.1

_Released March 26, 2024_

- **Kafka**: improved trigger stability in case of network failures.
- **Kafka**: updated `Avro` to 1.11.3, `kafka-avro-serializer` and `kafka-protobuf-serializer` to 7.6.0.
- **SAP**: optimized memory usage of metadata for RFM and BAPI.
- **SAP**: fixed bug when RFM name contains unsafe URL characters.
- **Database**: added support for synchronous actions cancellation.

### v23.0

_Released February 8, 2024_

OPA 23.0 is the minimum required version for use with the [Workato Logging Service](/en/features/logging-service). This release includes a major Java runtime and language upgrade, the agent now uses the latest 21 LTS version.

- **Kafka**: added support for Protobuf schema format.
- **HTTP**: the agent now correctly handles cases where the remote server responds before the request completes.
- **HTTP**: requests can now pass through a configured proxy server.
- **Hardening**: fixed bug where agent failed to reconnect when using a proxy server.
- **JMS**: fixed message parsing when sending from non-JMS applications.
- **TLS**: added support for ECC private keys and certificates.
- **MS SQL**: fixed connection problem when using `ActiveDirectory` authentication method.
- **SAP**: implemented sending IDoc batches to Workato webhook.
- **SAP**: support for receiving outbound IDocs from SAP for all partner types.
- **SAP**: keep `NUMC` data types as strings instead of integers.
- **Security**: updated Java to version 21.0.2+13.
- **Security**: updated `Spring Framework` to version 6.1.2, `Spring Boot` to 3.2.2, `AWS SQS` messaging library to 2.1.1.

## v22

### v22.2

_Released January 17, 2024_

- **Hardening**: fixed excessive memory consumption when using asynchronous actions.
- **Kafka**: fixed SSL configuration for cloud profiles.
- **Logging**: print more details when a shutdown signal is received.
- **SAP**: implemented functionality to manage IDoc batches.
- **SAP**: added customization capability for the `EDI_DC40` segment fields.

### v22.1

_Released December 22, 2023_

- **Security**: upgraded several libraries following OWASP recommendations.
- **Linux**: fixed RPM OPA upgrade process.
- **Linux**: fixed graceful shutdown script.
- **JMS**: fixed resolution of `mqcsp` property in IBM MQ configuration.
- **Files**: performance improvements for List files action.
- **Logging**: reduced amount of logs with debugging enabled.
- **MS SQL**: added SSL configuration support.
- **Docker**: starting and activating OPA can be done with a single command.
- **Kafka**: fixed support for SSL configuration. Added the option to provide a password for the client key file.

### v22.0

_Released November 2, 2023_

On-prem agent is now available as a docker image. Refer to [Install on-prem agent with Docker](/en/on-prem/groups/add-agent/docker) for installation instructions.

- **Security**: updated Java runtime to version 17.0.9+9.
- **MySQL**: updated JDBC driver to version 8.2.0.
- **Monitoring**: fixed initialization error when starting agent with monitoring feature enabled.
- **Hardening**: fixed rare reconnection bug when using a proxy.
- **Hardening**: fixed memory consumption for long-running agents.
- **Configuration**: reduced default graceful shutdown timeout to 30 seconds.

## v21

### v21.2

_Released October 16, 2023_

Added dedicated OPA distributions as part of the Australian data center release.

- **JMS**: fixed Jakarta EE compatibility issue with IBM MQ JMS driver.
- **SAP**: improved IDoc type validation.
- **SAP**: resolved `EDI_SEGMENTS_ADD_BLOCK is empty` bug.
- **SAP**: fixed agent shutdown behavior with SAP profiles being active.

### v21.1

_Released August 16, 2023_

- **Security**: updated Java runtime to version 17.0.8+7 and several other libraries to the latest versions as recommended by the vendors.
- **NTLM**: fixed bug with the HTTP status code handling.

### v21.0

_Released July 28, 2023_

Starting with this release, the Workato on-prem agent uses a simplified versioning scheme: major and minor version numbers only (21.0 instead of 2.21.0).

- **MS SQL**: added support for RFC 4180 specification in CSV bulk load (e.g. support for newlines in values).
- **Secrets**: added support for [Workato cloud secrets manager](/en/security/data-protection/secrets-management/secrets-management) and [clear secrets cache](/en/workato-api/environment-management#clear-secrets-management-cache) mechanism. Please note that clearing the secrets cache is not supported for the following on-premise connections: Kafka, SAP, JMS, and database with the connection pooling option enabled. These connectors require manual reconnection after the secret is rotated.
- **Linux**: added SHA-256 signature support for RPM packages to comply with the latest Red Hat Linux releases.
- **Usability**: fixed behavior when multiple agents connect with the same key. From now on, only the first connected agent keeps working while others shut down automatically.
- **Windows**: removed dependency on `vcruntime` binary, the installer doesn't ask for additional DLL anymore.
- **Logging**: reduced amount of log events when running in debug mode.
- **Extensions**: fixed auto-injection bug while using `jakarta.inject.Inject` annotation.
- **Security**: updated libraries according to the OWASP scanner recommendations.
- **Monitoring**: added telemetry for asynchronous operations.
- **SAP**: improved reliability of metadata load process.

## v2.20

### v2.20.0

_Released June 15, 2023_

This release migrates from the deprecated Java EE to the latest revision of the Jakarta EE API. If you are using extensions or custom JMS drivers, check their compatibility with the Jakarta EE specification before upgrading.

- **Security**: upgraded the following middleware libraries `Spring` to 6.0.9, `Jetty` to 11.0.15, `Spring LDAP` to 3.1.0.
- **Security**: added new privileges for on-prem files and on-prem command line scripts connections. [Learn more](/en/privileges#on-premise)
- **Kafka**: added new real-time `New message in topic` single and batch triggers. We recommend using these updated versions of the trigger as it guarantees higher reliability, especially when a recipe is stopped and started again. The previous Kafka triggers are still supported but were marked as deprecated.
- **Kafka**: fixed a bug that caused misconfiguration with the `sasl.jaas.config` property.
- **Redshift**: added microseconds to timestamps to avoid row collisions.

## v2.19

### v2.19.0

_Released May 24, 2023_

This release introduces the new activation flow for on-prem agents. For newly created agents, the private key used for the encryption of data transfers is now automatically generated and stored locally.

Refer to [Add on-prem agent](/en/on-prem/groups/add-agent) for the updated Windows OS installation flow. Additionally, you can find updated installation flow for [Linux DEB package](/en/on-prem/groups/add-agent/linux-deb) and [Linux RPM package](/en/on-prem/groups/add-agent/linux-rpm).

- **Security**: improved PKI activation flow.
- **Security**: trust certificates issued by `Let's Encrypt` by default.
- **Security**: upgraded several libraries following OWASP recommendations.
- **RecipeOps**: This version supports new [Workato RecipeOps trigger](/en/connectors/recipeops/triggers/opa-disconnected) to monitor unexpected on-prem agent connectivity issues.
- **System**: agent performance data is now sent to Workato for future analysis and improvements; no additional configuration is required. Refer to [Logging OPA activity](/en/on-prem/agents/logging#logging-opa-activity) for more information.
- **System**: cloud logging feature no longer requires additional configuration.
- **MS SQL**: added support for `useFmtOnly` connection property.
- **MySQL**: added support for `year` date type.
- **Kafka**: improved validation of `SASL` configuration.

## v2.18

### v2.18.1

_Released May 16, 2023_

- **SAP**: fixed schema generation and retrieval of custom-enhanced IDocs.
- **SAP**: fixed `Data was lost while copying a value` error when loading RFMs.

### v2.18.0

_Released March 10, 2023_

- **Security**: Java runtime upgraded to version 17.0.6+10.
- **Security**: PostgreSQL database driver updated to version 42.5.4.
- **JMS**: added redelivery options for ActiveMQ, by default number of retries is now unlimited.
- **Debug**: print full certificate details when TLS handshake fails.
- **Windows**: default encoding changed to UTF-8.
- **Windows**: installation updated to use the latest Windows service wrapper library.
- **Windows**: OPA windows service user account is set to `Local Service` instead of `Local System` used in previous versions.

## v2.17

### v2.17.1

_Released February 1, 2023_

- **SAP**: fixed multiple connections issue.

### v2.17.0

_Released January 26, 2023_

- **JMS, Kafka, SAP**: additional firewall configuration for these triggers is no longer required.
- **Security**: switched to TLSv1.3 for gateway tunnel connections.
- **Performance**: disabled buffering for database-related requests to reduce memory consumption.
- **Kafka**: added support for AVRO-encoded message keys.
- **Kafka**: upgraded `kafka-clients` library to version `7.3.1-ccs`.
- **SAP**: added support for `TYPE_UTCLONG` data type.
- **SAP**: implemented stateful RFC support, minimum required `SAP JCo` library version is 3.1.7.
- **MySQL**: fixed timezone issue for datetime columns in version 8.\*.
- **MySQL**: result set streaming is enabled by default.

## v2.16

### v2.16.0

_Released December 16, 2022_

This release introduces more strict approach to validation of third-party TLS certificates, potentially affecting behavior of on-prem HTTP connector. Using self-signed certificates may require additional setup, see [On-prem http profile](/en/on-prem/agents/connection/profile#http-profile) for details.

- **HTTP**: trustAll default behavior is changed, added support for self-signed certificates and mTLS.
- **HTTP**: fixed Bad Request errors while using encoded characters.
- **JMS**: connector no longer uses local database to store JMS subscriptions. Support for High Availability mode has been added.
- **Kafka**: added support for message headers.
- **Security**: upgraded `Vertx`, `Netty` and `Jetty` libraries to the latest versions.
- **Database**: added bulk triggers support.
- **Linux**: added fontconfig and bash dependencies for Linux DEB/RPM packages.
- **SAP**: dropped support of SAP JCo 3.0. Minimum required version is SAP JCo 3.1.7.
- **SAP**: SAP RFC connector does not attempt to subscribe for inbound IDocs if `program_id` is missing.
- **SAP**: SAP RFC connector ignores redundant IDoc release version.
- **SAP**: system information can be retrieved even if EP8 is not installed (Error `JCoTable of type TT_INSTTU is empty`). On-prem agent have to be explicitly authorized to use function module `OCS_GET_INSTALLED_SWPRODUCTS`.

## v2.15

### v2.15.0

_Released November 4, 2022_

- **Configuration**: added [cloud profiles](/en/on-prem/agents/connection/cloud) support which allows setting up on-prem connections directly in Workato.
- **JMS**: added support for headers and binary messages.
- **Network**: rolled back to default TLS implementation and SNI.
- **Network**: fixed bug during gateway reconnection.
- **Security**: upgraded to JRE 17.0.5+8.
- **Security**: upgraded Commons Text library.

* * *

## v2.14

### v2.14.1

_Released October 12, 2022_

- **Encryptor tool**: fixed initialization error after libraries upgrade.
- **Network**: added support for DNS requests through proxy.
- **Command-line scripts**: added error output into process execution result with non-zero exit code.
- **Security**: added TLS `strict` option for HTTP and SSL configuration.
- **Linux DEB/RPM**: fixed errors during package re-installation.
- **SAP**: connector doesn't use local file to store IDoc subscriptions and supports HA mode.

### v2.14.0

_Released September 16, 2022_

- **Security**: replaced internal agent web server to improve security and performance. This server doesn't use any port on localhost for processing requests by default. Launch options `bind`, `port` and `public` are no longer valid and will be completely removed in the future releases. Deprecated endpoint `/status` is not available anymore.
- **Security**: added an internal feature to route outgoing HTTP requests throughout the gateway instead of direct calls to `*.workato.com` domain.
- **Security**: fixed behavior when several agents are running with the same certificates. Now latest launched instance will continue to run while conflicting ones shutdown gracefully.
- **Security**: log events with `TRACE` level aren't sent into cloud storage anymore (if cloud logging feature is used).
- **Monitoring**: added new option `monitoring`. When enabled the agent records internal statistics related to resource utilization and performance. This data can be observed via UI using local management endpoint or exported for faster issues root cause analysis. [Learn more](/en/on-prem/agents/monitoring)
- **Configuration**: completely reworked static configuration parsing to unify errors and used value types.
- **Configuration**: added ability to disable cloud secrets caching for database properties. [Learn more](/en/on-prem/agents/connection/profile#database-profile)
- **Azure Key Vault**: added support for [Azure credentials encryption](/en/on-prem/agents/secrets-manager/microsoft-azure-key-vault#prerequisites).
- **SAP**: new IDoc trigger now ignores release version specified and uses same release version as SAP instance in all cases. This trigger notifies SAP about IDoc status updates, so it became possible to find undelivered IDocs.

* * *

## v2.13

### v2.13.1

_Released September 7, 2022_

- **On-prem files**: fixed issue with an invalid character in file path on Windows.

### v2.13.0

_Released August 12, 2022_

- **Java upgrade**: Java version and runtime to 17.0.3.
- **Linux distribution**: added [RPM](/en/on-prem/groups/add-agent/linux-rpm) and [DEB](/en/on-prem/groups/add-agent/linux-deb) packages.
- **Shutdown procedure**: agent waits for OS signals, tries to gracefully finish all running queries, and terminates the agent process. You can use option `shutdownTimeoutSeconds` to set a custom shutdown timeout; the default value is 300 seconds (5 minutes). We updated `bin/shutdown.sh` script to support this process. [Learn more](/en/on-prem/agents/shutdown)
- **Cloud logging**: enabled by default. Agent logs are sent to Workato for future improvements and bug fixes.
- **HTTP response compression**: enabled by default. This guarantees better communication throughput, yet can very slightly increase CPU consumption.
- **Health checks**: added `mgmt-listen` command line option to expose a technical endpoint. Workato recommends that you use it in system health checks, to run OPA inside containerized environment. The undocumented `/status` endpoint is deprecated; we will de-support it in future releases.
- **Security improvement**: upgraded several libraries with potential vulnerabilities identified in the security scan.
- **Custom HTTP SSL options**: internal agent communication is no longer affected.
- **Kafka**: added Avro and Schema Registry support.

* * *

## v2.12

### v2.12.2

_Released July 12, 2022_

- **On-prem files**: added actions to delete files and folders
- **MS SQL**: fixed the delimiter issue for bulk load action
- **Active Directory**: fixed error when using a custom attribute as a search filter

### v2.12.1

_Released June 29, 2022_

- **MS SQL on Windows service**: fixed DLL library loading issue
- **SAP**: fixed client number issue with leading zeros
- **PostgreSQL**: fixed issue related to timestamp with timezones
- **Extended logging**: for http 520 error
- **File encoding**: Added support for UTF-8 BOM

### v2.12.0

_Released June 8, 2022_

- **Oracle stored procedures**: Added support for Table/Object type parameters.
- **MySQL JDBC**: Added ability to replace MySQL JDBC driver with a custom version.
- **On-prem connections**: Fixed a connection error caused by on-prem file connections using a root or network base folder.
- **SAP on Windows**: Fixed a Windows service shutdown issue occurring when SAP connections are used.
- **Upgrades**: Removed python as a dependency for the [upgrade Script on Linux and Mac](/en/on-prem/agents/upgrade).

* * *

## v2.11

### v2.11.0

_Released May 21, 2022_

- **On-prem gateway**: Switched to the new on-prem gateway. Added `sg3` and `sg4` to the [allowlist](/en/security/ip-allowlists#on-premise-gateway-addresses).
- **On-prem CSV files**: Added File Encoding Option to On-prem CSV files triggers and actions.
- **SAP connector**: Added support for long-running RFCs in SAP connector.
- **Bulk load**: Added SQL Server Bulk Load support.
- **Upgrades**: Enhanced upgrade script to perform dependency checks.
- **Uploads**: Fixed stale uploads cleanup bug which caused ongoing uploads to be dropped.
- **JMS messages**: Fixed non-numeric message properties in JMS messages.
- **Java Runtime Environment**: Upgraded to 11.0.15+10.

* * *

## v2.10

### v2.10.2

_Released April 25, 2022_

- Support gzip compression for inbound requests
- Upgraded Spring framework to the latest version
- Support for parallel multipart uploads and retries
- Upload folder is not configurable any more: incomplete uploads will use staging directory (or temporary folder if not configured)
- Support for SG Data Center
- Faster connection checks for on-prem file profiles.

### v2.10.1

_Released March 30, 2022_

- Fixed issue causing the upgrade script to fail due to incorrect version comparison
- Improved file cleanup for staging folder
- Configuring a [staging folder](/en/on-prem/agents/connection/profile#server-profile) is no longer required
- Added support for moving staging files into network folders
- Fixed issue with inability to detect running OPA process in the shutdown script of some Linux distros

### v2.10.0

_Released February 24, 2022_

- [OPA Secrets manager](/en/on-prem/agents/secrets-manager) - [Azure Key Vault](/en/on-prem/agents/secrets-manager/microsoft-azure-key-vault) and Google Secret Manager support
- Data compression to improve data throughput performance
- Improved Kafka subscription handling
- TLS support available for PostgreSQL and MySQL
- SQLServer: Built-in support for integrated Windows authentication and Microsoft Entra ID password
- Added support for Active Directory multi-value attributes
- Now all the agents from group reads metadata from SAP during launch
- Server-side SAP configuration is not required when no IDocs are transferred
- There is no need to connect/disconnect SAP manually when OPA is restarted
- Added graceful shutdown script for Linux
- Fixed an issue with parsing of date types for JDBC Export query result action
- Fixed an issue caused by underscores in file profile names
- Fixed some typos in the Windows installer
- Fixed issue with OPA connectivity error on startup

* * *

## v2.9

### v2.9.3

_Released November 30, 2021_

- Support for output parameters in batched SQL statements
- Fixes reporting of uncategorized SQL errors
- Fixes crushing on misspelled HTTP endpoint URL
- Fixes automatic garbage collection for staging folder.

### v2.9.2

_Released September 16, 2021_

- Improved datetime handling support for Oracle
- Fixes usage of directory handles on file scan operations

### v2.9.1

_Released September 1, 2021_

- Fixed issue with metadata returned by on-prem download
- Improved PostgreSQL timestamp parsing
- Fixed issue with moving on-prem file to a network folder
- Fixed problem with running agent on Linux/Mac with folder path containing spaces

### v2.9.0

_Released July 7, 2021_

- Added support for AWS secret manager as a password encryption option
- Support for JMS headers and properties
- Oracle JDBC driver upgraded to version 21c
- Fix for on-prem files overwrite flag
- Configurable BLOB size limit
- Added support for "Collect IDocs" option of SAP Partner Profile
- SAP TIMS data type support
- Fixed metadata caching for input/output of SAP IDocs

* * *

## v2.8

### v2.8.1

_Released April 26, 2021_

- Fixes issues when using Websocket proxy
- Fixes return of multiple datasets from SQL Server stored procedure.

### v2.8.0

_Released March 29, 2021_

- Agent now uses OpenJDK 11
- Fixed issue with RFM/BAPI invocation without IDoc routing
- Parameterized query for Run custom SQL action
- JDBC connector triggers/actions
  - New/updated trigger
  - New/updated batch trigger
  - Insert batch action
  - Insert action
  - Update action
  - Delete action
- Fixed schema issue for on-prem MySQL
- Oracle JDBC driver updated to version 21c.

* * *

## v2.7

### v2.7.2

_Released December 17, 2020_

- Fixed timeout issue with long on-prem files upload
- Added Quote Character support for On-prem file trigger
- Redshift Connector On-premise support for all actions and triggers
  - New row
  - New/updated row
  - New rows (Batch)
  - New/updated rows (Batch)
  - New/updated rows via custom SQL (Batch)
  - New rows via custom SQL (Batch)
  - Select rows
  - Select rows using custom SQL
  - Insert row
  - Update rows
  - Upsert rows
  - Delete rows
  - Run custom SQL
  - Insert rows (Batch)
  - Update rows (Batch)
  - Upsert rows (Batch)
- Fixed issue with Linux/Mac upgrade script used in non-default home folder.

### v2.7.1

_Released October 12, 2020_

- Fixes "input line is too long" error in password encryptor tool on Windows
- Allows returning CLOBs as stored procedure output
- Support for long action SQL queries
- Fixes issue with NTLM-authenticated responses not providing payload on error
- Fixes issue with agent shutdown taking too long.

### v2.7.0

_Released July 22, 2020_

- SAP 2.0 Connector
  - SNC encryption
  - JCo 3.1 support
  - Improved RFC and BAPI performance
  - Added connectivity to multiple SAP RFC destinations simultaneously
  - Improved Config profile format
  - Improved logging
  - Added handling for RAW datatypes
  - Support for custom IDOCs and custom extensions
- IBM MQ JMS-based connectivity
- Allow duplicate HTTP headers when using on-prem HTTP.

* * *

## v2.6

This is a major upgrade from [**v2.5**](#v2-5). In order to improve reliability and throughput, Workato introduced [on-prem groups](/en/on-prem/groups).

On-prem groups help achieve zero downtime for recipes that involves on-prem connections and prevent data and revenue loss through missing SLAs. All critical workflows running on on-prem connections are kept running 100% of the time because recipe can process jobs successfully even when one of the user’s on-prem servers goes down.

To do so, the OPA will be connecting to an expanded set of Workato on-prem gateways. If you are using a firewall allowlist to explicitly allow OPA traffic to the Workato cloud, you may need to expand the [firewall allowlist](/en/security/ip-allowlists#on-premise-agent) accordingly.

Refer to [On-prem groups](/en/on-prem/groups) for more information.

### v2.6.4

_Released June 17, 2020_

- Fixes batch update issue with invoking callback functions more than once.

### v2.6.3

_Released May 27, 2020_

- Fix for SAP connector where IDOCs with Custom extensions did not show.
- Fix for SAP connector for RAW data type handling.
- Fix for SAP connector for nested structures.

### v2.6.2

_Released May 16, 2020_

- Allow large HTTP headers.
- Fixes LDAPS connection issue when using `trustAll` flag.
- Support for SQL update-only queries.
- Improved logging for Active Directory.
- Fix for SQL Server stored procedure issue.

### v2.6.1

_Released March 23, 2020_

- Fixes a connectivity issue in v2.6.0.

### v2.6.0

_Released March 5, 2020_

- Major release.
- Introduce [on-prem groups](/en/on-prem/groups).
- Introduce High Availability (HA) and load balancing.

* * *

## v2.5

Workato On-prem agent now supports database connection pooling to reduce lag between reconnection attempts. Oracle Binary Large Object (BLOB) size limit has been increased.

### v2.5.7

_Released January 17, 2020_

- Fixes the issue with connection pool not recycling connections properly.

### v2.5.6

_Released December 20, 2019_

- Support for database XML types.
- Ensure that command-line script is fully read for background scripts.
- Update MySQL JDBC driver.

### v2.5.5

_Released December 2019_

- Allows canceling database queries on recipe job timeout.
- Fixes Active Directory issue with retrieving a schema.

### v2.5.4

_Released October 31, 2019_

- Support for SAP connector array types.
- Log rotation feature.

### v2.5.3

_Released September 27, 2019_

- Fixes reconnection delay.
- Fixes for SAP connector classpath issue.
- Fixes the issue with uninstalling a Windows service.

### v2.5.2

_Released August 29, 2019_

- Fixes Windows service configuration shortcut.

### v2.5.1

_Released August 1, 2019_

- Fixes proxy authentication issues on initial connect.

### v2.5.0

_Released July 11, 2019_

- Support for database connection pooling.
- Oracle **SELECT** performance enhancements.
- Allow Oracle BLOBs larger than 4000 bytes.
- Added digital signature to Windows Installer.
- Windows installer is now able to deploy several agent instances on the same box.
- Fixes the issue of multiple connection attempts using the same key. When the agent recognizes that two or more agents are using same key, it will stop reconnecting.

---
