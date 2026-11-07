---
name: workato-genie-builder
description: Design and build Workato Agent Studio Genies (AI agents) with skills, knowledge bases, guardrails, chat triggers and MCP tools via Workato's official hosted MCP server (`workato`), grounded in the local Workato docs. Use when the user asks for a Genie, AI agent, skill or knowledge base in Workato.
---

# Build a Workato Genie

## 1. Research
```bash
python3 kb/search.py "genie" -s "Agent Studio"
cat kb/index/agent-studio.md
```
Must-read pages:
- `kb/docs/en/agentic/agent-studio/plan-genie-scope.md`: keep each Genie focused
- `kb/docs/en/agentic/agent-studio/create-a-genie.md`, `genies-configuration.md`
- `kb/docs/en/agentic/agent-studio/genie-design-patterns.md`
- Skills: `kb/docs/en/agentic/skills.md`, `kb/docs/en/agentic/skills/skill-design-best-practices.md`
- Knowledge: `kb/docs/en/agentic/agent-studio/knowledge-bases-vs-skills.md`, `knowledge-bases/`
- Guardrails and security: `kb/docs/en/agentic/agent-studio/guardrails/`, `security.md`
- Testing: `kb/docs/en/agentic/agent-studio/test-genie.md`
- Prebuilt Genies to adapt: `kb/index/workato-genies.md`
- API reference: `kb/docs/en/workato-api/agent-studio.md`

## 2. Design (confirm with the user)
- **Job description**: the Genie's purpose, personality, boundaries, and escalation rules
- **Skills**: one recipe-backed action each, with clear names and descriptions
- **Knowledge bases**: data sources and their ingestion recipes
- **Chat interface**: Workato GO, Slack, Teams, or an API client. Also user access and guardrails.

## 3. Build (Workato MCP)
1. Read `kb/docs/en/workato-api/agent-studio.md` for payloads. Tools: `post_agentic_genies`,
   `post_agentic_skills`, `post_agentic_knowledge_bases`, `post_agentic_genies_assign_skills`,
   `post_agentic_genies_assign_knowledge_bases`, `post_agentic_genies_start`.
2. Build the skill recipes (workato-recipe-builder), then create the skills.
3. Create the knowledge bases and assign their sources.
4. Create the Genie in the project folder, then assign the skills and knowledge bases.
5. Test the conversation flows. Start the Genie only on the user's approval.
