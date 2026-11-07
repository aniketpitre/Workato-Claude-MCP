---
url: 'https://docs.workato.com/en/connectors/openai.md'
description: >-
  The OpenAI connector enables you to automate AI workflows, generating text and
  images, classifying text, and running models through the OpenAI API in
  Workato.
---

# OpenAI

[OpenAI](https://openai.com/) is an artificial intelligence research organization behind the popular ChatGPT, which interacts in a conversational way. OpenAI has multiple models you can leverage for editing text, generating images, and text classification. You can create your own models and expose them internally using OpenAI.

> **FEATURE AVAILABILITY**
> 
> The OpenAI connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API Version

The OpenAI connector uses the [OpenAI API](https://platform.openai.com/docs/introduction).

### API call rate limits

Rate limits for API calls are determined by your OpenAI plan. Refer to the [OpenAI rate limits](https://platform.openai.com/docs/guides/rate-limits) documentation for more information.

## How to connect to OpenAI on Workato

The OpenAI connector uses an API key for authentication. Obtain the API key in OpenAI by navigating to the [OpenAI API keys page](https://platform.openai.com/account/api-keys). We recommend that you store the API key safely, as it is only displayed once.

![Configured OpenAI connection](/assets/new-openai-connection.B4vw2uS2.png)

## Supported OpenAI actions

- [Business actions](/en/connectors/openai/business-actions)
- [Send messages to OpenAI models](/en/connectors/openai/chatgpt-conversation)
- [Moderate text](/en/connectors/openai/moderate-text)
- [Generate text embedding](/en/connectors/openai/generate-text-embedding)
- [Generate images](/en/connectors/openai/generate-images)
- [Transcribe recording](/en/connectors/openai/translate-recording)
- [Translate recording](/en/connectors/openai/translate-recording)

---
