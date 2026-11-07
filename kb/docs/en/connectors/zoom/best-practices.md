---
url: 'https://docs.workato.com/en/connectors/zoom/best-practices.md'
description: >-
  Best practices for building recipes with the Zoom connector in Workato,
  including filtering trigger events and formatting webinar poll results.
---

# Zoom - Best Practices

We compiled a few of our best practices that make your life easier when developing workflows with Zoom on Workato.

## Filtering trigger events on Zoom

As the Zoom connector works on an organizational level, this means that jobs are created regardless of the user. To help filter only the events you want, make use of tracking fields in Zoom to define the purpose of your meetings or webinars. Tracking fields allow you to define the purpose of the meeting or webinar so you can label it as a sales call or a marketing webinar. Refer to the Zoom [tracking fields documentation](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) for more information.

When events are triggered in the Zoom connector, you can then use these tracking fields to filter events. Below, we have an example of 2 tracking fields we have set up for `Department` and purpose. These fields can be made required and help indicate the department and purpose of the meeting.

![Tracking fields in Zoom](/assets/tracking-field-set-up.DRiWKgdW.png)_Set up tracking fields in your Zoom instance_

When users have to schedule a Zoom meeting, they'll have additional fields to help label these meetings. These tracking fields can be assigned to meetings or webinars through the Zoom web UI or through the API.

![Tracking fields when scheduling a meeting](/assets/tracking-field-schedule.CfwoUrnq.png)_Set up tracking fields for each meeting_

As events are triggered in Zoom, recipes can be set up that listen on these triggers. In the example below, we have a recipe listening on new webinars starting in Zoom. By checking on the tracking fields assigned to that webinar, we can find out if the webinar is marketing related rather than an internal all-hands meeting. In this case, we would stop the job if the `Purpose` of the webinar was anything other than `Marketing`.

![Check tracking field on Workato](/assets/check-tracking-field.CP6zsMtt.png)_Use conditional statements in Workato to check if the tracking field for an event is correct._

## Making sense of Webinar results easily

Zoom Webinars have fantastic ways to make collecting data from attendees easy. They allow you to launch polls and also have Q&A sessions with your attendees. One critical part of this is massaging the webinar result data from Zoom into a templated format which is easy to read. This goes a long way when sending this data to Salesforce as sales reps will be able to read a specific registrants poll results more easily.

The first step is to create a message template in Workato. Message templates are a structured way to transform lists of data into another format of your design. In the example below, we have this new template called `Webinar poll`, which accepts an array of Questions and answers.

![Message template](/assets/message-template.DZUOHYP6.png)_Message templates for Webinar poll_

In the template input section, we have the following schema which can be copied and pasted:

```
[
  {
    "name": "Array",
    "type": "array",
    "optional": false,
    "properties": [
      {
        "name": "Question",
        "type": "string",
        "optional": false,
        "control_type": "text"
      },
      {
        "name": "Answer",
        "type": "string",
        "optional": false,
        "control_type": "text"
      }
    ]
  }
]
```

In the template body section, we have the following texts:

```
Webinar poll answers:
{{#Array}}
Question: {{Question}}
Answer: {{Answer}}
{{/Array}}
```

Back in any recipe where we are retrieving poll results from a Webinar, we can then use this message template `Webinar poll` which we have just created to create human readable notes.

![Recipe view](/assets/recipe-view.BuVvnneE.png)_Massage the data for poll results_

![action view](/assets/action-view.BRqeNRcF.png)_Use the message template we have just created_

After this message has been crafted using the `Webinar poll` message template and the poll results we retrieved, we have used it to create a note attached to this specific contact in Salesforce.

![Push note into Salesforce](/assets/salesforce-action-view.D68o0KFv.png)_Update contact with poll results_

![Note in Salesforce](/assets/note-view.Cj1clSvn.png)_Poll appears nicely formatted in Salesforce_

Refer to the [sample recipe](https://www.workato.com/recipes/1156429?st=add07c) for a working example.

---
