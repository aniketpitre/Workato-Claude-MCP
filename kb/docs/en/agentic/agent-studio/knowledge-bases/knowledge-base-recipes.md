---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/knowledge-bases/knowledge-base-recipes.md
description: >-
  Create a knowledge base recipe that syncs content from connected apps so your
  genie's knowledge base stays current with the latest data.
---

# Knowledge base recipes

Knowledge base recipes sync and update information from your connected applications to your knowledge base. The knowledge base recipe ensures that your genie's knowledge base has access to the latest data and stays aligned with your business requirements. Knowledge bases and knowledge base recipes can be assigned to multiple genies, including genies stored in different projects. Refer to [Create a genie manually](/en/agentic/agent-studio/create-a-genie) for complete steps on how to create a genie with a job description, AI model, chat interface, knowledge base, knowledge base recipe, and skills.

> **NEED AN EXAMPLE?**
> 
> Refer to the [Connect your knowledge base to Confluence](/en/getting-started/use-cases/agent-studio/knowledge-bases/knowledge-base-confluence-use-case) use case for a step-by-step example on how to create and connect your knowledge base to Confluence with a knowledge recipe.

## Getting started with Knowledge base recipes

Complete the following steps to create a knowledge recipe:

1. Sign in to Workato.
   
2. Go to **AI Hub > Agent Studio**.
   
3. Select the genie where you plan to create a knowledge base recipe.
   
4. Go to the **Knowledge bases** section and select the knowledge base where you plan to add your knowledge recipe.
   
   ![Go to the Knowledge bases section](/assets/genie-build-page.DQ8_sDC8.png)_Go to the **Knowledge bases** section_
   
5. Click **\+ Add knowledge**.
   
6. Select **New knowledge recipe**.
   
7. Enter a name for your knowledge recipe in the **Recipe name** field.
   
8. Use the **Location** drop-down menu to select a location for your knowledge recipe.
   
   ![Set up your knowledge recipe](/assets/set-up-knowledge-recipe.DSLepKGW.png)_Set up your knowledge recipe_
   
9. Click **Add knowledge base**. The recipe editor opens with the [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents) action from [Knowledge base by Workato](/en/agentic/agent-studio/connectors/knowledge-base-connector/knowledge-base-connector) automatically selected.
   
   ![Knowledge recipe with the document upsert action automatically selected](/assets/knowledge-recipe.CqTvF1Cz.png)_Knowledge recipe with the document upsert action automatically selected_
   
   > **NEW RECIPES USE THE UPSERT DOCUMENTS ACTION**
   > 
   > New knowledge base recipes use the [Upsert documents](/en/agentic/agent-studio/connectors/knowledge-base-connector/actions/upsert-documents) action. Recipes created earlier use the deprecated [Store knowledge](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/store-knowledge) action, which continues to run unchanged.
   
10. Configure your recipe.
    
11. Test your recipe to ensure workflow compatibility with your genie.
    
12. Click **Save**.
