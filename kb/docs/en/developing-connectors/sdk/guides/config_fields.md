---
url: 'https://docs.workato.com/en/developing-connectors/sdk/guides/config_fields.md'
description: >-
  Use config fields in the connector SDK to generate dependent input and output
  fields in actions and triggers based on user input.
---

# How-to guides - Using Config fields

Occasionally, input/output fields depend on user input. For example, when input fields for an action depend on a user's input in the same action. Here, we introduce `config_fields`. It is an optional key available in both actions and triggers. It is a special type of input field that can be used to generate other dependent input/output fields.

> **TIP**
> 
> Config fields keys can be used in both actions and triggers to introduce dynamicity to your connector.

## Sample connector - Chargebee

```ruby
{
  title: "Chargebee",

  # More connector code here

  actions: {
    create_object: {
      title: "Create object",
      subtitle: "Create object in Chargebee",

      description: lambda do |input, picklist_label|
        "Create <span class='provider'>#{picklist_label['object'] || 'object'}</span> in <span class='provider'>Chargebee</span>"
      end,

      config_fields: [
        {
          name: "object",
          label: "Object",
          control_type: 'select',
          pick_list: "objects",
          optional: false
        }
      ],

      input_fields: lambda do |object_definitions, connection, config_fields|
        object = config_fields['object']

        object_definitions[object]
      end,

      execute: lambda do |connection, input|
        object = input.delete('object')

        # Route to the appropriate endpoint based on selected object
        endpoint = case object
        when 'customer'
          '/api/v2/customers'
        when 'subscription'
          '/api/v2/subscriptions'
        when 'plan'
          '/api/v2/plans'
        else
          raise "Unsupported object type: #{object}"
        end

        post(endpoint, input).
          request_format_www_form_urlencoded
      end,

      output_fields: lambda do |object_definitions, connection, config_fields|
        object = config_fields['object']

        object_definitions[object]
      end
    }
  },

  object_definitions: {
    customer: {
      fields: lambda do |connection, config_fields, object_definitions|
        get("/api/v2/customers", limit: 1).
          dig('list',0,'customer').
          map do |key, value|
            if value.is_a?(Integer)
              type = 'integer'
              control_type = 'number'
            else
              type = 'string'
              control_type = 'text'
            end

            {
              name: key,
              label: key.labelize,
              type: type,
              control_type: control_type,
              sticky: true
            }
          end
      end
    },

    subscription: {
      fields: lambda do |connection, config_fields, object_definitions|
        get("/api/v2/subscriptions", limit: 1).
          dig('list',0,'subscription').
          map do |key, value|
            if value.is_a?(Integer)
              type = 'integer'
              control_type = 'number'
            else
              type = 'string'
              control_type = 'text'
            end

            {
              name: key,
              label: key.labelize,
              type: type,
              control_type: control_type,
              sticky: true
            }
          end
      end
    },

    plan: {
      fields: lambda do |connection, config_fields, object_definitions|
        get("/api/v2/plans", limit: 1).
          dig('list',0,'plan').
          map do |key, value|
            if value.is_a?(Integer)
              type = 'integer'
              control_type = 'number'
            else
              type = 'string'
              control_type = 'text'
            end

            {
              name: key,
              label: key.labelize,
              type: type,
              control_type: control_type,
              sticky: true
            }
          end
      end
    }
  },

  pick_lists: {
    objects: lambda do
      [
        ["Subscription", "subscription"],
        ["Customer", "customer"],
        ["Plans", "plan"]
      ]
    end,
  }
}
```

- [Chargebee API](https://apidocs.chargebee.com/docs/api/customers?prod_cat_ver=1#create-usecases)

## Step 1 - Action title, subtitle, description, and help

The first step to making a good action is to properly communicate what the actions does, how it does it and to provide additional help to users. To do so, Workato allows you to define the title, description, and provide hints for an action. Quite simply, the title is the title of an action and the subtitle provides further details of the action. The description of the action then contains specifications and explanation on what the action accomplishes and in the context of the application it connects to. Finally, the help segment provides users any additional information required to make the action work.

To know more about this step, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/actions#title)

## Step 2 - Define config\_fields

The `config_fields` key allows us to first collect some input from the end user to generate more input fields. In this action, we want the user to first select the object that they want to create, then use that input to generate fields relevant to the object they have just selected.

```ruby
  config_fields: [
    {
      name: "object",
      label: "Object",
      control_type: 'select',
      pick_list: "objects",
      optional: false
    }
  ],
```

Here, we are using the `select` control\_type which indicates a select drop-down input field. The valid options in this drop-down are from the `objects` picklist - `Subscription`, `Customer` and `Plans`.

![config-select](/assets/config-select.DXp9Uwxx.png)_Config fields look like input fields to the user_

## Step 3 - Define input\_fields

With config\_fields defined, we can now utilize the `config_fields` argument passed to the `input_fields` lambda function. We can reference the input given for the Object input drop-down from this argument and route it to the proper object\_definition.

```ruby
  input_fields: lambda do |object_definitions, connection, config_fields|
    object = config_fields['object']

    object_definitions[object]
  end,
```

For example, if the user selects the `Customer` input in the drop-down, the `input_fields` key would call the `object_definition['customer']`.

```ruby
  object_definitions: {
    customer: {
      fields: lambda do |connection, config_fields, object_definitions|
        get("/api/v2/customers", limit: 1).
          dig('list',0,'customer').
          map do |key, value|
            if value.is_a?(Integer)
              type = 'integer'
              control_type = 'number'
            else
              type = 'string'
              control_type = 'text'
            end

            {
              name: key,
              label: key.labelize,
              type: type,
              control_type: control_type,
              sticky: true
            }
          end
      end
    }
  },
```

The `object_definition['customer']` key sends a secondary request to Chargebee and transforms the response into [Workato Schema](/en/developing-connectors/sdk/sdk-reference/schema).

![config-select](/assets/input-fields-dynamics.DpHoq0lL.gif)_Selecting customers creates additional fields_

## Step 4 - Defining the execute key

The execute key tells Workato the endpoint to send the request to and which HTTP request method to use. Different objects usually require posting to different endpoints. Extract the config field value from the `input` hash before you send the request to the API.

```ruby
  execute: lambda do |connection, input|
    object = input.delete('object')

    # Route to the appropriate endpoint based on selected object
    endpoint = case object
    when 'customer'
      '/api/v2/customers'
    when 'subscription'
      '/api/v2/subscriptions'
    when 'plan'
      '/api/v2/plans'
    else
      raise "Unsupported object type: #{object}"
    end

    post(endpoint, input).
      request_format_www_form_urlencoded
  end,
```

In this example:

- We extract the selected object using `input.delete('object')`, which returns the value and removes it from the input hash
- We use a `case` statement to map each object type to its corresponding API endpoint
- We construct the appropriate POST request to the endpoint for the selected object
- Chargebee requires the input to be form urlencoded so we use `.request_format_www_form_urlencoded`

> **USE STRING INTERPOLATION TO SIMPLIFY ROUTING**
> 
> You can simplify routing with string interpolation when your API endpoints follow a consistent pattern (such as `/api/v2/{object}s`):
> 
> ```ruby
> execute: lambda do |connection, input|
>   object = input.delete('object')
> 
>   post("/api/v2/#{object}s", input).
>     request_format_www_form_urlencoded
> end,
> ```
> 
> Use the explicit `case` statement approach shown in the preceding example when endpoint paths vary or require additional logic.

## Step 5 - Defining output fields

For the output fields, we use the same logic as step 3 to generate the output fields.

```ruby
  output_fields: lambda do |object_definitions, connection, config_fields|
    object = config_fields['object']

    object_definitions[object]
  end
```

![config-select](/assets/output-fields-dynamics.Cyg1vBdk.gif)_Selecting customers creates additional fields_

> **Object definitions**
> 
> Note that `object_definitions` is passed in as an argument. Workato allows connector builders to supply the definitions of an object separately in the "object\_definitions" key. This key is used when the definitions of an object are large and/or can be dynamically obtained.
> 
> To know more about this, take a look at our [SDK reference](/en/developing-connectors/sdk/sdk-reference/object_definitions)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/advanced-connector-guide/introduction.md
description: >-
  Advanced guide to building robust, object-based connectors on the Workato SDK
  with a focus on usability and code quality.
---

# Workato advanced connector building guide

Here is a final guide that focuses on the usability and the code quality of a connector. We will be going through exercises that can help you plan out robust connectors as well as guidelines on writing connector code. At this point, we assume that you have read through the basics of connector building found in the [Connector SDK](/en/developing-connectors/sdk) documentation.

In this guide, we introduce the concept of object-based connectors, something that you should have seen before if you have used NetSuite, Salesforce, or numerous other connectors on Workato. Object-based connectors are ones that reduce the amount of clutter by allowing users to first select a verb such as “Create” or “Update” before selecting the object they want to create or update.

## What should I expect to gain from this guide?

This guide should help organize your thoughts around building connectors that are usable by a wide audience. While custom connectors could be used as a quick way for your team to connect to unsupported web APIs on Workato, this guide looks at a sustainable approach of connector building. Workato also allows users from our community to promote their custom connectors to become platform-wide connectors - ones that can be found and used by anyone on the platform.

If you're reading this guide to build a connector on Workato to your own web API, one great resource would be the [Google API design guide](https://cloud.google.com/apis/design/) which goes through resource-oriented API designs. Well built APIs greatly ease the connector building experience as well as integration experience for users of your application when creating recipes on Workato.

## Object-based connectors

You may find yourself wondering what object-based connectors are in the first place but before that we must first clarify what resources and procedures are in applications.

When looking at a cloud based application, we often see that most applications have several resources at their core. These resources hold data in structures that users of the application can interact with and appreciate. For example, a resource in a banking application could be a `Customer` which contains all relevant information to a customer in the bank.

On the other hand, applications also provide a whole host of other services beyond holding data in certain organized resources for their users. These processes that applications perform on resources in their systems also create large amounts of business value for their users. For example, a process in the same banking application could be a `Bank Transfer`. This process could also include certain validations such a checking the balance of each account as well as ensuring the atomicity of the operation.

When building connectors in Workato, we've found that object-based connectors can encompass **both** but often, we see that working with resources is often the foundation of a connector before moving on to specific processes.

In the next chapter, we will go through thought exercises that can better help you plan out your connectors.

## Share a completed connector

You can [upload your connector to the community library](/en/community-library/upload-connectors) to share it with other users. Sharing your connector can provide increased API adoption, more leads for your services, and greater exposure to integration use cases.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/advanced-connector-guide/connector-planning.md
description: >-
  Learn how to plan a Workato custom connector by mapping integration use cases
  to a minimum set of actions, triggers, and objects.
---

# Connector planning

Before even beginning writing a single line of code, we highly recommend spending some time planning out all integration use cases for users of your custom connector on Workato. You’ll then be able to decompose them into the minimum set of actions and triggers in your connector to satisfy these use cases. This list of actions and triggers can be expanded in the future.

Often, we’ve seen that connectors that are the most successful needn’t be the ones with the most actions or triggers but ones that power a wide range of business use cases from a prudent set of actions and triggers. If you’re building a connector to your platform as a way for your customers to integrate your services with the hundreds in Workato’s ecosystem, we would recommend going through this process with both a product manager and a developer to ensure the needs of your customers are met.

## Detailing down your integration use cases

Connectors can start small and grow big over time but it's important to make sure that your connector can help you, your team or your customers find success in the integration use cases you have scouted out. This requires some time and effort thinking about how users would use your connector in recipes. First up, we highly recommend brainstorming to find out the exact use cases that you want to automate on Workato. For teams building connectors for internal use, this could be a tedious and manual process that you hope to automate. For teams building connectors on Workato to list on our platform so your customers can use Workato to include your application in their recipes, this should be something that you can foresee driving the most business value.

### Example 1:

As a developer from XYZ labs tasked to build a connector to Salesforce on Workato, my company sees ourselves manually importing new leads from Marketo daily into Salesforce and poor response times to new signups to our platform. Customer data and orders also have to be routinely exported from Salesforce into NetSuite, taking up a significant amount of the business analyst's team. Often, new deals also contain line items for products not present in NetSuite which are present in Salesforce.

To save time and lower the chance of human error, the integrations team has settled on 5 integration use cases to solve the problems above:

1. Notifying your sales team in Slack about new leads in Salesforce
2. Syncing account data in Salesforce with customers in NetSuite
3. Syncing orders in Salesforce with sales receipts in NetSuite
4. Creating leads in Salesforce when leads arrive through Marketo
5. Syncing products in Salesforce with products in NetSuite

### Example 2:

XYZ lab’s main product is a cloud accounting software (XYZ accounting) that allows their customers to access and manage their financial accounts over any device. In order to expand the functionality of the platform, reduce customer churn and find new leads, the product team in XYZ labs is also looking to build an XYZ accounting connector on Workato. Users of XYZ accounting would then be able to use this connector to automate any of the tedious processes of exporting or importing accounting data out or into XYZ accounting.

After assessing the most heavily used portions of XYZ accounting as well as the variety of apps that people may use XYZ accounting with, a set of integration use cases were shortlisted as ones that would drive the most value for XYZ accounting customers.

1. New closed-won opportunities in Salesforce create invoices in XYZ accounting
2. New products in Salesforce create new products in XYZ accounting
3. New payments in XYZ accounting update opportunities in Salesforce
4. New vendors in XYZ accounting create new suppliers in Salesforce
5. New approved expense reports in Expensify create an expense in XYZ accounting

## Defining your base set of objects

After deciding on what integration use cases you want to solve, this often translates into actions and triggers in a connector that we want to implement on certain objects.

As a start, we would recommend shortlisting 4 or 5 objects which you want to interact with through a recipe in Workato. For smaller applications, this could mean all objects. For large applications with over hundreds of objects, this could mean shortlisting 5 of them which meet your integration use cases. It's completely fine to keep your scope small and iterate over time.

### Example 3:

As an integration developer from XYZ labs, the integration use cases highlighted by the operations team revolves around multiple objects in Salesforce. Based on these use cases, it appears that support for `Orders`, `Leads`, `Accounts`, `Products` will allow my team to build the recipes they are looking for.

### Example 4:

As a developer tasked to build the connector to XYZ accounting, we can see that support should be prioritized for `Invoices`, `Products`, `Payments`, `Vendors` and `Expense reports`. When building a connector to your application for your customers, it's common to extend the number of objects supported when needed to ensure that a larger number of customers can use your connector beyond the use cases you have defined.

## Exploring possible actions

After you’ve decided on the objects, you now need to decide on what actions to support for your chosen objects. In most cases, we’ve found that starting with basic “Create”, “Read”, “Update”, “Delete” and “Search” (CRUDS) actions for your chosen objects cover most integration needs - especially when combined used together in recipes. Sometimes, we have seen users forgo “Delete” actions in cases as the deletion of data via an automated recipe might be undesirable.

Another possible type of action to support would be batch actions. Batch actions are actions that work with more than a single object but multiple ones and are often used in scenarios where multiple objects need to be synced in and out of an application. Consider if your users need this functionality to fulfill a core use case or if this can functionality added on later.

Another misstep that we often see with new users of Workato would be to overcomplicate actions. By keeping actions simple and focused on handling one single thing, it makes recipes for your user’s easier to troubleshoot when errors do occur. For example, instead of creating an action - “Create a customer and attach the invoice to a customer”, this should be broken down into 2 actions - “Create a customer” and “Attach invoice”. This decoupling of actions makes them more general and allows your users to mix and match actions to achieve more.

> **API ACTION LIMITATIONS**
> 
> Be aware of the functionalities and limitations of the API you plan to build a connector for.
> 
> Most well-designed APIs have endpoints to perform CRUD actions, and some also offer batch endpoints to support high-volume use cases.

## Exploring possible triggers

Besides actions, we also recommend implementing object-based triggers to allow end-users of your user to trigger off events in your application. While Workato supports 3 types of triggers (polling, static webhooks and dynamic webhooks), it's often enough to implement a single type of trigger based on your integration use cases.

When deciding between polling triggers or webhook triggers, it's important to focus on how quickly your end-users would need to get their hands on new events. In time-sensitive situations - such as when a user requests for assistance on your website, webhooks might be the most appropriate to build recipes around to send help their way quickly. On the other hand, new sales in your CRM might not need to have webhook triggers where polling triggers might suffice.

> **API TRIGGER LIMITATIONS**
> 
> Be aware of the functionalities and limitations of the API you plan to build a connector for.
> 
> Some APIs support webhook functionality. When webhooks are not available, [polling triggers](/en/developing-connectors/sdk/guides/building-triggers/poll) can be a good alternative. If you are developing a connector for your own application, consider whether it should support webhook triggers.

For polling triggers, we often start with the basics such as triggers when objects are created or when objects created or updated.

## Exploring other actions/triggers that should be included or highlighted

For some applications, there may some special actions that aren’t included in your current shortlist of object-based actions and triggers. Review all integration use cases you and your team have set up to accomplish and take stock of any gaps in actions or triggers.

A great exercise would be to envision building recipes around the integration use cases you hope to accomplish and scout out any actions that may be missing. What we have found useful in Workato would be to draw a simple skeleton of the recipes that are needed to accomplish the use case.

### Example 5:

As the developer at XYZ labs building the XYZ connector on Workato, another important integration use case for our customers was the ability to use XYZ's integrated bank transfer functionality from a workplace messaging app like Slack. When drawing out the skeleton of the integration, we arrived at these steps:

| Recipe: New command on Slackbot executes bank transfer on XYZ accounting | Action supported? |
| --- | --- |
| Trigger: New “Post bank transfer” command on Slack | Yes |
| 1\. Search for a supplier on XYZ accounting | Yes |
| 2\. Execute bank transfer on XYZ accounting using supplier ID | No |
| 3\. Post reply on Slack to notify user | Yes |

Using this skeleton, it’s easy to see that we’ve missed out on an “Execute bank transfer” action which would be critical in this use case.

> **CONNECTOR BUILDING IS AN ADVANCED FEATURE**
> 
> Workato recommends gaining experience with recipe building before creating a custom connector. Refer to the [Getting started](/en/getting-started) guide to learn the basics, or explore the [Use cases](/en/getting-started/workato-use-cases) page for step-by-step walkthroughs of example recipes.

## Taking stock of your connector

By the end of this exercise, you should have a list of actions and triggers that you plan to build. When placed into a table format, it should look something similar to this:

|  | New/updated trigger | Create action | Retrieve action | Update action | Delete action | Search action | Execute action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Invoices | Yes | Yes | Yes | Yes | Yes | Yes |  |
| Products | Yes | Yes | Yes | Yes | Yes | Yes |  |
| Payments | Yes | Yes | Yes | Yes | Yes | Yes |  |
| Vendors | Yes | Yes | Yes | Yes | Yes | Yes |  |
| Expense reports | Yes | Yes | Yes | Yes | Yes | Yes |  |
| Bank Transfer | Yes |  | Yes |  |  | Yes | Yes |

### Connector building time

Now that you've sussed out what your connector generally looks like, its time to get building! The next chapter will go through how to organize and build your connector.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/advanced-connector-guide/connector-building-defining-schema.md
description: >-
  Learn how to organize and define object schema in a Workato SDK connector to
  keep code reusable and add new objects quickly.
---

# Connector building - Defining schema for your objects

In this next section, we go through our current thoughts on how to organize your connector. With this methodology and proper planning, you’ll find it easy to add support for new objects in your connector whilst keeping your code DRY through the use of our object definitions and methods fields. These are all guidelines from learnings that integration developers at Workato have learned over time and may alter slightly based on the application and API that we connect to.

This assumes you have already read all previous documentation about the functionality of the Workato SDK including advanced topics and have already defined and established a connection to the target application. In case you haven’t done so, we highly recommend you do so.

> **DATA FORMATS**
> 
> The following examples assume you're connecting to an API that accepts JSON. However, the same approach can be applied to APIs that accept other data formats.

Before going into specifics, here is a high-level overview of connector code could be organized.

![Mindmap of connector code](/assets/structure.D1G9f5IH.png)

Our main objective is to allow users of the connector to allow them to first select from a series of actions or triggers like:

1. New/updated object
2. New object
3. Create object
4. Update object
5. Search objects
6. Delete object

This would be followed by the user selecting the object in the action or trigger configuration. After the user selects the object, the connector should fetch and display the input and output fields relevant to the object selected. This is by calling the appropriate object\_definition based on the user's input to your `config_fields`. The user's input to your `config_field` can be found in the arguments passed to the `input_fields` lambda function.

For the execute block, we advise using a single method dedicated for each verb-object pair. This helps to ensure that any pre-processing of input data and post-processing of response data specific to that verb-object action can have a dedicated section in your code. Any general data formatting such as `after_error_response` or `after_response` methods can be contained directly in the execute block.

Ultimately, this helps to separate the responsibilities of each verb action and the objects it can support, allowing you to add support for new objects quickly or verb actions for existing objects.

## Defining the schema of objects

Before writing the code for any actions or triggers, a good practice is to explore the API documentation. Often we find that the payloads expected in requests and responses dealing with a specific object have very similar structures.

This creates great synergy for code reuse as the same schema definition could potentially be used across various actions. For example, in the case of XYZ accounting, the same invoice schema definition could be used for “Create”, “Read”, “Update”, “Delete” and “Search” actions. Below, we will go through how various patterns in defining schema and where to place it in your connector code so that it can be easily referenced.

The schema for input and output fields can be determined both dynamically and statically in Workato. Find out more about [object definitions.](/en/developing-connectors/sdk/sdk-reference/object_definitions) This largely depends on whether the API you are building a connector to has metadata endpoints available. Below, we first go through examples of how to define schema manually through examples before showing you an example of a dynamically defined input schema.

> **SCHEMA DEFINITION**
> 
> A schema definition configures the properties of an object. The properties are rendered as input fields when used in `input_fields` and as output datapills in follow-up actions when used in `output_fields`.

Consider using a collapsible section for these code blocks. The sheer length makes it difficult to navigate the document.

### Example 1: Statically defined schema

As a developer building the connector to XYZ labs, the representation of an “Invoice” object in our application might look something like this:

```json
  {
    "TxnDate": "2019-09-19",
    "ID": "1",
    "TotalAmt": 362.07,
    "Line": [
      {
        "Description": "Rock Fountain",
        "SalesItemLineDetail": {
          "Qty": 1,
          "UnitPrice": 275
        },
        "Line-Num": 1,
        "Amount": 275.0,
        "Id": "1"
      },
      {
        "Description": "Fountain Pump",
        "SalesItemLineDetail": {
          "Qty": 1,
          "UnitPrice": 12.75
        },
        "LineNum": 2,
        "Amount": 12.75,
        "Id": "2"
      }
    ],
    "DueDate": "2019-10-19",
    "DocNumber": "1037",
    "Deposit": 0,
    "Balance": 362.07,
    "CustomerRef": {
      "name": "Sonnenschein Family Store",
      "value": "24"
    },
    "BillEmail": {
      "Address": "Familiystore@intuit.com"
    },
    "BillAddr": {
      "Line1": "Russ Sonnenschein",
      "Long": "-122.1141681",
      "Lat": "37.4238562",
      "Id": "95"
    },
    "MetaData": {
      "CreateTime": "2014-09-19T13:16:17-07:00",
      "LastUpdatedTime": "2014-09-19T13:16:17-07:00"
    }
  }
```

While a create “Invoice” action may require a POST request similar to this:

```
  POST /invoice/create
  Content type:application/json

  {
    "Line": [
      {
        "Description": "Fountain straws",
        "SalesItemLineDetail": {
          "Qty": 100,
          "UnitPrice": 0.075,
        },
        "Line-Num": 1,
        "Amount": 7.50,
        "Id": "192 "
      },
    ],
    "CustomerRef": {
      "value": "1"
    }
  }
```

and an update “Invoice” action may require a POST similar to this:

```
  POST /invoice/update
  Content type:application/json

  {
    "ID": "1",
    "Line": [
      {
        "Description": "Fountain straws",
        "SalesItemLineDetail": {
          "Qty": 100,
          "UnitPrice": 0.075,
        },
        "Line-Num": 1,
        "Amount": 7.50,
        "Id": "192 "
      },
    ],
    "CustomerRef": {
      "value": "1"
    }
  }
```

As a general rule of thumb, when defining schema of an object in Workato, we want to be able to reuse as much of it as possible across different actions (such as create invoice and update invoice actions). As such, the schema we define should be a superset of all the possible parameters for this “Invoice” object. We should arrive at something like the following:

```ruby
  object_definitions: {
    invoice: lambda do |connection, config_fields|
      [
        { name: "Id" },
        { name: "TxnDate" },
        { name: "TotalAmt", type: "number" },
        {
          name: "Line",
          type: "array",
          of: "object",
          properties: [
            { name: "Description" },
            {
              name: "SalesItemLineDetail",
              type: "object",
              properties: [
                { name: "Qty", type: "number" },
                { name: "UnitPrice", type: "number" }
              ]
            },
            { name: "Line-Num", type: "number" },
            { name: "Amount", type: "number" },
            { name: "Id" }
          ]
        },
        { name: "Due-Date" },
        { name: "Doc Number" },
        { name: "Deposit", type: "number" },
        { name: "Balance", type: "number" },
        {
          name: "CustomerRef",
          type: "object",
          properties: [
            { name: "name" }
            { name: "value" }
          ]
        },
        {
          name: "BillEmail",
          type: "object",
          properties: [
            { name: "Address" }
          ]
        },
        {
          name: "BillAddr",
          type: "object",
          properties: [
            { name: "Line1" },
            { name: "Lon" },
            { name: "Lat" },
            { name: "Id" }
          ]
        },
        {
          name: "MetaData",
          type: "object",
          properties: [
            { name: "CreateTime", type: "date_time" },
            { name: "LastUpdatedTime", type: "date_time" }
          ]
        }
      ]
    end
  }
```

This schema is contained inside an `object_definition` called `invoice`.

For example, since creating an invoice shouldn't allow users to define the ID in cases where invoice IDs are auto-generated by XYZ accounting, this can be easily stripped from the input schema later on.

### Example 2: Dynamically defined schema

In most cases, we highly recommend using metadata endpoints whenever available to generate input and output fields instead of manually defining them. This reduces the number of enhancements you would need to make if the base object had new fields added and also allows you to add support for custom fields if the application supports it. For this example, we will be using [HubSpot](https://www.hubspot.com) which has metadata endpoints that describe the properties of “Contact” objects over [here.](https://developers.hubspot.com/docs/methods/contacts/v2/get_contacts_properties)

In cases like these, we want to make a request to this endpoint and use the response to build the input and output schema in a format Workato understands. Below we have a sample response from HubSpot’s metadata endpoint which gives us an array of JSON objects, each representing a “Contact” property.

```js
[
  {
    "name": "example_property_name",
    "label": "Example Property Name",
    "description": "Example Description of the property",
    "groupName": "contactinformation",
    "type": "string",
    "fieldType": "text",
    "options": [
      // if property is a drop-down, all options are detailed here
    ],
    "deleted": false,
    "displayOrder": -1,
    "readOnlyValue": false,
    "readOnlyDefinition": false,
    "hidden": false,
    "mutableDefinitionNotDeletable": false,
    "favorited": false,
    "favoritedOrder": -1,
    "calculated": false,
    "externalOptions": false,
    "displayMode": "current_value",
    "formField": true
  },
  // More properties below
]
```

Using this, we can define a method called `contact_schema` which takes in the same `action_type` argument as our earlier example on static definitions.

```ruby
  object_definitions: {
    contact: lambda do |connection, config_fields|
      get('/properties/v1/contacts/properties').map do |property|
        field = {
          name: property['name'],
          label: property['label'],
          hint: property['description'],
          type: call('type_mapping', property['type']),
          control_type: call('control_type_mapping', property['fieldType'])
        }

        if %w[select multiselect].include?(field[:control_type])
          picklist = {
            pick_list: property['options'].
            map { |option| [option['label'], option['value']]  }
          }
          field = field.merge(picklist)
        end

        if %w[boolean select multiselect].include?(field[:control_type])
          togglefield = {
            toggle_hint: 'Select manually',
            toggle_field: {
              name: property['name'],
              label: property['label'],
              type: 'string',
              control_type: 'text',
              toggle_hint: 'Map datapill',
              hint: "Enter in a valid option"
            }
          }
          field = field.merge(togglefield)
        end

        field
      end
    end,
  },

methods: {
    type_mapping: lambda do |input|
      case input
      when 'datetime'
        'date_time'
      when 'number'
        'integer'
      when 'booleancheckbox'
        'boolean'
      when 'bool'
        'boolean'
      when 'enumeration'
        'string'
      else
        input
      end
    end,

    control_type_mapping: lambda do |input|
      case input
      when 'textarea'
        'text-area'
      when 'datetime'
        'date_time'
      when 'booleancheckbox'
        'checkbox'
      when 'bool'
        'checkbox'
      when 'enumeration'
        'select'
      when 'radio'
        'select'
      when 'checkbox'
        'multiselect'
      else
        input
      end
    end
  }
```

In this method, we take the response from HubSpot and for each property, we map its values to a defined parameter in Workato’s schema. We also created 2 service methods called `type_mapping` and `control_type_mapping` that are responsible for defining the mappings of HubSpot data types (defined as `type` and `fieldType` in HubSpot) to those in `type` and `control_type` in Workato respectively.

Another thing to note would be the introduction of picklists and toggle fields for `control_types` that support them. In general, we will highly recommend using picklists alongside with string toggle fields as this gives your end-users the ability to statically pick a value or map a datapill instead. More details on increasing usability can be found later on.

> **METADATA ENDPOINTS**
> 
> Workato strongly recommends using metadata endpoints when building a connector to your own API. This is especially important for applications with custom fields, as metadata endpoints allow you to generate input fields that are specific to a user’s instance.

### Building actions

Now that you've learned how to build schema for the base objects you've chosen, its time to start building your first actions using these methods you've just defined.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/advanced-connector-guide/connector-building-building-actions.md
description: >-
  Build object-based actions for a Workato SDK connector using config fields,
  picklists, and reusable schema methods.
---

# Connector building - Building actions

Now that we’ve defined objects schema in methods, we can now start building out our CRUDS actions which will reference the schema methods we have just defined.

## Defining config fields

When dealing with object-based actions, we first need to define something called configuration fields. [Configuration fields](/en/developing-connectors/sdk/sdk-reference/actions#config-fields) are special input fields that you can define whose answers can dynamically generate other input fields.

```ruby
config_fields: [
  {
    name: 'object',
    optional: false,
    label: 'Object type',
    control_type: 'select',
    pick_list: 'object_list_create',
    hint: 'Select the object type from picklist.'
  }
],
```

![Config fields](/assets/config_fields.BiCb-coL.gif)_Selecting invoice causes invoice related input fields to appear_

Here we also introduce a [picklist](/en/developing-connectors/sdk/sdk-reference/picklists) which we can easily add additional objects as we introduce support for them.

> **DYNAMIC INPUT FIELDS**
> 
> You can also use configuration fields to dynamically generate input fields based on the user's selections. Refer to the [Defining input fields](#defining-input-fields) section for scenarios where the selected object requires additional information before accurate input fields can be displayed.

## Defining your title, subtitle, description, and help text

It is also highly recommended and really important to define helpful titles and descriptions for your actions. When dealing with object-based actions, this helps with the readability of recipes using your connector as well as improves user experience for those building recipes with your connector.

```ruby
actions: {
  create_object: {
    title: 'Create object',

    subtitle: 'Supports the creation of invoices, payments, and customers',

    description: lambda do |input, picklist_label|
      "Create a <span class='provider'>" \
      "#{picklist_label['object'] || 'object'}</span> in " \
      "<span class='provider'>XYZ Accounting</span>"
    end,

    help: lambda do |input, picklist_label|
      "Creates an #{picklist_label['object'] || 'object'} in XYZ. First, select from a list of " \
      'objects that we currently support. After selecting your object,' \
      ' dynamic input fields specific to the object selected ' \
      'will be populated.'
    end,

    config_fields: [
      {
        name: 'object',
        optional: false,
        label: 'Object type',
        control_type: 'select',
        pick_list: 'object_list_create',
        hint: 'Select the object type from picklist.'
      }
    ],
    # More code truncated here
  }
}
```

Over here we define title and subtitles to give users an idea of the action out of all the different actions in your connector. Remember to keep your title concise whilst using subtitles to provide a bit more information.

For descriptions, we allow you to use a lambda function (as shown in the example above) to dynamically change the description of the action when a user makes a selection in the config\_field. The same can be done for help text as shown in the example above.

![Bad example of dynamic descriptions](/assets/dynamic-description-1.CfR1Me_n.png)_Bad example with no dynamic description_

![Good example of dynamic descriptions](/assets/dynamic-description-2.DhvLWrIN.png)_Good example with dynamic description_

## Defining input fields

Another feature of creating clean and scalable input fields are that a single action can support multiple objects with a single `object_definitions` call. Since the value of configuration fields can only be accessed through an object\_definitions method, we suggest calling a generic object\_definitions that can later pull the appropriate schema based on the object the user has selected.

### Input

```ruby
input_fields: lambda do |object_definitions, connection, config_fields|

  object = config_fields['object']

  input_schema = object_definitions[object] # If user select invoice, evaluates to object_definitions['invoice']

  case object
  when 'invoice'
    input_schema.where('name !=': 'Id')
  else
    input_schema
  end
end,
```

### Object definition

```ruby
  object_definitions: {
    invoice: lambda do |connection, config_fields, object_definitions|
      [
        { name: "Id" },
        { name: "TxnDate" },
        { name: "TotalAmt", type: "number" },
        {
          name: "Line",
          type: "array",
          of: "object",
          properties: [
            { name: "Description" },
            {
              name: "SalesItemLineDetail",
              type: "object",
              properties: [
                { name: "Qty", type: "number" },
                { name: "UnitPrice", type: "number" }
              ]
            },
            { name: "Line-Num", type: "number" },
            { name: "Amount", type: "number" },
            { name: "Id" }
          ]
        },
        # More schema
      ]
    end
  }
```

When the object definition `invoice` is called, the schema relevant to the invoice is returned. In the `input_fields`, we then conditionally filter out the `id` field as it is not applicable to the creation of an invoice and should not be shown.

## Defining the execute block

When defining the execute block, we first store any generic methods for pre processing or post processing of data in the execute block. In the example below, use to generic methods that format payloads before being sent out the target API. After the formatting of the payload, a call is then made to a method which houses any specific data processing that needs to be done on a `action`\-`object` level as well as the final HTTP call to the appropriate endpoint.

Error handling surfaces relevant error messages, saving users significant time during recipe design and debugging.

> **ACTION TIMEOUT**
> 
> SDK actions have a 180-second [timeout](/en/recipes/recipe-job-errors#timeouts) limit.
> 
> You can use the `checkpoint!` method with file streaming actions to transfer files that exceed the timeout limit. Refer to the [Using our multistep framework to extend upload times](/en/developing-connectors/sdk/guides/building-actions/streaming/upload-stream-chunk-id#using-our-multistep-framework-to-extend-upload-times) section for additional information.

### Execute block

```ruby
execute: lambda do |connection,input|
  object_name = input.delete('object')

  response = call('create_#{object_name}_execute', payload).
              after_error_response(/.*/) do |_code, body, _header, message|
                error("#{message}: #{body}")
              end

  formatted_response
end,
```

### `action`\-`object` method

```ruby
create_invoice_execute: lambda do |payload|
  post('api/invoice/create', payload)
end,
```

## Defining the output fields

Output fields can be defined in the same way as input fields using the same schema method used earlier. When calling the schema method, remember to pass the parameter `output` so your method knows to return fields expected in the response. Often this includes metadata about the object that cannot be changed by users such as `created_at` or `updated_at` timestamps.

### Output

```ruby
output_fields: lambda do |object_definitions, connection, config_fields|
  object = config_fields['object']

  input_schema = object_definitions[object] # If user select invoice, evaluates to object_definitions['invoice']
end,
```

No further manipulation is needed as the invoice schema contained in `object_definition['invoice']` matches the fields returned from the API exactly.

## Example 1: Update invoice action in XYZ Accounting

Below, we go through one full example for an update object action in XYZ accounting.

### Sample code

```ruby
methods: {
  update_invoice_execute: lambda do |payload|
    patch('api/invoice/update', payload)
  end,

},

object_definitions: {

  invoice: {
    fields: lambda do |connection, config_fields, object_definitions|
      # same schema as above
    end
  },

},
actions: {

  update_object: {
    title: 'Update object',

    subtitle: 'Updates an object in XYZ accounting.',

    description: lambda do |input, picklist_label|
      "Update a <span class='provider'>" \
      "#{picklist_label['object'] || 'object'}</span> in " \
      "<span class='provider'>XYZ Accounting</span>"
    end,

    help: lambda do |input, picklist_label|
      {
        body:
        "Updates an #{picklist_label['object'] || 'object'} in XYZ. First, select from a list of " \
        'objects that we currently support. After selecting your object,' \
        ' dynamic input fields specific to the object selected ' \
        'will be populated.'
      }
    end,

    config_fields: [
      {
        name: 'object',
        optional: false,
        label: 'Object type',
        control_type: 'select',
        pick_list: 'object_list_update',
        hint: 'Select the object type from picklist.'
      }
    ],

    input_fields: lambda do |object_definitions, connection, config_fields|
      object = config_fields['object']

      input_schema = object_definitions[object]
    end,

    execute: lambda do |connection,input|
      object_name = input.delete('object')

      response = call('update_#{object_name}_execute', payload).
                  after_error_response(/.*/) do |_code, body, _header, message|
                    error("#{message}: #{body}")
                  end

      response
    end,

    output_fields: lambda do |object_definitions, connection, config_fields|
      object = config_fields['object']

      input_schema = object_definitions[object]
    end,

    sample_output: lambda do |connection, input|
      payload = {
        "limit" => 1,
        "status" => "closed"
      }
      call("search_#{input['object']}_execute", payload)
    end

  }
  # More actions below
},

pick_lists: {
  object_list_update: lambda do
    [
      ["Invoice","invoice"]
    ]
  end,
  # More picklists below
}
```

The example below showcases all the different steps needed to create an update object action. Currently this code only shows support for a single object - `Invoices`. The structure for the update object action is largely identical to that of the create object action where configuration fields, titles, subtitles, descriptions, help text, input fields, output fields, execute, and sample output blocks are defined generically. Most of the magic happens in object definitions and methods where object-specific code is introduced to retrieve specific schema and make HTTP calls to endpoints related to that object.

### Building triggers

Lets move on to learning about building object based triggers.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/advanced-connector-guide/connector-building-building-triggers.md
description: >-
  Build an object-based polling trigger for a Workato SDK connector using config
  fields, a poll block, dedup, and reusable schema methods.
---

# Connector building - Building triggers

Building triggers follow almost the same format as actions. To make them object based, we'll be making use of configuration fields as well as the schema methods we defined earlier. Below, we go through an example of a polling trigger. Do take note there are some differences in the blocks expected when creating a polling trigger, dynamic webhook trigger and a static webhook trigger.

## Defining config fields

When dealing with object-based triggers, we first need to define something called a configuration fields. [Configuration fields](/en/developing-connectors/sdk/sdk-reference/triggers#config-fields) are special input fields that you can define whose answers can dynamically generate other input fields. Since triggers don't often need any additional input fields, this configuration field is used to dynamically generate the expected output of this trigger.

```ruby
config_fields: [
  {
    name: 'object',
    optional: false,
    label: 'Object type',
    control_type: 'select',
    pick_list: 'object_list_new_updated_trigger',
    hint: 'Select the object type from picklist.'
  }
],
```

![Config fields](/assets/config_fields-trigger.DeRtsn-k.gif)_Selecting invoice causes invoice related data-pills to appear_

Here we also introduce a [picklist](/en/developing-connectors/sdk/sdk-reference/picklists) which we can easily add additional objects as we introduce support for them.

> **DYNAMIC INPUT FIELDS**
> 
> You can also use configuration fields to dynamically generate input fields based on the user's selections. Refer to the [Defining input fields](#defining-input-fields) section for scenarios where the selected object requires additional information before accurate input fields can be displayed.

## Defining your title, subtitle, description, and help text

It is also highly recommended and really important to define helpful titles and descriptions for your actions. When dealing with object-based actions, this helps with the readability of recipes using your connector as well as improves user experience for those building recipes with your connector.

```ruby
triggers: {

  new_updated_object: {

    title: "New/updated object",

    subtitle: "Triggers when an object is created or updated",

    description: lambda do |input, picklist_label|
      "New/updated <span class='provider'>" \
      "#{picklist_label['object'] || 'object'}</span> in " \
      "<span class='provider'>XYZ Accounting</span>"
    end,

    help: lambda do |input, picklist_label|
      {
        body:
        "Triggers when an #{picklist_label['object'] || 'object'} is created " \
        ' or updated in XYZ.'
      }
    end,

    config_fields: [
      {
        name: 'object',
        optional: false,
        label: 'Object type',
        control_type: 'select',
        pick_list: 'object_list_new_updated_trigger',
        hint: 'Select the object type from picklist.'
      }
    ],
  }
}
```

Over here we define title and subtitles to give users an idea of the action out of all the different actions in your connector. Remember to keep your title concise whilst using subtitles to provide a bit more information.

For descriptions, we allow you to use a lambda function (as shown in the example above) to dynamically change the description of the action when a user makes a selection in the config\_field. The same can be done for help text as shown in the example above.

![Bad example of dynamic descriptions](/assets/dynamic-description-1.CfR1Me_n.png)_Bad example with no dynamic description_

![Good example of dynamic descriptions](/assets/dynamic-description-2.DhvLWrIN.png)_Good example with dynamic description_

## Defining input fields

Since triggers do not need much configuration from the user, there is no need for any object definitions to be called in our example here. One pattern that we do recommend in triggers whenever possible is to add an optional input field so users can retrospectively pull data when the trigger is first started. This input field will take in a timestamp value and use that to pull any data.

### Input

```ruby
input_fields: lambda do
  [
    {
      name: 'since',
      label: 'When first started, this recipe should pick up events from',
      type: 'timestamp',
      optional: true,
      hint: 'When you start recipe for the first time, it picks up Salesforce records ' \
      'from this specified date and time. Once recipe has been run or tested, ' \
      'value cannot be changed.'
    }
  ]
end,
```

## Defining the poll block

For polling triggers, the poll block is where the code for each poll is executed. There are numerous arguments that can be used in the poll block including a `closure` argument which allows you to reference any data from a previous poll. This closure value is useful by allowing your trigger to store a cursor on where it last polled. Often, closure stores timestamp values of when the last record it saw as well as any offsets if it needs to poll immediately.

> **POLLING TRIGGER BEST PRACTICES**
> 
> When building polling triggers, we recommend that you use endpoints that return a list of records and support query parameters for filtering records by timestamp. Refer to Greenhouse's [Get list candidates](https://developers.greenhouse.io/harvest.html#get-list-candidates) API documentation as an example.

### Expected JSON response from XYZ accounting

```js
{
  "results": [
    {
      "TxnDate": "2019-09-19",
      "ID": "1",
      "TotalAmt": 362.07,
      "Line": [
        {
          "Description": "Rock Fountain",
          "SalesItemLineDetail": {
            "Qty": 1,
            "UnitPrice": 275,
          },
          "Line-Num": 1,
          "Amount": 275.0,
          "Id": "1"
        },
        {
          "Description": "Fountain Pump",
          "SalesItemLineDetail": {
            "Qty": 1,
            "UnitPrice": 12.75,
          },
          "LineNum": 2,
          "Amount": 12.75,
          "Id": "2"
        }
      ],
      "DueDate": "2019-10-19",
      "DocNumber": "1037",
      "Deposit": 0,
      "Balance": 362.07,
      "CustomerRef": {
        "name": "Sonnenschein Family Store",
        "value": "24"
      },
      "BillEmail": {
        "Address": "Familiystore@intuit.com"
      },
      "BillAddr": {
        "Line1": "Russ Sonnenschein",
        "Long": "-122.1141681",
        "Lat": "37.4238562",
        "Id": "95"
      },
      "MetaData": {
        "CreateTime": "2014-09-19T13:16:17-07:00",
        "LastUpdatedTime": "2014-09-19T13:16:17-07:00"
      }
    },
    // more results
  ],
  "more_results": true
}
```

### poll block

```ruby
poll: lambda do |connection, input, closure|
  limit = 100
  closure = closure || {}

  updated_since = (closure['last_updated_since'] || input['since']).to_time.utc.iso8601

  params = {
    "order_by" => "updated_at",
    "order_type" => "asc",
    "limit" => limit,
    "offset" => closure['offset'],
    "updated_since" => updated_since
  }

  response = call("trigger_#{input['object']}_poll", params)

  records = response['results']

  poll_again = response['more_results']

  if poll_again # If we can poll for more, update offset
    closure['offset'] =  closure['offset'] + limit
  else # If not, reset offset and last_updated_since
    closure['offset'] = 0
    closure['last_updated_since'] = records.last['MetaData']['LastUpdatedTime']
  end

  {
    events: records,
    next_poll: closure,
    can_poll_more: poll_again
  }
end,
```

In the poll block, we first prepare the payload with the appropriate parameters to query for only records after the last time we polled. This is done by referencing the closure values of the last poll.

The parameters are passed into an object-specific method to execute the poll and the response is expected to be the JSON response above. The closure values are reset based on response of the poll and the output of each poll block is a hash with 3 expected values - the records, the closure hash and "can\_poll\_more" - a boolean value which determines whether the trigger should poll again.

Refer to [Polling triggers](/en/developing-connectors/sdk/sdk-reference/triggers) for more information.

## Defining the dedup block

For each record in the array of records passed on from the poll block, Workato also checks to see if it has seen the record before. To do so, the dedup block should contain a string that combines various parts of a record to ensure that it is unique. In the example below, we've used the `invoice` id and `invoice` last updated timestamp to see if this updated record has been seen before.

```ruby
dedup: lambda do |record|
  "#{record['results']['Id']}@#{record['results']['MetaData']['LastUpdatedTime']}"
end,
```

## Defining the output fields

Output fields can be defined using the same schema method used earlier. When calling the schema method, remember to pass the parameter `output` so your method knows to return fields expected in the response. Often this includes metadata about the object that cannot be changed by users such as `created_at` or `updated_at` timestamps.

### Output

```ruby
    output_fields: lambda do |object_definitions, connection, config_fields|
      object = config_fields['object']

      input_schema = object_definitions[object]
    end,
```

### Object definition

```ruby
    invoice: {
      fields: lambda do |connection, config_fields, object_definitions|
        # same schema as above
      end
    },
```

## Defining your sample output

Sample outputs are a great way to hint to give users context about the data-pills they are mapping in downstream actions. When labels might still leave room for confusion, sample outputs bridge the gap in understanding by allowing you to pull data in real time from the user's own application. In the example below, we construct a payload artificially before using a search object method to retrieve the first record found in the user's own instance of XYZ accounting.

### Sample output

```ruby
sample_output: lambda do |connection, input|
  payload = {
    "limit" => 1
  }
  call("search_#{input['object']}_execute", payload)
end
```

The output of this block is then passed to the output fields block and rendered to the right of every data-pill which is matched. This could significantly reduce the amount of time it takes for users whilst troubleshooting.

![Good example of dynamic descriptions](/assets/sample_output.CSFX72XE.png)_Sample output renders in grey text next to each data-pill_

### Common code patterns & limitations

Now that you've seen some examples of how to build object-based actions and triggers, we now go through some code patterns which can be reused in your connector.

---
