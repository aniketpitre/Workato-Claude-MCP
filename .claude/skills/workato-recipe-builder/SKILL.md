---
name: workato-recipe-builder
description: Design and build Workato recipes (triggers, actions, conditions, loops, formulas, error handling, recipe functions) in the connected workspace via Workato's official hosted MCP server (`workato`), grounded in the local Workato docs knowledge base. Use when the user asks to create, fix, explain or improve a Workato recipe or automation.
---

# Build a Workato recipe

## 1. Understand the goal
Pin down the recipe design inputs from `kb/docs/en/recipes/building-recipes.md`:
- **Goal**: what the recipe does
- **Data flow**: which data moves or changes
- **Apps**: which apps send, receive, or process the data
- **Trigger**: what starts the job
- **Error handling**: what happens when a step fails

## 2. Research the docs (always)
```bash
python3 kb/search.py "<app> <trigger or action name>" -s Connectors
python3 kb/search.py "<concept, e.g. repeat helper / monitor error / batch>"
```
- Connector specifics: `kb/docs/en/connectors/<app>.md` and its `triggers/` and `actions/` folders.
  Check the trigger type (polling, real-time, or scheduled), the required inputs, and the limits.
- Logic: `kb/docs/en/recipes/steps.md`, `loops.md`, `kb/docs/en/recipes/best-practices-error-handling.md`
- Formulas: `kb/docs/en/formulas/*.md`
- Reusable logic: recipe functions in `kb/docs/en/features/callable-recipes.md`
- Cost: `kb/docs/en/recipes/optimizing-task-usage.md`

## 3. Check the workspace (Workato MCP)
- Recipe tools: `get_recipes`, `get_recipes_` (read existing code as a template), `post_recipes`,
  `put_recipes_`, `post_recipe_validators_validate`, `get_recipes_jobs`, `get_recipes_test_cases`.
- List projects and folders, existing connections, and similar recipes to reuse.
- Note which connections are missing. The user must authorize new connections in the Workato UI.

## 4. Propose, then build
1. Present the plan: project or folder, recipe name (`kb/docs/en/recipes/naming-conventions.md`),
   trigger, numbered steps, data mappings, error handling, and connections used.
2. Wait for the user to confirm.
3. Write the recipe `code` JSON (trigger, then actions, then conditions or loops, then the
   monitor/error block). Base it on an existing recipe's code from `get_recipes_`. Validate it with
   `post_recipe_validators_validate`, then create it with `post_recipes` in the project folder.
4. Run recipe tests if available, inspect jobs, and fix errors (`kb/docs/en/recipes/recipe-job-errors.md`).
5. Start the recipe only when the user says so.

## Conventions
- Never build in Home assets. Use a project folder.
- Wrap external calls in a Monitor block with a meaningful error path.
- Prefer batch or bulk triggers and actions for volume. Keep polling intervals sensible.
- State which KB pages informed the design.
