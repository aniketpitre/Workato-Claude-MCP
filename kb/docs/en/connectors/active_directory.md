---
url: 'https://docs.workato.com/en/connectors/active_directory.md'
description: >-
  Connect Active Directory to Workato to automate user, group, and resource
  management. The connector authenticates with LDAP through an on-premise agent
  (OPA).
---

# Active Directory

Active Directory is a directory service developed by Microsoft to manage access to resources in a network. The service runs on a Windows Server.

## How to connect to Active Directory on Workato

The Active Directory connector authenticates with LDAP through an on-prem agent (OPA).

> **CLOUD PROFILE CONFIGURATION**
> 
> You don't need to edit the OPA's `config.yml` file when connecting using a [Cloud profile](/en/on-prem/agents/connection/cloud).

Complete the following steps to set up your Active Directory connection:

1. Enter a **Connection name** that identifies which Active Directory instance Workato is connected to.
   
2. Select an **On-prem group** if your database runs in a network that does not support direct connection. Ensure your on-prem group has an active [on-prem agent](/en/on-prem/agents).
   
3. Provide the profile name defined in your OPA's `config.yml` file in the **On-prem LDAP connection profile** field. This option is only visible when you select an on-prem group that supports [connection profiles](/en/on-prem/agents/connection/profile).
   
4. Provide the LDAP **URL**. Use the format `ldap://myserver.example.com:389` for non-SSL connections or `ldaps://myserver.example.com:636` for SSL connections.
   
5. Enter the **Username** (principal), typically the distinguished name (DN) of an admin user, to authenticate with the LDAP server.
   
6. Provide the **Password** (credentials) for LDAP server authentication.
   
7. Provide the **Base** DN for LDAP requests. This setting ensures all DNs you use or receive in LDAP operations are relative to this LDAP path.
   
8. Expand the **Configure SSL settings** section and configure the following fields if your connection requires SSL encryption:
   
   Configure SSL settings
   
   1. Enter the path for the PEM-encoded certificate or a trusted CA in the **Certificate** field.
      
   2. Enter the full content of a PEM-encoded client certificate in the **SSL certificate** field.
      
   3. Enter the private **SSL certificate key** for mutual SSL setup. This field is required if you specify an **SSL certificate**.
      
   4. Use the **Trust all** drop-down menu to enable or disable self-signed certificates.
      
   
9. Click **Connect** to complete the setup. ![Configured Active Directory connection](/assets/connection.BjMBPzrN.png)_Complete the connection fields and click **Connect**_

---
