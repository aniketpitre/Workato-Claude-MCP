---
url: 'https://docs.workato.com/en/pricing/usage-metrics/api-proxy.md'
description: >-
  Learn how Workato measures API Proxy usage in API Proxy Calls, including
  calculation rules and examples.
---

# API Proxy usage

Workato measures API Proxy usage in API Proxy Calls. Each successful request to an API Proxy counts as one API Proxy Call, whether or not transformation is applied. Response time does not affect the count.

API Proxy requests consume fewer credits per call than Managed API requests, because proxying a request is a lighter operation than running a full Managed API.

## How API Proxy Calls are measured

The following diagram demonstrates how requests to an API Proxy are measured.

```mermaid
%%{init: {'themeVariables': {'fontSize': '18px'}, 'flowchart': {'padding': 4, 'nodePadding': 4}}}%%
flowchart LR
    AR(["&nbsp;&nbsp;&nbsp;API Request&nbsp;&nbsp;&nbsp;<br/>&nbsp;&nbsp;&nbsp;(1 API Proxy Call)&nbsp;&nbsp;&nbsp;"]) <--> GT["<br/><br/>API<br/>Gateway<br/><br/><br/>"]
    GT <--> B["<br/><br/>&nbsp;&nbsp;API&nbsp;&nbsp;<br/>&nbsp;&nbsp;Proxy&nbsp;&nbsp;<br/>&nbsp;&nbsp;recipe&nbsp;&nbsp;<br/><br/>"]
    classDef default fill:#fff,stroke:#67eadd,stroke-width:2px,color:#000;
    classDef Gateway fill:#e1fffc,stroke:#67eadd,stroke-width:2px,color:#24434f;
    classDef Recipe stroke:#5159f6,stroke-width:2px,fill:#fff;
    classDef Focus fill:#e2e0f5,stroke:#5159f6,stroke-width:2px,color:#000;
    class GT Gateway
    class B Recipe
    class AR Focus
```

Total usage: 1 API Proxy Call per request

## API Proxy calculation rules

API Proxy usage calculations follow the general [usage calculation rules](/en/pricing/usage-metrics#rules), where successful calls count toward usage and failed calls are excluded.

Workato uses the following additional rules to calculate API Proxy usage:

- The job must finish as designed, even if it returns expected errors such as `4xx` or `5xx` status codes defined in the recipe logic.
- Cached API responses from GET requests count toward API Proxy Call usage the same way as non-cached responses.

## API Proxy usage examples

The following examples demonstrate how Workato calculates API Proxy usage.

### API Proxy recipe

**Overview**

```mermaid
%%{init: {'themeVariables': {'fontSize': '18px'}, 'flowchart': {'padding': 4, 'nodePadding': 4}}}%%
flowchart LR
    AR(["&nbsp;&nbsp;&nbsp;API Request&nbsp;&nbsp;&nbsp;<br/>&nbsp;&nbsp;&nbsp;(1 API Proxy Call)&nbsp;&nbsp;&nbsp;"]) <--> GT["<br/><br/>API<br/>Gateway<br/><br/><br/>"]
    GT <--> B["<br/><br/>&nbsp;&nbsp;API&nbsp;&nbsp;<br/>&nbsp;&nbsp;Proxy&nbsp;&nbsp;<br/>&nbsp;&nbsp;recipe&nbsp;&nbsp;<br/><br/>"]
    classDef default fill:#fff,stroke:#67eadd,stroke-width:2px,color:#000;
    classDef Gateway fill:#e1fffc,stroke:#67eadd,stroke-width:2px,color:#24434f;
    classDef Recipe stroke:#5159f6,stroke-width:2px,fill:#fff;
    classDef Focus fill:#e2e0f5,stroke:#5159f6,stroke-width:2px,color:#000;
    class GT Gateway
    class B Recipe
    class AR Focus
```

**API Proxy recipe**

![API Proxy recipe](/assets/api-call-proxy.BrZEfCGT.png)_API Proxy recipe_

**Explanation**

API Proxies contribute to usage as API Proxy Calls. Each request to an API Proxy counts as 1 API Proxy Call. Response time does not affect the count.

#### Usage totals

- **Total usage per request**: 1 API Proxy Call

### API Proxy recipe with transformation

**Overview**

```mermaid
%%{init: {'themeVariables': {'fontSize': '18px'}, 'flowchart': {'padding': 4, 'nodePadding': 4}}}%%
flowchart LR
    AR(["&nbsp;&nbsp;&nbsp;API Request&nbsp;&nbsp;&nbsp;<br/>&nbsp;&nbsp;&nbsp;(1 API Proxy Call)&nbsp;&nbsp;&nbsp;"]) <--> GT["<br/><br/>API<br/>Gateway<br/><br/><br/>"]
    GT <--> B["<br/>&nbsp;&nbsp;API Proxy recipe&nbsp;&nbsp;<br/>&nbsp;&nbsp;with&nbsp;&nbsp;<br/>&nbsp;&nbsp;transformation&nbsp;&nbsp;<br/><br/>"]
    classDef default fill:#fff,stroke:#67eadd,stroke-width:2px,color:#000;
    classDef Gateway fill:#e1fffc,stroke:#67eadd,stroke-width:2px,color:#24434f;
    classDef Recipe stroke:#5159f6,stroke-width:2px,fill:#fff;
    classDef Focus fill:#e2e0f5,stroke:#5159f6,stroke-width:2px,color:#000;
    class GT Gateway
    class B Recipe
    class AR Focus
```

**API Proxy recipe with transformation**

![API Proxy recipe with transformation](/assets/api-call-proxy-transformation.Z3jjFEUk.png)_API Proxy recipe with transformation_

**Explanation**

API Proxies with transformation contribute to usage as API Proxy Calls. Each request counts as 1 API Proxy Call. Response time does not affect the count.

#### Usage totals

- **Total usage per request**: 1 API Proxy Call

---
