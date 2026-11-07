# Workato × Claude

Connect Claude to your Workato workspace through **Workato's official hosted MCP server**
(the Developer API MCP server at `https://app.trial.workato.com/mcp`), and give Claude an
always-current knowledge base built from the **official Workato documentation**
(docs.workato.com). Together they let Claude design and build recipes, MCP servers, Genies,
skills, and knowledge bases directly in your Workato platform.

```
┌──────────────┐  official Workato MCP (API token)  ┌──────────────────────────┐
│ Claude Code  │ ─────────────────────────────────▶ │ Workato workspace        │
│ / Desktop    │   ~300 tools: recipes, genies, MCP │ app.trial.workato.com    │
│              │   servers, KBs, skills, validators └──────────────────────────┘
│              │
│              │  reads before building               ┌──────────────────────────┐
│              │ ◀────────────────────────────────── │ kb/  (4,500+ docs pages) │
└──────────────┘   kb/search.py, kb/INDEX.md          │ synced daily from        │
                                                      │ docs.workato.com         │
                                                      └──────────────────────────┘
```

## What's in this repo

| Path | Purpose |
| --- | --- |
| `.mcp.json` | Registers Workato's official hosted **MCP server** (`/mcp`, API-token auth) |
| `kb/docs/en/**.md` | The full Workato documentation as Markdown, one file per page (~4,500 pages) |
| `kb/INDEX.md`, `kb/index/*.md` | Table of contents by docs section (Recipes, Connectors, MCP, Agent Studio, ...) |
| `kb/search.py` | Fast local full-text search (SQLite FTS5, no dependencies) |
| `kb/sync.py` | Incremental sync from docs.workato.com (`llms.txt`, `llms-full.txt`, sitemap) |
| `kb/CHANGELOG.md`, `kb/last_sync.json` | What changed in the docs on each sync |
| `.github/workflows/sync-workato-docs.yml` | Daily GitHub Action that keeps `kb/` current |
| `CLAUDE.md` | Working rules for Claude: research in KB → check API contract → plan → confirm → validate → build |
| `.claude/skills/` | Build playbooks: recipes, MCP servers, Genies/skills/knowledge bases |

## 1. Connect Claude to your workspace (official Workato MCP)

Workato hosts an MCP server that turns every Developer API endpoint your API client role allows
into an MCP tool (see `kb/docs/en/mcp/developer-api-mcp.md`). It works on Free and trial
workspaces and doesn't need AIRO.

| Workspace | MCP URL |
| --- | --- |
| Free / Developer Sandbox / trial (this workspace) | `https://app.trial.workato.com/mcp` |
| US | `https://app.workato.com/mcp` |
| EU | `https://app.eu.workato.com/mcp` |

1. In Workato, go to **Workspace admin → API clients**. Create a client role that has the endpoints
   you want as tools (recipes, folders, projects, connections, Agent Studio, MCP servers, data
   tables, and so on), then create an API client with that role and copy its token.
2. Export the token. `.mcp.json` reads it from the environment and never stores it in git:

```bash
export WORKATO_API_TOKEN="wrkatrial-..."
```

3. Open Claude Code in this repo, approve the `workato` server, and check `/mcp`. It should list
   about 300 tools. Then try *"List my Workato projects."*

To add it globally instead of per project:

```bash
claude mcp add --transport http workato https://app.trial.workato.com/mcp --header "Authorization: Bearer $WORKATO_API_TOKEN"
```

### Claude Desktop

```json
{
  "mcpServers": {
    "workato": {
      "command": "npx",
      "args": ["mcp-remote", "https://app.trial.workato.com/mcp", "--header", "Authorization: Bearer <YOUR_API_TOKEN>"]
    }
  }
}
```

> **AIRO MCP** (`/airo_mcp`) is a separate, higher-level Workato MCP server. It isn't available on
> this Free workspace. If your plan gains AIRO later, see `kb/docs/en/airo/mcp.md`.

## 2. Optional: Workato Labs toolkit (official, GitHub `workato-devs`)

Workato's open-source **Labs** org adds connector-specific recipe knowledge and a CLI:

- **recipe-skills**: a Claude Code plugin that teaches recipe JSON, datapills, and connector actions.
  Inside Claude Code run:

  ```text
  /plugin marketplace add workato-devs/recipe-skills
  /plugin install recipe-skills@workato-labs
  ```

- **wk CLI** (`brew install workato-devs/tap/wk`): pull, push, diff, and lint recipes as files.
  `wk auth login --token <token> --environment dev --region trial`.

## 3. Knowledge base

```bash
python3 kb/search.py "salesforce new record trigger"
python3 kb/search.py "hashed token" -s MCP -n 5
python3 kb/search.py --read en/recipes/building-recipes --heading "Error handling"
python3 kb/search.py --sections
```

Update it yourself at any time (about 20 seconds; only changed pages are rewritten):

```bash
python3 kb/sync.py
```

Add `--full` to re-download everything. The GitHub Action runs the sync daily and commits any
changes, and `kb/CHANGELOG.md` records what Workato changed.

How it works: `llms.txt` provides the page list and sections; `llms-full.txt` provides most
pages' Markdown in one request; the remaining pages are fetched as `<page>.md`. Sitemap `lastmod`
dates skip unchanged pages. Removed pages are deleted. The search index (`kb/index.sqlite`) is
rebuilt automatically when the manifest changes and is not committed.

## 4. Build with Claude

Example prompts once the Workato MCP server is connected:

- *"Build a recipe in project Test: when a new Salesforce lead is created, enrich it and post to Slack. Use the docs first."*
- *"Turn my 'Create ticket' recipe into a skill and expose it through a new MCP server."*
- *"Create an IT helpdesk Genie with a knowledge base from Confluence and a create-Jira-ticket skill."*

Claude follows `CLAUDE.md`: research the KB, propose a plan, wait for your confirmation, validate,
then build. It never starts, stops, or deletes assets without your approval.

## Requirements

- Python 3.9+ (standard library only) for `kb/`
- Node.js for `npx mcp-remote` (Claude Desktop only)
- Workato account (Free/trial works) and an API client token
