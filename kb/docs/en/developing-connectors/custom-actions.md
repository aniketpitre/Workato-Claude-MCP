---
url: 'https://docs.workato.com/en/developing-connectors/custom-actions.md'
description: >-
  Build new actions for a connector Workato already supports by defining the API
  request and response, reusing the existing auth framework.
---

# Custom actions

Want to build actions for a connector that Workato already supports? Custom actions enable you to use the existing connector framework to build new actions, instead of building something from scratch via the [HTTP universal connector](/en/developing-connectors/http-v2) or the [SDK](/en/developing-connectors/sdk). Custom actions allow you to easily build your action by telling Workato what the action's request and response should look like. This can be obtained from the API documentation.

Building a custom action is an accelerated way of building an action via the HTTP connector, as the custom action utilizes the connector's existing authorization framework and already understands the API for that app.

## App support for custom actions

Most apps on Workato support custom actions. Custom actions can be found in the actions picklist of the connector.

![Selecting the custom action](/assets/custom-action-selection.x4PwqZcV.png)_Selecting the custom action_

The custom action will list the scopes available. Typically, you can only read or write to objects that you have scopes for. For example, when we select custom action for the Slack connector, we see that only the following scopes are included:

```
channels:read, channels:write, chat:write:bot, chat:write:user, groups:read, groups:write,
users:read, users:read.email
```

![App scopes available for the custom action](/assets/app-scopes.Ds9B5xpU.png)_App scopes available for the custom action_

If you build an action that requires additional scopes, the action will throw an error when it tries to make the request with the API. For example, this error is returned when we try to build a create reminder action in Slack, as we have no `reminders:write` permission.

![Scope error returned by the API when call is made](/assets/custom-action-scope-error-output.BwNHq_Cw.png)_Scope error returned by the API when call is made_

If you'd like to see custom actions or additional scopes added to a connector on Workato, contact your Customer Success Representative to file an enhancement request.

## Custom action input fields

This section details the configuration input fields in the custom action.

| Input field | Description |
| --- | --- |
| Action name | Provide a name for the custom action. This name appears as the action title. |
| Request type | Specify the HTTP method of the API endpoint you plan to call. |
| Path | Provide the relative URI to append to the base URI. Don’t prefix with `/` unless you plan to override the default path. For example, Slack’s base URI is `https://slack.com/api/`. Entering `conversations.list` sends the request to `https://slack.com/api/conversations.list`, while `/conversations.list` sends it to `https://slack.com/conversations.list`. Add the `/` prefix when working with a different base path, such as an older API version. |
| URL params (For `GET` and `DELETE`) | Provide the URL parameters if the API request uses `GET` or `DELETE`. These are URL-encoded before sending. |
| Input (For `POST`, `PUT`, and `PATCH`) | Provide the JSON request body if the API request uses `POST`, `PUT`, or `PATCH`. |
| Output | Describe to Workato the output schema you expect the API to return. This will be used to generate the output datatree. |

## Custom action example - building Slack list conversations action

This example demonstrates how to build a custom Slack action that lists conversations, which are channel-like objects, such as public channels, private channels, and direct messages. You can refer to the [Slack API documentation](https://api.slack.com/methods/conversations.list) for more information.

1. Select **Custom action** as your Slack action.
   
   ![Select the Slack custom action](/assets/custom-action-selection.x4PwqZcV.png)_Select the Slack custom action_
   
2. Enter a name for your action in the **Action name** field, such as `List conversations`. This changes the action title in the recipe editor.
   
   ![Naming your custom action](/assets/name-custom-action.BZ0cQHHW.gif)_Naming your custom action_
   
3. Select the HTTP method for the request based on the API endpoint you're calling. The Slack `list.conversations` endpoint uses a `GET` method.
   
   ![Slack's API documentation for list conversations](/assets/slack-list-channels-http-method-docs.DBPT5sAy.png)_Slack's API documentation for list conversations_
   
4. After you select the relevant HTTP method, the relevant input fields appear.
   
   ![Additional fields show up when you select HTTP method](/assets/select-http-method.BmL4u35K.gif)_Additional fields show up when you select HTTP method_
   
5. Enter `conversations.list` or `https://slack.com/api/conversations.list` in the **Path** field.
   
   ![Adding URL endpoint for list conversations](/assets/add-url-endpoint.BdVzO9s0.png)_Adding URL endpoint for list conversations_
   
6. Add URL parameters to your request in the **Request URL parameters** field. There are no required arguments for this API endpoint except for the authentication token, which Workato handles through your established Slack connection.
   
   ![Slack API documentation on arguments for list conversations endpoint](/assets/slack-docs-list-channel-arguments.BpoTM3Cm.png)_Slack API documentation on arguments for list conversations endpoint_
   
   To exclude archived conversations and limit the number of conversations returned, define the following parameters:
   
   - `exclude_archived`: Select **Boolean** as your **Data type**.
   - `limit`: Select **Integer** as your **Data type**.
   
   ![Adding URL params for the custom action](/assets/add-custom-action-params.wrMHS1vO.gif)_Adding URL params for the custom action_
   

After you define the parameters, provide the values for them. In this example, the values are hardcoded to `true` for **exclude\_archived** and `20` for **quota**, but you can replace these with datapills if you plan to pass variables.

![Filling in values for params](/assets/fill-in-param-values.YBZ8MxSR.gif)_Filling in values for params_

There's just one last thing to provide - the output schema. This can be typically copied from the API documentation and pasted into Workato. Here's the JSON response copied from the Slack API documentation.

```
{
    "ok": true,
    "channels": [
        {
            "id": "C012AB3CD",
            "name": "general",
            "is_channel": true,
            "is_group": false,
            "is_im": false,
            "created": 1449252889,
            "creator": "U012A3CDE",
            "is_archived": false,
            "is_general": true,
            "unlinked": 0,
            "name_normalized": "general",
            "is_shared": false,
            "is_ext_shared": false,
            "is_org_shared": false,
            "pending_shared": [],
            "is_pending_ext_shared": false,
            "is_member": true,
            "is_private": false,
            "is_mpim": false,
            "updated": 1678229664302,
            "topic": {
                "value": "Company-wide announcements and work-based matters",
                "creator": "",
                "last_set": 0
            },
            "purpose": {
                "value": "This channel is for team-wide communication and announcements. All team members are in this channel.",
                "creator": "",
                "last_set": 0
            },
            "previous_names": [],
            "num_members": 4
        },
        {
            "id": "C061EG9T2",
            "name": "random",
            "is_channel": true,
            "is_group": false,
            "is_im": false,
            "created": 1449252889,
            "creator": "U061F7AUR",
            "is_archived": false,
            "is_general": false,
            "unlinked": 0,
            "name_normalized": "random",
            "is_shared": false,
            "is_ext_shared": false,
            "is_org_shared": false,
            "pending_shared": [],
            "is_pending_ext_shared": false,
            "is_member": true,
            "is_private": false,
            "is_mpim": false,
            "updated": 1678229664302,
            "topic": {
                "value": "Non-work banter and water cooler conversation",
                "creator": "",
                "last_set": 0
            },
            "purpose": {
                "value": "A place for non-work-related flimflam, faffing, hodge-podge or jibber-jabber you'd prefer to keep out of more focused work-related channels.",
                "creator": "",
                "last_set": 0
            },
            "previous_names": [],
            "num_members": 4
        }
    ],
    "response_metadata": {
        "next_cursor": "dGVhbTpDMDYxRkE1UEI="
    }
}
```

We can copy this and paste it in Workato to generate the output datatree.

![Generate output datatree in Workato with JSON response sample in API documentation](/assets/generate-output-schema.DJ7GPuBL.gif)_Generate output datatree in Workato with JSON response sample in API documentation_

This tells Workato what response schema to expect, and the datapills generated can be used in subsequent steps of the recipe to move data into other apps.

![Generated output datatree in Workato](/assets/generated-output-datatree.Bx1Z5AyF.gif)_Generated output datatree in Workato_

However, if the actual response does not contain the data you have specified in this response sample, the datapills will not have a value.

Your custom Slack action is ready for testing. Use the Scheduler by Workato **New recurring event** trigger and click **Test recipe**.

![Completed Slack custom action to list conversations](/assets/full-slack-custom-action.D00k83AK.gif)_Completed Slack custom action to list conversations_

After testing the recipe, you can see the input passed into the action in the detailed job history.

![Job history - input data](/assets/list-channels-action-input.DqsZQSRF.png)_Job history - input data_

You can also view the detailed output returned by the Slack API to check if the API call was successful. If the `Ok` field is `true`, the call was successful.

![Job history - output showing conversation data returned](/assets/list-channels-action-output._ZLVyY9a.png)_Job history - output showing conversation data returned_

---
