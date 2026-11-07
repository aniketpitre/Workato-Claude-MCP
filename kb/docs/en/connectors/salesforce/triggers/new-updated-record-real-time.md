---
url: >-
  https://docs.workato.com/en/connectors/salesforce/triggers/new-updated-record-real-time.md
description: >-
  This trigger monitors Salesforce in real-time for newly created or updated
  objects.
---

# Salesforce - New/updated record trigger (real-time)

This trigger monitors Salesforce in real-time for newly created or updated objects.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object type to monitor. |
| Fields to retrieve | Select the fields to retrieve from the object. Workato retrieves all fields by default. Entering specific fields to retrieve improves recipe performance and mitigates [schema errors](/en/connectors/salesforce/troubleshoot-runtime#schema-errors). |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

### Configuration in Salesforce

Complete the following steps to configure the trigger in Salesforce:

1. Refer to the [Input](#input) section to configure the input fields for this trigger. Workato generates an endpoint URL in the collapsible **HELP** section based on the **Object** you select and the connected Salesforce organization.
   
2. Copy the endpoint URL. This URL tells Salesforce to send real-time events about relevant objects to this Workato recipe.
   
   > **WARNING**
   > 
   > This endpoint URL is unique to the selected object and connected Salesforce organization. You must regenerate this endpoint URL if the object or Salesforce connection changes.
   
   ![Workato generates endpoint URL for Salesforce flow](/assets/new-updated-object-trigger-webhook-url-generate.PfzOTNPZ.gif)_Workato generates endpoint URL for Salesforce flow_
   
3. Use the endpoint URL to configure a [new outbound message in Salesforce](/en/connectors/salesforce/real-time-triggers#configure-a-new-outbound-message-in-salesforce) for the object type this trigger monitors.
   
4. Go to **Setup > Process Automation > Flows** in your Salesforce organization and click **New Flow**. The Salesforce flow setup wizard opens.
   
   ![Open the Salesforce flow setup wizard](/assets/create-new-flow-salesforce.BRgud0Zt.gif)_Open the Salesforce flow setup wizard_
   
5. Select **Record-Triggered Flow**, then click **Create**.
   
   ![Select Record-Triggered Flow in Salesforce](/assets/record-triggered-flow.ClcMvE8V.png)_Select Record-Triggered Flow in Salesforce_
   
6. Select the Salesforce object type to monitor. In `Configure Trigger` select `A record is created or updated`. In `Optimize the Flow for` select `Actions and Related Records`.
   
   > **WARNING**
   > 
   > Do not set any entry conditions as this conflicts with the backup polling mechanism in place.
   
   ![Set up the Salesforce flow to be triggered when record is created or updated](/assets/configure-flow-trigger-salesforce-create-update.CxpOyMwW.png)_Set up the Salesforce flow to be triggered when record is created or updated_
   
7. In the Flow Builder view, click **+** (add element) and select `Action`.
   
8. Go to the **Outbound Message** tab.
   
9. Select the Outbound Message that you previously configured for this trigger.
   
10. Click **Done**, then **Save**.
    
    ![Add Outbound Message as action in Salesforce flow](/assets/add-outbound-message-to-flow-create.B3iu9yqu.gif)_Add Outbound Message as action in Salesforce flow_
    
11. Enter a label and an API Name for the flow, then click **Save**.
    
    ![Save the Salesforce flow](/assets/save-flow-salesforce.CwCcXQrb.png)_Save the Salesforce flow_
    
12. Click **Activate**.
    
    ![Activate the flow in Flow Builder](/assets/activate-flow-salesforce-create-update.Bl3J9Emu.gif)_Activate the flow in Flow Builder_
    
13. Return to Workato and start the recipe.
    

You can test that the recipe is working by causing a trigger event in Salesforce while the recipe is active. Workato creates a new job immediately if the Salesforce flow and Workato trigger are configured correctly.

## Output

The output of this action varies based on your selected **Object** and **Fields to retrieve**. Refer to Salesforce's [Overview of Salesforce Objects and Fields](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_concepts.htm) guide for more information on available objects and fields.
