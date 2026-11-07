---
url: 'https://docs.workato.com/en/connectors/openapi/update-record-action.md'
description: Update a record via OpenAPI.
---

# OpenAPI - Update record action

The **Update record** action updates a record using OpenAPI. The list of objects is dynamically generated based on the API endpoints found in the [OpenAPI document](https://restfulapi.net/).

![Update record action](/assets/openapi-update-record-action.DjhY9NCH.png)_Update record action_

## Input

| Input fields | Description |
| --- | --- |
| OpenAPI document source | Define how to provide the OpenAPI document to the connector. Workato recommends loading it from a URL. Alternatively, you can copy and paste the contents of the file. |
| Server URL | Provide a URL to the target host or service, for example, `https://app.example.com` or `https://example.com/app`. Relative endpoint paths from the OpenAPI document are appended to the server URL to construct the full endpoint URL. |
| Object | Select an object from the drop-down list of linked objects. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors.md
description: >-
  Learn how to use the OpenAPI connector as a template to build a custom
  application-specific connector in Workato with the Connector SDK.
---

# Using the OpenAPI connector to create custom connectors

An application-specific connector gives you full flexibility and the recommended user experience. However, building a connector from scratch might take a long time. To reduce the time building a connector, use the OpenAPI connector as a basis or template for creating an application connector.

Once converted, the new application-specific connector can be used in Workato recipes in place of the universal OpenAPI connector.

**Not sure if this is the right approach for you?** In most cases, the OpenAPI connector can be used as-is. There are, however, some situations where creating a custom connector may be required. For example:

- Customizing the connector's name or icon
- Implementing a custom authentication flow
- Adding app-specific connection fields
- Simplifying connection settings

If any of the above are applicable, creating a custom connector is likely the recommended approach.

* * *

## Prerequisites

To set up an OpenAPI connection, you'll need:

- **Familiarity with the Workato Connector SDK.** Refer to the [SDK documentation](/en/developing-connectors/sdk) for more info.
  
- **Privileges in Workato that allow you to:**
  
  - Create connections
  - Create and modify SDK connectors
- **A Swagger file that**:
  
  - Conforms to the OpenAPI v2 or v3 [specification](https://swagger.io/specification/v3/)
  - Is valid JSON or YAML

* * *

## Step 1: Install the connector

The first step is to install the connector in your Workato account. If you've already done this, skip to [Step 2](#step-2-create-a-new-sdk-connector-in-workato).

1. Open [the connector in the community library](https://app.workato.com/custom_adapters/50046/details?community=true).
   
2. Click **Install connector**.
   
3. Click **Release latest version**.
   

* * *

## Step 2: Create a new SDK connector in Workato

- [Step 2.1: Copy OpenAPI connector source code](#copy-source-code)
- [Step 2.2: Create an SDK connector](#create-sdk-connector)

### Step 2.1: Copy OpenAPI connector source code

1. Sign in to your Workato account if you aren't already.
   
2. Navigate to **Tools > Connector SDK**.
   
3. Click the **OpenAPI** tile.
   
4. Select and copy the contents of the **Source code**.
   

### Step 2.2: Create an SDK connector

1. Navigate back to the **Connector SDK** page.
   
2. Click **\+ New connector**.
   
3. Replace the contents of the **Source code** with the code you copied from [Step 2.1](#copy-source-code).
   
4. Click the **pencil icon** or the connector's name and re-name the connector:
   
   ![Renaming a new SDK connector](/assets/rename-connector.Cedfovq4.gif)
   
5. If you want to replace the connector's icon:
   
   1. Hover over the default icon until **Upload** appears:
      
      ![Renaming a new SDK connector](/assets/upload-icon._noxrqb_.gif)
      
   2. Click the icon.
      
   3. Select and upload a new icon.
      
6. Click **Save** to save the connector.
   

* * *

## Step 3: Customize the connector's configuration

This step will show you how to modify the connector's connection settings. There are two ways to accomplish this:

> **TIP**
> 
> We recommend customizing the source code only when necessary to simplify version upgrades. The more customization a connector has, the more complex an upgrade can be.

- [**Add custom fields or modify default connection fields.**](#add-modify-connection-fields)
- [**Hard-code connection values.**](#hard-code-connection-values) This approach is useful for simplifying connection setup for your users. For example: Instead of asking a user to provide a link to an OpenAPI document, you can hard-code it.

Refer to the [OpenAPI default connection fields reference](/en/connectors/openapi/reference/default-connection-fields) for more info about connection fields.

### Adding and modifying connection fields

To add or modify connection fields, locate the `connection.fields` list. Workato uses this list to generate the connection user interface.

By default, Workato populates this list with fields like **OpenAPI document source**, **Document URL**, and so on. If you don't want a field to display, you can remove it from the list, or [hard-code its value](#hard-code-connection-values) so users don't have to provide it.

For example: Your application only requires an API key for authentication. You could remove all default fields and add a single `api_key` field, where the user will be prompted to provide their API key:

```ruby
connection: {
  fields: [
    {
      name: 'api_key',
      label: 'API key',
      hint: 'Refer to <a href="<YOUR_DOC_URL>"><APP> docs</a> ' \
            'for help retrieving your API key.',
      optional: false,
      control_type: 'password'
    }
  ]
}
```

> **TIP**
> 
> Refer to the [SDK Schema reference](/en/developing-connectors/sdk/sdk-reference/schema) for more info about defining fields and their properties.

### Hard-coding connection values

To simplify connection setup for your users, you can hard-code connection values. This removes a step from setup by providing required connection values on behalf of the user.

**Except for authentication-related fields**, connection values can be hard-coded in the `adjust_connection` method. This method is invoked from other methods across the source code and affects the connector's behavior. When changes are made to this method, they're applied everywhere the method is invoked.

Use the following convention to add a field to `adjust_connection`. Replace `<FIELD_NAME>` with the `name` of the field, and `value` with its hard-coded value.

```ruby
methods: {
  adjust_connection: lambda do |connection|
    connection.merge (
      {
        '<FIELD_NAME>' => '<VALUE>',
        '<FIELD_NAME>' => '<VALUE>'
      }
    )
  end,
  [...]
}
```

For example: In the [previous section](#add-modify-connection-fields), all default connection fields were removed from `connection.fields`. These field values must be hard-coded in `adjust_connection` to successfully configure the connector.

In the example above, we removed the existing connection fields from `connection.fields`. To successfully configure the connector, we need to hard-code the fields in `adjust_connection`:

```ruby
methods: {
  adjust_connection: lambda do |connection|
    connection.merge (
      {
        'definition_mode' => 'url',
        'definition_url' => 'https://petstore3.swagger.io/api/v3/openapi.yaml',
        'base_url' => 'https://petstore3.swagger.io/api/v3/',
        'advanced' => {
          'test_endpoint' => '/pet/findByStatus?status=%3D%5B%22available%22%5D',
          'documentation_href' => 'https://redocly.github.io/redoc/?url=https://petstore3.swagger.io/api/v3/openapi.yaml'
        }
      }
    )
  end,
  [...]
}
```

Refer to the [OpenAPI connection field reference](/en/connectors/openapi/reference/default-connection-fields) for more info about fields, including names and descriptions.

**Note**: Required fields must be present in `connection.fields` or hard-coded in `adjust_connection`.

* * *

## Step 4: Implement authentication

If authentication fields have been customized or a custom authentication flow is required, you'll need to modify the `authorization` section of the source code.

> **NOTE**
> 
> If authentication details are provided via connection fields included in the default source code, you can skip this step.

The specific methods you'll need to modify can vary depending on your requirements and the authentication method being used. Refer to the [SDK Authorization reference](/en/developing-connectors/sdk/sdk-reference/connection/authorization#sdk-reference-authorization) for more info.

For example: In [Step 3](#add-modify-connection-fields), we replaced the default connection fields with a single `api_key` field. In this case, the `authorization.apply` method should be updated to correctly configure the custom authorization flow.

There are two ways to handle implementation, each with its own advantages:

- **Keep the code mostly as-is and only update the connection variable.** **Note**: Keeping the original code makes applying source code upgrades easier.
  
  View an example
  
  ```ruby
  authorization: {
    type: 'custom_auth',
    apply: lambda do |connection|
      connection = connection.merge(
        {
          'auth_method' => 'header',
          'auth_headers' => "api_key: Bearer #{connection['api_key']}",
        }
      )
      auth_method = connection['auth_method']
      # don't apply any credentials when requesting the API definition
      if connection['definition_mode'] == 'url' &&
         current_url == connection['definition_url']
        auth_method = nil
      end
      case auth_method
      when 'none'
        # nothing to do
      when 'basic'
        username = connection['basic_auth_user']
        password = connection['basic_auth_password']
        encoded = "#{username}:#{password}".encode_base64
        headers(Authorization: "Basic #{encoded}")
      when 'header'
        auth_headers_input = connection['auth_headers']
        lines = auth_headers_input.split(/\n+|\r+/)
        headers_hash = {}
        lines.each do |header|
          next if header.blank?
  
          header = header.split(':', 2)
          header_name = header[0]
          header_value = header[1].strip
          headers_hash[header_name] = header_value
        end
        headers(headers_hash)
      end
    end
  },
  [...]
  ```
  
- **Replace existing code with new, custom code.** With this approach, the code is specific and easy to read. The downside, however, is that due to the customization, applying source code upgrades may be more complex.
  
  View an example
  
  ```ruby
  authorization: {
    type: 'custom_auth',
    apply: lambda do |connection|
      headers(api_key: => "api_key: Bearer #{connection['api_key']}")
    end
  },
  [...]
  ```
  

* * *

## Step 5: Configure on-prem connectivity

If you require on-prem connectivity, you can configure the connector to communicate through an [on-prem agent (OPA)](/en/on-prem/agents).

> **NOTE**
> 
> You can skip this step if on-premise connectivity isn't required.

After configuring a new OPA, locate the `secure_tunnel` key at the beginning of your SDK connector's source code:

![The secure\_tunnel key in connector source code](/assets/secure-tunnel-key.B18k8UZO.png)

When set to `true`, the **Is this app in a private network**? field in the connector's setup will be available. Users can then select the OPA to connect to.

* * *

## What's next?

That's it - you've created a custom connector! From here, you can:

- [Customize the connector's user interface](/en/connectors/openapi/guides/customizing-openapi-interfaces)
- [Learn more about connection fields](/en/connectors/openapi/reference/default-connection-fields)
- [Learn about upgrading source code versions](/en/connectors/openapi/guides/upgrading-openapi-based-connector-source-code)

---

---
url: >-
  https://docs.workato.com/en/connectors/openapi/guides/customizing-openapi-interfaces.md
description: >-
  Customize the user interface that the OpenAPI connector generates, including
  object and field names, hints, API operation grouping, and hidden fields.
---

# Customizing user interfaces for OpenAPI connectors

In addition to universal connectivity, the OpenAPI connector allows you to customize its user interface in Workato. We recommend customizing the interface to improve the user experience.

In this guide, we'll show you how to:

1. [Customize object names and hints](#objects)
2. [Customize how API operations are grouped into actions](#api-operation-grouping)
3. [Hide action input fields](#ignore-input-fields)
4. [Customize the connector's application name](#application-name)

* * *

## Best practices

When customizing the user interface of an OpenAPI connector, we recommend following these best practices:

1. **Verify object hints are present and accurate.** Ensuring information is easy to access and understand will help your users get up and running quickly.
   
   If you have the ability to directly edit your Swagger file, add object hints and external links if needed.
   
2. **If building a custom connector**, replace `OpenAPI` [with your application's name](#application-name).
   
3. **Test, test, test!** Whether you're developing a custom connector or customizing the interface for a standard OpenAPI connector, make sure to iteratively test your changes. Identifying an issue is easier if you test one change at a time.
   

* * *

## Customizing objects

Details about objects are automatically extracted from endpoint fields. In this section, we'll cover:

- Choosing the [object name field](#object-names)
- [Customizing object hints and links](#object-hints-links)
- [Substitution rules for object names and hints](#object-name-hint-substitutions)
- Using [Static object names](#static-object-names) to map user-friendly display names for objects and operations

### Example endpoint

The examples in this article will use the following endpoint:

```json
/*  swagger-petstore-1-1.json */

{
   "paths":{
      "/pet":{
         "post":{
            "tags":[
               "pet"
            ],
            "summary":"Create a new pet",
            "description":"Add a new pet to the store. [More information](https://app.swaggerhub.com/apis/Colon-Org/Swagger-PetStore-3.0/1.1)",
            "operationId":"createPet",
            "requestBody":{
               "description":"Add a new pet to the store",
               "content":{ ... },
               "required":true
            }
         }
      }
   }
}
```

### Customizing object names

**Object names** refer to the types of records an API interacts with, such as `pet` or `user`. In the Recipe Editor, users can select the type of object an action interacts with:

![Highlighted object picker field in the Workato UI](/assets/select-object.CMHNP1NX.png)_Picklist of which object to operate on_

Objects names are derived from the object's `summary`, `description`, or `operationId` field. When setting up the connection, users are prompted to select one of these options in the **Object name** field.

![Select the object name field](/assets/object-name-field.CI8IfYhi.png)_Connection setup: Select the object name field_

If `summary` is chosen, the object name will be based on _"Create a new pet"_, (view [example endpoint](#example-endpoint)). After excluded words are removed (such as `a` or `and`), the resulting object name will be `Pet`.

**Note**: You can hard-code the object name field if developing a custom connector. Refer to the [Using The OpenAPI Connector To Create Custom Connectors](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors#hard-code-connection-values) guide for more info.

However, we recommend directly editing the Swagger file instead.

## Customizing object hints and links

**Object hints** are short, helpful descriptions that display below the object picker field:

![Example documentation link in object hint in Workato Recipe Editor](/assets/external-doc-link-in-ui.DOpTd2Uw.png)_Object hints_

Users can use an object's `summary` or `description` field as the object name by default. When setting up the connection, users are prompted to select one of these options in the **Object hint** field.

If `description` is chosen, the object hint will be _"Add a new pet to the store. [More information](https://app.swaggerhub.com/apis/Colon-Org/Swagger-PetStore-3.0/1.1)"_, (view [example endpoint](#example-endpoint)).

> **EXTERNAL LINK FORMAT**
> 
> External links in object field hints must adhere to one of the following formats:
> 
> - **Standard links**, which contains the full URL and is typically formatted as `[link text](url)`. For example: `[Workato](https://www.workato.com)`. These types of links are rendered as-is and don't require any configuration.
> - **Categorized relative links**, formatted as `[link text](key:path)`. The `key` references a base URL that, when combined with the `path`, creates a full URL. For example:
>   - Base URL: `https://docs.swagger-store.io/docs/`
>   - Path: `pets/statuses`
>   - Full URL: `https://docs.swagger-store.io/docs/pets/statuses`
> 
> ### Adding a base URL
> 
> In the following example, set up the `key` of _"doc"_:
> 
> ```json
> /*  swagger-petstore-1-1.json */
> 
> {
>   ...
>   "description":"Multiple status values can be provided with comma separated strings. See [documentation](doc:pets/statuses) for all possible statuses."
>   ...
> }
> ```
> 
> You will need to supply the base URL (`https://docs.swagger-store.io/docs/`) to complete the helplink.
> 
> Configure the **External documentation links** connection fields in Workato:
> 
> ![External documentation links configured for an OpenAPI connector in Workato](/assets/external-doc-links.WQuUwnd7.png)_Connection setup: External documentation links_

**Note**: You can hard-code the object hint field if developing a custom connector. Refer to the [Using the OpenAPI connector to create custom connectors](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors#hard-code-connection-values) guide for more info.

However, we recommend directly editing the Swagger file instead.

## Using substitution rules

In some cases, removing filler words and keywords from object names and hints doesn't produce the recommended results.

Let's say we're working with [**object names**](#object-names) and want to use the `summary` field for extraction. The object's `summary` is `"Allows users to create a pet"`.

If only filler words and keywords are removed, the result will be `Allows users to pet` - definitely not an ideal result.

You can modify extracted values before keywords and filler words are removed using the [**Object name substitutions**](/en/connectors/openapi/reference/default-connection-fields#object-name-substitutions) and [**Object hint substitutions**](/en/connectors/openapi/reference/default-connection-fields#object-hint-substitutions) fields.

The table below demonstrates how a substitution rule that strips `Allows users to` from `Allows users to create a pet` would improve the final result:

| Description | Value |
| --- | --- |
| **Input** | Value is extracted from the object's `summary` field | `Allows users to create a pet` |
| **Pattern** | Uses capture group to extract characters after `Allows users to` | `Allows users to (.+)` |
| **Replacement** | Replaces value with results of first capture group ( `(.+)` ) | `\1` |
| **Substitution result** | Value after applying the substitution rule | `Create a pet` |
| **Final result** | Final object name after removing filler words (`a`, `the`, etc.) and known words (ex: `Create`) from **Substitution result** | `Pet` |

> **NOTE**
> 
> When multiple substitution rules are present:
> 
> - Workato applies the rules in the order they are present
> - The value is replaced for every matching `pattern`
> - Subsequent rules use the previous rule's result
> 
> Additionally, some hints contain [relative links to external sites](#external-links).

## Static object names

If the OpenAPI spec does not provide user-friendly names for individual API endpoints, use Status object names to map descriptive display names for eat object and operation.

To remap the operation in the [example endpoint](#example-endpoint), we will provide a display name for the "Create a new Pet" (`"operationID": "createPet"`).

![Connection setup: Adding a static object name](/assets/static-object-names.D5JEnhxL.png)_Connection setup: Adding a static object name_

* * *

## Customizing API operation grouping

- [Understanding API operation assignment](#api-operation-assignment)
- [Default API operation grouping rules](#default-api-operation-grouping-rules)
- [Substitution rules for API operations](#api-operation-substitutions)

### Understanding API operation assignment

The OpenAPI connector contains a set of default rules for grouping API operations into recipe actions. These rules also control the objects displayed in the object picker when setting up an action.

The following image demonstrates how two API operations from a Swagger file would map to actions in the Recipe Editor:

![Examples of API operation assignment in the Workato Recipe Editor](/assets/operation-grouping-example.CC196t3h.png)

> **MISSING SOME API OPERATIONS?**
> 
> If an action doesn't contain an API operation you expect it to, look for it in the **Execute operation** action.
> 
> If an API operation can't be matched, the connector will group the operation under this 'fallback' action. Refer to the [Default operation grouping rules section](#default-api-operation-grouping-rules) below for more info.

Grouping rules are based on two factors:

- **Keywords in the API operation's summary and operation ID**. When the connector parses the Swagger file to create recipe actions, it's also checking for keywords in the API operation's `summary` and `operationId` fields. The connector uses these keywords to assign operations to recipe actions.
  
  For example, an operation ID of `createPet` would assign the operation to the **Create record** action. This is because the operation ID contains the word `create`.
  
- **The operation's HTTP method**, which is specified in the Swagger file. HTTP methods describe the type of action an operation performs for a given object, such as `create` (usually `POST`) or search (`GET`).
  
  For example, operations that use the `GET` method would be assigned to either the **Search records** or **Get record details by ID** action.
  
  To disable this grouping method, set the **Use HTTP method semantics for grouping operations** field to **No** when setting up the connection. This can be useful if an API doesn't follow REST standards. For example, every endpoint uses the `POST` method.
  

### Default API operation grouping rules

The following table details the default operation grouping rules for OpenAPI connectors. The table columns are as follows:

- **Name and description**: The name and description of the action
  
- **Operation keywords**: The keyword(s) the connector uses to perform [API operation grouping](/en/connectors/openapi/guides/customizing-openapi-interfaces#api-operation-grouping). If an API operation's `summary` or `operationId` contains these keywords, it will be mapped to this action in the Recipe Editor.
  
  For example: If a `summary` or `operationId` contains `add` or `adds`, the API operation will be assigned to the **Create record** action.
  
- **HTTP methods**: If the **Use HTTP method semantics for grouping operations** option is enabled, the connector will match the methods list to this action.
  
  For example: If an operation uses the `POST` method, it will be assigned to the **Create record** and **Update record** actions.
  

| Name and description | Operation keywords | HTTP methods |
| --- | --- | --- |
| **Create record** Creates a new record of a specified object type. For example, if a `pet` object is selected, this action will create a new `pet` record. | create, creates; update, updates; post, posts; add, adds; upload, uploads; new | POST, PUT |
| **Update record** Updates an existing record using its unique identifier. | create, creates; update, updates; put, puts; set, sets; upload, uploads; modify, modifies; manipulate, manipulates | PUT, POST, PATCH |
| **Search records** Searches for records of a specified object type. | return, returns; find, finds; list, lists (all); search, searches; retrieves objects/records/all; get(s) (a) collection (of); get list (of) | GET |
| **Get record details by ID** Retrieves a record using its unique identifier. | get, gets; return, returns; find, finds; show, shows; retrieve, retrieves; single; download, downloads; getSingle; get-single | GET |
| **Delete record** | delete, deletes; remove, removes; kill, kills | DELETE |
| **Execute operation** This action is considered a 'fallback'. If an API operation can't be matched to a specific action, it will be grouped under this action. |  | POST, PUT, GET, DELETE, PATCH |

### Substitution rules for API operations

If operation IDs in your Swagger file aren't as simple as `createPet` or `searchPets`, you can use substitution rules to improve or customize API operation grouping.

#### How to apply substitution rules

Substitution rules are applied to the specified fields before the grouping logic. If a field contains certain patterns that do not align with your planned grouping, you can create rules to replace them with preferred terminology or structure.

![Substitution rules](/assets/substitution-rules-1.DdjnBklc.png)_Apply substitution rules to API operation details_

To apply substitution rules fill in the following fields in Workato:

1. - Apply to
   - Select the part of the API operation detail you plan the rule to affect. You can choose from `Operation ID`, `Summary`, `Description`, and `Path`.
2. - Pattern
   - Enter the regular expression pattern that identifies the text you plan to change.
3. - Replacement
   - Provide the new text that replaces the identified pattern.

The following table demonstrates how a substitution rule transforms an operation ID of `operation-8452/pet-create` to `create-pet`:

| Description | Value |
| --- | --- |
| **Input** | Value is extracted from object's `operationId` field | `operation-8452/pet-create` |
| **Pattern** | Uses capture groups to extract the `object` (`pet`) and verb (`create`) of the operation ID | `operation-8452/(?<object>.+)-(?<verb>.+)` |
| **Replacement** | Replaces value with results of the capture groups | `\2-\1` |
| **Final result** | Final operation ID after applying the substitution rule | `create-pet` |

The connector can now assign the API operation to the **Create record** action with an improved operation ID of `create-pet`.

> **NOTE**
> 
> When multiple substitution rules are present:
> 
> - Workato applies the rules in the order they are present
> - The value is replaced for every matching `pattern`
> - Subsequent rules use the previous rule's result

#### String substitutions

String substitutions precede the application of built-in keyword rules. These substitutions modify the operation's `summary`, `operationId`, `description`, and `path` to ensure endpoint attributes match the expected keywords for action mapping.

The following table details the operation grouping rules for OpenAPI connectors after string substitutions:

| Action type | Operation keywords | HTTP methods | Special conditions |
| --- | --- | --- | --- |
| **Create record** | `posts`, `post`, `creates or updates`, `create or update`, `creates new`, `create new`, `create a new`, `creates a new`, `creates`, `create`, `adds`, `add`, `uploads`, `upload` | POST, PUT | \- |
| **Update record** | `puts`, `put`, `patches`, `patch`, `creates or updates`, `create or update`, `updates`, `update`, `sets`, `set`, `uploads`, `upload`, `edits`, `edit`, `modifies`, `modify`, `manipulates`, `manipulate` | PUT, POST, PATCH | \- |
| **Search records** | `returns a collection of`, `return a collection of`, `returns collection of`, `return collection of`, `returns a list of`, `return a list of`, `returns list of`, `return list of`, `returns a collection`, `return a collection`, `returns collection`, `returns a list`, `return a list`, `returns\list`, `return list`, `list or find`, `lists or finds`, `gets a collection of`, `gets a collection`, `get collection of`, `get collection`, `get list\of`, `get list`, `get all`, `gets all`, `list all`, `lists all`, `lists`, `list`, `searches`, `search`, `retrieves objects`, `retrieve records`, `retrieves all`, `retrieve all` | GET | Must not have an `id`, `ids`, or `<record_id_field_name>` request parameter. Must have a response field of type array. |
| **Get record details by ID** | `gets`, `getSingle`, `get-single`, `get single`, `get`, `downloads`, `download`, `returns`, `return`, `finds`, `find`, `shows`, `show`, `retrieves`, `retrieve`, `provides`, `provide`, `query`, `reads`, `read` | GET | Must have an `id`, `ids`, or `<record_id_field_name>` request parameter. Must not be prefixed with **Search records** action keywords. |
| **Delete record** | `deletes`, `delete`, `removes`, `remove`, `kills`, `kill` | DELETE | \- |

#### New/update trigger requirements

For the **New/update** trigger to correctly identify relevant API operations, each operation must meet the following conditions:

- **Satisfy search records action criteria**: Aligns with the requirements set for the **Search records** action.
- **Timestamp request parameter**: Includes a timestamp request parameter, typically named `update`, `change`, `modify`, `time`, `stamp`, `since`, or `start`.
- **Timestamp in response**: Features a timestamp field in the response, recording the last update time. Common field names are `update`, `change`, `create`, `modify`, `modified`, `time`, or `stamp`.
- **Identifier in response**: Contains an identifier field in the response, typically named `id` or `name`.

#### HTTP method-based grouping

The `use_operation_names_for_grouping` setting in the OpenAPI connector determines how HTTP methods influence operation grouping.

When this setting is enabled, the following rules are applied based on their HTTP methods:

- **Create record** action: Assigns an endpoint if the HTTP method is POST or PUT.
- **Update record** action: Assigns an endpoint if the HTTP method is POST or PUT.
- **Delete record** action: Assigns an endpoint if the HTTP method is DELETE.
- **Search records** action: Assigns an endpoint if the HTTP method is GET.
- **Get record details by ID** action: Assigns an endpoint if the HTTP method is GET, provided the operation doesn't qualify for the **Search records** action.
- **Execute operation** action: Assigns an endpoint if it doesn't fit into the **Search records**, **Create record**, **Update record**, **Get record details by ID**, or **Delete record** actions.
- **New/update** trigger: Assigns an endpoint if the HTTP method is GET.

When this setting is disabled, the following rules are applied for operation grouping:

- **Update record** action: Available only when the endpoint isn't classified under the **Create record** action.
- **Delete record** action: Available only when the endpoint isn't classified under the **Create record** or **Update record** action.
- **Search records** action: Available only when the endpoint isn't classified under the **Delete record**, **Create record**, or **Update record** actions.
- **Get record details by ID** action: Available only when the endpoint isn't classified under the **Delete record**, **Search records**, **Create record**, or **Update record** action.
- **Execute operation** action: Available for endpoints not fitting into the **Search records**, **Create record**, **Update record**, **Get record details by ID**, or **Delete record** actions.

## Filtering API endpoints

This section instructs you on how to filter API endpoints effectively.

### List of rules

You can define rules to manage API endpoint visibility by configuring each rule to show or hide endpoints. This gives you control over which endpoints appear.

![Filter rules](/assets/filter-endpoint-rules.XMK3cvAp.png)_View and manage your API endpoint filter rules_

### How to define a rule

To define filtering rules, fill in the following fields in Workato:

![Filter endpoint field](/assets/filter-endpoint-fields.mVtk-FJ8.png)_Define the specifics of your filtering rule_

1. Choose to include or exclude endpoints in the **Type** field. `Include` rules are processed first, followed by `exclude` rules.
   
2. Choose HTTP methods (`POST`, `GET`, `PUT`, `PATCH`, `DELETE`) in the **HTTP Method** field to filter endpoints by operation type.
   
3. Enter [regular expressions](https://en.wikipedia.org/wiki/Regular_expression#POSIX_basic_and_extended) to match endpoint [tags](https://swagger.io/specification/#tag-object) in the **Tag** field.
   
4. Enter [regular expressions](https://en.wikipedia.org/wiki/Regular_expression#POSIX_basic_and_extended) to match [operation IDs](https://swagger.io/specification/#operation-object) in the **Operation ID** field.
   
5. Enter [regular expressions](https://en.wikipedia.org/wiki/Regular_expression#POSIX_basic_and_extended) to match URL [paths](https://swagger.io/specification/#paths-object) in the **URL Path** field.
   

Ensure each endpoint meets all specified conditions for inclusion or exclusion. The system applies `AND` logic in rule processing.

#### Configuration sample

```ruby
{
  ...
  "advanced" => {
    "endpoint_filter_rules" => [
      {
        "type" => "include",
        "operation_id" => "createPet"
      },
      ...
    ]
  }
  ...
}
```

## Ignoring action input fields

Actions in Workato contain input fields used to configure the action. Using the **Ignore specific request fields** field when setting up the connection, you can specify fields to ignore. Ignored input fields are hidden from view when users set up actions.

For example, let's say an endpoint contains a `links` field. Using the following configuration, this field can be ignored:

![Connector configured to ignore input fields named links](/assets/ignore-input-fields.BVUc11nu.png)

Nested fields can also be ignored by providing the field path using dot notation. For example, if `links` had a `url` field you wanted to ignore, you would enter `links.url` as the **Field name**:

![Connector configured to ignore input fields named links](/assets/ignore-nested-input-fields.4TF67gGv.png)

* * *

## Customizing the application name

In the default source code, `OpenAPI` is used in several places. We recommend replacing this value with the name of your application when you create a custom connector.

> **CUSTOMIZE APPLICATION NAME FOR CUSTOM CONNECTORS**
> 
> This section applies only to [custom OpenAPI connectors](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors).

Along with changing the application name, you can change other text elements to improve the user experience. For example, changing `via` to `in`.

Let's look at an example using the `create_record` action. In this case, `OpenAPI` is used in the action's subtitle:

```ruby
create_record: {
  title: 'Create record',
  subtitle: 'Create record via OpenAPI',
  description: lambda do |_input, picklist_label|
    record = picklist_label['object_for_create'] || 'record'
    "Create <span class='provider'>#{record}</span> " \
      'via <span class="provider">OpenAPI</span>'
  end,
  [...]
```

Then in the recipe editor, the action will display like this:

![Highlighted action subtitle in the Workato UI](/assets/app-name-in-action-subtitle.HClDveZ3.png)

Along with action subtitles, changing the application name to that of your application can affect several elements in the recipe editor, including:

- **Object field hints**:
  
  ![Highlighted object field hint in the Workato UI](/assets/app-name-object-hint.DzLOT47B.png)
  
- **Recipe action descriptions**:
  
  ![Highlighted action subtitle in the Workato UI](/assets/app-name-action-description.DemoeoI-.png)
  

To simplify replacing `OpenAPI` with your application's name, perform a **case-sensitive** find/replace in the source code. **Note**: To perform this action, you may need to use a text editor like Sublime Text.

---

---
url: >-
  https://docs.workato.com/en/connectors/openapi/guides/upgrading-openapi-based-connector-source-code.md
description: >-
  Learn how to apply new versions of the OpenAPI source code and re-release the
  connector in your workspace, for both customized and non-customized
  connectors.
---

# Upgrading An OpenAPI-based Connector's Source Code

Over time, new versions of the OpenAPI source code will be released. These updates can include new features, enhancements, and/or bug fixes.

When a new version of the OpenAPI is available, the following banner will display on the connector's source code page:

![Updated OpenAPI connector version banner in the Workato UI](/assets/upgrade-available-banner.ucDRZCvl.png)

To take advantage of the updates, you'll need to apply the new version and re-release the connector in your workspace. How you perform the upgrade depends on whether you've customized the connector or not:

- [Non-customized connector](#upgrade-non-custom-connector)
- [Customized connector](#upgrade-custom-connector)

* * *

## Prerequisites

To upgrade an OpenAPI connector's source code, you'll need:

- **Familiarity with the Workato Connector SDK.** Refer to the [SDK documentation](/en/developing-connectors/sdk) for more info.
  
- **Privileges in Workato that allow you to:**
  
  - Modify SDK connections
- **For [customized connectors](#upgrade-custom-connector), you'll need a file comparison tool** like [Diffchecker](https://www.diffchecker.com/).
  

* * *

## Upgrading A Non-Customized Connector

1. Sign into your Workato account, if you aren't already.
   
2. Navigate to **Tools > Connector SDK**.
   
3. Click the tile of the OpenAPI connector you want to upgrade.
   
4. In the **An update is available!** banner, click the **Update connector** button:
   
   ![Updated OpenAPI connector version banner in the Workato UI](/assets/upgrade-available-banner.ucDRZCvl.png)
   
5. After reviewing the changes, click the **Release latest version** button in the top right corner of the page. This releases the new version of the connector in your workspace and allows it to be used in recipes.
   
6. In the window that displays, summarize the changes:
   
   ![Change summary and confirmation window](/assets/confirm-version-release-window.Co6Sj0jz.png)
   
7. When finished, click **Release**.
   

If successful, a **Successfully released version \[X\]** banner will display.

* * *

## Upgrading A Customized Connector

If you've customized your connector's source code, the upgrade process has some additional steps:

- [Step 1: Retrieve code for both versions](#retrieve-code-versions)
- [Step 2: Compare versions and resolve conflicts](#compare-resolve-code)
- [Step 3: Test the new version](#test-new-version)
- [Step 4: Release the new version](#release-new-version-custom)

This tutorial uses a file comparison tool - like the one built into GitHub - to identify differences between code versions. If you've used Workato's [Recipe Diff](/en/recipe-development-lifecycle/compare-versions-with-recipe-diff) feature, the concept is the same but for recipes.

In the image below, for example, is a text comparison of a file in GitHub:

![Example of a diff in GitHub](/assets/github-diff.HkViAs-G.png)

### Step 1: Retrieve Code For Both Versions

In this step, you'll retrieve your customized connector code and the source code for the new version.

1. Sign into your Workato account, if you aren't already.
   
2. Navigate to **Tools > Connector SDK**.
   
3. Click the tile of the OpenAPI connector you want to upgrade.
   
4. Select and copy the customized **Source code** to a convenient location, like a text file. **You'll need this in the next step.**
   
5. In the **An update is available!** banner, click the **Update connector** button. This will overwrite the customized source code with the new version:
   
   ![Updated OpenAPI connector version banner in the Workato UI](/assets/upgrade-available-banner.ucDRZCvl.png)
   

Leave this page open for now - you'll need it in the next step.

### Step 2: Compare Versions And Resolve Conflicts

In this step, you'll compare the code versions in your file comparison tool, apply changes, and resolve conflicts.

The instructions and examples in this section use [Diffchecker](https://www.diffchecker.com/), but you can use the file comparison tool you're comfortable with.

1. In your file comparison tool, copy and paste your **customized code** into the **Original Text** field.
   
2. Copy and paste the **new version source code** in the **Changed Text** field.
   
   Your setup should be similar to this:
   
   ![Code setup in the Diffchecker app](/assets/diffchecker-code-setup.Bp2NDGfw.png)
   
3. Click **Find Difference**.
   
4. Differences between the code versions will be highlighted. On a section-by-section basis, compare the versions and decide what to **keep from your customized code** and what to **use from the new version code**.
   
   In the example below, we kept the **title of our customized connector** by merging it into the **new version code**:
   
   ![Applying a change from customized code to new version code](/assets/diffchecker-apply-changes.DwODFDZZ.gif)
   
5. Repeat the previous step until you've reviewed the entirety of the changes between the versions.
   

### Step 3: Test The New Version

In this step, you'll use the [SDK Test code tab](/en/developing-connectors/sdk/quickstart/debugging) to test the new version of the connector.

**Note**: At least one active connection is required to use the **Test code** tab.

1. In your file comparison tool, copy the new version of your customized code.
   
2. Navigate back to the browser window where the connector is open in your Workato account.
   
3. Paste the customized code into the **Source code** field.
   
4. In the **Debug** section, use the **Connection** and **Actions** options to test the new version.
   
   **Note**: The **Test code** tab runs on the latest version of the code currently in the code editor. Before a test is run, unsaved changes will be saved and a new latest version of the connector will be created. A notification will display when this occurs.
   

When you've finished testing and resolving any issues, move onto [releasing the new version](#release-new-version-custom).

### Step 4: Release The New Version

In this step, you'll release the new version of the connector in your workspace. Releasing the new version allows it to be used in recipes.

1. After you've finished testing the new version, click the **Release latest version** button in the top right corner of the page.
   
2. In the window that displays, summarize the changes:
   
   ![Change summary and confirmation window](/assets/confirm-version-release-window.Co6Sj0jz.png)
   
3. When finished, click **Release**.
   

If successful, a **Successfully released version \[X\]** banner will display.

---

---
url: >-
  https://docs.workato.com/en/connectors/openapi/reference/default-connection-fields.md
description: >-
  Reference for the default connection fields used by the OpenAPI connector,
  including authentication method, document source, and OAuth 2.0 settings.
---

# OpenAPI default connection fields reference

When using the [OpenAPI connector to create custom connectors](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors), you control the fields end users see when setting up a connection.

This guide serves as a reference for the default connection fields in the [universal OpenAPI connector](/en/connectors/openapi/).

## Field reference documentation

Each connection field in the OpenAPI connector has its own section in this guide. In each section, you'll find the following info:

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>Description</strong></td><td>A description of the field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>UI name</strong></td><td>The name of the field as it displays in Workato, ex: <strong>Authentication method</strong></td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>The name of the field in the connector's source code, ex: <code>auth_method</code></td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Whether the field is required or not</td></tr></tbody></table>

## Required fields

While you can customize connection fields, the following fields must be present in [`connection.fields`](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors#add-modify-connection-fields) or [`adjust_connection`](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors#hard-code-connection-values) to successfully configure [a custom OpenAPI connector](/en/connectors/openapi/guides/using-openapi-to-create-custom-connectors):

- [Authentication method](#auth-method) (`auth_method`)- [Basic auth user](#basic-auth-user) (`basic_auth_user`) **\***- [Document content](#definition-content) (`definition_content`) **\***- [OpenAPI document source](#definition-mode) (`definition_mode`)- [Document URL](#definition-url) (`definition_url`) **\***- [Header authorization](#auth-headers) (`auth_headers`) **\***- [OAuth2 authorization URL](#authorization-url) (`authorization_url`) **\***- [OAuth2 token URL](#token-url) (`token_url`) **\***- [Client ID](#client-id) (`client_id`) **\***- [Client Secret](#client-secret) (`client_secret`) **\***- [Username](#username) (`username`) **\***- [Password](#username) (`username`) **\***- [Query param authorization](#query-params) (`query_params`) **\***- [Server URL](#base-url) (`base_url`)

> **INFO**
> 
> The `*` symbol indicates the marked field is dependent on another field. Refer to the marked field's documentation for more information.

## Allow long field hints

If set to `No`, object hints will be stripped to a single paragraph. The default is `No`.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Allow long field hints</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.allow_multi_paragraph_hint</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Authentication method

> **THIS IS A REQUIRED FIELD.**

The authentication method the connection uses. The value of this field determines what other values the user must provide for authentication:

- `none` (no other input required)
- `basic` (see [Basic auth user](#basic-auth-user) and [Basic auth password](#basic-auth-password))
- `header` (see [Header authorization](#header-authorization))
- `query` (see [Query param authorization](#query-param-auth))
- `oauth2_client_credentials` (see [OAuth2 token URL](#token-url), [How does the API require credentials to be sent to request a token?](#access-token-request-mode), [Client ID](#client-id), [Client Secret](#client-secret) and [Scopes](#scopes))
- `oauth2_authorization_code` (see [OAuth2 authorization URL](#authorization-url), [OAuth2 token URL](#token-url), [How does the API require credentials to be sent to request a token?](#access-token-request-mode), [Client ID](#client-id), [Client Secret](#client-secret) and [Scopes](#scopes))
- `oauth2_resource_owner_password` (see [OAuth2 token URL](#token-url), [Client ID](#client-id), [Client Secret](#client-secret), [Username](#username), [Password](#password) and [Scopes](#scopes))

Refer to the [OpenAPI authentication guide](/en/connectors/openapi/guides/authentication) for more info about supported authentication methods.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Authentication method</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>auth_method</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes</td></tr></tbody></table>

## Basic auth user

> **THIS IS A REQUIRED FIELD.**

The name of the application user/account.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Basic auth user</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>basic_auth_user</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, if <strong>Authentication method</strong> is set to <code>basic</code></td></tr></tbody></table>

## Basic auth password

The password of the user. An alternative to your password would be an API key or API token, retrieved from your account settings.

This should be kept secret.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Basic auth password</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>basic_auth_password</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Schema depth limit

Define the maximum depth for nested fields to be includes in the input and output schema descriptions.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Schema depth limit</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.max_schema_depth</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

> **Limit nested fields**
> 
> If your input or output schema contains too many nested fields, it may be difficult to use the connector.
> 
> For example, a `company` object has a property of `parentCompany` which is another `company` object. Further, the parent company may also have another `parentCompany`.
> 
> [Schema depth limit](#max-schema-depth) and [Schema recursion limit](#max-recursion-depth) allows you to prevent this nesting from continuing indefinitely.

## Schema recursion limit

Define the maximum depth recursive schema definitions to be included in input and output schema descriptions.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Schema recursion limit</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.max_recursion_depth</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

> **Limit nested fields**
> 
> If your input or output schema contains too many nested fields, it may be difficult to use the connector.
> 
> For example, a `company` object has a property of `parentCompany` which is another `company` object. Further, the parent company may also have another `parentCompany`.
> 
> [Schema depth limit](#max-schema-depth) and [Schema recursion limit](#max-recursion-depth) allows you to prevent this nesting from continuing indefinitely.

## Document content

> **THIS IS A REQUIRED FIELD.**

Content of the OpenAPI document. Format is either JSON or YAML. Supports OpenAPI v3.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Document content</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>definition_content</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>OpenAPI document source</strong> is set to <code>content</code></td></tr></tbody></table>

## Documentation links

Link to the application documentation, user guides, or company web site. This documentation link will be provided in the help text of your connector's triggers or actions.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Documentation link</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.documentation_href</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## OpenAPI document source

> **THIS IS A REQUIRED FIELD.**

Defines how to provide the OpenAPI document to the connector. The preferred approach is to load it from a URL. Otherwise, copy and paste the contents of the file.

The value of this field determines what other values the user must provide. Must be one of the following:

- `url` (see [Document URL](#definition-url))
- `content` (see [Document content](#definition-content))

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>OpenAPI document source</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>definition_mode</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes</td></tr></tbody></table>

## Document URL

> **THIS IS A REQUIRED FIELD.**

This URL must be publicly accessible at all times. Any future changes to the document itself appear automatically in the Workato recipe editor. The document can be in either JSON or YAML format. Supports OpenAPI v3.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Document URL</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>definition_url</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>OpenAPI document source</strong> is set to <code>url</code></td></tr></tbody></table>

## External documentation links

When defined, allows object field descriptions to link to external websites like API references or documentation.

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#external-links) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>External documentation links</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.external_links</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Filter API endpoints

Defines rules for filtering endpoint.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Filter API endpoints</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.endpoint_filter_rules</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

### Sample

```ruby
{
  ...
  "advanced" => {
    "endpoint_filter_rules" => [
      {
        "type" => "include",
        "operation_id" => "createPet"
      },
      ...
    ]
  }
  ...
}
```

> **API endpoint filter rules**
> 
> You can use **include** or **exclude** filter rules.
> 
> You can also filter based on the HTTP method (`http_method`), Tag (`tag`), Operation ID (`operation_id`), or URL path (`Path`).

## Header authorization

A list of headers to be added to API requests. Used for applications that require additional headers outside of the usual username and password or API key, or if you want to customize the headers sent in the request. Header authentication can be used when you have a generated token ready for use.

Examples:  
`API-Key: 1234567890   X-API-Token: abc123`

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Header authorization</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>auth_headers</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>header</code></td></tr></tbody></table>

## Ignore request fields

Defines the specific request fields the connector should ignore.

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#ignore-input-fields) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Ignore specific request fields</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.ignore_request_fields</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## OAuth2 authorization URL

URL that Workato redirects you to when you select the ‘Connect’ button. This usually brings you to the login screen of your app.

This should be publicly available from the API documentation of the app you’re connecting to, under the Authentication section.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>OAuth2 authorization URL</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>authorization_url</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code> or <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 token URL

URL that Workato will retrieve an auth token from. This auth token is used to verify that we have permission to access your app and its data.

This should be publicly available from the API documentation of the app you’re connecting to, under the Authentication section.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>OAuth2 token URL</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>token_url</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code> or <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 token request mode

Send client ID and secret in token request body or as a base64 encoded string in the header.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>How does the API require credentials to be sent to request a token?</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>access_token_request_mode</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code>.</td></tr></tbody></table>

## OAuth2 client ID

Public ID of the OAuth app that should be tied to Workato.

This is usually found in the Settings or Integrations page (or equivalent) of your logged in app account that you wish to connect to and should be kept secret.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Client ID</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>client_id</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code> or <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 client secret

Matching private key that the application will verify along with the Client ID.

This is usually found in the Settings or Integrations page (or equivalent) of your logged in app account that you wish to connect to and should be kept secret.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Client Secret</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>client_secret</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code> or <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 user

The name of the application user/account.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Username</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>username</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 password

The password of the user. An alternative to your password would be an API key or API token, retrieved from your account settings.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Password</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>username</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## OAuth2 scopes

Scopes are permissions that you can request from the app.

This is usually found in the Settings or Integrations page (or equivalent) of your logged in app account that you wish to connect to.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Scopes</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>scopes</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>oauth2_client_credentials</code> or <code>oauth2_authorization_code</code> or <code>oauth2_resource_owner_password</code>.</td></tr></tbody></table>

## Object hint

Defines the field in the OpenAPI document the connector should use to display object hints.

The [default implementation](#default-object_hint_field) allows the user to select between the `summary` and `description` fields.

Consider the following object from a sample OpenAPI document:

- If `summary`, **Update an existing pet** would be used as the object hint
- If `description`, **Update an existing pet by Id** would be used as the object hint

```json
{
   "paths":{
      "/pet":{
         "put":{
            "tags":[
               "pet"
            ],
            "summary":"Update an existing pet",
            "description":"Update an existing pet by Id",
            "operationId":"updatePet",
            "requestBody":{
               "description":"Update an existent pet in the store",
               "content":{ ... },
               "required":true
            }
         }
      }
   }
}
```

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#object-hints-links) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Object hint</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.object_hint_field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Object hint substitutions

Defines a list of substitutions for object hints. Useful for modifying object hint field values and improving the object picker user experience.

Substitution objects include the following properties:

- `pattern`: A regular expression string, optionally including capture groups.
- `replacement`: The string value to replace all occurrences of `pattern`. This value may contain back-references to the `pattern`'s capture groups of:
  
  - The form `\d`, where `d` is a group **number**. For example: `\1`
  - Or `\k`, where `n` is a group **name**. For example: `\object`
  
  If a double-quoted string, both back-references must be preceded by an additional backslash (`\`). **Note**: Special match variables such as `$&` won't refer to the current match within the replacement.

Refer to the [Customizing OpenAPI interfaces guide](/connectors/openapi/guides/customizing-openapi-interfaces.html#object-hint-substitutions) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Object hint substitutions</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.object_hint_substitutions</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Object name

Defines the field in the OpenAPI document the connector should use to display object names.

The [default implementation](#default-object_label_field) allows the user to select between the `summary` and `operation_id` fields.

Consider the following object from a sample OpenAPI document:

- If `summary`, **Update an existing pet** would be used as the object name
- If `operation_id`, **updatePet** would be used as the object name

```json
{
   "paths":{
      "/pet":{
         "put":{
            "tags":[
               "pet"
            ],
            "summary":"Update an existing pet",
            "description":"Update an existing pet by Id",
            "operationId":"updatePet",
            "requestBody":{
               "description":"Update an existent pet in the store",
               "content":{ ... },
               "required":true
            }
         }
      }
   }
}
```

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#object-names) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Object name field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.object_label_field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Object name substitutions

Defines a list of substitutions for object names. Useful for modifying object name values and improving the object picker user experience.

Substitution objects include the following properties:

- `pattern`: A regular expression string, optionally including capture groups.
- `replacement`: The string value to replace all occurrences of `pattern`. This value may contain back-references to the `pattern`'s capture groups of:
  
  - The form `\d`, where `d` is a group **number**. For example: `\1`
  - Or `\k`, where `n` is a group **name**. For example: `\object`
  
  If a double-quoted string, both back-references must be preceded by an additional backslash (`\`). **Note**: Special match variables such as `$&` won't refer to the current match within the replacement.

Refer to the [Customizing OpenAPI interfaces guide](/connectors/openapi/guides/customizing-openapi-interfaces.html#object-hint-substitutions) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Object name substitutions</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.object_name_substitutions</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Substitutions for grouping

Defines text-based substitution rules for endpoint grouping operations. This is useful when the built-in grouping rules do not meet the specific needs of your API structure.

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#api-operation-substitutions) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Substitutions for endpoint grouping</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.substitutions_for_grouping</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Operation name field

Defines the field to use for operation names in the picklist of the [**Execute API operation** action](/en/connectors/openapi/guides/customizing-openapi-interfaces#api-operation-assignment). Defaults to [object name field](#object-label-field).

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Operation name field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.execute_operation_label_field</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Query param authorization

A list of query parameters to be added to the API requests.

Examples:  
`api_key: 1234567890   token: abc123`

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Query param authorization</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>query_params</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes, when <strong>Authentication method</strong> is set to <code>query</code></td></tr></tbody></table>

## Record ID field name

Defines the name of the field that holds an object's unique ID value.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Record ID field name</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.record_id_field_name</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Static object names

Defines the a list of user-friendly names for objects and operations.

Refer to the [Customizing OpenAPI user interfaces guide](/en/connectors/openapi/guides/customizing-openapi-interfaces#static-object-names) for more info and examples.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Static object names</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.object_label_map</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Only required if the OpenAPI document doesn't provide user-friendly names for individual API endpoints.</td></tr></tbody></table>

### Sample

```ruby
{
  ...
  "advanced" => {
    "object_label_map" => [
      {
        "operation_id" => "createPet",
        "label" => "Create a new Pet"
      },
      ...
    ]
  }
  ...
}
```

> **Object\_label\_map syntax**
> 
> You can format the `object_label_map` in the following ways:
> 
> 1. Provide an array of objects with `operation_id` and `label`. The example shown uses this syntax.
> 2. Provide an object with keys (for operation IDs) and values (display names/labels).

## Server URL

> **THIS IS A REQUIRED FIELD.**

A URL to the target host or service. Relative endpoint paths from the OpenAPI document will be appended to this URL to construct a full endpoint URL.

**Note**: If you want to hard-code this field's value - meaning end-users won't need to provide a value when setting up the connector - you'll need to provide the field in two methods:

- `adjust_connection`:
  
  ```ruby
  methods: {
      adjust_connection: lambda do |connection|
        connection.merge(
          {
            'definition_mode' => 'url',
            'definition_url' => 'https://petstore3.swagger.io/api/v3/openapi.yaml',
            'base_url' => 'https://petstore3.swagger.io/api/v3/',
            'documentation_href' => 'https://redocly.github.io/redoc/?url=https://petstore3.swagger.io/api/v3/openapi.yaml'
          }
        )
      end
    [ ... ]
  }
  ```
  
- `base_uri`:
  
  ```ruby
  base_uri: lambda do |connection|
    'https://petstore3.swagger.io/api/v3/'
  end
  ```
  

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Server URL</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>base_url</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>Yes</td></tr></tbody></table>

## Test request URL

The relative path of an API endpoint the connector will use to test the connection.

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Test endpoint path</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.test_endpoint</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

## Use HTTP method semantics for grouping

Indicates if HTTP methods should be used for [grouping API operations](/en/connectors/openapi/guides/customizing-openapi-interfaces#api-operation-assignment).

This should be enabled unless the endpoints in a Swagger file don't follow [REST guidelines](https://restfulapi.net/).

<table style="display:table;" width="100%; fixed"><tbody><tr><td style="vertical-align:top;background-color:#e4e8eb;" width="25%; fixed"><strong>UI name</strong></td><td>Use HTTP method semantics for grouping operations</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Source code name</strong></td><td>advanced.use_operation_names_for_grouping</td></tr><tr><td style="vertical-align:top;background-color:#e4e8eb;"><strong>Required?</strong></td><td>No</td></tr></tbody></table>

---
