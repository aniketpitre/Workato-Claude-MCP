---
url: 'https://docs.workato.com/en/workbot/workbot-advanced-topics.md'
description: >-
  Learn how to design the Workbot for Slack conversational interface with
  buttons, menus, modals, and other Slack interactive components.
---

# Designing the Workbot interface

Workbot for Slack supports many of Slack's interactive components, including buttons, menus, and modals. Use them in your Workbot recipes to collect information from users, format Workbot messages, and trigger subsequent recipes. Combine these components with the appropriate triggers and actions to customize the Workbot conversational interface.

## Which interface feature do I use?

| Feature | Description | Use it with |
| --- | --- | --- |
| [App home](/en/workbot/workbot-actions#publish-app-home-view) | A 1:1 interactive space shared between you and Workbot, containing timely and customized content. For example, a list of time off requests that need your approval. | **New event** trigger with **Publish app home view** action |
| Attachment fields | Creates a two-column layout below the message text that dynamically displays information related to the message. For example, in a message announcing a new Salesforce account, Workbot can include that account's company name, annual revenue, and phone number. | **Post message** or **Post command reply** actions |
| [Block kit](/en/workbot/block-kit) | Slack's UI framework, with which you can add UI elements such as buttons, images, and menus to Workbot messages. | **Post message**, **Post command reply**, **Open/update or push**, or **Publish app home view** actions |
| [Buttons](/en/workbot/workbot-buttons) | Triggers another command based on the button you click. For example, when a user reports an issue to Workbot, it can prompt them to select a button to specify the type, such as HR or IT. | **Post command reply** or a **Post message** action |
| [Dynamic menu](/en/workbot/workbot-dynamic-menus) | A drop-down menu in a modal or dialog that generates menu options as the user types. This is recommended when you expect a large number of menu options, such as companies in Salesforce. | **New dynamic menu event** trigger |
| Messages | The standard way to communicate with Workbot. Send and receive messages from Workbot via direct message or in a channel to which Workbot has been invited. | **Post command** trigger with **Post message** or **Post command reply** actions |
| [Message menus](/en/workbot/workbot-message-menus) | Triggers another command based on the item you select. For example, when a user reports an issue to Workbot, it can prompt them to select a menu item to clarify the priority (low, medium, or high). | **Post command reply** or a **Post message** action |
| [Modals](/en/workbot/modals) | Interactive pop-up windows that collect information from users. | **Open/update or push** action |
| [Slash commands](/en/workbot/configuring-slash-commands) | A phrase that you can enter in the Slack message box to trigger a recipe. For example `/createissue`. | [Enterprise Workbots](/en/workbot/workbot-custom-bots) that contain the **Post command** trigger |

---
