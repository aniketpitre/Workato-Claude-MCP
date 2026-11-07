---
url: 'https://docs.workato.com/en/developing-connectors/sdk/sdk-reference/test.md'
description: >-
  Reference for the test lambda in the Workato connector SDK, which verifies
  that supplied credentials establish a valid connection.
---

# SDK Reference - `test`

This section enumerates all the possible keys available when testing your connection.

> **Quick Overview**
> 
> The `test` lambda tells your connector how to check if the connection is valid. After it has taken the input from the user and executed the `authorization` block, this test verifies that the credentials supplied are valid via a simple HTTP request.
> 
> The `test` lambda is executed when a connection a user first clicks connect. The only exception is for OAuth2 authorization code grant connections, where the connection is marked as connected when Workato has successfully exchanged the authorization code for access tokens.
> 
> The `test` lambda is also executed for all types of connections upon recipe start and job rerun to ensure that the connection's credentials are still valid.

## Structure

```ruby
    test: lambda do |connection|
      # see test: documentation for more information
    end
```

* * *

## `test`

| Attribute | Description |
| --- | --- |
| Key | `test` |
| Type | lambda function |
| Required | True |
| Description | A simple HTTP request that can verify that we have established a successful connection. This connection is marked as "Successful" when the HTTP response is 2XX. |

Example - test:

APIs normally provide an endpoint that returns information about the authenticated user. These endpoints are ideal for your connector to verify that connection has been established.

```ruby
    test: lambda do |connection|
      get('/api/v5/me')
    end
```

In cases where this is not available, you may also choose to use simple requests. Normally this could be to search for results in the target API. These requests should also allow you to verify that the connection is valid.

```ruby
    test: lambda do |connection|
      get("https://person.clearbit.com/v1/people/email/eeshansim@gmail.com")
    end
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/sdk-reference/custom-action.md
description: >-
  Reference for the custom_action key in the Workato connector SDK, used to let
  users build custom actions when no standard action exists.
---

# SDK Reference - `custom_action`

This section enumerates all the possible keys to define a custom action.

> **Quick Overview**
> 
> The `custom_action` key allows you to quickly define custom actions to unblock users of your connector when no standard action is available to them. Keep in mind that these actions require users to understand certain API concepts like how to find the relevant API endpoints and payload schema.

## Structure

```ruby
    custom_action: Boolean,

    custom_action_help: {
      learn_more_url: String,

      learn_more_text: String,

      body: String
    }
```

* * *

## `custom_action`

| Attribute | Description |
| --- | --- |
| Key | `custom_action` |
| Type | Boolean |
| Required | Optional. Defaults to false where no custom action is added to your connector. Set to true to add custom actions as an option for your users. |
| Description | This adds a custom action to your connector. |
| Expected Output | `Boolean` i.e. `true` |
| UI reference |  |

* * *

## `custom_action_help`

| Attribute | Description |
| --- | --- |
| Key | `custom_action_help` |
| Type | Hash |
| Required | Optional. If custom\_action is `true`, then this hash allows you to customize the help text in your action. |
| Description | Allows you to configure the help body, help button url and label. |
| Expected Output | `Hash` See below for more information |
| UI reference |  |

> **TIP**
> 
> Custom action help is important to guide users to the proper websites to collect information such as API documentation.

* * *

## `learn_more_url`

| Attribute | Description |
| --- | --- |
| Key | `learn_more_url` |
| Type | String |
| Required | Optional. |
| Description | Defines the URL to send users when they click on the help link in the custom action. |
| Expected Output | `'www.api-reference.com'` |

* * *

## `learn_more_text`

| Attribute | Description |
| --- | --- |
| Key | `learn_more_text` |
| Type | String |
| Required | Optional. |
| Description | The label for the hyperlink text in the help. |
| Expected Output | `'API documentation'` |

* * *

## `body`

| Attribute | Description |
| --- | --- |
| Key | `body` |
| Type | String |
| Required | Optional. |
| Description | The main help text body that appears above the learn more button. This body is HTML compatible. |
| Expected Output | `'<p>Build your own Chargebee action with a HTTP request. <b>The request will be authorized with your Chargebee Hana connection.</b></p>` |

---
