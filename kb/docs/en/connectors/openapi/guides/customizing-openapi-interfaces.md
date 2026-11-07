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
