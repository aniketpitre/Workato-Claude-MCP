---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/import-via-oas/extending-oas-connector.md
description: >-
  Learn how to iterate on a connector generated from an OAS by adjusting
  connection fields, adding hints, and refining actions in the Workato SDK.
---

# Extending your OAS Generate connector

Connector generation is often just the beginning of your connector building journey. Below, you will find recommendations and guidelines on how to continue to iterate on your connector such as:

- [Adjusting your connection fields](#adjusting-your-connection-fields)
- [Adding a test API request](#adding-a-test-api-request)
- [Adjusting each action's title, help, and more](#adjusting-each-action-s-title-help-and-more)
- [Adjusting input/output fields of your actions](#adjusting-input-output-fields-of-your-actions)
- [Adding triggers](#adding-triggers)

> **TIP**
> 
> Many of the pointers below assume you have knowledge of Workato's Connector SDK framework. Where possible, links will be provided for relevant topics for further reading.

## Adjusting your connection fields

When generating a connector, you may find that fields in the connection - e.g. API keys - are not easy for users to find. We recommend adding hints to these fields to make it easier for users to understand how to find these credentials easily. This can be added to fields defined in the `:connection` hash under the `:fields` attribute. For example, the `hint` attribute can be added to each field and is HTML compatible to include links as well.

Sample generated code below with no hints for connection fields.

```ruby
  :connection         => {
    :authorization => {
      :type  => "api_key",
      :apply => lambda do |connection|
        headers(:"Ocp-Apim-Subscription-Key" => connection['Ocp-Apim-Subscription-Key'])
      end
    },
    :fields        => [
      {
        :name         => "Ocp-Apim-Subscription-Key",
        :label        => "API key",
        :control_type => "password",
        :optional     => false
      }
    ],
    :base_uri      => lambda do |connection|
      'https://api.mediavalet.com' + '/'
    end
  },
  :test               => lambda do
    true
  end,
```

Sample generated code below with hints for connection fields.

```ruby
  :connection         => {
    :authorization => {
      :type  => "api_key",
      :apply => lambda do |connection|
        headers(:"Ocp-Apim-Subscription-Key" => connection['Ocp-Apim-Subscription-Key'])
      end
    },
    :fields        => [
      {
        :name         => "Ocp-Apim-Subscription-Key",
        :label        => "API key",
        :control_type => "password",
        :hint         => "Find your API key <a href='www.example.com/api_key' target='_blank'>here</a>"
        :optional     => false
      }
    ],
    :base_uri      => lambda do |connection|
      'https://api.mediavalet.com' + '/'
    end
  },
  :test               => lambda do
    true
  end,
```

> **Further reading**
> 
> - [SDK reference for `connection`](/en/developing-connectors/sdk/sdk-reference/connection)
> - [Schema glossary](/en/developing-connectors/sdk/sdk-reference/schema)
> - [Guides for creating connections on Workato](/en/developing-connectors/sdk/guides/authentication)

## Adding a `test` API request

The [`test` lambda](/en/developing-connectors/sdk/sdk-reference/test) in a connector is meant to contain a simple API test that utilizes the user's given credentials and expects a 2XX HTTP response. This tells Workato that the user provided credentials are valid. When generating your connector however, you will find that your `test` lambda's output is statically set to a boolean `true` which may cause false positives when your user's give credentials.

Sample generated code below where `test` block is set to `true`.

```ruby
  :connection         => {
    :authorization => {
      :type  => "api_key",
      :apply => lambda do |connection|
        headers(:"Ocp-Apim-Subscription-Key" => connection['Ocp-Apim-Subscription-Key'])
      end
    },
    :fields        => [
      {
        :name         => "Ocp-Apim-Subscription-Key",
        :label        => "API key",
        :control_type => "password",
        :hint         => "Find your API key <a href='www.example.com/api_key' target='_blank'>here</a>"
        :optional     => false
      }
    ],
    :base_uri      => lambda do |connection|
      'https://api.mediavalet.com' + '/'
    end
  },
  :test               => lambda do
    true
  end,
```

To adjust your connector, you will need to find a simple API endpoint that doesn't need much user input as a test request. One common example may be an endpoint to retrieve a list of a specific record type and limiting the result set.

Sample generated code below where `test` block is set to a GET request to the `assets` endpoint to get a single result.

```ruby
  :connection         => {
    :authorization => {
      :type  => "api_key",
      :apply => lambda do |connection|
        headers(:"Ocp-Apim-Subscription-Key" => connection['Ocp-Apim-Subscription-Key'])
      end
    },
    :fields        => [
      {
        :name         => "Ocp-Apim-Subscription-Key",
        :label        => "API key",
        :control_type => "password",
        :hint         => "Find your API key <a href='www.example.com/api_key' target='_blank'>here</a>"
        :optional     => false
      }
    ],
    :base_uri      => lambda do |connection|
      'https://api.mediavalet.com' + '/'
    end
  },
  :test               => lambda do
    get('assets', top: 1)
  end,
```

You may use the debugger to continue to test your connection to ensure that it is working properly.

> **Further reading**
> 
> - [SDK reference for `test`](/en/developing-connectors/sdk/sdk-reference/test)
> - [Defining HTTP methods](/en/developing-connectors/sdk/sdk-reference/http)
> - [Using the debugger](/en/developing-connectors/sdk/guides/debugging)

## Adjusting each action's title, help, and more

Connectors should follow a specific nomenclature for their actions and triggers such as `Create Asset` or `Search Invoices`. This is described further in our [connector best practices](/en/developing-connectors/sdk/guides/best-practices#actions). However, when generating actions from an OAS, there is no guarantee that the action titles, subtitles, descriptions and help will follow our recommendations. It is the responsibility of the connector developer to ensure that these best practices are followed - to ensure a consistent experience for your end users.

Sample generated action

```ruby
  :Assets_AddAttributesToAsset                               => {
    :title         => "Create Asset Attributes",
    :subtitle      => "Create Asset Attributes in NextGen API",
    :help          => "Add attributes to an asset.",
    :input_fields  => lambda do |object_definitions|
      object_definitions['Assets_AddAttributesToAsset_input']
    end,
    :output_fields => lambda do |object_definitions|
      object_definitions['Assets_AddAttributesToAsset_200_output']
    end,
    :execute       => lambda do |connection, input, extended_input_schema|
      call(:Assets_AddAttributesToAsset_execute, connection, input, extended_input_schema)
    end
  },
```

For each action, you should take note of each `title`, `subtitle`, `help` attribute and adjust the values where appropriate. You may also add additional information to make it clearer for end users.

Sample generated acton with `subtitle` and `help` adjusted.

```ruby
  :Assets_AddAttributesToAsset                               => {
    :title         => "Create Asset Attributes",
    :subtitle      => "Creates an Asset Attributes e.g. MIME Type or Source",
    :help          => "Add attributes to an asset. You can add any attributes like MIME Type or Source of the asset for further classification of your assets.",
    :input_fields  => lambda do |object_definitions|
      object_definitions['Assets_AddAttributesToAsset_input']
    end,
    :output_fields => lambda do |object_definitions|
      object_definitions['Assets_AddAttributesToAsset_200_output']
    end,
    :execute       => lambda do |connection, input, extended_input_schema|
      call(:Assets_AddAttributesToAsset_execute, connection, input, extended_input_schema)
    end
  },
```

Find out more about [different attributes of an action](/en/developing-connectors/sdk/sdk-reference/actions).

> **Further reading**
> 
> - [SDK reference for `actions`](/en/developing-connectors/sdk/sdk-reference/actions)
> - [Best practices for actions](/en/developing-connectors/sdk/guides/best-practices#actions)
> - [Guides for creating actions on Workato](/en/developing-connectors/sdk/guides/building-actions)

## Adjusting input/output fields of your actions

There could be instances where your action's input and output fields are not exactly in the format you expect, such as minor tweaks to the labels given to these fields, or perhaps additional hints. You may find the schema for generated action within `object_definition` mentioned in the `input_fields` and `output_fields` lambdas of any action and to adjust the schema, you would simply need to change the Workato schema defined there.

For example, for a sample generated action

```ruby
  :Assets_AddAttributesToAsset                               => {
    :title         => "Create Asset Attributes",
    :subtitle      => "Create Asset Attributes in NextGen API",
    :help          => "Add attributes to an asset.",
    :input_fields  => lambda do |object_definitions|
      object_definitions['Assets_AddAttributesToAsset_input']
    end,
    :output_fields => lambda do |object_definitions|
      object_definitions['Assets_AddAttributesToAsset_200_output']
    end,
    :execute       => lambda do |connection, input, extended_input_schema|
      call(:Assets_AddAttributesToAsset_execute, connection, input, extended_input_schema)
    end
  },
```

You can find object\_definitions called `:Assets_AddAttributesToAsset_input` and `Assets_AddAttributesToAsset_200_output` which hold the Workato schema. Take note that object\_definitions can be used by multiple actions so one change may affect other recipes. You may also observe certain unfamiliar fields in the generated `Workato` schema such as `direction`, `location` and `original_name`. **Do not change or remove these attributes**.

> **Further reading**
> 
> - [SDK reference for `object_definitions`](/en/developing-connectors/sdk/sdk-reference/object_definitions)

## Adding triggers

There are no triggers when generating a connector but you can reuse existing components in your generated connector to create triggers. You may reuse the same `methods` and `object_definitions` generated for a similar "Search records" action to create these triggers. Alternatively, you may also build these triggers from scratch if needed.

> **Further reading**
> 
> - [SDK reference for `triggers`](/en/developing-connectors/sdk/sdk-reference/triggers)
> - [Best practices for triggers](/en/developing-connectors/sdk/guides/best-practices#triggers)
> - [Guides for creating actions on Workato](/en/developing-connectors/sdk/guides/building-triggers)
