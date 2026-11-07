---
url: 'https://docs.workato.com/en/workbot/workbot-troubleshooting.md'
description: >-
  Troubleshoot common Workbot for Slack errors, including recipe execution
  failures, offline bots, and untriggered custom bot recipes.
---

# Troubleshooting Workbot for Slack

Sometimes Workbot may raise errors or issues. Here are some common errors and issues that Workbot might tell you about, and how to handle them.

## Recipe execution error

Workbot is powered by Workato recipes to fetch your app data, such as retrieving Salesforce opportunities data, or to write data to your apps, such as creating a new account in Salesforce. When Workbot tries to execute your command but encounters an unexpected error, Workbot responds with the following message:

![workbot recipe execution](/assets/troubleshooting-workbot-1.CquTiOcY.png)_Workbot error message about recipe execution error_

Usually, there is also a short description included about the error. To fix this error, you will have to go to the recipe, look for the failed job, and [debug the error](/en/recipes/jobs#viewing-details-for-a-specific-job) that happened in the job.

## Workbot offline

At times, you may find that despite having an active recipe or connection, Workbot appears to be offline. This is usually temporary.

Occasionally, reconnecting your Workbot connection helps to get it back online. Reconnect just like how you would reconnect to Slack. Navigate to **Connections**, find the Workbot connection, disconnect, and connect again.

## Custom bot recipe not triggered

You may encounter an error where invoking the command of the custom bot doesn't trigger a recipe.

Follow these troubleshooting methods to resolve the issue:

1. Go to **Tools > Custom OAuth profile** and select the profile for your custom bot.
   
2. Copy the request URL that contains `/actions`. For example, `https://app.workato.com/slack_webhooks/actions?coak_id=9670`.
   
   ![Request URL](/assets/request-url.C-8GTvfo.png)_Request URL_
   
3. Ensure that the request URL in the **Interactive Components** section of your Slack API app matches the one in your Workato custom OAuth profile. Update the configurations to the same request URL if they don't match.

---
