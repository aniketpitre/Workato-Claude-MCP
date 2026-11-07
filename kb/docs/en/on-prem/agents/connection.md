---
url: 'https://docs.workato.com/en/on-prem/agents/connection.md'
description: >-
  Learn how on-prem agent connections route requests from your private
  environment using cloud profiles or connection profiles.
---

# Connections using an on-prem agent

A [connection](/en/connections) determines where requests will be made from. With a direct connection, requests will be executed from Workato servers. A connection using an on-prem agent will have requests sent from the environment where the agent is installed in.

> **SUMMARY**
> 
> - An on-prem agent lets you securely send Workato requests from the private environment where the agent is installed.
> - There are two types of on-prem connections: cloud profiles and connection profiles. Connector triggers and actions are the same for either type.
> - Cloud profiles are set up directly in Workato, so you don't need to access the machine where the on-prem agent is installed.
> - Connection profiles are set up manually in a `config.yml` file on the machine where the on-prem agent is installed.

For some of your connections, you may want to specify whether it connects through Workato servers or through your on-prem agent. The triggers and actions available in the chosen connector are the same regardless of your choice of connection. An on-prem app connection needs to point to a specific [connection profile](/en/on-prem/agents/connection/profile) in your on-prem agent.

You can set up a connection for an on-prem agent in two ways:

- **Cloud profile**: Set up the connection directly in Workato. Refer to [Cloud profiles](/en/on-prem/agents/connection/cloud) for more information.
- **Connection profile**: Set up connection details in the on-prem agent config file. Refer to [Connection profiles](/en/on-prem/agents/connection/profile) for more information.

## Cloud profile

[Cloud profiles](/en/on-prem/agents/connection/cloud) allow you to set up a connection directly in Workato, just like for regular connectors. You don't have to open and edit config file of your on-prem agent.

![On-prem group for cloud profiles](/assets/on-prem-cloud-profile.CvVG1H5O.png)_On-prem group for cloud profiles_

### Connecting to database using cloud profile

All database connectors give you the option to connect through an on-prem agent. In the connection fields, select the desired on-prem group from the field labeled **Connection type**.

Once you select the on-prem group that allows [cloud profile configuration](/en/on-prem/groups/create-group) you can set up the connection directly in Workato as for the regular cloud connector. Just fill in the required fields and click **Connect**.

![Database connection using cloud profiles](/assets/on-prem-agent-db-cloud.DxhDh-9a.png)_Database connection using cloud profile_

### Connecting to on-prem file system using cloud profile

All on-prem files connectors must be connected through an on-prem agent. In the connection fields, select the desired on-prem group from the field labeled **On-prem group**.

Once you select the on-prem group, you can fill in the properties for on-prem file system. Click **Connect** to test your connection.

> **MANAGE ON-PREM FILE CONNECTIONS**
> 
> Users must have **Full access** for [Connection - on-prem files](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#on-premise) to create, edit, or delete on-prem file connections.

![On-prem file connection using cloud profile](/assets/on-prem-agent-file-cloud.Dv0a5TWj.png)_On-prem file connection using cloud profile_

## Connection profile

When using [connection profile](/en/on-prem/agents/connection/profile) you have to manually fill in the connection details in the config file of your on-prem agent.

![On-prem group for connection profiles](/assets/on-prem-conn-profile.DPszXNmy.png)_On-prem group for connection profiles_

### Connecting to database profiles using connection profile

All database connectors give you the option to connect through an on-prem agent. In the connection fields, Select the desired on-prem group from the field labeled **Connection type**.

Once you select the on-prem group, enter the **On-prem connection profile** name. This profile name should be the same as what you configured in the `database` section of the `config.yml` configuration file.

In the following example, we are connecting to a SQL Server database with the profile name `production`.

```yaml
database:
  production:
    adapter: sqlserver
    host: localhost
    username: me
    password: foobar
```

When configuring a SQL Server connection to this profile, we will need to provide the profile name accordingly.

![Database connection using on-prem agent ](/assets/database-opa-connection.COgajhcm.png)_Database connection using on-prem agent_

### Connecting to on-prem file system profiles using connection profile

All on-prem files connectors must be connected through an on-prem agent. In the connection fields, Select the desired on-prem group from the field labeled **On-prem group**.

Once you select the on-prem group, enter the **On-prem connection profile** name. This profile name should be the same as what you configured in the `files` section of the `config.yml` configuration file.

```yaml
files:
  hrfiles:
    base: "C:/Documents/HR"
```

When configuring an on-prem files connection to this profile, we will need to provide the profile name accordingly.

> **MANAGE ON-PREM FILE CONNECTIONS**
> 
> Users must have **Full access** for [Connection - on-prem files](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#on-premise) to create, edit, or delete on-prem file connections.

![On-prem file connection using on-prem agent](/assets/files-opa-connection.DDxNlrS1.png)_On-prem file connection using on-prem agent_

## Next Steps

- [Upgrade your on-prem agent](/en/on-prem/agents/upgrade)
- [Avoid exposure of any sensitive data by using the encryptor tool provided](/en/on-prem/agents/password-encryption)
- [Run your on-prem agent in environments with limited internet connectivity](/en/on-prem/agents/proxy)
- [Connect to legacy applications using Java](/en/on-prem/agents/extension)

---
