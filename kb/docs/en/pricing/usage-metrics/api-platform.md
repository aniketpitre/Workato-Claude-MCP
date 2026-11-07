---
url: 'https://docs.workato.com/en/pricing/usage-metrics/api-platform.md'
description: >-
  Learn how Workato measures Managed API usage in API Calls, including
  calculation rules and examples.
---

# Managed API usage

Workato measures Managed API usage in API Calls. Each API request fulfilled by a Managed API is measured as an API Call, so a quick response counts as one API Call, and longer-running responses count as more.

The number or type of steps inside a Managed API recipe don't contribute to usage. A Managed API recipe with few steps and one with many consume the same number of API Calls when their response times are equal. This differs from workflow recipes, where each action step contributes to usage.

> Some plans measure Managed API usage in [Tasks](/en/recipes/tasks) rather than API Calls. Refer to your contract or contact your Customer Success Representative for more information.

## How API Calls are measured

The following diagram demonstrates how requests to a Managed API are measured.

```mermaid
%%{init: {'themeVariables': {'fontSize': '18px'}, 'flowchart': {'padding': 4, 'nodePadding': 4}}}%%
flowchart LR
    AR(["&nbsp;&nbsp;&nbsp;API Request&nbsp;&nbsp;&nbsp;<br/>&nbsp;&nbsp;&nbsp;(N API Calls)&nbsp;&nbsp;&nbsp;"]) <--> GT["<br/><br/>API<br/>Gateway<br/><br/><br/>"]
    GT <--> B["<br/><br/>&nbsp;&nbsp;Managed&nbsp;&nbsp;<br/>&nbsp;&nbsp;API&nbsp;&nbsp;<br/>&nbsp;&nbsp;recipe&nbsp;&nbsp;<br/><br/>"]
    classDef default fill:#fff,stroke:#67eadd,stroke-width:2px,color:#000;
    classDef Gateway fill:#e1fffc,stroke:#67eadd,stroke-width:2px,color:#24434f;
    classDef Recipe stroke:#5159f6,stroke-width:2px,fill:#fff;
    classDef Focus fill:#e2e0f5,stroke:#5159f6,stroke-width:2px,color:#000;
    class GT Gateway
    class B Recipe
    class AR Focus
```

Total usage: N API Calls per successful request

## Managed API calculation rules

Managed API usage calculations follow the general [usage calculation rules](/en/pricing/usage-metrics#rules), where successful calls count toward usage and failed calls are excluded.

Workato uses the following additional rules to calculate Managed API usage:

- The recipe must execute completely without internal errors.
- The job must finish as designed, even if it returns expected errors such as `4xx` or `5xx` status codes defined in the recipe logic.
- Cached API responses count toward API Call usage the same way as non-cached responses.
- Synchronous recipe function calls are part of the API Call and don't add extra usage. Asynchronous recipe function calls run as independent workflows measured in Tasks.
- A Managed API recipe with IDP steps or Event streams publishes contributes Pages or Events on top of API Calls.

## Managed API usage examples

The following examples demonstrate how Workato calculates usage for API Calls in different scenarios.

### Managed API: API recipe

**Overview**

```mermaid
%%{init: {'themeVariables': {'fontSize': '18px'}, 'flowchart': {'padding': 4, 'nodePadding': 4}}}%%
flowchart LR
    AR(["&nbsp;&nbsp;&nbsp;API Request&nbsp;&nbsp;&nbsp;<br/>&nbsp;&nbsp;&nbsp;(N API Calls)&nbsp;&nbsp;&nbsp;"]) <--> GT["<br/><br/>API<br/>Gateway<br/><br/><br/>"]
    GT <--> B["<br/><br/>&nbsp;&nbsp;Managed&nbsp;&nbsp;<br/>&nbsp;&nbsp;API&nbsp;&nbsp;<br/>&nbsp;&nbsp;recipe&nbsp;&nbsp;<br/><br/>"]
    classDef default fill:#fff,stroke:#67eadd,stroke-width:2px,color:#000;
    classDef Gateway fill:#e1fffc,stroke:#67eadd,stroke-width:2px,color:#24434f;
    classDef Recipe stroke:#5159f6,stroke-width:2px,fill:#fff;
    classDef Focus fill:#e2e0f5,stroke:#5159f6,stroke-width:2px,color:#000;
    class GT Gateway
    class B Recipe
    class AR Focus
```

**Managed API recipe**

![Managed API recipe](/assets/api-call.Cw7j9leL.png)_Managed API recipe_

**Explanation**

Managed APIs contribute to usage as API Calls. Each request to a Managed API counts as N API Calls, where N depends on the response time and your metering interval.

Managed APIs don't contribute to Tasks, even if the recipe contains steps that would otherwise be eligible.

#### Usage totals

- **Total usage per request**: N API Calls

### Recipe function called synchronously from an API recipe

**Overview**

```mermaid
%%{init: {'themeVariables': {'fontSize': '18px'}, 'flowchart': {'padding': 4, 'nodePadding': 4}}}%%
flowchart LR
    AR(["&nbsp;&nbsp;&nbsp;API Request&nbsp;&nbsp;&nbsp;<br/>&nbsp;&nbsp;&nbsp;(N API Calls)&nbsp;&nbsp;&nbsp;"]) <--> GT["<br/><br/>API<br/>Gateway<br/><br/><br/>"]
    GT <--> P["<br/><br/>&nbsp;&nbsp;Parent&nbsp;&nbsp;<br/>&nbsp;&nbsp;API&nbsp;&nbsp;<br/>&nbsp;&nbsp;recipe&nbsp;&nbsp;<br/><br/>"]
    P <--> C["<br/>&nbsp;&nbsp;Synchronous&nbsp;&nbsp;<br/>&nbsp;&nbsp;Recipe&nbsp;&nbsp;<br/>&nbsp;&nbsp;Function&nbsp;&nbsp;<br/><br/>"]
    classDef default fill:#fff,stroke:#67eadd,stroke-width:2px,color:#000;
    classDef Gateway fill:#e1fffc,stroke:#67eadd,stroke-width:2px,color:#24434f;
    classDef Recipe stroke:#5159f6,stroke-width:2px,fill:#fff;
    classDef Focus fill:#e2e0f5,stroke:#5159f6,stroke-width:2px,color:#000;
    class GT Gateway
    class P,C Recipe
    class AR Focus
```

**API recipe**

![API recipe](/assets/api-call-parent-synchronous.BJfe5bw9.png)_API recipe calls a recipe function synchronously_

**Recipe function**

![Recipe function](/assets/api-call-child-synchronous.DtQJjZeX.png)_Recipe function called synchronously_

**Explanation**

An API recipe in this example calls a recipe function synchronously. The recipe function must execute as part of the end-to-end execution of the API request because it's synchronous. It's considered a continuation of the same API request and doesn't contribute any additional usage separately.

#### Usage totals

- **Total usage per request**: N API Calls

### Recipe function called asynchronously from an API recipe

**Overview**

```mermaid
%%{init: {'themeVariables': {'fontSize': '18px'}, 'flowchart': {'padding': 4, 'nodePadding': 4}}}%%
flowchart LR
    AR(["&nbsp;&nbsp;&nbsp;API Request&nbsp;&nbsp;&nbsp;<br/>&nbsp;&nbsp;&nbsp;(N API Calls)&nbsp;&nbsp;&nbsp;"]) <--> GT["<br/><br/><br/>API<br/>Gateway<br/><br/><br/><br/>"]
    GT <--> P["<br/><br/><br/>&nbsp;&nbsp;Parent&nbsp;&nbsp;<br/>&nbsp;&nbsp;API&nbsp;&nbsp;<br/>&nbsp;&nbsp;recipe&nbsp;&nbsp;<br/><br/><br/>"]
    P -.->|async| C
    subgraph C["Asynchronous Recipe<br/>Function"]
        direction TB
        CTop[ ]
        CS["Action steps<br/>(8 Tasks)"]
        CTop ~~~ CS
    end
    classDef default fill:#fff,stroke:#67eadd,stroke-width:2px,color:#000;
    classDef Ghost fill:none,stroke:none,color:transparent;
    classDef Gateway fill:#e1fffc,stroke:#67eadd,stroke-width:2px,color:#24434f;
    classDef Recipe stroke:#5159f6,stroke-width:2px,fill:#fff;
    classDef Focus fill:#e2e0f5,stroke:#5159f6,stroke-width:2px,color:#000;
    class GT Gateway
    class P,C Recipe
    class AR Focus
    class CS Focus
    class CTop Ghost
```

**API recipe**

![API recipe](/assets/api-call-parent-asynchronous.mWZUWuYp.png)_API recipe calls a recipe function asynchronously_

**Recipe function**

![Recipe function](/assets/api-call-child-asynchronous.0p-2HVg-.png)_Recipe function called asynchronously_

**Explanation**

An API recipe in this example calls a recipe function asynchronously. The recipe function executes independently of the original API request because it's asynchronous. It's considered an independent workflow and measured in Tasks.

The total usage is N API Calls plus the Tasks the asynchronous recipe function incurs (8 in this example).

#### Usage totals

- **API recipe**: N API Calls
- **Recipe function**: 8 Tasks
- **Total usage per request**: N API Calls + 8 Tasks

---
