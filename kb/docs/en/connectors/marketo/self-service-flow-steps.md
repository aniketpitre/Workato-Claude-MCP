---
url: 'https://docs.workato.com/en/connectors/marketo/self-service-flow-steps.md'
description: >-
  Learn how Marketo self-service flow steps work with Workato to send lead data
  in bulk from smart campaign flows, plus setup steps and FAQs.
---

# Marketo - Self-service Flow Steps

[Self-service Flow Steps](https://experienceleague.adobe.com/docs/marketo/using/product-docs/core-marketo-concepts/smart-campaigns/flow-actions/flow-step-service.html?lang=en) in Marketo enable you to integrate custom actions directly into your smart campaign flows. With Workato, you can design these flow steps to efficiently send lead data in bulk to any connected application, streamlining your marketing automation processes.

## Benefits of Self-service Flow Steps

Self-service Flow Steps offer several benefits:

- Reusable flow steps across services
  
- Create reusable flow steps that marketers can quickly incorporate into their custom flows. This approach eliminates the need to rely on lists within Marketo to initiate integrations with Workato.
  
- Higher throughput for lead processing
  
- Add Workato flow steps to batch campaigns in Marketo, allowing you to process thousands of leads simultaneously as a single job within the recipe.
  

## Use cases

- Integrate with CRM and sales tools
  
- Create custom flow steps that automatically add leads to other platforms, such as [Outreach](/en/connectors/outreach) or [Salesforce](/en/connectors/salesforce).
  
- Advanced segmentation with product data
  
- Pull product usage data from [Snowflake](/en/connectors/snowflake) and sync it to leads in Marketo for more refined segmentation.
  
- Enhanced lead enrichment
  
- Perform advanced lead enrichment using vendors like [ZoomInfo](/en/connectors/zoom-info) or Clearbit, ensuring your lead data is comprehensive and up-to-date.
  
- Sync data from ABM tools
  
- Pull insights from ABM (account-based marketing) tools like 6sense or Demandbase and sync them directly to leads in Marketo.
  

## How to use Self-service Flow Steps in Workato

Self-service Flow Steps in Workato combine a trigger and an action to streamline your Marketo integrations. For the Marketo connector, use the following:

- [New Marketo Self Service Flow Step trigger](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger): This trigger receives data from the Marketo flow.
- [Return data to Marketo Self Service Flow Step action](/en/connectors/marketo/return-data-to-marketo-self-service-flow-step-action): This action sends data back to Marketo to update the lead.

### Steps to configure Self-service Flow Steps

#### In Workato

1. Sign in to your Workato instance.
   
2. Create a new recipe.
   
3. Enter a name for your recipe in the **Name** field, select the location where you plan to store it in the **Location** field, and select **Trigger from an app** in the **Pick a starting point** field.
   
4. Click **Start building**.
   
5. Search for and select **Marketo** as your app.
   
6. Select the [New Marketo Self Service Flow Step trigger](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger).
   
7. Select your **Marketo** instance.
   
8. Copy the **Swagger Endpoint URL** in the trigger hint. This value is required to add a new service in Marketo:
   
   ```text
   https://marketo-gateway.workato.com/api/v1/users/{YOUR_USER_ID}/recipes/{YOUR_RECIPE_ID}/swagger
   ```
   
9. Configure the [input fields](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger) for the trigger. Be sure to save the API key you provide in this step, as this value is required to add a new service in Marketo.
   
10. Click **`+` Add step > Action in app**.
    
11. Select **Marketo** as your app.
    
12. Select the [Return data to Marketo Self Service Flow Step action](/en/connectors/marketo/return-data-to-marketo-self-service-flow-step-action).
    
13. Configure the [input fields](/en/connectors/marketo/return-data-to-marketo-self-service-flow-step-action) for the action.
    
    At this point, your recipe should resemble the following: ![sample-flow-step](/assets/sample-flow-step.DG39hRWL.png)_Self-service Flow Steps recipe_
    
14. Optional. Add more steps to your recipe to send or retrieve data from other apps.
    

#### In Marketo

1. Sign in to your Marketo instance.
   
2. Navigate to **Admin > Integration > Service providers** and click **Add new service**.
   
   ![sample-flow-step](/assets/add-new-service.z9U1nkrH.png)_Create a new service in Marketo_
   
3. Provide the **Swagger Endpoint URL** (from the help section of your trigger) in the **URL** field.
   
4. Provide the **API key** from the trigger configuration in the **API key** field.
   
   In the following steps, verify in Marketo the fields being sent to and from Workato. These must match the inputs specified in your Workato trigger configuration.
   
5. Create a campaign with a flow to test your newly registered flow step. As you send leads through the flow, you should see jobs created in Workato.
   
6. Continue to refine your recipe as required to meet your use case. If you need to include additional lead attributes or flow inputs from Marketo, you can adjust your trigger configuration. You must register a new service in Marketo each time you update the trigger configuration.
   

## Self-service Flow Steps FAQs

Why doesn't my updated recipe display new incoming or outgoing fields for my Marketo Self-service Flow Step?

Since Self-service Flow Steps are registered only once during service setup, you must retire your old Self-service Flow Step in Marketo and register a new one.

Why are some lead fields not mapped properly during service setup?

Today, our Self-service Flow Steps only support `string` data type fields. Alternatively, use the [Get leads action](/en/connectors/marketo/get-objects-action) to get the lead fields you require and the [Update leads action](/en/connectors/marketo/update-object-action) to update the lead fields.

Why aren't some lead fields sent from Marketo transferred to the trigger output in Workato?

Verify that you have mapped your fields properly in the service setup. Each field you have selected in your `incoming lead attributes` should be mapped to the lead attribute in Marketo during the service provider setup.

![Service field mapping setup](/assets/field-mapping-setup.D3G-Bb-Y.png)

Why does Marketo ask me to resolve collisions?

The service name and flow step name are derived from your recipe name. As such, you can see collisions with other flow steps if they share the same exact name. Marketo prompts you to provide a different name to distinguish it from existing flow steps.

![Resolve collisions](/assets/resolve-collisions.Ba2m_OLm.png)

  

> **FURTHER READING**
> 
> - [New Marketo Self Service Flow Step trigger (real-time)](/en/connectors/marketo/new-marketo-self-service-flow-step-trigger)
> - [Return data to Marketo Self Service Flow Step action](/en/connectors/marketo/return-data-to-marketo-self-service-flow-step-action)

---
