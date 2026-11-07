---
url: 'https://docs.workato.com/en/developing-connectors/sdk/sdk-reference/actions.md'
description: >-
  Reference for the actions key in the Workato connector SDK, covering all keys
  used to define an action's input, output, and execution.
---

# SDK Reference - `actions`

This section enumerates all the possible keys to define an action.

> **Quick Overview**
> 
> The `actions` key can only be used in both recipes and the SDK **Test code** tab after you have created a successful connection. Actions receive data from earlier steps in a recipe via datapills, send a request to an endpoint and present the response as datapills.

## Structure

```ruby
    actions: {

      [Unique_action_name]: {
        title: String,

        subtitle: String,

        description: lambda do |input, picklist_label|
          String
        end,

        help: lambda do |input, picklist_label|
          Hash
        end,

        display_priority: Integer,

        batch: Boolean,

        bulk: Boolean,

        deprecated: Boolean,

        config_fields: Array

        input_fields: lambda do |object_definitions, connection, config_fields|
          Array
        end,

        execute: lambda do |connection, input, extended_input_schema, extended_output_schema, continue|
          Hash
        end,

        output_fields: lambda do |object_definitions, connection, config_fields|
          Array
        end,

        sample_output: lambda do |connection, input|
          Hash
        end,

        retry_on_response: Array,

        retry_on_request: Array,

        max_retries: Int,

        summarize_input: Array,

        summarize_output: Array
      },

      [Another_unique_action_name]: {
        ...
      }
    },
```

* * *

## `title`

| Attribute | Description |
| --- | --- |
| Key | `title` |
| Type | String |
| Required | Optional. Defaults to title built from labeled key. |
| Description | This allows you to define the title of your action, which might differ from the name of the key assigned to it - Key = `search_object_query`, title = `"Search object via query"` |
| Expected Output | `String` i.e. `"Search object via query"` |
| UI reference |  |

> **TIP**
> 
> In Workato, we generally advise the following structure "\[Verb\] \[Object\]" - "Create lead" or "Search object" rather than "Lead created".

* * *

## `subtitle`

| Attribute | Description |
| --- | --- |
| Key | `subtitle` |
| Type | String |
| Required | Optional. Defaults to subtitle inferred from connector name and action title. |
| Description | This allows you to define the subtitle of your action. |
| Expected Output | `String` i.e. `"Use complex queries to search objects in Percolate"` |
| UI reference |  |

> **TIP**
> 
> To make your subtitles meaningful, try to provide more information in here whilst keeping your titles concise. For example, your title could be "Create object" whereas your subtitle could be "Create objects like leads, customers, and accounts in Salesforce." When users search for a specific action, Workato also searches for matches in the subtitle.

* * *

## `description`

| Attribute | Description |
| --- | --- |
| Key | `description` |
| Type | lambda function |
| Required | Optional. Defaults to description inferred from connector name and action title. |
| Description | This allows you to define the description of your action when viewed in the recipe editor. This can be a static description or a dynamic one based on your needs. |
| Possible Arguments | `input` - Hash representing user given inputs defined in `input_fields` `picklist_label` - Only applicable for picklists where a user's answer consist of both a picklist label and value. This Hash represents the label for a user's given inputs for picklist fields. See below for use cases. |
| Expected Output | `String` i.e. `"Create a <span class='provider'>campaign</span> in <span class='provider'>Percolate</span>"` Add the `<span>` HTML tags to add weight to your description text. |
| UI reference |  |

Example - description:

For the `description` lambda function, you have access to two arguments to make your descriptions dynamic. This is useful when you want to change your description based on how a given user has configured the action. These changes can be incredibly useful for your users to ensure they know what this action is doing without having to click and view the action's configuration to understand what it does.

```ruby
    create_object: {
      description: lambda do |input, picklist_label|
        "Create a <span class='provider'>#{picklist_label['object'] || 'object'}</span> in " \
        "<span class='provider'>Percolate</span>"
      end,

      config_fields: [
        {
          name: 'object',
          control_type: 'select',
          pick_list: 'object_types',
          optional: false
        }
      ]

      # More keys to define the action
    }
```

In the preceding example, the action is a generic object action that allows the user to choose between multiple object types when configuring the recipe. You can change the description of the object the user selects by referencing the `picklist_label` argument.

* * *

## `help`

| Attribute | Description |
| --- | --- |
| Key | `help` |
| Type | lambda function |
| Required | Optional. No help is displayed otherwise. |
| Description | The help text that is meant to guide your users as to how to configure this action. You can also point them to documentation. |
| Possible Arguments | `input` - Hash representing user given inputs defined in `input_fields` `picklist_label` - Only applicable for picklists where a user's answer consist of both a picklist label and value. This Hash represents the label for a user's given inputs for picklist fields. See below for use cases. |
| Expected Output | `Hash` or `String` See below for examples. |
| UI reference |  |

Example - help:

The output of the `help` lambda function can either be a simple String or a Hash. Below we go through the two examples:

- String

```ruby
    help: lambda do |input, picklist_label|
      'Create an object in Percolate. First, select from a list of ' \
      'objects that we currently support. After selecting your object,' \
      ' dynamic input fields specific to your scope and object selected ' \
      'will be populated.' \
      ' Creating an approval denotes submitting a specified piece of content' \
      ' or campaign for a specific approval workflow.'
    end,
```

- Hash

```ruby
    help: lambda do |input, picklist_label|
      {
        body: "First, filter by the object you want then fill up the input fields " \
        "which appear based on the object you have selected. Amongst other things, " \
        "you’ll be able to search for contacts in your company and cloud recordings from the past. ",
        learn_more_url: "https://docs.workato.com/connectors/zoom/event-actions.html#search-event-details",
        learn_more_text: "Learn more"
      }
    end,
```

* * *

## `display_priority`

| Attribute | Description |
| --- | --- |
| Key | `display_priority` |
| Type | Integer |
| Required | Optional. Defaults to zero, otherwise to the alphabetical ordering of actions titles. |
| Description | This allows you to influence the ordering of the action in the recipe editor so that you can highlight top actions. The higher the integer, the higher the priority. If two actions have the same priority, they are ordered by their titles. |

* * *

## `batch`

| Attribute | Description |
| --- | --- |
| Key | `batch` |
| Type | Boolean |
| Required | Optional. |
| Description | This presents a "Batch" tag next to your action to indicate that this action works with multiple records. Normally used in batch triggers or batch create/update/upsert actions where users can pass a list of records. |
| UI reference |  |

* * *

## `bulk`

| Attribute | Description |
| --- | --- |
| Key | `bulk` |
| Type | Boolean |
| Required | Optional. |
| Description | This presents a "Bulk" tag next to your action to indicate that this action works with a large flat file of records. Normally used bulk create/update/upsert actions where users pass a CSV of records. |
| UI reference |  |

* * *

## `deprecated`

| Attribute | Description |
| --- | --- |
| Key | `deprecated` |
| Type | Boolean |
| Required | Optional. |
| Description | This presents a "deprecated" tag next to your action to indicate that this action has been deprecated. Recipes which used to use this action will continue to work but future recipes will not be able to search and select this action. |
| UI reference |  |

> **TIP**
> 
> Deprecation is a great way to move users to new actions when changes are not backwards compatible. This gives you more freedom to make your actions more usable or cater for upcoming API changes.

* * *

## `config_fields`

| Attribute | Description |
| --- | --- |
| Key | `config_fields` |
| Type | Array |
| Required | Optional. |
| Description | This key accepts an array of hashes which show up as input fields shown to a user. Config fields are shown to a user before input fields are rendered and can be used to alter what set of input fields are shown to an end user. This is often used in generic object actions where config fields prompt a user to select the object and input fields are rendered based on that selection. Refer to [Workato Schema](/en/developing-connectors/sdk/sdk-reference/schema) for more information on defining config fields. |
| Expected Output | Array of hashes. Each hash in this array corresponds to a separate config field. |
| UI reference |  |

> **TIP**
> 
> Config fields are powerful tools to introduce dynamic behavior to your actions. Use them to make your connector easier to use and discover new features. In the example gif above, you can see that the input "Event" actually causes more input fields to render. These input fields are rendered based on the selection of the value "Meeting".

* * *

## `input_fields`

| Attribute | Description |
| --- | --- |
| Key | `input_fields` |
| Type | lambda function |
| Required | True |
| Description | This lambda function allows you to define what input fields should be shown to a user configuring this action in the recipe editor. Output of this lambda function should be an array of hashes, where each hash in this array corresponds to a separate input field. Refer to [Workato Schema](/en/developing-connectors/sdk/sdk-reference/schema) for more information on defining input fields. |
| Possible Arguments | `object_definitions` - Allows you to reference an object definitions. Object definitions are stores of these arrays hashes which may be used to represent both input fields or output fields (datapills). These can be referenced by any action or trigger. `connection` - Hash representing user given inputs defined in `connection`. `config_fields` - Hash representing user given inputs defined in `config_fields`, if applicable. |
| Expected Output | Array of hashes. Each hash in this array corresponds to a separate input field. |
| UI reference |  |

* * *

## `execute`

| Attribute | Description |
| --- | --- |
| Key | `execute` |
| Type | lambda function |
| Required | True |
| Description | This lambda function allows you to define what this action does with the inputs that have been passed to it from an end user. These inputs may be static values or datapills from upstream actions or the trigger. These are then used to send a HTTP request to retrieve data that can be presented as datapills. Optionally, you can also use the execute lambda function to do any pre-processing of input data before sending it as a request and post-processing of response data before passing it out as datapills. |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `Connection` `input` - Hash representing user given inputs defined in `input_fields` `extended_input_schema` - See below for examples. `extended_output_schema` - See below for examples `continue` - Hash representing cursor from the previous invocation of execute. OPTIONAL and used for asynchronous actions. See below for examples. |
| Expected Output | Hash representing the data to be mapped to the output datapills of this action. |

Example - execute: - extended\_input\_schema and extended\_output\_schema

Extended input and output schema is any schema from `object_definitions` that is used in your action. This information is often useful when you dynamically generate schema and you want to use it to do data pre- or post-processing. These arguments do not include config\_fields.

For example, you may use extended\_input\_schema to know which inputs are datetimes and should be transformed to Epoch time which is accepted by the target API. In the same fashion, you may use extended\_output\_schema to take the response and transform Epoch variables into ISO8601 datetimes again.

```ruby
    create_object: {
      description: lambda do |input, picklist_label|
        "Create a <span class='provider'>#{picklist_label['object'] || 'object'}</span> in " \
        "<span class='provider'>Percolate</span>"
      end,

      config_fields: [
        {
          name: 'object',
          control_type: 'select',
          pick_list: 'object_types',
          optional: false
        }
      ],

      input_fields: lambda do |object_definitions, connection, config_fields|
        object = config_fields['object']
        object_definitions[object].ignored('id')
      end,

     execute: lambda do |connection, input, extended_input_schema, extended_output_schema|
       puts extended_input_schema
       # [
       #   {
       #     "type": "string",
       #     "name": "status",
       #     "control_type": "select",
       #     "label": "Status",
       #     "hint": "Status is required for creating Content",
       #     "pick_list": "post_statuses",
       #     "optional": false
       #   },
       #   ...
       # ]

       puts extended_output_schema
       # [
       #   {
       #     "type": "string",
       #     "name": "id",
       #     "control_type": "text",
       #     "label": "Content ID",
       #     "hint": "The Content ID, Example: <b>post:45565410</b>.",
       #     "optional": true
       #   },
       #   {
       #     "type": "string",
       #     "name": "status",
       #     "control_type": "select",
       #     "label": "Status",
       #     "hint": "Status is required for creating Content",
       #     "pick_list": "post_statuses",
       #     "optional": false
       #   },
       #   ...
       # ]
     end,

     output_fields: lambda do |object_definitions, connection, config_fields|
       object = config_fields['object']
       object_definitions[object]
      end,
    }
```

Example - execute: - continue

When working with asynchronous APIs to kickstart a long running job or process in a target application, often times you'll send a request and expect an ID that corresponds to that job or process. Your action would then want to constantly check back with the API to see if the job is completed before retrieving results or moving on to the next step in the recipe.

For example, when you send a request to Google BigQuery to start a query, Google BigQuery might send you back the job ID. Your task would be to now regularly check back with Google BigQuery to see if the query is completed before retrieving the rows.

Rather than having the user configure this logic in the recipe, you can now embed this entire logic into a single action with "multi-step" actions on your custom connector. To use "multi-step" actions, the `continue` argument is used in conjunction with a dedicated method called `reinvoke_after`. Below, we go through some examples of what the `continue` argument might be.

Refer to the [multistep actions guide](/en/developing-connectors/sdk/guides/building-actions/multistep-actions) for more information.

```ruby
    multistep_action_sample: {
      input_fields: lambda do |object_definitions, connection, config_fields|

      end,

     execute: lambda do |connection, input, e_i_s, e_o_s, continue|

      if !continue.present? #continue is nil on the first invocation of the execute
        puts continue
        # nil
        reinvoke_after(seconds: 100, continue: { current_step: 1 })
      elsif continue['current_step'] == 1 #first reinvocation
        puts continue
        # {
        #   "current_step": 1
        # }
        reinvoke_after(seconds: 100, continue: { current_step: continue['current_step'] + 1 })
      else
        puts continue
        # {
        #   "current_step": 2
        # }
      end

     end,

     output_fields: lambda do |object_definitions, connection, config_fields|

      end,
    }
```

* * *

## `before_suspend`

| Attribute | Description |
| --- | --- |
| Key | `before_suspend` |
| Type | lambda function |
| Required | False |
| Description | This lambda function is exclusive to [Wait for resume actions](/en/developing-connectors/sdk/guides/building-actions/wait-for-resume-actions). It is invoked after the `suspend` method is called in the `execute` lambda. It allows you to define an authenticated API request based on the `apply` to an external system to register a callback to resume the job. |
| Possible arguments | `resume_token`: This token is specific to a particular job and is generated by the Workato framework. When the external system intends to resume a job, it must include this token in its resume request to the Resume job API.; `expires_at`: Timestamp in PST representing the time the job expires and resumes with a timeout.; `continue`: The `continue` hash passed from the `suspend` method. This can contain important information including the ID of the process in the external system. |
| Expected output | N/A |

* * *

## `before_resume`

| Attribute | Description |
| --- | --- |
| Key | `before_resume` |
| Type | lambda function |
| Required | False |
| Description | This lambda function is exclusive to [Wait for resume actions](/en/developing-connectors/sdk/guides/building-actions/wait-for-resume-actions). It is invoked after the external system has dispatched the API request to resume the job. It enables you to control the state of the `continue` hash, which is transmitted back to the `execute` lambda when the job resumes. Additionally, it grants access to the data value in the API request. |
| Possible arguments | `data`: This represents the `data` value in the API request to resume the job.; `input`: The input that the recipe sends directly to the action.; `continue`: The `continue` hash passed from the `suspend` method. This can contain important information, including the ID of the process in the external system. |
| Expected output | N/A However, the lambda allows you to edit the value of the `continue` hash. |

Example- Edit the value of the continue hash

This example demonstrates how to edit the value of the `continue` hash.

If the `continue` method passed from the `suspend` method is:

```ruby
{
  "state": "suspended",
  "job_id": "abc_123"
}
```

and the `before_resume` lambda is:

```ruby
before_resume: lambda do |data, input, continue|
  if continue["state"] == "suspended"
    continue["state"] = "resumed"
    continue["payload"] = "important data"
  else
    { "result" => "Unexpected state" }
  end
end,
```

Then the `continue` argument passed to the `execute` lambda looks like this:

```ruby
{
  "state": "resumed",
  "job_id": "abc_123",
  "payload": "important data"
}
```

* * *

## `before_timeout_resume`

| Attribute | Description |
| --- | --- |
| Key | `before_timeout_resume` |
| Type | lambda function |
| Required | False |
| Description | This lambda function is exclusive to [Wait for resume actions](/en/developing-connectors/sdk/guides/building-actions/wait-for-resume-actions). It is invoked when the `expires_at` time has passed and Workato has not received an API request to resume the job. It allows you to manage the state of the `continue` hash which is passed back to the `execute` lambda when the job resumes. |
| Possible arguments | `input`: The input that the recipe sends directly to the action.; `continue`: The `continue` hash passed from the `suspend` method. This can contain important information, including the ID of the process in the external system. |
| Expected output | N/A However, the lambda allows you to edit the value of the `continue hash`. Refer to the `before_resume` example to learn more. |

* * *

## `output_fields`

| Attribute | Description |
| --- | --- |
| Key | `output_fields` |
| Type | lambda function |
| Required | True |
| Description | This lambda function allows you to define what output fields (datapills) should be shown to a user configuring this action in the recipe editor. The output of this lambda function should be an array of hashes, where each hash in this array corresponds to a separate output field (datapill). Refer to [Workato Schema](/en/developing-connectors/sdk/sdk-reference/schema) for more information on defining output fields. |
| Possible Arguments | `object_definitions` - Allows you to reference an object definitions. Object definitions are stores of these arrays which can represent either input and output fields. These can be referenced by any action or trigger. `connection` - Hash representing user given inputs defined in `connection`. `config_fields` - Hash representing user given inputs defined in `config_fields`, if applicable. |
| Expected Output | Array of hashes. Each hash in this array corresponds to a separate input field. |
| UI reference |  |

Example - output\_fields:

Output fields relate directly to the datapills that users see in the recipe editor. The definition of these output fields are mapped to the output of the `execute` lambda function which is a hash.

```ruby
    create_object: {
     execute: lambda do |connection, input, extended_input_schema, extended_output_schema|
       post("/object/create", input)
       # JSON response passed out of the execute: lambda function.
       #  {
       #    "id": 142414,
       #    "title": "Newly created object",
       #    "description": "This was created via an API"
       #  }
     end,

     output_fields: lambda do |object_definitions, connection, config_fields|
       [
         {
           name: "id",
           type: "integer"
         },
         {
           name: "title",
           type: "string"
         },
         {
           name: "description",
           type: "string"
         }
       ]
      end,
    }
```

* * *

## `sample_output`

| Attribute | Description |
| --- | --- |
| Key | `sample_output` |
| Type | lambda function |
| Required | False. |
| Description | This lambda function allows you to define a sample output that is displayed next to your output fields (datapills). |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `connection`. `input` - Hash representing user given inputs defined in `input_fields` |
| Expected Output | Hash. This hash should be a stubbed output of the `execute` lambda function. |
| UI reference |  |

* * *

## `retry_on_response`

| Attribute | Description |
| --- | --- |
| Key | `retry_on_response` |
| Type | Array |
| Required | False. |
| Description | **Used in conjunction with retry\_on\_request: and max\_retries:** Use this declaration to implement a retry mechanism for certain HTTP methods and responses. This guards against APIs which may sometime return errors due to server failure such as 500 Internal Server Error codes. When supplying this array, we will accept what error codes to retry on as well as entire string or regex expressions. In cases where no error code is defined, Workato will only search the message body for any given regex or plain string IF the error codes fall under a default list of codes: (429, 500, 502, 503, 504, 507). When supplying an entire string instead of regex, this will give only retry if the entire response matches exactly. If entire strings or regex match and error codes are defined, both the error codes and strings must match for retries to be triggered |
| Expected Output | Array. For example, `[500]` or `[500,/error/]` or `[‘“error”’, 500]` |

* * *

## `retry_on_request`

| Attribute | Description |
| --- | --- |
| Key | `retry_on_request` |
| Type | Array |
| Required | False. |
| Description | **Used in conjunction with retry\_on\_request: and max\_retries:** Use this declaration to implement a retry mechanism for certain HTTP methods and responses. This guards against APIs which may sometime return errors due to server failure such as 500 Internal Server Error codes. Optional. When not defined, it defaults to only “GET” and “HEAD” HTTP requests. |
| Expected Output | Array. For example, `[“GET”]` or `[“GET”, “HEAD”]` |

* * *

## `max_retries`

| Attribute | Description |
| --- | --- |
| Key | `max_retries` |
| Type | Int |
| Required | False. |
| Description | **Used in conjunction with retry\_on\_request: and max\_retries:** Use this declaration to implement a retry mechanism for certain HTTP methods and responses. This guards against APIs which may sometime return errors due to server failure such as 500 Internal Server Error codes. The number of retries. A maximum of 3 allowed. If more than 3, action retries 3 times. Workato waits 5 seconds for the first retry and increases the interval by 5 seconds for each subsequent retry. |
| Expected Output | Int. For example, `1` or `2` |

> **TIP**
> 
> - We recommend using only one HTTP method per action if possible
> - Multiple GET requests within a single action are also possible
> - Since we retry on an action level, actions should be defined to only at most only one POST request. This guards against cases where the first post request succeeds and the second post request fails.

Example - Implementing the retry mechanism

Retrying an API request is very useful in ensuring that your actions (and recipes) are tolerant to any inconsistencies in the target App. To implement this, you will need to use a combination of the retry\_on\_response:, retry\_on\_request: and max\_retries: keys.

```ruby
    actions: {
      custom_http: {
        input_fields: lambda do |object_definitions|
          [{ name: 'url', optional: false }]
        end,

        execute: lambda do |_connection, input|
          {
            results: get(input['url'])
          }
        end,

        output_fields: lambda do |object_definitions|
          []
        end,

        retry_on_response: [500, /error/] # contains error codes and error message match rules

        retry_on_request: ["GET", "HEAD"],

        max_retries: 3
      }
    }
```

* * *

## `summarize_input`

| Attribute | Description |
| --- | --- |
| Key | `summarize_input` |
| Type | Array |
| Required | False. |
| Description | Use this to summarize your input which contain long lists. Summarizing your input is important to keep the jobs page lightweight so it can load quickly. In general, when your input has lists that are longer than 100 lines, they should be summarized. |
| Expected Output | Array. For example, `['leads']` or `['report.records', 'report.description']` |

* * *

## `summarize_output`

| Attribute | Description |
| --- | --- |
| Key | `summarize_output` |
| Type | Array |
| Required | False. |
| Description | Use this to summarize your actions output which contain long lists. Summarizing your output is important to keep the jobs page lightweight so it can load quickly. In general, when your output has lists that are longer than 100 lines, they should be summarized. |
| Expected Output | Array. For example, `['leads']` or `['report.records', 'report.description']` |
| UI reference |  |

Example - Summarizing inputs and outputs in job data

When working with large arrays or data, Workato tries to show all the data in the input and output tabs of the job for each action. Sometimes, this can get confusing when we are working with a large numbers of records or large strings. You can use the `summarize_input` and `summarize_output` keys to summarize the data in your job input and output tabs to make it more human readable for users of your connector.

```ruby
    input_fields: lambda do
      [
        {
          name: 'report',
          type: 'object',
          properties: [
            {
              name: 'records',
              type: :array,
              of: :object,
              properties: [
                {
                  name: 'item_name',
                  type: 'string'
                }
              ]
            },
            {
              name: 'description',
              type: 'string'
            },
            {
              name: 'comment',
              type: 'string'
            }
          ],
        }
      ]
    end,

    summarize_input: ['report.records', 'report.description'],
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/sdk-reference/triggers.md
description: >-
  Reference for the triggers key in the Workato connector SDK, covering polling,
  dynamic webhook, and static webhook trigger definitions.
---

# SDK Reference - `triggers`

This section enumerates all the possible keys to define a trigger. There are 3 types of triggers available for you to use in Workato:

- Polling triggers (Check for new events every 5 minutes)
- Dynamic webhook triggers (Triggers in real time from webhooks. Programmatic subscription and teardown of webhook URLs must be possible in the App)
- Static webhook triggers (Triggers in real time from webhooks. Webhook URLs are passed from Workato to App by the end user.)

> **Quick Overview**
> 
> The `triggers` key can only be used in both recipes and the SDK **Test code** tab after you have created a successful connection. Triggers are configured by end users of your connector and kick start recipes.

## Structure

```ruby
    triggers: {

      [Unique_trigger_name]: {
        title: String,

        subtitle: String,

        description: lambda do |input, picklist_label|
          String
        end,

        help: lambda do |input, picklist_label|
          Hash
        end,

        display_priority: Integer,

        batch: Boolean,

        bulk: Boolean,

        deprecated: Boolean,

        config_fields: Array

        input_fields: lambda do |object_definitions, connection, config_fields|
          Array
        end,

        webhook_key: lambda do |connection, input|
          String
        end,

        webhook_response_type: String,

        webhook_response_body: String,

        webhook_response_headers: String,

        webhook_response_status: Integer,

        webhook_payload_type: String,

        webhook_subscribe: lambda do |webhook_url, connection, input, recipe_id|
          Hash or Array
        end,

        webhook_refresh: lambda do |webhook_subscribe_output|
          Array
        end,

        webhook_unsubscribe: lambda do |webhook_subscribe_output, connection|
          Hash
        end,

        webhook_notification: lambda do |input, payload, extended_input_schema, extended_output_schema, headers, params, connection, webhook_subscribe_output|
          Hash or Array
        end,

        poll: lambda do |connection, input, closure|
          Hash
        end,

        dedup: lambda do |record|
          String
        end,

        output_fields: lambda do |object_definitions, connection, config_fields|
          Array
        end,

        sample_output: lambda do |connection, input|
          Hash
        end,

        summarize_input: Array,

        summarize_output: Array
      },

      [Another_unique_trigger_name]: {
        ...
      }
    },
```

* * *

## `title`

| Attribute | Description |
| --- | --- |
| Key | `title` |
| Type | String |
| Required | Optional. Defaults to title built from labeled key. |
| Description | This allows you to define the title of your trigger, which might differ from the name of the key assigned to it - Key = `new_updated_object`, title = `"New/updated object"` |
| Expected Output | `String` i.e. `"New/updated object"` |
| UI reference |  |

> **TIP**
> 
> In Workato, we generally advise the following structure for triggers "\[Adjective\] \[Object\]" - "New lead" or "New/updated contact" rather than "Lead created".

* * *

## `subtitle`

| Attribute | Description |
| --- | --- |
| Key | `subtitle` |
| Type | String |
| Required | Optional. Defaults to subtitle inferred from connector name and trigger title. |
| Description | This allows you to define the subtitle of your trigger. |
| Expected Output | `String` i.e. `"Use complex queries to search objects in Percolate"` |
| UI reference |  |

> **TIP**
> 
> To make your subtitles meaningful, try to provide more information in here whilst keeping your titles concise. For example, your title could be "New/updated object" whereas your subtitle could be "Trigger off new/updated leads, contacts etc." When users search for a specific triggers, Workato also searches for matches in the subtitle.

* * *

## `description`

| Attribute | Description |
| --- | --- |
| Key | `description` |
| Type | lambda function |
| Required | Optional. Defaults to description inferred from connector name and trigger title. |
| Description | This allows you to define the description of your trigger when viewed in the recipe editor. This can be a static description or a dynamic one based on your needs. |
| Possible Arguments | `input` - Hash representing user given inputs defined in `input_fields` `picklist_label` - Only applicable for picklists where a user's answer consist of both a picklist label and value. This Hash represents the label for a user's given inputs for picklist fields. See below for use cases. |
| Expected Output | `String` i.e. `"New or updated <span class='provider'>campaign</span> in <span class='provider'>Percolate</span>"` Add the `<span>` HTML tags to add weight to your description text. |
| UI reference |  |

Example - description:

For the `description` block, you have access to two arguments to make your descriptions dynamic. This is useful when you want to change your description based on how a given user has configured the action. These changes can be incredibly useful for your users to ensure they know what this action is doing without having to click and view the action's configuration to understand what it does.

```ruby
    new_updated_object: {
      description: lambda do |input, picklist_label|
        "New or updated <span class='provider'>#{picklist_label['object'] || 'object'}</span> in " \
        "<span class='provider'>Percolate</span>"
      end,

      config_fields: [
        {
          name: 'object',
          control_type: 'select',
          pick_list: 'object_types',
          optional: false
        }
      ]

      # More keys to define the action
    }
```

In the preceding example, the action is a generic object action that allows the user to choose between multiple object types when configuring the recipe. You can change the description of the object the user selects by referencing the `picklist_label` argument.

* * *

## `help`

| Attribute | Description |
| --- | --- |
| Key | `help` |
| Type | lambda function |
| Required | Optional. No help is displayed otherwise. |
| Description | The help text that is meant to guide your users as to how to configure this trigger. You can also point them to documentation. |
| Possible Arguments | `input` - Hash representing user given inputs defined in `input_fields` `picklist_label` - Only applicable for picklists where a user's answer consist of both a picklist label and value. This Hash represents the label for a user's given inputs for picklist fields. See below for use cases. `connection` - Hash representing user given inputs defined in `connection`. `webhook_base_url` - Used when you are using [static webhook triggers](/en/developing-connectors/sdk/guides/building-triggers/static-webhook). String representing the static webhook url of your connector. |
| Expected Output | `Hash` or `String` See below for examples. |
| UI reference |  |

Example - help:

The output of the `help` lambda function can either be a simple String or a Hash. Below we go through the two examples:

- String

```ruby
    help: lambda do |input, picklist_label, connection, webhook_base_url|
      'Create an object in Percolate. First, select from a list of ' \
      'objects that we currently support. After selecting your object,' \
      ' dynamic input fields specific to your scope and object selected ' \
      'will be populated.' \
      ' Creating an approval denotes submitting a specified piece of content' \
      ' or campaign for a specific approval workflow.'
    end,
```

- Hash

```ruby
    help: lambda do |input, picklist_label, connection, webhook_base_url|
      {
        body: "First, filter by the object you want then fill up the input fields " \
        "which appear based on the object you have selected. Amongst other things, " \
        "you’ll be able to search for contacts in your company and cloud recordings from the past. ",
        learn_more_url: "https://docs.workato.com/connectors/zoom/event-actions.html#search-event-details",
        learn_more_text: "Learn more"
      }
    end,
```

Example - Static webhook triggers - Using connection and inputs to create a Unique webhook URL

When you may have a single connector and static webhook url that needs to power multiple recipes across multiple connections, you might need your users to register webhook URLs that contain attributes specific to their connections. You can now do this through the `help` lambda where you can provide a webhook URL for your users to register that include any connection attributes within the webhook's URL parameters.

```ruby
    {
      title: "Sample connector",

      webhook_keys: lambda do |params, headers, payload|
        "#{params['org_id']}@#{payload['formId']}"
      end,

      triggers: {
        sample_static_webhook_trigger: {

          help: lambda do |input, picklist_label, connection, webhook_base_url|
            next unless webhook_base_url.present?
            <<~HTML
            Creates a job when an form submission is received. To set this webhook up,
            'you will need to register the webhook below under "settings" => "webhooks" => "new". <br>
            <b>Webhook endpoint URL</b>
            <b class="tips__highlight">#{webhook_base_url}?org_id=#{connection['org_id']}</b>
            HTML
          end,

          webhook_key: lambda do |connection, input|
            "#{connection['org_id']}@#{input['formId']}"
          end,

          input_fields: lambda do |object_definitions, connection, config_fields|
            [
              {
                name: 'formId',
                label: "Form",
                control_type: "select",
                pick_list: "forms",
                hint: "Select the form you want to trigger this recipe off."
              }
            ]
          end,
        }
      }
    }
```

* * *

## `display_priority`

| Attribute | Description |
| --- | --- |
| Key | `display_priority` |
| Type | Integer |
| Required | Optional. Defaults to zero, otherwise to the alphabetical ordering of actions titles. |
| Description | This allows you to influence the ordering of the trigger in the recipe editor so that you can highlight top triggers. The higher the integer, the higher the priority. If two triggers have the same priority, they are ordered by their titles. |

* * *

## `batch`

| Attribute | Description |
| --- | --- |
| Key | `batch` |
| Type | Boolean |
| Required | Optional. |
| Description | This presents a "Batch" tag next to your action to indicate that this action works with multiple records. Normally used in batch triggers or batch create/update/upsert actions where users can pass a list of records. |
| UI reference |  |

* * *

## `bulk`

| Attribute | Description |
| --- | --- |
| Key | `bulk` |
| Type | Boolean |
| Required | Optional. |
| Description | This presents a "Bulk" tag next to your action to indicate that this action works with a large flat file of records. Normally used bulk create/update/upsert actions where users pass a CSV of records. |
| UI reference |  |

* * *

## `deprecated`

| Attribute | Description |
| --- | --- |
| Key | `deprecated` |
| Type | Boolean |
| Required | Optional. |
| Description | This presents a "deprecated" tag next to your action to indicate that this action has been deprecated. Recipes which used to use this action will continue to work but future recipes will not be able to search and select this action. |
| UI reference |  |

> **TIP**
> 
> Deprecation is a great way to move users to new actions when changes are not backwards compatible. This gives you more freedom to make your actions more usable or cater for upcoming API changes.

* * *

## `config_fields`

| Attribute | Description |
| --- | --- |
| Key | `config_fields` |
| Type | Array |
| Required | Optional. |
| Description | This key accepts an array of hashes which show up as input fields shown to a user. Config fields are shown to a user before input fields are rendered and can be used to alter what set of input fields are shown to an end user. This is often used in generic object actions where config fields prompt a user to select the object and input fields are rendered based on that selection. Inputs given to `config_fields` can be referenced by the connector in the `input_fields` lambda function via an argument. It is also present as an argument in all `object_defintions`. Refer to [Workato Schema](/en/developing-connectors/sdk/sdk-reference/schema) for more information on defining config fields. |
| Expected Output | Array of hashes. Each hash in this array corresponds to a separate config field. |
| UI reference |  |

> **TIP**
> 
> Config fields are powerful tools to introduce dynamic behavior to your actions. Use them to make your connector easier to use and discover new features. In the example gif above, you can see that the input "Event" actually causes more input fields to render. These input fields are rendered based on the selection of the value "Meeting".

* * *

## `input_fields`

| Attribute | Description |
| --- | --- |
| Key | `input_fields` |
| Type | lambda function |
| Required | True |
| Description | This lambda function allows you to define what input fields should be shown to a user configuring this trigger in the recipe editor. Output of this lambda function should be an array of hashes, where each hash in this array corresponds to a separate input field. Refer to [Workato Schema](/en/developing-connectors/sdk/sdk-reference/schema) for more information on defining input fields. |
| Possible Arguments | `object_definitions` - Allows you to reference an object definitions. Object definitions are stores of these arrays hashes which may be used to represent both input fields or output fields (datapills). These can be referenced by any action or trigger. `connection` - Hash representing user given inputs defined in `connection`. `config_fields` - Hash representing user given inputs defined in `config_fields`, if applicable. |
| Expected Output | Array of hashes. Each hash in this array corresponds to a separate input field. |
| UI reference |  |

* * *

## `webhook_key`

| Attribute | Description |
| --- | --- |
| Key | `webhook_key` |
| Type | lambda function |
| Required | True if trigger is a static webhook trigger. False otherwise. Should not be used when `webhook_subscribe`, `webhook_unsubscribe` is defined. |
| Description | **Used in conjunction with `webhook_keys` which should be present as a root level key in the connector - same level as `actions` and `triggers`** Allows you to use any user input from the connection or trigger to build a unique signature for this trigger. This can also be a static string value. When the signature in this lambda function match the signature in the `webhook_keys` lambda function, webhooks are sent to this trigger. See our [Static webhook guide for more details.](/en/developing-connectors/sdk/guides/building-triggers/static-webhook) |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `connection`. `input` - Hash representing user given inputs defined in `input_fields` |
| Expected Output | Array of hashes. Each hash in this array corresponds to a separate input field. |

Example - webhook\_key:

The `webhook_key` lambda function is specific to a single trigger and the output signature if built from user inputs. On the other hand, the `webhook_keys` lambda function is tied to the entire connector and the output signature is built from the incoming webhook's attributes like its body, headers, and query parameters. When expecting a match in these two signature, it becomes easy to see how routing is done from incoming webhooks to the proper trigger to create jobs.

```ruby
    {
      title: "Sample connector",

      webhook_keys: lambda do |params, headers, payload|
        payload['formId']
      end,

      triggers: {
        sample_static_webhook_trigger: {

          help: lambda do |_input, _picklist_label|
            {
              body: “Triggers in real-time whenever an event is created. Set up this trigger by registering the Webhook URL ” \
                    “below in <b>Settings</b> => <b>Webhooks</b>.“,
              learn_more_url: “https://docs.workato.com”,
              learn_more_text: “Learn more”
            }
          end,

          webhook_url_help: lambda do |_connection, _input, webhook_base_url|
            webhook_base_url
          end,

          input_fields: lambda do |object_definitions, connection, config_fields|
            [
              {
                name: 'formId',
                label: "Form",
                control_type: "select",
                pick_list: "forms",
                hint: "Select the form you want to trigger this recipe off."
              }
            ]
          end,

          webhook_key: lambda do |connection, input|
            input['formId']
          end,
        }
      }
    }
```

* * *

## `webhook_response_type`

| Attribute | Description |
| --- | --- |
| Key | `webhook_response_type` |
| Type | String |
| Required | Optional. Only applies to Dynamic webhook triggers ( triggers with `webhook_subscribe` and `webhook_unsubscribe`) |
| Description | By default, Workato responds with no content-type headers to webhook events. `webhook_response_type` allows for 'plain' and 'json' which corresponds to content-type headers `text/plain` and `application/json` respectively. |

* * *

## `webhook_response_body`

| Attribute | Description |
| --- | --- |
| Key | `webhook_response_body` |
| Type | String |
| Required | Optional. Only applies to Dynamic webhook triggers ( triggers with `webhook_subscribe` and `webhook_unsubscribe`) |
| Description | By default, Workato responds with an empty body to webhook events. `webhook_response_body` allows for a mustache template that allows you to define how Workato should respond to webhooks. |

Mustache templates have access to the following variables:

| name | description | example usage |
| --- | --- | --- |
| headers | Contains request headers. Headers are normalized (x–custom-header -> X-Custom-Header) | `{ “challenge”:“{{{headers.X-Challenge}}}” }` |
| body | Request body is parsed according to the `webhook_response_type`. You can use dot notation to access nested values. | `{ “challenge”: “{{body.x-challenge}}” }` |
| query | Contains query params | `{ “X-Challenge”: “{{query.challenge}}” }` |

Example - webhook\_response\_body: - Defining a custom webhook response

Use `webhook_response_body` in two scenarios:

1. You need to respond with a static string or JSON response to the webhook sender.

```ruby
  webhook_response_type: 'json',
  webhook_response_body: '{ "success": true }',
```

will result in Workato responding with a content-type `application/json` and the body

```json
{
  "success": true
}
```

2. You need to respond with a dynamic response based on the webhook event. For example, when webhook senders send a webhook event to confirm that the webhook URL is ready.

```ruby
  webhook_response_type: 'json',
  webhook_response_body: '{ “challenge”: “{{body.verification.Challenge}}” }',
```

If the sender sends a webhook with the body

```json
{
  "verification": {
    "Challenge": "abc123"
  }
}
```

Then Workato would respond with

```json
{
  "challenge": "abc123"
}
```

In some cases, webhook senders may also send an array of events. You may also use regular iterators in Mustache to work with arrays.

For example, if the sender (based on Microsoft Event Grid)sends a webhook validation event with the body

```json
[
  {
    "id": "2d1781af-3a4c-4d7c-bd0c-e34b19da4e66",
    "topic": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "subject": "",
    "data": {
      "validationCode": "512d38b6-c7b8-40c8-89fe-f46f9e9622b6",
      "validationUrl": "https://rp-eastus2.eventgrid.azure.net:553/eventsubscriptions/myeventsub/validate?id=0000000000-0000-0000-0000-00000000000000&t=2022-10-28T04:23:35.1981776Z&apiVersion=2018-05-01-preview&token=1A1A1A1A"
    },
    "eventType": "Microsoft.EventGrid.SubscriptionValidationEvent",
    "eventTime": "2022-10-28T04:23:35.1981776Z",
    "metadataVersion": "1",
    "dataVersion": "1"
  }
]
```

and expects us to respond with the `data.validationCode`. You may define your `webhook_response_body` as such.

```ruby
  webhook_response_type: 'json',
  webhook_response_body: '{{#body}}{ "validationResponse": “{{data.validationCode}}” }{{/body}}',
```

There may be a variety of situations where webhook senders may expect custom responses:

1. Static or dynamic responses for each webhook event
2. Responding to a challenge to confirm the webhook URL is ready to accept events

In our investigation, we have rarely found both to be the case. As such, this singular key `webhook_response_body` aims to accomplish both use cases. You may also use inbuilt logic such as [inverted sections](https://mustache.github.io/mustache.5.html#Inverted-Sections) in mustache templates for greater control over the webhook responses.

* * *

## `webhook_response_headers`

| Attribute | Description |
| --- | --- |
| Key | `webhook_response_headers` |
| Type | String |
| Required | Optional. Only applies to Dynamic webhook triggers ( triggers with `webhook_subscribe` and `webhook_unsubscribe`) |
| Description | By default, Workato responds with an standard headers (rate limit, byte quota) to webhook events. `webhook_response_headers` allows for a mustache template that allows you to define what headers Workato should include in response headers. See [webhook\_response\_body](#webhook-response-body) |

> **WARNING**
> 
> Workato only supports customization of headers starting with `x-` with the exception of `x-forwarded-host`, `x-forwarded-proto`, `x-forwarded-port`, `x-forwarded-for`, `x-request-id`, `x-frame-options` and `x-powered-by`.

* * *

## `webhook_response_status`

| Attribute | Description |
| --- | --- |
| Key | `webhook_response_status` |
| Type | Integer |
| Required | Optional. Only applies to Dynamic webhook triggers ( triggers with `webhook_subscribe` and `webhook_unsubscribe`) |
| Description | By default, Workato responds with 200 to webhook events. `webhook_response_status` allow you to customize this to any 2XX response codes. |

> **WARNING**
> 
> Workato only supports customization 2XX response codes.

* * *

## `webhook_payload_type`

| Attribute | Description |
| --- | --- |
| Key | `webhook_payload_type` |
| Type | String |
| Required | Optional. Defaults to "parsed" |
| Description | By default, Workato parses incoming webhook payloads using [JSON.parse()](https://ruby-doc.org/stdlib-2.6.3/libdoc/json/rdoc/JSON.html#method-i-parse). Setting `webhook_payload_type` to "raw" allows you to receive the raw webhook payload instead of a JSON parsed one. |

Example - webhook\_payload\_type: - Verifying webhooks or handling XML webhooks

Use `webhook_payload_type` in two scenarios:

1. You need to compute a webhook payload signature based on the **raw** payload. You may do so in the webhook notification lambda before using `workato.parse_json` to get the parsed json payload.

```ruby
      webhook_payload_type: "raw",

      webhook_notification: lambda do |input, payload, extended_input_schema, extended_output_schema, headers, params, connection, webhook_subscribe_output|
        original_payload = payload
        client_secret = input['client_secret'] || account_property('hubspot_webhook_client_secret')
        if client_secret.present?
          source_string = client_secret + original_payload
          v1_signature = source_string.encode_sha256.encode_hex
        end

        if (client_secret.present? && v1_signature == headers['X-Hubspot-Signature']) || !client_secret.present?
          payload = workato.parse_json(payload).select do |event|
            event['propertyName'] == input['contact_property'] && event['subscriptionType'] == 'contact.propertyChange'
          end

          if payload.length > 0
            {
              events: payload,
              headers: headers,
              webhook_validated: client_secret.present? ? true : false
            }
          end
        end
      end,
```

2. You are receiving a webhook that is not in JSON format.

```ruby
      webhook_payload_type: "raw",

      webhook_notification: lambda do |input, payload, extended_input_schema, extended_output_schema, headers, params, connection, webhook_subscribe_output|
        payload.from_xml
      end,
```

* * *

## `webhook_subscribe`

| Attribute | Description |
| --- | --- |
| Key | `webhook_subscribe` |
| Type | lambda function |
| Required | True if trigger is a dynamic webhook trigger. False otherwise. Should not be used when `webhook_key` is defined. |
| Description | This lambda function is used by dynamic webhook triggers to programmatically subscribe to webhooks. This function is invoked when a user starts the recipe using the trigger with this defined. See our [Dynamic webhook guide for more details.](/en/developing-connectors/sdk/guides/building-triggers/dynamic-webhook) |
| Possible Arguments | `webhook_url` - String representing the **recipe-specific webhook URL**. This should be passed on to the API when creating the webhook subscription. `connection` - Hash representing user given inputs defined in `connection`. `input` - Hash representing user given inputs defined in `input_fields` `recipe_id` - Int representing the ID of the recipe in Workato. |
| Expected Output | There are two possible outputs: - A hash which is passed on as `webhook_subscribe_output` to `webhook_unsubscribe`, `webhook_notification` and `webhook_refresh` lambda functions. - An array where the first index is the same hash passed on as `webhook_subscribe_output` and the second index is the webhook expiration datetime which will trigger `webhook_refresh`. |

Dealing with webhook subscriptions that expire

Certain APIs like [Microsoft's Graph API](https://docs.microsoft.com/en-us/graph/api/subscription-post-subscriptions?view=graph-rest-1.0&tabs=http) allow you to create webhook subscriptions but they expire after a certain amount of time. This means your triggers need to be able to intelligently know when the webhook subscription is about to expire and refresh this subscription so you continue to receive events.

Sample code where webhook expires after 1 hour.

```ruby
      webhook_subscribe: lambda do |webhook_url, connection, input, recipe_id|
        [
          post("https://www.acme.com/api/webhook_subscriptions", url: webhook_url),
          1.hour.from_now
        ]
      end,

      webhook_refresh: lambda do |webhook_subscribe_output|
        [
          patch("https://www.acme.com/api/webhook_subscriptions/#{webhook_subscribe_output['id']}", refresh: true),
          1.hour.from_now
        ]
      end,

      webhook_unsubscribe: lambda do |webhook_subscribe_output, connection|
        delete("https://www.acme.com/api/webhook_subscriptions/#{webhook_subscribe_output['id']}")
      end,
```

In the example above, the output of `webhook_subscribe` is an array that contains a datetime value that corresponds to the next time `webhook_refresh` is invoked to refresh the webhook subscription. This is similarly done for `webhook_refresh` as well. Take note that the output of `webhook_refresh` replaces the original `webhook_subscribe_output` as well.

* * *

## `webhook_refresh`

| Attribute | Description |
| --- | --- |
| Key | `webhook_refresh` |
| Type | lambda function |
| Required | False. Only applicable when `webhook_subscribe` is defined. |
| Description | This lambda function is invoked when your webhook subscription is set to have an expiry time, defined in the output of `webhook_subscribe`. It allows you to refresh as webhook subscriptions so your trigger can continue to receive events. |
| Possible Arguments | `webhook_subscribe_output` - Hash representing the output of the `webhook_subscribe` lambda function. |
| Expected Output | \- An array where the first index is the same hash passed on as `webhook_subscribe_output` and the second index is the webhook expiration datetime which will trigger `webhook_refresh`. |

* * *

## `webhook_unsubscribe`

| Attribute | Description |
| --- | --- |
| Key | `webhook_unsubscribe` |
| Type | lambda function |
| Required | True if trigger is a dynamic webhook trigger. False otherwise. Should not be used when `webhook_key` is defined. |
| Description | This lambda function is used by dynamic webhook triggers to programmatically teardown webhooks subscriptions. This function is invoked when a user stops the recipe using the trigger with this defined. See our [Dynamic webhook guide for more details.](/en/developing-connectors/sdk/guides/building-triggers/dynamic-webhook) |
| Possible Arguments | `webhook_subscribe_output` - Hash representing the output of the `webhook_subscribe` lambda function. `connection` - Hash representing user given inputs defined in `connection`. |
| Expected Output | No output necessary. |

* * *

## `webhook_notification`

| Attribute | Description |
| --- | --- |
| Key | `webhook_notification` |
| Type | lambda function |
| Required | True if trigger is either a dynamic webhook trigger or a static webhook trigger. |
| Description | This lambda function handles what this trigger should do with a webhook sent to it. You may use this function to do any data manipulation. This lambda function does not allow you to make additional HTTP requests or invoke additional reusable `methods`. |
| Possible Arguments | `input` - Hash representing user given inputs defined in `input_fields` `payload` - Hash representing the incoming webhook's payload. `extended_input_schema` - See below for examples. `extended_output_schema` - See below for examples `headers` - Hash representing the incoming webhook's headers. `params` - Hash representing the incoming webhook's query parameters. `connection` - Hash representing user given inputs defined in `connection`. `webhook_subscribe_output` - Hash representing the output of the `webhook_subscribe` lambda function. |
| Expected Output | Hash which represents the output of a single job or an array of hashes which represent individual jobs. |

> **Note**
> 
> The webhook\_notification lambda does not allow users to call `methods` or HTTP methods. If webhook payloads are skinny, please add actions that can take the output of the trigger to perform additional HTTP requests.

> **Webhook Validations**
> 
> - Workato performs validations on JSON based webhooks - denoted by the webhook's `Content-Type` header, to ensure that the payload is valid JSON. Otherwise, Workato responds with 400 bad request.
> - Incoming webhook payloads are expected to be UTF-8 compatible and Workato responds with 400 bad request if UTF-8 incompatible characters are found.

* * *

## `poll`

| Attribute | Description |
| --- | --- |
| Key | `poll` |
| Type | lambda function |
| Required | True if trigger is a [polling trigger](/en/developing-connectors/sdk/guides/building-triggers/poll) or [Hybrid triggers](/en/developing-connectors/sdk/guides/building-triggers/hybrid-triggers) |
| Description | This lambda function handles the how this trigger retrieves new records from an API to create jobs. This function is invoked every poll interval (5 mins by default but configurable on a recipe level). |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `connection`. `input` - Hash representing user given inputs defined in `input_fields` `closure` - Hash representing the cursor values passed to the `poll` lambda function from the previous execution of this same function. `extended_input_schema` - See below for examples. `extended_output_schema` - See below for examples |
| Expected Output | Hash which contains 3 attributes - Array of records to be turned into jobs - Boolean flag which tells the trigger to poll again immediately instead of 5 mins later - Value/Hash which is stored as the closure which will be passed to the next execution of this same function. See below for examples |

> **TIP**
> 
> Closure values can be either a simple string/integer or a hash if you need to store multiple values for your cursor.

Example - poll:

The poll block's output should be a hash in the following structure:

```ruby
    poll: lambda do |connection, input, closure, _eis, _eos|

      # Timestamp which we need to filter records based off.
      updated_since = (closure || input['since']).to_time.utc.iso8601
      request_page_size = 100

      records = get("/records/endpoint").
                  params(
                     # filter for records only updated after this time
                    updated_since: updated_since,
                    page_size: request_page_size
                  )
      # Example JSON response
      # {
      #   data: [
      #     {
      #       "id": "abcd123",
      #       "name": "record1"
      #       ...
      #     },
      #     {
      #       "id": "dcba321",
      #       "name": "record2",
      #       ...
      #     },
      #     ...
      #   ],
      #   total_records: 1000
      # }

      # Derive last updated since timestamp to filter
      next_updated_since = records['data'].last['updated_at'] unless records.blank?

      {
        # Event accepts an array of records. Each record is a new job.
        events: records['data'],
        # Closure value which is passed as closure argument in next poll
        next_poll: next_updated_since,
        # Boolean flag to denote whether we should wait 5 mins to poll or poll immediately.
        # Poll immediately if total records is still more than page size.
        can_poll_more: records['total_records'] >= request_page_size
      }
    end,
```

Example - poll: - extended\_input\_schema and extended\_output\_schema

Extended input and output schema is any schema from `object_definitions` that is used in your action. This information is often useful when you dynamically generate schema and you want to use it to do data pre- or post-processing. These arguments do not include config\_fields.

For example, you may use extended\_input\_schema to know which inputs are datetimes and should be transformed to Epoch time which is accepted by the target API. In the same fashion, you may use extended\_output\_schema to take the response and transform Epoch variables into ISO8601 datetimes again.

```ruby
    create_object: {
      description: lambda do |input, picklist_label|
        "Create a <span class='provider'>#{picklist_label['object'] || 'object'}</span> in " \
        "<span class='provider'>Percolate</span>"
      end,

      config_fields: [
        {
          name: 'object',
          control_type: 'select',
          pick_list: 'object_types',
          optional: false
        }
      ],

      input_fields: lambda do |object_definitions, connection, config_fields|
        object = config_fields['object']
        object_definitions[object].ignored('id')
      end,

     execute: lambda do |connection, input, extended_input_schema, extended_output_schema|
       puts extended_input_schema
       # [
       #   {
       #     "type": "string",
       #     "name": "status",
       #     "control_type": "select",
       #     "label": "Status",
       #     "hint": "Status is required for creating Content",
       #     "pick_list": "post_statuses",
       #     "optional": false
       #   },
       #   ...
       # ]

       puts extended_output_schema
       # [
       #   {
       #     "type": "string",
       #     "name": "id",
       #     "control_type": "text",
       #     "label": "Content ID",
       #     "hint": "The Content ID, Example: <b>post:45565410</b>.",
       #     "optional": true
       #   },
       #   {
       #     "type": "string",
       #     "name": "status",
       #     "control_type": "select",
       #     "label": "Status",
       #     "hint": "Status is required for creating Content",
       #     "pick_list": "post_statuses",
       #     "optional": false
       #   },
       #   ...
       # ]
     end,

     output_fields: lambda do |object_definitions, connection, config_fields|
       object = config_fields['object']
       object_definitions[object]
      end,
    }
```

* * *

## `dedup`

| Attribute | Description |
| --- | --- |
| Key | `dedup` |
| Type | lambda function |
| Required | True. |
| Description | This lambda function allows you to deduplicate trigger events so you don't trigger off the same events twice. This is done by forming a unique signature string based off attributes of the incoming record. |
| Possible Arguments | `record` - Hash representing a single record. This is a single index in the `events` array of a `poll` lambda function or the Hash output of the `webhook_notification` lambda function. . |
| Expected Output | String - "#{record\['id'\]}@#{record\['created\_at'\]}" or "#{record\['id'\]}@#{record\['updated\_at'\]}" |

* * *

## `output_fields`

| Attribute | Description |
| --- | --- |
| Key | `output_fields` |
| Type | lambda function |
| Required | True |
| Description | This lambda function allows you to define what output fields (datapills) should be shown to a user configuring this trigger in the recipe editor. The output of this lambda function should be an array of hashes, where each hash in this array corresponds to a separate output field (datapill). Refer to [Workato Schema](/en/developing-connectors/sdk/sdk-reference/schema) for more information on defining output fields. |
| Possible Arguments | `object_definitions` - Allows you to reference an object definitions. Object definitions are stores of these arrays which can represent either input and output fields. These can be referenced by any action or trigger. `connection` - Hash representing user given inputs defined in `connection`. `config_fields` - Hash representing user given inputs defined in `config_fields`, if applicable. |
| Expected Output | Array of hashes. Each hash in this array corresponds to a separate input field. |
| UI reference |  |

* * *

## `sample_output`

| Attribute | Description |
| --- | --- |
| Key | `sample_output` |
| Type | lambda function |
| Required | False. |
| Description | This lambda function allows you to define a sample output that is displayed next to your output fields (datapills). |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `connection`. `input` - Hash representing user given inputs defined in `input_fields` |
| Expected Output | Hash. This hash should be a stubbed output of the `execute` lambda function. |
| UI reference |  |

* * *

## `summarize_input`

| Attribute | Description |
| --- | --- |
| Key | `summarize_input` |
| Type | Array |
| Required | False. |
| Description | Use this to summarize your input which contain long lists. Summarizing your input is important to keep the jobs page lightweight so it can load quickly. In general, when your input has lists that are longer than 100 lines, they should be summarized. |
| Expected Output | Array. For example, `['leads']` or `['report.records', 'report.description']` |

* * *

## `summarize_output`

| Attribute | Description |
| --- | --- |
| Key | `summarize_output` |
| Type | Array |
| Required | False. |
| Description | Use this to summarize your actions output which contain long lists. Summarizing your output is important to keep the jobs page lightweight so it can load quickly. In general, when your output has lists that are longer than 100 lines, they should be summarized. |
| Expected Output | Array. For example, `['leads']` or `['report.records', 'report.description']` |
| UI reference |  |

Example - Summarizing inputs and outputs in job data

When working with large arrays or data, Workato tries to show all the data in the input and output tabs of the job for each action. Sometimes, this can get confusing when we are working with a large numbers of records or large strings. You can use the `summarize_input` and `summarize_output` keys to summarize the data in your job input and output tabs to make it more human readable for users of your connector.

```ruby
    input_fields: lambda do
      [
        {
          name: 'report',
          type: 'object',
          properties: [
            {
              name: 'records',
              type: :array,
              of: :object,
              properties: [
                {
                  name: 'item_name',
                  type: 'string'
                }
              ]
            },
            {
              name: 'description',
              type: 'string'
            },
            {
              name: 'comment',
              type: 'string'
            }
          ],
        }
      ]
    end,

    summarize_input: ['report.records', 'report.description'],
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/sdk-reference/object_definitions.md
description: >-
  Reference for the object_definitions key in the Workato connector SDK, used to
  define and reuse input and output field schema.
---

# SDK Reference - `object_definitions`

Object definitions represent specific resources from a target application. For example, they represent the schema for Salesforce leads or Snowflake rows.

These definitions are stored as arrays of hashes, and are used in both input and output fields.

> **Avoid repeating code with object definitions**
> 
> Store object definition in one place and reuse throughout the custom connector.

## Structure

```ruby
    object_definitions: {

      [Unique_object_definition_name]: {
        fields: lambda do |connection, config_fields, object_definitions|
          Array
        end
      },

      [Another_unique_object_definition_name]: {
        ...
      }
    },
```

* * *

| Attribute | Description |
| --- | --- |
| Key | `fields` |
| Type | lambda function |
| Required | True |
| Description | This lambda function is invoked whenever its parent object\_definition's key is called in an action or trigger. It is able to make HTTP requests to dynamically build schema from metadata endpoints. The output of this lambda function should be an array of hashes that represents the input or output fields. This is called Workato Schema. Refer to [Workato Schema](/en/developing-connectors/sdk/sdk-reference/schema) for more information |
| Possible Arguments | `connection` - Hash representing user given inputs defined in the connection. `config_fields` - Hash representing the user given inputs from config fields in the action or trigger that referenced this object definition. `object_definitions` - Allows you to reference other object\_definitions. |
| Expected Output | Array |

> **DEFINE ARGUMENTS FOR OBJECT DEFINITIONS**
> 
> You must define arguments for your object definitions, even if they are not used. Workato determines whether your schema is static or dynamic based on whether your object definitions have arguments defined. Changing your schema from static to dynamic is considered backward incompatible; you must stop running recipes and refresh the schema for the changes to take effect.
> 
> **Static object definition**
> 
> ```ruby
> lead: {
>   fields: lambda do
>     [
>       { name: "name", type: :boolean },
>       { name: "email" },
>       { name: "number"}
>     ]
>   end
> }
> ```
> 
> **Dynamic object definition**
> 
> ```ruby
> lead: {
>   fields: lambda do |connection, config_fields, object_definitions|
>     [
>       { name: "name", type: :boolean },
>       { name: "email" },
>       { name: "number"}
>     ]
>   end
> }
> ```
> 
> _Workato recommends that you define all object\_definitions dynamically (with arguments) to ensure no issues arise from any future changes._

Example - fields

Object\_definitions can be static and simply store an array. When this object definition is referenced, the `fields` lambda function returns this array.

```ruby
    object_definitions: {
      lead: {
        fields: lambda do |connection, config_fields, object_definitions|
          [
            { name: "name", type: :boolean },
            { name: "email" },
            { name: "number"}
          ]
        end
      }
    }
```

Object\_definitions can also be dynamic and make HTTP requests to metadata endpoints. When this object definition is referenced, the `fields` lambda function makes this request, receives the response and should massage the response into the same array that can be returned to the `input_fields` or `output_fields` lambda function that referenced it. Refer to [Workato Schema](/en/developing-connectors/sdk/sdk-reference/schema) for more information on defining `input_fields` and `output_fields`.

```ruby
    object_definitions: {
      form: {
        fields: lambda do |connection|
          get("https://api.unbounce.com/pages/#{connection['page_id']}/form_fields")["formFields"].
            map { |field| { name: field["id"] } }
        end
      }
    }
```

Example - Building schema from multiple object\_definitions

To keep your code DRY, our recommendation is to logically break up your schema definitions into separate object\_definitions. These object\_definitions may be dynamically generated separately and pieced together.

```ruby
    object_definitions: {
      create_object_output: {
        fields: lambda do |connection, config_fields, object_definitions|
          if config_fields['object'] == 'customer'
            [
              {
                name: 'customer',
                type: 'object',
                properties: object_definitions['customer_schema']
              },
              {
                name: 'card',
                type: 'object',
                properties: object_definitions['card_schema']
              }
            ]
          elsif config_fields['object'] == 'subscription'
            [
              {
                name: 'customer',
                type: 'object',
                properties: object_definitions['customer_schema']
              },
              {
                name: 'subscription',
                type: 'object',
                properties: object_definitions['subscription_schema']
              },
              {
                name: 'card',
                type: 'object',
                properties: object_definitions['card_schema']
              }
            ]
          end
        end
      }
    }
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/sdk-reference/picklists.md
description: >-
  Reference for the pick_lists key in the Workato connector SDK, used to
  generate select, multiselect, and tree drop-down input fields.
---

# SDK Reference - `pick_lists`

Picklists are used in conjunction with some input fields to enumerate the possible options in a drop-down. Picklist options can be stored in the `pick_lists` key or defined directly in the input field hash. Input fields that use `pick_list` attribute have to be of the following `control_type`:

- `select`
  - Allows the user to select a single input from the drop-down.
- `multiselect`
  - Allows the user to select multiple inputs from the drop-down.
- `tree`
  - Allows the user to select a single or multiple inputs from a hierarchical drop-down.

> **Quick Overview**
> 
> Pick lists are a great way to make your connector easier to use when the API only accepts a certain set of values. Rather than having the user type it in manually, you should use picklists so they can easily select the value from a drop-down. The `pick_list` key is where you can store these options and refer to them when building your input fields.

## Structure

```ruby
    pick_lists: {

      [Unique_pick_list_name]: lambda do |connection, pick_list_parameters|
        Array
      end,

      [Another_unique_pick_list_name]: lambda do |connection, pick_list_parameters|
        Array
      end
    },
```

* * *

| Attribute | Description |
| --- | --- |
| Key | `[Unique_pick_list_name]` |
| Type | lambda function |
| Required | True |
| Description | This lambda function is invoked whenever its parent object\_definition's key is called in an action or trigger. It is able to make HTTP requests to dynamically build schema from metadata endpoints. The output of this lambda function should be an array of hashes that represents the input or output fields. |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `connection` `pick_list_parameters` - Used when defining dependent picklists. |
| Expected Output | Array of Array |

Pick\_lists outputs should be a 2D array in the following format:

```ruby
[
  [ "Picklist Label", "Value" ],
  [ "Picklist Label", "Value" ],
  [ "Picklist Label", "Value" ],
  [ "Picklist Label", "Value" ]
]
```

> **\- pick\_lists not allowed for connections fields**

Example - options in connection fields

When defining enumerable values for connection fields, take note that you may not reference `pick_lists` defined in your connector.

Instead, you may define these fields statically and using the schema attribute - `options`

```ruby
connection: {
  fields: [
    {
      name: 'environment',
      label: 'Instance environment',
      control_type: 'select',
      options: [
        ['Production', 'production'],
        ['Sandbox', 'Sandbox']
      ]
    }
  ]
}
```

Example - pick\_lists: - Static

Pick\_lists can be static. When referenced, this definition would return the array stored in it. When an input field references this picklist, this array is returned and rendered on the front end as a drop-down.

```ruby
    input_fields: lambda do |object_definitions|
      [
        {
          name: 'event_category',
          control_type: 'select',
          pick_list: 'events'
        }
      ]
    end,
```

```ruby
    pick_lists: {
      events: lambda do |connection|
        [
          ["Meeting","meeting"],
          ["Webinar","webinar"],
          ["Cloud recording","recording"],
          ["User","user"],
        ]
      end
    },
```

Example - pick\_lists: - dependent & static

Dependent pick lists allow you to change the contents of a pick list based on the value of another field. For example, rather than displaying all the cities in a single pick list, we can selectively display only cities from a country, selected in another field.

```ruby
    input_fields: lambda do |_object_definitions|
      [
        {
          name: 'country',
          control_type: 'select',
          pick_list: 'countries',
          optional: false
        },
        {
          name: 'city',
          control_type: 'select',
          pick_list: 'cities',
          pick_list_params: { country: 'country' },
          optional: false
        }
      ]
    end
```

```ruby
    pick_lists: {
      countries: lambda do |_connection|
      [
        ['United States', 'USA'],
        ['India', 'IND']
      ]
      end,

      cities: lambda do |_connection, country:|
      {
        'USA' => [
          ['New York City', 'NYC'],
          ['San Fransisco', 'SF']
        ],
        'IND' => [
          ['Bangalore', 'BNG'],
          ['Delhi', 'DLH']
        ]
      }[country]
      end
    }
```

Example - pick\_lists: - dependent & dynamic

In this example, accounts is an independent dynamic pick list while properties is a dependent dynamic pick list. When defining dynamic picklists, the response from the HTTP request should still be transformed into the same array of arrays.

In this example, we used the `.pluck` function to do the transformation.

```ruby
    input_fields: lambda do |_object_definitions|
      [
        {
          name: 'scope_id',
          label: 'Team',
          optional: false,
          control_type: 'select',
          pick_list: 'tenant_licenses'
        },
        {
          name: 'platform_id',
          control_type: 'select',
          pick_list: 'platforms',
          label: 'Platform',
          pick_list_params: { scope_ids: 'scope_id' },
          hint: 'Platform is required for creating Content'
        }
      ]
    end
```

```ruby
    pick_lists: {
      tenant_licenses: lambda do |connection|
        app_id = get("api/v5/client/client:#{connection['client_id']}")&.
                   dig('data', 'app_id')
        tenant_id = get("/api/v5/app/#{app_id}")&.dig('data', 'tenant_id')
        get('/api/v5/license/').
          params(tenant_id: tenant_id,
                 statuses: 'active')['data']&.
          select { |lic| lic['parent_id'].present? }&.
          pluck('name', 'id')
      end,

      platforms: lambda do |_connection, scope_ids:|
        get('/api/v5/platform/').
          params(scope_ids: scope_ids)['data']&.
          pluck('name', 'id')
      end,
    }
```

Example - pick\_lists: - tree

Workato also allows for `tree` type picklists. Tree picklists are often used to model hierarchical structures in applications such as file/folder structures. When using tree picklists, traditional `pick_list_parameters` are ignored and replaced by a double splat variable.

To explain this, we will use the concept of a file and folder structure, where folders might contain additional folders or files. All folders and files are considered nodes, while the main distinction is that folders might have child nodes whereas files may not. When you define a tree picklist, each time the user clicks on a folder node, the picklist is re-evaluated to build out the child nodes within it. The value of the folder node that the user clicked on can be found by `args&.[](:__parent_id)`. If this value is nil, this indicates that we are at the root node.

```ruby
    input_fields: lambda do |_object_definitions|
      [
        {
          name: 'path',
          label: 'File path',
          optional: false,
          control_type: 'tree',
          pick_list: "file_path"
        },
      ]
    end
```

```ruby
    pick_lists: {
      file_path: lambda do |_connection, **args|
        # Get sub folders
        if (folder_path = args&.[](:__parent_id)).presence
          path = []
          response = get("/pubapi/v1/fs#{folder_path}").params(list_content: true, sort_by: 'name')
          if response['is_folder']
            path << response['folders']&.map { |folder| [folder['name'].labelize, folder['path'].gsub(' ', '%20'), nil, true] }
            path << response['files']&.map { |file| [file['name'].labelize, file['path'].gsub(' ', '%20'), nil, false] } if response['files'].present?
            Array.wrap(path.compact).flatten(1)
          end
        else
          # Get root folders
          get('/pubapi/v1/fs/')['folders']&.map do |folder|
            [folder['name'].labelize, folder['path'].gsub(' ', '%20'), nil, true]
          end
        end
      end,
    }
```

In the above case, we have wanted to only allow users to select files to be downloaded. However, in a variety of cases, you might want to allow users to also select folders (the nodes) as you want them to provide a path to a folder instead of a file. This can be configured like below:

```ruby
    input_fields: lambda do |_object_definitions|
      [
        {
          name: 'path',
          label: 'Folder path',
          optional: false,
          control_type: 'tree',
          pick_list: 'folder_path',
          tree_options: {
            selectable_folder: true
          }
        },
      ]
    end
```

Another variation is when you need to allow end users to select multiple folders. This can be configured like below:

```ruby
    input_fields: lambda do |_object_definitions|
      [
        {
          name: 'path',
          label: 'Folder path',
          optional: false,
          control_type: 'tree',
          pick_list: 'folder_path',
          tree_options: {
            selectable_folder: true,
            multi_select: true,
            force_selection_hierarchy: true # Setting this to true causes all child nodes to be selected when the parent is selected.
          }
        },
      ]
    end
```

---
