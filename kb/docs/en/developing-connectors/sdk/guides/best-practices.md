---
url: 'https://docs.workato.com/en/developing-connectors/sdk/guides/best-practices.md'
description: >-
  Best practices for building custom connectors on the Workato SDK, covering
  code, security, authentication, actions, triggers, and testing.
---

# SDK Development Best Practices

Refer to the following list of best practices which makes development of your custom connector easier to build, test, and maintain:

- [General best practices](#general)
- [Security best practices](#security)
- [Root key-specific best practices](#root-key-specific)
- [Action best practices](#actions)
- [Trigger best practices](#triggers)
- [Usability and testing best practices](#usability-and-testing)

> **SUMMARY**
> 
> - Keep code clean and understandable, and be expressive in naming.
> - Use secure authentication and user-friendly fields, and don't include sensitive data in code.
> - Use minimal, low-privilege endpoints for tests.
> - Prefer dynamic object definitions over static, include user-friendly labels, and use `control_type` judiciously.

* * *

## General

These best practices relate directly to the development of a custom connector on Workato's SDK platform.

- The connector should be named after the application. This makes it easier for you or collaborators in your workspace to search for your own custom connector
  
  - If a standard/global connector already exists, the SDK should be named `<app name> (Custom)`, which indicates it’s custom SDK connector
- Provide trigger and action level hints when building actions. This allows users who aren't familiar with your connector understand which action to choose
  
- Avoid leaving unused variables, methods, pick lists and object\_definitions inside your connector code
  
- Keep the code clean, easy to read, understand, and extensible
  
  - Follow the DRY principle of Ruby, use methods and object\_definitions for reusable code liberally
- Always be expressive when declaring named objects or methods
  
  - Use the snake case naming convention for declaring actions, triggers, pick lists, methods, and variables
  - Do not use short codes, special chars for declaring variables
  - Users should be able to understand what each block of code is trying to accomplish based on its name
  - Include comments before Actions and Triggers, indicate what it does and any special instructions and limitations
- Include empty lines between each key (methods, actions, triggers, pick lists etc.). This makes your code more readable for those looking to improve upon it
  
- Use the `dig` method when you need to navigate data to two or more levels. [Learn more](https://ruby-doc.org/core-2.3.0/Hash.html#method-i-dig)
  
- Use `#{}` instead of string concatenation (`"string" + "string"`) whenever possible
  
  - `#{}` is more defensive as errors are not raised when the variable is not declared
- Use Date fields and format cautiously, ensure the time zones are handled
  
- Avoid puts inside the code except for when testing and debugging using the **Console** section of the **Recent tests** tab
  
- Avoid implementing triggers(strictly) and actions for endpoints with HTTP Rate limits
  
  - If the action is required, then handle rate limit logic on the recipe but not in the connector code
- Each Trigger and Action should have a description tag with appropriate action or trigger name
  
  - Standard convention: `<action/trigger> <object> in <applicationName>`
  - Example: Search invoices in Xero

* * *

## Security

- Perform validations in the `execute` lambda that are necessary to safeguard your end user's target application. Expect that users may map data from applications such as Slack, Teams, or external forms and there may be attempts to perform injection or path traversal attacks.
  - If you control the application, ensure that the applications you work with handle these inputs by sanitizing inputs received from API requests. API providers should understand more deeply the situations where specific inputs are sensitive to malicious user input.
  - On the Workato end, ensure you make additional attempts to prevent malicious input by validating inputs.
  - Advise your end users to avoid providing free-form user input into sensitive fields. For example, specifying drop-downs of enumerated values where possible.

* * *

## Root Key-specific

- [Connection](#root-key-connection)
- [Test](#root-key-test)
- [Object definitions](#root-key-object-definitions)

### Connection

- Use control\_type: password for sensitive data
  
- For OAuth 2.0 connections that allow you to request for scopes in the authorization URL, this should be an input that users of your connector can select when creating a connection.
  
- Use control\_type: subdomain and url when requesting user input about a subdomain parameter
  
  - This makes your input fields more usable to end users and minimizes the amount of human error possible
  - Example:
    
    ```ruby
    fields: lambda do |_connection, _config_fields|
      {
          name: 'sub_domain',
          control_type: 'subdomain',
          url: '.salesforce.com',
          optional: false,
          hint: 'Provide salesforce sub-domain for example, <code>test_instance</code>'
      }
    end
    ```
    
- If the connector is intended for distribution, ensure that no sensitive details are kept inside the code
  
  - This is especially important for Client IDs and Secrets when authenticating through an OAuth 2.0 flow
- Define refresh\_token and detect\_on keys for authorization tokens that expires over time. While your initial connection may be successful, your connection may break when the token expires
  
- Provide reference links to aid users into how to attain credentials to create a successful connection
  
  - A simple thing like adding a link to the URL that lets you generate API keys or client IDs and secrets are go a long way for users of your custom connector.
- Ensure required scopes are included in the authorization URL for OAuth 2.0 authentication
  
- When using `type: "custom_auth"`, the `acquire` key is only run if the `detect_on` or `refresh_on` is triggered. When using the `acquire` key to retrieve credentials like tokens, be sure to include the error code that is returned when your `test` key is executed without retrieving the proper tokens.
  
- Include version of the API if the app supports multiple versions at the same time
  
- Store the API url in connection hash
  
  - If the base url is dynamic and tenant specific, use acquire key to fetch the base\_url dynamically
- Use picklists to select production, sandbox environments if the SDK need to support different environments
  
- Use picklists in the `fields` key in the `connection` key to avoid typos, which leads to connection failures
  
- Use base\_uri(when applicable) to set the base url for API calls, which avoids keeping the full URL in triggers, methods, and picklists
  
  - Example:
  
  ```ruby
  base_uri: lambda do |connection|
    if connection['custom_domain']
      "https://#{connection['custom_domain']}"
    else
      'https://go.trackvia.com'
    end
  end
  ```
  
- Use the static base\_uri or acquire the base\_url from the endpoint (if there is an API which returns base\_url account specific)
  

### Test

- Use endpoint with least privileges and minimum data in the response for testing the connection.
  
  - For example, use endpoint “get(/profile/me”), which may hold min. data in the memory.
- Minimize the get method to store least possible data on the test endpoint call.
  
  - This reduces the amount of time to successfully create a connection
  - Validate connection status before a recipe is started

### Object Definitions

- Dynamic object definitions should be preferred over static object definitions
  
  - Dynamic object definitions reduce the amount of maintenance of the custom connector - especially when users can create custom fields in the application which you want to connect to
  - Dynamic object definitions normally depend on sending HTTP requests to metadata endpoints of the App you hope to connect to. Use the response to transform the data into the format expected in the `input_fields` and `output_fields` keys.
- Ensure that your object definitions are always defined with arguments, even if they are not used. This prevents any backwards compatibility issues in the future.
  
- Special characters are not allowed in object field names except underscore `_`
  
- Use labels to increase the usability for custom connector end users
  
  - For example, some APIs provide metadata endpoints whose responses come with suitable labels for fields. For example, metadata about fields in an target application may contain an `ID` field as well as a `name` field. This may require us to map `name` in our object definitions to `ID` and `label` in our object definitions to `name` to maximize usability for end users.
- Use `control_type` judiciously to reduce user error
  
  - For example, use `control_type` = `date_time` instead of `text` when looking to collect date time input
- Toggle fields should be used for `boolean`, `select`, `multi-select` control\_types to allow users to toggle to `text` input to map datapills during recipe design time
  
- When Toggle option is provided, toggle hints should indicate allowed values.
  
  - List values on the recipe UI if only few values, otherwise link to the appropriate page to show possible values for the toggle field
- Use number type when you need double and float, currency values.
  
- Use static pick\_list values for select options if the options are static for example, Genders, Address Type, Currency types
  

* * *

## Actions

- [General](#action-general)
- [Memory management](#action-memory-management)

### General

- Actions should be clearly named
  
  - Naming conventions for actions:
    - Get - Get only one specific record by ID
    - Search - Return 0, 1, or more records based on a search query
    - List - List out all records
    - Add - Create a new record
    - Create - Create a new record
    - Update - Update an existing record
    - Upsert - Create a new record or update an existing record
- Be sure to perform validations on input\_fields whenever necessary
  
  - We always advise guarding against edge cases by performing validation
- Use `help` tag, to indicate any special instructions to the user
  
- In execute block, call target application endpoints only for the data
  
  - Metadata HTTP requests should have been executed in `object_definitions`
- Use methods as much as possible to reduce redundant code
  
- Use `after_response` block to capture response header information like cookies etc.
  
- It’s good practice to have a custom action in connector for CRUD operations, which can be used for any endpoint
  
- Actions that delete entire tables or impact object\_definitions are not advisable in Workato
  
  - These actions have lasting impacts and potentially lead to data loss
  - It is advised for these actions to be deliberate and done directly by the an admin on the application instead of through a recipe

### Memory management

- **Optimize recipe actions**
  - Remove redundant or unnecessarily heavy attributes from the action inputs, keeping only fields that are actually required.
  - Review the size of entities that are passed into the action to avoid excessive payloads.
  - Use streaming or pagination when working with large files or datasets.
    - For example, download or upload files in chunks (for example, 5–10 MB at a time) rather than reading the entire file into memory.
    - For APIs that support pagination or cursors, process pages sequentially instead of loading all records at once.

* * *

## Triggers

- [General](#trigger-general)
- [Consecutive polling](#consecutive-polling)
- [Memory management](#trigger-memory-management)
- [Sample output](#trigger-sample-output)
- [Error handling](#trigger-error-handling)

### General

- Name of the trigger should be specific to what it does
  
- For example, New employee in Replicon - Triggers when new employee created in Replicon
  
- Naming conventions for Triggers:
  
  - New - Trigger that detects when objects are created
  - New or updated - Trigger that detects when objects are either created or updated
  - Deleted - Trigger that detects when objects are deleted
- `Since` input fields are often useful for users to retrieve data from the past
  
  - This could be an optional field to allow users the ability to pull records from a past date when first starting the recipe
  - Traditionally, APIs should support this by allowing you to query records since a past date using a set parameter
- Avoid making unnecessary API requests in the poll key as this key is executed at least once in each trigger poll
  
- Use closure key to store query fields, page number, last modified date time (only if required)
  
  - Information cached in closure is persisted across poll intervals.
- Use methods as much as possible to reduce redundant code
  
- Dynamic webhooks should be used in APIs that have functionality for programmatically setting up and tearing down of webhook URLs
  
  - Static webhooks are the alternative but require you to manually register Workato's given static URL

### Consecutive polling

When polling, triggers can poll consecutively to retrieve valid results. The `can_poll_more` boolean attribute in the SDK’s trigger poll lambda response controls this behavior. When set to `true`, the trigger initiates an immediate poll. Workato enforces a quota on the maximum number of consecutive polls in a single poll cycle when no jobs are produced. Refer to the [Consecutive polls in a single poll cycle without jobs](/en/developing-connectors/sdk/guides/trigger-limit#consecutive-polls-in-a-single-poll-cycle-without-jobs) section for more information.

Adhere to the following best practices to configure `can_poll_more` effectively and ensure compliance with polling quotas:

#### Set `can_poll_more` to `true` only when additional pages remain for polling

Set the `can_poll_more` flag to `true` only when additional pages of data are available to retrieve. This prevents unnecessary API calls and avoids indefinite polling.

For example, if an API returns a paginated response and the number of records retrieved matches the page size, this may indicate more records to fetch. In such cases, set `can_poll_more` to `true`. Otherwise, set it to `false` and wait for the next polling interval.

#### Optimize event retrieval with appropriate filters

Configure triggers to retrieve only the necessary events during each poll.

For example, use filters to pull events created or updated since the last poll. Apply filters such as `last_modified` or `created_at` timestamps to avoid retrieving redundant data.

#### Leverage webhooks for real-time monitoring

For real-time monitoring, webhooks are more efficient than polling triggers. Webhooks push data to your application as events occur, reducing the need for continuous polling and minimizing load on the source system and your application.

### Memory management

- **Separate polling from heavy processing**
  
  - Keep triggers focused solely on polling for new/updated records.
  - Move memory-intensive operations like attachment downloads, large binary file processing, and repeated API calls to separate actions to prevent out-of-memory and timeout errors.
- **Optimize memory usage in triggers**
  
  - Avoid downloading all data at once without pagination.
  - Minimize unnecessary data copying or transformations within the poll method.
  - Consider polling more frequently with selective field retrieval rather than processing large datasets in a single operation.

### Sample output

- In Workato recipes, every action or trigger should have sample output data populated with output datapills under app data section
  
  - This gives users information about the data being passed to downstream systems, improving usability
- Static sample output data is preferred for the objects with fewer fields
  
  - Dynamic sample outputs can be used for objects with large amounts of fields
  - Avoid too much of data transformation and too many API calls to show sample data in the `sample_output` key
  - For download files actions, use static data in `sample_output` key
- Ensure the sample data is populated for each trigger or action(output)
  
  - This should show up as grey text next to each datapill
  - When triggers do not have any input fields, the datatree does not show up until a second action is added

### Error handling

- Signal exceptions using the raise method
  
- Catch validation errors early, instead of waiting for API to return errors.
  
- Implement Error handling when you need to handle specific error codes in the SDK and define your own response
  
- Don’t suppress exceptions, better to expose more API information than hide them
  

* * *

## Usability And Testing

- [General](#usability-general)
- [Usability rules](#usability-rules)

### General

- Check the Recipe UI for actions and triggers
  
- Ensure the action names, triggers names, labels, and help instructions clearly communicate their purpose to the end user
  
- Remember to set up some end to end tests for your custom connector by creating recipes
  
  - This is especially useful for pushing new versions of your connector to your production workspace by first testing it in recipes using your sandbox environment

### Usability Rules

Now that you’ve learned some concepts behind creating object-based actions and triggers, you should test your connector. Test its functionality not only in the Connector SDK **Test code** tab, but also when used in a recipe. When you reach this stage, you may also start to take note of certain aspects of your connector which are not as usable as you would hope. Good connectors are not only well organized in terms of code but place user experience front and center in the entire recipe building experience. Here are some rules that distinguish good connectors from those that aren't user-friendly:

1. [Descriptive help text](#descriptive-help-text)
   
2. [User-friendly input fields](#user-friendly-input-fields)
   
3. [Descriptive error messages](#descriptive-error-messages)
   

#### Descriptive Help Text

Help texts in actions are critical in helping your users plug any knowledge gaps they may have about the actions you've built. Here are some important details that you should include in the help texts of your actions:

- [Supported API versions](#supported-api-versions)
- [Object-specific help](#object-specific-help)
- [Links to documentation](#links-to-documentation)
- [Field-level hints](#field-level-hints)
- [Field-level help](#field-level-help)

##### Supported API versions

API versions of the application you are connecting to help manage expectations for your users. They would have a better understanding of what to expect in terms of functionality for your connector.

##### Object-specific help

Different objects may require different action level help hints. Help texts can be easily changed based on the object users select.

```ruby
help: lambda do |input, picklist_label|
  if input['object'] == 'invoice'
    {
      body: "Creates an invoice in XYZ. Invoices in XYZ accounting are essential " \
      "components of the platform. This action supports the creation of invoices " \
      "including custom fields",
      learn_more_url: "docs.xyz.com",
      learn_more_text: "Learn to setup this action"
    }
  else
    {
      body: "Creates an object in XYZ. First, select from a list of " \
      'objects that we currently support. After selecting your object,' \
      ' dynamic input fields specific to the object selected ' \
      'will be populated.'
    }
  end
end,
```

##### Links to documentation

Help texts can also include links to appropriate documentation if users need more information about how to set up this action.

![Help text hints](/assets/help-text-link.CTdtaqA_.png)_Linking to documentation can help your users when not all the information can be contained in a small paragraph_

##### Field-level hints

Hints are an essential way to guide your users on how to use a specific input field. Let them know about input expected such as whether you require the timestamp to be in a specific date format (iso8601 or DD/MM/YYYY) etc.

##### Field-level help

In cases where it is critical for your users to read this to configure the action properly, we suggest using field level help. This should be used sparingly.

```ruby
[
  {
    control_type: "text",
    label: "Txn date",
    type: "string",
    name: "TxnDate",
    optional: true,
    sticky: true,
    help: {
      title: "Extra info",
      text: "This field is super important"
    }
  }
]
```

![Help text hints](/assets/field-level-help.D2d_seF5.png)_Bring attention to a specific field using field level help_

#### User-Friendly Input Fields

Here are some simple rules that would help fine-tune your connector to make it as user-friendly as possible. When creating connectors with the eventual aim of getting them listed on Workato as globally scope connectors, these rules will form an important part of the UIUX review that we put each connector through.

1. Is the label of the input field descriptive enough? Be as explicit as possible when defining labels on input fields so your end users are on the same page as you. While the `name` of the field may be `id`, changing the label to `Invoice ID` makes it immediately clear to end users what they are doing.
   
2. Is the type and control\_type of the input field accurate? Types and control\_types help your users know what kind of values they are working with. Workato defaults the type and control\_type to string and text if nothing is defined.
   
3. Did you declare hints for input fields that might still be ambiguous after changing the label? Using hints are a great way to guide your users even more. Links in HTML format can also be used.
   
4. Does this input field only accept a defined set of values? Using select drop-downs make it easier for your users to give correct input instead of typing in their answers manually. This also reduces the number of errors they might face.
   
5. Does this input field accept ID values? For example, a `create invoice` action in XYZ accounting might require an input field that contains the ID of the associated customer. Since your users might not have IDs of customers on hand, but the name of the customer instead, you may consider making the input field a picklist which shows customer names as the label but provides the ID of the customer as the value instead.
   
6. When using drop-downs, always also include a toggle\_field option that allows your users to map datapills if they need to. While a drop-down is great, sometimes your users may need to map datapills instead. Remember to change the toggle\_hints accordingly.
   
7. Is this drop-down a config field? If yes, ensure that the secondary toggle field has `control_type` set to `plain-text` to prevent datapills from being mapped. Config fields shouldn't accept datapills as other input fields in the action rely on the information.
   
8. Are all required fields in the action or trigger labeled as required? Users should be able to quickly understand which fields they need to fill in for this action to be valid.
   
9. Are there any optional fields that will be commonly used? Making these fields sticky can bring end-users attention to their input fields instead of having them search for them.
   
10. Are you dynamically retrieving possible custom fields for end users of your connector? Use the `custom` parameter in each custom field to provide your users with feedback on which fields are standard and which fields are custom to them.
    

For each input field, we suggest running through this series of questions quickly. Once you get the hang of it, it becomes a simple process of highlighting input fields which need adjustments before going back into the schema definitions to make changes.

#### Descriptive Error Messages

Descriptive error messages are a crucial part of the recipe building experience for end-users. Without the proper error messages, users have a tough time figuring out why their recipes are failing. If you haven’t checked out the possible ways to surface errors on Workato, do check out our [error handling guide.](/en/developing-connectors/sdk/guides/error-handling)

Here are some general rules to include proper error handling in your connector.

1. Does your connector use picklists or dynamic schema of any sort? Chaining an `after_error_response` function allows your users to receive exact information of what may have gone wrong. [Example here.](/en/developing-connectors/sdk/guides/error-handling#handling-object-definition-errors)
   
2. Does your connector have certain fields that are required together, such as a start date and end date? Whilst these fields may not be required all the time, some fields are often required together. In cases like these, validations may help surface these errors better and also reduce the number of API calls made unnecessarily. [Example here.](/en/developing-connectors/sdk/guides/error-handling#validating-inputs)
   
3. Does the API you are connecting to respond with appropriate HTTP status codes? In certain cases, APIs may send back responses that should actually be errors but have their HTTP status as `200`. In cases like these, using an `after_error_response` function can help highlight issues to your users instead. [Example here.](/en/developing-connectors/sdk/guides/error-handling#handling-response-errors)

---

---
url: >-
  https://docs.workato.com/en/developing-connectors/sdk/guides/advanced-connector-guide/connector-building-code-patterns.md
description: >-
  Learn useful coding patterns for Workato SDK connectors, including how to
  handle special characters in field names and datapills.
---

# Connector building - Useful coding patterns

There are some known limitations to Workato's platform that have fixes in the works. In the meantime, here are some ways that you can easily solve for any limitations that you might find when building a custom connector.

## Handling special characters

One known limitation of relates closely to datapills in Workato. When input or output fields are defined with names that have these special characters, input fields don’t show up and output datapills render incorrectly.

```
-<>!@#$%^&*()+={}:;'"`~,.?
```

For example, schema defined where

```ruby
{
  name: “due-date”
}
```

Would not show up as a string input field and datapills would turn render as long strings instead of datapills.

![Broken datapill](/assets/broken-datapill.BAl9H38s.png)_When names of schema have special characters, datapills are renders incorrectly_

instead of

![Proper datapill](/assets/proper-datapill.DroiaEjz.png)_There is a need to render them properly by switching out the special characters in their names_

Fortunately, there is a workaround which we highly recommend you build into your connector as well. ( You could even copy and paste the following if it fits.) We create a series of 3 methods, `format_schema`, `format_payload`, `format_schema` which can be called at the beginning and end of each `execute` block. We had done something similar in our earlier example when defining our action.

### `format_schema`

Sample code snippet:

```ruby
format_schema: lambda do |schema|
  if schema.is_a?(Array)
    schema.map do |array_value|
      call('format_schema', array_value)
    end
  elsif schema.is_a?(Hash)
    schema.map do |key,value|
      if %w[name].include?(key.to_s)
        value = call('replace_special_characters',value.to_s)
      elsif %w[properties toggle_field].include?(key.to_s)
        value = call('format_schema', value)
      end
      { key => value }
    end.inject(:merge)
  end
end,
```

Since fields where names contain keys cause errors, we need a service method that can take invalid schema and convert any names into formats we can handle. The method above recursively searches through a given schema and replaces any special characters with a valid string. For example,

```ruby
[
  {
    control_type: "text",
    label: "Txn date",
    type: "string",
    name: "Txn-Date"
  }
]
```

Would be converted to

```ruby
[
  {
    control_type: "text",
    label: "Txn date",
    type: "string",
    name: "Txn__hyp__Date"
  }
]
```

This allows the field to be displayed in Workato with no observable difference to the end user as labels are preserved. This service method can be called on either static or dynamic schema.

### `format_payload`

Sample code snippet:

```ruby
format_payload: lambda do |payload|
  if payload.is_a?(Array)
    payload.map do |array_value|
      call('format_payload', array_value)
    end
  elsif payload.is_a?(Hash)
    payload.map do |key, value|
      key = call('inject_special_characters',key)
      if value.is_a?(Array) || value.is_a?(Hash)
        value = call('format_payload', value)
      end
      { key => value }
    end.inject(:merge)
  end
end,
```

This method should be called when input from the job is passed through the `execute` block. At this stage, this method recursively searches through the input hash and finds any markers that a special character was replaced and transforms it back to its original form. The return from this method is a formatted payload with all special characters replaced back in.

### `format_response`

Sample code snippet:

```ruby
format_response: lambda do |payload|
  if payload.is_a?(Array)
    payload.map do |array_value|
      call('format_response', array_value)
    end
  elsif payload.is_a?(Hash)
    payload.map do |key, value|
      key = call('replace_special_characters',key)
      if value.is_a?(Array) || value.is_a?(Hash)
        value = call('format_response',value)
      end
      { key => value }
    end.inject(:merge)
  end
end,
```

When working with responses, we still need to match them back to the Workato valid schema. As such, we need to transform the keys in our responses from our network traffic back to replace any special characters. This should be done immediately after we get a response back from a HTTP call.

### `replace_special_characters` and `inject_special_characters`

Samples code snippet:

```ruby
replace_special_characters: lambda do |input|
  input.gsub(/[-<>!@#$%^&*()+={}:;'"`~,.?|]/,
  '-' => '__hyp__',
  '<' => '__lt__',
  '>' => '__gt__',
  '!' => '__excl__',
  '@' => '__at__',
  '#' => '__hashtag__',
  '$' => '__dollar__',
  '%' => '__percent__',
  '^' => '__pwr__',
  '&' => '__amper__',
  '*' => '__star__',
  '(' => '__lbracket__',
  ')' => '__rbracket__',
  '+' => '__plus__',
  '=' => '__eq__',
  '{' => '__rcrbrack__',
  '}' => '__lcrbrack__',
  ';' => '__semicol__',
  '\'' => '__apost__',
  '`' => '__bckquot__',
  '~' => '__tilde__',
  ',' => '__comma__',
  '.' => '__period__',
  '?' => '__qmark__',
  '|' => '__pipe__',
  ':' => '__colon__',
  '\"' => '__quote__'
)
end,

inject_special_characters: lambda do |input|
  input.gsub(/(__hyp__|__lt__|__gt__|__excl__|__at__|__hashtag__|__dollar__|\__percent__|__pwr__|__amper__|__star__|__lbracket__|__rbracket__|__plus__|__eq__|__rcrbrack__|__lcrbrack__|__semicol__|__apost__|__bckquot__|__tilde__|__comma__|__period__|__qmark__|__pipe__|__colon__|__quote__|__slash__|__bslash__)/,
  '__hyp__' => '-',
  '__lt__' => '<',
  '__gt__' => '>',
  '__excl__' => '!',
  '__at__' => '@',
  '__hashtag__' => '#',
  '__dollar__' => '$',
  '__percent__' => '%',
  '__pwr__' => '^',
  '__amper__' => '&',
  '__star__' => '*',
  '__lbracket__' => '(',
  '__rbracket__' => ')',
  '__plus__' => '+',
  '__eq__' => '=',
  '__rcrbrack__' => '{',
  '__lcrbrack__' => '}',
  '__semicol__' => ';',
  '__apost__' => '\'',
  '__bckquot__' => '`',
  '__tilde__' => '~',
  '__comma__' => ',',
  '__period__' => '.',
  '__qmark__' => '?',
  '__pipe__' => '|',
  '__colon__' => ':',
  '__quote__' => '"'
)
end
```

## Avoid encoded query parameters

Workato's SDK automatically encodes query parameters in GET requests, which can break requests for APIs that expect exact formatting. To avoid this, build the query string manually and append it directly to the URL.

For example:

```ruby
url = "https://api.example.com/reports"
query_string = "addressVerification=true&poi[latitude]=#{input['latitude']}&poi[longitude]=#{input['longitude']}"

get("#{url}?#{query_string}")
```

This preserves the exact casing and structure required by the API. Use this pattern when the API expects raw query strings or rejects encoded characters.

## Header casing in SDK console

Case-sensitive headers may appear with incorrect casing when you test connectors in the SDK console.

This issue affects only the console interface. The SDK console formats header names for display, but Workato sends the request with the exact casing defined in your code.

For example:

```ruby
case_sensitive_headers(BPMCSRF: connection['BPMCSRF'],
                       Cookie: connection['Cookie'])
```

In the console, a header like `BPMCSRF` may display as `Bpmcsrf`, but the actual request uses the correct casing. You don't need to change your code.

## Summary

Object based actions and triggers in Connectors are something we highly recommend. Not only do they improve user experience for your users but they also make it so much easier to extend your connector when done properly. Here are a few of the main concepts we covered:

1. Defining the base schema of each object in a service method. Don’t forget to include an input argument that allows you to adjust the schema based on the action type.
2. Use object\_definitions to pull the proper input and output field schema based on the object selected
3. When defining actions or triggers, make sure to declare all blocks especially `description` blocks. This will vastly increase usability for your users.
4. Contain any general processing inside execute blocks but leverage on dedicated object execute methods (i.e. `create_invoice_execute`)for anything specific. i.e. Use `format_paylod` and `format_response` in the execute block before using the `create_#{object}_execute` method.

### Usability rules

Great connectors not only have great architecture but look and feel great to use. Read on to find out more about how you can make your connector easy to use.

---
