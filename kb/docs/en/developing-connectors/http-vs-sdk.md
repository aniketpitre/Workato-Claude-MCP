---
url: 'https://docs.workato.com/en/developing-connectors/http-vs-sdk.md'
description: >-
  Compare the Workato HTTP connector and Connector SDK by authentication methods
  and data types to choose the right approach for your connector.
---

# HTTP connector and the Connector SDK

Workato provides the following options to enable you to build your own connector:

- **HTTP connector**: Allows you to make API requests using a visual interface
- **Connector SDK**: Provides programmatic control over connector behavior and advanced customization options

The Connector SDK supports advanced customization and works for users with development experience. You can use the [Connector Copilot](/en/developing-connectors/sdk/copilot) to generate code, explore examples, and streamline development.

This document describes the differences between these options and helps you determine the approach for your connector development.

## Authentication methods

APIs use a range of authentication mechanisms, from basic authentication (username and password) to more complex methods like OAuth 2.0.

The HTTP connector and the Connector SDK support the following authentication methods:

| Authentication method | HTTP | SDK |
| --- | --- | --- |
| OAuth 1.0 | ❌ | ✔ |
| OAuth 2.0 | ✔ | ✔ |
| Basic auth | ✔ | ✔ |
| Plain API key/token | ✔ | ✔ |
| Digest auth | ❌ | ✔ |
| Multi-step auth | ❌ | ✔ |

## Data types

The HTTP connector and the Connector SDK support the following data types:

| Data type | HTTP | SDK |
| --- | --- | --- |
| JSON on REST | ✔ | ✔ |
| XML on REST | ✔ | ✔ |
| URL encoded Form | ✔ | ✔ |
| Multipart | ✔ | ✔ |
| Binary | ✔ | ✔ |

## Capabilities

The HTTP connector and the Connector SDK offer the following capabilities:

| Capability | HTTP | SDK |
| --- | --- | --- |
| Trigger closure | ❌ | ✔ |
| Updated record trigger | Sometimes | ✔ |
| Webhook + poll trigger | ❌ | ✔ |
| Data transformation | ❌ | ✔ |
| Data pre/post processing | ❌ | ✔ |
| Pagination | ❌ | ✔ |
| While loop | ✔ | ✔ |
| For loop | ✔ | ✔ |

## Additional functionality

The HTTP connector and the Connector SDK have the following additional functionality:

| Functionality | HTTP | SDK |
| --- | --- | --- |
| Sharing | ✔ | ✔ |
| Clone and run recipes | ✔ | ❌ |
| Reusable (cross recipe) | ❌ | ✔ |
| Manual webhook | ✔ | ✔ |
| Auto webhook | Can cause issues | ✔ |

---
