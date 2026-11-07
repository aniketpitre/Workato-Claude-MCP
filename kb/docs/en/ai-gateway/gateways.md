---
url: 'https://docs.workato.com/en/ai-gateway/gateways.md'
description: >-
  Gateways are Workato's egress control point for enterprise AI traffic. Model
  Gateway, MCP Gateway, Agent Gateway, and API Gateway each govern a different
  kind of call through one policy, telemetry, and identity plane.
---

# Gateways

Gateways are the enforcement point for enterprise AI traffic in the Workato AI control plane ecosystem. Each call passes through a gateway that authenticates the caller, applies the policies an admin owns, and captures the call for audit and observability.

Four gateways run through the Workato AI control plane and each governs a different kind of traffic:

| Gateway | What it governs |
| --- | --- |
| Model Gateway | LLM calls from applications, agents, and Workato platform services |
| MCP Gateway | MCP client traffic to Workato-composed, prebuilt, and third-party MCP servers |
| Agent Gateway | Agent-to-agent (A2A) collaboration and orchestration through open protocols |
| API Gateway | Managed REST endpoints your workspace exposes to applications and partners |

The gateways share one policy, telemetry, and identity plane. You can apply rate limits, token limits, IP access restrictions, allowlists, and audit trails consistently across every gateway rather than reimplementing them for each product.

## Model Gateway

Model Gateway is the exit path for LLM calls from Workato recipes, genies, copilots, and external applications. Applications connect through an OpenAI-compatible or Anthropic-compatible API instead of holding provider credentials directly. The gateway resolves each call to a provider and model and enforces the policies you've attached.

Model Gateway solves three problems that come from hardcoded model choices scattered across services:

- **No enforcement**: A team can call any model, including models that aren't reviewed, aren't compliant, or aren't cost-appropriate.
- **Change means a redeploy**: Swapping a deprecated model or moving traffic to a newer model requires editing and shipping every service that calls an LLM.
- **The decision is invisible**: Because the model is chosen in client code, there isn't a single place to see or govern what's actually being called on whose behalf.

Model Gateway addresses these by turning model selection into governed configuration. You define **routes** that resolve to a provider and model, either directly or through rules that match on tags, keys, parameters, or request complexity. Applications reference a route by its route ID, so you can re-point traffic through configuration alone, without editing client code.

Refer to [Model Gateway](/en/ai-gateway) for more information.

## MCP Gateway

MCP Gateway governs MCP interactions across your organization, including MCP servers you compose in Workato, Workato prebuilt MCP servers, and third-party servers integrated by proxy. Every client connection passes through it, and every tool invocation is authenticated, authorized, and rate-limited before it reaches the runtime.

MCP Gateway provides the following:

- **Authentication and authorization**: End users authenticate through API tokens, Workato Identity credentials, or SSO. Authorization scopes what the authenticated caller can do at both the server level and in the tool's backend.
- **Traffic limits**: Rate and concurrency limits protect MCP servers and the systems behind them.
- **Audit and observability**: Every request and tool invocation is captured for governance.
- **Governance policies**: Policies apply uniformly across the entire MCP estate rather than being configured per server.

Refer to [MCP Gateway](/en/mcp/mcp-gateway) for more information.

## Agent Gateway

Agent Gateway covers agent-to-agent collaboration and orchestration through open protocols. Agents delegate work, call each other, and share context using the following supported protocols:

- **[Agent-to-Agent (A2A)](/en/connectors/a2a)** for direct agent-to-agent invocation.
- **[MCP Gateway](/en/mcp/mcp-gateway)** for agent-to-tool orchestration and shared context.

Governance for agent-to-agent traffic is inherited from the surrounding gateways. A2A calls that terminate at a tool traverse MCP Gateway. LLM calls made in the course of an agent conversation traverse Model Gateway. The Workato AI control plane registry, policies, and audit trails apply to both flows without a separate configuration surface.

## API Gateway

API Gateway is the managed API surface for your workspace. It publishes recipes and services as authenticated REST endpoints, enforces rate limits and quotas per collection or access key, and monitors usage across every consumer.

Use API Gateway to:

- Expose recipes and services as versioned, authenticated APIs. Supported authentication methods include OAuth 2.0, JWT, and OpenID Connect.
- Enforce rate limits, quotas, concurrency controls, and access policies on API collections.
- Mediate protocols and data formats between clients and backends.
- Monitor request volume, latency, and errors across every API consumer.

Refer to [API Gateway](/en/api-mgmt/api-gateway) for more information.

## Where the gateways fit in the AI control plane

Gateways are one component of the [AI control plane](/en/control-plane), alongside the registry, cost controls, and governance. They handle traffic in flight while the surrounding Workato AI control plane manages the assets that traffic touches, the identities that authenticate to it, and the policies that govern it.

---
