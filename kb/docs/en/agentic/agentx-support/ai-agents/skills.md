---
url: 'https://docs.workato.com/en/agentic/agentx-support/ai-agents/skills.md'
description: >-
  Create and manage AgentX Support skills that detect user intent and route
  conversations to the right response flow for your AI agent.
---

# AgentX Support - Skills

Skills help the AI agent understand user intent and determine which response [flow](/en/agentic/agentx-support/ai-agents/flows) to trigger.

When a user message matches a skill, the agent routes the conversation to the associated flow. The flow defines how the agent responds, whether by sending messages, guiding the user through a process, calling APIs, or triggering external workflows.

You can create and manage skills from the **Skills** tab.

![Skills](/assets/skills.DAUIrPho.png)_Skills_

## Create a skill

Complete the following steps to add a skill to your AI agent:

1. Select your AI agent.
   
2. Click **\+ Add skills**.
   
3. Enter a meaningful name and description for the skill. The agent uses these to understand customer queries and match them to the appropriate response.
   
   ![Add skills](/assets/add-skills.CGeKuvi1.png)_Add skills_
   
4. Specify the **Type** for the skill.
   
   - Select **Flow** to associate the skill with a predefined step-by-step interaction.
   - Select **Policy** to define a goal-driven behavior using a set of instructions the agent should follow. If you select this option, enter a **Goal** and **Instructions** to guide the agent in handling the customer's request.
5. Optional. Click **\+ New Tag** to add tags to the skill for easier filtering and organization.
   
6. Click **Submit**.
   

## Add sentences to a skill

You can add example sentences to a skill to help the AI agent understand how customers might express that need. These examples improve the agent's ability to recognize relevant questions and route them to the correct skill.

We recommend adding at least five varied and natural-sounding examples that reflect how customers might phrase their requests.

Complete the following steps to add a sentence for a skill:

1. Click the skill.
   
2. Select the **Sentences** tab.
   
   ![Add sentences for skills](/assets/add-sentences.D4Ta2dyw.png)_Add sentences for skills_
   
3. Enter a sentence in the **Type an example matching the intent** textbox and press Return.
   
   Alternatively, you can add sentences in bulk by clicking **\+ Bulk upload**.
   
4. Optional. Click the wand icon next to a sentence to generate additional example sentences.
   
5. Click **Save**.
   

## Activate and deactivate skills

You can change the status of skills by clicking the **Status** toggle. This instructs the AI agent to not execute the response and fall back to the default workflow.

---
