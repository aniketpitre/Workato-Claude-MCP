---
url: 'https://docs.workato.com/en/recipes/decision-models.md'
description: >-
  Learn how Workato decision models centralize reusable conditional business
  logic with decision tables, branches, and schema configs.
---

# Decision models

Decision models are scalable and reusable assets that streamline and centralize complex conditional business logic. Decision models allow teams to improve consistency and reduce maintenance by building logic once and reusing it across multiple recipes and projects.

Decision models contain [decision tables](/en/features/decision-models/decision-tables) that evaluate fields, conditional branches that control the flow of data, and schema configurations that define the inputs and outputs. Refer to the [Model components](#decision-tables) section for an overview of decision model components or the [Set up a decision model](/en/features/decision-models/model-builder) page for detailed configuration steps.

The [Decision Models connector](/en/features/decision-models/decision-models-by-workato) calls an existing decision model from a recipe, including skill recipes used by genies and MCP servers, and returns the results for use in downstream recipe steps. This behavior is similar to the [Recipe functions](/en/connectors/recipe-functions) connector, which calls an existing recipe.

> **ROLE BASED ACCESS CONTROL**
> 
> You can configure access to decision models using Workato [role-based access control](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets).
> 
> [Custom roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#custom-roles) created before April 1, 2026 don't have permissions to access decision models. Contact a workspace admin to update your permissions if you require access to decision models.

## Model components

Decision models include the following components:

**Decision tables**

**Decision table** nodes define conditional business rules. They intake data (Input fields), evaluate it based on business logic you specify, and output results (Output fields) accordingly. Refer to [Create a Decision table node](/en/features/decision-models/model-builder#create-a-decision-table-node) to add a Decision table to a model.

![Decision table node](/assets/decision-table-node.C2EIJ6gb.png)_Decision table node_

Alternatively, refer to [Configure decision table rules](/en/features/decision-models/decision-tables#configure-decision-table-rules) to configure evaluation logic for a decision table.

![Example decision table for routing marketing leads](/assets/decision-table.DubRYOmN.png)_Example decision table for routing marketing leads_

**Model Inputs**

A **Model Inputs** node defines the input schema of the Decision model. These fields are supplied to the model from the recipe that calls it and are available as inputs in any node. Refer to [Create an input field](/en/features/decision-models/model-builder#create-an-input-field) to configure a **Model Inputs** node.

![Model Inputs node](/assets/input-node.CToAL0vt.png)_**Model Inputs** node_

**Model fields**

The **Fields** sidebar defines the data (model fields) that moves between nodes. Model fields are needed to carry data to the **Model Outputs** node, which returns the fields you specify to the recipe that called the model. Refer to [Create a model field](/en/features/decision-models/model-builder#create-a-model-field) to configure model fields.

![Fields sidebar](/assets/model-fields-sidebar.CsI82MNe.png)_**Fields** sidebar_

**Model Outputs**

A **Model Outputs** node defines the data (Output fields) that the model returns to the recipe that called it. Refer to [Configure output fields](/en/features/decision-models/model-builder#configure-output-fields) to configure a **Model Outputs** node.

![Model Outputs node](/assets/output-node.mrYZOvwL.png)_**Model Outputs** node_

**Conditional branches**

**Conditional branches** define a set of conditions that control the flow of data in the model using business logic you specify. Refer to [Create conditional branches](/en/features/decision-models/model-builder#create-conditional-branches) to configure conditional branches.

![Conditional branch](/assets/conditional-branch.C2a1r0jy.png)_Conditional branch_

---
