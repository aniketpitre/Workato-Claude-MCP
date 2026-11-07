---
url: 'https://docs.workato.com/en/recipes/editor.md'
description: >-
  An overview of the Workato recipe editor, including the recipe canvas, the
  toolbar, the step configuration panel, and how to refresh a recipe's schema.
---

# Recipe editor

The recipe editor is where you build and test a recipe. It combines a visual recipe canvas that shows the recipe's trigger and actions, a toolbar to add steps, a panel to configure the selected step, and controls to save, test, and refresh the recipe. You open the editor when you [create a recipe](/en/recipes#create-a-new-recipe) or edit an existing one. When you create a recipe, you first choose a [starting point](/en/recipes#recipe-starting-points) to set its trigger.

![The recipe editor with the AIRO panel open](/assets/recipe-editor.C3abITco.png)_The recipe editor_

The editor also shows which teammates are currently editing the same recipe. Refer to [Collaboration safeguards](/en/recipes/collaboration-safeguards) for more information.

## Build and test views

The editor has two views, which you switch between using the **Build** and **Test** toggle at the top of the editor:

- **Build**: The default view, where you assemble and configure the recipe's trigger and actions on the recipe canvas.
- **Test**: Where you run a test of the recipe and review the results. Refer to [Test your recipe](#test-your-recipe) for more information.

## Recipe canvas

The recipe canvas displays your recipe as an ordered sequence of steps. Every recipe begins with a [trigger](/en/recipes/triggers), which defines the event that starts the recipe, followed by one or more [actions](/en/recipes/steps#action-step). Each step is numbered in the order it runs.

Add step (**+**) buttons appear on the recipe canvas, and between steps when you hover. Click **\+ Add step** to open a menu of common step types you can insert. Select a step on the canvas to open its [configuration panel](#configure-a-step).

![A recipe on the canvas with a Salesforce New Lead trigger and a Slack Post message action](/assets/recipe-canvas.YO52DpqU.png)_The recipe canvas_

## Toolbar

The toolbar at the bottom of the recipe canvas groups the building blocks you can add to a recipe by category. Each button opens a menu of options. Add a step from the **Logic**, **Apps**, **AI**, or **More** menus by dragging an item from the menu onto the canvas. Dragging is required to add a step. Clicking an item without dragging closes the menu without adding it.

![The recipe editor toolbar with Logic, Apps, AI, More, and Ask AIRO buttons](/assets/toolbar.C5o17KRH.png)_The toolbar_

**Logic**

**Logic** adds control flow and non-app steps to the recipe:

- **Action in app**: Add an [action](/en/recipes/actions) from a connected app.
- **IF condition**, **ELSE IF condition**, and **ELSE**: Branch the recipe based on [conditions](/en/features/if-conditions).
- **Repeat for each**: Loop over a list of items with a [Repeat for each](/en/recipes/repeat-for-each) loop.
- **Repeat while**: Loop while a condition is true with a [Repeat while](/en/recipes/loops) loop.
- **Handle errors**: Catch and respond to errors with a [Handle errors](/en/recipes/steps#handle-errors-step) step.
- **Stop job**: End the job with a [Stop job](/en/recipes/steps#stop-step) step.

![The Logic menu open in the toolbar](/assets/toolbar-logic.BSRDyDYh.png)_The Logic menu_

**Apps**

**Apps** opens a searchable list of your connected apps so you can add an app trigger or action. Search for an app, then select a trigger or action to add it to the recipe. Refer to [Connectors](/en/connectors) for more information.

![The Apps menu open in the toolbar](/assets/toolbar-apps.FNnvmz3w.png)_The Apps menu_

**AI**

**AI** adds AI-powered steps to the recipe:

- **Genie**: Add a [Workato Genie](/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector) step.
- **Workato Skill**: Add a [Workato Skill](/en/agentic/skills) step.
- **AI by Workato**: Use the built-in [AI by Workato](/en/connectors/ai-by-workato) connector.
- **OpenAI**: Use the [OpenAI](/en/connectors/openai) connector.
- **Azure OpenAI**: Use the [Azure OpenAI](/en/connectors/azure-openai) connector.
- **IDP by Workato**: Extract data from documents with [IDP by Workato](/en/connectors/idp-by-workato).

![The AI menu open in the toolbar](/assets/toolbar-ai.C4LUr0JV.png)_The AI menu_

**More**

**More** adds steps for other Workato capabilities:

- **API platform**: Build an API endpoint with the [API platform](/en/api-management).
- **Decision model**: Add a [decision model](/en/recipes/decision-models) step.
- **Data table**: Read from or write to a [data table](/en/data-tables).
- **Recipe function**: Call a [recipe function](/en/connectors/recipe-functions).

![The More menu open in the toolbar](/assets/toolbar-more.DHK2206f.png)_The More menu_

**Ask AIRO**

**Ask AIRO** opens the [AIRO](/en/airo) panel, where you can describe what you're trying to create in natural language and get help finding apps, building steps, and answering questions as you work. Use the A+I keyboard shortcut to toggle the AIRO panel in and out of view. Refer to [Build recipes with AIRO](/en/airo/build/recipes) for more information.

![The AIRO panel open on the side of the recipe editor with a chat input](/assets/toolbar-ask-airo.C9mIm4mF.png)_The Ask AIRO panel_

## Add a recipe step

You can add a step to your recipe from the recipe canvas or from the toolbar:

- **From the recipe canvas**: Hover where you plan to add the step and click **\+ Add step** to open a menu of common step types, such as **Action in app**, **IF condition**, **Repeat for each**, and **Handle errors**. Select a step type to insert it at that position.
- **From the toolbar**: Open a category (**Logic**, **Apps**, **AI**, or **More**) in the [toolbar](#toolbar), then drag an item from the menu onto the canvas. Dragging is required to add a step. Clicking an item without dragging closes the menu without adding it.

![The add step button and the step type picker on the recipe canvas](/assets/add-step-standard.DEbq8cJp.png)_The step type picker on the recipe canvas_

Configure the new step in the [step configuration panel](#configure-a-step), then click **Save** to save the recipe.

## Configure a recipe step

Select a step to open its configuration panel, where you set up what the step does. Configuring an app step involves selecting the app, the trigger or action, and the [connection](/en/connections), then filling in the step's input fields.

![The step configuration panel for a Slack action, showing the setup breadcrumb, Help, and input fields](/assets/configure-recipe-step.39tjoBZF.png)_The step configuration panel_

Input fields accept plain values in text mode by default. You can switch a field to [formula mode](/en/formulas/formula-mode) to transform data with formulas. Optional settings, such as a trigger condition, are available through toggles in the panel. An inline help section explains the step, and controls let you search within the configuration or clear it.

You can also [skip a step](/en/recipes/steps/skip-step) to exclude it from a run, which is useful for testing a recipe incrementally.

Use a step's more options (**...**) menu for additional actions, including adding a comment to leave notes for collaborators, copying the step, and applying [data masking](/en/features/data-masking) to hide sensitive values from job history.

## Recipe data

The **Recipe data** panel provides the datapills you can map into step fields. It includes the output of earlier steps, along with a **Properties** datatree that contains [default datapills](/en/recipes/data-pills-and-mapping#default-datapills), [project properties](/en/features/project-properties), and [environment properties](/en/features/account-properties). Drag a datapill from this panel into a field to use it in your recipe. Refer to [Datapills](/en/recipes/data-pills-and-mapping) for more information.

![The Recipe data panel showing the Properties datatree and a step's output datapills](/assets/output-datatree.HB1YHzMj.png)_The Recipe data panel_

## Editor controls

The editor controls let you view, save, test, and maintain the recipe.

**Zoom**

The zoom control adjusts the size of the recipe on the recipe canvas. Select the zoom percentage to open the menu, which offers the following options:

- **Zoom in** and **Zoom out**: Adjust the zoom level incrementally.
- **Fit to screen**: Scale the recipe to fit the canvas.
- **Zoom to 25%**, **Zoom to 50%**, and **Zoom to 100%**: Set a specific zoom level.

The menu also shows the keyboard shortcut for each option.

![The zoom menu open in the editor controls](/assets/control-zoom.DBI9fkHW.png)_The zoom menu_

**Save**

**Save** saves your changes to the recipe and creates a new [recipe version](/en/recipes/version-management).

**Test**

**Test** opens the [Test view](#test-your-recipe) to run the recipe and review the results.

**Exit**

**Exit** closes the recipe editor and returns you to the recipe page.

## Refresh schema

A recipe's schema is the set of fields Workato reads from your connected apps and makes available as datapills. The recipe editor doesn't automatically reflect fields you add, remove, or rename in an app. Click **Refresh** to pull the current field structure from your connected apps so the editor shows the fields that exist now.

The **Refresh** button appears after you add a trigger or an action to the recipe.

![The Refresh control in the editor with a tooltip explaining it updates fields added or removed in your app](/assets/refresh-schema.BBxhIgR1.png)_The Refresh button_

### When to refresh the schema

Refresh the schema when the fields in a connected app no longer match what the recipe editor displays. This commonly happens when you:

- Add, remove, or rename a field in an app that your recipe uses. For example, refresh after adding a [Salesforce](/en/connectors/salesforce/troubleshoot-runtime) custom field so you can map it in your recipe.
- Need an output field or datapill that hasn't appeared yet, such as the **File content** datapill on the [Snowflake Export query result](/en/connectors/snowflake/export-query-result) action.
- See a [design-time error](/en/recipes/recipe-design-time-errors) for an unavailable field, a [job error](/en/recipes/recipe-job-errors) from a schema change, or a broken dependency after [deploying a recipe to an environment](/en/features/environments/deploying-projects-to-an-environment).

### Refresh the schema

Complete the following steps to refresh a recipe's schema:

1. Open the recipe in the recipe editor.
   
2. Click **Refresh**. This pulls the current field structure from the connected apps used in the recipe.
   
3. Review the trigger and action steps for newly available fields, and update any field mappings affected by fields that were removed or renamed.
   
4. Click **Save** to save the recipe.
   

A schema refresh creates a new version of the recipe. Refer to [Recipe version management](/en/recipes/version-management#schema-changes) for more information.

## Test your recipe

Switch to the **Test** view to run test jobs and review the results. If you haven't run a test yet, click **Test** to start one. Refer to [Testing recipes](/en/recipes/testing) for more information.

![The Build and Test toggle and the Test button in the recipe editor](/assets/test-mode-toggle.DfyGX4cL.png)_The Build and Test toggle and the Test button_

Confirm the recipe works as expected before you exit the editor and [start it](/en/recipes/start-and-stop#start-recipe) to begin processing events.

## Keyboard shortcuts

Speed up recipe building with keyboard shortcuts for common actions, such as save, undo and redo, zoom, and skip steps. Refer to [Keyboard shortcuts for recipe design](/en/recipes/keyboard-shortcuts) for the full list for Mac and Windows.

> **FURTHER READING**
> 
> - [Recipe design](/en/recipes/building-recipes)
> - [Triggers](/en/recipes/triggers)
> - [Steps and actions](/en/recipes/steps)
> - [Datapills and mapping](/en/recipes/data-pills-and-mapping)
> - [Recipe version management](/en/recipes/version-management)

---
