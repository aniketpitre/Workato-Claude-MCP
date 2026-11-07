---
url: 'https://docs.workato.com/en/recipes/steps/steps-faqs.md'
description: >-
  Answers to common questions about recipe steps in Workato, including action
  steps, conditional steps, and repeat steps.
---

# Steps FAQs

Get answers to frequently asked steps questions.

What are recipe steps?

Recipes are workflows made up of steps. [Steps](/en/recipes/steps#steps) contain actions or control flow statements that help you describe automation logic.

What are action steps in a recipe?

[Action steps](/en/recipes/steps#action-step) perform operations in a target application, such as creating, updating, or searching for data. Action steps require input fields and return output data.

An example is searching for Zendesk organizations by Salesforce account name and updating a Zendesk organization using the ID from the search action.

How can I use conditional action steps in a recipe?

[Conditional action steps](/en/recipes/steps#example-conditional-action-step) help decide whether to perform certain actions based on conditions. Conditions are useful for making decisions within recipes. For example, the IF condition step allows recipes to run specific actions based on whether a defined condition exists or not.

When should I use the repeat step in a recipe?

Use the [repeat step](/en/recipes/steps#repeat-step) when you plan to perform a set of actions for every item in a list, like invoice line items. The repeat step is beneficial for iterating through lists.

For example, you can sync Salesforce accounts to Zendesk as organizations, where each Salesforce account is processed one at a time.

How is the repeat in batches action step used in recipes?

The [repeat in batches action step](/en/recipes/steps#repeat-step) is used when data transmission from an upstream app processes too fast for the downstream app to receive it. The repeat in batches action step processes data in smaller batches for the downstream app to consume.

You configure this step by selecting the repeat action step, entering the input list, and then setting the batch size to handle large data sets in smaller batches.

When should I use the stop step action step in a recipe?

The [stop step action](/en/recipes/steps#stop-step) is used to end a job before completion, especially when there is a logic error. You can configure stop step to mark the job as successful or failed.

For example, when you expect Salesforce accounts to be present in Zendesk as organizations, and no corresponding organization is found, the recipe does not continue to the next step.

What is the handle errors step?

The [handle errors step](/en/recipes/steps#handle-errors-step) is used to monitor and manage errors in actions. This gives you the ability to retry actions or take remedial actions in case of errors.

For example, you can set up actions within the Monitor block to be auto-retried up to three times with specified time intervals between retries.

You can also use the handle errors step with auto-retry in cases where an action fails temporarily due to network issues. The recipe attempts to execute the steps again for a maximum of three tries.

Can I copy and paste recipe steps?

Yes. Click anywhere in your recipe and then drag your cursor over the steps you plan to [copy](/en/troubleshooting/tips-and-tricks/copy-paste#copy-paste-steps). This creates a blue box around the selected steps. On Mac, press command+c to copy the steps, and press command+v to paste the steps. On Windows, press ctrl+c to copy the steps, and press ctrl+v to paste the steps.

Why do some of my steps turn red when I copy and paste?

[Steps turn red](/en/troubleshooting/tips-and-tricks/copy-paste#remap-datapills-and-auto-suggestion) after pasting when mapping dependencies break. Follow the onscreen suggestions to remap the dependencies.

---
