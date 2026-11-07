---
url: 'https://docs.workato.com/en/airo/usage-inspiration/automate-to-do-list.md'
description: >-
  Use AIRO to build a solution that turns meeting notes into Trello cards and a
  Slack summary.
---

# Automate your to-do list with AIRO

AIRO can turn meeting action items into a to-do list and a status update automatically, so nothing gets missed after the meeting ends. Describe what you want in a single sentence, and AIRO fills in the details you leave out to build the automation.

Video guide: The to-do list that writes itself

[Video](https://www.youtube.com/embed/yKAp4Ew521c)

> **STEPS MAY VARY**
> 
> AIRO can take a different path to achieve the same goal. The questions it asks and the steps it takes may differ from this example.

## Describe the problem

Start a new conversation with AIRO and describe the problem the way you'd describe it to a coworker:

`After a Google Calendar meeting ends, pull the action items out of the meeting notes in Google Drive, add each one to my Trello to-do list, and send me a rundown in Slack before the next meeting. The meeting notes are a Google Doc whose file name matches the calendar event's title.`

## Choose a project

AIRO asks where the automation should be stored. Create a new project or pick an existing project.

## Answer AIRO's questions, or start with defaults

AIRO reads your request, identifies the apps and trigger involved, and asks about anything it can't infer, such as where your notes are stored, which Trello board to use, and how early to send the rundown. Tell AIRO to start with defaults if you'd rather not answer every question yourself.

## Review the blueprint and connect your apps

AIRO shows you an outline of the automation before it builds anything, also known as a [blueprint](/en/airo/blueprints).

Confirm the blueprint, then connect the apps involved, in this example, Google Calendar, Google Drive, Trello, and Slack.

## Let AIRO write the steps

AIRO writes every step of the recipe itself, including pulling the notes from Drive, extracting each action item, creating the Trello cards, and setting up the Slack rundown. It adds a short comment to each step explaining what it does, so the recipe stays readable even when you didn't specify every detail yourself.

## Provide anything AIRO still needs

AIRO flags anything it can't fill in on its own, such as your Slack ID, and tells you where to find it. Enter the missing values in the recipe steps AIRO points you to.

## Save and start the recipe

Save the recipe, exit the recipe editor, and start it. The recipe waits for your next trigger event, in this example, the end of a calendar meeting, before it runs the rest on its own.

---
