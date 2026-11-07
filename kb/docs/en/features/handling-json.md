---
url: 'https://docs.workato.com/en/features/handling-json.md'
description: >-
  Learn how to handle raw JSON in Workato recipes using JSON tools by Workato or
  custom connectors to extract datapills from name/value pairs.
---

# Handling JSON

JSON (JavaScript Object Notation) is a lightweight format for structured data exchange. APIs, webhooks, and external systems commonly use JSON to send data in name/value pairs and arrays.

Workato typically exposes data as input fields and output datapills automatically in recipes. However, some workflows require direct access to raw JSON, especially when handling webhook payloads, HTTP responses, or unstructured file content.

## JSON tools by Workato

Use [JSON tools by Workato](/en/connectors/json-by-workato) to extract datapills from raw JSON when the structure isn't automatically exposed. This connector provides the [Parse JSON document action](/en/connectors/json-by-workato/parse-json-action), which accepts a sample structure and parses actual JSON content at runtime.

## Build custom connectors for advanced JSON handling

Use a connector with schema control and authentication support if your use case involves repeated JSON structures or full API integration.

| Custom connector | Description |
| --- | --- |
| HTTP connector | Use HTTP actions and triggers to receive and send raw JSON. Refer to the [HTTP documentation](/en/developing-connectors/http-v2) for more information. |
| Connector SDK | Use the Connector SDK to build reusable connectors with full control over input and output fields, authentication, and triggers. This framework allows developers to maintain and distribute connectors for teams integrating with external systems. Refer to the [Connector SDK](/en/developing-connectors/sdk) documentation for more information. |

Refer to the [HTTP vs SDK](/en/developing-connectors/http-vs-sdk) documentation for a detailed comparison.

---
