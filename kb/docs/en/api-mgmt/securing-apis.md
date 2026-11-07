---
url: 'https://docs.workato.com/en/api-mgmt/securing-apis.md'
description: >-
  Learn how Workato API management secures your APIs with clients, applications,
  authentication methods, and mutual TLS enforcement.
---

# API security

APIs are critical interfaces to your business systems, managing data flow and enabling essential functionalities. Securing APIs is crucial to prevent unauthorized access and potential data breaches that compromise sensitive information.

Workato's API management capabilities provide robust tools to secure your API ecosystem:

## API clients and applications

Workato enables you to [create API clients](/en/api-mgmt/api-client-mgmt#create-new-client), which are logical groupings of users, such as members from the same organization. These clients gain access to API collections through [applications](/en/api-mgmt/api-client-mgmt#api-keys). Applications enable you to control who can interact with your APIs and which API collections clients can access. You can assign an authentication method and policy restrictions at the client level, and create applications with granular controls like allowed IP addresses.

> **LEGACY ACCESS PROFILES**
> 
> Access profiles are the legacy method for API access management, replaced by applications. Refer to [Access profiles](/en/api-mgmt/api-client-mgmt#access-profile) for the deprecation timeline.

You can also configure an API proxy collection on a custom domain to accept unauthenticated requests, which removes the access profile requirement for that collection. Refer to [Unauthenticated API collections](/en/api-mgmt/unauthenticated-collections) for more information.

## Authentication methods

Workato supports several [authentication methods](/en/api-mgmt/access-tokens) to safeguard your API interactions:

- [Auth tokens](/en/api-mgmt/auth-token) for straightforward, token-based authentication.
- [OAuth 2.0](/en/api-mgmt/oauth2) for a robust authorization framework that allows granular permissions.
- [JSON Web Tokens (JWT)](/en/api-mgmt/jwt-token) for stateless, secure information exchange.
- [OpenID Connect](/en/api-mgmt/oidc) for identity verification based on the OAuth 2.0 protocol.
- [OAuth 2.0 (Token Introspection)](/en/api-mgmt/oauth2-token-introspection) to validate external tokens issued by Identity Providers.

You can configure each authentication method at the client level, applying it to all applications created for that client. This ensures that API clients are authenticated and authorized according to your security policies.

Using Workato's API management tools, you can ensure your APIs are secure and compliant with industry standards.

### Enforce mutual TLS (mTLS)

Workato adds an extra layer of protection with mutual TLS (mTLS). mTLS requires clients to present a valid certificate during the SSL handshake when enabled.

Workato validates both the access token and the client certificate. This ensures that only authenticated clients with trusted certificates can access your APIs.

Use mTLS to enforce certificate-based trust with your configured authentication method. Refer to the [Mutual TLS authentication](/en/api-mgmt/mtls) guide for more information.

---
