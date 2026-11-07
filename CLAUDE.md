# Workato + Claude workspace

This repo connects Claude Code to a Workato workspace and gives Claude a local, always-current
copy of the official Workato documentation to build from.

- **Workspace access**: Workato's official hosted **Developer API MCP server** (`workato` in
  `.mcp.json`, `https://app.trial.workato.com/mcp`, API-token auth). It exposes about 300 tools, one
  per Developer API endpoint (`get_recipes`, `post_recipes`, `post_agentic_genies`,
  `post_mcp_mcp_servers`, `post_recipe_validators_validate`, ...). Each tool takes fixed `verb` and
  `path` arguments; copy them from the tool schema. The token's API client role decides which
  tools exist. Do not build a replacement server. (AIRO MCP isn't available on this Free plan.)
- **Knowledge**: `kb/` holds the Workato docs as Markdown (from docs.workato.com `llms.txt`).

## Working rules

1. **Look it up before you build.** For any Workato task, read the relevant docs in `kb/`
   first. Don't rely on memory: Workato changes often, and the KB is synced daily.
   - Search: `python3 kb/search.py "<query>"` (add `-s "<section>"` to narrow, `-n 15` for more)
   - Browse: `kb/INDEX.md` → `kb/index/<section>.md` → the page under `kb/docs/en/...`
   - Read one section of a page: `python3 kb/search.py --read en/recipes/triggers --heading "Polling"`
   - Connector docs live under `kb/docs/en/connectors/<app>/` (triggers/, actions/).
2. **Then check the API contract.** Each MCP tool maps to a Developer API endpoint documented in
   `kb/docs/en/workato-api/*.md` (index: `kb/docs/en/workato-api/resources.md`). Read the
   payload section before any `post_`/`put_` call.
3. **Plan, confirm, build.** Before you create or change anything in the workspace, summarise
   the plan (assets, folder or project, connections, trigger, and steps) and ask the user to
   confirm. Never start, stop, or delete recipes or Genies in the workspace without explicit
   approval.
4. **Build in a project folder**, never in Home assets (the API rejects it). Follow
   `kb/docs/en/recipes/naming-conventions.md`.
   Validate recipe JSON with the `post_recipe_validators_validate` tools before you call
   `post_recipes` or `put_recipes_`.
5. **Cite the docs you used** (KB path) when you explain a design decision.
6. **Keep the KB fresh.** If `kb/last_sync.json` is more than a few days old, run
   `python3 kb/sync.py`. It's incremental and takes about 20 seconds.

## Skills

- `.claude/skills/workato-recipe-builder`: design and build recipes
- `.claude/skills/workato-mcp-server-builder`: expose recipes, APIs, or Genies as MCP servers
- `.claude/skills/workato-genie-builder`: Agent Studio Genies, skills, and knowledge bases

## Key entry points in the KB

| Topic | Start here |
| --- | --- |
| Recipe design | `kb/docs/en/recipes/building-recipes.md`, `kb/index/recipe-design.md` |
| Triggers / actions / data pills | `kb/docs/en/recipes/triggers.md`, `actions.md`, `data-pills-and-mapping.md` |
| Formulas | `kb/docs/en/formulas/`, `kb/index/workato-expression-language.md` |
| Error handling | `kb/docs/en/recipes/best-practices-error-handling.md` |
| Recipe functions | `kb/docs/en/features/callable-recipes.md` |
| MCP servers | `kb/docs/en/mcp/mcp-servers.md`, `mcp-server-design.md`, `mcp-server-tool-design.md` |
| Genies / Agent Studio | `kb/docs/en/agentic/agent-studio/create-a-genie.md`, `genie-design-patterns.md` |
| Skills / knowledge bases | `kb/docs/en/agentic/skills.md`, `kb/docs/en/agentic/agent-studio/knowledge-bases/` |
| Workato MCP (this connection) | `kb/docs/en/mcp/developer-api-mcp.md` |
| Developer API (reference) | `kb/docs/en/workato-api/resources.md` |
| Connector SDK | `kb/docs/en/developing-connectors/sdk.md` |

Don't edit anything under `kb/docs/`, `kb/index/`, `kb/INDEX.md`, or `kb/manifest.json` by hand:
`kb/sync.py` generates them.
