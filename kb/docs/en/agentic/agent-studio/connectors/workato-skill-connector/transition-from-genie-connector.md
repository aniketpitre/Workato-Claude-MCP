---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/workato-skill-connector/transition-from-genie-connector.md
description: >-
  What changes moving from the Workato Genie connector to the Workato Skill
  connector, and how to migrate an existing skill.
---

# Transition from the Workato Genie connector

Skills were previously exclusively defined with the [Workato Genie connector](/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector). The Workato Skill connector now provides the skill functionality of the Workato Genie connector without requiring access to genies and is the default for new skills. This page describes what changes for builders, the status of skills built on the Workato Genie connector, and the steps to migrate an existing skill.

## What's new for builders

The Workato Skill connector changes the availability of skills and allows builders to replace a skill trigger:

- **Plan availability**: Builders on Business MCP and Enterprise MCP plans can create and use skills without Workato Agent Studio.
- **Trigger flexibility**: Workato sets the **Start workflow** trigger as the default when you create a skill. After you configure the **Start workflow** trigger, you can replace it with another trigger.

## Workato Genie connector skill deprecation

The **Start workflow** trigger and **Return response** action in the [Workato Genie connector](/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector) are deprecated and won't receive new enhancements. Existing skills built on the Workato Genie connector continue to function and remain assignable to genies.

## Frequently asked questions

Refer to [Workato Skill connector FAQs](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector-faqs) for answers to common questions about the transition.

## Migrate an existing skill

Complete the following steps to migrate a Workato Genie connector skill to the Workato Skill connector:

1. Select the skill to migrate.
   
2. Click **...** (More actions), then select **Clone**. Cloning the recipe lets you migrate and test the new skill without affecting live agents.
   
3. Use the **Where do you want to save your copy?** drop-down menu to select where to save the recipe copy.
   
4. Click **Clone**.
   
5. Click **Edit**.
   
6. Select the Workato Genie connector **Start workflow** trigger and replace it with the Workato Skill connector **Start workflow** trigger.
   
7. Recreate the parameters schema and result schema in the new trigger. Refer to the [Start workflow trigger](/en/agentic/agent-studio/connectors/workato-skill-connector/start-workflow) documentation for more information.
   
8. Replace the Workato Genie connector **Return response** action with the Workato Skill connector **Return response** action.
   
9. Enter the values to return to the calling agent for each parameter in the **Results** section. Refer to the [Return response action](/en/agentic/agent-studio/connectors/workato-skill-connector/return-response) documentation for more information.
   
10. Test the recipe to confirm it's configured correctly.
    
11. Assign the skill to any MCP servers or genies that previously used the Workato Genie connector skill.
