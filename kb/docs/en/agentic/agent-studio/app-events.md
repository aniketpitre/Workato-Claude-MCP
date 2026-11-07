---
url: 'https://docs.workato.com/en/agentic/agent-studio/app-events.md'
description: >-
  Learn how to create App Events that enable genies to proactively respond to
  triggers from external systems like Salesforce or Zoom, without waiting for
  user input.
---

# App Events

App Events enable genies to act proactively by responding to triggers from external systems, such as Salesforce or Zoom, instead of waiting for a user to initiate a conversation. These events help embed genies directly into existing workflows and allow genies to anticipate user needs and offer assistance without being prompted.

App Events enable you to:

- Automate complex tasks that are difficult to define in recipes.
- Surface relevant tasks to users at the right time.
- Reduce user burden by helping organize, manage, and complete tasks.
- Increase genie effectiveness by giving it context earlier in the process.

Watch a quick video guide: Create an App Event in Agent Studio

[Video](https://www.youtube.com/embed/Wlqks9dwZhk?rel=0&si=6CfFTTD2uBnTuCa5)

For example, ITGenie receives a notification that a new request for NetSuite access was just approved for you by the IT team. ITGenie automatically processes this app event to determine if next steps are required.

![App event example](/assets/app-event-example.HNrIJwi0.png)_App event example_

Refer to [App Events vs Agent orchestration](/en/agentic/agent-studio/app-events-vs-agent-orchestration) for recommended uses for App events and Agent orchestration.

## Create an app event

Complete the following steps to create an app event for your genie:

1. Sign in to Workato.
   
2. Go to **AI Hub > Agent Studio**. A list of your existing genies displays.
   
3. Select the genie where you plan to add an app event.
   

You can create a dedicated recipe from the genie editor, or add the action to an existing recipe.

**Create from the genie editor**

1. Go to the **Triggers** section and click **\+ Add**.
   
2. Select **Notify a user from a recipe**.
   
   ![Menu for adding a trigger to a genie, with Notify a user from a recipe selected.](/assets/add-app-events.BpRDSElj.png)_Triggers section menu_
   
   Workato creates a recipe with the **Send business event** action already added and opens the recipe editor. Refer to the [Send business event](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/send-business-event) action reference for a field-level description of inputs and outputs.
   
   ![Recipe editor showing the Send business event action already added to the recipe.](/assets/send-app-event.BIVdx_rh.png)_**Send business event** action in the recipe editor_
   
3. Optional. Rename the recipe.
   
4. Click **Select an app and trigger event** and configure the trigger that should fire this app event.
   

**Add to an existing recipe**

1. Go to the recipe where you plan to add an app event.
   
2. Click the **Select an app and action** step.
   
3. Search for and select `Workato Genie`.
   
4. Select the **Send business event** action.
   

### Configure the action

Complete the following steps to configure the **Send business event** action:

1. Click the **Send business event** action.
   
2. Ensure that the correct genie is selected in the **Genie** field.
   
   ![Send business event action setup](/assets/app-event-setup.5HCBHWB7.png)_**Send business event** action setup_
   
3. Enter the email of the user who should receive notification in the **User email** field.
   
   > **USER ACCESS**
   > 
   > The user you select must be active and have assigned access to this genie.
   
4. Go to the **Notification to user** field and enter the notification you plan to send before the genie starts processing the event.
   
5. Go to the **Business event data** field and enter a prompt to tell the genie what it should do. For example:
   
   ```plaintext
   
   Complete the following steps to process this lead:
   
   - Search Salesforce for leads and then create or update the lead.
   - Search Salesforce for matching accounts. Create or update the account and attach the lead.
   - Research the company and lead on the internet.
   - Provide a summary for the SDR by adding it to the lead in Salesforce.
   - Prepare an agenda for the prospective call for the SDR.
   ```
   
6. Optional. Enter the conversation ID in the **Conversation ID** field if you plan to enable the genie to continue a previous conversation with the user.
   
7. Test your recipe to ensure workflow compatibility with your genie.
   
8. Click **Save**.
   
9. Click **Start recipe** to activate it.

---
