---
url: 'https://docs.workato.com/en/workflow-apps/component-actions/file-use-case.md'
description: >-
  End-to-end example of a Workflow app that uses a file component and a Run
  recipe action to upload a profile picture to an external system and preview it
  in the page.
---

# Example use case: File upload

The following example demonstrates how to configure a Workflow app that lets users upload a profile picture, store it in an external system, and preview it before the user submits the page.

## Enable action on file upload

Complete the following steps to enable a **Recipe run** action on file upload:

1. Create a new Workflow app or select an existing one.
   
2. Select a **file** component and go to the **Action** panel. The action's **Trigger** event is pre-selected as `Value changed`.
   
3. Use the **Action** drop-down menu to select `Run recipe`.
   
4. Use the **Recipe** drop-down menu to click **Create recipe**. This opens the **Set up your recipe** page in a new tab.
   
   ![Action setup](/assets/action-setup.CxgQ59nV.png)_Action on file upload setup_
   

## Configure a recipe to process a file uploaded to your app

1. Enter a unique **Name** for this recipe.
   
2. Use the **Location** drop-down menu to ensure the recipe is in the same folder as your app page.
   
3. Click **Start building**.
   
   Workato generates a recipe pre-configured with the **New component event** (real-time) trigger and the **Return data to component** action:
   
   ![Recipe outline](/assets/new-component-event-outline.jvzr1OeR.png)_Recipe outline_
   
4. Modify the New component event trigger
   
   1. Select the **New component event** trigger.
      
   2. Go to the **Setup** tab.
      
      The setup tab displays the recipe's input and output parameters. Use them to receive data, such as files, from your page and return data back to it.
      
   3. Go to **Input parameters** and click **Add input parameters**.
      
   4. Define the page data, in this case a file to use in your recipe. You must provide the **Name**, **Data type**, and **Optional** status for each input parameter. You can also provide an optional **Label** and **Hint**.
      
      Select `File` as the **Data type** to pass a file uploaded to your app to the recipe.
      
      ![Configure input parameters](/assets/input-parameters-recipe.CyksOhTq.png)_Configure input parameters_
      
   
5. Configure an action in an app
   
   Complete the following steps to configure one or more **Action in an app** steps to process the uploaded file. For example, you can save the uploaded profile picture to your organization's HR management software.
   
   1. Click **Select an app and action** step in the recipe.
      
   2. Search for and select the app you plan to use. A list of available actions for the app displays.
      
   3. Select the action you plan to use, such as a file upload, download, or attachment action in a document storage or content management system.
      
   4. Select the connection type you plan to use for the component event recipe.
      
      ![Connection type](/assets/ruc-recipe.CyQNjW7-.png)_Choose a connection type_
      
      - **End user's connection**: Workflow apps recipes perform actions based on the identity and permissions of the user who connects to the application. End users authenticate with their own credentials to retrieve or modify data in an external app.
      - **This recipe's connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
      
      **_Only app connections that use OAuth 2.0 authorization code grant are available for end user's connection. Refer to [Verified user access](/en/agentic/agent-studio/verified-user-access) for more information._**
      
   5. Select an existing connection or click **\+ New connection** to [create a new connection](/en/connections#connection-basics).
      
   6. Configure the action based on your requirements.
      
   7. Map the File name (Step 1) or File contents (Step 1) datapills into the action's input fields as necessary to save the file.
      
   8. Add additional steps as required.
      
   
6. Modify the Return data to component action
   
   Complete the following steps to return recipe data to your app:
   
   1. Select the **Return data to component** action.
      
   2. Use the **Consider this action as successful?** drop-down to define whether the action completed successfully.
      
   3. Click **Save** and **Exit**.
      
   

## Configure your app to preview the profile picture

You can configure your app to preview the uploaded profile picture by mapping the file component into an image component.

> **INFO**
> 
> Image components only support image file types, such as `.png`, `.jpg`, and `.jpeg`.

1. Return to the page editor and add a new **Image** component to your page.
   
2. Go to the **Source** section of the properties panel and select **Page data**.
   
   ![Page data selected as the image source in the properties panel.](/assets/page-profile-picture.DsPF1vgP.png)_Select **Page data** as the image source_
   
3. Use the **Image data** drop-down menu to select the file component input to display.
   
4. Enter **Alt text** for your image.
   
5. Use the **Visible** toggle to make the image visible in all conditions or only under specific conditions. For example, you can make this component's visibility **Conditional** so that it only displays after a file has been uploaded.
   
6. Optional. Modify the **Image fitting** setting to make the image **Resize to fit** or **Expand to fill** its container.
   
7. Optional. Modify the **Horizontal alignment**.
   
8. Optional. Modify the **Vertical alignment**.
   

![Preview an uploaded image](/assets/profile-image.COyRwfhg.png)_Preview an uploaded image_

---
