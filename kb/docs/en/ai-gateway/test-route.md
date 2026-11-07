---
url: 'https://docs.workato.com/en/ai-gateway/test-route.md'
description: >-
  Send a test request to Model Gateway through the OpenAI-compatible or
  Anthropic-compatible API to confirm a route works.
---

# Test a route

Send a request to Model Gateway's endpoint to confirm a route works.

> **PREREQUISITES**
> 
> The access key you use must have the route you're testing in its **Route(s)** list. Refer to [Create an access key](/en/ai-gateway/access-keys#create-an-access-key).

Authenticate with an access key and pass the route ID as the `model` value. Model Gateway accepts OpenAI-compatible and Anthropic-compatible requests for any route regardless of the provider you use.

**OpenAI-compatible**

Replace `<model-gateway-url>` in the following example with the URL shown in the **Access key generated** dialog when you created the access key. Model Gateway resolves the request to the route's provider and model, applies any assigned policy, and returns an OpenAI-compatible chat completion response, regardless of which provider served the request.

```shell
curl <model-gateway-url> \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <access-key>" \
  -d '{
    "model": "<route-id>",
    "messages": [
      {
        "role": "user",
        "content": "Hello"
      }
    ]
  }'
```

**Anthropic-compatible**

Replace `<model-gateway-host>` in the following example with the host from the URL shown in the **Access key generated** dialog, for example `https://ai.workato.com`. Model Gateway resolves the request to the route's provider and model and applies any assigned policy.

```shell
curl <model-gateway-host>/anthropic/v1/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <access-key>" \
  -d '{
    "model": "<route-id>",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "Hello"
      }
    ]
  }'
```

Refer to [Connect clients](/en/ai-gateway/connect-clients) to configure Claude Desktop, Claude Code, or the Anthropic SDKs to send requests through Model Gateway.

---
