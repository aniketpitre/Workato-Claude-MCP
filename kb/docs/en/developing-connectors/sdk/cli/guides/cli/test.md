---
url: 'https://docs.workato.com/en/developing-connectors/sdk/cli/guides/cli/test.md'
description: >-
  Run the connection test lambda locally with the Workato SDK gem for simple
  auth, advanced auth, and OAuth 2.0 connection scenarios.
---

# How-to guides - Running your test lambda on CLI

In this segment, we will run through how to run CLI commands for the test lambda function.

## Prerequisites

- You have installed and can run the Workato SDK Gem. Read our [getting-started guide](/en/developing-connectors/sdk/cli/guides/getting-started) to know more.
- You have a connector with at least the authentication (connection key) and test lambda defined. You use the samples provided below.
- You have a working set of credentials. If you are using a sample connector code, ensure that you have the appropriate credentials for the connector.

## This guide will walk you through how to:

- Invoke the test lambda for simple auth scenarios
  
- Simple auth scenarios include basic authentication, API key, or any similar forms. The threshold for this authentication is that the credentials the user supplies are all that is needed to authenticate. No additional follow-up steps are needed, such as retrieving an access token.
  
- Invoke the test lambda for advanced auth scenarios
  
- Advanced auth scenarios are when you use the input that the user has supplied to get another set of credentials later on. For example, if you're authenticating with OAuth 2.0 client credentials flow, when the user passes over a client ID and secret, you'd use these to get an access token in the `acquire:` lambda.
  
- Invoke the test lambda for OAuth2 (Auth code grant) scenarios
  
- If your type in the connection is set to `oauth2`.
  

## Why you should run the test lambda

This connection test lambda is run when the user first attempts to connect after they have supplied all the inputs for the connection, except for OAuth2 (Auth code grant) connections.

Additionally, all authentication types including OAuth 2 (Auth code grant) will invoke the test lambda to verify the connection is still valid when a recipe is first started.

> **Why OAuth2 does not require the test lambda on first connection**
> 
> The OAuth2 (Auth code grant) connection is confirmed by Workato when a token is retrieved from the OAuth2 token endpoint. Once a valid token has been received from your authorization server, the connection is deemed valid. Thus, there is no need to run additional connection test.

## Invoking the test lambda for Simple Auth

### Sample connector

The code in `connector.rb`.

```ruby
{
  title: 'Chargebee-demo',

  connection: {
    fields: [
      {
        name: 'api_key',
        control_type: 'password',
        hint: 'You can find your API key final change3' \
          "under 'Settings'=>'Configure Chargebee'=>'API Keys and Webhooks'" \
          " in Chargebee's web console.",
        label: 'Your API Key'
      },
      {
        name: 'domain',
        control_type: 'subdomain',
        url: 'chargebee.com'
      }
    ],

    authorization: {
      type: 'basic_auth',

      apply: lambda do |connection|
        user(connection['api_key'])
      end
    },

    base_uri: lambda do |connection|
      "https://#{connection['domain']}.chargebee.com"
    end
  },

  test: lambda do |_connection|
    get('/api/v2/plans', limit: 1)
  end,
}
```

Credentials in `settings.yaml.enc`.

```yaml
api_key: valid_api_key
domain: valid_domain
```

### Running the test lambda

When you run the command

```shell
$ workato exec test
```

You get the output

```shell
{
  "list": [
    {
      "plan": {
        "id": "cool-product",
        "name": "cool product",
        "price": 10000,
        "period": 2,
        "period_unit": "week",
        "pricing_model": "flat_fee",
        "free_quantity": 0,
        "status": "active",
        "enabled_in_hosted_pages": true,
        "enabled_in_portal": false,
        "addon_applicability": "all",
        "is_shippable": false,
        "updated_at": 1630235299,
        "giftable": false,
        "resource_version": 1630235299389,
        "object": "plan",
        "charge_model": "flat_fee",
        "taxable": true,
        "currency_code": "SGD",
        "show_description_in_invoices": true,
        "show_description_in_quotes": false,
      }
    }
  ],
  "next_offset": "[\"10000\",\"487940\"]"
}
```

This is the literal output of the `test` lambda we have defined but Workato relies not so much on the actual output, but that the request was executed successfully.

> **TIP**
> 
> You can also use other options like `--verbose` to see the detailed logs of any HTTP requests sent when building your `output_fields` and `--output` to save the output of the function to a JSON file.

## Invoking the test lambda for advanced Auth

### Sample connector - advanced auth

The code in `connector.rb`.

```ruby
{
    name: "Percolate",
    connection: {
      fields: [
        { name: "client_id",
          optional: false,
          hint: "To create client ID, the system admin or manager can click " \
          "<a href='https://percolate.com/app/settings/developer/apps/new' " \
          "target='_blank'>here</a> to register a new client application." },
        { name: "client_secret",
          control_type: "password",
          optional: false,
          hint: "To create client secret, the system admin or manager can click" \
          " <a href='https://percolate.com/app/settings/developer/apps/new' " \
          "target='_blank'>here</a> to register a new client application." },
        { name: "environment",
          optional: false,
          control_type: "select",
          pick_list: [%w[Production production], %w[Sandbox sandbox],
                      %w[Internal internal]] }
      ],

      authorization: {
        type: "custom_auth",

        acquire: lambda do |connection|
          hash = Base64.encode64("client:#{connection['client_id']}:#{connection['client_secret']}").gsub("\n", "")
          post("https://percolate.com/auth/v5/token/")
            .payload(grant_type: "client_credentials")
            .headers(Authorization: "Basic " + hash)
            .request_format_www_form_urlencoded
            .after_response do |_code, body, headers|
              body["headers"] = headers
              body
            end
        end,

        detect_on: [401, 403],

        refresh_on: [401, 403],

        apply: lambda do |connection|
          if current_url.include?("https://percolate.com")
            headers(Authorization: "Bearer #{connection['access_token']}")
          end
        end
      },

      base_uri: lambda do |_connection|
        "https://percolate.com"
      end
    },

    test: lambda do |_connection|
      get("/api/v5/me")
    end,
}
```

Credentials in `settings.yaml.enc`.

```yaml
client_id: valid_client_id
client_secret: valid_client_secret
environment: production
```

### Running the test lambda

When you run the command

```shell
workato exec test --verbose
```

You may get the output

```shell
SETTINGS
{
  "client_id": "valid_client_id",
  "client_secret": "valid_client_secret",
  "environment": "production",
}
INPUT
{
}

RestClient.get "https://percolate.com/api/v5/me", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "Authorization"=>"Bearer ", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 401 Unauthorized | application/json 65 bytes
Progress: |=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=|
RestClient.post "https://percolate.com/auth/v5/token/", "grant_type=client_credentials", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "Authorization"=>"Basic ", "Content-Length"=>"29", "Content-Type"=>"application/x-www-form-urlencoded", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 25 bytes
Progress: |=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=|

Refresh token triggered on response "401 Unauthorized"
Update settings file with new connection attributes? (Yes or No)
```

First, the output indicates that there is no `access_token` in the settings file as the connection test lambda (`api/v5/me` endpoint) returned a `401` response.

This triggers the `acquire` lambda (`auth/v5/token` endpoint). The `acquire` lambda is `POST` api call to the authorization endpoint. When this happens the output of `acquire` block is then merged to the `connection` hash. This is the same behavior on the Workato platform where the `acquire` lambda is only invoked if the `refresh_on` signals.

The `refresh_on` attribute in the `acquire` lambda triggers if the current access token expires and will retrieve a new access token. This will trigger whenever you invoke the connection test lambda or any other lambdas.

Lastly, the Gem asks for permissions to override your settings file, which is synonymous with your `connection` hash on the Workato platform. If you type "Yes", the Gem will now update your settings file with the output of the `acquire` lambda.

```shell
Update settings file with new connection attributes? (Yes or No) Yes
RestClient.get "https://percolate.com/api/v5/me", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "Authorization"=>"Bearer example_token", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 65 bytes
Progress: |=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=|

OUTPUT
# Output of the test lambda
```

Your credentials in `settings.yaml.enc` will be updated.

```yaml
client_id: valid_client_id
client_secret: valid_client_secret
environment: production
id: token:example_token
expires_in: 2592000
updated_at: '2021-08-30T14:54:35+00:00'
user_id: user:130135
grant_id: grant:1216779461986395763
access_token: example_token
token_type: bearer
```

## Invoking the test lambda for OAuth2 (Auth code grant) scenarios

For Auth code grant flows, the Workato Gem allows you to emulate the OAuth2 flow using the `workato oauth2` command. This behavior allows you to quickly debug and understand how the OAuth2 experience will look like for your end users.

### Sample connector - OAuth 2 Connector

The code in `connector.rb`.

```ruby
{
  title: 'TrackVia',
  connection: {
    fields: [
      {
        name: 'custom_domain',
        control_type: 'subdomain',
        label: 'TrackVia subdomain',
        hint: 'Enter your TrackVia subdomain. e.g. customdomain.trackvia.com. By default, <b>go.trackvia.com</b> will be used.',
        optional: 'true'
      },
      {
        name: 'account_id',
        control_type: :number,
        label: 'Account ID',
        hint: 'Specify the account to connect to',
        optional: true
      },
      {
        name: 'client_id',
        control_type: :text,
        label: 'TrackVia App Client ID',
        hint: 'Enter the Client ID of your own OAuth app registered on TrackVia',
        optional: 'false'
      },
      {
        name: 'client_secret',
        control_type: :text,
        label: 'TrackVia App Client secret',
        hint: 'Enter the Client secret of your own OAuth app registered on TrackVia',
        optional: 'false'
      }
    ],

    authorization: {
      type: 'oauth2',

      authorization_url: lambda { |connection|
        "https://#{connection['custom_domain'].presence || 'go.trackvia.com'}/oauth/authorize?response_type=code"
      },

      acquire: lambda do |connection, auth_code, redirect_uri|
        url = "https://#{connection['custom_domain'].presence || 'go.trackvia.com'}"
        response = post("#{url}/oauth/token").payload(
          redirect_uri: redirect_uri,
          grant_type: 'authorization_code',
          code: auth_code,
          client_id: connection['client_id'],
          client_secret: connection['client_secret']
        ).request_format_www_form_urlencoded
        user_key = get("#{url}/3scale/openapiapps").params(access_token: response['access_token']).dig(0, 'userKey')
        [
          response,
          nil,
          {
            user_key: user_key
          }
        ]
      end,

      refresh: lambda do |connection, refresh_token|
        url = "https://#{connection['custom_domain'].presence || 'go.trackvia.com'}"
        post("#{url}/oauth/token").payload(
          client_id: connection['client_id'],
          client_secret: connection['client_secret'],
          grant_type: 'refresh_token',
          refresh_token: refresh_token
        ).request_format_www_form_urlencoded
      end,

      refresh_on: [401, 403],

      apply: lambda { |connection, access_token|
        params(user_key: connection['user_key'])
        headers(Authorization: "Bearer #{access_token}")
        headers('account-id': connection['account_id']) if connection['account_id'].present?
      }
    },

    base_uri: lambda do |connection|
      if connection['custom_domain'].presence
        "https://#{connection['custom_domain']}/openapi/"
      else
        "https://go.trackvia.com/openapi/"
      end
    end
  },

  test: lambda do |connection|
    get('views')
  end,
}
```

Credentials in `settings.yaml.enc`.

```yaml
client_id: valid_client_id
client_secret: valid_client_secret
```

You can now run the following commands to go through the OAuth2 Authorization code flow which includes a browser popup. Include `--verbose` to enable detailed logging of the OAuth2 flow.

```shell
workato oauth2 --verbose
```

This will simulate the entire flow from the browser popup to the output url of the `authorization_url`, receiving the Auth Code to your callback url as well as subsequent calls contained in either your `token_url` lambda or your `acquire` lambda. Lastly, the flow will update your `settings.yaml` file with the latest set of credentials received from the OAuth2 flow.

![SDK Gem OAuth2 flow](/assets/SDK_gem_oauth2_flow.eRYcswQM.gif)_The SDK Gem emulates the OAuth2 flow on Workato_

At the end of the flow, you should have a `settings.yaml.enc` file that is updated with the latest credentials.

```yaml
client_id: valid_client_id
client_secret: valid_client_secret
user_key: valid_user_key
tokenType: bearer
expires_in: 299
expiration: '2021-10-19T15:36:39.221+0000'
scope:
- trust
- read
- write
apiVersion: '22.18'
access_token: valid_access_token
refresh_token: valid_refresh_token
```

### Running the test lambda

Now after you've successfully gone through the flow, you may be use the same `workato exec test` command to verify you're applying your token properly in your requests!

Depending on when you received your token, you may also see a intermediary command from the Gem asking if you'd like to refresh your access tokens (if it has expired). This is done when HTTP requests are made which have a response that triggers the `refresh_on` block. Selecting yes would cause the Gem to update your settings file with the latest auth credentials.

```shell
$ workato exec test --verbose
```

You may get the output

```shell
SETTINGS
{
  "client_id": "valid_client_id",
  "client_secret": "valid_client_secret",
  "user_key": "valid_user_key",
  "tokenType": "bearer",
  "expires_in": "299",
  "expiration": "2021-10-19T15:36:39.221+0000",
  "scope": ["trust", "read", "write"],
  "apiVersion": "2.18",
  "access_token": "valid_access_token",
  "refresh_token": "valid_refresh_token"
}
INPUT
{
}

RestClient.get "https://go.trackvia.com/openapi/views", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "Authorization"=>"Bearer valid_access_token", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 401 Unauthorized | application/json 65 bytes
Progress: |=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=|
RestClient.post "https://go.trackvia.com/oauth/token", "grant_type"=>"client_credentials", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "refresh_token"=>"valid_refresh_token", "Content-Length"=>"29", "Content-Type"=>"application/x-www-form-urlencoded", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 25 bytes
Progress: |=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=|

Refresh token triggered on response "401 Unauthorized"
Updated settings file with new connection attributes? (Yes or No)
```

First, the output indicates that there is no valid `access_token` in the settings file as the connection test lambda (`openapi/views` endpoint) returned a `401` response. The access token may have expired.

This triggers the `acquire` lambda (`/oauth/token` endpoint). The `acquire` lambda is a `POST` api call to the authorization endpoint. When this happens the output of `acquire` block is then merged to the `connection` hash. This is the same behavior on the Workato platform where the `acquire` lambda is only invoked if the `refresh_on` signals.

The `refresh_on` attribute in the `acquire` lambda triggers if the current access token expires and will retrieve a new access token. This will trigger whenever you invoke the connection test lambda or any other lambdas.

Lastly, the Gem asks for permissions to override your settings file, which is synonymous with your `connection` hash on the Workato platform. If you type "Yes", the Gem will now update your settings file with the output of the `acquire` lambda.

```shell
Updated settings file with new connection attributes? (Yes or No) Yes
RestClient.get "https://go.trackvia.com/openapi/views", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "Authorization"=>"Bearer new_valid_access_token", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 65 bytes
Progress: |=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=|

OUTPUT
# Output of the test lambda
```

Your credentials in `settings.yaml.enc` will be updated.

```yaml
client_id: valid_client_id
client_secret: valid_client_secret
user_key: valid_user_key
tokenType: bearer
expires_in: 299
expiration: '2021-10-19T15:41:39.221+0000'
scope:
- trust
- read
- write
apiVersion: '22.18'
access_token: new_valid_access_token
refresh_token: new_valid_refresh_token
```

> **Note**
> 
> You may also use `workato exec` to execute lambdas in your `authorization` hash like `acquire` and `refresh`. **That said, we highlight recommend you use `workato exec test` and `workato oauth2` which handle the updating of your `settings.yaml` file automatically.**

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/cli/actions.md
description: >-
  Run and debug connector actions locally with the Workato SDK gem, invoking
  execute, input_fields, and output_fields lambdas on the CLI.
---

# How-to guides - Running actions on CLI

In this segment, we will be going through how you can run actions using the Workato Gem.

## Prerequisites

- You have installed and can run the Workato SDK Gem. Read our [getting-started guide](/en/developing-connectors/sdk/cli/guides/getting-started) to know more.
- You have a working connector with at least 1 action. You use the sample connector provided below.
- You have a working set of credentials. If you are using a sample connector code, ensure that you have the appropriate credentials for the connector.

## Sample connector - Chargebee

The code in `connector.rb`.

```ruby
{
  title: 'Chargebee-demo',

  connection: {
    fields: [
      {
        name: 'api_key',
        control_type: 'password',
        hint: 'You can find your API key final change3' \
          "under 'Settings'=>'Configure Chargebee'=>'API Keys and Webhooks'" \
          " in Chargebee's web console.",
        label: 'Your API Key'
      },
      {
        name: 'domain',
        control_type: 'subdomain',
        url: 'chargebee.com'
      }
    ],

    authorization: {
      type: 'basic_auth',

      apply: lambda do |connection|
        user(connection['api_key'])
      end
    },

    base_uri: lambda do |connection|
      "https://#{connection['domain']}.chargebee.com"
    end
  },

  test: lambda do |_connection|
    get('/api/v2/plans', limit: 1)
  end,

  actions: {

    search_customers: {
      title: 'Search customers',
      subtitle: 'Search for customers using name',
      description: 'Search customer in Chargebee',

      input_fields: lambda do |_object_definitions|
        [
          {
            name: 'name',
            label: 'Name to query by',
            hint: 'Provide the name of the customer to query'
          },
          {
            name: 'id',
            label: 'Name to query by',
            hint: 'Provide the name of the customer to query'
          }
        ]
      end,

      execute: lambda do |_connection, input, _input_schema, _output_schema|
        get('/api/v2/customers', input)
      end,

      output_fields: lambda do |_object_definitions|
        [
          {
            name: 'first_name'
          },
          {
            name: 'last_name'
          },
          {
            name: 'id'
          }
        ]
      end
    }

  },

}
```

Credentials in `settings.yaml.enc` .

```yaml
api_key: valid_api_key
domain: valid_domain
```

> **TIP**
> 
> If you're using an encrypted settings.yaml file, you will need to use `workato edit <PATH>` to edit or create the file. Refer to [workato edit](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-edit) for more information on editing encrypted files.

With the SDK Gem, you'll be able to invoke individual lambda functions in your action and gain greater control over how each part of your action works. For example, you may run your `execute` lambda function independently from your `input_fields` lambda.

## Running your input fields and output fields lambdas

In this guide, we will be covering input\_fields lambdas. You can run output\_fields lambdas the same way.

> **TIP**
> 
> Sometimes, you may find yourself with a sample payload request or response. You can also use the `workato generate schema` CLI command to convert this payload easily into Workato schema. Learn more about [Workato CLI generate schema](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-generate-schema).

Your input\_fields lambda is expected to return Workato schema which corresponds to the input fields we should show to the user. In the case we have above, it simply returns the Workato schema stored within.

```shell
$ workato exec actions.search_customers.input_fields

[
  {
    "name": "name",
    "label": "Name to query by",
    "hint": "Provide the name of the customer to query"
  },
  {
    "name": 'limit',
    "hint": 'Total number of records to return'
  }
]
```

But you may also provide additional arguments when required. For example, if your input\_fields is dependent on your `config_fields`, you would be required to pass `config_fields` for it to work. This can be done using something similar to below - where `customer_config.json` represents the `config_fields` argument of the lambda.

```shell
$ workato exec actons.search_customers.input_fields --config-fields='fixtures/actions/search_customers/customer_config.json'
```

> **TIP**
> 
> You can also use other options like `--verbose` to see the detailed logs of any HTTP requests sent when building your `input_fields` and `--output` to save the output of the function to a JSON file.
> 
> You do not need to pass anything for the object\_definitions argument as the gem can reference it when it looks at your connector.

## Running your execute lambda

Your execute lambda is expected to return a hash which represents the output of the action. In the case we have above, it returns response that Chargebee sends to us. You can see that we have referenced an `input` in the command which points to a JSON file stored in our `fixtures` folder. This file should contain the actual value passed to the `execute` lambda from the `input_fields`.

In this situation, the contents of the file `fixtures/actions/search_customers/input.json` contains:

```JSON
{
  "name": "bennett",
  "limit": 1
}
```

When we run the CLI command to run the `execute` lambda:

```shell
$ workato exec actions.search_customers.execute --input='fixtures/actions/search_customers/input.json' --verbose

SETTINGS
{
  "api_key": "valid_api_key",
  "domain": "valid_domain"
}
INPUT
{
  "name": "bennett",
  "limit": 1
}

RestClient.get "https://test.chargebee.com/api/v2/customers?limit=1&name=bennett", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 753 bytes
Progress: |--=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=-|

OUTPUT
{
  "list": [
    {
      "customer": {
        "id": "abc",
        "first_name": "John",
        "last_name": "doe",
        "email": "john@gmail.com",
        "phone": "+100",
        "auto_collection": "on",
        "net_term_days": 0,
        "allow_direct_debit": false,
        "created_at": 1630848839,
        "taxability": "taxable",
        "updated_at": 1630848840,
        "locale": "en-US",
        "pii_cleared": "active",
        "resource_version": 1630848840782,
        "deleted": false,
        "object": "customer",
        "card_status": "valid",
        "promotional_credits": 0,
        "refundable_credits": 0,
        "excess_payments": 0,
        "unbilled_charges": 0,
        "preferred_currency_code": "SGD",
      }
    }
  ],
  "next_offset": "[\"1630848839000\",\"42903379\"]"
}
```

Note that we have used `--verbose` so the SDK gem has printed out more information including the API requests and responses.

The input for `connection` is assumed to be the `settings.yaml.enc` file and does not need to be declared unless you want to use a different settings.yaml file.

> **TIP**
> 
> You can also use other options like `--output` to save the output of the function to a JSON file.

## Running the entire action

Whilst running your execute lambda allows you to stub the `input` argument, often time, you also want to see how input passed to the input fields is then run through the action. For example, in cases where you may use schema attributes like `convert_input` and `convert_output` which do casting of data types.

For example, when a user gives you input for the above example where `limit` is provided as a string, you would need to convert this value to an integer.

```json
#fixtures/actions/search_customers/input.json
{
  "name": "bennett",
  "limit": "1"
}
```

This can be done with schema attributes like `convert_input` which takes this value and done the conversion.

```ruby
[
  {
    "name": "name",
    "label": "Name to query by",
    "hint": "Provide the name of the customer to query"
  },
  {
    "name": 'limit',
    "convert_input": "integer_conversion",
    "hint": "Total number of records to return"
  }
]
```

After transformation, your `input` argument to the `execute` lambda will look like this:

```ruby
{
  "name": "bennett",
  "limit": 1
}
```

> **TIP**
> 
> When users provide static values or text values in input fields, you should assume they will be passed to your execute as strings. Using attributes like `convert_input` and `convert_output` allow you to do transformation of data even before it is presented as the `input` argument to your `execute` lambda.
> 
> Learn more about [converting input and converting output](/en/developing-connectors/sdk/sdk-reference/schema#using-convert-input-and-convert-output-for-easy-transformations).

To test this transformation out that occurs from schema, when we have to run the CLI command to run the entire action:

```shell
$ workato exec actions.search_customers --input='fixtures/actions/search_customers/input.json' --verbose

SETTINGS
{
  "api_key": "valid_api_key",
  "domain": "valid_domain"
}
INPUT
{
  "name": "bennett",
  "limit": "1"
}

RestClient.get "https://test.chargebee.com/api/v2/customers?limit=1&name=bennett", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 753 bytes
Progress: |--=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=-|

OUTPUT
{
  "list": [
    {
      "customer": {
        "id": "1",
        "first_name": "bennett",
        "last_name": "doe",
        "email": "bennett@gmail.com",
        "phone": "+100",
        "auto_collection": "on",
        "net_term_days": 0,
        "allow_direct_debit": false,
        "created_at": 1630848839,
        "taxability": "taxable",
        "updated_at": 1630848840,
        "locale": "en-US",
        "pii_cleared": "active",
        "resource_version": 1630848840782,
        "deleted": false,
        "object": "customer",
        "card_status": "valid",
        "promotional_credits": 0,
        "refundable_credits": 0,
        "excess_payments": 0,
        "unbilled_charges": 0,
        "preferred_currency_code": "SGD",
      }
    }
  ],
  "next_offset": "[\"1630848839000\",\"42903379\"]"
}
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/cli/multistep-actions.md
description: >-
  Run and debug multistep connector actions locally with the Workato SDK gem,
  invoking individual lambdas and handling reinvoke_after.
---

# How-to guides - Running multistep actions on CLI

In this segment, we will be going through how you can run and easily debug multistep actions using the Workato Gem.

## Prerequisites

- You have installed and can run the Workato SDK Gem. Read our [getting-started guide](/en/developing-connectors/sdk/cli/guides/getting-started) to know more.
- You have a working connector with at least 1 multistep action.
- You have a working set of credentials. If you are using a sample connector code, ensure that you have the appropriate credentials for the connector.

## Sample connector - Google BigQuery

This example is based on the [BigQuery connector example](/en/developing-connectors/sdk/guides/building-actions/multistep-actions#sample-connector-google-bigquery) from the multistep actions guide.

Credentials in `settings.yaml.enc` .

```yaml
iss: service_account_email@example.com
private_key: "-----BEGIN PRIVATE KEY-----...-----END
  PRIVATE KEY-----\\n"
access_token: valid_access_token
expires_in: 3599
token_type: Bearer
```

> **TIP**
> 
> If you're using an encrypted settings.yaml file, you will need to use `workato edit <PATH>` to edit or create the file. Refer to [workato edit](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-edit) for more information on editing encrypted files.

With the SDK Gem, you'll be able to invoke individual lambda functions in your action and gain greater control over how each part of your action works. For example, you may run your `execute` lambda function independently from your `input_fields` lambda. Refer to the [actions guide](/en/developing-connectors/sdk/cli/guides/cli/actions) for more information on running your `input_fields` and `output_fields` lambdas.

## Running your execute lambda for multistep actions

With multistep actions, we need to take note that special methods like `reinvoke_after` will cause the job in Workato to be put to sleep for a defined amount of time.

```ruby
reinvoke_after(seconds: 10, continue: { current_step: current_step + 1, jobid: continue['jobid']})
```

> **TIP**
> 
> On the Workato platform, step time is set to be a minimum of 60 seconds. On the SDK Emulator, however, the step time between checks can be set to be lower for debugging purposes.

The above method call in your `execute` lambda will results in the job being put to sleep for 10 seconds before being awoken again where execution begins at the **start of the execute block**. The SDK Gem emulates this behavior so you'll be able to examine how your action might behave on Workato.

The `bigquery_input.json` file in this example contains the following:

```JSON
{
    "project_id": "named-reporter-237205",
    "query": "SELECT * FROM `named-reporter-237205.Lead_data.2mill_table` t1",
    "wait_for_query": "true"
}
```

To run a multistep action, you give the same command as you would a standard action.

```shell
workato exec actions.query.execute --input='bigquery_input.json' --verbose

SETTINGS
{
  "iss": "service_account_email@example.com",
  "private_key": "-----BEGIN PRIVATE KEY-----...-----END
  PRIVATE KEY-----\\n",
  "access_token": "valid_access_token",
  "expires_in": 3599,
  "token_type": "Bearer"
}
INPUT
{
  "project_id": "named-reporter-237205",
  "query": "SELECT * FROM `named-reporter-237205.Lead_data.2mill_table` t1",
  "wait_for_query": "true"
}

RestClient.post "https://bigquery.googleapis.com/bigquery/v2/projects/named-reporter-237205/queries", "{\"query\":\"SELECT * FROM `named-reporter-237205.Lead_data.2mill_table` t1 left join `named-reporter-237205.Lead_data.2mill_table` t2 on t1.start_time = t2.start_time\",\"timeoutMs\":\"25000\",\"useLegacySql\":false}", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "Authorization"=>"Bearer ya29.c.Kp8BFQgUT1EOcK5YBwTEv60KokPYvLLWJRFsbfd9S0oGEB3cW5cp1pXTJRZreYPB4B06Z1_YdvhLQByhe9fP_FjziQc6rCtEfGs9zZdMZpXKUFHWEqzG44qxni-jibwaLEgWLw3zaqv42y00x28jUmZQdP3AQilOPdn1xRwf6s-gWi_95d1t0qDe478VnclTIrZ_SmCMtDTTbdU1yvkA80TQ...", "Content-Length"=>"207", "Content-Type"=>"application/json", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 176 bytes

RestClient.get "https://bigquery.googleapis.com/bigquery/v2/projects/named-reporter-237205/jobs/job_LnXWC2bcE64hzeBlYMPWNCsMwavn", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "Authorization"=>"Bearer ya29.c.Kp8BFQgUT1EOcK5YBwTEv60KokPYvLLWJRFsbfd9S0oGEB3cW5cp1pXTJRZreYPB4B06Z1_YdvhLQByhe9fP_FjziQc6rCtEfGs9zZdMZpXKUFHWEqzG44qxni-jibwaLEgWLw3zaqv42y00x28jUmZQdP3AQilOPdn1xRwf6s-gWi_95d1t0qDe478VnclTIrZ_SmCMtDTTbdU1yvkA80TQ...", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 2062 bytes

OUTPUT
{
  "jobId": "abc123",
  "totalRows": 1000,
  "pageToken": "123abc",
  "rows": [
    ...rows...
  ],
  "manualLink": "https://www.example.com"
}
```

Note that we have used `--verbose` so the SDK gem has printed out more information including the API requests and responses. This also allows you to see the multistep in action, where the Gem allows you to wait before executing a request to check on the job execution.

> **TIP**
> 
> You can also use other options like `--output` to save the output of the function to a JSON file.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/cli/download-streaming-actions.md
description: >-
  Run and debug streaming download file actions and their streams callback
  locally on the CLI using the Workato SDK gem.
---

# How-to guides - Running streaming download actions/triggers on CLI

In this segment, we will be going through how you can run and easily debug actions that utilize file streaming using the Workato Gem. File streaming can be differentiated into two main components that go together - download file actions and upload file actions. Below, we will go over the steps to a download file action in the CLI.

## Prerequisites

- You have installed and can run the Workato SDK Gem. Read our [getting-started guide](/en/developing-connectors/sdk/cli/guides/getting-started) to know more.
- You have an understanding of the mechanics of file streaming on the SDK. Read our [guides](/en/developing-connectors/sdk/guides/building-actions/streaming) to learn more.

## Download file - Sample connector - Egnyte

We will be using the [Egnyte connector](/en/developing-connectors/sdk/guides/building-actions/streaming/download-stream) as an example.

### Running the `execute` lambda for the download file action

With download file actions, it is important to note that when the action/trigger is executed in a job, the actual downloading of the file contents (contained in the `streams` callback) is not triggered at that point in time. The `streams` callback of a download file action is only triggered when the datapill representing the file contents is used in a downstream action.

As such, in the SDK Gem, you may test your download file action as a normal action; and your `streams` callback separately. Let's go over the download file action first.

```ruby
execute: lambda do |connection, input|
  file_path = input['file_path']&.gsub(/%2F/, '/')

  file_details = get("/pubapi/v1/fs/#{file_path}")

  file_details['file_contents'] = workato.stream.out("download_file_by_path", { file_path: file_path})

  file_details
end,
```

Alongside the execute lambda, you will also need a input JSON file such as `egnyte_download_file_input.json` when executing the download file action in the SDK CLI.

```JSON
{
    "file_path": "/path/to/sample/file"
}
```

To run a download file action, you give the same command as you would a standard action.

```shell
workato exec actions.download_object.execute --input='egnyte_download_file_input.json' --verbose

SETTINGS
{
  "domain": "acme.egnyte.com",
  "client_id": "client_id",
  "client_secret": "client_secret",
  "access_token": "valid_access_token",
  "refresh_token": "valid_refresh_token",
  "expires_in": 3599,
  "token_type": "Bearer"
}
INPUT
{
    "file_path": "/path/to/sample/file"
}

RestClient.get "https://acme.egnyte.com/pubapi/v1/fs/path/to/sample/file", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "Authorization"=>"Bearer valid_access_token", "Content-Length"=>"207", "Content-Type"=>"application/json", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 176 bytes

OUTPUT
{
  "checksum": "abc123",
  "size": 1000,
  "path": "/path/to/sample/file",
  "name": "file",
  "file_contents": {
    "__stream__": true,
    "name": "stream",
    "input": {
      "file_path": "/path/to/sample/file"
  }
}
```

Note that the actual downloading of the file from Egnyte has not actually happened at this point - only the evaluation of the `execute` lambda excluding the `download_file_by_path` stream has been done when calling the action via the CLI. The output of the `file_contents` is an artificial value for a file stream.

> **TIP**
> 
> You can also use other options like `--output` to save the output of the function to a JSON file.

### Running the `streams` lambda used in the download file action

Now, to debug and test the `streams` lambda directly, you can use the CLI to invoke the lambda directly.

```ruby
streams: {
  download_file_by_path: lambda do |input, starting_byte_range, ending_byte_range, requested_byte_size|
    # Example starting_byte_range = 0
    # Example ending_byte_range = 10485759
    # Example requested_byte_size = 10485760 (10MB)
    chunk = get("/pubapi/v1/fs-content/#{file_path}").
              headers("Range": "bytes=#{starting_byte_range}-#{ending_byte_range}").
              response_format_raw
    # if the chunk.size is smaller than the requested byte_size,
    # then we know we are at the end of the file.
    [chunk, chunk.size < requested_byte_size]
  end
}
```

With the SDK Gem, you are able to invoke the specific streaming callback lambda to simulate the download of a single chunk, or loop over the entire download process to download multiple chunks sequentially.

You can invoke the stream using the following parameters to read a single chunk:

```shell
workato exec streams.download_file_by_path --input='egnyte_download_file_input.json' --from=0 --frame_size=256 --verbose

SETTINGS
{
  "domain": "acme.egnyte.com",
  "client_id": "client_id",
  "client_secret": "client_secret",
  "access_token": "valid_access_token",
  "refresh_token": "valid_refresh_token",
  "expires_in": 3599,
  "token_type": "Bearer"
}
INPUT
{
    "file_path": "/path/to/sample/file"
}

RestClient.get "https://acme.egnyte.com/pubapi/v1/fs-content/path/to/sample/file", "Range"=>"bytes=0-255", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "Authorization"=>"Bearer valid_access_token", "Content-Length"=>"207", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 206 PartialContent | text/csv 255 bytes, 1.85s

OUTPUT
[
  "256_byte_string",
  false
]
```

To read all chunks, you can invoke the stream with the same 3 parameters but with a bang (`!`) method.

```shell
workato exec streams.download_file_by_path! --input='egnyte_download_file_input.json' --frame_size=256 --verbose
```

> **TIP**
> 
> Take note that the `from` argument does not work with the bang (`!`) method. We advise that you test this on smaller files to avoid waiting for a long time for the download process to finish.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/cli/upload-streaming-actions.md
description: >-
  Run and debug upload file streaming actions and triggers for your custom
  connector on the Workato SDK CLI using the SDK gem.
---

# How-to guides - Running upload streaming actions/triggers on CLI

In this segment, we will be going through how you can run and easily debug actions that utilize file streaming using the Workato Gem. File streaming can be differentiated into two main components that go together - download file actions and upload file actions. Below, we will go over the steps to execute an upload file action in the CLI.

## Prerequisites

- You have installed and can run the Workato SDK Gem. Read our [getting-started guide](/en/developing-connectors/sdk/cli/guides/getting-started) to know more.
- You have an understanding of the mechanics of file streaming on the SDK. Read our [guides](/en/developing-connectors/sdk/guides/building-actions/streaming) to learn more.

## Upload file - Sample connector - Upload file to url

We will be using the [generic upload file to url connector](/en/developing-connectors/sdk/guides/building-actions/streaming/upload-stream-content-range) as an example.

### Running the `execute` lambda for the Upload file action

With upload file streaming actions, the definition of the input is important here as it has to contain information about an incoming file stream that the action will utilize. There are numerous options to simulate a file stream which we will go over.

```ruby
execute: lambda do |_connection, input, _input_schema, _output_schema, closure|
  # Calling workato.stream.in runs in a loop where the input should be file.
  # It can accept both entire files or the output of a streaming-enabled download file action
  workato.stream.in(input["file"]) do |chunk, starting_byte_range, ending_byte_range, eof, next_starting_byte_range|
    put(input['url']).
      headers("Content-Range": "bytes #{starting_byte_range}-#{ending_byte_range}/*").
      request_body(chunk).presence
  end

  # This commits the upload
  post(input['url'], { "commit": true } )

end,
```

Alongside the execute lambda, you will also need a input JSON file such as `upload_file_input.json` when executing the upload file action in the SDK CLI. Below, we have an example of a mocked stream whose chunks are defined explicitly - each chunk is a separate key in the `chunks` hash.

```JSON
{
    "file_name": "sample_file",
    "file": {
      # this hash simulates a file stream which is
      # the output of a download file object
      "__stream__": true,
      "chunks": {
        "0": "abcd",
        "4": "efgh",
        "8": "ijkl",
        "12": "mn"
      }
    },
    "url": "https://www.friendly_upload_url.com"
}
```

To run the upload file action, you give the same command as you would a standard action.

```shell
workato exec actions.upload_to_url.execute --input='upload_file_input.json' --verbose

SETTINGS
{}
INPUT
{
    "file_name": "sample_file",
    "file": {
      "__stream__": true,
      "chunks": {
        "0": "abcd",
        "4": "efgh",
        "8": "ijkl",
        "12": "mn"
      }
    },
    "url": "https://www.friendly_upload_url.com"
}

RestClient.put "https://www.friendly_upload_url.com", "Content-Range"=>"bytes=0-3", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 201 Created | 0 bytes, 1.46s

RestClient.put "https://www.friendly_upload_url.com", "Content-Range"=>"bytes=4-7", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 201 Created | 0 bytes, 1.46s

RestClient.put "https://www.friendly_upload_url.com", "Content-Range"=>"bytes=8-11", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 201 Created | 0 bytes, 1.46s

RestClient.put "https://www.friendly_upload_url.com", "Content-Range"=>"bytes=11-13", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 201 Created | 0 bytes, 1.46s

RestClient.post "https://www.friendly_upload_url.com", "{\"commit\":true}", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "Content-Length"=>"88", "Content-Type"=>"application/json", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 201 Created | 0 bytes, 1.46s

OUTPUT
{
  "file_size": 13,
  "file_path": "/path/to/sample/file",
  "file_name": "file_name"
}
```

### Variations to mock streams

Beyond mocking streams by declaring chunks manually, you can mock streams in a variety of ways.

> **TIP**
> 
> Take note that streams can take longer than your average actions to finish execution - depending on the size of the file and network. It is recommended to test with smaller files rather than production sizes.

Mock streams with each chunk explicitly

```JSON
{
    "file": {
      "__stream__": true,
      "chunks": {
        "0": "abcd",
        "4": "efgh",
        "8": "ijkl",
        "12": "mn"
      }
    }
}
```

Mock streams by utilizing a stream implemented for a download file action/trigger in the same connector

```JSON
{
    "file": {
      "__stream__": true,
      "name": "stream_within_same_connector", # name of the stream in the connector
      "input": { # input that will be passed to the stream callback
        "file_path": "/path/to/sample/file"
      }
    },
}
```

Mock streams by providing a static stream

```JSON
{
    "file": {
      "data": "123456789",
      "eof": true
    },
}
```

Mock streams by providing a string

```JSON
{
    "file": "qwertyuiop[]"
}
```

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/cli/triggers.md
description: >-
  Run and debug connector triggers locally with the Workato SDK gem on the
  command line to develop and test your custom connector.
---

# How-to guides - Running Triggers on CLI

In this segment, we will be going through how you can run triggers using the Workato Gem.

## Prerequisites

- You have installed and can run the Workato SDK Gem. Read our [getting-started guide](/en/developing-connectors/sdk/cli/guides/getting-started) to know more.
- You have a working connector with at least 1 trigger. You use the sample provided below.
- You have a working set of credentials. If you are using a sample connector code, ensure that you have the appropriate credentials for the connector.

## Sample connector - Chargebee

The code in `connector.rb`.

```ruby
{
  title: 'Chargebee-demo',

  connection: {
    fields: [
      {
        name: 'api_key',
        control_type: 'password',
        hint: 'You can find your API key final change3' \
          "under 'Settings'=>'Configure Chargebee'=>'API Keys and Webhooks'" \
          " in Chargebee's web console.",
        label: 'Your API Key'
      },
      {
        name: 'domain',
        control_type: 'subdomain',
        url: 'chargebee.com'
      }
    ],

    authorization: {
      type: 'basic_auth',

      apply: lambda do |connection|
        user(connection['api_key'])
      end
    },

    base_uri: lambda do |connection|
      "https://#{connection['domain']}.chargebee.com"
    end
  },

  test: lambda do |_connection|
    get('/api/v2/plans', limit: 1)
  end,

  triggers: {
    new_updated_object: {

      description: lambda do |_input, picklist_label|
        "New/updated <span class='provider'>#{picklist_label['object'] || 'object'}</span> in <span class='provider'>Chargebee</span>"
      end,

      config_fields: [
        {
          name: 'object',
          control_type: 'select',
          pick_list: 'objects',
          optional: false
        }
      ],

      input_fields: lambda do
        [
          {
            name: 'since',
            type: :date_time,
            optional: true,
            sticky: true
          }
        ]
      end,

      poll: lambda do |_connection, input, closure|
        page_size = 100
        closure = {} if closure.blank?
        closure['updated_since'] = (closure['updated_since'] || input['since'] || 1.hour.ago).to_time.utc.to_i

        params = {
          "sort_by[asc]": 'updated_at',
          limit: page_size,
          "updated_at[after]": closure['updated_since']
        }

        params['offset'] = closure['offset']

        response = get("/api/v2/#{input['object'].pluralize}", params)

        if response['next_offset'].present?
          closure['offset'] = response['next_offset']
        else
          closure['offset'] = nil
          unless response['list'].size == 0
            closure['updated_since'] =
              response['list'].last[input['object']]['updated_at']
          end
        end

        {
          events: response['list'],
          next_poll: closure,
          can_poll_more: response['next_offset'].present?
        }
      end,

      dedup: lambda do |event|
        if event['subscription'].present?
          "#{event['subscription']['id']}@#{event['subscription']['updated_at']}"
        else
          "#{event['customer']['id']}@#{event['customer']['updated_at']}"
        end
      end,

      output_fields: lambda do |object_definitions|
        object_definitions['new_updated_object_output']
      end
    },

  },
}
```

Credentials in `settings.yaml.enc` .

```yaml
api_key: valid_api_key
domain: valid_domain
```

> **TIP**
> 
> If you're using an encrypted settings.yaml file, you will need to use `workato edit <PATH>` to edit or create the file. Refer to [workato edit](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-edit) for more information on editing encrypted files.

With the SDK Gem, you'll be able to invoke individual lambda functions in your action and gain greater control over how each part of your action works. For example, you may run your `execute` lambda function independently from your `input_fields` lambda.

## Running your input fields and output fields lambdas

In this guide, we will be covering output\_fields lambdas. You can run input\_fields lambdas the same way.

> **TIP**
> 
> Sometimes, you may find yourself with a sample payload request or response. You can also use the `workato generate schema` CLI command to convert this payload easily into Workato schema. Learn more about [Workato CLI generate schema](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-generate-schema).

Your output\_fields lambda is expected to return Workato schema which corresponds to the input fields we should show to the user. In the case we have above, when you invoke the `output_fields` lambda, the Gem will handle the evaluation of any downstream `object_definitions` or `methods` you have referenced.

```shell
$ workato exec triggers.new_updated_object.output_fields --config-fields='fixtures/triggers/new_updated_object/customer_config.json'

[
  {
    "name": "customer",
    "type": "object",
    "properties": [
      {
        "control_type": "text",
        "label": "ID",
        "type": "string",
        "name": "id"
      },
      # More Schema here
    ]
  }
]
```

> **TIP**
> 
> You can also use other options like `--verbose` to see the detailed logs of any HTTP requests sent when building your `output_fields` and `--output` to save the output of the function to a JSON file.
> 
> You do not need to pass anything for the object\_definitions argument as the gem can reference it when it looks at your connector.

## Running your poll lambda

Your poll lambda is expected to return a hash which represents the output of the poll lambda. You have two ways to run your poll lambda to test functionality.

1. [Running your poll lambda with pagination](#running-your-poll-lambda-with-pagination)
2. [Running your poll lambda without pagination](#running-your-poll-lambda-without-pagination)

### Running your poll lambda with pagination

This is done with the command `.poll` which tells the SDK Gem to paginate through all records if `can_poll_more` is true. In the example below, you can see that we have given `.poll` and given the `since` input of `6/09/2021`. The SDK Gem would then send as many requests as necessary to simulate the polling mechanism. You can see that we have referenced an `input` in the command which points to a JSON file stored in our `fixtures` folder. This file should contain the actual value passed to the `poll` lambda from the `input_fields` and `config_fields`.

The `fixtures/triggers/new_updated_object/customer_input_poll.json` file in this example contains the following:

```JSON
{
  "object": "customer",
  "since": "6/09/2021"
}
```

```shell
$ workato exec triggers.new_updated_object.poll --input='fixtures/triggers/new_updated_object/customer_input_poll.json' --verbose

SETTINGS
{
  "api_key": "valid_api_key",
  "domain": "valid_domain"
}
INPUT
{
  "object": "customer",
  "since": "6/09/2021"
}

RestClient.get "https://live_Zbaoo7hGqvi3cqrza8WiXxQa8kBPAPQF@empressporridge.chargebee.com/api/v2/customers?limit=10&offset=&sort_by%5Basc%5D=updated_at&updated_at%5Bafter%5D=1630857600", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 2608 bytes
RestClient.get "https://live_Zbaoo7hGqvi3cqrza8WiXxQa8kBPAPQF@empressporridge.chargebee.com/api/v2/customers?limit=10&offset=%5B%221630857607410%22%2C%2240736845%22%5D&sort_by%5Basc%5D=updated_at&updated_at%5Bafter%5D=1630857600", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 1800 bytes
Progress: |=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---|

OUTPUT
{
  "events": [
    {
      "customer": {
        "id": "abc",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone": "+100",
        "auto_collection": "on",
        "net_term_days": 0,
        "allow_direct_debit": false,
        "created_at": 1629814951,
        "taxability": "taxable",
        "updated_at": 1630857613,
        "locale": "en-SG",
        "pii_cleared": "active",
        "resource_version": 1630857613348,
        "deleted": false,
        "object": "customer",
        "card_status": "valid",
        "promotional_credits": 0,
        "refundable_credits": 0,
        "excess_payments": 0,
        "unbilled_charges": 0,
        "preferred_currency_code": "SGD",
      },
    },
    # More customers here
  ],
  "can_poll_more": false,
  "next_poll": {
    "updated_since": 1630857613,
    "offset": null
  }
}
```

Note that we have used `--verbose` so the SDK gem has printed out more information including the API requests and responses.

> **TIP**
> 
> You can also use other options like `--output` to save the output of the function to a JSON file.
> 
> You can see that the `config_field` - `object` is passed in the input json. In Workato, config\_fields are merged with normal `input_fields` when received in the `execute`, `poll` or `webhook` lambdas.

### Running your poll lambda without pagination

This is done with the command `.poll_page` which tells the SDK Gem to only invoke the `poll` lambda once regardless of the `can_poll_more` value. In the example below, you can see that we have given `.poll` and given the `since` input of `6/09/2021`. The SDK Gem sends a single request and stops execution after the first request is done.

```shell
workato exec triggers.new_updated_object.poll_page --input='fixtures/triggers/new_updated_object/customer_input_poll.json' --verbose

SETTINGS
{
  "api_key": "valid_api_key",
  "domain": "valid_domain"
}
INPUT
{
  "object": "customer",
  "since": "6/09/2021"
}

RestClient.get "https://live_Zbaoo7hGqvi3cqrza8WiXxQa8kBPAPQF@empressporridge.chargebee.com/api/v2/customers?limit=10&offset=&sort_by%5Basc%5D=updated_at&updated_at%5Bafter%5D=1630857600", "Accept"=>"application/json", "Accept-Encoding"=>"gzip, deflate", "User-Agent"=>"rest-client/2.0.2 (darwin19.6.0 x86_64) ruby/2.4.10p364"
# => 200 OK | application/json 2608 bytes

Progress: |=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---|

OUTPUT
{
  "events": [
    {
      "customer": {
        "id": "abc",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone": "+100",
        "auto_collection": "on",
        "net_term_days": 0,
        "allow_direct_debit": false,
        "created_at": 1629814951,
        "taxability": "taxable",
        "updated_at": 1630857613,
        "locale": "en-SG",
        "pii_cleared": "active",
        "resource_version": 1630857613348,
        "deleted": false,
        "object": "customer",
        "card_status": "valid",
        "promotional_credits": 0,
        "refundable_credits": 0,
        "excess_payments": 0,
        "unbilled_charges": 0,
        "preferred_currency_code": "SGD",
      },
    },
    # More customers here
  ],
  "next_poll": {
    "updated_since": 1630857600,
    "offset": "[\"1630857607410\",\"40736845\"]"
  },
  "can_poll_more": true
}
```

Note that we have used `--verbose` so the SDK gem has printed out more information including the API requests and responses.

> **TIP**
> 
> You can also use other options like `--output` to save the output of the function to a JSON file.
> 
> You can see that the `config_field` - `object` is passed in the input json. In Workato, config\_fields are merged with normal `input_fields` when received in the `execute`, `poll` or `webhook` lambdas.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/cli/methods.md
description: >-
  Run connector methods locally with the Workato SDK gem on the command line to
  develop and debug your custom connector code.
---

# How-to guides - Running methods on CLI

In this segment, we will be going through how you can run methods using the Workato Gem.

## Prerequisites

- You have installed and can run the Workato SDK Gem. Read our [getting-started guide](/en/developing-connectors/sdk/cli/guides/getting-started) to know more.
- You have a working connector with at least 1 method. You use the sample connector provided below.
- You have a working set of credentials. If you are using a sample connector code, ensure that you have the appropriate credentials for the connector.

## Sample connector - Chargebee

The code in `connector.rb`.

```ruby
{
  title: 'Chargebee-demo',

  connection: {
    fields: [
      {
        name: 'api_key',
        control_type: 'password',
        hint: 'You can find your API key final change3' \
          "under 'Settings'=>'Configure Chargebee'=>'API Keys and Webhooks'" \
          " in Chargebee's web console.",
        label: 'Your API Key'
      },
      {
        name: 'domain',
        control_type: 'subdomain',
        url: 'chargebee.com'
      }
    ],

    authorization: {
      type: 'basic_auth',

      apply: lambda do |connection|
        user(connection['api_key'])
      end
    },

    base_uri: lambda do |connection|
      "https://#{connection['domain']}.chargebee.com"
    end
  },

  test: lambda do |_connection|
    get('/api/v2/plans', limit: 1)
  end,

  methods: {
    get_customers: lambda do
      get('/api/v2/customers')
    end,

    sample_method: lambda do |string1, string2|
      string1 + ' ' + string2
    end,
  },
}
```

Credentials in `settings.yaml.enc` .

```yaml
api_key: valid_api_key
domain: valid_domain
```

> **TIP**
> 
> If you're using an encrypted settings.yaml file, you will need to use `workato edit <PATH>` to edit or create the file. Refer to [workato edit](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-edit) for more information on editing encrypted files.

With the SDK Gem, you'll be able to invoke a method individually and gain greater control over how each method works.

## Example 1. Running the `get_customers` method

The `get_customers` method in the preceding example has no declared input arguments. The method fetches customers and returns the API response when the SDK Gem invokes it.

```shell
$ workato exec methods.get_customers
{
  "list": [
    {
      "customer": {
        "id": "abc",
        "first_name": "John",
        "last_name": "doe",
        "email": "john@gmail.com",
        "phone": "+100",
        "auto_collection": "on",
        "net_term_days": 0,
        "allow_direct_debit": false,
        "created_at": 1630848839,
        "taxability": "taxable",
        "updated_at": 1630848840,
        "locale": "en-US",
        "pii_cleared": "active",
        "resource_version": 1630848840782,
        "deleted": false,
        "object": "customer",
        "card_status": "valid",
        "promotional_credits": 0,
        "refundable_credits": 0,
        "excess_payments": 0,
        "unbilled_charges": 0,
        "preferred_currency_code": "SGD",
      }
    }
  ],
  "next_offset": "[\"1630848839000\",\"42903379\"]"
}
```

> **TIP**
> 
> You can also use other options like `--verbose` to see the detailed logs of any HTTP requests sent when your method is ran and `--output` to save the output of the function to a JSON file.
> 
> If no `settings.yaml` file is defined, the SDK Gem will assume the default `settings.yaml.enc` file to utilize for any HTTP requests.

## Example 2. Running the `sample_method` method

The second method we will cover in the example above is the `sample_method` method, which has 2 arguments. You can see that we have referenced an `args` in the command which points to a JSON file stored in our `fixtures` folder. This file should contain an array **where each index in the array corresponds to a single argument.**

The `fixtures/triggers/new_updated_object/customer_input_poll.json` file in this example contains the following:

```JSON
[
    "Hello",
    "world"
]
```

Here is an example the method being run:

```shell
$ workato exec methods.sample_method --args='fixtures/actions/search_customers/customer_config.json'
"Hello world"
```

> **TIP**
> 
> You can also use other options like `--verbose` to see the detailed logs of any HTTP requests sent when your method is ran and `--output` to save the output of the function to a JSON file.
> 
> If no `settings.yaml` file is defined, the SDK Gem will assume the default `settings.yaml.enc` file to utilize for any HTTP requests.

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/cli/guides/cli/pick_lists.md
description: >-
  Run connector picklists locally with the Workato SDK gem on the command line
  to develop and debug your custom connector code.
---

# How-to guides - Running Picklists on CLI

In this segment, we will be going through how you can run methods Picklists the Workato Gem.

## Prerequisites

- You have installed and can run the Workato SDK Gem. Read our [getting-started guide](/en/developing-connectors/sdk/cli/guides/getting-started) to know more.
- You have a working connector with at least 1 method. You use the sample connector provided below.
- You have a working set of credentials. If you are using a sample connector code, ensure that you have the appropriate credentials for the connector.

## Sample connector - Chargebee

The code in `connector.rb`.

```ruby
{
  title: 'Chargebee-demo',

  connection: {
    fields: [
      {
        name: 'api_key',
        control_type: 'password',
        hint: 'You can find your API key final change3' \
          "under 'Settings'=>'Configure Chargebee'=>'API Keys and Webhooks'" \
          " in Chargebee's web console.",
        label: 'Your API Key'
      },
      {
        name: 'domain',
        control_type: 'subdomain',
        url: 'chargebee.com'
      }
    ],

    authorization: {
      type: 'basic_auth',

      apply: lambda do |connection|
        user(connection['api_key'])
      end
    },

    base_uri: lambda do |connection|
      "https://#{connection['domain']}.chargebee.com"
    end
  },

  test: lambda do |_connection|
    get('/api/v2/plans', limit: 1)
  end,

  pick_lists: {

    static: lambda do
      [
        %w[Subscription subscription],
        %w[Customer customer],
        %w[Plans plan]
      ]
    end,

    dynamic: lambda do
      get('/api/v2/customers')['list'].map do |index|
          [
            index['customer']['first_name'],
            index['customer']['id']
          ]
      end
    end,

    dependent: lambda do |connection, params|
      get('/api/v2/customers', params)['list'].map do |index|
          [
            index['customer']['first_name'],
            index['customer']['id']
          ]
      end
    end,

    dependent_with_names: lambda do |connection, limit:|
      get('/api/v2/customers', limit: limit)['list'].map do |index|
          [
            index['customer']['first_name'],
            index['customer']['id']
          ]
      end
    end

  },
}
```

Credentials in `settings.yaml.enc` .

```yaml
api_key: valid_api_key
domain: valid_domain
```

> **TIP**
> 
> If you're using an encrypted settings.yaml file, you will need to use `workato edit <PATH>` to edit or create the file. Refer to [workato edit](/en/developing-connectors/sdk/cli/reference/cli-commands#workato-edit) for more information on editing encrypted files.

With the SDK Gem, you'll be able to invoke a picklist individually.

## Example 1. Running the `static` pick\_list

The first pick\_list we will cover in the example above is the `static` pick\_list. Like it's name suggests, it stores a static list of values and when invoked, will just return this value.

Here is an example the pick\_list being run:

```shell
$ workato exec pick_lists.static
[
  [
    "Subscription",
    "subscription"
  ],
  [
    "Customer",
    "customer"
  ],
  [
    "Plans",
    "plan"
  ]
]
```

## Example 2. Running the `dynamic` pick\_list

The next pick\_list is one that sends a request out and massages the response into a pick\_list format. Here, the connection settings required to authorize the request is assumed to be the default `settings.yaml.enc` file. If this is not what you want, you can use `--settings` to override this.

Here is an example the pick\_list being run:

```shell
$ workato exec pick_lists.dynamic
[
  [
    "dd",
    "AzyuHzSiORQAo1JUb"
  ],
  [
    "fdsfdf",
    "16Bji8SfZHHDm7v"
  ]
]
```

## Example 3. Running the `dependent` pick\_list

The next pick\_list is one that sends a request out and massages the response into a pick\_list format. Here, the connection settings required to authorize the request is assumed to be the default `settings.yaml.enc` file. If this is not what you want, you can use `--settings` to override this.

The `fixtures/pick_lists/dependent/input.json` file in this example contains the following:

```JSON
{
    "limit": "1"
}
```

Here is an example the pick\_list being run:

```shell
$ workato exec pick_lists.dependent --args='fixtures/pick_lists/dependent/input.json'
[
  [
    "dd",
    "AzyuHzSiORQAo1JUb"
  ]
]
```

## Example 4. Running the `dependent_with_names` pick\_lists

In other cases, you might have a picklist that accepts named arguments. In this case, this picklist has the named argument `limit:`.

When you pass the arguments via CLI, the contents of the file `fixtures/pick_lists/dependent_with_names/input.json` should look like this:

```JSON
{
    "limit": "1"
}
```

Here is an example the pick\_list being run:

```shell
$ workato exec pick_lists.dependent_with_names --args='fixtures/pick_lists/dependent_with_names/input.json'
[
  [
    "dd",
    "AzyuHzSiORQAo1JUb"
  ]
]
```

---
