---
url: 'https://docs.workato.com/en/airo/usage-inspiration/form-to-slack-alert.md'
description: >-
  Use AIRO to build a solution that sends a Slack alert when someone submits a
  Google Form.
---

# Build a form-to-Slack alert with AIRO

AIRO can alert you the moment someone submits a form, so you don't have to rely on an email notification. Describe the problem in a conversation, and AIRO builds the alert without you opening the recipe editor.

Video guide: Build a form-to-Slack alert with AIRO

[Video](https://www.youtube.com/embed/vgHxvu7N7fg)

> **STEPS MAY VARY**
> 
> AIRO can take a different path to achieve the same goal. The questions it asks and the steps it takes may differ from this example.

## Describe the problem

Start a new conversation with AIRO and describe the problem the way you'd describe it to a coworker:

`People keep filling out my event signup form, and I keep missing it in my inbox.`

## Answer AIRO's questions

AIRO checks the two things it needs before building anything:

- **Which form**: for example, a Google Forms form you already use to collect responses.
- **Where to be notified**: for example, Slack, so you see a new response as soon as it comes in.

## Choose a project and connect your apps

AIRO asks whether the automation should be stored in an existing project or a new project. It also asks you to connect the apps involved, such as Slack and Google Sheets, before it starts building.

## Let AIRO build the alert

AIRO builds the automation that alerts you in Slack the moment someone submits the form, then tells you what's left to finish the connection. Link the form to a spreadsheet in Google Forms, and tell AIRO to connect to it.

## Let AIRO catch mistakes

AIRO tells you when it can't find a detail you gave it, such as the wrong spreadsheet name, instead of guessing or failing silently. For example, AIRO might say it can't find a sheet with the name you gave it, but found a similarly named one, and ask you to confirm before it continues.

## Finish the last details in chat

AIRO asks for anything it still needs, such as who to notify and what the notification message should say. It can draft an example message format for you to approve, so you finish the automation without leaving the conversation.

## Save and start the recipe

Save the recipe and start it. Form submissions now appear in Slack instead of an inbox notification you might miss.

This example builds a single recipe directly from a conversation, without going through the full blueprint planning flow. Refer to [Blueprints](/en/airo/blueprints) to plan larger, multi-step automation projects with AIRO first.

---
