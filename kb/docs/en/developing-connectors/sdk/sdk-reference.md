---
url: 'https://docs.workato.com/en/developing-connectors/sdk/sdk-reference.md'
description: >-
  Reference for the Workato connector SDK root keys, including connection,
  actions, triggers, object_definitions, methods, and streams.
---

# SDK Reference

This is the full list of all possible attributes that you can include in your Workato connector. This section is organized by the root keys of a connector:

- `connection` - Handles all aspects pertaining to how your connector should establish a connection with a target API.
- `test` - Works hand in hand with the `connection` key to verify that a connection has been successfully established.
- `actions` - Contains the definition of all actions in your connector.
- `triggers` - Contains the definition of all triggers in your connector.
- `object_definitions` - Define commonly used input or output fields and reference them later on in your actions and triggers.
- `pick_lists` - Used to generate drop-downs in input fields.
- `methods` - Create reusable methods which can be called from anywhere in your connector.
- `secure_tunnel` - Used to created OPA compatible connectors to communicate with on-premise systems.
- `webhook_keys` - Used in conjunction with Static webhook triggers.
- `streams` - Used in conjunction with actions and triggers to implement file streaming.

In addition to this, the SDK reference also contains the following information regarding

- Defining input and output fields
- Using HTTP Methods to send requests
- Available ruby methods that can be used in your connector code

## Sample Connector Skeleton

Each connector in Workato is a big hash that contains the root keys detailed above. Below, we have an example of a summarized connector. Not all keys are required.

```ruby
{
  title: 'My sample connector',

  connection: Hash,

  test: lambda do
    Boolean
  end,

  custom_action: Boolean,

  custom_action_help: Hash,

  actions: Hash,

  triggers: Hash,

  object_definitions: Hash,

  pick_lists: Hash,

  methods: Hash,

  secure_tunnel: Boolean,

  webhook_keys: lambda do
    String
  end,

  streams: Hash
}
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/sdk-reference/connection.md
description: >-
  Reference for the connection key in the Workato connector SDK, including
  fields, extended_fields, authorization, and base_uri.
---

# SDK Reference - `connection`

This section enumerates all the possible keys available when defining your connection.

> **Quick Overview**
> 
> To put it simply, the `connection` hash contains all the instructions your connector needs to establish a successful connection.
> 
> - The `fields` key tells your connector what input fields to show so it can collect information for authorization.
> - The `extended_fields` key allows you to dynamically show more connection fields based on previous inputs. This field is optional to define.
> - The `authorization` key tells your connector what to do with the information it has collected - use that to exchange it for an access\_token.
> - The `base_uri`key tells your connector what to prepend to every HTTP request after connection is successful. This allows you to use relative paths in your connector code when defining actions and triggers.

## Structure

```ruby
  connection: {
    fields: Array,

    extended_fields: lambda do |connection|
      Array
    end,

    authorization: Hash,

    base_uri: lambda do |connection|
      String
    end
  }
```

* * *

## fields

The 'fields' key has the following attributes:

<dl><dt>Key</dt><dd><code>fields</code></dd><dt>Type</dt><dd>Array</dd><dt>Required</dt><dd>False</dd><dt>Description</dt><dd>Accepts an array of hashes. Each hash in this array corresponds to a separate input field.<br>To learn how to define input fields in Workato, see <a href="/en/developing-connectors/sdk/sdk-reference/schema.html">SDK Reference - Schema</a>.</dd></dl>

### Picklists in connection fields

For fields with `control_type` defined as `select` or `multiselect`, use the `options` attribute to define a static picklist instead of the `pick_list` attribute.

> **Picklist does not apply to connection hash**
> 
> References to any picklists you defined in your connector are not accessible in the `connection` hash because no credentials have been received at this time.

### Example: Connection fields with picklist nested in advanced settings

```ruby
    fields: [
      {
        name: 'api_key',
        control_type: 'password',
        hint: 'You can find your API key final change3' \
          "under 'Settings'=>'Configure Chargebee'=>'API Keys and Webhooks'" \
          " in Chargebee's web console.",
        label: 'Your API Key',
        default: "helloaaaabbb",
        optional: false
      },
      {
        name: 'domain',
        control_type: 'subdomain',
        url: 'chargebee.com'
      },
      {
        name: "advanced_settings",
        type: "object",
        optional: "true",
        properties: [
          {
            name: "environment",
            optional: true,
            control_type: "select",
            options: [
              ["Development", "dev"],
              ["Production", "prod"]
            ]
          }
        ]
      }
    ],
```

* * *

## extended\_fields

The 'extended\_fields' key has the following attributes:

<dl><dt>Key</dt><dd><code>extended_fields</code></dd><dt>Type</dt><dd>lambda function</dd><dt>Required</dt><dd>False</dd><dt>Description</dt><dd>Allows you to optionally display more input fields based on your connection. The output is expected to be a valid Workato schema. Find out more about <a href="/en/developing-connectors/sdk/sdk-reference/schema.html">SDK Reference - Schema</a>.</dd></dl>

### How to use extended\_fields

With `extended_fields`, you can dynamically display additional fields based on previous input fields. If your connection setup is complex and consists of many input fields, consider limiting the number of fields that a user can see. Instead of displaying all fields at the same time, use `extended_fields` to control how many fields to display to the user initially, and when to display additional fields.

In this case, `extended_fields` provides you with the added benefit of controlling which fields to display for the users during connection setup, and guiding them through the experience. In some cases, you may also restrict some fields from the display when they are not relevant.

### Example: Connection fields with extended\_fields

```ruby
    fields: [
      {
        name: "api_key",
        control_type: "password",
        hint: "You can find your API key " \
          "under 'Settings'=>'Configure Chargebee'=>'API Keys and Webhooks'" \
          " in Chargebee's web console.",
        label: "Your API Key"
      },
      {
        name: "custom_domain",
        label: "Are you using a custom domain?",
        extends_schema: true,
        control_type: "checkbox"
      }
    ],

    extended_fields: lambda do |connection|
      if connection['custom_domain'] == "true"
        [
          {
            name: "domain",
            control_type: "subdomain",
            extends_schema: true,
            url: ".acme.com"
          }
        ]
      end
    end,
```

Workato passes the connection hash to all other lambdas, including `authorization` and `execute`. The connection hash contains values from both `fields` and `extended_fields`.

### Example: Connection fields with extended\_fields and extends\_schema

The following example shows how to use `extends_schema` within `extended_fields` to create a connection setup that has multiple steps.

```ruby
  connection: {
    fields: [
      {
        name: "api_key",
        control_type: "password",
        hint: "You can find your API key " \
          "under 'Settings'=>'Configure Chargebee'=>'API Keys and Webhooks'" \
          " in Chargebee's web console.",
        label: "Your API Key"
      },
      {
        name: "custom_domain",
        label: "Are you using a custom domain?",
        extends_schema: true,
        control_type: "checkbox"
      }
    ],

    extended_fields: lambda do |connection|
        [
          (
            if connection['custom_domain'] == "true"
              {
                name: "domain",
                control_type: "subdomain",
                optional: false,
                url: ".acme.com"
              }
            end
          ),
          (
            if connection['custom_domain'] == "true"
              {
                name: "instance_type",
                control_type: "select",
                extends_schema: true,
                optional: false,
                options: [ ["Production", "production"], ["Sandbox", "sandbox"]]
              }
            end
          ),
          (
            if connection['instance_type'] == "sandbox"
              {
                name: "protocol",
                control_type: "select",
                optional: false,
                options: [ ["HTTPS", "https://"], ["HTTP", "http://"]]
              }
            end
          )
        ].compact
    end,

    authorization: {
      type: 'basic',

      apply: lambda { |connection, access_token|
        headers("x-api-key": "#{connection['api_key']}")
      }
    },

    base_uri: lambda do |connection|
        if connection['custom_domain'] == "true"
          "#{connection['protocol']}#{connection['domain']}.acme.com/"
        else
          "https://api.acme.com/"
        end
    end
  },
```

* * *

## authorization

The 'authorization' key has the following attributes:

<dl><dt>Key</dt><dd><code>authorization</code></dd><dt>Type</dt><dd>Hash</dd><dt>Required</dt><dd>True</dd><dt>Description</dt><dd>Accepts an object with child keys corresponding to different types of authentication</dd></dl>

Find out more about the `authorization` hash in [SDK Reference - authorization](/en/developing-connectors/sdk/sdk-reference/connection/authorization).

* * *

## base\_uri

The 'base\_uri' key has the following attributes:

<dl><dt>Key</dt><dd><code>base_uri</code></dd><dt>Type</dt><dd>lambda function</dd><dt>Required</dt><dd>False. However, we recommend it.</dd><dt>Description</dt><dd>Defines the base URI for all future HTTP requests.</dd><dt>Possible Arguments</dt><dd><dl class="horizontal-dl"><dt>connection</dt><dd>Hash that represents user-provided inputs defined in <code>Connection</code>.</dd></dl></dd><dt>Expected Output</dt><dd><code>String</code>, such as one of:<br><ul><li><code>"https://#{connection['host']}.com/"</code></li><li><code>"https://api.acme.com"</code></li></ul></dd></dl>

### Configuring your base\_uri

When you define your `base_uri` key, make sure to note the final URI that you provide. There are two scenarios when using `base_uri` in conjunction with any downstream HTTP requests.

1. When you have a preceding "/" (forward slash) in the verb method (such as `get('/hello/there')`), we ignore any path parameters in the `base_uri`.
   
   For example, `https://api.hubapi.com/test/` defined as your `base_uri` effectively becomes `https://api.hubapi.com`. The request is sent to `https://api.hubapi.com/hello/there`.
   
2. If you **don’t** have a preceding "/" (forward slash) in the verb method (such as `get('hello/there')`), we adopt the path parameters in your `base_uri`.
   
   For example, `https://api.hubapi.com/test/` defined as your `base_uri` remains `https://api.hubapi.com/test/`. The request is sent to `https://api.hubapi.com/test/hello/there`.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/sdk-reference/connection/authorization.md
description: >-
  Reference for the authorization hash in the Workato connector SDK, covering
  auth types, tokens, refresh, and applying credentials.
---

# SDK Reference - `authorization`

This section enumerates all possible keys in the `authorization` hash. Some keys apply only to specific types of authentication. Immediately after the user clicks "Connect", Workato runs the code in the `authorization` hash.

The `authorization` hash contains all instructions for your connector to retrieve and use authorization parameters. This may be simple: where to place an API key in future requests. It could also be much more complex: running a series of HTTP requests to retrieve an access token.

## Structure

```ruby
  authorization: {
    type: String,

    client_id: lambda do |connection|
      String
    end,

    client_secret: lambda do |connection|
      String
    end,

    authorization_url: lambda do |connection|
      String
    end,

    token_url: lambda do |connection|
      String
    end,

    acquire: lambda do |connection, auth_code, redirect_uri, verifier|
      Hash or Array
    end,

    apply: lambda do |connection, access_token|
      # see apply documentation for more information
    end,

    refresh_on: Array,

    detect_on: Array,

    refresh: lambda do |connection, refresh_token|
      Hash or Array
    end,

    identity: lambda do |connection|
      String
    end,
    pkce: lambda do |verifier, challenge|
      Hash
    end,

    selected: lambda do |connection|
      String
    end,

    options: Hash,

    noopener: Boolean
  }
```

* * *

## `type`

| Attribute | Description |
| --- | --- |
| Key | `type` |
| Type | String |
| Required | True |
| Description | Denotes the type of authentication used for this connector. |
| Expected Output | **One of the following:** "basic\_auth" - Used for Basic authentication. "api\_key" - Used for API key authentication. "oauth2" - Used only for OAuth 2.0 **Auth Code Grant flows**. For other OAuth variations, use "custom\_auth". "custom\_auth" - Free form authentication. Use this for multi-step, JWT, or non-standard Auth methods. "multi" - Allows you to define multiple authentication methods at once |

* * *

## `client_id`

| Attribute | Description |
| --- | --- |
| Key | `client_id` |
| Type | lambda function |
| Required | True if `type` is "oauth2". Ignored otherwise |
| Description | Defines the client\_id to use in Authorization URL and Token URL requests |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `Connection` |
| Expected Output | `String` i.e. `#{connection['client_id']}` |

* * *

## `client_secret`

| Attribute | Description |
| --- | --- |
| Key | `client_secret` |
| Type | lambda function |
| Required | True if `type` is "oauth2" and `acquire` is not defined. Ignored otherwise |
| Description | Defines the client\_secret to use in Token URL requests |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `Connection` |
| Expected Output | `String` i.e. `#{connection['client_secret']}` |

* * *

## `authorization_url`

| Attribute | Description |
| --- | --- |
| Key | `authorization_url` |
| Type | lambda function |
| Required | True if the `type` is "oauth2"; ignored otherwise. |
| Description | Denotes the authorization URL that users should be sent to in OAuth 2.0 Auth code grant flow. |
| Possible Arguments | `connection` - Hash representing user-given inputs defined in `Connection`. |
| Expected Output | `String` Example: `"https://podio.com/oauth/authorize"` or `"#{connection['domain']}/oauth/authorize"` |

Workato automatically appends these standard OAuth 2.0 parameters for the authorization URL:

<dl><dt>state</dt><dd>The state to protect against CSRF attacks. Don’t configure this, as Workato uses the state to route the callback request properly.</dd><dt>redirect_uri</dt><dd>Set to <code>https://www.workato.com/oauth/callback</code>; does not have to be configured.</dd></dl>

Configure the following query parameter manually:

<dl><dt>response_type</dt><dd>This query parameter must be set to <code>code</code>.</dd><dd>Example:<pre>    <code>authorization_url: lambda do |connection| "https://acme.com/api/oauth/authorization?response_type=code"
end,</code>
    </pre></dd></dl>

You may chose to include scope in your Authorization URLs.

* * *

## `token_url`

| Attribute | Description |
| --- | --- |
| Key | `token_url` |
| Type | lambda function |
| Required | True if `type` is "oauth2" and `acquire` is not defined. Ignored otherwise. |
| Description | Denotes the token URL that used to receive an access\_token |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `Connection` |
| Expected Output | `String` i.e. `"https://podio.com/oauth/token"` or `"#{connection['domain']}/oauth/token"` |

Workato automatically appends the following standard OAuth 2.0 parameters for the token URL:

<dl><dt>grant_type</dt><dd>Set to <code>authorization_code</code></dd><dt>code</dt><dd>The authorization code received from authorization url callback</dd><dt>redirect_uri</dt><dd>Set to `https://www.workato.com/oauth/callback` and does not have to be configured</dd><dt>client_id</dt><dd>Inferred from the <code>client_id</code> lambda, if present.</dd><dt>client_secret</dt><dd>This is inferred from the <code>client_secret</code>lambda, if present.</dd></dl>

* * *

## `acquire`

| Attribute | Description |
| --- | --- |
| Key | `acquire` |
| Type | lambda function |
| Required | True if `type` is "custom\_auth". Optional if `type` is "oauth2" Ignored otherwise |
| Description | If `type` is "custom\_auth", the `acquire` lambda function is only run if `refresh_on` or `detect_on` is triggered. If `type` is "oauth2", the `acquire` lambda function is run after we receive the callback from the authorization\_url. |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `Connection` `auth_code` - Only applicable if `type` is "oauth2". String representing the auth\_code received from Authorization URL callback. `redirect_uri` - Provides the appropriate redirect URI based on the Workato DC you are in. e.g. US DC would be `https://www.workato.com/oauth/callback`. `verifier` - Used only in PKCE authentication, whereby you will have access to the verifier defined in the `pkce` lambda. |
| Expected Output | **Variable - see examples below.** |

Example - acquire: - type: "oauth2"

If you specify `type` as "oauth2", the `acquire` block expects the output as an array of hashes. The array must contain the following values, in sequence:

<dl><dt>Tokens</dt><dd>Tokens must be in a hash with exact key names: <code>access_token</code>, <code>refresh_token</code> and <code>refresh_token_expires_in</code>.</dd><dt>Owner ID</dt><dd>This is an optional value used for clobber detection; if not used, substitute with nil.</dd><dt>Other values</dt><dd>If the API returns tokens with other keys, such as <code>id_access</code> and <code>id_refresh</code>, you can map them here. Supply an optional hash that can be merged with the original `connection` hash.</dd></dl>

```ruby
    acquire: lambda do |connection, auth_code|
      response = post("https://login.mypurecloud.com/oauth/token").
        payload(
          grant_type: "authorization_code",
          code: auth_code,
          redirect_uri: "https://www.workato.com/oauth/callback"
        )
      [
        { # This hash is for your tokens
      	  access_token: response["access_token"],
      	  refresh_token: response["refresh_token"],
          refresh_token_expires_in: response["refresh_token_expires_in"]
      	},
        # This hash is for your Owner ID. It is optional
      	nil,
        # This is for any other value you want to append to your connection object which you can reference later on.
      	{ instance_id: nil }
      ]
    end,
```

The key `refresh_token_expires_in` which denotes the seconds from now that the refresh token will expire. Since Workato only knows to refresh connections when there are jobs, there are cases where short lived refresh tokens may be expired for recipes where jobs come infrequently. For example, if the refresh token expires in 1 week and the recipe is only run once every 2 weeks, both the connection's access and refresh tokens would have expired by the time the recipe is run.

If the key `refresh_token_expires_in` is supplied, Workato will refresh the connection automatically without the need for any jobs, preserving the connection for as long as needed. There is no need to add a buffer to this time as Workato already adds a buffer to this time. For example, if the `refresh_token_expires_in` is 100 seconds, we would refresh the connection at the 85 second mark.

In some cases, APIs may not respond with expiration times for the refresh token or may respond in actual timestamps. You may also artificially create the `refresh_token_expires_in` value if you know the validity of the refresh token.

```ruby
    acquire: lambda do |connection, auth_code|
      response = post("https://login.mypurecloud.com/oauth/token").
        payload(
          grant_type: "authorization_code",
          code: auth_code,
          redirect_uri: "https://www.workato.com/oauth/callback"
        )
      [
        { # This hash is for your tokens
      	  access_token: response["access_token"],
      	  refresh_token: response["refresh_token"],
          refresh_token_expires_in: 604800 # Value in seconds. You can provide the value manually as well.
      	},
        # This hash is for your Owner ID. It is optional
      	nil,
        # This is for any other value you want to append to your connection object which you can reference later on.
      	{ instance_id: nil }
      ]
    end,
```

Example - acquire: - type: "custom\_auth"

If you specify `type` as "custom\_auth", the `acquire` lambda function expects the output as a single hash. Workato then merges the output into the original `connection` hash.

```ruby
  authorization: {
    acquire: lambda do |connection|
      {
        authtoken: get('https://accounts.zoho.com/apiauthtoken/nb/create')
      }
    end,

    refresh_on: 401
```

Original `connection` hash:

```ruby
    {
      "email": "john@gmail.com", # Given by User
      "password": "pinkfloyd" # Given by User
    }
```

When the user clicks the "Connect" button, Workato invokes the `test` lambda with the `connection` hash. If the `test` lambda fails with error code `401` (for example), Workato runs the `acquire` block.

After running the `acquire` block, the `connection` hash looks like this:

```ruby
    {
      "email": "john@gmail.com", # Given by User
      "password": "pinkfloyd" # Given by User
      "authtoken": "SAMPLE_TOKEN"
    }
```

Workato then attempts to invoke the `test` lambda again, with the new `connection` hash. If the `test` lambda succeeds, the connection appears as `Successful`.

Workato runs `acquire` only when the system triggers `refresh_on`, because `connection` hashes may have valid tokens. Examples:

- When the user disconnects from a valid connection that has an `authtoken` value
- When the user clicks **Connect**, and Workato attempts to use this `authtoken` instead of using a new one

* * *

## `apply`

| Attribute | Description |
| --- | --- |
| Key | `apply` |
| Type | lambda function |
| Required | True |
| Description | Defines the authentication parameters Workato adds to subsequent HTTP requests in the connector. |
| Possible arguments | `connection` - Hash representing user given inputs defined in `Connection`., `access_token` - Only applicable if `type` is "oauth2". Represents the `access_token` received from Token URL or `acquire` block. |

Example - apply

The `apply` block's lambda function can output multiple commands to attach authorization parameters to all requests. The following example illustrates common methods:

```ruby
    apply: lambda do |connection|
      # Adds in URL parameters passed as a hash object
      # i.e. authtoken=[connection['authtoken']]
      params(authtoken: connection['authtoken'])

      #Adds in payload fields (PATCH, POST, PUT only) passed as hash
      payload(grant_type: "authorization_code",
              client_id: connection["client_id"],
              client_secret: connection["client_secret"],
              code: auth_code)

      # Adds in headers into every request passed as a hash.
      # The variable access_token can be retrieved from input prompts defined in the 'fields' schema earlier or a return from the acquire block
      # i.e. Authorization : Bearer [given access token]
      headers("Authorization": "Bearer #{connection["access_token"]}")

      # Used in conjunction with password function
      # i.e. sends the input as username and password in HTTP authentication
      user(connection["username"])
      password(connection["username"])
    end
```

  

> **ACCESS AND MODIFY THE PAYLOAD OF A CURRENT REQUEST**
> 
> You can use the `apply` method to access and modify the payload of a current request. This is useful when you plan to update an existing payload or copy information into the header.
> 
> The following example demonstrates how to add a `user_id` from the connection to the payload before the final request is sent:
> 
> ```ruby
> apply: lambda do |connection|
>   if connection['user_id'].present? # Check if user_id exists in the connection
>     params = {}
>     payload do |current_payload| # Access the current payload
>       params = current_payload.dig('params') # Extract the params hash
>     end
>     params['user'] = connection['user_id'] # Insert user_id from the connection
>     payload({ "params": params }) # Merge the updated params into the payload
>   end
> end
> ```

Here are special variables that you can call in the `apply` lambda function:

<dl><dt><code>current_url</code></dt><dd>Enables matches on the current URL, and applies proper authentication.</dd><dd><pre><code class="ruby">apply: lambda do |_connection, access_token|
  if current_url.include?('https://developer.api.autodesk.com/cost/')
    headers('Authorization': "Bearer #{access_token}", 'Content-Type' =&gt; 'application/json')
  else
    headers('Authorization': "Bearer #{access_token}", 'Content-Type' =&gt; 'application/vnd.api+json')
  end
end</code>
</pre></dd><dt><code>current_verb</code></dt><dd>Enables matches on the current HTTP verb, and applies proper authentication.</dd><dd><pre><code class="ruby">apply: lambda do |_connection, access_token|
  if current_verb.include?('GET')
    headers('Authorization': "Bearer #{access_token}", 'Content-Type' =&gt; 'application/json')
  else
    headers('Authorization': "Bearer #{access_token}", 'Content-Type' =&gt; 'application/vnd.api+json')
  end
end</code></pre></dd></dl>

* * *

## `refresh_on`

This is an optional array of signals that identify when the system must re-acquire credentials. When it receives an error response (400, 401, 500...), the SDK framework checks the list of signals. If it finds a match, it triggers a re-authorization by running either the `refresh` lambda function for `type: oauth2` connections, or the `acquire` block for `type: custom_auth` connections.

| Attribute | Description |
| --- | --- |
| Key | `refresh_on` |
| Type | Array |
| Required | False. If not defined, will default to one attempt at re-acquiring credentials for all errors. |
| Description | Tells Workato when to refresh authentication credentials. This accepts an array of integers which are matched to HTTP response codes or Regex expressions which are matched on the response body. |
| Expected Output | Array of ints or strings - `[ 401, /Unauthorized/ ]` |

Example - \`refresh\_on\`:

This example demonstrates the multiple approaches for defining what "signals" to watch.

<dl><dt>401</dt><dd>The response status code</dd><dt>"Unauthorized"</dt><dd>The exact string that matches the whole body or title of the response</dd><dt>/Unauthorized/</dt><dd>The regex expression that matches the body or title of the response</dd></dl>

```ruby
    refresh_on: [
      401,
      'Unauthorized',
      /Unauthorized/,
      /Invalid Ticket Id/
    ]
```

* * *

## `detect_on`

Some APIs don't signal errors with explicit response status code, such as `401`. Instead, they return a `200` (pseudo- successful response) with a payload that signals the error.

For such APIs, Workato does not pick up an error (expired credentials, bad requests, and so on); it interprets it as a successful request because of the `200`response code. However, a match with signals raises an error. When it finds a match, two things can happen:

1. There can also be a match with `refresh_on` signals. This triggers a re-authorization where the `acquire` block runs instead of the system raising an error. Then, `detect_on` matches errors that hide behind the `200` response code to identify that the system must refresh the credentials.
   
2. If there is no match with signals that are defined in `refresh_on`, the system raises an error.
   

| Attribute | Description |
| --- | --- |
| Key | `detect_on` |
| Type | Array |
| Required | False |
| Description | Tells Workato when to raise an error due to a signal in the response to a request. This accepts an array of integers which are matched to HTTP response codes or Regex expressions which are matched on the response body. |
| Expected Output | Array of ints or strings - `[ 401, /Unauthorized/ ]` |

Example - detect\_on

This example demonstrates multiple approaches for defining "signals" to watch in `detect_on`.

<dl><dt>"sample error message"</dt><dd>The exact string that matches the whole body or title of the response</dd><dt>/^\{"response":\{"error".+$/</dt><dd>Regex expression that matches the body or title of the response</dd></dl>

```ruby
    detect_on: [
      "sample error message",
      /^\{"response":\{"error".+$/
    ]
```

* * *

## `refresh`

This lambda applies only to `type: "oauth2"` connections.

In many situations, the API expires the access token after a prescribed amount of time. The system then uses a refresh token to obtain a new access token. Refresh tokens do not expire, usually.

Not all APIs issue refresh token credentials. Check with your provider about this requirement.

| Attribute | Description |
| --- | --- |
| Key | `refresh` |
| Type | lambda function |
| Required | False but recommended and only valid for `type: oauth2` connections. |
| Description | This function will be executed if we either receive a non 2XX response in any API request, the `refresh_on` signal is triggered or if Workato knows that the refresh token is about to expire. This is used to obtain new access tokens. If this is not defined, Workato attempts to use the standard OAuth 2.0 refresh mechanism where possible or reruns the `acquire` lambda function. |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `Connection` `refresh_token` - Represents the `refresh_token` received from Token URL or `acquire` block. |
| Expected Output | A hash that contains a new access token. Optionally this hash can include a new refresh token (which will override the original refresh token) and a time delay before Workato refreshes the access token and refresh token. See the example below. |

Example - refresh

If you specify `type:` as "oauth2", the `refresh` block expects the output as a hash. This hash must include the keys for `access_token`, and potentially for `refresh_token` if the system creates a new refresh token each time.

It is also recommended you include the key `refresh_token_expires_in` which denotes the seconds from now that the refresh token will expire. Since Workato only knows to refresh connections when there are jobs, there are cases where short lived refresh tokens may be expired for recipes where jobs come infrequently. For example, if the refresh token expires in 1 week and the recipe is only run once every 2 weeks, both the connection's access and refresh tokens would have expired by the time the recipe is run.

If the key `refresh_token_expires_in` is supplied, Workato will refresh the connection automatically without the need for any jobs, preserving the connection for as long as needed. There is no need to add a buffer to this time as Workato already adds a buffer to this time. For example, if the `refresh_token_expires_in` is 100 seconds, we would refresh the connection at the 85 second mark.

For example, if the response from the refresh token url is as follows:

```json
{
  "access_token": "new_access_token",
  "refresh_token": "new_refresh_token",
  "refresh_token_expires_in": 604800
}
```

Then you should configure the HTTP request for the API call in the following manner:

```ruby
      refresh: lambda do |connection, refresh_token|
        url = "https://#{connection['custom_domain'].presence || 'go.trackvia.com'}"
        response = post("#{url}/oauth/token").payload(
          client_id: connection['client_id'],
          client_secret: connection['client_secret'],
          grant_type: 'refresh_token',
          refresh_token: refresh_token
        ).request_format_www_form_urlencoded
      end,
```

Alternatively, to return an array of hashes that override or add new values to your connection hash, implement something like this:

```ruby
    refresh: lambda do |connection, refresh_token|
      url = "https://#{connection['custom_domain'].presence || 'go.trackvia.com'}"
      response = post("#{url}/oauth/token").payload(
        client_id: connection['client_id'],
        client_secret: connection['client_secret'],
        grant_type: 'refresh_token',
        refresh_token: refresh_token
      ).request_format_www_form_urlencoded

      [
        { # This hash is for your tokens
          access_token: response["access_token"],
          refresh_token: response["refresh_token"],
          refresh_token_expires_in: response["refresh_token_expires_in"]
        },
        {
          user_key: user_key # Will be merged into connection hash
        }
      ]
    end,
```

In some cases, APIs may not respond with expiration times for the refresh token or may respond in actual timestamps. You may also artificially create the `refresh_token_expires_in` value if you know the validity of the refresh token.

```ruby
    refresh: lambda do |connection, refresh_token|
      url = "https://#{connection['custom_domain'].presence || 'go.trackvia.com'}"
      response = post("#{url}/oauth/token").payload(
        client_id: connection['client_id'],
        client_secret: connection['client_secret'],
        grant_type: 'refresh_token',
        refresh_token: refresh_token
      ).request_format_www_form_urlencoded

      [
        { # This hash is for your tokens
          access_token: response["access_token"],
          refresh_token: response["refresh_token"],
          refresh_token_expires_in: 604800 # Value in seconds. You can provide the value manually as well.
        },
        {
          user_key: user_key # Will be merged into connection hash
        }
      ]
    end,
```

* * *

## `identity`

The `identity` lambda displays additional information about the connection. This output appears on the connection page, providing extra context about the authenticated user or connection.

| Attribute | Description |
| --- | --- |
| Key | `identity` |
| Type | Lambda function |
| Required | False. |
| Description | The lambda allows you to display additional information about the connection object. You can make an HTTP request to retrieve user identity details, or reference existing values from the connection object. Refer to the [acquire lambda documentation](/en/developing-connectors/sdk/sdk-reference/connection/authorization#acquire) for details on appending values from the acquire lambda to the connection object. You can reference these values in the `identity` lambda. |
| Possible arguments | `connection` - A hash representing inputs defined in the `Connection` object. |
| Expected output | A string containing details about the connection (for example, "[user@example.com](mailto:user@example.com)", "Refresh token expires in 86400 seconds") |
|  |  |

Example - identity

In this example, the `identity` lambda makes an HTTP GET request to retrieve user information from a third-party API. It extracts the user’s email and displays it on the connection page. Use this when the connection object doesn't directly include the email.

```ruby
      identity: lambda do |_connection|
        get("https://app.asana.com/api/1.0/users/me")["data"]["email"]
      end,
```

You can also use this lambda to return values from the connection object. The following example retrieves the `username` from the connection object:

```ruby
      identity: lambda do |connection|
        connection["username"]
      end,
```

Additionally, you can customize the output of the lambda using values from the connection object to provide detailed information. The following example fetches the Company ID and displays a formatted string on the connection page:

```ruby
      identity: lambda do |connection|
        "Company ID: #{connection['company_id']}"
      end,
```

* * *

## `pkce`

This lambda applies only to `type: "oauth2"` connections and is only needed when OAuth2 Authorization code grant with PKCE authentication is needed. This lambda allows you to defined the parameters for PKCE such as the code verifier, code challenge and challenge method.

| Attribute | Description |
| --- | --- |
| Key | `pkce` |
| Type | lambda function |
| Required | False. Only needed for Auth code grant flows with PKCE |
| Description | This lambda allows you to set the parameters for the PKCE flow. It receives 2 arguments, `verifier` and `challenge`, where the `verifier` is an opaque string of 128 characters and the `challenge` is a url safe string that is the SHA256 of the verifier. In some cases, if you need a longer or shorter verifier, you can supply your own. |
| Possible Arguments | `verifier` - Opaque string of 128 characters. `challenge` - SHA256 of the `verifier` |
| Expected Output | Hash which contains 3 attributes, `verifier`, `challenge` and `challenge_method`. |

[Learn more about creating Authorization Code Grant flows with PKCE](/en/developing-connectors/sdk/guides/authentication/oauth/auth-code-pkce).

* * *

## `selected`

This lambda applies only to `type: "multi"` connections.

Use this lambda when defining `type: "multi"`; specify which inputs in the original inputs fields map to the correct Authentication type. Use this together with a declared `options`.

If `selected` is not defined but `type: "multi"` is defined, Workato defaults to any input with the internal name:`name: "auth_type"`

| Attribute | Description |
| --- | --- |
| Key | `selected` |
| Type | lambda function |
| Required | False. Required for `type: "multi"` connections. |
| Description | Workato runs this function will be executed based on the inputs given in `fields` and should output a string that will match against a key defined in the `options` hash. Defaults to the field with `auth_type` as the internal name. |
| Possible Arguments | `connection` - Hash representing user given inputs defined in `Connection` |
| Expected Output | A string that matches any keys defined in the `options` hash. |

* * *

## `options`

This lambda applies only to `type: "multi"` connections.

This hash contains the definition of multiple authentication flows when you plan a connector that supports multiple authentication types.

| Attribute | Description |
| --- | --- |
| Key | `options` |
| Type | Hash |
| Required | False. Required for `type: "multi"` connections. |
| Description | Hash that contains the definitions of the various authentication types within a "multi" authentication flow connector. |

Schema for nested authentication definitions

Consider the schema with nested authentication definitions:

```ruby
  options: {
    [unique_option_name]: {
        type: String,

        fields: Array,

        client_id: lambda do |connection|
          String
        end,

        client_secret: lambda do |connection|
          String
        end,

        authorization_url: lambda do |connection|
          String
        end,

        token_url: lambda do |connection|
          String
        end,

        acquire: lambda do |connection, auth_code|
          Hash or Array
        end,

        apply: lambda do |connection, access_token|
          # see apply documentation for more information
        end,

        refresh_on: Array,

        detect_on: Array,

        refresh: lambda do |connection, refresh_token|
          Hash or Array
        end,
    },

    [Another_unique_option_name]: {
        ...
    }
  }
```

Within the `options` hash, you must define two components for an authentication flow:

1. The _**key**_ that is unique to the authentication flow
2. The _**mechanics**_ of the authentication flow that is similar to an entirely new `authorization` hash.

Consider this example:

```ruby
    fields: [
      {
        name: "auth_type",
        control_type: "select",
        pick_list: [["OAuth2", "stripe_oauth2"], ["API Key", "stripe_api_key"]],
        default: "api_key",
        extends_schema: true
      }
    ],
    authorization: {

      type: "multi",

      selected: lambda do |connection|
        connection["auth_type"]
      end,

      options: {
        stripe_oauth2: {
          type: "oauth2",

          fields: [
            { name: 'authorization_url' },
            { name: 'token_url' },
            { name: 'client_id' },
            { name: 'client_secret' },
          ],

          authorization_url: lambda do |connection|
            connection['authorization_url']
          end,

          token_url: lambda do
            "https://api.stripe.com/accessToken"
          end,

          apply: lambda do |_, access_token|
            headers("Authorization": "OAuth2 #{access_token}")
          end,
        },

        stripe_api_key: {
          type: "custom_auth",

          fields: [
            {
              name: "api_key",
            }
          ],

          apply: lambda do |connection|
            headers("Authorization": "Bearer" + " " + connection["api_key"])
          end
        }
      },
    },
```

Here, you we defined 2 authentication flows, `stripe_oauth2` and `stripe_api_key`. These keys can be anything as long as they match the output of the `selected` lambda. In each of the flows, you can see and define all lambdas in the hash. For the `stripe_oauth2` option, we defined the `type` of the authentication flow as `oauth2`, `authorization_url`, `token_url` and the `apply` block.

The significant difference here is that you can define an additional `fields` key inside each authentication flow. This adds more input fields that are based on the selected authentication method; Workato adds these fields automatically.

* * *

## `noopener`

The `noopener` attribute applies only to OAuth 2.0 connections.

It specifies the `rel="noopener"` HTML attribute. This attribute improves security by adding `rel="noopener"` to links that open in a new browser tab or window.

| Attribute | Description |
| --- | --- |
| Key | `noopener` |
| Type | Boolean |
| Required | No. Defaults to `false`. Users can set to `true` for enhanced security. |
| Description | When set to `true`, the OAuth 2.0 authorization page launches with `target="blank"` and `rel="noopener"` attributes. This attribute improves security and prevents linked third-party websites from taking control of the browser tab through the window object. |

---
