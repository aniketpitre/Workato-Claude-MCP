---
url: >-
  https://docs.workato.com/en/getting-started/use-cases/hubspot-salesforce-workbot-for-teams.md
description: >-
  Build a recipe that creates new Salesforce leads from new HubSpot deals and
  posts a message in Microsoft Teams.
---

# Create Salesforce leads from new HubSpot deals recipe

This use case guides you through connecting [HubSpot](/en/connectors/hubspot), [Salesforce](/en/connectors/successfactors/successfactors), and [Workbot for Microsoft Teams](/en/workbot-for-teams/workbot) to create a powerful automation.

## What does this recipe do?

This recipe monitors HubSpot for new deals. If the deal is associated with a contact in HubSpot, the recipe creates a new lead in Salesforce, and Workbot for Microsoft Teams posts a message containing details about the new Salesforce lead.

```mermaid
flowchart TD
  subgraph Configuration[" "]
    direction TB
    subgraph NewDeal[&nbsp HubSpot New deal trigger &nbsp]
      Trigger(Trigger) --- setup1(setup)
    end
    subgraph GetAssociations[&nbsp HubSpot Get associations batch action &nbsp]
      Action1(Action) --- setup2(setup)
    end
    subgraph GetContact[&nbsp HubSpot Get contact action &nbsp]
      Action2(Action) --- setup3(setup)
    end
    subgraph CreateLead[&nbsp Salesforce Create lead action &nbsp]
      Action3(Action) --- setup4(setup)
    end
    subgraph GetLeadDetails[&nbsp Salesforce Get lead details by ID action &nbsp]
      Action4(Action) --- setup5(setup)
    end
    subgraph Workbot[&nbsp Workbot for Microsoft Teams Post message action &nbsp]
      Action5(Action) --- setup6(setup)
    end
  end
  CreateRecipe([Create recipe]) -- Configure your recipe --> Configuration --> Workflow([Automated workflow])
  NewDeal --> GetAssociations --> GetContact -->  CreateLead --> GetLeadDetails --> Workbot
  classDef default fill:#fff,stroke:#67eadd,stroke-width:2px;
  classDef WorkatoTeal fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
  classDef SubgraphDash fill:#e1fffc,stroke:#f66,stroke-width:2px,color:#000,stroke-dasharray: 5 5
  class CreateRecipe,Trigger,setup1,Action1,setup2,Action2,setup3,Action3,setup4,Action4,setup5,Action5,setup6,Workflow WorkatoTeal
  class NewDeal,GetAssociations,GetContact,CreateLead,GetLeadDetails,Workbot SubgraphDash
  classDef SubgraphLight stroke:#67eadd,stroke-width:2px
  class Configuration SubgraphLight
```

## Create your recipe

Complete the following steps to build a recipe that creates Salesforce leads from new HubSpot deals:

> **USE CASES ARE INTENDED AS EXAMPLES ONLY**
> 
> This use case serves as an example. Modifications to triggers, actions, or conditional logic may be necessary to adapt this recipe to your workflow.

1. Sign in to Workato.
   
2. Select the project where you plan to create the recipe.
   
3. Create connections for HubSpot, Salesforce, and Workbot for Microsoft Teams:
   
   Create a HubSpot connection.
   
   ### Create a HubSpot connection
   
   This step creates a connection between Workato and your HubSpot account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `HubSpot` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![Connect to HubSpot](/assets/connect.CRWjdjwr.png)_Connect to HubSpot_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Optional. Expand the **Advanced settings** section and use the **Scopes** drop-down menu to select permissions to request for the connection.
      
   6. Optional. Select the profile for the connection in the **Custom OAuth profile** drop-down menu. Alternatively, [create a new profile for HubSpot](/en/connectors/hubspot/custom-oauth).
      
   7. Click **Connect**.
      
   8. Select the HubSpot account where you plan to authorize Workato and click **Choose Account**.
      
      ![Choose account](/assets/select-account.BvvC0buZ.png)_Select an account_
      
   
   Create a Salesforce connection.
   
   ### Create a Salesforce connection
   
   This step creates a connection between Workato and your Salesforce account.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Salesforce` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![Salesforce connection setup](/assets/connect.CnntY3nd.png)_Salesforce connection setup_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Auth type** drop-down menu to select the authentication method. The default is OAuth 2.0.
      
   6. Use the **Sandbox** drop-down menu to specify whether the Salesforce account is a sandbox account.
      
   7. Optional. Expand **Advanced settings** to configure advanced connection options.
      
   8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
      
      - This custom OAuth profile ensures that the connection is restricted to the same set of scopes you selected for all users with the profile, and the authentication flow uses the client app linked to the custom profile.
   9. Click **Connect**.
      
   10. Enter your Salesforce account credentials and click **Log In**.
       
       ![Salesforce connection setup](/assets/login.CIu5oc0P.png)_Log in to your Salesforce account_
       
   
   Create a Workbot for Microsoft Teams connection.
   
   ### Create a Workbot for Microsoft Teams connection
   
   This step creates a connection between Workato and your Workbot for Microsoft Teams account.
   
   **Note**: You must [add Workbot to Microsoft Teams](/en/workbot-for-teams/getting-started#add-workbot-to-microsoft-teams) before you can establish the connection in Workato.
   
   1. Click **Create > Connection** or press C twice.
      
   2. Search for and select `Workbot for Microsoft Teams` on the **New connection** page.
      
   3. Provide a name for your connection in the **Connection name** field.
      
      ![Connect to Workbot for Microsoft Teams](/assets/connect.BtbzhBLH.png)_Image caption_
      
   4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
      
   5. Use the **Auth type** drop-down menu to select **OAuth 2.0**.
      
   6. Optional. Expand the **Advanced settings** section to select permissions to request for the connection.
      
   7. Optional. Select the custom OAuth profile for the connection in the **Custom OAuth profile** drop-down menu.
      
   8. Click **Sign in with Microsoft**.
      
   
4. Go back to your project and click **Create > Recipe** or press C+R.
   
   ![Create a new recipe](/assets/create-recipe-standard.CiyoivKN.png)_Create a new recipe_
   
5. Select the project where you plan to store the recipe from the **Location** drop-down menu.
   
6. Click **Pick a starting point**, then select **Trigger from an app**.
   
7. Set up your HubSpot New record (deal) trigger.
   
   ### Set up HubSpot New record (deal) trigger
   
   This trigger monitors HubSpot for new deals and retrieves details about the amount and close date.
   
   1. Search for and select the HubSpot connector.
      
      ![Choose HubSpot](/assets/choose.BfILEyWG.png)_Choose HubSpot_
      
   2. Select the **New record** trigger.
      
      ![Select the New record trigger](/assets/new-record.gtCkG8A_.png)_Select the New record trigger_
      
   3. Select **Deal** from the **Object** drop-down menu.
      
   4. Select deal properties to retrieve from the **Properties** drop-down menu. This example selects **Amount** and **Close Date**.
      
      ![Configure the New deal trigger](/assets/new-deal-config.SbnXQGrk.png)_Configure the New deal trigger_
      
   
8. Click **\+ Add step** and select **Action in app**.
   
   ![Click Add step > Action in app](/assets/add-step-standard.DEbq8cJp.png)_Click **Add step > Action in app**_
   
9. Set up your HubSpot Get associations action (batch).
   
   ### Set up HubSpot Get associations action (batch)
   
   This step retrieves the contact associated with the deal that triggered the recipe.
   
   1. Search for and select the HubSpot connector.
      
      ![Choose HubSpot](/assets/choose.BfILEyWG.png)_Choose HubSpot_
      
   2. Select the **Get associations** batch action.
      
      ![Select the Get associations batch action](/assets/get-associations.De3pw5qZ.png)_Select the Get associations batch action_
      
   3. Select **Deal** from the **From object** drop-down menu.
      
   4. Select **Contact** from the **To object** drop-down menu.
      
   5. Map the HubSpot ID (Step 1) datapill to the **From object ID** field.
      
      ![Configure the Get associations action](/assets/associations-config.ouJW3o5s.png)_Configure the Get associations action_
      
   
10. Click **\+ Add step** and select **IF condition**.
    
    ![Click Add step > IF condition](/assets/if-condition-standard.DI59XkdU.png)_Click **Add step > IF condition**_
    
    How do IF conditions work?
    
    ### HubSpot and Salesforce IF condition example
    
    An [IF condition](/en/features/if-conditions) lets you to make decisions based on specific conditions. You can control your recipe workflow by executing different actions depending on whether a condition you specify is true or false.
    
    ```mermaid
    flowchart TD
        A([Get associations action]) --> B(Is the HubSpot deal associated with a contact?)
        B -->|Yes| C(Get HubSpot contact information and create Salesforce lead)
        B ---->|No| E(No action is required)

        classDef default fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
    ```
    
11. Set up your HubSpot IF condition.
    
    ### Set up a HubSpot IF condition
    
    This step checks if a contact is associated with the new HubSpot deal.
    
    1. Map the HubSpot List size (Step 2) datapill (under the **Results** list) to **Data field**.
       
    2. Select **greater than** from the **Condition** drop-down menu.
       
    3. Enter `0` in the **Value** field.
       
       ![Configure the IF condition](/assets/if-condition-config.DLfLMSrO.png)_Configure the IF condition_
       
    
12. Click **Select an app and action**.
    
13. Set up your HubSpot Get record (contact) action.
    
    ### Set up HubSpot Get record (contact) action
    
    This step retrieves information about the contact associated with the deal from HubSpot.
    
    1. Search for and select the HubSpot connector.
       
       ![Choose HubSpot](/assets/choose.BfILEyWG.png)_Choose HubSpot_
       
    2. Select the **Get record** action.
       
       ![Select the Get record action](/assets/get-record.HGGMelNO.png)_Select the Get record action_
       
    3. Select **Contact** from the **Object** drop-down menu.
       
    4. Map the HubSpot To object ID (Step 2) datapill to the **ID** field. This instructs the recipe to retrieve information about the contact associated with the new deal.
       
    5. Specify the fields you plan to retrieve in the **Fields to retrieve** field. This example selects the following fields:
       
       - **Company Name**
       - **Last Name**
       - **Annual Revenue**
       - **City**
       - **Country/Region**
       - **Email**
       - **First Name**
       - **Phone Number**
       - **State/Province**
       - **Job Title**
       
       You can select additional fields as required by your use case, or that you plan to sync when creating the lead in Salesforce.
       
       ![Configure the Get contact action](/assets/get-contact-config.BlDaInIe.png)_Configure the Get contact action_
       
    
14. Click **\+ Add step** and select **Action in app**.
    
    ![Click Add step > Action in app](/assets/add-action-step.CaFDaYX8.gif)_Click **Add step > Action in app**_
    
15. Set up your Salesforce Create record (lead) action.
    
    ### Set up Salesforce Create record (lead) action
    
    This step creates the lead in Salesforce using information about the contact from HubSpot.
    
    1. Search for and select the Salesforce connector.
       
       ![Choose Salesforce](/assets/choose.K4EwwvB5.png)_Choose Salesforce_
       
    2. Select the **Create record** action.
       
       ![Select the Create record action](/assets/create-record.CQ90OufQ.png)_Select the Create record action_
       
    3. Select **Lead** from the **Object** drop-down menu.
       
    4. Map datapills from the HubSpot **Get contact** action to the fields you plan to sync to the Salesforce lead. The **Company** and **Last Name** fields are required.
       
       For example, this recipe maps the following HubSpot datapills to their respective Salesforce fields:
       
       - Company Name (Step 4) to the **Company** field.
       - Last Name (Step 4) to the **Last Name** field.
       - Annual Revenue (Step 4) to the **Annual Revenue** field.
       - City (Step 4) to the **City** field.
       - Country/Region (Step 4) to the **Country** field.
       - Email (Step 4) to the **Email** field.
       - First Name (Step 4) to the **First Name** field.
       - Phone Number (Step 4) to the **Phone** field.
       - Company Name (Step 4) to the **Company** field.
       - State/Region (Step 4) to the **State/Province** field.
       - Job Title (Step 4) to the **Title** field.
    
16. Click **\+ Add step** and select **Action in app**.
    
17. Set up your Salesforce Get record details by ID action.
    
    ### Set up Salesforce Get record details by ID action
    
    This step retrieves details about the new lead created in Salesforce.
    
    1. Search for and select the Salesforce connector.
       
       ![Choose Salesforce](/assets/choose.K4EwwvB5.png)_Choose Salesforce_
       
    2. Select the **Get record details by ID** action.
       
       ![Select the Get record details by ID action](/assets/get-record-by-id.Dt_RJF3w.png)_Select the Get record details by ID action_
       
    3. Select **Lead** from the **Object** drop-down menu.
       
    4. Map the Salesforce Object ID (Step 5) datapill to the **Object ID** field.
       
       ![Configure the Get lead details by ID action](/assets/get-lead-config.nkBMOfy9.png)_Configure the Get lead details by ID action_
       
    
18. Click **\+ Add step** and select **Action in app**.
    
19. Set up your Workbot for Microsoft Teams Post message action.
    
    ### Set up Workbot for Microsoft Teams Post message action
    
    This step posts a message in Microsoft Teams containing details about the new Salesforce lead.
    
    1. Search for and select the Workbot for Microsoft Teams connector.
       
       ![Choose Workbot for Microsoft Teams](/assets/choose.IJoiDJ15.png)_Choose Workbot for Microsoft Teams_
       
    2. Select the **Post message** action.
       
       ![Select the Post message action](/assets/post-message.P_T1ZDEl.png)_Select the Post message action_
       
    3. Select the channel where you plan to send the message from the **Message recipient** drop-down menu.
       
    4. Locate the **Message** field and click **Add block**.
       
    5. Fill out the following fields in the first block:
       
       - **Type**: Select **Text block**.
       - **Block text**: Enter `🔔 New Salesforce Lead Created!`.
       - **Text type**: Select **Header**.
    6. Click **Add block**.
       
    7. Fill out the following fields in the second block:
       
       - **Type**: Select **Text block**.
       - **Block text**: Enter `📌 Lead Name:` and map the Salesforce Full Name (Step 6) datapill.
       - **Text type**: Select **Body text**.
    8. Click **Add block**.
       
    9. Fill out the following fields in the third block:
       
       - **Type**: Select **Text block**.
       - **Block text**: Enter `🏢 Company:` and map the Salesforce Company (Step 6) datapill.
       - **Text type**: Select **Body text**.
    10. Click **Add block**.
        
    11. Fill out the following fields in the fourth block:
        
        - **Type**: Select **Text block**.
        - **Block text**: Switch this field to [formula mode](/en/formulas/formula-mode), enter `'📞 Phone: ' +`, map the Salesforce Phone (Step 6) datapill, and append the `.to_phone(area_code: true)` formula.
        - **Text type**: Select **Body text**.
        
        ![Configure the phone block](/assets/phone-config.C8tluPzx.png)_Configure the phone block_
        
    12. Click **Add block**.
        
    13. Fill out the following fields in the fifth block:
        
        - **Type**: Select **Text block**.
        - **Block text**: Enter `✉️ Email:` and map the Salesforce Email (Step 6) datapill.
        - **Text type**: Select **Body text**.
    14. Click **Add block**.
        
    15. Fill out the following fields in the sixth block:
        
        - **Type**: Select **Text block**.
        - **Block text**: Switch this field to [formula mode](/en/formulas/formula-mode), enter `'💰 Deal Amount: ' +`, map the HubSpot Amount (Step 1) datapill, and append the `.to_i.to_currency` formula.
        - **Text type**: Select **Body text**.
        
        ![Configure the deal amount block](/assets/deal-amount-config.B6kdtpyu.png)_Configure the deal amount block_
        
    16. Click **Add block**.
        
    17. Fill out the following fields in the seventh block:
        
        - **Type**: Select **Text block**.
        - **Block text**: Switch this field to [formula mode](/en/formulas/formula-mode), enter `'📆 Close Date: ' +`, map the HubSpot Close Date (Step 1) datapill, and append the `.strftime("%m/%d/%Y")` formula.
        - **Text type**: Select **Body text**.
        
        ![Configure the close date block](/assets/close-date-config.BW0l_dYP.png)_Configure the close date block_
        
    18. Click **Add block**.
        
    19. Fill out the following fields in the eighth and final block:
        
        - **Type**: Select **Text block**.
        - **Block text**: Enter `🎯 Lead Source: HubSpot`.
        - **Text type**: Select **Body text**.
    
    ![Example message containing Salesforce lead details](/assets/teams-message.DvcKWFEr.png)_Example message containing Salesforce lead details_
    
20. Click **Save**.
    

Your **Create Salesforce leads from new HubSpot deal** recipe is ready to test and implement.

Example recipe configuration.

![Create Salesforce leads from new HubSpot deal recipe](/assets/recipe.CO182W0L.png)_Create Salesforce leads from new HubSpot deal recipe_
