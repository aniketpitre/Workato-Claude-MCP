---
url: 'https://docs.workato.com/en/agentic/agentx-support/ai-agents/actions.md'
description: >-
  Create actions in AgentX Support that define tasks an AI agent can perform in
  a conversation, with input and output parameters.
---

# AgentX Support - Actions

Actions define the tasks your AI agent can perform during a conversation, such as creating a support ticket, checking an order status, or listing payment methods. Every action consists of a name, description, and a defined set of input and output parameters.

![Actions](/assets/actions.DZp4I8eZ.png)_Actions_

The AI agent automatically invokes actions based on how a skill or flow is configured. When an action is triggered, it can use the returned values to personalize responses or continue the conversation accordingly.

For example:

- If a customer asks to cancel an order, the agent can trigger the `request_order_cancellation` action.
- If the action requires more information, such as an `order_id`, the agent can prompt the customer to provide it.

## Create an action

Complete the following steps to create an action:

1. Select your AI agent.
   
2. Go to **Actions > Actions Definitions**.
   
3. Click **New Action**.
   
4. Select an existing flow to associate with the action.
   
5. Enter an action name in the **Name** field. For example, `create_support_ticket`.
   
6. Enter an action description in the **Description** field. For example:
   
   > If the agent can't assist or the customer requests human help, use this action to create a support case.
   
7. Specify input and output parameters for your action. For example, you can define the following input parameters for the `create_support_ticket` action:
   
   - `name`
   - `email`
   - `subject`
   - `description`
   
   You can then define `status` as an output parameter.
   
8. Click **Submit** to create the action.

---
