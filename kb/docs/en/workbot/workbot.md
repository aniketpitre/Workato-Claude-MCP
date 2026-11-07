---
url: 'https://docs.workato.com/en/workbot/workbot.md'
description: >-
  Workbot for Slack is a Workato chatbot that lets your team monitor business
  apps, post notifications, and update data from within Slack.
---

# Workbot for Slack

[Video](https://www.youtube.com/embed/iP_1ZcTUtVs)

[Workbot for Slack](https://www.workato.com/platform/workbot?utm_source=docs&utm_medium=referral&utm_campaign=workbot) is a Workato chatbot that helps you monitor and interact with your business apps from within Slack.

Your team can configure Workbot to post notifications to Slack channels when important events happen, such as when a key customer files a ticket, a lead from a Fortune 500 company fills in a form on your website, or when a DevOps alert is created.

You can also retrieve information from your apps and post it to Slack, or create and update business data from within Slack. To cut down on notifications volume, apps can now send you smart notifications based on user-specified filters.

![Workbot1](/assets/workbot-1.DMuQsK1C.png)

By default, Workbot comes with a set of pre-built recipes that allows you to interact with your applications and enable notifications with minimal setup.

Workbot for Slack isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## Slack connector VS Workbot for Slack connector

Workato offers both the Slack connector and the Workbot for Slack connector.

The Workbot for Slack connector provides you with the tools to build bot interaction experiences. Workbot is comprised of a user interface and a series of recipes, through which users send and retrieve data from other apps. Users interact with Workbot in Slack channels and direct messages.

The Slack connector is a workspace automation tool. You can build recipes that authorize your Slack team as a team member, post messages to channels, send direct messages to Slack team members, and manage channels and groups. Recipes built on the Slack connector allow you to respond to message buttons and menus.

A detailed comparison table for both the Slack connector and the Workbot for Slack connector is below.

| Features | Slack Connector | Workbot for Slack Connector |
| --- | --- | --- |
| [Attachments](https://api.slack.com/docs/message-attachments) | [Yes](/en/connectors/slack.html#example-message-with-attachment) | [Yes](/en/workbot/workbot-actions.html#post-command-reply) |
| [Message buttons](https://api.slack.com/docs/message-buttons) | [Yes](/en/connectors/slack.html#using-slack-message-buttons) | Yes |
| [Message menus](https://api.slack.com/docs/message-menus) | Yes | Yes |
| [Threads](https://api.slack.com/docs/message-threading) | [Yes](/en/connectors/slack.html#using-slack-threads) | Yes |
| Need to install into Slack team? | Yes | Yes |
| Post as user customization | No, always post as authenticated user. | No, always post as Workbot. |
| Pre-built recipes/commands? | No | [Yes](https://www.workato.com/workbot-slack) |
| Notifications need to be set up? | No. Recipes that post Slack messages just have to be started, and notifications will start being posted to the specified channel. | No. Recipes that post Slack messages just have to be started, and notifications will start being posted to the specified channel. |
| Runtime user access? | [Yes](/en/features/runtime-user-connections.html) | [Yes](/en/features/runtime-user-connections.html) |
| Pass data (parameters) to subsequent messages/recipes | No | Yes |

## Notes

1. Make sure that Workbot is in the channel to run commands. Do this by inviting it to the channel.
2. Just like talking to a real person, use @workbot because you want it to be alerted.
3. When you send Workbot a direct message, you don't need to use @workbot because it knows you are talking to it.
4. When you invite Workbot into the channel, **anyone** in that channel can interact with Workbot via commands.
5. When first installing Workbot into your Slack team, Workbot will detect the **latest** app connections you have made in your Workato account and automatically connect to them.

---
