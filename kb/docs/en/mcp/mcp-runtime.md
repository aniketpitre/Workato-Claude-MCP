---
url: 'https://docs.workato.com/en/mcp/mcp-runtime.md'
description: >-
  The MCP Runtime is the Workato-hosted layer that operates your MCP servers,
  handles client traffic, and runs each tool with the user's own identity.
---

# MCP Runtime

The MCP Runtime is the layer that hosts and operates your MCP servers. Workato runs the MCP servers, handles client traffic, and executes each tool invocation. Your team doesn't provision or maintain any infrastructure.

## MCP Runtime key features

- **Hosted by Workato**: Every MCP server runs on Workato's managed runtime.
- **User identity and context**: Verified user access works through [runtime user connections](/en/features/runtime-user-connections) and allows each end user to authenticate with their own credentials when accessing a tool that requires authentication. This ensures that workflows perform actions using the identity and permissions of the individual user. Refer to [MCP verified user access](/en/mcp/verified-user-access) for more information.

```mermaid
graph LR
X("User signs in with <br/> their own credentials") --> Y(("Workato authenticates <br/> the user"))
B("MCP servers")
C("Tools")

Y --Accessed with the <br/> user's credentials--> B
Y --Tools run with the identity <br/> and permissions assigned <br/> to the user--> C

classDef default fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
classDef WorkatoBlue fill:#5159f6,stroke:#5159f6,stroke-width:2px,color:#fff;
class Y WorkatoBlue
```

---
