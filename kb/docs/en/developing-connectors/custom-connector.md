---
url: 'https://docs.workato.com/en/developing-connectors/custom-connector.md'
description: >-
  Build your own custom connector with the Workato Connector SDK to add triggers
  and actions for any application you want to integrate.
---

# Connector SDK

Build your own connector with the Connector SDK. Find out more about how you can [build your own custom connector](/en/developing-connectors/sdk).

![Workato](/assets/workato-developer-program.DTcpKHL7.png)

## What is a custom connector?

A connector allows Workato to interact with a single application through a series of [triggers](/en/recipes/triggers) and [actions](/en/recipes/actions). Triggers monitor for events that occur in the application you hope to connect to and kickstart a workflow of actions that we call [recipes](/en/workato-concepts#recipes). Actions carry out specific pre-defined operations in the target application.

Connectors built on the SDK are called **custom connectors**. These connectors have a private scope by default which means that they are only visible and available to the connector owner. After the connector is built and ready, you also have the ability to share it with others on various levels.

## What is Connector SDK

Workato was built with the philosophy that anyone can do enterprise-level integrations without any coding involved. As such, connectors on the platform should aim to balance functionality with ease of use. Whether you're developing a connector for your own team's use or you're a third-party developer looking to list your connector on Workato, reading this documentation is useful in getting you started on your journey.

## Before we begin...

Workato has a whole host of other features and functionalities that might help you achieve what you are hoping for such as our universal HTTP connector or custom actions if your integration needs aren't so complex. [Learn more](/en/developing-connectors).

If you've decided that a custom connector is necessary, do check in at our [community library](https://app.workato.com/browse/connectors) to see if anyone has contributed a custom connector to the application you're looking for. Our friendly support team via chat on our main website can also help you check our internal repository of custom connectors built by our customer success team.

Reading the SDK documentation is still useful as you'll be able to install these custom connectors and continue working on them if you wish to do so. By default, the examples are in JSON. It is highly recommended that you read about how other data formats can be handled if the API you plan to connect to uses a different data format.

---
