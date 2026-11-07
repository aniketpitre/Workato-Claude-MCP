---
url: 'https://docs.workato.com/en/developing-connectors/http/http-faqs.md'
description: >-
  Answers to common questions about developing HTTP connectors in Workato,
  including HTTP Connector V2 triggers, actions, and capabilities.
---

# HTTP FAQs

Get answers to frequently asked questions about developing HTTP connectors.

What is the HTTP Connector V2 in Workato?

The [HTTP Connector V2](/en/developing-connectors/http-v2#http-connector-v2) is an enhanced version of Workato's tool that allows integration with any cloud application that has an HTTP-based API. This connector allows you to create new connectors and add triggers or actions to existing Workato connectors.

How is the HTTP Connector V2 different from the deprecated HTTP Connector V1?

The [HTTP Connector V2](/en/developing-connectors/http-v2#http-connector-v2) launched in July 2018. It offers improved functionalities and user interface compared to the deprecated HTTP V1. HTTP V2 includes updated features for building integrations more efficiently and effectively.

What types of triggers and actions does the HTTP Connector V2 support?

The HTTP Connector V2 supports two triggers:

- [New event trigger through a webhook](/en/connectors/workato-webhooks)
- [New event trigger through polling](/en/developing-connectors/http/building-http-trigger#new-event-via-polling)

The HTTP Connector V2 one action:

- [Send Request](/en/developing-connectors/http/building-http-action#building-a-http-action)
  - This action allows you to configure an HTTP request to an endpoint and use the response data.

How can I use the HTTP Connector V2 for real-time triggers?

You can use the [New event trigger through a webhook](/en/connectors/workato-webhooks) provided by the HTTP Connector V2 as a real-time trigger. Workato provides a unique target URL for webhooks, which are processed immediately as trigger events.

What is the process for setting up a connection using the HTTP Connector V2?

Basic steps to [set up a connection](/en/developing-connectors/http/connection-setup#http-connection-setup) include:

- Select the HTTP Connector V2 from the connector menu.
- Enter the required fields, such as the endpoint URL.
- Configure the authentication information.

How long does it typically take to build an action with the HTTP Connector V2?

It usually takes less than 20 minutes to build a [custom action](/en/developing-connectors/custom-actions#custom-actions) using the HTTP Connector V2. The length of time depends on the complexity of the integration and familiarity with the Workato platform.

Can I use the HTTP Connector V2 to interact with any cloud application with an API?

Yes. The [HTTP Connector V2](/en/developing-connectors/http-v2) is designed to integrate with any cloud application that exposes an HTTP-based API, making it versatile for various integration use cases.

What are some common use cases for the HTTP Connector V2?

Users frequently [use the HTTP Connector V2](/en/developing-connectors/http-v2#http-use-cases) to:

- Create invoices in accounting systems
- Retrieve metrics from analytics applications
- Trigger workflows from online form submissions

What should I do if I'm still using the HTTP Connector V1?

We recommend that you transition to HTTP Connector V2 for better functionality and support if you are still using the [HTTP Connector V1](/en/developing-connectors/http#http-connector-v1).

Why am I getting a 307 Temporary Redirect error when enabling automatically follow redirects?

If you encounter a `307 Temporary Redirect` error, note that automatic redirects are not enabled by default for HTTP methods such as `POST` and `PUT`. However, they are enabled for `GET` and `HEAD` requests. This behavior aligns with the [RFC protocol guidelines on automatic redirects](https://www.rfc-editor.org/rfc/rfc9110.html#name-redirection-3xx). The guidelines advise caution with automatic redirects for unsafe methods.

To handle these redirects, you can manually implement logic in your recipes. Use [error monitoring](/en/recipes/steps#handle-errors-step) to create your own `307` redirect handling. Then, use the `Location` header returned with the original call to manage the redirect effectively.

What should I do if I encounter a certificate verify failed error?

If you encounter a `certificate verify failed` error, it may be due to an incomplete certificate chain or untrusted self-signed certificates. Complete the following steps to resolve this issue:

1. Ensure you have the complete certificate chain. This includes the server certificate, intermediate certificates, and root certificate, with each separated by an empty line.
   
2. Input the entire chain into the **TLS server custom CA certificate** field in your HTTP connection settings.
   

Refer to the [HTTP SSL certificate verify failed troubleshooting guide](/en/troubleshooting/http-ssl-certificate-verify-failed-error) for more detailed instructions.

---
