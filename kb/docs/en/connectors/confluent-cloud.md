---
url: 'https://docs.workato.com/en/connectors/confluent-cloud.md'
description: >-
  The Confluent Cloud connector lets you automate Kafka streaming workflows:
  publish messages to a topic and trigger recipes on new messages in a topic.
---

# Confluent Cloud

[Confluent Cloud](https://www.confluent.io/confluent-cloud/) is a fully managed event streaming platform based on Apache Kafka. It offers a cloud-native, scalable, and highly available Kafka platform, simplifying the deployment, management, and operation of Kafka clusters.

The Confluent Cloud connector allows you to build real-time data pipelines and streaming applications. It integrates with the [Confluent Cloud Schema Registry](https://docs.confluent.io/cloud/current/sr/index.html), which provides schema management for Kafka and ensures data standardization and compatibility as schemas evolve.

## API version

The Confluent Cloud connector uses the Confluent Cloud API.

## How to connect to Confluent Cloud

Workato supports connecting to Confluent Cloud using [SASL/PLAIN authentication](#authentication-sasl-plain).

## SASL/PLAIN authentication

Complete the following steps to establish a connection to Confluent Cloud:

1. Sign in to your Workato account and navigate to the project where you plan to add your Confluent Cloud connection.
   
2. Click **Create > Connection** or press C+C. Select **Confluent Cloud** as your connection.
   
3. Enter the following information in the provided fields:
   
   ![Configure your connection](/assets/connect.CVwE_0SY.png)_Configure your connection_
   
   - Connection name
     
   - Give this connection a unique name that identifies to which Confluent Cloud instance it is connected.
     
   - Seed brokers
     
   - Provide a comma-separated list of seed brokers in the form of `host:port`.
     
   - Username
     
   - Provide the username for SASL/PLAIN authentication. Refer to our guide on [generating SASL/PLAIN credentials](#credentials) to learn more.
     
   - Password
     
   - Provide the password for SASL/PLAIN authentication. Refer to our guide on [generating SASL/PLAIN credentials](#credentials) to learn more.
     
   - Stream Governance
     
   - Click **Show** to expand hidden fields. This portion of the configuration is required if you plan to use the Confluent Cloud Schema Registry as a source for your message schemas. Refer to our guide on [generating Stream Governance credentials](#stream-governance-credentials) to learn more.
     
     - Stream Governance API URL
       
     - Provide the URL of your Stream Governance API (Schema Registry and Stream Catalog API).
       
     - Stream Governance username
       
     - Provide the username for your schema registry. This value is the Stream Governance API key name in Confluent Cloud.
       
     - Stream Governance password
       
     - Provide the password for your schema registry. This is the Stream Governance API key secret in Confluent Cloud.
       
4. Click **Connect**.
   

### Generate SASL/PLAIN credentials

Complete the following steps to generate SASL/PLAIN credentials:

1. Sign in to your [Confluent Cloud](https://confluent.cloud/) account.
   
2. On the left panel, select **Environments** and click the specific Kafka Cluster to open its overview page.
   
   ![Select a cluster](/assets/cluster.DD3QqK4c.png)_Select a cluster_
   
3. From the left panel, select **Cluster settings**.
   
4. Locate the **Bootstrap servers** entry. This provides you with a list of host and port combinations necessary for configuring your Kafka clients. It typically looks like a list of URLs, for example, `pkd-lzurc.us-west1.gcp.confluent.cloud:9091`, where each entry consists of a host and a port. This is your **Seed brokers** value.
   
   ![Cluster settings](/assets/cluster-settings.cW5hgCop.png)_Find the Bootstrap servers/Seed brokers entry_
   
5. Select **API Keys** from the left side navigation bar.
   
   ![API keys](/assets/api-key-add.DZR9FT7T.png)_Select API keys from the left panel_
   
6. Click **\+ Add key** to create a new API key.
   
7. Copy the **API key** and **API secret**. These values are used as the **Username** and **Password** respectively in the Workato connection settings.
   

### Generate Stream Governance credentials

Complete the following steps to generate Stream Governance credentials:

1. Sign in to your [Confluent Cloud](https://confluent.cloud/) account.
   
2. Select **Environments** from the left navigation bar and click the **Environment** you plan to use.
   
   ![Go to Environments](/assets/cluster.DD3QqK4c.png)_Open Environments_
   
3. Find the **Stream Governance API**, located on the right panel. Copy the **Endpoint** value. This is the **Stream Governance API URL** in the Workato connection settings.
   
   ![Copy Endpoint value ](/assets/stream-gov-url.DaAxQ827.png)_Copy the Endpoint value_
   
4. In the **Stream Governance API** section, under **Credentials** click **{N} keys**.
   
   ![Copy Endpoint value ](/assets/stream-gov-credentials.DghUMd-h.png)_Click {N} keys_
   
5. Click **\+ Add key** to create a new Stream Governance API key.
   
6. Copy the **API key** and **API secret**. These values are used as the **Stream Governance username** and **Stream Governance password** respectively in the Workato connection settings.
   

> **SCHEMA REGISTRY REQUIREMENTS**
> 
> Workato requires Stream Governance credentials for use cases that involve using your Confluent Cloud Schema Registry as a source for your message schemas. The following steps are optional if you plan to use a [common data model](/en/features/common-data-model) as your schema source.

---
