---
url: 'https://docs.workato.com/en/workflow-apps/component-actions/translation-app.md'
description: >-
  Build a Workflow app that uses Run recipe actions and AI by Workato to
  translate documents into a target language.
---

# Example use case: Translation app

This example demonstrates how to create a simple page powered by [Run recipe](/en/workflow-apps/component-actions/run-recipe) and [Reset/reload components](/en/workflow-apps/component-actions/reset-components) actions and [variables](/en/workflow-apps/component-actions#variables). This app enables end-users to translate documents into any target language using [AI by Workato](/en/connectors/ai-by-workato).

> **EXAMPLE USE CASE**
> 
> This guide uses a translation use case and is intended to serve as an example. Recipe modifications, such as trigger, action, and conditional logic configuration, may require additional customizations to suit your specific requirements.

## Prerequisites

- [AI by Workato](/en/connectors/ai-by-workato)
- Workflow apps with the [Run recipe](/en/workflow-apps/component-actions/run-recipe) and [Reset/reload components](/en/workflow-apps/component-actions/reset-components) actions enabled

Creating a translation app consists of the following steps:

1. [Create a new app](#app-create)
2. [Design your app](#app-design)
3. [Enable actions](#actions-enable)
4. [Configure your recipe](#recipe-configure)
5. [Surface recipe output in page components](#page-finalize)
6. [Publish your app](#app-publish)

**_You can also start with an existing Workflow app. If you have an existing app where you want to enable run recipe and reset/reload components actions, proceed to [Enable actions](#actions-enable)._**

## Create a new app

Create a new app

Complete the following steps to create a new app:

1. Go to **Platform > Workflow apps portal**.
   
2. Click **\+ New app**.
   
3. Go to the **Project name** field and provide a unique name for the project.
   
4. Go to the **App name** field and type a unique name for the application. This name is visible to the end-users of your app.
   
5. Deselect the **Submit requests** and **Review requests** options.
   
6. Click **Create project**.
   

## Design your app

Design your app

1. Go to your new app and click **Create page**.
   
2. Go to the **Page name** field and type a unique name for the page.
   
3. Modify existing page components:
   
   1. Click the text component at the top of the page and go to the properties panel to customize the app title and supporting text.
      
   2. Click the **Name** component and click the **Delete** icon to remove it from your page.
      
   3. Click the **Description** component, go to the **Properties** panel and type `Text to translate` in the **Label** field.
      
   4. Mark this component as **Required**.
      
   5. Customize the color, image, and resize the main container as necessary.
      
4. Add a component that enables app users to specify their text’s original language:
   
   1. Go to the **Page components** panel and select a **Single-select** component. Drag and drop it onto your page.
      
   2. Go to the **Component properties** panel and select **Manual** as the source and provide a list of **Options**.
      
   3. Leave this field as **Optional**.
      
   4. Go to the **Hint** field and type `Leave blank to let the app detect the original language automatically`.
      
5. Add a component that requires app users to select a target language:
   
   1. Go to the **Page components** panel and select a **Single-select** component. Drag and drop it onto your page.
      
   2. Go to the **Component properties** panel, select **Manual** as the source, and provide a list of languages as options.
      
   3. Mark this field as **Required**.
      
6. Add a component that requires app users to select an output format for the translated text:
   
   1. Go to the **Page components** panel and select a **Single-select** component. Drag and drop it onto your page.
      
   2. Go to the **Component properties** panel, select **Manual** as the source, and provide a list of options. In this example, we are providing `html`, `markdown`, and `plain text`.
      
7. Add a container to your page that will hold the translated text:
   
   1. Go to the **Page components** panel and select a container.
      
   2. Drag and drop it onto your page.
      
   3. Go to the **Page components** panel and select a text component. Drag and drop it onto your page.
      
   4. Go to the **Component properties** panel and type `Translated text` in the **Text** field.
      
   5. Go to the **Page components** panel and select a text component. Drag and drop it onto your page.
      
   6. Leave this component blank for now.
      
   7. Go to the **Page components** panel and select a button component. Drag and drop it onto your page.
      
   8. Go to the **Component properties** panel **\> Design** and type `Reset` in the **Label** field.
      
   9. Click the **Action** tab.
      
   10. Go to the **Action** menu and select **Reset components’ value**.
       
   11. Go to the **Components** field and select the component values you plan to clear, for example, **Page**.
       
   
   Your configuration should look as follows:
   
   ![Reset button configuration](/assets/translate-reset-button.BUjZbLbt.png)_Reset button configuration_
   
8. Click **Preview** to preview your app’s appearance.
   
9. Click **Save**.
   

## Enable actions

In this example, we plan to enable the following functionality for our application:

- When users click **Submit**, a recipe runs that translates their original text into the target language they specify.
- This recipe returns the translated text to the application.
- Users can click a **Reset** button to reset values for all page components, enabling them to translate a new text.

Enabling the **Run recipe** action requires working in the page editor and the recipe editor.

Complete the following steps to enable action when users click **Submit**:

1. Select the **Submit** button.
   
2. Go to the **Properties panel > Action**.
   
3. Use the **Action** drop-down menu to select **Run recipe**.
   
4. Use the **Recipe** drop-down menu to click **Create recipe**. This opens the **Set up your recipe** page in a new browser tab.
   

## Configure your recipe

Customizing this recipe consists of modifying the trigger, adding additional recipe steps, and returning data to page components.

Complete the following steps to set up your recipe:

1. Go to the **Name** field and provide a unique name for your recipe that distinguishes its purpose.
   
2. Select a location for your recipe. The recipe must be contained within the same project as your Workflow app.
   
3. Click **Start building**.
   
   Workato generates a recipe pre-configured with the **New component event** (real-time) trigger and the **Return data to component** action:
   
   ![Recipe outline](/assets/new-component-event-outline.jvzr1OeR.png)_Recipe outline_
   
4. Modify the New component or drop-down event trigger
   
   1. Select the **New component or drop-down event** trigger.
      
   2. Go to the **Setup** tab.
      
   3. Go to **Input parameters** and click **\+ Add field**.
      
   4. Go to the **Name** field and provide a unique name for this parameter.
      
   5. Go to the **Label** field and provide a unique name for this parameter, such as `target language`.
      
   6. Go to the **Data type** field and select **String**.
      
   7. Go to the **Optional** field and select `Yes` or `No`. When `No`, users must provide input for this parameter in the corresponding Workflow apps field.
      
   8. Optional. Go to the **Hint** field and provide a hint to help users fill out this field.
      
      Your configuration should look as follows:
      
      ![Input parameter configuration](/assets/translate-input-parameter.BbH8G2nU.png)_Input parameter configuration_
      
   9. Create the following additional input parameters:
      
      | Parameter name | Label | Data type | Optional |
      | --- | --- | --- | --- |
      | source\_text | Source text | String | No |
      | output\_format | Output format | String | Yes |
      
   10. Go to **Output schema** and click **\+ Add field**. This portion of the configuration enables you to define the type of data you plan to return to your app.
       
   11. Go to the **Name** field and provide a unique name for this parameter, such as `translated_text`.
       
   12. Go to the **Label** field and provide a unique name for this parameter, such as `translated text`.
       
   13. Go to the **Data type** field and select **String**.
       
   14. Go to the **Optional** field and select `Yes` or `No`. When `No`, users must provide input for this parameter in the corresponding Workflow apps field, and this field should also be marked as required.
       
   15. Optional. Go to the **Hint** field and provide a hint to help users fill out this field.
       
   
5. Add additional recipe steps
   
   Add an additional recipe step to get data from other applications and return it to your app. This step uses AI by Workato to translate text.
   
   1. Click **Step 2**.
      
   2. Search for and select **AI by Workato** as your app.
      
   3. Select the **Translate text** action.
      
   4. Go to the **Output language** field and map in the Target language (Step 1) datapill.
      
   5. Go to the **Source text** field, type `Translate the following into`, and map in the Output format (Step 1) and Source Text (Step 1) datapills.
      
   
   Your configuration should look as follows:
   
   ![Datapill mapping](/assets/translate-ai-workato.DF6J01IP.png)_Datapill mapping_
   
6. Modify the return data to component action
   
   Complete the following steps to return the translated text to your page:
   
   1. Select the **Return data to component** action.
      
   2. Go to the **Consider action as successful** field and select `Yes`.
      
   3. Go to the **Translated text** field and map in the Translated text (Step 2) datapill.
      
   4. Optional. Go to the **Successful toast message** field and provide a custom success message. Otherwise, no successful message is displayed.
      
   5. Click **Save** and **Exit**.
      
   6. Click **Start recipe**.
      
   

Your completed recipe should look as follows:

![Completed recipe](/assets/translate-recipe-complete.BTwYijC-.png)_Completed recipe_

## Surface recipe output in page components

Return to the page editor to surface translated text in page components.

Complete the following steps to finalize your app:

1. Create a page variable
   
   1. Click the page canvas.
      
   2. Go to **Properties panel > Design**.
      
   3. Click **\+ Add variable**.
      
   4. Go to the **Name** field and type a unique name for your variable, such as `translated text`.
      
   5. Go to the **Data type** field and select `String`.
      
   6. Optional. Provide a default value for your variable, such as <null>.
      
   7. Click **Done**.
      
   
   Your configuration should look as follows:
   
   ![Create a variable](/assets/translate-variable-create.BMXKV-WQ.png)_Create a variable_
   
2. Map in datapills
   
   1. Click the **Submit** button to select it and go to the **Component properties** panel.
      
   2. Go to the **source text** field and map in the Value (Text to translate) datapill.
      
   3. Go to the **Target language** field and map in the Selected value (Target language) datapill.
      
   4. Go to the **Output format** field and map in the Selected value (Output format) datapill.
      
   
   Your configuration should look as follows:
   
   ![Map in input parameters](/assets/translate-input-parameters.UQfbpEWo.png)_Map in input parameters_
   
3. Configure a variable
   
   This variable is used to return the translated text to your app.
   
   1. Go to the **Recipe output to set value > Recipe output** field and select **translated-text**. This is the output field you defined in your recipe.
      
   2. Go to the **Set value for** field and select the **translated-text** variable.
      
   
   Your configuration should look as follows:
   
   ![Use recipe output to set variable values](/assets/translate-variable-map.I6qW2ubn.png)_Use recipe output to set variable values_
   
4. Map your variable into a component
   
   This variable will contain the translated text.
   
   1. Go to the **Translated text** container.
      
   2. Select the **Text** component.
      
   3. Go to the **Properties panel > Text**.
      
   4. Map in the Translated-text datapill from the **Page data** module.
      
   
   Your configuration should look as follows:
   
   ![Variable configuration](/assets/translate-variable.CRbjdTzb.png)_Variable configuration_
   
5. Click **Save** and **Exit**.
   

## Publish your app

Complete the following steps to publish your app:

1. Go to the project that contains your app.
   
2. Click **Go live**.
   
   **_One or more user groups must be added to your app before you can publish it._**

---
