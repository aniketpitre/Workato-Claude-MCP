---
url: 'https://docs.workato.com/en/connectors/a2a/resume-task.md'
description: >-
  You can resume a task in the INPUT_REQUIRED state after receiving a text
  response.
---

# A2A Protocol - Resume a task

An agent returns the task in the `INPUT_REQUIRED` state when it needs clarification. You can route the agent's question through an app, such as a Jira issue, a Workbot message, or other approval flow to get a response. The agent resumes the task with a second **Send task** action after the agent receives a response from the app.

The following is an example workflow to resume a task:

1. Configure a step that captures a human response to the agent's question. The following are examples of how apps can retrieve a human response:
   
   - **Direct send**: Use if the required information is already available in the recipe data, such as a field from the trigger. Pass this information directly to the follow-up Send Task.
   - **Jira ticket**: Create a Jira issue with the agent's question as the description. An assignee reviews and updates the ticket, then a separate recipe triggers on ticket resolution and returns the answer.
   - **Workbot message**: Send a Workbot DM or channel message to the relevant person. Collect the reply by using the Workbot interaction trigger. Send the reply as the follow-up message.
2. Add a second **Send task** action after the human response is collected.
   
3. Map the task ID from the first **Send task** action to the **Task ID (resume only)** field of the second action.
   
4. Map the human response into the **Message** field.
   

When the agent receives the follow-up message with the existing task ID, it resumes the original task rather than starting a new one.

---
