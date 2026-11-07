---
url: 'https://docs.workato.com/en/ai-gateway/configure.md'
description: >-
  Set up Model Gateway by adding providers, creating routes, issuing access
  keys, and defining policies that control rate limits, token limits, and IP
  access.
---

# Configure Model Gateway

Set up [Model Gateway](/en/ai-gateway) to connect your LLM providers, create routes that determine which model serves each request, and issue access keys that control who can use them.

Model Gateway configuration builds on three objects. Create them in the following order:

1. **[Provider](/en/ai-gateway/providers)**: A connection to an LLM service, such as Anthropic or Azure OpenAI, along with the credentials Model Gateway uses to authenticate.
2. **[Route](/en/ai-gateway/routes)**: The target that serves a request. A route resolves to a provider and model, either directly or through rules.
3. **[Access key](/en/ai-gateway/access-keys)**: The credential an application presents to Model Gateway. Each access key grants access to one or more routes.

[Policies](/en/ai-gateway/policies) are optional. Create a policy when you need to cap the request rate or token usage of the routes and access keys assigned to it, or restrict access by IP address.

## Add a provider

Add a provider for each LLM service you plan to route requests to. Model Gateway supports Anthropic, OpenAI, OpenAI Compatible, Azure OpenAI, AWS Bedrock, AWS Bedrock Mantle, Fireworks, and Gemini. Refer to [Add a provider](/en/ai-gateway/providers#add-a-provider).

## Create a route

Create a route that resolves to a provider and model. Choose a direct route to send every request to one model, or a rule-based or intelligent route to select a model per request. Refer to [Create a route](/en/ai-gateway/routes#create-a-route).

## Create an access key

Create an access key for each team or application, and select the routes it can use. Refer to [Create an access key](/en/ai-gateway/access-keys#create-an-access-key).

## Test a route

Send a request with your access key and route ID to confirm the route works. Refer to [Test a route](/en/ai-gateway/test-route).

## Connect Anthropic-compatible clients

Configure Claude Desktop, Claude Code, or the Anthropic SDKs to send requests through Model Gateway. Refer to [Connect clients](/en/ai-gateway/connect-clients#connect-anthropic-compatible-clients).

## Create a policy

Optional. Create a policy to apply rate limits, token limits, and IP access restrictions, then assign it to access keys or routes. Refer to [Create a policy](/en/ai-gateway/policies#create-a-policy).

## Validation messages

Model Gateway returns the following validation messages:

| Field | Message | Condition |
| --- | --- | --- |
| **Connection name**, **Name** | `Name cannot exceed 100 characters.` | The name is longer than 100 characters. |
| **API URL** | `Please enter a valid URL.` | The value isn't a valid URL. |
| **Attempt timeout (in seconds)** | `Value must be between 1 and 360 seconds.` | The value is outside the supported range. |

---
