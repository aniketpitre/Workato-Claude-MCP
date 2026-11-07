---
url: 'https://docs.workato.com/en/developing-connectors/sdk.md'
description: >-
  Build custom Workato connectors with the Connector SDK to integrate
  applications not covered by prebuilt connectors using triggers and actions.
---

# Connector SDK

![Workato](/assets/workato-developer-program.DTcpKHL7.png) Our SDK documentation provides detailed instructions for creating customized connectors that seamlessly integrate with applications not directly supported by Workato's pre-built connectors. Building a high-quality connector on the Workato platform requires managing technical aspects of connector development as well as focusing on the user experience of your connector.

Workato was built with the philosophy that anyone can do enterprise-level integrations without any coding involved. Connectors on the platform aim to balance functionality with ease of use. Whether you're developing a connector for your own team's use or you're a third-party developer looking to list your connector on Workato, this documentation can help you on your journey.

> **FEATURE AVAILABILITY**
> 
> Connector SDK is available by default. Refer to your pricing plan and contract to learn more.

## What is a custom connector?

[Video](https://www.youtube.com/embed/bfmavANqHNI)

A connector enables Workato to engage with a single application through a sequence of [triggers](/en/recipes/triggers) and [actions](/en/recipes/actions). Triggers actively monitor events within the target application and initiate a series of actions known as [recipes](/en/workato-concepts#recipes). Actions carry out specific pre-defined operations in the target application.

Connectors built on the SDK are called **custom connectors**. These connectors have a private scope by default. This means they are only visible and available to the connector owner. You can choose to share your custom connector with open source code or closed source code. Both methods support automatic update notifications for users and child connectors when a new version is released.

> **EMBEDDED AND AUTOMATION HQ COMPATIBILITY**
> 
> Custom connectors support child connector workflows and automatic update notifications for [Embedded](/en/oem) users and [Automation HQ](/en/automation-hq) users.

## Before you begin

Workato provides features and functionalities to help you, including our universal HTTP connector and custom actions if your integration needs aren't so complex. Learn more about [universal connectors](/en/developing-connectors) and [custom actions](/en/developing-connectors/custom-actions).

If you've decided that a custom connector is necessary, you can search the [community library](https://www.workato.com/browse/connectors) to see if anyone has contributed a custom connector to the application you're looking for. Our support team on our [main website](https://www.workato.com) can also help you check our internal repository of custom connectors over chat.

The SDK documentation remains useful, enabling you to install and further develop custom connectors as needed. Note that the examples provided in the documentation primarily use JSON. We highly recommend familiarizing yourself with how other data formats can be handled if the API you intend to connect with uses a different data format.

---
