---
url: 'https://docs.workato.com/en/recipes/projects-faqs.md'
description: >-
  Answers to common questions about Workato projects, including what they are,
  how to organize them, and their key components.
---

# Projects FAQs

Get answers to frequently asked questions (FAQs) about projects.

## What is a project in Workato?

View answer

A **Project** in Workato is a repository where you can store integration assets such as recipes, connections, and sub-folders. It serves as a container for organizing related assets, typically grouped by department, use case, application, or process. [Projects](/en/projects#projects) allow you to manage and share integration components efficiently across teams.

## How should I organize projects in my workspace?

View answer

We recommend that you organize projects based on **use case**, **department**, **application**, or **process** to maintain a clear structure. For example:

- **By department**: Organize projects for HR, Finance, and IT.
- **By use case**: Separate projects to automate onboarding, invoicing, or reporting.
- **By app**: Group all recipes and connections related to a specific application, such as Salesforce or NetSuite.

Proper organization simplifies management and helps team members find assets. Refer to the [Best practices for projects](/en/projects#best-practices-for-using-projects) section for detailed recommendations.

## What are the key components of a project?

View answer

Each project contains the following:

- **Recipes**: Automation workflows that perform tasks.
- **Connections**: Links between Workato and external applications, such as Salesforce or Slack.
- **Folders and sub-folders**: Structures for organizing recipes and connections within a project.
- **Smart folders**: Dynamic folders that display assets you can access based on their status (active/inactive).

This structure enables flexible and efficient organization of all integration assets. Learn more about the [key components of a project](/en/projects#projects).

## How do I share connections across multiple projects?

View answer

You can share connections across multiple projects in Workato to enable teams to reuse established integrations and avoid duplicating setup efforts. For example, a Salesforce connection used in a CRM project can be shared with a marketing automation project without creating a new connection. Refer to [Connections](/en/projects#assets-page) for more information.

## What are the best practices for managing project lifecycles in Workato?

View answer

Ensure the following when managing the [lifecycle of a project](/en/projects#best-practices-for-using-projects):

- **Consistency between workspaces**: Before importing a project to a new workspace, verify that a project with the same name exists. If not, create one to maintain organization.
- **Organize root-level assets properly**: If you import a project into the `All Projects` destination, each folder converts into a separate project, which may clutter your workspace.

Following these steps helps maintain a clean and efficient workspace.

## What is the home assets project, and how is it used?

View answer

The [Home assets](/en/projects#home-assets) project is a default folder where all imported and deployed assets are displayed when **All Projects** is selected. It is automatically created in older workspaces when the projects feature is introduced. If you import assets and do not specify a project, the assets are placed in the Home assets folder. This helps keep unorganized assets in one location for easier management.

## How can I create and organize a project in Workato?

View answer

Complete the following steps to create a project:

1. Go to the **Projects** menu.
   
2. Select **Create > Project** or press C+P.
   
3. Enter a **Project name**.
   
4. Select a starting point for your project:
   
   - **Build a recipe** to create a project that contains a [recipe](/en/recipes).
   - **Build a genie** to create a project that contains a [genie](/en/agentic/workato-genies).
   - **Build an MCP server** to create a project that contains an [MCP server](/en/mcp).
   - **Build an app** to create a project that contains a [workflow app](/en/workflow-apps).
   - **Start from scratch** to create a blank project.
5. Create folders within the project to store your recipes and connections.
   

Folders allow you to categorize assets within the project for better organization. For example, you can separate recipes by use case. Learn more about how to [create a project](/en/projects#create-a-project-and-folder).

You can also customize your projects with colors and icons. Refer to [Customize a project](/en/projects#customize-a-project) for more information.

## How do permissions work for projects in Workato?

View answer

Project permissions are managed through a combination of [environment roles](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles) and [project roles](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) in the [new permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2):

- **Environment roles**: Control whether collaborators can create projects, manage project membership, and assign project roles in an environment.
- **Project roles**: Control what collaborators can view, create, edit, deploy, or delete within a specific project.

For example, an **Environment admin** can create a project but must also have a **Project admin** role to manage project content.

In workspaces using the legacy permissions model, collaborator roles control both project level and environment level permissions. Refer to the [Migrate to the new access control model](/en/user-accounts-and-teams/role-based-access/migrate-roles) guide to split legacy roles into project and environment roles in the new model.

Refer to the [Privileges reference](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference) for a full list of available permissions.

## What are Smart Folders, and how do they help manage projects?

View answer

[Smart Folders](/en/projects#smart-folders) dynamically display all recipes and connections you can access across your projects. You can filter contents by various attributes such as active/inactive recipes or connected/disconnected connections. Smart folders improve asset management across different projects, particularly in larger workspaces with multiple integrations.

## Can I move assets between projects, and how does it impact dependencies?

View answer

Yes. You can [move assets](/en/projects#move-assets-folders-recipes-connections), such as recipes, connections, and folders, between projects using a drag-and-drop interface. When you move an asset, all dependencies are resolved automatically, ensuring that workflows function correctly. For example, if a recipe relies on a connection, moving it to a different project maintains the connection.

---
