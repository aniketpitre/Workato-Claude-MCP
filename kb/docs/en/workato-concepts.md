---
url: 'https://docs.workato.com/en/workato-concepts.md'
description: >-
  Learn core Workato concepts including recipes, triggers, actions, conditional
  statements, connections, and jobs that power automated workflows.
---

# Concepts

This page provides conceptual information about recipe workflows, triggers, actions, conditional statements, and more.

> **SUMMARY**
> 
> - Recipes are user-created automated workflows in Workato that can span multiple apps. Every recipe consists of a trigger and one or more actions.
> - Triggers are events that start recipe actions, either in real-time or at scheduled intervals.
> - Recipe steps, such as actions, conditional actions, and list actions, execute every time a trigger event occurs.
> - Connections authorize recipes to interact with apps, and a job represents the flow of each trigger event through a recipe.

## Recipes

A recipe is an automated workflow that executes a series of steps to integrate and process data across multiple applications. Every recipe includes a trigger that initiates the workflow and one or more actions that execute when a trigger event occurs. Recipes use connectors to interact with different apps, ensuring seamless data flow across systems.

Recipes run in the background, continuously monitoring for trigger events and executing actions automatically. If a recipe is stopped and later restarted, it resumes processing from where it left off. Recipes can also be public or private, allowing for collaboration and reuse across Workato users.

Learn more about [recipes](/en/recipes).

> **WORKATO ACADEMY**
> 
> Explore [Workato Academy](https://academy.workato.com) to gain hands-on experience with the Workato platform. Complete the Workato Foundations courses to learn how to use Workato effectively in your workflows. [Get started](https://academy.workato.com/learn/courses/80/workato-foundations-level-1-on-demand).

### Connections

A connection authorizes a recipe to interact with apps like Salesforce and Zendesk through triggers and actions. Connections are reusable, allowing you to use the same connection across multiple recipes.

Learn more about [connections](/en/connections).

![Connections](/assets/connections.lyIZY7l6.png)_Salesforce and Zendesk connections from the recipe view_

### Triggers

A trigger specifies the event that initiates the actions in a recipe.

Triggers can be activated in various ways. For example, they might activate when a specific event occurs in an app, a new line is added to a file, or on a scheduled basis.

![Trigger example](/assets/trigger-example.BinshFIp.png)_An example of a trigger_

Depending on the API, Workato either receives trigger events in real-time or periodically polls the app to detect them.

Learn more about [triggers](/en/recipes/triggers).

### Steps and actions

A recipe executes steps each time a trigger event occurs. Every recipe requires at least one step. The simplest step is an action, such as creating an organization in Zendesk.

![Action example](/assets/action-example.CL-CiTXy.png)_An example of an action_

Steps in Workato can include actions, conditional actions, list actions, actions that call other recipes, or try/catch blocks.

Learn more about [recipe steps](/en/recipes/steps) and [actions](/en/recipes/actions).

### Datatree and datapills

Video guide: Datatree, data mapping, and data types

[Video](https://www.youtube.com/embed/OXv-qVdGKl0)

Every step, including triggers, adds data to the recipe. This data is accessible in the recipe through the datatree.

The datatree contains individual data fields called datapills. You can use datapills in subsequent steps to map data to input fields. Learn more about [datapills](/en/recipes/data-pills-and-mapping).

The following screenshot displays the output datatree for the **New Salesforce account** trigger. This datatree lists all variables available when a trigger event occurs.

![Output datatree](/assets/output-datatree.HB1YHzMj.png)_Output datatree for the New Salesforce account trigger_

When a new Salesforce account is created, the following values become accessible:

- Account Description
- Account Fax
- Account ID
- Account Name
- Account Phone
- Account Source
- Account Type

You can map these values to input fields in subsequent recipe steps.

### Input fields and fields mapping

Triggers and actions include input fields. The values you map to these fields define how triggers and actions execute customized workflows. Input fields accept variables (datapills) or constants.

Inserting variables (datapills) or constants into input fields is called fields mapping. Learn more about [fields mapping](/en/recipes/data-pills-and-mapping#fields-mapping).

The following screenshot displays an expanded view of the **Create organization in Zendesk** action, with values mapped to its **Name** and **Notes** input fields.

![Input fields](/assets/input-fields.CQCVIAw3.png)_Input fields for the Create organization in Zendesk action_

#### Mapping variables

The Salesforce Account Name (Step 1) datapill is mapped to the **Name** input field. This mapping ensures that the name of each new Salesforce account detected by the recipe becomes the organization name in Zendesk. For example, a Salesforce account named **Sattei Winery** creates a Zendesk organization named **Sattei Winery**.

![Input field with variable mapping](/assets/input-field-with-variable.BnHcfkM1.png)_Input field with variable mapping_

#### Mapping constants

The **Notes** input field maps to the constant, `Synced over from Salesforce`. This mapping ensures all Zendesk organizations created through Workato include the phrase `Synced over from Salesforce` in their **Notes** field.

![Input field with constant mapping](/assets/input-field-with-constant.CJ84o0fR.png)_Input field with constant mapping_

The following screenshot displays the newly created Zendesk organization:

![Newly created Zendesk organization](/assets/zendesk-organization.CAvxEpwK.png)_Newly created Zendesk organization Sattei Winery_

### Jobs

A job represents the flow of a trigger event through the recipe. Each time a trigger event occurs, the recipe executes its actions. Jobs succeed when all actions execute successfully. If an error occurs, subsequent actions do not run unless error handling is configured.

Learn more about [jobs](/en/recipes/jobs).

#### Job report

The job report summarizes all trigger events processed by the recipe. Each trigger event's flow through the recipe is a job.

This report provides details such as the date, time, and job ID for each processed job. Click a job to view more detailed information.

Learn more about [job reports](/en/recipes/jobs#viewing-job-reports).

![Jobs history](/assets/jobs-history.DuXxNdcK.png)_Job report page_

#### Job details

The job details page provides step-by-step input and output for a single trigger event as the recipe processes it. You can use this page to troubleshoot recipes by viewing the data passed into each step and the output returned after each step executes.

Learn more about [job details](/en/recipes/jobs#viewing-details-for-a-specific-job).

![Job details page](/assets/job-details-page.Y-iEcqjG.png)_Job details page showing details of the Create organization in Zendesk action_

---
