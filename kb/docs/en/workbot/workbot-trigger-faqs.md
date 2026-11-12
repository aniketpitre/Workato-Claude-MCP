---
url: 'https://docs.workato.com/en/workbot/workbot-trigger-faqs.md'
description: >-
  Answers to common questions about Workbot for Slack triggers, including how
  commands are processed and which triggers are available.
---

# Workbot trigger FAQs

Get answers to frequently asked questions (FAQs) about Workbot triggers.

## How are Workbot commands processed, and what role does a Workato recipe play?

View answer

Each [Workbot command](/en/workbot/workbot-triggers#workbot-triggers-for-slack) is processed using a Workato recipe. The recipe's trigger picks up the Workbot command as an event, and the recipe determines the actions to be carried out in response to the command. This allows you to create custom workflows executed through Slack commands.

## What are the available triggers in the Workbot for Slack connector?

View answer

The Workbot for Slack connector provides five [triggers](/en/workbot/workbot-triggers#workbot-triggers-for-slack):

- New command
- New help message
- New event (real-time)
- New shortcut trigger
- New URL mention

These triggers enable various interactions and automated workflows within Slack.

## How does the New command trigger work, and what input fields can be configured for it?

View answer

The [New command](/en/workbot/workbot-triggers#new-command-trigger-building-custom-commands) trigger is used to configure custom Workbot commands. It monitors Slack for the specified command and executes recipe actions when the command is called. You can configure input fields, such as:

- App
- Action
- Action data
- Command input fields
- Command hint

## What is the format for creating a Workbot command, and how are input parameters defined?

View answer

Workbot commands are created by [combining three elements](/en/workbot/workbot-triggers#workbot-command-format):

- App
- Action
- Action data

[Input parameters](/en/workbot/workbot-triggers#workbot-command-input-parameters-format) for commands are defined using a specific format that includes fields, such as:

- Name
- Prompt
- Data type
- Hint
- Example

## What output datapills are available from the New command trigger, and what information do they provide?

View answer

The **New command** trigger generates [output datapills](/en/workbot/workbot-triggers#new-command-trigger-output-datapills), including information about the command, such as:

- App
- Action data
- Action
- Message ID
- Context

The output datapills created for the **New command** can be used in subsequent recipe actions.

## How can I customize the help message for Workbot in Slack using the New help message trigger?

View answer

The **New help message** trigger allows you to fully [customize Workbot's help message](/en/workbot/workbot-triggers#reasons-to-use-new-help-message-trigger) response when users request help. You can:

- Personalize messages
- Display different help messages based on user roles
- Provide alternative help messages

## What events can be subscribed to using the New event trigger, and can it work with Slack's Events API?

View answer

The [New event trigger](/en/workbot/workbot-triggers#new-event-trigger) executes when a specified event occurs in a Slack workspace. Users can subscribe to various events and configure how the trigger responds to a specific event. This trigger works with Slack's Events API and allows for event customization.

## How does the New shortcut trigger work, and what are its applications?

View answer

The [New shortcut trigger](/en/workbot/workbot-shortcuts#new-shortcut-trigger-real-time) lets you launch workflows from global shortcuts or convert Slack messages into tasks or tickets using message shortcuts. It collects input fields from users and then creates tasks or tickets based on the user input.

## What is the purpose of the New URL mention trigger, and which types of URLs are supported?

View answer

The [New URL mention trigger](/en/workbot/workbot-triggers#new-url-mention) monitors certain types of URLs in Slack and retrieves pre-defined, formatted data when those URLs are mentioned. Currently, this trigger supports Salesforce and GitHub URLs and can be used to display additional information based on the mentioned URL.

## How does the New dynamic menu event trigger work, and what are its applications?

View answer

The [New dynamic menu event trigger](/en/workbot/workbot-triggers#new-dynamic-menu-event) is used in Workbot command recipes with dynamic menu options. This trigger executes when a user enters information into a dynamic menu field, and then returns the user's input. This trigger is often used to refine search results or perform actions based on user input.

---
