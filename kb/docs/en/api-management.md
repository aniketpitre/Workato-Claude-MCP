---
url: 'https://docs.workato.com/en/api-management.md'
description: >-
  The Workato API Platform lets you build, secure, publish, and monitor APIs
  with an API gateway, proxies, recipes, collections, and governance.
---

# API Platform

Workato's [API Platform](https://www.workato.com/platform/api-management?utm_source=docs&utm_medium=referral&utm_campaign=api-management) features enterprise-grade capabilities, encompassing key API management functionalities including our API gateway, governance, design, security and monitoring features.

The API Platform enables you to create API proxies, which securely forward traffic to your internal APIs.

The API Platform also enables you to create [API recipes](/en/api-mgmt/api-recipes/), which expose recipe functionality as API endpoints. This allows you to share data with partners or use the functionality in other recipes.

You can create [API collections](/en/api-mgmt/api-collections) from groups of endpoints, whether the endpoints are recipe-based or proxy-based.

API publishers can control access to endpoints, monitor requests, and set quotas on usage.

> **FEATURE AVAILABILITY**
> 
> The API Platform is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.

## Key capabilities

The API platform has the following key capabilities.

### API gateway

The API gateway offers robust capabilities for managing your APIs, integrating advanced security, efficient routing, and effective mediation to ensure optimal performance and reliability. [Learn more](/en/api-mgmt/api-gateway).

### API governance

Effective governance ensures that your APIs are secure, compliant, and managed according to best practices. This includes activity auditing, versioning, and lifecycle management. Implement granular access control and policies to manage usage and access. API access policies allow you to enforce rate limiting and quota management. These policies prevent overuse by a single client and ensure efficient and secure use of your APIs. [Learn more](/en/api-mgmt/api-governance).

### API design

Workato accelerates API development with intuitive features that simplify the creation, deployment, and management of APIs. With recipe and proxy endpoints, you can build your own APIs on Workato using a low-code/no-code approach, or securely expose your existing APIs. Define the endpoints, methods, and data structures for your APIs with Workato's native tools for API design and documentation. [Learn more](/en/api-mgmt/api-design).

### API monitoring

Track and analyze API usage and performance with comprehensive monitoring and analytics tools. The API platform dashboard enables you to visualize real-time data for your endpoints and API collections. This includes metrics such as response times, error messages, and traffic patterns, enabling proactive management and optimization of APIs. [Learn more](/en/api-mgmt/dashboard).

### API security

Securely expose your APIs with Workato’s enterprise-grade security measures. Workato's API gateway supports various authentication methods to ensure secure access to APIs. Use OAuth 2.0, JWT tokens and OpenID Connect to provide flexibility and security in how APIs are accessed and used. [Learn more](/en/api-mgmt/access-tokens).

## Key concepts and features

This section provides key concepts and features for the API Platform.

Get the quick version in this video!

[Video](https://www.youtube.com/embed/t-szYp53mnQ?rel=0&si=tDzpy4CNzWsNaZMK)

### API collections

An API collection is a set of endpoints that can be managed together. These endpoints can be API recipe-based or API proxy-based. [Learn more](/en/api-mgmt/api-collections).

### Access policies

An access policy can be used to set restrictions on the usage of an API. A single policy can be associated with one or more clients (or, for legacy clients, one or more access profiles). [Learn more](/en/api-mgmt/api-access-policies).

### Access profiles (legacy)

Access profiles are the legacy method for API access management, replaced by [API keys](#api-keys). A single client could have one or more access profiles. An access profile specified one or more API collections to which the client had access, and was optionally associated with an access policy. [Learn more](/en/api-mgmt/api-client-mgmt#access-profile).

### API keys

A client can generate one or more API keys to authenticate requests, access assigned API collections, and enforce access policies. [Learn more](/en/api-mgmt/api-client-mgmt#api-keys).

### API proxy

An API proxy is a gateway that separates a client-facing API from internal APIs. You can securely expose internal APIs as endpoints while making use of management features provided by the API Platform. [Learn more](/en/api-mgmt/api-collections).

### API recipes

An API recipe is a type of [recipe](/en/recipes/building-recipes) that can be used to create API endpoints. Using the [API Platform](/en/api-management) feature, you can expose these endpoints to external users or use them in other recipes. [Learn more](/en/api-mgmt/api-recipes/).

### API tokens

An API token grants access to the API collections assigned to a client's API key (or, for legacy clients, an access profile). Refer to the [API tokens](/en/api-mgmt/access-tokens) documentation for more information.

### Clients

A client is a user to whom access to one or more API collections can be granted. [Learn more](/en/api-mgmt/api-client-mgmt).

### Concurrency

Concurrency refers to the number of requests that can be processed simultaneously at a given time.

### Concurrency limit

The concurrency quota is the maximum number of requests your workspace can process simultaneously.

### Dashboard

A customizable tool to visualize real-time data on API collections and endpoints. [Learn more](/en/api-mgmt/dashboard).

### Endpoints

An endpoint is a single callable REST interface. It has an associated public URL.

For API recipe-based endpoints, calls to the URL initiate a recipe that has a [New API Request trigger](/en/api-mgmt/api-recipes/trigger-new-api-request). [Learn more](/en/api-mgmt/api-endpoints).

For API proxy-based endpoints, calls to the endpoint URL are forwarded to a target URL in an HTTP connection.

### Library

The library is a catalog of APIs that are discoverable by other users in your organization. [Learn more](/en/api-mgmt/api-library).

### Peak concurrent API requests

This represents the summary of peak API requests processed simultaneously across a workspace.

### Queue

The system automatically places requests in a queue when the concurrency quota is reached. It processes these queued requests when other concurrent requests complete.

### Queue size

The queue size represents the maximum number of requests that can be held in a queue when the concurrency quota is reached. When the queue reaches its full capacity, the system rejects any new incoming requests.

### Recipe-level concurrency

Recipe-level concurrency is a feature that allows you to set specific concurrency quotas for individual API recipes. This enables you to prioritize selected endpoints or moderate high-traffic endpoints.

---
