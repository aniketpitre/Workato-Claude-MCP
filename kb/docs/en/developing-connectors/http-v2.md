---
url: 'https://docs.workato.com/en/developing-connectors/http-v2.md'
description: >-
  Use the Workato HTTP connector to integrate with any HTTP-based API, set up
  triggers and actions, and make custom requests to any endpoint.
---

# HTTP connector V2

The HTTP connector enables you to integrate with applications or services that provide HTTP-based APIs (Application Programming Interfaces). This allows you to interact programmatically with the service to perform various actions, such as retrieving data or creating and updating records.

This documentation covers the V2 HTTP connector, which launched in July 2018. Refer to the [V1 HTTP connector documentation](/en/developing-connectors/http) if you're using the deprecated V1 HTTP connector.

## How to use the HTTP connector

The HTTP connector provides universal API access for integrating with applications that don't have a prebuilt connectors in Workato. You can use the HTTP connector to make custom HTTP requests to any API endpoint, providing greater flexibility compared to prebuilt connectors that are designed for specific services. The HTTP connector enables you set up [triggers](/en/developing-connectors/http/building-http-trigger) and [actions](/en/developing-connectors/http/building-http-action), and map data from the HTTP response to variables for use in subsequent steps of your recipe. You can also define custom headers, query parameters, error handling, and request bodies, which is not possible with prebuilt connectors.

You must manually configure the HTTP method, URL, headers, and body for each request. You can also manually configure custom handling for data parsing and mapping.

## HTTP use cases

The HTTP connector is recommended for the following use cases:

- Custom integrations with APIs that do not have a prebuilt connector in Workato.
  - For example, you can create an invoice in your accounting system by making a `POST` request with a JSON request body.
- Prototyping and testing API interactions before building a more robust integration.
- Custom request and response handling.

> **WEBHOOKS CONNECTOR**
> 
> You can use the [New event via webhook trigger](/en/connectors/workato-webhooks/wizard) if your use case requires your recipe to respond to trigger events in real-time. Verify that your app allows you to create webhooks before pursuing this option.

## More resources

- [HTTP connection setup](/en/developing-connectors/http/connection-setup)
- [Build an HTTP trigger](/en/developing-connectors/http/building-http-trigger)
- [Build an HTTP action](/en/developing-connectors/http/building-http-action)

---
