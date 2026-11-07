---
url: 'https://docs.workato.com/en/agentic/agent-studio/test-genie.md'
description: >-
  Use Test mode to chat directly with your genie and test skill and knowledge
  base retrieval with custom use case scenarios.
---

# Agent Studio Test mode

Test mode lets you run your genie in a live, isolated environment during development. You can chat directly with your genie and set up frequently repeated scenarios to test specific responses. The LLM reads your job description, calls skills, and searches the knowledge base. This setup mirrors production behavior.

Test mode allows you to test your genie by asking your own questions or using your own set of established common scenarios. For example, an **Authentication issues** sample scenario may include the following prompts:

- `I can't log in to my account.`
- `Can you reset my password?`
- `My user ID isn't recognized.`

You can add custom prompts to your scenarios to observe how your genie performs in specific use cases. Refer to [Permissions and access governance](/en/agentic/agent-studio/test/permissions-and-access-governance) for information on how to provide testing access to users.

## Test mode workflow

Test mode relies on the following workflow:

- **Skills run against live connected systems**: Your Submit Leave Request skill connected to your production HR system submits real leave requests during testing. Temporarily connect the skill to a sandbox environment or be prepared to reverse whatever it creates before running a test that triggers a write operation. Your recipe doesn't know it's being called from a test session.
  
- **Intermediate messages are visible during execution**: Intermediate Messages are visible in Test mode and have parity with the messages that are shown in production. Your genie sends intermediate messages with real-time status updates and partial findings as it works through a task before the final response is generated. Intermediate messages are supported in Slack, Microsoft Teams, and Workato GO. For example, if a user asks your genie to summarize the knowledge base, the genie first sends an intermediate message, such as `I'll search the knowledge base and provide you with a summary` before returning the final two-sentence summary. You can use **Test** mode to observe intermediate messages in the conversation history panel to verify that your genie is communicating progress accurately and helpfully at each step.
  

> Intermediate messages are automatically enabled on all supported chat interfaces. You can disable intermediate messages for genies at the project level. Refer to [Disable intermediate messages](/en/agentic/agent-studio/chat-interface/chat-interface#disable-intermediate-messages) for more information.

- **Each test session maintains its own conversation context**: Your genie remembers what was said earlier in the same test session. This means you can run multiple test scenarios back to back without resetting, but context from the first scenario bleeds into the second and produces misleading results. Use the **Reset** button between scenarios to clear the conversation history and start fresh.
  
- **Test mode uses your builder identity, not an end-user identity**: Skills using [Verified User Access](/en/agentic/agent-studio/verified-user-access) to execute with the requesting user's credentials use your credentials as the builder when called in Test mode. Identity-dependent behavior, such as fetching leave balances, reflects your account instead of the end-user. Consider this when you review results.
  

## Test mode connections

Your genie executes skills using the connection established in the recipe even when skills use [Verified user access](/en/agentic/agent-studio/verified-user-access). This means that your genie doesn't use an end-user connection configured in the skill when testing.

Complete the following steps if you encounter issues with skill execution during testing:

1. Verify that the recipe's connection is properly configured and authenticated.
   
2. Check the recipe's logic to ensure it's working as expected.
   
3. Ensure the connection includes the required permissions and scopes for the operations you plan to test.
   

## Create a sample scenario and test messages

You can create a custom sample scenario and add your own messages to it. You can add multiple messages to each scenario. Refer to [Best practices for testing agents](/en/agentic/agent-studio/test/best-practices) for more examples on how to structure your tests.

Complete the following steps to create a sample scenario and messages:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Agent Studio**. A list of your existing genies displays.
   
3. Select the genie where you plan to add a scenario and messages.
   
4. Click the mode toggle to switch from **Build** to **Test**.
   
5. Go to the **Start testing** section and click **\+ Add scenario**.
   
   ![Start testing](/assets/start-testing-section.XpH1HmVM.png)_**Start testing** section_
   
6. Provide a name and description for your scenario.
   
   ![Add scenario](/assets/add-scenario.CQs0JRTj.png)_Add scenario_
   
7. Click **Add scenario**. The new scenario displays in the sidebar.
   
8. Click **+Add message**.
   
9. Enter a message you plan to add to the scenario.
   
   ![Add message](/assets/add-message.7RB8kw86.png)_Enter a message_
   
10. Click the ✓ (checkmark) icon to save the message.
    
11. Select a message from the sample scenario message options. Your message is automatically logged and saved to the conversation history panel.
    

### Edit a sample scenario message

Complete the following steps to edit a sample message:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Agent Studio**. A list of your existing genies displays.
   
3. Select the genie you plan to test.
   
4. Click the mode toggle to switch from **Build** to **Test**.
   
5. Go to the **Start testing** section and select the sample scenario you plan to use.
   
6. Click the message you plan to edit.
   
7. Click **...** (ellipses) and select **Edit message**.
   
8. Update the message for your use case.
   
9. Click the ✓ (checkmark) icon to save the updated message.
   
10. Select the message you edited from the sample scenario message options. Your message is automatically logged and saved to the conversation history panel.

---
