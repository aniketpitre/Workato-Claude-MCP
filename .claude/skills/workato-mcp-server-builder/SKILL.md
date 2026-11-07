---
name: workato-mcp-server-builder
description: Create and manage Workato-hosted MCP servers (from project recipes/skills, API collections, Genies or prebuilt MCP servers), design their tools, auth and access policies, using the official AIRO MCP server and the local Workato docs knowledge base. Use when the user wants to expose Workato capabilities to AI agents via MCP.
---

# Build a Workato MCP server

## 1. Research
```bash
python3 kb/search.py "MCP server" -s MCP
cat kb/index/mcp.md kb/index/prebuilt-mcp-servers.md
```
Must-read pages:
- `kb/docs/en/mcp/mcp-servers.md`: server types and how to create one
- `kb/docs/en/mcp/mcp-server-design.md` and `mcp-server-tool-design.md`: tool naming, descriptions, granularity
- `kb/docs/en/agentic/skills/mcp-server-skills.md`: recipes as skills or tools
- `kb/docs/en/mcp/mcp-authentication.md`, `verified-user-access.md`: tokens, OAuth, end-user identity
- `kb/docs/en/mcp/prebuilt-mcps.md`: check whether a prebuilt server already covers the need
- API reference: `kb/docs/en/workato-api/mcp-servers.md`

## 2. Decide the shape
- **Prebuilt** MCP server: fastest, if one fits.
- **Project asset server** with tools from skills or recipe functions: custom business actions.
- **API collection server**: expose existing API platform endpoints.
- **Genie tools**: let MCP clients talk to a Genie.

Design each tool as one clear business action with a precise description and typed, minimal
inputs and outputs (see the tool design guide).

## 3. Build (AIRO MCP)
1. Call `docs_get` for the skill and MCP tool guides.
2. Create or convert the underlying recipes into skills, using the workato-recipe-builder skill where needed.
3. Confirm the plan with the user, then create the MCP server in the project folder and assign the tools.
4. Configure auth (hashed token by default, or verified user access) and user-group access.
5. Give the user the MCP URL and how to connect it, for example
   `claude mcp add --transport http <name> <mcp_url>`. Treat tokens as secrets and never commit them.
