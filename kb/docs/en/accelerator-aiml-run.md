---
url: 'https://docs.workato.com/en/accelerator-aiml-run.md'
description: >-
  Use the AIML accelerator to train a machine learning model and get predictions
  for intelligent automation in Workato.
---

# How to use this accelerator

## Train ML model

Follow these steps to train an ML (machine learning) model.

1. In Workato, create a new recipe.
   
2. Choose a trigger according to your use case.
   
3. Add an action and app. Select **AIML Accelerator** as the application and **Train AIML Model** as the action.
   
4. Select a **Model Identifier** as defined in the **AIML | Data Fields** lookup table.
   
5. Configure an **if condition** to check for the **is\_success** flag. The **is\_success** flag returns **true** if the preceding action was successful and **false** if it was unsuccessful.
   
6. Add the actions for success or failure accordingly. For example, if **is\_success** returns as **false**, you may decide to send a Slack message or email notification.
   
7. Click **Save**.
   
8. Click **Test** to run the recipe.
   

## Stage training data

1. In Workato, create a new recipe.
   
2. Choose a trigger according to your use case.
   
3. Add an action and app. Select **AIML Accelerator** as the application and **Train AIML Model** as the action.
   
4. Select a **Model Identifier** as defined in the **AIML | Data Fields** lookup table.
   
5. Configure an **if condition** to check for the **is\_success** flag. The **is\_success** flag returns **true** if the preceding action was successful and **false** if it was unsuccessful.
   
6. Add the actions for success or failure accordingly. For example, if **is\_success** returns as **false**, you may decide to send a Slack message or email notification.
   
7. Click **Save**.
   
8. Click **Test** to run the recipe.
   

## Get a prediction

Follow these steps to get a prediction.

1. In Workato, create a recipe.
   
2. Add an action and an app. Select **AIML Accelerator** as the application and **Train AIML Model** as the action.
   
3. Select the **Model Identifier** as defined in the **AIML | Data Fields** lookup table.
   
4. Load the values from the fields in the **AIML|Data Fields** lookup table into the input fields. Ensure the values match the corresponding **Model Identifier**. If fields are missing, check the **AIML | Data Fields** lookup table.
   
5. Configure an **if condition** to check for the **is\_success** flag. The **is\_success** flag returns **true** if the preceding action was successful and **false** if it was unsuccessful.
   
6. Add the actions for success or failure accordingly. For example, if **is\_success** returns as **false**, you may decide to send a Slack message or email notification.
   
7. Click **Save**.
   
8. Click **Test** to run the recipe.

---
