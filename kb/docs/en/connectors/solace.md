---
url: 'https://docs.workato.com/en/connectors/solace.md'
description: >-
  Solace provides an event streaming and management platform built around the
  PubSub+ event broker, which lets applications, microservices, and devices
  publish and subscribe to messages over queues and topics.
---

# Solace

[Solace](https://solace.com/) provides an event streaming and management platform built around the PubSub+ event broker, which lets applications, microservices, and devices publish and subscribe to messages over queues and topics. The `Solace` connector enables you to publish messages to Solace topics and queues, receive messages individually or in a batch from a queue, acknowledge messages received in manual acknowledgement mode, and trigger recipes when new messages arrive on a queue or topic.

> **PRIVATE RELEASE**
> 
> This connector is in private release. Private release features are available in production, but only to selected customers. Contact your Customer Success Manager to enable this feature.

## Prerequisites

You must have the following prerequisites to use the `Solace` connector:

- An active [on-prem agent](/en/on-prem) with a configured on-prem group.
- A Solace PubSub+ broker reachable from that on-prem agent, and its broker URL.
- Credentials for one of the connector's supported authentication types. Refer to the Solace [Configuring Client Usernames](https://docs.solace.com/Configuring-and-Managing/Configuring-Client-Usernames.htm) guide for basic authentication credentials or the Solace [Configuring OAuth Authorization](https://docs.solace.com/Security/Configuring-OAuth-Authorization.htm) guide for OAuth credentials.
- Optional. SEMP management endpoint credentials, if you want Workato to populate the queue name drop-down automatically instead of entering queue names manually.

## Connection setup

The `Solace` connector supports the following authentication types:

- [Basic](#basic-connect)
- [OAuth 2.0](#oauth2-connect)

#### Connect to Solace using Basic authentication

Complete the following steps to set up a basic authentication connection to `Solace` in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Solace` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Use the **On-prem group** drop-down menu to select the on-prem group you plan to use to connect to Solace. Refer to [on-prem agents](/en/on-prem) for more information.
   
6. Enter your Solace broker's host URL in the **Broker URL** field. For example, `tcps://your-broker:55443` for a TLS connection or `tcp://your-broker:55555` for a plaintext connection.
   
7. Optional. Enter the name of the message VPN to connect to in the **Message VPN** field.
   
8. Use the **Authentication type** drop-down menu to select **Basic**.
   
9. Enter your Solace client username in the **Username** field. Refer to the Solace [Client Username Configuration](https://docs.solace.com/Configuring-and-Managing/Configuring-Client-Usernames.htm) guide to generate these values.
   
10. Enter your Solace client password in the **Password** field.
    
11. Optional. Expand the **SEMP management** section to let Workato populate the **Queue name** drop-down automatically in the queue-based trigger and actions, instead of entering queue names manually:
    
    1. Enter your Solace SEMP management endpoint URL in the **SEMP URL** field. For example, `https://your-broker:943`.
       
    2. Enter the credentials for that SEMP endpoint in the **SEMP user name** and **SEMP password** fields.
       
12. Optional. Expand the **Additional connection properties** section and click **Add parameter** to pass extra Solace session properties to the broker. For example, `JCSMPProperties.REAPPLY_SUBSCRIPTIONS`.
    
13. Click **Connect**.
    

#### Connect to Solace using OAuth 2.0 authentication

Complete the following steps to set up an OAuth 2.0 connection to `Solace` in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Solace` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Use the **On-prem group** drop-down menu to select the on-prem group you plan to use to connect to Solace. Refer to [on-prem agents](/en/on-prem) for more information.
   
6. Enter your Solace broker's host URL in the **Broker URL** field. For example, `tcps://your-broker:55443` for a TLS connection or `tcp://your-broker:55555` for a plaintext connection.
   
7. Optional. Enter the name of the message VPN to connect to in the **Message VPN** field.
   
8. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
9. Expand the **OAuth 2.0 settings** section and enter your identity provider's access token endpoint URL in the **Token endpoint** field. Refer to the Solace [Configuring OAuth Authorization](https://docs.solace.com/Security/Configuring-OAuth-Authorization.htm) guide to generate these values.
   
10. Enter your OAuth client's **Client ID** and **Client secret**.
    
11. Optional. Enter one or more scopes in the **Scope** field.
    
12. Optional. Expand the **SEMP management** section to let Workato populate the **Queue name** drop-down automatically in the queue-based trigger and actions, instead of entering queue names manually:
    
    1. Enter your Solace SEMP management endpoint URL in the **SEMP URL** field. For example, `https://your-broker:943`.
       
    2. Enter the credentials for that SEMP endpoint in the **SEMP user name** and **SEMP password** fields.
       
13. Optional. Expand the **Additional connection properties** section and click **Add parameter** to pass extra Solace session properties to the broker. For example, `JCSMPProperties.REAPPLY_SUBSCRIPTIONS`.
    
14. Click **Connect**.

---
