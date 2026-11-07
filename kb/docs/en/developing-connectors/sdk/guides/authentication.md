---
url: 'https://docs.workato.com/en/developing-connectors/sdk/guides/authentication.md'
description: >-
  Learn the authentication methods the Workato SDK supports for custom
  connectors, including basic, API key, OAuth 2.0, JWT, and AWS.
---

# Building connections

When connecting to an API, you must first authenticate your custom connector. To do this, you must "inform" the API that it can trust you and send potentially sensitive information to you.

Workato supports the following formalized forms of authentication. You can also add custom approaches to authenticate yourself. Read the documentation for the API to choose the form of authentication that is most suitable for the custom connector that you are building.

- [Basic authentication](/en/developing-connectors/sdk/guides/authentication/basic-authentication)
- [API key authentication](/en/developing-connectors/sdk/guides/authentication/api-key)
- [Header authentication](/en/developing-connectors/sdk/guides/authentication/header-auth)
- [JWT authentication](/en/developing-connectors/sdk/guides/authentication/jwt)
- [OAuth 2.0 authentication (Auth code grant)](/en/developing-connectors/sdk/guides/authentication/oauth/auth-code)
- [OAuth 2.0 authentication (Auth code grant with PKCE)](/en/developing-connectors/sdk/guides/authentication/oauth/auth-code-pkce)
- [OAuth 2.0 authentication (Client Credentials)](/en/developing-connectors/sdk/guides/authentication/oauth/client-credentials)
- [OAuth 2.0 authentication (ROPC)](/en/developing-connectors/sdk/guides/authentication/oauth/ropc)
- [AWS authentication](/en/developing-connectors/sdk/guides/authentication/aws_auth)
- [On-premise authentication](/en/developing-connectors/sdk/guides/authentication/on-prem)
- [Custom authentication](/en/developing-connectors/sdk/sdk-reference/connection/authorization)
- [Multiple authentication formats in a single connector](/en/developing-connectors/sdk/guides/authentication/multi_auth)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/authentication/basic-authentication.md
description: >-
  Set up basic authentication for a Workato SDK connector using a username and
  password in the connection fields definition.
---

# How-to Guide - Basic Authentication

Typically, a basic authentication requires a username and password combination when making requests. Make sure to include those two fields in the connection fields definition.

## Sample Connector - ClickTime

```ruby
{
  title: 'ClickTime',

  connection: {
    fields: [
      {
        name: 'username',
        optional: true,
        hint: 'Your email used for login'
      },
      {
        name: 'password',
        control_type: 'password',
      }
    ],

    authorization: {
      type: 'basic_auth',

      apply: lambda do |connection|
        user(connection['username'])
        password(connection['password'])
      end
    },

    base_uri: lambda do |connection|
      "https://app.clicktime.com"
    end
  },

  test: lambda do |connection|
    get("/api/1.3/session")
  end

  #More connector code here
}
```

- Refer to the [full ClickTime connector code](https://github.com/workato/custom_connector_docs/blob/master/custom_connectors/basic_auth/click_time_connector.rb) for a complete example.
- Check out the [ClickTime API](https://support.clicktime.com/hc/en-us/articles/360002884071-REST-API-v2-General-Information#basic)

## Step 1 - Defining Connection fields

This component tells Workato what fields to show to a user trying to establish a connection. In the case of Basic Authentication, you would need the `username` and `password` of the end user to establish a connection.

| Information from User | Description |
| --- | --- |
| username | The username of the individual who will authenticate the connection. |
| password | The password of the individual who will authenticate the connection. |

This is done in the `fields` key, which accepts an array of hashes. Each hash in this array corresponds to a separate input field.

```ruby
    fields: [
      {
        name: 'username',
        optional: true,
        hint: 'Your email used for login'
      },
      {
        name: 'password',
        control_type: 'password',
      }
    ],
```

![Configured ClickTime connection fields](/assets/clicktime_conn.BG1KzMy5.png)

> **TIP**
> 
> When defining fields, you need to at least provide the `name` key. Additional attributes like `optional`, `hint` and `control_type` allow you to customize other aspects of these fields. For sensitive information like Client Secrets, remember to use the `control_type` as `password`.
> 
> Refer to [Connection fields](/en/developing-connectors/sdk/sdk-reference/connection#fields) for more information on defining input fields in Workato.

## Step 2 - Defining authorization

This component tells Workato what to do with the values received from the input fields to establish a connection. This is handled through your `authorization` key. In this key, you begin by first defining the `type` of authorization. For Basic authentication, you should use `basic_auth`.

```ruby
    authorization: {
      type: 'basic_auth',

      apply: lambda do |connection|
        user(connection['username'])
        password(connection['password'])
      end
    }
```

## Step 3 - Applying the credentials to subsequent HTTP requests

Next, you need to tell Workato how to make use of the username and password you expect to receive from a user of this connector. This is done in the `apply` key where you can reference the username and password collected through the `connection` argument. Any instructions you introduce in the `apply` key are subsequently applied to all HTTP requests this connector sends after connection is established.

In this example, we have defined the username we received (`connection['username']`) to be added to the `user` field of any request. The same has been done for the password (`connection['password']`) to be added to the `password` field of any request.

## Step 4 - Setting the API's base URI

This component tells Workato what the base URL of the API is. This key is optional but allows you to provide only relative paths in the rest of your connector when defining HTTP requests. Refer to [base URI configuration](/en/developing-connectors/sdk/sdk-reference/connection#base-uri) for more information on configuring your `base_uri`.

```ruby
    base_uri: lambda do |connection|
      "https://app.clicktime.com"
    end
```

> **TIP**
> 
> This lambda function also has access to the `connection` argument. This is especially useful if the base URI of the API might change based on the user's instance. The `connection` argument can be accessed in the following format:
> 
> ```ruby
>     base_uri: lambda do |connection|
>       "https://#{connection['domain']}.com/api"
>     end
> ```

## Step 5 - Testing the connection

Now that we have defined the fields we need to collect from an end user and what to do with the inputs from those fields, we now need a way to test this connection. This is handled in the `test` key. Take note that this is a root level key - outside of the `connection` definition.

```ruby
    test: lambda do |connection|
      get("/api/1.3/session")
    end
```

In this key, you need to provide an endpoint that allows us to send a sample request using the new credentials we just received. If we receive a 200 OK HTTP response, we show the connection as Successful. In the example above, we are sending a `GET` request to the `/api/1.3/session` endpoint and expecting a 200 response if the username and password provided are valid.

## Connections SDK reference

To be more familiar with the available keys within the `connection` key and their parameters, check out our [SDK reference](/en/developing-connectors/sdk/sdk-reference/connection).

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/authentication/api-key.md
description: >-
  Set up API key authentication for a Workato SDK connector, passing the key
  through URL parameters, headers, or credentials.
---

# How-to Guide - API Key Authentication

API key authentication is an authentication method that traditionally asks users to generate API keys in the application that they want to connect to. This API key may be scoped to the permissions of the user generating them or permissions could be configured on a key by key basis.

There are a variety of ways in which an API may expect to receive an API key. Common examples include:

- Adding them in the URL parameters of each request (`GET www.api.com/resource?api-key=XXX`)
- Adding them in the headers of each request (`X-API-KEY: XXX`)
- Adding them to the username or password field of each request (`-u XXX` or `-u :XXX`)

## Sample Connector - Iterable

```ruby
{
  title: 'Iterable',

  connection: {
    fields: [
      {
        name: 'api_key',
        label: 'API key',
        control_type: 'password',
        optional: false,
        hint: 'Get your <b>standard</b> API key <a href="https://app.' \
        'iterable.com/settings/apiKeys" target="_blank">here</a>.'
      }
    ],

    authorization: {
      type: 'api_key',

      apply: lambda do |connection|
        headers(api_key: connection['api_key'])
      end
    },

    base_uri: lambda do |connection|
      'https://api.iterable.com'
    end
  },

  test: lambda do |connection|
    get('/api/channels')
  end,

  #More connector code here
}
```

- Refer to the [full Iterable connector code](https://github.com/workato/custom_connector_docs/blob/master/custom_connectors/api_key_auth/iterable.rb) for a complete example.
- Check out the [Iterable API](https://api.iterable.com/api/docs)

## Step 1 - Defining Connection fields

This component tells Workato what fields to show to a user trying to establish a connection. In the case of API key authentication, you would need the `API key` that the user has generated in Iterable.

| Information from User | Description |
| --- | --- |
| api key | The api key generated by the end user for Workato. |

This is done in the `fields` key, which accepts an array of hashes. Each hash in this array corresponds to a separate input field.

```ruby
    fields: [
      {
        name: 'api_key',
        label: 'API key',
        control_type: 'password',
        optional: false,
        hint: 'Get your <b>standard</b> API key <a href="https://app.' \
        'iterable.com/settings/apiKeys" target="_blank">here</a>.'
      }
    ],
```

![Configured Iterable connection fields](/assets/iterable_conn.CIgMbYy4.png)

> **TIP**
> 
> When defining fields, you need to at least provide the `name` key. Additional attributes like `optional`, `hint` and `control_type` allow you to customize other aspects of these fields. For sensitive information like Client Secrets, remember to use the `control_type` as `password`.
> 
> Refer to [Connection fields](/en/developing-connectors/sdk/sdk-reference/connection#fields) for more information on how to define input fields in Workato.

## Step 2 - Defining authorization

This component tells Workato what to do with the values received from the input fields to establish a connection. This is handled through your `authorization` key. In this key, you begin by first defining the `type` of authorization. For API Key authentication, you should use `api_key`.

```ruby
    authorization: {
      type: 'api_key',

      apply: lambda do |connection|
        headers(api_key: connection['api_key'])
      end
    },
```

## Step 3 - Applying the credentials to subsequent HTTP requests

Next, you need to tell Workato how to make use of the API key you expect to receive from a user of this connector. This is done in the `apply` key where you can reference the API Key collected through the `connection` argument. Any instructions you introduce in the `apply` key are subsequently applied to all HTTP requests this connector sends after connection is established.

In this example, we have defined the API key we received (`connection['api_key']`) to be added to the headers of any request. For every HTTP request sent, the headers will contain `api_key: XXX` where `XXX` is the API key.

## Step 4 - Setting the API's base URI

This component tells Workato what the base URL of the API is. This key is optional but allows you to provide only relative paths in the rest of your connector when defining HTTP requests. Refer to [base URI configuration](/en/developing-connectors/sdk/sdk-reference/connection#base-uri) for more information on configuring your `base_uri`.

```ruby
    base_uri: lambda do |connection|
      "https://api.iterable.com"
    end
```

> **TIP**
> 
> This lambda function also has access to the `connection` argument. This is especially useful if the base URI of the API might change based on the user's instance. The `connection` argument can be accessed in the following format:
> 
> ```ruby
>     base_uri: lambda do |connection|
>       #some code here
>     end
> ```

## Step 5 - Testing the connection

Now that we have defined the fields we need to collect from an end user and what to do with the inputs from those fields, we now need a way to test this connection. This is handled in the `test` key.

```ruby
    test: lambda do |connection|
      get('/api/channels')
    end,
```

In this key, you need to provide an endpoint that allows us to send a sample request using the new credentials we just received. If we receive a 200 OK HTTP response, we show the connection as Successful. In the example above, we are sending a `GET` request to the `/api/channels` endpoint and expecting a 200 response if the API key is valid.

## Variations

In cases when you need to send the API keys in the URL parameters or User fields in each request, you simply need to modify your `apply` key.

### API key in URL parameters

```ruby
    authorization: {
      type: 'api_key',

      apply: lambda do |connection|
        params(api_key: connection['api_key']) # For URL parameters
      end
    },
```

### API key in Username field

```ruby
    authorization: {
      type: 'api_key',

      apply: lambda do |connection|
        user(connection['api_key']) # For username
        password("") # user method needs to be accompanied with an empty password declaration.
      end
    },
```

## Connections SDK reference

To be more familiar with the available keys within the `connection` key and their parameters, check out our [SDK reference](/en/developing-connectors/sdk/sdk-reference/connection).

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/authentication/header-auth.md
description: >-
  Set up header authentication for a Workato SDK connector by passing a
  user-supplied token in the request authorization header.
---

# How-to Guides - Header Authentication

For APIs requiring header authentication, this can be easily accomplished if the token is supplied by the user directly through user input fields.

## Sample connector - Generic connector

```ruby
{
  title: 'My connector',

  connection: {

    fields: [
      {
        name: "token",
        control_type: "string",
        label: "Bearer token",
        optional: false,
        hint: "Available in 'My Profile' page"
      }
    ],

    authorization: {
      type: 'custom_auth',

      apply: lambda do |connection|
        headers("Authorization": "Bearer #{connection["token"]}")
      end
    },

    base_uri: lambda do |connection|
      "https://api.acmestudios.com"
    end
  },

  test: lambda do |connection|
    get('/me')
  end,
}
```

## Step 1 - Defining Connection fields

In the `connection` key, we define the input fields in the `fields` key in an array of hashes. Each hash in the array represents a single input field. Inside, we will be able to declare the name of the input field, hints that are displayed to the end user among other parameters. In our example, we define the 'token' input fields.

> **TIP**
> 
> When defining fields, you need to at least provide the `name` key. Additional attributes like `optional`, `hint` and `control_type` allow you to customize other aspects of these fields. For sensitive information like Client Secrets, remember to use the `control_type` as `password`.
> 
> Refer to [Connection fields](/en/developing-connectors/sdk/sdk-reference/connection#fields) for more information on defining input fields in Workato.

## Step 2 - Applying the token to subsequent HTTP requests

In the `apply` key, we pass in the token provided by the user in `header()` in the from of a key-value pair. By doing so, Workato will append the token to every HTTP request made by the connector to help authenticate each request.

## Step 3 - Setting the API's base URI

This component tells Workato what the base URL of the API is. This key is optional but allows you to provide only relative paths in the rest of your connector when defining HTTP requests. Refer to [base URI configuration](/en/developing-connectors/sdk/sdk-reference/connection#base-uri) for more information on configuring your `base_uri`.

```ruby
    base_uri: lambda do |connection|
      "https://api.acmestudios.com"
    end
```

> **TIP**
> 
> This lambda function also has access to the `connection` argument. This is especially useful if the base URI of the API might change based on the user's instance. The `connection` argument can be accessed in the following format:
> 
> ```ruby
>     base_uri: lambda do |connection|
>       "https://#{connection['domain'].com/api}"
>     end
> ```

## Step 4 - Testing the connection

Now that we have defined the fields we need to collect from an end user and what to do with the inputs from those fields, we now need a way to test this connection. This is handled in the `test` key.

```ruby
    test: lambda do |connection|
      get("/me")
    end
```

In this block, you need to provide an endpoint that allows us to send a sample request using the new credentials we just received. If we receive a 200 OK HTTP response, we show the connection as Successful. In the example above, we are sending a `GET` request to an example endpoint `/me` and expecting a 200 response if the token is valid.

## Connections SDK reference

To be more familiar with the available keys within the `connection` key and their parameters, check out our [SDK reference](/en/developing-connectors/sdk/sdk-reference/connection).

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/authentication/jwt.md
description: >-
  Set up JSON web token (JWT) authentication for a Workato SDK connector,
  signing tokens with a private or public key.
---

# How-to guides - JSON web token authentication

JSON Web Token(JWT) is an Internet standard for creating data with optional signature and/or optional encryption whose payload holds JSON that asserts some number of claims.

In authentication, JWTS are signed either using a private or public key. For example, a server could generate a token that has the claim "logged in as admin" and provide that to a client. The client could then use that token to prove that it is logged in as admin. The authorized client can then pull information that admins are cleared to access.

JWTs are designed to be compact, URL-safe, and usable especially in a web-browser single-sign-on (SSO) context.

Refer to the [JWT Introduction](https://jwt.io/introduction/) for more information on JSON web tokens.

## Sample connector - Google calendar connector

```ruby
{
  title: 'My Google calendar connector',

  connection: {
    fields: [
      {
        name: 'iss',
        label: 'Issuer',
        optional: false,
        hint: 'The email address of the service account'
      },
      {
        name: 'sub',
        label: 'Email address',
        optional: false,
        hint: 'Email address of the user that you are impersonating'
      },
      {
        name: 'private_key',
        optional: false,
        hint: 'Copy and paste the private key that came from the downloaded json.<br>' \
          "Click <a href='https://developers.google.com/identity/protocols/oauth2/service-account/' " \
          "target='_blank'>here</a> to learn more about Google Service Accounts.",
        control_type: 'password',
        multiline: true
      }
    ],

    authorization: {
      type: 'custom_auth',

      acquire: lambda do |connection|
        jwt_body_claim = {
          "iat": now.to_i,
          "exp": 1.hour.from_now.to_i,
          "aud": 'https://oauth2.googleapis.com/token',
          "iss": connection['iss'],
          "sub": connection['sub'],
          "scope": 'https://www.googleapis.com/auth/calendar'
        }
        private_key = connection['private_key'].gsub(/\\n/, "\n")
        jwt_token = workato.jwt_encode(
          jwt_body_claim,
          private_key,
          "RS256"
        )

        post('https://oauth2.googleapis.com/token').
          payload(grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
            assertion: jwt_token).
          request_format_www_form_urlencoded
      end,

      apply: lambda do |connection|
        headers("Authorization": "Bearer #{connection['access_token']}")
      end,

      refresh_on: [401, 403]
    },

    base_uri: lambda do |connection|
      'https://www.googleapis.com/calendar/v3'
    end
  },

  test: lambda do |connection|
    get('/colors')
  end,

  # More connector code here
}
```

- Refer to the [full Google Calendar connector code](https://app.workato.com/custom_adapters/27268/code?token=08f9f02a) for a complete example.
- Check out the [Google calendar API](https://developers.google.com/calendar/v3/reference)

## Step 1 - Defining Connection fields

This component tells Workato what fields to show to a user trying to establish a connection. In the case of Client Credentials Authentication, you would need the Client ID and Client Secret that the user has generated in Percolate.

| Information needed | Description |
| --- | --- |
| Issuer | The "iss" (issuer) claim identifies the principal that issued the JWT. |
| Subject | The "sub" (subject) claim identifies the principal that is the subject of the JWT. The claims in a JWT are normally statements about the subject. In this case, it is the email address of the user that you are impersonating. |
| Private/public key | This is the "password" that is obtained from the downloaded JSON. |

This is done in the `fields` key, which accepts an array of hashes. Each hash in this array corresponds to a separate input field.

```ruby
    fields: [
      {
        name: 'iss',
        label: 'Issuer',
        optional: false,
        hint: 'The email address of the service account'
      },
      {
        name: 'sub',
        label: 'Email address',
        optional: false,
        hint: 'Email address of the user that you are impersonating'
      },
      {
        name: 'private_key',
        optional: false,
        hint: 'Copy and paste the private key that came from the downloaded json.<br>' \
          "Click <a href='https://developers.google.com/identity/protocols/oauth2/service-account/' " \
          "target='_blank'>here</a> to learn more about Google Service Accounts.",
        control_type: 'password',
        multiline: true
      }
    ],
```

![Configured Google calendar connection fields](/assets/googlecal_conn.BR5-MYQV.png)

> **TIP**
> 
> When defining fields, you need to at least provide the `name` key. Additional attributes like `optional`, `hint` and `control_type` allow you to customize other aspects of these fields. For sensitive information like Client Secrets, remember to use the `control_type` as `password`.
> 
> Refer to [Connection fields](/en/developing-connectors/sdk/sdk-reference/connection#fields) for more information on defining input fields in Workato.

## Step 2 - Defining the authorization type

This component tells Workato what to do with the values received from the input fields to establish a connection. This is handled through your `authorization` key. In this key, you begin by first defining the `type` of authorization. For JWT authentication, you should use `custom_auth`.

```ruby
    type: 'custom_auth'
```

## Step 3 - Acquiring the access token

In the `acquire` key, we first generate a JWT token by creating a JWT body claim and signing it with the private key that the user provided. We do this by passing in the `jwt_body_claim` and `private_key` to Workato, note that this must be sent with `jwt_encode` under the `RS256` signing algorithm. Next, we then pass in the generated token to Google API's token URL as payload. Here, we assign the `grant_type` and `assertion` as `urn:ietf:params:oauth:grant-type:jwt-bearer` and the generated JWT token respectively. Note that the payload of the request must be sent with `request_format_www_form_urlencoded`.

```ruby
    acquire: lambda do |connection|
      jwt_body_claim = {
        "iat": now.to_i,
        "exp": 1.hour.from_now.to_i,
        "aud": 'https://oauth2.googleapis.com/token',
        "iss": connection['iss'],
        "sub": connection['sub'],
        "scope": 'https://www.googleapis.com/auth/calendar'
      }
      private_key = connection['private_key'].gsub(/\\n/, "\n")
      jwt_token = workato.jwt_encode(jwt_body_claim, private_key, "RS256")

      post('https://oauth2.googleapis.com/token').
        payload(grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
          assertion: jwt_token)
        .request_format_www_form_urlencoded
    end,
```

Upon receiving a the request, the API returns a JSON response.

```json
{
  "access_token": "my-authentication-token",
  "token_type": "bearer",
  "expires_in": "seconds-until-expiration",
  "error": "optional-error-message"
}
```

## Step 4 - Applying the access token to subsequent HTTP requests

Next, you need to tell Workato how to make use of the access token it has retrieved from Google calendar. This is done in the `apply` block where you can reference the access token now stored in the `connection` argument. Any instructions you introduce in the `apply` block are subsequently applied to all HTTP requests this connector sends after connection is established.

```ruby
    apply: lambda do |connection|
      headers("Authorization": "Bearer #{connection['access_token']}")
    end
```

In this example, we have defined the access token (`connection['access_token']`) to be added to the headers of any request. For every HTTP request sent, the headers will contain `Authorization: Bearer XXX` where `XXX` is the access token stored in the `connection` hash.

## Step 5 - Defining token refresh behavior

As JWT tokens are only valid for short amounts of time, we need to tell this connector to refresh the JWT token when it expires. This can be easily done with the `refresh_on` key, that contains a list of HTTP response codes or regex functions. This list is matched to any responses to a HTTP request and triggers the `acquire` key is a match is found.

```ruby
    refresh_on: [401, 403],
```

## Step 6 - Setting the API's base URI

This component tells Workato what the base URL of the API is. This key is optional but allows you to provide only relative paths in the rest of your connector when defining HTTP requests. Refer to [base URI configuration](/en/developing-connectors/sdk/sdk-reference/connection#base-uri) for more information on configuring your `base_uri`.

```ruby
    base_uri: lambda do
      'https://www.googleapis.com/calendar/v3'
    end
```

> **TIP**
> 
> This lambda function also has access to the `connection` argument. This is especially useful if the base URI of the API might change based on the user's instance. The `connection` argument can be accessed in the following format:
> 
> ```ruby
>     base_uri: lambda do |connection|
>       "https://#{connection['domain'].com/api}"
>     end
> ```

## Step 7 - Testing the connection

Now that we have defined the fields we need to collect from an end user and what to do with the inputs from those fields, we now need a way to test this connection. This is handled in the `test` key.

```ruby
    test: lambda do |connection|
      get("/colors")
    end
```

In this key, you need to provide an endpoint that allows us to send a sample request using the new credentials we just received. If we receive a 200 OK HTTP response, we show the connection as Successful. In the example above, we are sending a `GET` request to the [`/colors` endpoint](https://developers.google.com/calendar/v3/reference/colors/get) and expecting a 200 response if the JWT is valid.

## Connections SDK reference

To be more familiar with the available keys within the `connection` key and their parameters, check out our [SDK reference](/en/developing-connectors/sdk/sdk-reference/connection).

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/authentication/oauth/auth-code.md
description: >-
  Build a custom connector that authenticates with the OAuth 2.0 authorization
  code grant to impersonate a user when connecting to an API.
---

# How-to Guide - OAuth 2.0 Authorization Code Variant

The OAuth 2.0 Authorization code flow is a way for Workato to impersonate a specific user when authenticating to an API. This is done by getting the user's consent via a browser popup when they first attempt to connect.

## Sample Connector - Podio

```ruby
{
  title: 'My Podio connector',

  connection: {
    fields: [
      {
        name: 'client_id',
        optional: false
      },
      {
        name: 'client_secret',
        optional: false,
        control_type: 'password'
      }
    ],

    authorization: {
      type: "oauth2",

      authorization_url: lambda do
        "https://percolate.com/auth/oauth2"
      end,

      token_url: lambda do
        "https://podio.com/oauth/token"
      end,

      client_id: lambda do |connection|
        connection['client_id']
      end,

      client_secret: lambda do |connection|
        connection['client_secret']
      end,

      apply: lambda do |connection, access_token|
        headers("Authorization": "OAuth2 #{access_token}")
      end,

      refresh_on: [401, 403],

      refresh: lambda do |connection, refresh_token|
        response = post("https://podio.com/oauth/token").
                      payload(
                        grant_type: "refresh_token",
                        client_id: connection["client_id"],
                        client_secret: connection["client_secret"],
                        refresh_token: refresh_token
                      )
        [
          { # This hash is for your tokens
            access_token: response["access_token"],
            refresh_token: response["refresh_token"]
          }
        ]
      end,
    }
  },

  test: lambda do |connection|
    get('/oauth/scope')
  end,

  #More connector code here
}
```

- Check out the [Podio API](https://developers.podio.com/authentication/server_side)

## Step 1 - Defining Connection fields

This component tells Workato what fields to show to a user trying to establish a connection. In the case of Authentication code authentication, you would need the Client ID and Client Secret that the user has generated in Podio.

| Information needed | Description |
| --- | --- |
| Client ID | This is the "username" that this specific custom connector has registered with the API. This might mean signing Workato up as a verified application in the application. |
| Client secret | This is the "password" that this specific custom connector has registered with the API. This might mean signing Workato up as a verified application in the application. **Don't share your client secret with others** |

This is done in the `fields` key, which accepts an array of hashes. Each hash in this array corresponds to a separate input field.

```ruby
    fields: [
      {
        name: 'client_id',
        optional: false
      },
      {
        name: 'client_secret',
        optional: false,
        control_type: 'password'
      }
    ],
```

![Configured Podio connection fields](/assets/podio_conn.BSXTJKje.png)

> **TIP**
> 
> When defining fields, you need to at least provide the `name` key. Additional attributes like `optional`, `hint` and `control_type` allow you to customize other aspects of these fields. For sensitive information like Client Secrets, remember to use the `control_type` as `password`.
> 
> Refer to [Connection fields](/en/developing-connectors/sdk/sdk-reference/connection#fields) for more information on defining input fields in Workato.

Using environment properties to store static client IDs and secrets for your organization

When building a connector for your entire organization, it is often inefficient to have each individual provide client IDs and secrets when making connections. Workato allows you to use environment properties for this very purpose, to securely store these credentials.

You can remove the fields for `client_id` or `client_secret` from the connection code, and use the `account_property` method instead, to reference properties that point to the appropriate values.

**Example for HubSpot**

```ruby
authorization_url: lambda do |connection|
  client_id = account_property('hubspot_webhook_client_id')
  "https://app.hubspot.com/oauth/authorize?client_id=#{client_id}&response_type=code&scope=crm.objects.companies.read crm.objects.contacts.read crm.objects.deals.read"
end,

acquire: lambda do |connection, auth_code, redirect_uri|
  client_id = account_property('hubspot_webhook_client_id')
  client_secret = account_property('hubspot_webhook_client_secret')
  response = post("https://api.hubapi.com/oauth/v1/token").
    payload(client_id: client_id,
      client_secret: client_secret,
      grant_type: 'authorization_code',
      code: auth_code,
      redirect_uri: redirect_uri).
    request_format_www_form_urlencoded
  [
    {
      access_token: response['access_token'],
      refresh_token: response['refresh_token']
    },
    nil,
    nil
  ]
end,
```

## Step 2 - Defining the authorization type

This component instructs Workato what to do with the values received from the input fields to establish a connection. This is handled through your `authorization` key. In this key, you begin by first defining the `type` of authorization. In this case, you should use `oauth2`.

```ruby
      type: "oauth2",
```

## Step 3 - Defining client ID, client secret, authorization url, and token url

With the authorization code grant variant of OAuth 2, you supply 4 key attributes to your connector:

- The authorization url - where we will redirect the user via a browser popup to provide authorization.
- The token url - where this connector will send a request to receive an access token after receiving an auth code from the authorization url
- The client ID - The public ID of the OAuth app assigned to this connection.
- The client secret - The private key of the OAuth app assigned to this connection.

```ruby
    authorization_url: lambda do |connection|
      "https://podio.com/oauth/authorize"
    end,

    token_url: lambda do |connection|
      "https://podio.com/oauth/token"
    end,

    client_id: lambda do |connection|
      connection['client_id']
    end,

    client_secret: lambda do |connection|
      connection['client_secret']
    end,
```

When defining the `authorization_url` lambda function, you do not have to explicitly pass in the client ID, redirect URI, or state. Workato does that for you. Sometimes, you may have to add scope to the URL.

However, if the application requires you to register the redirect URI beforehand, use this callback URL:

```url
https://www.workato.com/oauth/callback
```

This unified callback URL works across all Workato data centers.

When defining the `token_url` lambda function, you do not have to explicitly pass in the client ID, client secret, and grant\_type. Workato does that for you. For the `token_url` request, we follow RFC standards and use a `POST` request with the relevant information in the payload body.

When defining the `client_id` and `client_secret`, you may use inputs from the end user, which you previously collected from the `fields` portion. Workato does not recommend that you code these inputs.

When Workato exchanges the short-lived authorization code for a longer-living access token, we expect the response from the `token_url` endpoint to contain 2 main values - `access_token` and `refresh_token`. Here is a sample response:

```json
{
  "access_token": "my-authentication-token",
  "token_type": "bearer",
  "expires_in": "seconds-until-expiration",
  "refresh_token": "my-refresh-token",
  "error": "optional-error-message",
  "ref":
  {
    "type": "user",
    "id": USER_ID
  }
}
```

The authentication stores the values associated with `access_token` and `refresh_token`.

> **VIRTUAL PRIVATE WORKATO (VPW) CUSTOMERS**
> 
> This feature requires configuration steps that are specific to your Virtual Private Workato (VPW) instance. If you are a VPW customer, refer to your VPW private documentation for the configuration details for your instances.

## Step 4 - Applying the access token to subsequent HTTP requests

In the apply key, we apply the acquired access token as a header input.

We can retrieve the `access_token` by referencing simply passing in `access_token` as a parameter into the apply key. This argument `access_token` is automatically assigned from the output of the `token_url` lambda function.

```ruby
    apply: lambda do |connection, access_token|
      headers("Authorization": "OAuth2 #{access_token}")
    end,
```

To learn more about the available parameters and keys in the connection object, see [SDK Reference - connection](/en/developing-connectors/sdk/sdk-reference/connection).

## Step 5 - Defining token refresh behavior

In most cases, OAuth 2.0 Authentication has both short-lived access tokens and long-lived refresh tokens. Sometimes, refresh tokens don't expire.

> **WARNING**
> 
> Not all APIs issue refresh token credentials. Check with the API about this requirement.

When the access-token expires, you can define the behavior that your connector should take to refresh the access token using the refresh token.

```ruby
    refresh_on: [401, 403],

    refresh: lambda do |connection, refresh_token|
      response = post("https://podio.com/oauth/token").
                    payload(
                      grant_type: "refresh_token",
                      client_id: connection["client_id"],
                      client_secret: connection["client_secret"],
                      refresh_token: refresh_token,
                      redirect_uri: 'https://www.workato.com/oauth/callback'
                    )
      [
        {
          access_token: response["access_token"],
          refresh_token: response["refresh_token"]
        }
      ]
    end,
```

To refresh your access token, you have to use two keys in the `authorization` key - `refresh_on` and `refresh`. `refresh_on` accepts an array that may contain HTTP response codes or regex strings. If an HTTP request in the connector receives any of the HTTP response codes, or if the body of the payload matches a regex string, it will execute the code in the `refresh` key to attempt to retrieve a new access token.

In the `refresh` key, you have access to an argument that represents the `refresh_token` received from the initial token request. The expected output of this lambda function is an array where the first index is a hash denoting the new `access_token` as well as the new `refresh_token` if applicable. These will be used to update the initial values for a long lasting connection.

To learn more about the refresh lambda, see [SDK Reference - authorization](/en/developing-connectors/sdk/sdk-reference/connection/authorization#refresh).

## Step 6 - Setting the API's base URI

This component tells Workato what the base URL of the API is. This key is optional but allows you to provide only relative paths in the rest of your connector when defining HTTP requests. Refer to [base URI configuration](/en/developing-connectors/sdk/sdk-reference/connection#base-uri) for more information on configuring your `base_uri`.

```ruby
    base_uri: lambda do |connection|
      'https://podio.com'
    end
```

> **TIP**
> 
> This lambda function also has access to the `connection` argument. This is especially useful if the base URI of the API might change based on the user's instance. The `connection` argument can be accessed in the following format:
> 
> ```ruby
>     base_uri: lambda do |connection|
>       "https://#{connection['domain'].com/api}"
>     end
> ```

## Step 7 - Testing the connection

Now that we have defined the fields we need to collect from an end user and what to do with the inputs from those fields, we now need a way to test this connection. This is handled in the `test` key.

```ruby
    test: lambda do
      get('/oauth/scope')
    end,
```

In this block, you need to provide an endpoint that allows us to send a sample request using the new credentials we just received. If we receive a 200 OK HTTP response, we show the connection as Successful. In the example above, we are sending a `GET` request to the `/oauth/scope` endpoint and expecting a 200 response if the API key is valid.

## Auth code grant variations

In cases that deviate from the normal standard authentication flows, use our `acquire` block. This block allows you to define the HTTP calls that occurs during the authentication process. For example, some APIs require the authorization token to be obtained by using a `POST` request with basic authentication.

> **TIP**
> 
> Using the `acquire` block instead of the `token_url` block is often recommended for users who need greater control. The `acquire` block allows you to control all aspects of the API request to retrieve access tokens as well as greater flexibility in terms scheduling automatic token refreshes via the `refresh_token_expires_in` key and storing other metadata such as OAuth scopes in the connection hash.

### Using the `acquire` key

In the case below, we used the acquire key to send a `POST` HTTP call with basic authentication since our `token_url` block defaults to header authentication. You can then pull the `access_token` and `refresh_token` from the response to the `POST` call.

```ruby
    authorization: {
      type: "oauth2",

      authorization_url: lambda do |connection|
        params = {
          response_type: "code",
          client_id: connection["client_id"]
        }.to_param

        "https://login.mypurecloud.com/oauth/authorize?" + params
      end,

      acquire: lambda do |connection, auth_code|
        response = post("https://login.mypurecloud.com/oauth/token").
          payload(
            grant_type: "authorization_code",
            code: auth_code,
            redirect_uri: "https://www.workato.com/oauth/callback"
          ).
          user(connection["client_id"]).
          password(connection["client_secret"]).
          request_format_www_form_urlencoded

        # After defining the POST method, we now need to define the
        # output of the acquire key in a fashion that we can recognise
          [
            {
              access_token: response["access_token"],
              refresh_token: response["refresh_token"],
              refresh_token_expires_in: response["expires_in"] # Expiration time of the refresh token from now in seconds
            },
            nil,
            # Optional. Will be merged into connection hash
            { instance_id: nil }
          ]
        end,

        apply: lambda do |connection, access_token|
          headers("Authorization": "Bearer #{connection["access_token"]}")
        end
      }
    },
```

The methods `.user` and `.password` are the equivalent of appending `Authorization: BASIC` and `<user>:<password>` in BASE-64 String encoding in the `POST` request header. Note that the request must be sent with `request_format_www_form_urlencoded`.

Upon receiving a the request, the API returns a JSON response like below:

```json
{
  "access_token": "token",
  "token_type": "bearer",
  "expires_in": 86400,
  "refresh_token": "my-refresh-token",
  "error": "optional-error-message"
}
```

Take note that an array of hashes is the expected output when using the `acquire` key for OAuth 2.0 authentication methods. Each index in the array should have the following values in sequence:

- Tokens - Must be a hash with the exact keys for `access_token`, `refresh_token` and `refresh_token_expires_in`. `refresh_token` and `refresh_token_expires_in` values are optional but recommended
- Owner ID - This is an optional value used for clobber detection (substitute with `nil` if not used)
- Other values - Here you can supply an optional hash that will be merged with the original connection hash.

Which matches the connector code here:

```ruby
  [
    {
      access_token: response["access_token"],
      refresh_token: response["refresh_token"],
      refresh_token_expires_in: response["expires_in"] # in seconds
    },
    nil,
    # Optional. Will be merged into connection hash
    { instance_id: nil }
  ]
```

## Connections SDK reference

To be more familiar with the available keys within the `connection` key and their parameters, check out our [SDK reference](/en/developing-connectors/sdk/sdk-reference/connection).

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/authentication/oauth/auth-code-pkce.md
description: >-
  Build a custom connector that authenticates with the OAuth 2.0 authorization
  code grant using Proof Key for Code Exchange (PKCE).
---

# How-to Guide - OAuth 2.0 Authorization Code Variant with Proof Key for Code Exchange (PKCE)

The OAuth 2.0 Authorization code flow is a way for Workato to impersonate a specific user when authenticating to an API. This is done by getting the user's consent via a browser popup when they first attempt to connect. In this variant with PKCE, there is an additional verification step where a challenge is presented in the authorization URL and the verifier is presented in the final token exchange request.

## Sample Connector - Dropbox

```ruby
{
  title: "Dropbox pkce",

  connection: {
    fields: [
      { name: 'client_id' },
      { name: 'client_secret' }
    ],
    authorization: {
      type: "oauth2",

      client_id: lambda do |connection|
        connection['client_id']
      end,

      client_secret: lambda do |connection|
        connection['client_secret']
      end,

      pkce: lambda do |verifier, challenge|
        {
          verifier: verifier,
          challenge: challenge,
          challenge_method: "S256"
        }
      end,

      authorization_url: lambda do |connection|
        "https://www.dropbox.com/oauth2/authorize?client_id=#{connection['client_id']}&response_type=code"
      end,

      token_url: lambda do |_connection|
        "https://api.dropbox.com/oauth2/token"
      end,

      apply: lambda do |_connection, access_token|
        headers('Authorization': "Bearer #{access_token}")
      end
    },
  },

  test: lambda do |_connection|
    post("https://api.dropboxapi.com/2/check/app", {})
  end,

  #More connector code here
}
```

- Check out the [Dropbox API](https://dropbox.tech/developers/pkce--what-and-why-)

## Step 1 - Defining connection fields

This component tells Workato what fields to show to a user trying to establish a connection. In the case of authentication code grant with PKCE, you would need the Client ID and Client Secret that the user has generated in Dropbox's developer console.

This is done in the `fields` key, which accepts an array of hashes. Each hash in this array corresponds to a separate input field.

```ruby
    fields: [
      {
        name: 'client_id',
        optional: false
      },
      {
        name: 'client_secret',
        optional: false,
        control_type: 'password'
      }
    ],
```

> **TIP**
> 
> When defining fields, you need to at least provide the `name` key. Additional attributes like `optional`, `hint` and `control_type` allow you to customize other aspects of these fields. For sensitive information like Client Secrets, remember to use the `control_type` as `password`.
> 
> Learn more about how to [define input fields](/en/developing-connectors/sdk/sdk-reference/connection#fields) in Workato.

## Step 2 - Defining the authorization type

This component instructs Workato what to do with the values received from the input fields to establish a connection. This is handled through your `authorization` key. In this key, you begin by first defining the `type` of authorization. In this case, you should use `oauth2`, similar to the Authorization Code Grant flow.

```ruby
      type: "oauth2",
```

## Step 3 - Defining the Client ID, Client Secret and PKCE parameters

These components tell the SDK framework what to use for the client ID, client secret and PKCE parameters later on.

```ruby
      client_id: lambda do |connection|
        connection['client_id']
      end,

      client_secret: lambda do |connection|
        connection['client_secret']
      end,

      pkce: lambda do |verifier, challenge|
        {
          verifier: verifier,
          challenge: challenge,
          challenge_method: "S256"
        }
      end,
```

In our example, we simple map the user's inputs for the client ID and secret to the relevant `client_id` and `client_secret` lambdas respectively. This is done with the `connection` argument which is a hash representing the user's inputs in the `fields` defined earlier.

Next, you'll also need to define the `pkce` lambda, which is an important marker that signifies that this is an Authorization Code Grant Flow with PKCE. Within this lambda, you will receive 2 arguments which correspond to the `verifier` and `challenge`. You may simple use both of these arguments as-is and pass them as the output of the `pkce` lambda as seen in the example.

## Step 4 - Defining authorization url, and token url

With the PKCE variant of OAuth 2, you supply 2 the authorization url and the token url - similar to the normal auth code grant flow.

- The authorization url - where we will redirect the user via a browser popup to provide authorization.
- The token url - where this connector will send a request to receive an access token after receiving an auth code from the authorization url

```ruby
  authorization_url: lambda do |connection|
    "https://www.dropbox.com/oauth2/authorize"
  end,

  token_url: lambda do |connection|
    "https://api.dropbox.com/oauth2/token"
  end,
```

When defining the `authorization_url` lambda function, Workato automatically passes the following parameters:

- client ID
- redirect URI
- code challenge
- state

In some cases, you may have to add scope to the URL as needed. If the application requires that you register the redirect URI beforehand, use the following URL: `https://www.workato.com/oauth/callback`.

When defining the `token_url` lambda function, Workato automatically passes the following parameters:

- client ID
- client secret
- code verifier
- grant\_type

For the `token_url` request, we follow RFC standards and use a `POST` request with the relevant information in the payload body. When Workato exchanges the short-lived authorization code for a longer-living access token, we expect the response from the `token_url` endpoint to contain 2 main values - `access_token` and `refresh_token`. Here is a sample response:

```json
{
  "access_token": "my-authentication-token",
  "token_type": "bearer",
  "expires_in": "seconds-until-expiration",
  "refresh_token": "my-refresh-token",
  "error": "optional-error-message",
  "ref":
  {
    "type": "user",
    "id": USER_ID
  }
}
```

The authentication stores the values associated with `access_token` and `refresh_token`.

## Step 5 - Applying the access token to subsequent HTTP requests

In the apply key, we apply the acquired access token as a header input.

We can retrieve the `access_token` by referencing simply passing in `access_token` as a parameter into the apply key. This argument `access_token` is automatically assigned from the output of the `token_url` lambda function.

```ruby
    apply: lambda do |connection, access_token|
      headers("Authorization": "OAuth2 #{access_token}")
    end,
```

To learn more about the available parameters and keys in the connection object, see [SDK Reference - connection](/en/developing-connectors/sdk/sdk-reference/connection).

## Step 6 - Defining token refresh behavior

In most cases, OAuth 2.0 Authentication has both short-lived access tokens and long-lived refresh tokens. Sometimes, refresh tokens don't expire.

> **WARNING**
> 
> Note that not all APIs issue refresh token credentials. Check with the API about this requirement.

When the access-token expires, you can define the behavior that your connector should take to refresh the access token using the refresh token.

```ruby
    refresh_on: [401, 403],

    refresh: lambda do |connection, refresh_token|
      response = post("https://api.dropbox.com/oauth2/token").
                    payload(
                      grant_type: "refresh_token",
                      client_id: connection["client_id"],
                      client_secret: connection["client_secret"],
                      refresh_token: refresh_token,
                      redirect_uri: 'https://www.workato.com/oauth/callback'
                    )
      [
        {
          access_token: response["access_token"],
          refresh_token: response["refresh_token"]
        }
      ]
    end,
```

To refresh your access token, you have to use two keys in the `authorization` key - `refresh_on` and `refresh`. `refresh_on` accepts an array that may contain HTTP response codes or regex strings. If an HTTP request in the connector receives any of the HTTP response codes, or if the body of the payload matches a regex string, it will execute the code in the `refresh` key to attempt to retrieve a new access token.

In the `refresh` key, you have access to an argument that represents the `refresh_token` received from the initial token request. The expected output of this lambda function is an array where the first index is a hash denoting the new `access_token` as well as the new `refresh_token` if applicable. These will be used to update the initial values for a long lasting connection.

To learn more about the refresh lambda, see [SDK Reference - authorization](/en/developing-connectors/sdk/sdk-reference/connection/authorization#refresh).

## Step 7 - Setting the API's base URI

This component tells Workato what the base URL of the API is. This key is optional but allows you to provide only relative paths in the rest of your connector when defining HTTP requests. Learn how to [configure your base URI](/en/developing-connectors/sdk/sdk-reference/connection#base-uri).

```ruby
    base_uri: lambda do |connection|
      'https://api.dropboxapi.com'
    end
```

> **TIP**
> 
> This lambda function also has access to the `connection` argument. This is especially useful if the base URI of the API might change based on the user's instance. The `connection` argument can be accessed in the following format:
> 
> ```ruby
>     base_uri: lambda do |connection|
>       "https://#{connection['domain'].com/api}"
>     end
> ```

## Step 8 - Testing the connection

Now that we have defined the fields we need to collect from an end user and what to do with the inputs from those fields, we now need a way to test this connection. This is handled in the `test` key.

```ruby
    test: lambda do
      post("https://api.dropboxapi.com/2/check/app", {})
    end,
```

In this block, you need to provide an endpoint that allows us to send a sample request using the new credentials we just received. If we receive a 200 OK HTTP response, we show the connection as Successful. In the example above, we are sending a `POST` request to the `/2/check/app` endpoint and expecting a 200 response if the access token we just received is valid.

## Auth code grant PKCE variation

In some cases, you may need to use the `acquire` lambda to complete the token request. Here we have an example with the same Dropbox connection, except using the `acquire` lambda.

```ruby
  connection: {
    fields: [
      { name: 'client_id' },
      { name: 'client_secret' }
    ],
    authorization: {
      type: "oauth2",

      client_id: lambda do |connection|
        connection['client_id']
      end,

      client_secret: lambda do |connection|
        connection['client_secret']
      end,

      pkce: lambda do |verifier, challenge|
        {
          verifier: verifier,
          challenge: challenge,
          challenge_method: "S256"
        }
      end,

      authorization_url: lambda do |connection|
        "https://www.dropbox.com/oauth2/authorize?client_id=#{connection['client_id']}&response_type=code"
      end,

      acquire: lambda do |connection, auth_code, redirect_uri, verifier|
        response = post("https://api.dropbox.com/oauth2/token",
          grant_type: "authorization_code",
          code: auth_code,
          redirect_uri: redirect_uri,
          client_secret: connection["client_secret"],
          code_verifier: verifier,
          client_id: connection["client_id"]
        ).request_format_www_form_urlencoded

        [
          {
            access_token: response["access_token"],
            refresh_token: response["refresh_token"],
            refresh_token_expires_in: response["expires_in"] # Expiration time of the refresh token from now in seconds
          },
          nil,
          { instance_id: nil }
        ]
      end,

      apply: lambda do |_connection, access_token|
        headers('Authorization': "Bearer #{access_token}")
      end
    },
  },
```

Take note that you receive an additional argument, `verifier` in the `acquire` lambda which corresponds to the same verifier you passed as the output of the `pkce` lambda.

## Connections SDK reference

To be more familiar with the available keys within the `connection` key and their parameters, check out our [SDK reference](/en/developing-connectors/sdk/sdk-reference/connection).

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/authentication/oauth/client-credentials.md
description: >-
  Build a custom connector that authenticates with the OAuth 2.0 client
  credentials flow for server-to-server access to a target API.
---

# How-to Guide - OAuth 2.0 Client Credentials Authentication

The OAuth 2.0 Client Credentials flow is traditionally a way for server to server authentication. This allows you to build a connector that can authenticate as the Workato server which communicates to your target API server.

## Sample Connector - Percolate

```ruby
{
  title: 'My Percolate connector',

  connection: {
    fields: [
      {
        name: 'client_id',
        optional: false,
      },
      {
        name: 'client_secret',
        control_type: 'password',
        optional: false,
      }
    ],

    authorization: {
      type: 'custom_auth', #Set to custom_auth

      acquire: lambda do |connection|
        hash = ("#{connection['client_id']}:#{connection['client_secret']}").base64.gsub("\n", '')
          # Token URL
        response = post('https://percolate.com/auth/v5/token/').
                      payload(grant_type: 'client_credentials').
                      headers(Authorization: "Basic " + hash).
                      request_format_www_form_urlencoded

        {
          access_token: response["access_token"],
          refresh_token: response["refresh_token"]
        }
      end,

      detect_on: [401, 403],

      refresh_on: [401, 403],

      apply: lambda do |connection|
        headers("Authorization": "Bearer #{connection['access_token']}")
      end
    },

    base_uri: lambda do |connection|
      'https://percolate.com'
    end

  },

  test: lambda do |connection|
    get('/api/v5/me')
  end,

  #More connector code here
}
```

- Refer to the [full Percolate connector code](https://app.workato.com/custom_adapters/12095/details?token=4d19f8fa) for a complete example.
- Check out the [Percolate API](https://percolate.dev/reference#createaccesstoken)

## Step 1 - Defining Connection fields

This component tells Workato what fields to show to a user trying to establish a connection. In the case of Client Credentials Authentication, you would need the Client ID and Client Secret that the user has generated in Percolate.

| Information needed | Description |
| --- | --- |
| Client ID | This is the public ID of the OAuth app that should be tied to Workato. This might mean signing Workato up as a verified application in the application |
| Client secret | This is the matching private key that the API will verify along with the Client ID. This might mean signing Workato up as a verified application in the application. **Don't share your client secret with others** |

This is done in the `fields` key, which accepts an array of hashes. Each hash in this array corresponds to a separate input field.

```ruby
    fields: [
      {
        name: 'client_id',
        optional: false,
      },
      {
        name: 'client_secret',
        control_type: 'password',
        optional: false,
      }
    ],
```

![Configured Percolate connection fields](/assets/percolate_conn.CFC2Se9m.png)

> **TIP**
> 
> When defining fields, you need to at least provide the `name` key. Additional attributes like `optional`, `hint` and `control_type` allow you to customize other aspects of these fields. For sensitive information like Client Secrets, remember to use the `control_type` as `password`.
> 
> Refer to [Connection fields](/en/developing-connectors/sdk/sdk-reference/connection#fields) for more information on defining input fields in Workato.

## Step 2 - Defining the authorization type

This component tells Workato what type of authentication type this connection should use. This is handled through your `type` key in the `authorization` object. For Client Credentials authentication, you should use `custom_auth`.

```ruby
      type: 'custom_auth'
```

## Step 3 - Acquiring the access token

The next step is to define what this connector should do to retrieve an access token. This is done in the `acquire` lambda function.

```ruby
      acquire: lambda do |connection|
        hash = ("client:#{connection['client_id']}:#{connection['client_secret']}").base64.gsub("\n", '')
        response = post('https://percolate.com/auth/v5/token/'). # Token URL
                      payload(grant_type: 'client_credentials').
                      headers(Authorization: "Basic " + hash).
                      request_format_www_form_urlencoded

        {
          access_token: response["access_token"]
        }
      end,
```

In the `acquire` key, we pass in the `client_id` and `client_secret` which were input fields defined in the `fields` key. These values are available via the argument to the lambda function - `connection`. We pass them as headers and in BASE-64 String encoding. Note that the body of the request must be sent with `request_format_www_form_urlencoded` as per Percolates requirements. This request is then sent to Percolate's Token URL.

Upon receiving a the request, the API returns a JSON response.

```json
{
  "access_token": "my-authentication-token",
  "token_type": "bearer",
  "expires_in": "seconds-until-expiration",
  "error": "optional-error-message"
}
```

The output of the `acquire` lambda function is expected to be an object which is merged into the original connection object. For example:

```ruby
# Original Connection hash
{
  client_id: "abcd1234",
  client_secret: "secretClientSecret"
}

# After acquire key is executed
{
  client_id: "abcd1234",
  client_secret: "secretClientSecret",
  access_token: "my-authentication-token"
}
```

## Step 4 - Applying the access token to subsequent HTTP requests

Next, you need to tell Workato how to make use of the access token it has retrieved from Percolate. This is done in the `apply` key where you can reference the access token now stored in the `connection` argument. Any instructions you introduce in the `apply` key are subsequently applied to all HTTP requests this connector sends after connection is established.

```ruby
    apply: lambda do |connection|
      headers("Authorization": "Bearer #{connection['access_token']}")
    end
```

In this example, we have defined the access token (`connection['access_token']`) to be added to the headers of any request. For every HTTP request sent, the headers will contain `Authorization: Bearer XXX` where `XXX` is the access token stored in the `connection` hash.

## Step 5 - Defining token refresh behavior

There may be situations in which the API expires the access token after a prescribed amount of time. In these cases, you would need to define `refresh_on` signals to let Workato know when to retrieve a new access\_token from the OAuth server. `refresh_on` accepts an array which may contain HTTP response codes or regex strings.

If an HTTP request in the connector receives any of the HTTP response codes, it will attempt to retrieve a new access token. Likewise, if the contents of the body payload matches any of the defined regex strings, it will retrieve a new access token.

In the example using `type: custom_auth`, it will execute the code in the `acquire` key.

```ruby
    refresh_on: [401, 403],
```

When the `acquire` lambda is run again, this is the expected response from Percolate.

```json
{
  "access_token": "my-NEW-authentication-token",
  "token_type": "bearer",
  "expires_in": "seconds-until-expiration",
  "error": "optional-error-message"
}
```

The expected output of the `acquire` lambda function is a hash which is merged into the original connection hash. For example:

```ruby
# Original Connection hash
{
  client_id: "abcd1234",
  client_secret: "secretClientSecret",
  access_token: "my-authentication-token"
}

# After acquire lambda is executed
{
  client_id: "abcd1234",
  client_secret: "secretClientSecret",
  access_token: "my-NEW-authentication-token"
}
```

## Step 6 - Setting the API's base URI

This component tells Workato what the base URL of the API is. This key is optional but allows you to provide only relative paths in the rest of your connector when defining HTTP requests. Refer to [base URI configuration](/en/developing-connectors/sdk/sdk-reference/connection#base-uri) for more information on configuring your `base_uri`.

```ruby
    base_uri: lambda do |connection|
      'https://percolate.com'
    end
```

> **TIP**
> 
> This lambda function also has access to the `connection` argument. This is especially useful if the base URI of the API might change based on the user's instance. The `connection` argument can be accessed in the following format:
> 
> ```ruby
>     base_uri: lambda do |connection|
>       "https://#{connection['domain'].com/api}"
>     end
> ```

## Step 7 - Testing the connection

Now that we have defined the fields we need to collect from an end user and what to do with the inputs from those fields, we now need a way to test this connection. This is handled in the `test` key.

```ruby
    test: lambda do
      get('/api/v5/me')
    end,
```

In this block, you need to provide an endpoint that allows us to send a sample request using the new credentials we just received. If we receive a 200 OK HTTP response, we show the connection as Successful. In the example above, we are sending a `GET` request to the `/api/v5/me` endpoint and expecting a 200 response if the API key is valid.

## Connections SDK reference

To be more familiar with the available keys within the `connection` key and their parameters, check out our [SDK reference](/en/developing-connectors/sdk/sdk-reference/connection).

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/authentication/oauth/ropc.md
description: >-
  Build a custom connector that authenticates with the OAuth 2.0 resource owner
  password credentials flow to exchange a username and password for tokens.
---

# How-to Guide - OAuth 2.0 Resource owner password credentials authentication

The OAuth 2.0 resource owner password credentials flow is traditionally a server-to-server authentication method. This allows you to build a connector that can authenticate as the Workato server and communicate to your target API server. This flow allows the exchange of a user's username and password for an access token and, optionally, a refresh token.

## Sample Connector - Microsoft Entra ID

```ruby
{
  title: 'My Azure connector',

  connection: {
    fields: [
      {
        name: 'tenant_id',
        optional: false,
      }
      {
        name: 'client_id',
        optional: false,
      },
      {
        name: 'client_secret',
        control_type: 'password',
        optional: false,
      },
      {
        name: 'username',
        optional: false,
      },
      {
        name: 'password',
        control_type: 'password',
        optional: false,
      }
    ],

    authorization: {
      type: 'custom_auth', #Set to custom_auth

      acquire: lambda do |connection|
        token_url = "https://login.microsoftonline.com/#{connection['tenant_id']}/oauth2/v2.0/token"
        response = post(token_url).
                    payload(client_id: "#{connection['client_id']}",
                      client_secret: "#{connection['client_secret']}",
                      username: "#{connection['username']}",
                      password: "#{connection['password']}",
                      grant_type: "password").
                    request_format_www_form_urlencoded


        {
          access_token: response["access_token"],
        }
      end,

      refresh_on: 401,

      apply: lambda do |connection|
        headers("Authorization": "Bearer #{connection['access_token']}")
      end
    }

  },

  test: lambda do |connection|
    get( #Some accessible endpoint )
  end,

  #More connector code here
}
```

## Step 1 - Defining Connection fields

This component tells Workato what fields to show to a user trying to establish a connection. In the case of resource owner password credentials, you would need the Client ID and Client Secret that the user has generated in Azure. You will also need to provide the Username and Password of the user account that you will be using to authorize the connection.

| Information needed | Description |
| --- | --- |
| Client ID | This is the public ID of the OAuth app that should be tied to Workato. This might mean signing Workato up as a verified application in the application |
| Client secret | This is the matching private key that the API will verify along with the Client ID. This might mean signing Workato up as a verified application in the application. **Don't share your client secret with others** |
| Username | This is the username of the user account that is giving permission to authenticate the client. |
| Password | This is the password of the user account that is giving permission to authenticate the client. |

This is done in the `fields` key, which accepts an array of hashes. Each hash in this array corresponds to a separate input field.

```ruby
    fields: [
      {
        name: 'tenant_id',
        optional: false,
      }
      {
        name: 'client_id',
        optional: false,
      },
      {
        name: 'client_secret',
        control_type: 'password',
        optional: false,
      },
      {
        name: 'username',
        optional: false,
      },
      {
        name: 'password',
        control_type: 'password',
        optional: false,
      }
    ],
```

![Configured Azure connection fields](/assets/azure_conn.Bw0acIFU.png)

> **TIP**
> 
> When defining fields, you need to at least provide the `name` key. Additional attributes like `optional`, `hint` and `control_type` allow you to customize other aspects of these fields. For sensitive information like Client Secrets, remember to use the `control_type` as `password`.
> 
> Refer to [Connection fields](/en/developing-connectors/sdk/sdk-reference/connection#fields) for more information on defining input fields in Workato.

## Step 2 - Defining the authorization type

This component tells Workato what type of authentication type this connection should use. This is handled through your `type` key in the `authorization` object. For Client Credentials authentication, you should use `custom_auth`.

```ruby
      type: 'custom_auth'
```

## Step 3 - Acquiring the access token

In the `acquire` key, we pass in the `client_id`, `client_secret`, `username`, and `password` provided by users of connector as payload. Note that the payload of the request must be sent with `request_format_www_form_urlencoded`. We also identify `password` as the grant type and we pass this in as payload in the `POST` request. This request is then sent to Microsoft's Token URL.

```ruby
    acquire: lambda do |connection|
      response = post("https://login.microsoftonline.com/#{connection['tenant_id']}/oauth2/v2.0/token"). # Token URL
                    payload(client_id: "#{connection['client_id']}",
                      client_secret: "#{connection['client_secret']}",
                      username: "#{connection['username']}",
                      password: "#{connection['password']}",
                      grant_type: "password").
                    request_format_www_form_urlencoded

      {
        access_token: response["access_token"],
      }
    end,
```

Upon receiving a the request, the API returns a JSON response.

```json
{
  "access_token": "my-authentication-token",
  "token_type": "bearer",
  "expires_in": "seconds-until-expiration",
  "error": "optional-error-message"
}
```

The expected output of the `acquire` lambda function is a hash which is merged into the original connection hash. For example:

```ruby
# Original Connection hash
{
  client_id: "abcd1234",
  client_secret: "secretClientSecret"
}

# After acquire block is executed
{
  client_id: "abcd1234",
  client_secret: "secretClientSecret",
  access_token: "my-authentication-token"
}
```

## Step 4 - Applying the access token to subsequent HTTP requests

Next, you need to tell Workato how to make use of the access token it has retrieved from Microsoft. This is done in the `apply` key where you can reference the access token now stored in the `connection` argument. Any instructions you introduce in the `apply` block are subsequently applied to all HTTP requests this connector sends after connection is established.

```ruby
    apply: lambda do |connection|
      headers("Authorization": "Bearer #{connection['access_token']}")
    end
```

In this example, we have defined the access token (`connection['access_token']`) to be added to the headers of any request. For every HTTP request sent, the headers will contain `Authorization: Bearer XXX` where `XXX` is the access token stored in the `connection` hash.

## Step 5 - Setting the API's base URI

This component tells Workato what the base URL of the API is. This key is optional but allows you to provide only relative paths in the rest of your connector when defining HTTP requests. Refer to [base URI configuration](/en/developing-connectors/sdk/sdk-reference/connection#base-uri) for more information on configuring your `base_uri`.

> **TIP**
> 
> This lambda function also has access to the `connection` argument. This is especially useful if the base URI of the API might change based on the user's instance. The `connection` argument can be accessed in the following format:
> 
> ```ruby
>     base_uri: lambda do |connection|
>       #some code here
>     end
> ```

## Step 6 - Testing the connection

Now that we have defined the fields we need to collect from an end user and what to do with the inputs from those fields, we now need a way to test this connection. This is handled in the `test` key.

```ruby
    test: lambda do
      get(# Some accessible code)
    end,
```

In this key, you need to provide an endpoint that allows us to send a sample request using the new credentials we just received. If we receive a 200 OK HTTP response, we show the connection as Successful.

## Connections SDK reference

To be more familiar with the available keys within the `connection` key and their parameters, check out our [SDK reference](/en/developing-connectors/sdk/sdk-reference/connection).

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/authentication/aws_auth.md
description: >-
  Set up AWS authentication for a Workato SDK connector using access keys or IAM
  role authentication via the Security Token Service.
---

# How-to Guides - AWS Service Authentication

AWS services can be authenticated in two ways. Workato supports AWS libraries that simplify the authentication process by helping you to generate the AWS V4 Signature so you can focus on building actions and triggers.

This guide shows you how to implement dual authentication for both:

- [Access key authentication](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html)
- [IAM role authentication through AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)

> **RECOMMENDED IAM ROLE FOR AUTHENTICATION**
> 
> AWS and Workato both recommend using AWS IAM role authentication. We recommend that you make this the default authentication method for the users of your connector.

## Create IAM role and ARN retrieval

Refer to the [IAM role-based authentication for AWS](/en/security/data-protection/secrets-management/iam-role-based-authentication-for-aws) page for instructions on how to create an IAM role for Workato and retrieve your Amazon resource name (ARN).

## Sample connector - Generic connector

```ruby
{
  title: "Sample AWS S3 Connector",

  connection: {
    fields: [
      {
        name: "aws_auth_type",
        label: "AWS Authorization type",
        control_type: "select",
        optional: false,
        pick_list: [
          ["IAM role", "aws_role_based"],
          ["Access key", "aws_key_secret"]
        ],
        default: "aws_role_based",
        hint: 'Learn more about Amazon S3 authorization support <a href="http://docs.workato.com/connectors/s3.html#connection-setup" target="_blank">here</a>.'
      },
      {
        name: "aws_assume_role",
        label: "IAM role ARN",
        optional: false,
        ngIf: 'input.aws_auth_type == "aws_role_based"',
        help: {
          title: "Using IAM Role authorization",
          text: <<~HELP
            Create an IAM role in your AWS account using the following data:
            <br/>&nbsp;- Use Workato AWS Account ID <b>{{ authUser.aws_iam_external_id }}</b>
            to generate the <b>Principal</b> for the role.
            <br/>&nbsp;- Use <b>{{ authUser.aws_workato_account_id }}</b> as the <b>External ID</b> for the role.
            <br/>&nbsp;- Set this field's value to the newly created role's ARN.
            <br/><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html"
            target="_blank">Learn more</a>.
          HELP
        }
      },
      {
        name: "aws_api_key",
        label: "Access key ID",
        control_type: "password",
        optional: false,
        hint: "Go to <b>AWS account name</b> > <b>Security Credentials</b> > <b>Users</b>. Get API key from existing user or create new user.",
        ngIf: 'input.aws_auth_type == "aws_key_secret"'
      },
      {
        name: "aws_secret_key",
        label: "Secret access key",
        control_type: "password",
        optional: false,
        hint: "Go to <b>AWS account name</b> > <b>Security Credentials</b> > <b>Users</b>. Get secret key from existing user or create new user.",
        ngIf: 'input.aws_auth_type == "aws_key_secret"'
      },
      {
        name: "aws_region",
        optional: false,
        hint: "AWS service region. If your account URL is <b>https://eu-west-1.console.s3.amazon.com</b>, use <b>eu-west-1</b> as the region."
      }
    ],

    authorization: {
      type: "custom_auth"
    }
  },

  test: lambda do |connection|
    call(:list_buckets, connection)
  end,

   methods: {
    list_buckets: lambda do |connection|
      signature = aws.generate_signature(
        # The connection object defined earlier.
        connection: connection,
        # The internal name of the AWS service you are targeting
        service: "s3",
        # The AWS service region you are targeting.
        # For services with a globally unique endpoint such as IAM, use us-east-1.
        region: connection["aws_region"],
        # The host of the API url.
        # Optional and defaults to "#{service}.#{region}.amazonaws.com".
        # In some cases like AWS API Gateway and AWS IAM, your host may not follow this standard and require you to override the host.
        host: "s3.dualstack.#{connection['aws_region']}.amazonaws.com",
        # The relative path of the endpoint. Optional and defaults to "/"
        path: "/",
        # The verb used for the request. Optional and defaults to "GET"
        method: "GET",
        # The query parameters for the request. Optional and defaults to {}
        params: { "list-type" => 2, "max-keys" => 1000 },
        # The headers for the request. Optional and defaults to {}
        headers: {},
        # The payload for the request. Optional and defaults to ""
        payload: ""
      )
      url = signature[:url]
      headers = signature[:headers]

      response = get(url).headers(headers).response_format_xml

      files = response.dig("ListBucketResult", 0, "Contents")
      files = Array.wrap(files).map do |content|
        content.each_with_object({}) do |(k, v), obj|
          obj[k] = Array.wrap(v).dig(0, "content!")
        end
      end

      { "files" => files }
    end
  }
}
```

## Step 1 - Defining Connection fields

In the `connection` key, we define the input fields in the `fields` key in an array of hashes. Each hash in the array represents a single input field. Inside, we will be able to declare the name of the input field, hints that are displayed to the end user among other parameters. In this example, we're presenting two ways for users to authenticate which is decided by their input for the field `aws_auth_type`.

Based on this selection, we selectively show/hide the next fields for `aws_assume_role` or `aws_api_key` and `aws_secret_key`. This is done with the attribute `ngIf`.

> **TIP**
> 
> Most AWS services have the same authentication, which allows you to use the same connection fields in the preceding example.
> 
> If you do choose to add more fields, you need to at least provide the `name` key. Additional attributes like `optional`, `hint` and `control_type` allow you to customize other aspects of these fields. For sensitive information like Client Secrets, remember to use the `control_type` as `password`.
> 
> Learn how to define [input fields in Workato](/en/developing-connectors/sdk/sdk-reference/connection#fields).

## Step 2 - Generating the AWS signature

Compared to other ways to authenticate, AWS requires a unique signature for each request as the current time is a component of the signature. As such, your connector should not use the `apply` lambda as there are no credentials to apply on a general basis.

Instead, you should use the `aws.generate_signature` method to get the valid URL and signature before making an API call. In our example, you can see that we have created a method `list_buckets` that makes a GET request to S3.

```ruby
    list_buckets: lambda do |connection|
      signature = aws.generate_signature(
        # The connection object defined earlier.
        connection: connection,
        # The internal name of the AWS service you are targeting
        service: "s3",
        # The AWS service region you are targeting.
        # For services with a globally unique endpoint such as IAM, use us-east-1.
        region: connection["aws_region"],
        # The host of the API url.
        # Optional and defaults to "#{service}.#{region}.amazonaws.com".
        # In some cases like AWS API Gateway and AWS IAM, your host may not follow this standard and require you to override the host.
        host: "s3.dualstack.#{connection['aws_region']}.amazonaws.com",
        # The relative path of the endpoint. Optional and defaults to "/"
        path: "/",
        # The verb used for the request. Optional and defaults to "GET"
        method: "GET",
        # The query parameters for the request. Optional and defaults to {}
        params: { "list-type" => 2, "max-keys" => 1000 },
        # The headers for the request. Optional and defaults to {}
        headers: {},
        # The payload for the request. Optional and defaults to ""
        payload: ""
      )
      url = signature[:url]
      headers = signature[:headers]

      response = get(url).headers(headers).response_format_xml

      files = response.dig("ListBucketResult", 0, "Contents")
      files = Array.wrap(files).map do |content|
        content.each_with_object({}) do |(k, v), obj|
          obj[k] = Array.wrap(v).dig(0, "content!")
        end
      end

      { "files" => files }
    end
```

## Step 3 - Testing the connection

With the method defined earlier, you'd be able to call this method in the test to verify the user's credentials.

```ruby
  test: lambda do |connection|
    call(:list_buckets, connection)
  end,
```

## Troubleshooting tips

Testing your connection may not verify your AWS signature correctly. Instead, wrap a simple API request in a method, like in the preceding example, and stub the connection during initial development to test an action:

```ruby
{
  title: "Sample AWS S3 Connector",

  connection: {
    fields: [
      #  Same fields as earlier
    ],

    authorization: {
      type: "custom_auth"
    }
  },

  test: lambda do |connection|
    true
  end,

  actions: {
    sample_action: {
      execute: lambda do |connection|
        call(:list_buckets, connection)
      end
    }
  },

  methods: {
    list_buckets: lambda do |connection|
      # Method from earlier
    end
  }
}
```

By testing the "sample\_action" action, you'll have better insight for debugging into the errors raised by the Workato SDK framework or the AWS API you are connecting to.

## Connections SDK reference

Learn about the available keys within the `connection` key in the [SDK reference](/en/developing-connectors/sdk/sdk-reference/connection).

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/authentication/on-prem.md
description: >-
  Configure OPA authentication in a custom connector to route HTTP requests
  through an on-prem agent instead of Workato IP addresses.
---

# How-to guide - OPA authentication

HTTP requests made in a custom adapter are sent from Workato [IP addresses](/en/security/ip-allowlists#traffic-from-workato) by default. You can configure the adapter to instead route all requests through an [on-prem agent](/en/on-prem).

Complete the following steps to enable OPA authentication in a custom connector:

1. Sign in to Workato.
   
2. Go to **Tools > Connector SDK**.
   
3. Select the connector you plan to modify, or click **\+ New connector** to [create a new connector](/en/developing-connectors/sdk/guides/walkthrough#create-a-custom-connector).
   
4. Add `secure_tunnel` set to `true` as a top level property in your custom adapter code.
   
   > **USE OPA FOR TLS CERTIFICATES**
   > 
   > Configure TLS client certificates in the OPA connection profile instead of your SDK connector code. OPA terminates TLS to your target service, and the certificate must be configured in the HTTP profile. Refer to [On-prem agent – Connection profiles](/en/on-prem/agents/connection/profile#http-profile) for instructions to configure TLS client certificates in OPA. The connection returns SSL errors if you configure the certificate in the SDK connector.
   
   For example:
   
   ```ruby
   {
     title: 'On-prem example connector',
     secure_tunnel: true,
   
     connection: {
       fields: [{ name: 'profile', hint: 'On-prem example connector profile' }],
       authorization: { type: 'none'},
       apply: ->() {
         headers('X-Workato-Connector': 'enforce')
       }
     },
   
     test: ->(connection) {
       post("http://localhost/ext/#{connection['profile']}/computeDigest", { payload: 'test' })
     }
   }
   ```
   
     
   
   > **ADD OPA TO AN EXISTING CONNECTOR**
   > 
   > Use the `||` operator to specify the existing authentication method as the default when you add new authentication methods to an existing connector.
   > 
   > In the following example, the value left of the `||` operator, `auth_type`, is evaluated first. If the value is `nil` or `false`, the right value, `api_key`, is evaluated.
   > 
   > ```ruby
   > selected: lambda do |connection|
   >   connection["auth_type"] || 'api_key'
   > end,
   > ```
   
5. Click **Save > Release latest version**.
   
6. Summarize the changes you made to the connector in the **Confirm release** modal.
   
   ![Change summary and confirmation window](/assets/confirm-version-release-window.Co6Sj0jz.png)_Summarize your changes to the connector_
   
7. Click **Release** to release the new version of the connector in your workspace and allow it to be used in recipes.
   

The **New connection** page for your connector displays the **Connection type** drop-down menu after you set `secure_tunnel` to `true`. You can use this menu to select the [on-prem group](/en/on-prem/groups#on-prem-group) you plan to use for your connection.

**Connector without OPA**

![Connection without option to use OPA](/assets/OPA-example-without-secure-tunnel.DwqWcAfP.png)_**New connection** page without `secure_tunnel` enabled_

**Connector with OPA**

![Connection with option to use OPA](/assets/OPA-example-with-secure-tunnel.-eQlwgum.png)_**New connection** page with `secure_tunnel` enabled_

## Next steps

Refer to the [SDK reference](/en/developing-connectors/sdk/sdk-reference/connection) guide for a list of available `connection` keys and parameters or refer to the following guides set up an on-prem agent:

- [Create an on-prem group](/en/on-prem/groups/create-group)
- [Add an agent to a group](/en/on-prem/groups/add-agent)
- [Run an agent](/en/on-prem/agents/run)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/authentication/multi_auth.md
description: >-
  Build multiple authentication flows in a single Workato SDK connector, letting
  users choose between OAuth 2.0, API key, and more.
---

# How-to Guide - Building multiple authentication flows

You may have to build multiple authentication (multi-auth) methods depending on the various use cases that you plan for your connector to support. For example, you can choose to support the OAuth2 Authorization Code Grant method that requires impersonation of a particular user during API authentication. You can also use API keys or client credentials for stable machine-to-machine authentication if you plan for your connector to support data orchestration use cases. However, it's important to note that Workato doesn't currently support runtime user connections for multi-auth connections.

To achieve multiple authentication flows, Workato's Connector SDK enables you to define segregated and isolated authentication flows within your connector.

> **AUTHENTICATION METHODS**
> 
> This guide assumes you have basic knowledge of the other forms of authentication supported in Workato. Ensure you understand other basic forms of authentication in Workato such as [OAuth2](/en/developing-connectors/sdk/guides/authentication/oauth/auth-code) and [API keys](/en/developing-connectors/sdk/guides/authentication/api-key) as we reference them in this guide.

## Sample Connector - Stripe

To learn more about this connector, see [Stripe API Authentication](https://stripe.com/docs/api/authentication) documentation.

```ruby
{
  title: 'Stripe',

  connection: {
    fields: [
      {
        name: "auth_type",
        control_type: "select",
        pick_list: [["OAuth2", "stripe_oauth2"], ["API Key", "stripe_api_key"]],
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
            { name: 'client_id' },
            { name: 'client_secret' },
          ],

          authorization_url: lambda do |connection|
            "https://connect.stripe.com/oauth/authorize?scope=read_write"
          end,

          token_url: lambda do
            "https://connect.stripe.com/oauth/token"
          end,

          apply: lambda do |_, access_token|
            headers("Authorization": "Bearer #{access_token}")
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
            headers("Authorization": "Bearer #{connection['api_key']}")
          end
        }
      },
    },

    base_uri: lambda do
       "https://api.stripe.com/"
    end
  },

  test: lambda do |connection|
    get('/v1/customers', limit: 1)
  end,

  #More connector code here
}
```

## Build a connector with multiple authentication flows

Complete the following steps to build a connector with multiple authentication flows:

1. Define common connection fields
   
   When planning for multiple authentication flows for the connector, start by deciding which fields are common across all authentication flows. This could be the API base url, or the target connector environment. Minimally, you must dedicate a field to selecting the authentication type that supports each connection scenario.
   
   The example we use in this discussion, Stripe, has only the authentication type as a common connection field.
   
   <dl><dt>Authentication Type</dt><dd>The authentication type from a defined picklist.<br>Has the following important attributes<dl><dt>Schema attribute</dt><dd><code>extends_schema: true</code> tells Workato to evaluate the connection schema again when the use changes the value of this field</dd><dt>Picklist values</dt><dd><code>stripe_oauth2</code> and <code>stripe_api_key</code>are important in the subsequent connector definition.</dd></dl></dd></dl>
   
   This is done in the `fields` key, which accepts an array of hashes. Each hash in this array corresponds to a separate input field.
   
   ```ruby
       fields: [
         {
           name: "auth_type",
           label: "Authentication Type",
           control_type: "select",
           pick_list: [["OAuth2", "stripe_oauth2"], ["API Key", "stripe_api_key"]],
           extends_schema: true
         }
       ]
   ```
   
2. Define the pathway to the selected authentication flow
   
   This component informs Workato what to do with the values it receives from the input fields, and what authentication flow to use. It is implemented through the `authorization` key. Start by defining the `type` of authorization as `"multi"`.
   
   ```ruby
       authorization: {
         type: "multi",
   
         selected: lambda do |connection|
           connection["auth_type"]
         end,
       },
   ```
   
3. Define the various authentication flows
   
   Define the multiple authentication flows within the `options` hash that contains all flows for your connector. Implement this through the `selected` lambda that receives the `connection` argument. This enables you to reference all connection inputs defined in `fields`, and expects a string value as the output.
   
   ```ruby
       authorization: {
         type: "multi",
   
         selected: lambda do |connection|
           connection["auth_type"]
         end,
   
         options: {
           stripe_oauth2: {
             type: "oauth2",
   
             fields: [
               { name: 'client_id' },
               { name: 'client_secret' },
             ],
   
             authorization_url: lambda do |connection|
               "https://connect.stripe.com/oauth/authorize?scope=read_write"
             end,
   
             token_url: lambda do
               "https://connect.stripe.com/oauth/token"
             end,
   
             apply: lambda do |_, access_token|
               headers("Authorization": "Bearer #{access_token}")
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
               headers("Authorization": "Bearer #{connection['api_key']}")
             end
           }
         },
       },
   ```
   
   Each key in the `option` hash must correspond exactly to one possible output value of the `selected` lambda. In our case, you can see that the result value of `selected` can be either `stripe_oauth2` or `stripe_api_key`, because they are the only two possible options that we defined in the `auth_type` input field. This matches exactly to the keys you defined in the `options` hash.
   
   Within each key, you can define further attributes for the authentication flows, such as `type`, `apply`, `acquire`, and others. This enables you to build specific authentication flows based on existing use cases. You can also define an additional key within each option as a nested `fields` array, to support the authentication flow for specific fields.
   
   In our example, we define fields `client_id` and `client_secret` for OAuth2, and the field `api_key` for API key authentication. We also define all keys required for an OAuth2 flow within the `stripe_oauth2` hash, and all keys required for API key authentication in the `stripe_api_key` hash.
   
     
   
   > **AUTHENTICATION TYPES**
   > 
   > Multi-authentication supports multiple authentication flows and types. Refer to the [SDK authentication](/en/developing-connectors/sdk/guides/authentication) guide for a complete list of authentication types.
   
   > **CONVERT AN EXISTING CONNECTOR TO MULTI-AUTH**
   > 
   > Use the `||` operator to specify the existing authentication method as the default when you add new authentication methods to an existing connector.
   > 
   > In the following example, the value left of the `||` operator, `auth_type`, is evaluated first. If the value is `nil` or `false`, the right value, `api_key`, is evaluated.
   > 
   > ```ruby
   > selected: lambda do |connection|
   >   connection["auth_type"] || 'api_key'
   > end,
   > ```
   
4. Set the API's base URI
   
   The API's base URI instructs Workato on the base URL of the API. This key is optional; however, it enables you to provide relative-only paths in the rest of your connector definition through HTTP requests. Learn how to configure your [base URI](/en/developing-connectors/sdk/sdk-reference/connection#base-uri).
   
   ```ruby
       base_uri: lambda do
          "https://api.stripe.com/"
       end
   ```
   
     
   
   > **URI CONNECTION ARGUMENT**
   > 
   > This lambda function has access to the `connection` argument. This is very useful when the base URI of the API changes depending on the user's instance. You can access the `connection` argument in the following format:
   > 
   > ```ruby
   >     base_uri: lambda do |connection|
   >       #some code here
   >     end
   > ```
   > 
   > Additionally, if the base URI changes with the authentication type, you can implement `IF-ELSE` structures to change it dynamically, as demonstrated in the following example:
   > 
   > ```ruby
   >     base_uri: lambda do |connection|
   >       if connection['auth_type'] == "stripe_oauth2"
   >        "https://api.stripe.com/"
   >       else
   >        "https://www.stripe.com/api"
   >       end
   >     end
   > ```
   
5. Test the connection
   
   After defining the fields and the flows for each authentication option, you must test the new connection. Use the `test` key:
   
   ```ruby
     test: lambda do |connection|
       get('/customers', limit: 1)
     end,
   ```
   
   The `test` key provides an endpoint for sending sample requests using the new credentials from the user. Successful connections get a `200 OK HTTP` response. In the preceding example above, a `GET` request to the `/api/channels` endpoint returns a `200` response when we have a valid API key.
   

## Connections SDK reference

For further information about the available keys within the `connection` key and their parameters, see the [SDK reference](/en/developing-connectors/sdk/sdk-reference/connection).

---
