---
url: 'https://docs.workato.com/en/airo/blueprints.md'
description: >-
  Blueprints transform business requirements into implementation plans. AIRO
  recommends the Workato asset that fits each requirement.
---

# Blueprints

Blueprints map business requirements to the Workato assets a solution needs. You can start with a complete requirements document, such as a product requirements document or business requirements document, or with a high-level concept, and AIRO works with you to fill in gaps and refine your requirements.

AIRO analyzes your requirements and generates a blueprint that identifies the assets your solution needs. The blueprint follows Workato best practices and helps you understand the project requirements before you build any assets. You can explore each asset to understand its purpose and select which assets AIRO builds.

![Blueprint builder view of an Employee Onboarding Automation blueprint, showing recipe, function, and API cards connected by CALLS relationships](/assets/blueprints.wyCCLXYE.png)_A blueprint with the assets AIRO identified for the solution_

Refer to [Create your first blueprint](/en/airo/blueprints/create) for a walkthrough that builds an employee onboarding solution.

## View blueprints

You can view your blueprints by going to **Projects > Blueprints**.

![View blueprints at the workspace level](/assets/blueprints-sidebar.CacrSRrt.png)_View blueprints at the workspace level_

Alternatively, select a specific project or folder and click the **Blueprints** tab.

![View blueprints from within your project](/assets/blueprints-in-projects.Dbm6OjRt.png)_View blueprints from within your project_

Refer to [Manage blueprints](/en/airo/blueprints/manage) to rename, delete, sort, and filter them.

## Which assets can AIRO build from a blueprint?

AIRO can build the following assets from blueprints:

- Recipes
- Recipe functions
- API recipes
- Genies
- Skills
- MCP servers

AIRO can't build the following asset types from a blueprint:

- Event topics
- Lookup tables
- Data tables
- Message templates
- Common data models
- Data pipelines
- Workflow apps

> **KNOWLEDGE BASES**
> 
> Knowledge bases aren't part of a blueprint's asset map. If a genie in the blueprint requires a knowledge base, AIRO creates or updates it separately and attaches it directly to the genie.

## How does AIRO decide what to build first?

AIRO builds assets in dependency order, not the order in which they appear in the blueprint. For example:

- Recipe functions are built before recipes that call them.
- Skills are built before genies or MCP servers that use them.
- API recipes and recipe functions are built before MCP servers that expose them.
- Genies are built after their required skills and knowledge bases are available.

This ensures each asset's dependencies are ready before it's built.

---
