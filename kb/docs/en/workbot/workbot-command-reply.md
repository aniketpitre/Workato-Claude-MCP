---
url: 'https://docs.workato.com/en/workbot/workbot-command-reply.md'
description: >-
  Configure the Workbot Post command reply action to respond to Slack users with
  queried data, confirmations, and message attachments.
---

# Creating a Command Reply

Use either the **Post command reply** or **Post message** action to respond to the user on Slack. You can configure Workbot to return data that was queried by the command or to respond to the user with a message confirming whether the command was successful or not. See the graphic below for an example use case.

![Workbot Command trigger and the Command response diagram](/assets/anatomy-of-a-command-reply-1.B8gNyG8U.gif)_Example of a Command reply_

This page guides you through the second part of building your first Workbot - [create an issue in Github](https://www.workato.com/recipes/663926-create-an-issue-on-github-from-slack-using-workbot#recipe). If you have not already done so, follow the steps in [configure the New command trigger](/en/workbot/workbot-commands#step-1-configure-the-new-command-trigger).

## Step two: Configure the Post command reply action

In the following steps, you configure the **Post command reply** action with datapills from the GitHub action output.

1. Under the Github action, click to add a new action. Select **Workbot for Slack** > **Post command reply**.
2. Select the connection that you have established.
3. In the **Message text** field, enter the message that Workbot will use in its reply: Issue `Number` created  
   Use the Number (Step 2)
4. Expand the **Message attachment** options and configure these fields with the following text and datapills:
   - **Title**: _Name of issue_ Title (Step 2)
   - **Title link**: URL (Step 2)
   - **Attachment text**: _Description_ Body (Step 2)  
     _Assignee_ Username
   - **Attachment color**: Select **Good**  
     This sets the vertical bar to the left of the message to green.
5. Click **Save**.

This is how the **Message attachment** fields should look: ![Message attachment with expanded fields](/assets/message-format-expanded-with-fields-1.BYSH1VMg.png)

This is how the message will appear to users in Slack: ![Command reply explained](/assets/command-reply-explained-1.Dgj94i0V.png)

## Test the command

To test the command, start the recipe and open the Slack workspace in which Workbot is installed.

1. In Slack, send a direct message to Workbot, and enter `github create issue`.  
   Workbot responds with `Enter issue:` as demonstrated in the screenshot below: ![Github create issue](/assets/github-create-issue-1.B8np6GDs.png)
2. Enter the issue title.  
   Workbot responds with `Enter description` as demonstrated in the screenshot below: ![Github enter description](/assets/github-enter-description-1.OekukpPl.png)
3. Enter the description of the issue.  
   Workbot responds with `Enter assignee:`![Github enter assignee](/assets/github-enter-assignee-1.BtOfNNmy.png)
4. Enter your name.  
   Workbot takes the information you provided, creates a new issue in Github, and returns a confirmation message. See the screenshot below for an example confirmation message: ![Github command reply](/assets/github-command-reply-1.BHb959OQ.png)

## Next

You can make the command reply more interactive by including [attachment fields](/en/connectors/slack#example-message-with-attachment), [images](/en/connectors/slack#example-message-with-attachment), [buttons](/en/connectors/slack#using-slack-message-buttons), and message menus. To learn more, see [Designing the Workbot experience](/en/workbot/workbot-advanced-topics).

Explore other ways Workbot has automated tasks for our community of users in [Community Recipes](https://www.workato.com/browse/recipes?q=workbot).

---
