# Workato × Claude

Connect Claude to your Workato workspace through **Workato's official MCP server (AIRO MCP)**, and
give Claude an always-current knowledge base built from the **official Workato documentation**
(docs.workato.com). Together they let Claude design and build recipes, MCP servers, Genies,
skills, and knowledge bases directly in your Workato platform.

```
┌──────────────┐  official AIRO MCP (OAuth / token)  ┌──────────────────────────┐
│ Claude Code  │ ──────────────────────────────────▶ │ Workato workspace        │
│ / Desktop    │   recipes, genies, MCP servers,     │ app.trial.workato.com    │
│              │   KBs, skills, data tables, jobs    └──────────────────────────┘
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
| `.mcp.json` | Registers Workato's official **AIRO MCP server** for this project (Developer Sandbox URL) |
| `kb/docs/en/**.md` | The full Workato documentation as Markdown, one file per page (~4,500 pages) |
| `kb/INDEX.md`, `kb/index/*.md` | Table of contents by docs section (Recipes, Connectors, MCP, Agent Studio, ...) |
| `kb/search.py` | Fast local full-text search (SQLite FTS5, no dependencies) |
| `kb/sync.py` | Incremental sync from docs.workato.com (`llms.txt`, `llms-full.txt`, sitemap) |
| `kb/CHANGELOG.md`, `kb/last_sync.json` | What changed in the docs on each sync |
| `.github/workflows/sync-workato-docs.yml` | Daily GitHub Action that keeps `kb/` current |
| `CLAUDE.md` | Working rules for Claude: research in KB → AIRO `docs_get` → plan → confirm → build |
| `.claude/skills/` | Build playbooks: recipes, MCP servers, Genies/skills/knowledge bases |

## 1. Connect Claude to your workspace (official AIRO MCP)

Workato ships its MCP server **inside the platform**. It's not a GitHub project (see
`kb/docs/en/airo/mcp.md`). Data center URLs:

| Workspace | URL |
| --- | --- |
| Developer Sandbox / trial (this workspace) | `https://app.trial.workato.com/airo_mcp` |
| US | `https://app.workato.com/airo_mcp` |
| EU | `https://app.eu.workato.com/airo_mcp` |

### Option A: OAuth (recommended, interactive)

`.mcp.json` already registers the server. Clone the repo, then:

```bash
claude
```

Inside Claude Code run `/mcp`, select `workato-airo-mcp-server`, choose **Authenticate**, then click
**Authorize** in the browser. Sign in to the right workspace and environment first.

If you prefer to add it globally rather than per project:

```bash
claude mcp add --transport http workato-airo-mcp-server https://app.trial.workato.com/airo_mcp
```

### Option B: API token (headless)

1. In Workato, go to **Workspace admin → API clients → Client roles**, edit or create a role, and
   enable the **AIRO MCP Server** permission.
2. Create an API client with that role and copy its token.
3. Add the server with a bearer header:

```bash
claude mcp add --transport http workato-airo-mcp-server https://app.trial.workato.com/airo_mcp --header "Authorization: Bearer $WORKATO_API_TOKEN"
```

Token connections act as the workspace owner. Keep the token out of git.

### Claude Desktop

Edit `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "workato-airo-mcp-server": {
      "command": "npx",
      "args": ["mcp-remote", "https://app.trial.workato.com/airo_mcp", "--transport", "http-first"]
    }
  }
}
```

Verify with the prompt: *"List my Workato projects."*

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

Example prompts once AIRO MCP is connected:

- *"Build a recipe in project Test: when a new Salesforce lead is created, enrich it and post to Slack. Use the docs first."*
- *"Turn my 'Create ticket' recipe into a skill and expose it through a new MCP server."*
- *"Create an IT helpdesk Genie with a knowledge base from Confluence and a create-Jira-ticket skill."*

Claude follows `CLAUDE.md`: research the KB, check AIRO's `docs_get`, propose a plan, wait for your
confirmation, then build. It never starts, stops, or deletes assets without your approval.

## Requirements

- Python 3.9+ (standard library only) for `kb/`
- Node.js for `npx mcp-remote` (Claude Desktop only)
- Workato account with AIRO access
