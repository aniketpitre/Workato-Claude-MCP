---
url: 'https://docs.workato.com/en/connectors/celonis.md'
description: >-
  The Celonis connector lets you automate process mining workflows by triggering
  recipes on new events and signals from the Celonis process automation engine.
---

# Celonis

Celonis helps companies around the world discover inefficiencies in their day to day business operations through process mining. Besides finding these inefficiencies, Celonis helps you take action in real time to resolve these bottlenecks through Workato.

## How to connect to Celonis on Workato

There is no authentication needed.

![Configured Celonis connection](/assets/connection.z7M860f5.png)

| Field | Description |
| --- | --- |
| Connection name | Give this connection a unique name that identifies which Celonis instance it is connected to. |

## New event trigger

This trigger picks up events sent to Workato from the Celonis process automation engine.

### Input

| Input field | Description |
| --- | --- |
| Event Name | Give your event a meaningful name. This should describe the event you have received from Celonis - Blocked purchase order event |
| Payload Schema | The expected attributes of the event being sent to Workato from Celonis. This should match the payload in defined in Celonis. |

### Output

The output fields match what you have defined in your payload schema exactly.

## How to set up your Celonis new event trigger

1. After identifying signals in Celonis, convert them into skills in Action engine.
   
2. After setting up a new skill, add a new action by clicking into actions and then `Add Action`.
   

![new action](/assets/action-engine.DnfKTles.png)

3. Create a new action if you have not already done so.

![Action engine](/assets/Add-action.SAbLuqxc.png)

4. This will bring you to Celonis's process automations where you can trigger automations on this signal. Here, you'll find the Workato connector which can trigger new recipes.
   
5. When prompted for the URL for the Workato connector, you will need to head over to Workato and retrieve the `Webhook URL` in your Celonis trigger.
   

![Workato trigger](/assets/workato-webhook.BvjBklD_.png)

6. Be sure to define the payload on the Celonis end to provide sufficient details for your Workato recipe to work. This should include details such as the specific purchase order number.
   
7. Publish your process automation and head back to your project in the action engine on Celonis. Go through the steps to add a new action again and select the custom action you have just created
   

![Celonis connector](/assets/automatic-action.CY69_o90.png)

8. To have this action trigger automatically for new signals picked up, select the `Execute for new Signals` checkbox. This will allow new signals to immediately trigger a Workato recipe.

---
