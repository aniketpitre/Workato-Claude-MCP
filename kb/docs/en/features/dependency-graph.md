---
url: 'https://docs.workato.com/en/features/dependency-graph.md'
description: >-
  Use the Workato dependency graph to visualize relationships between workspace
  assets and analyze the impact of upstream and downstream changes.
---

# Dependency graph

The **Dependency graph** visualizes the relationships between assets in your workspace. You can use this feature to analyze dependencies and the potential impact of asset changes.

Refer to the following sections for more information about using the Dependency graph to view upstream and downstream dependencies in your workspace:

- [Access the Dependency graph](#accessing-graph)
- [Navigation features](#viewing-features)
- [Supported assets](#supported-assets)

![Workato Dependency graph](/assets/recipes.Cmh6tNoo.png)_Workato Dependency graph_

Watch a quick video overview

[Video](https://www.youtube.com/embed/9JaetuTIBoM?rel=0&rel=0)

> **FEATURE AVAILABILITY**
> 
> The Dependency graph is included in specific pricing plans. Refer to your pricing plan and contract to learn more.

## Access the Dependency graph

Complete the following steps to access the Dependency graph:

1. Sign in to your Workato account.
   
2. Go to **Operations hub > Dependency graph** in your workspace.
   
3. Select an [Asset](#supported-assets) type, such as **Connections**.
   
4. Select a specific asset to view its interdependencies. The following example shows interdependencies for an **Asana - Team** connection:
   
   ![Selecting a connection in the Connections Dependency graph](/assets/selecting-asset.D5Umaz6c.gif)
   
5. Click an asset to open a view of its interdependencies, or hover over the asset and click the (outbound link) icon to open the asset in a new browser tab.
   
   **Click an asset**
   
   ![Opening interdependency view for dependency](/assets/inspect-dependency.CUaFVdgI.gif)_Click an asset to open a view of its interdependencies._
   
   **Click the outbound link icon**
   
   ![Dedicated dependency page icon in Dependency graph](/assets/open-dependency-page.C6YWOhzu.png)_Hover over the asset and click the (outbound link) icon to open the asset in a new browser tab._
   

## Navigation features

You can use the following features to navigate the Dependency graph:

- **Zoom in/out**: Click the zoom percentage in the upper-right corner to open the zoom menu, then select **Zoom in**, **Zoom out**, or a specific zoom level.
- **Fit to screen**: Select **Fit to screen** to adjust the graph to your screen size.
- **Drag**: Click and drag anywhere on the graph to pan.

![Dependency graph navigation controls](/assets/navigation-controls.Dxb-uoGx.png)

## Supported assets

Select an asset type from the **Asset** drop-down menu to view its dependencies:

- **[Apps](/en/connectors)**: Shows how recipes use various apps. By default, the graph displays all apps in **Active** recipes. You can display inactive recipes using the **Recipe status** filter.

Apps

You can use the **Apps** view to determine:

- **Which apps your team is integrating or automating**: The Apps Dependency graph only includes apps with at least one connection.
  
- **The flows you're creating for a single app**: Click an app to view its overview, which displays the app's individual connections, the recipes that use each connection, and more.
  
- **Which apps are most highly used**: The number below each app icon indicates how many recipes use the app.
  
- **How your team uses apps together**: Connecting lines show which apps are used together in recipes. When you hover over an app, the lines display a number indicating how many recipes use both apps together.
  

For example, the following Box app is used in 3 recipes total, including 2 recipes that also use Salesforce:

![Number of recipes connected apps are used in together](/assets/app-graph-connected-apps.CbusxOYR.gif)

- **[Recipes](/en/recipes/building-recipes)**: Shows how a specific recipe uses connections and other resources.
- **[Connections](/en/connections)**: Shows the recipes that use a specific connection, including custom connections.
- **[Environment properties](/en/features/account-properties)**: Shows how your recipes use a specific environment property.
- **[Genies](/en/agentic/agent-studio)**: Shows how a specific genie uses connections, skills, and knowledge bases.
- **[Knowledge bases](/en/agentic/agent-studio#knowledge-base)**: Shows how your genies use a specific knowledge base.
- **[Skills](/en/agentic/skills)**: Shows how your genies and MCP servers use a specific skill.
- **[API collections](/en/api-mgmt/api-collections)**: Shows the usage of API endpoints in a specific API collection.
- **[Custom connectors](/en/developing-connectors/sdk#what-is-a-custom-connector)**: Shows the recipes that use a specific custom connection.
- **[Workflow apps](/en/workflow-apps)**: Shows how a specific workflow app uses data tables and recipes.
- **[Pages](/en/workflow-apps/builder-experience#pages)**: Shows how your recipes and Custom apps use a specific page.
- **[Lookup tables](/en/features/lookup-tables)**: Shows how your recipes use a specific lookup table.
- **[MCP servers](/en/mcp/mcp-servers)**: Shows how a specific MCP server uses skills and API collections.
- **[Project properties](/en/features/project-properties)**: Shows how your recipes use a specific project property.
- **[Event topics](/en/connectors/pubsub)**: Shows how your recipes use a specific Event topic.
- **[Data tables](/en/data-tables)**: Shows how your recipes and custom apps use a specific data table.
- **[Common data models](/en/features/common-data-model)**: Shows how your recipes use a specific custom object.
- **[Templates](/en/features/message-template)**: Shows how your recipes use a specific message template.
- **[Data pipelines](/en/data-orchestration/data-pipeline-recipe/create-data-pipeline-recipe)**: Shows the usage of a specific data pipeline.

---
