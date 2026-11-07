---
url: 'https://docs.workato.com/en/connectors/kafka.md'
description: >-
  Connect Apache Kafka to Workato to automate event streaming workflows by
  consuming and publishing messages to topics on your Kafka cluster.
---

# Apache Kafka

[Apache Kafka](https://kafka.apache.org/intro) is an open-source distributed event streaming platform. It is used by many industries and organizations to process payments and perform other financial transactions in real-time, to collect and immediately react to customer interactions and orders, and to serve as the foundation for data platforms, microservices, and much more.  
Using Workato Apache Kafka connector you can link with your local or web Kafka cluster instance and:

- Consume messages using the [New message trigger](/en/connectors/kafka/new-message-trigger) or [New messages trigger (batch)](/en/connectors/kafka/new-messages-trigger-batch).
- Send messages using the [Publish message action](/en/connectors/kafka/publish-message) or [Publish messages action (batch)](/en/connectors/kafka/publish-messages-batch).

## How to connect to Apache Kafka in Workato

Complete the following steps to establish a connection to Apache Kafka in Workato using a cloud profile OPA:

> **LOCAL PROFILE SETUP**
> 
> The steps in this guide configure an Apache Kafka connection using a [Cloud Profile](/en/on-prem/agents/connection/cloud). Refer to the [Apache Kafka Profile](/en/on-prem/agents/connection/profile#apache-kafka-profile) guide to configure a connection using a `config.yml` file.

1. Enter a **Connection name** that identifies which Apache Kafka instance Workato is connected to.
   
   ![Configured Apache Kafka connection](/assets/connection.B1DylYTl.png)_Create your connection_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **On-prem group** drop-down menu to select an on-prem group that uses a [cloud profile](/en/on-prem/agents/connection/cloud).
   
4. Enter a server **URL** that uses the `kafka` or `kafka+ssl` protocol.
   
5. Specify a **Timeout** in milliseconds for general operations.
   
6. Enter the following values in `.pem` format to connect to Kafka using SSL/TLS:
   
   1. Enter an X509 **Server certificate** and **SSL client certificate**.
      
   2. Enter an RSA **SSL client key**.
      
   3. Optional. Enter an RSA **SSL client key password**. Don't inline password-protected private keys.
      
7. Optional. Expand the **Additional properties for Kafka connection** section and click **Add parameter** to define additional properties.
   
   Define additional properties
   
   You can define any Kafka [producer](https://kafka.apache.org/documentation/#producerconfigs) or [consumer](https://kafka.apache.org/documentation/#newconsumerconfigs) configuration properties. For example, `bootstrap.servers` or `batch_size`.
   
   Some properties are unavailable because the on-prem agent overrides them. Protected properties include the following:
   
   | Property name | Details |
   | --- | --- |
   | key.serializer | Only `StringSerializer` is supported by agent. |
   | value.serializer | Only `StringSerializer` is supported by agent. |
   | key.deserializer | Only `StringSerializer` is supported by agent. |
   | value.deserializer | Only `StringSerializer` is supported by agent. |
   | auto.offset.reset | Defined by recipes. |
   | enable.auto.commit | Defined internally. |
   
   The Kafka connector uses Apache Avro, a binary serialization format. Avro defines what fields are present and their type using JSON schemas. The connector stores data in a schema registry. The Kafka connector requires schema registry version 6.1.4 or later. For example:
   
   ![On-prem kafka avro connection](/assets/on-prem-kafka-avro-connection.BnxG4zoD.png)_Kafka connection configuration with schema registry URL_
   
8. Click **Connect**.
   

> **TROUBLESHOOT NO PROFILE FOUND ERRORS**
> 
> Refer to the [On-prem connections issues](/en/on-prem/agents/opa-troubleshooting/troubleshoot-opa-connections#kafka-no-profile-found-error) troubleshooting guide if you encounter a `No profile found` error.

---
