---
url: 'https://docs.workato.com/en/agentic/agentic.md'
description: >-
  Agentic is a low-code platform for building and managing AI agents called
  genies that take action and orchestrate workflows across your systems.
---

# Agentic

Agentic provides a low-code, no-code platform for building and managing AI agents that take action and orchestrate workflows dynamically. Agents built in Agent Studio are called genies. Each genie has a job description, skills, and knowledge bases that define how it acts across your systems, collaborates with other agents, and executes complex workflows end to end.

## Workato Agent Registry

[Agent Studio](https://app.workato.com/genies) serves as a centralized agent registry for your organization. It provides a single place to publish, discover, consume, and govern access to every genie in your organization, whether [packaged](/en/agentic/workato-genies) or [custom](/en/agentic/agent-studio).

![Agent Studio](/assets/ai-hub.DNPo8b6H.png)_Agent Studio_

Each genie in the registry has an agent card that describes the genie's capabilities and configuration. Agent cards contain the following information:

- **[AI model](/en/agentic/agent-studio/ai-model/ai-model)**: The LLM that powers the genie.
- **[Chat interface](/en/agentic/agent-studio/chat-interface/chat-interface)**: The interface through which users interact with the genie, such as Slack, Microsoft Teams, or Workato GO.
- **[Job description](/en/agentic/agent-studio/ai-model/ai-model)**: The genie's defined role, goals, and behavioral constraints.
- **[Skills](/en/agentic/skills)**: The actions and workflows the genie can execute.
- **[App events](/en/agentic/agent-studio/app-events)**: Triggers from external systems that enable the genie to act proactively without waiting for user input.
- **[KPIs](/en/agentic/agent-studio/action-board)**: The outcomes the genie is designed to drive or measure. KPIs are only available for genies that use the Workato GO chat interface.

![Agent card](/assets/skill-card.CKlN-XQ2.png)_Agent cards display the genie's AI model, skills, job description, and more_

Agent cards give enterprises a standardized way to describe and manage agents across their organization, with access controls that define who can consume or interact with each genie.

You can use [XChange](/en/xchange) to package genies through a governed review and approval workflow for distribution across workspaces. You can distribute approved packages to child workspaces or [publish to the community library](/en/xchange#publish-a-package-to-library), where users with XChange access can discover and install the packages.

## Agent version management

You can manage versions at two levels as you iterate on a genie's skills, prompts, and job description:

- **Skills**: Each skill maintains a version history as changes are made. You can compare versions, roll back to a previous version, and run test cases against a specific version. Refer to [Skill version management](/en/agentic/skills/version-management) for more information.
- **Environments**: You can maintain separate copies of a genie across development, test, and production [environments](/en/features/environments). Versions can be [deployed](/en/features/environments/deployment) from one environment to the next as they are validated, and multiple versions can run in parallel across environments.

**Skills**

![Skill version management](/assets/skill-versioning.CM6FSBZV.png)_Skill version management_

**Environments**

![Agent version management](/assets/agent-version-management.Qk11lSak.png)_Agent version management_

Refer to [Lifecycle and operations](/en/recipes/managing-recipes) for more information.

## Large action models (LAM)

Large action models (LAM) extend LLMs with the ability to plan and execute multi-step workflows autonomously across apps and data systems.

Agent Studio lets you build large action models by extending an LLM of your choice with reasoning, skill discovery, and workflow orchestration. The result is a genie that can execute multi-step business processes [autonomously](/en/agentic/agent-studio/agent-orchestration), going beyond knowledge retrieval to take action across enterprise apps. These models continuously improve by observing live process instances on the platform, learning which action sequences succeed and adapting their behavior to increase accuracy and reliability over time.

## Multi-modal input and output

Genies support multiple input types including text, images, and documents such as PDFs, Word files, and CSVs. Inputs can come from multiple [knowledge bases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) that store and sync content from connected systems, or directly from end users through chat interfaces such as Slack, Microsoft Teams, and [Workato GO](/en/agentic/workato-go). Files submitted through the chat interface can also be [passed to skills](/en/agentic/agent-studio/upload-files-and-images#add-files-and-images-to-your-skill-recipes) for downstream processing.

Refer to [Upload files and images](/en/agentic/agent-studio/upload-files-and-images) for supported file types and size quotas.

## Agent memory

Genies retain context within a session innately, and can reference earlier messages to maintain continuity throughout a conversation.

You can configure the following features for persistent memory across sessions:

- Use [knowledge bases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) to store reference content such as policies, documentation, and conversation history that genies retrieve through semantic search when responding to users. Refer to [Connect your knowledge base to Confluence](/en/getting-started/use-cases/agent-studio/knowledge-bases/knowledge-base-confluence-use-case) for a worked example.
- Use [Data tables](/en/data-tables) to store structured records that genies can query through skills for exact results, aggregations, or user-specific data. For example, store conversation IDs per user so the genie retains context across multiple interactions. Refer to [Build a personal assistant genie with Telegram](/en/getting-started/use-cases/agent-studio/genies/personal-assistant-genie-telegram-agent-orchestration-use-case) for a step-by-step example.

## Decision models and agents

Skills can invoke [decision models](/en/recipes/decision-models) using the [Decision Models connector](/en/features/decision-models/decision-models-by-workato) and enable genies to apply complex conditional business logic without that logic being embedded in the skill itself.

This separates policy management from agent logic. Business rules can be updated in the decision model without modifying the genie's skills or job description.

Refer to the following use cases for worked examples:

- [Process purchase orders with a procurement genie](/en/getting-started/use-cases/agent-studio/genies/procurement-genie-decision-model): Decision model in a skill for deterministic order fulfillment
- [Route requests across agents with a decision model](/en/getting-started/use-cases/agent-studio/genies/route-requests-across-agents-decision-model): Decision model for multi-agent routing

## Agent-to-agent communication

Genies can delegate tasks to other genies using skills that call the [Assign task to genie](/en/agentic/agent-studio/agent-orchestration#assign-task-action) action. This enables multi-agent architectures where a primary genie hands off subtasks to specialist genies and acts on the returned response, supporting patterns such as classification, routing, validation, and chained processing.

Genies can also call any [A2A Protocol](https://a2a-protocol.org/latest/)\-compliant agent using the [A2A Protocol connector](/en/connectors/a2a). A2A is an open standard for AI agent interoperability across frameworks and vendors, including Google ADK, LangGraph, Amazon Bedrock AgentCore, and Azure AI Foundry. This allows Workato genies to delegate tasks to external agents and act on the result, and supports both synchronous and asynchronous patterns.

## Genie conversation observability

You can review genie conversation history directly in the Workato UI. The **Conversations** page shows a full record of past interactions, and each skill invocation runs as a job with its own history in the [Operations hub](/en/features/admin-dashboard).

![Genie conversation history](/assets/conversations-observability.IzctXPls.png)_Genie conversation history_

Refer to [Conversations history](/en/agentic/agent-studio/conversations) for more information on reviewing conversations, debugging errors, reviewing retention, and configuring access permissions.

Workato also supports log streaming to destinations, such as Amazon S3, Splunk, or Datadog, and [API access](/en/workato-api/agent-studio#conversations) to query conversation history programmatically. This provides compliance for integration with external observability pipelines. Refer to [Genie conversation events](/en/features/activity-audit-log-streaming-sample#genie-conversations) for sample conversation logs.

> **FEATURE AVAILABILITY**
> 
> Genie conversation streaming and API access are only available to users on specific pricing plans. Refer to your pricing plan and contract to learn more.

## Skills

Skills equip genies with a toolset to take action and respond to end users. Each skill has the following parts:

- Logic that executes when the genie invokes it.
- A skill prompt that tells the genie when and how to use the skill.

Skills can connect to any Workato-supported app, a custom API, a data table, or an external MCP server.

Refer to [Skills](/en/agentic/skills) for more information.

---
