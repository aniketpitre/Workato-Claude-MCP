---
url: 'https://docs.workato.com/en/agentic/agent-studio/genies-configuration.md'
description: >-
  Learn the key components of a genie in Agent Studio, including its AI model,
  chat interface, knowledge base, and skills.
---

# Genie key components

A genie is an AI-powered agent that can talk to people, understand what users need, and then perform actions, such as fetch information, run automations, or complete tasks. A genie takes action unlike a typical chatbot that simply provides answers.

> **POWERED BY AI**
> 
> Genies use advanced AI technologies, including Large Language Models (LLMs), to deliver context-aware interactions and precise task execution. Ensure that you review and test your genie’s behavior and skills to meet organizational requirements before deploying it across your workspace.

## Get started with genie key components

Genies consist of the following key components:

| Genie component | Function | Description | Get started |
| --- | --- | --- | --- |
| [AI model and job description](/en/agentic/agent-studio/ai-model/ai-model) | Defines your genie's LLM, behavior, persona, and constraints. | Instructions and guidelines, such as tone, formatting, and role. | [Get started with AI models and job descriptions](/en/agentic/agent-studio/ai-model/ai-model#getting-started-with-ai-models-and-job-descriptions) |
| [Chat Interface](/en/agentic/agent-studio/chat-interface/chat-interface) | Provides a space for users to interact with your genie. | Platform-specific configurations for the interface you select. Options are: Slack, Teams, and Workato GO. | [Get started with chat interfaces](/en/agentic/agent-studio/chat-interface/chat-interface#getting-started-with-a-chat-interface) |
| [Knowledge Base](/en/agentic/agent-studio/knowledge-bases/knowledge-bases) | Provides a source of factual information for answering user questions, such as FAQs, policies, and company data. | Includes structured data, documents, articles, and other text-based resources. | [Get started with knowledge bases](/en/agentic/agent-studio/knowledge-bases/knowledge-bases#getting-started-with-knowledge-bases) |
| [Skills](/en/agentic/skills) | Enables your genie to take action, such as retrieving data from an app or sending a message. | Built using Workato workflows and recipes. | [Get started with skills](/en/agentic/skills#getting-started-with-skills) |

### Learn more about AI models

The AI model you select can affect how your genie interprets the job description, general performance, and whether additional features, such as [Action board](/en/agentic/agent-studio/action-board), is available. Learn more about [AI models](/en/agentic/agent-studio/ai-model/ai-model).

### Learn about genie user access

You can provide end users with access to specific genies after you create an end-user group. Learn more about [user group management](/en/agentic/agent-studio/manage-users-and-access).

## Enhance your genie

You can add additional components to further customize your genie for specific use cases.

| Genie component | Description | Get started |
| --- | --- | --- |
| [App Events](/en/agentic/agent-studio/app-events) | Enable genies to act proactively by responding to triggers from external systems, such as Salesforce or Zoom, instead of waiting for a user to initiate a conversation. | [Get started with App Events](/en/agentic/agent-studio/app-events#create-an-app-event) |
| [Business approvals](/en/agentic/agent-studio/business-approvals) | Build skills with approval workflows to ensure that operations, such as provisioning access to an application, are reviewed by a designated approver before execution. | [Get started with Business approvals](/en/agentic/agent-studio/business-approvals#create-approval-request-action) |
| [Agent orchestration](/en/agentic/agent-studio/agent-orchestration#agent-orchestration) | Enable your genies to work autonomously within recipes with assigned tasks. | [Get started with Agent orchestration](/en/agentic/agent-studio/agent-orchestration#assign-task-action) |
| [Action board](/en/agentic/agent-studio/action-board) | Build a dashboard of KPI metrics for your genie. Action board is only available for genies using Workato GO as the chat interface. | [Get started with Action board](/en/agentic/agent-studio/action-board#create-a-kpi) |

## Learn about genie performance

The [Overview page](/en/agentic/agent-studio/genie-overview-page) includes a metrics dashboard. Each genie built in Agent Studio generates interaction data that you can analyze. The following metrics can help you understand how effectively your genie is performing, whether users are engaging with it, and how its skills and knowledge bases are being used.

- Total conversations
- Total end-user messages
- Unique users
- Response time analysis
- Conversation volume
- Skills usage heat map

The [Conversations page](/en/agentic/agent-studio/conversations) provides a complete view of your genie's interaction history. The Conversations page displays a table of past conversation threads, including key details such as:

- Conversation topic
- User who started the conversation
- Started at
- Last message at
- Started via
- Unique conversation ID
- Number of errors encountered

## Test your genie

[Test mode](/en/agentic/agent-studio/test-genie) allows you to test your genie by asking your own questions or [using your own scenarios](/en/agentic/agent-studio/test-genie#create-a-sample-scenario-and-test-messages) during the build process.

## Explore use cases

[Agent Studio use cases](/en/getting-started/use-cases/agent-studio/agent-studio-use-cases) provide steps on how perform the following actions:

- Create a genie
- Create and connect a knowledge base
- Create a knowledge base recipe
- Create a skill
- Upload files and images to your genie

---
