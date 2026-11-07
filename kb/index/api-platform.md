# API platform

68 pages. Paths are relative to the repository root.


## API platform

- **API Platform** - `kb/docs/en/api-management.md` - The Workato API Platform lets you build, secure, publish, and monitor APIs with an API gateway, proxies, recipes, collections, and governance.
- **AI gateway** - `kb/docs/en/api-mgmt/ai-gateway.md` - Learn how AI gateway collections expose secured Workato endpoints so LLMs, GPTs, and AI agents can take actions on your behalf.
- **API collections** - `kb/docs/en/api-mgmt/api-collections.md` - Group API endpoints with a common access pattern into Workato API collections, covering proxy, recipe, and AI gateway collection types.
- **API developer portal** - `kb/docs/en/api-mgmt/api-developer-portal.md` - Use the Workato API developer portal to share API documentation, manage client access, control authentication, and let clients test endpoints.
- **API edge gateway** - `kb/docs/en/api-mgmt/api-edge-gateway.md` - API Edge Gateway routes API traffic from on-premise environments to the Workato API platform with centralized management, observability, and policy control.
- **API Endpoint Management** - `kb/docs/en/api-mgmt/api-endpoints.md` - Manage and expose recipe-based and proxy-based API endpoints with the Workato API platform, and organize them into API collections for consistent access.
- **API Gateway** - `kb/docs/en/api-mgmt/api-gateway.md` - The Workato API gateway gives you a single entry point to secure, route, and optimize APIs with authentication, traffic management, and data mediation.
- **API Governance** - `kb/docs/en/api-mgmt/api-governance.md` - Govern your APIs in Workato with access policies, RecipeOps monitoring triggers, and recipe version management for rate limits and quota control.
- **API Library** - `kb/docs/en/api-mgmt/api-library.md` - The API library is a centralized catalog where users in your workspace discover, document, and test shared API collections with auto-generated OpenAPI specs.
- **API monitoring and analytics** - `kb/docs/en/api-mgmt/api-monitoring-analytics.md` - Track API usage and performance in Workato with dashboard metrics and logs covering response times, error messages, and traffic patterns across endpoints.
- **Security Best Practices for APIs** - `kb/docs/en/api-mgmt/api-security.md` - Learn security best practices for Workato APIs, including protecting API tokens, refreshing tokens, and using IP allowlists.
- **Calling APIs** - `kb/docs/en/api-mgmt/calling-apis.md` - Learn how to call API platform endpoints from other recipes or external tools using Auth token, OAuth 2.0, or JWT authorization headers.
- **API platform quotas** - `kb/docs/en/api-mgmt/limits.md` - Reference for Workato API platform quotas, including the default thresholds and notes that apply to API platform usage.
- **API security** - `kb/docs/en/api-mgmt/securing-apis.md` - Learn how Workato API management secures your APIs with clients, applications, authentication methods, and mutual TLS enforcement.

## API collections

- **API collection management FAQs** - `kb/docs/en/api-mgmt/api-collections-management-faqs.md` - Answers to common questions about API collection management in Workato, including collection types, access, and how to manage endpoints.
- **Configure collection settings** - `kb/docs/en/api-mgmt/api-collections/configure-settings.md` - Configure Workato API collection settings, including version, description, URL, sharing, and Postman sync for recipe, proxy, and AI gateway collections.
- **Download OpenAPI spec** - `kb/docs/en/api-mgmt/api-collections/download-openapi.md` - Download an OpenAPI 3.0 or 2.0 spec for a Workato API collection to document all endpoints and use them with tools like Postman.
- **Edit an API collection** - `kb/docs/en/api-mgmt/api-collections/edit-collection.md` - Access and edit a Workato API collection after you create it, using the overview page to manage endpoints and collection settings.
- **API proxy collections** - `kb/docs/en/api-mgmt/api-collections/gateway-collection.md` - Create an AI gateway collection in Workato to expose endpoints to LLMs, GPTs, and AI applications for secure, authorized actions.
- **API proxy collections** - `kb/docs/en/api-mgmt/api-collections/proxy-collection.md` - Create an API proxy collection in Workato to forward requests to your existing API backend with monitoring, access control, and authentication.
- **API recipe collections** - `kb/docs/en/api-mgmt/api-collections/recipe-collection.md` - Create an API recipe collection in Workato to expose business logic through secure, customizable endpoints powered by individual API recipes.
- **SOAP API recipe collection** - `kb/docs/en/api-mgmt/api-collections/soap-api-recipe-collection.md` - Create a SOAP API recipe collection in Workato to expose SOAP 1.1 or 1.2 endpoints generated from a WSDL definition for legacy systems.
- **Sync to Postman** - `kb/docs/en/api-mgmt/api-collections/sync-postman.md` - Sync a deployed Workato API collection to your Postman workspace to increase visibility and drive adoption through internal and external portals.
- **Unauthenticated API collections** - `kb/docs/en/api-mgmt/unauthenticated-collections.md` - Allow an API proxy collection to accept unauthenticated requests so public endpoints, such as OIDC discovery documents, can be served without client credentials.

## API developer portal

- **Access the developer portal** - `kb/docs/en/api-mgmt/access-developer-portal.md` - Log in to the API developer portal with a magic link or Workato Identity to discover, test, and consume published APIs.
- **Configure the developer portal** - `kb/docs/en/api-mgmt/configure-developer-portal.md` - Set up the Workato developer portal to brand your client portal, manage client access, and publish API collections.
- **Custom domain** - `kb/docs/en/api-mgmt/custom-domain-portal.md` - Configure a custom domain to serve the Workato API developer portal under your own branded URL with automatic TLS certificates.
- **JIT user settings** - `kb/docs/en/api-mgmt/developer-portal-jit.md` - Configure JIT user settings to set the authentication method and policy for API clients created when users log in to the developer portal via SSO.

## API endpoints

- **API endpoint caching** - `kb/docs/en/api-mgmt/api-caching.md` - Learn how API endpoint caching stores GET responses to cut duplicate requests, speed up recipe actions, and reduce jobs.
- **API Endpoints FAQs** - `kb/docs/en/api-mgmt/api-endpoints-management-faqs.md` - Find answers to common questions about managing API endpoints in Workato, including error codes, testing, securing, and monitoring endpoint usage.
- **API proxy endpoints** - `kb/docs/en/api-mgmt/api-proxy-endpoints.md` - Create API proxy endpoints in the Workato API platform to securely forward requests to external APIs with managed security, transformation, and access.
- **Apply API proxy transformations** - `kb/docs/en/api-mgmt/api-proxy-transformation.md` - Configure API proxy transformations to modify requests and responses as they pass through the Workato gateway, aligning client and target schemas and formats.
- **API recipe endpoints** - `kb/docs/en/api-mgmt/api-recipes.md` - API recipes are a Workato recipe type you can call as API endpoints to share data and logic with other recipes or external users.
- **API Recipes - Respond to API request Action** - `kb/docs/en/api-mgmt/api-recipes/action-response-to-api-request.md` - Reference for the Respond to API request action in Workato API recipes, which ends the job and sends the HTTP response defined by the New API request trigger.
- **SOAP API recipe walkthrough** - `kb/docs/en/api-mgmt/api-recipes/soap-walkthrough.md` - Build a Workato SOAP API recipe that parses and processes SOAP requests through a target API hosted on-premises using an HTTP connection.
- **API Recipes - New API request trigger** - `kb/docs/en/api-mgmt/api-recipes/trigger-new-api-request.md` - Reference for the New API request trigger in API recipes, covering request and response content type, headers, and schema inputs.
- **Create an API recipe** - `kb/docs/en/api-mgmt/api-recipes/walkthrough.md` - Create a Workato API recipe so external partners and internal users can access and consume data through an API endpoint.
- **Configure a new API proxy endpoint** - `kb/docs/en/api-mgmt/configure-proxy-endpoint.md` - Configure a new API proxy endpoint to forward requests to an external API, including creating, viewing, and setting up the schema.
- **Configure a new API recipe endpoint** - `kb/docs/en/api-mgmt/configure-recipe-endpoint.md` - Configure a new API recipe endpoint in an API recipe collection so clients can call your recipe through the Workato API platform.
- **Testing API Endpoints** - `kb/docs/en/api-mgmt/testing-endpoints.md` - Learn how to test recipe-based and proxy-based API endpoints in the Workato API platform before exposing them to clients.

## API governance

- **API Access Policies** - `kb/docs/en/api-mgmt/api-access-policies.md` - Learn how API access policies use rate limit and request quota rules to control how clients call your Workato APIs.
- **RecipeOps by Workato** - `kb/docs/en/connectors/recipeops.md` - Use RecipeOps by Workato to monitor and manage active recipes, automating responses to stopped recipes and failed jobs.
- **RecipeOps - API policy quota violation trigger** - `kb/docs/en/connectors/recipeops/triggers/api-policy-violation.md` - The API policy quota violation trigger in the RecipeOps connector fires when an access profile exceeds a policy quota threshold of 80, 90, or 100 percent.
- **RecipeOps - API request timeout trigger** - `kb/docs/en/connectors/recipeops/triggers/api-request-timeout.md` - The API request timeout trigger in the RecipeOps connector fires when an API request to any workspace endpoint exceeds its configured timeout limit.
- **RecipeOps - API concurrency threshold exceeded** - `kb/docs/en/connectors/recipeops/triggers/concurrency-exceeded.md` - The API concurrency threshold exceeded trigger in the RecipeOps connector fires when workspace API requests exceed 80% of the concurrency quota.
- **RecipeOps - API policy rate limit violation trigger** - `kb/docs/en/connectors/recipeops/triggers/rate-limit-violation.md` - The API policy rate limit violation trigger in the RecipeOps connector fires when an access profile exceeds its assigned API rate limits.
- **Recipe Version Management** - `kb/docs/en/recipes/version-management.md` - Learn how Workato tracks recipe versions, logs recipe and schema changes, and lets you compare versions with Recipe Diff.

## API monitoring & analytics

- **API Platform - Logs** - `kb/docs/en/api-mgmt/api-logs.md` - Use API logs to view incoming API requests across your workspace, filter by status, client, or collection, and export records as CSV to troubleshoot issues.
- **API Platform - Dashboard** - `kb/docs/en/api-mgmt/dashboard.md` - Use the Workato API platform dashboard to monitor endpoints and collections, track requests, errors, and policy violations in real time.

## API security

- **Access Tokens** - `kb/docs/en/api-mgmt/access-tokens.md` - Learn how Workato access tokens authenticate API recipe clients, and compare Auth Token, OAuth 2.0, JWT, and OpenID Connect formats.
- **Manage API clients and applications** - `kb/docs/en/api-mgmt/api-client-mgmt.md` - Manage API clients and applications in Workato to group users, authenticate requests, control collection access, and set security parameters.
- **Auth Token** - `kb/docs/en/api-mgmt/auth-token.md` - Learn how to retrieve and refresh an Auth token, the simplest way to authenticate an API request with the Workato API platform.
- **Create an API client with DCR** - `kb/docs/en/api-mgmt/create-client-dcr.md` - Create an API client that uses a dynamic client registration provider so consumers can generate their own credentials in the developer portal.
- **Custom validation** - `kb/docs/en/api-mgmt/custom-validation.md` - Configure custom validation for Workato API management.
- **API platform - JSON Web Token** - `kb/docs/en/api-mgmt/jwt-token.md` - Set up JSON Web Token (JWT) authentication for API platform clients using RSA or HMAC signing to authenticate calls with signed tokens.
- **API platform - Extract JWT payload claims** - `kb/docs/en/api-mgmt/jwt-token/extract-jwt-payload-claims.md` - Learn how to extract JWT payload claims such as email, employee ID, and scopes in a Workato recipe using the JWT claims datapill.
- **JWT Token** - `kb/docs/en/api-mgmt/jwt-workato-claim.md` - Learn how the Workato API platform inspects JWT claims to match the API key and authorize incoming requests from identity providers.
- **Mutual TLS** - `kb/docs/en/api-mgmt/mtls.md` - Configure mutual TLS (mTLS) for an API platform client to require valid client certificates verified against your workspace truststore.
- **OAuth 2.0 token introspection** - `kb/docs/en/api-mgmt/oauth2-token-introspection.md` - Set up OAuth 2.0 token introspection on an API client to validate access tokens issued by an external identity provider for each request.
- **API platform - OAuth2.0** - `kb/docs/en/api-mgmt/oauth2.md` - Set up OAuth 2.0 client credentials authentication for API platform clients to call Workato endpoints using access tokens instead of static tokens.
- **OpenID Connect** - `kb/docs/en/api-mgmt/oidc.md` - Configure OpenID Connect authentication so the API platform verifies JWTs issued by your identity provider for cross-domain access.

## Settings

- **API concurrency** - `kb/docs/en/api-mgmt/api-concurrency.md` - Configure API concurrency in Workato to set how your workspace queues or rejects requests when the simultaneous request quota is reached.
- **Dynamic client registration** - `kb/docs/en/api-mgmt/api-dynamic-client.md` - Set up dynamic client registration so Workato can register API clients with your IdP like Okta and issue OAuth 2.0 credentials automatically.
- **API Prefix** - `kb/docs/en/api-mgmt/api-prefix.md` - Learn how API prefixes set unique base paths per Workato account so you can separate development, testing, and production endpoints and reuse collection paths.
- **Custom authorization** - `kb/docs/en/api-mgmt/custom-authorization.md` - Configure custom authorization to enforce additional claims on API endpoints, enabling role-based access control and custom business logic.
- **Custom Domain** - `kb/docs/en/api-mgmt/custom-domain.md` - Configure a custom domain to route Workato API platform endpoints through your own subdomain instead of the default apim.workato.com URL.
- **API traffic mirroring** - `kb/docs/en/api-mgmt/traffic-mirroring.md` - Configure API traffic mirroring to send Workato API request and response payloads to a SIEM provider for anomaly detection and PII monitoring.
- **Truststore** - `kb/docs/en/api-mgmt/truststore.md` - Manage certificate bundles in the Workato Truststore to define trusted CA chains that validate client certificates during mTLS authentication.
