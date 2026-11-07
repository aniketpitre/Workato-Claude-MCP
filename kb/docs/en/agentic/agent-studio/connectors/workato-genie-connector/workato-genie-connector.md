---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/workato-genie-connector/workato-genie-connector.md
description: >-
  Use the Workato Genie connector to assign tasks, send business events, manage
  approvals, and store knowledge from within a recipe.
---

# Workato Genie connector

The Workato Genie connector provides actions to interact with genies and their supporting systems from within a recipe.

> **CONNECTOR ACCESS**
> 
> The Workato Genie connector is available to customers on plans with [Agent Studio](/en/agentic/agent-studio) enabled.

## Connection setup

The Workato Genie connector is a built-in connector. It doesn't require authentication or connection setup.

## Actions

The Workato Genie connector supports the following recipe actions:

- [Assign task to genie](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/assign-task-to-genie)
- [Assign task to user](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/assign-task-to-user)
- [Create approval request](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/create-approval-request)
- [Send business event](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/send-business-event)
- [Store knowledge](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/store-knowledge) Deprecated. Refer to [Deprecated features](#deprecated-features) for more information.

## Deprecated features

The following Workato Genie connector features are deprecated. These features continue to function in existing recipes but don't receive new enhancements:

- **Start workflow trigger**: The trigger used to define skills. Replaced by the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector), which provides the same functionality without requiring access to genies. You can't add this trigger to new skills.
- **Return response action**: The action used to return a result from a skill. Replaced by the **Return response** action in the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector).
- **Store knowledge action**: The action used to store documents in a knowledge base. Replaced by the [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents) action in [Knowledge base by Workato](/en/agentic/agent-studio/connectors/knowledge-base-connector/knowledge-base-connector). Existing recipes continue to run unchanged. Refer to [Migrate from the Store knowledge action](/en/agentic/agent-studio/connectors/knowledge-base-connector/knowledge-base-connector#migrate-from-the-store-knowledge-action) for the field mapping.

Refer to [Transition from the Workato Genie connector](/en/agentic/agent-studio/connectors/workato-skill-connector/transition-from-genie-connector) for migration steps.
