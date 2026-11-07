---
url: 'https://docs.workato.com/en/connectors/ruby-snippets-by-workato.md'
description: >-
  The Ruby snippets by Workato connector enables you to write custom Ruby code
  and run it in your recipes to perform actions such as invoking external
  services.
---

# Ruby snippets by Workato

Ruby is a popular language for web development. The **Ruby snippets by Workato** connector enables you to write custom Ruby code and insert it into your recipe to execute a custom action. This allows you to use Ruby to perform actions such as invoking external services.

> **ALLOWLISTED RUBY METHODS ONLY**
> 
> Only allowlisted Ruby methods can be added to your recipe. Refer to [Available Ruby methods](/en/developing-connectors/sdk/sdk-reference/ruby_methods#available-ruby-methods) for more information.

No connection set up is required to use the **Ruby snippets by Workato** connector.

![Ruby snippets by Workato](/assets/ruby-snippets-by-workato.CKaoxzlz.png)_Ruby snippets by Workato_

## Runtime version

The Ruby snippets by Workato connector runs on Ruby 2.7.

## Required sections

| Section | Description |
| --- | --- |
| Name | Provide a descriptive name that indicates the purpose of the action. For example, `Get account details`. |
| Input | Use this section to pass data into your Ruby code. |
| Output schema | Use this section to define the data structure that your Ruby code outputs. |
| Ruby snippet source | Select **Define manually** to write the Ruby snippet directly in this action, or select **Use a resource** to use a [resource](/en/resources) as the Ruby snippet. |
| Ruby Snippet Resource | Select the resource to use as the Ruby snippet. This field appears when you select **Use a resource** in the **Ruby snippet source** drop-down menu. |
| Code | Use this section to add the Ruby code you plan to execute. This code can use the data passed in the **Input** section and must return a hash that matches the structure defined in the **Output schema** section. This field appears when you select **Define manually** in the **Ruby snippet source** drop-down menu. |

## Limitations

The Ruby snippets by Workato connector has the following quotas:

| Description | Quota | Notes |
| --- | --- | --- |
| Memory quota for Ruby connector actions, including libraries, temporary memory, and inputs | 256 MB | NA |
| Timeout for Ruby connector actions | 30 seconds | NA |
| Read request timeout for Ruby connector actions | 30 seconds | This quota applies to the following action: **Invoke custom Ruby code** action |

Additionally, user-provided libraries are not supported.

## Input

The **Input** section in your Ruby snippet allows you to pass data into the Ruby code. This can be data from a previous step in the recipe or any other data you plan to use within your Ruby code. You can access the data in the **Input** section using the `input` keyword in your Ruby code.

![Input](/assets/ruby-input.DhbjkrTO.png)_Input section_

You must define the input fields you plan to use in your action:

1. Go to the **Input** section.
   
2. Click **Add field**.
   
3. Add a **Label** to your input.
   
   ![Add field](/assets/input-add-field-ruby.BHhsuSkz.png)_Add new field_
   
4. Use the **Data type** drop-down menu to select the data type you plan to use, such as string or boolean.
   
5. Optional. Enter a description or provide additional context to help users in the **Hint** field.
   
6. Click **Add field** to add the input field to your action.
   
7. Repeat these steps for all input fields you plan to pass to your Ruby code.
   

## Output schema

The output schema defines the data structure that your Ruby code outputs. This is useful if you plan to use the output of the Ruby code in subsequent recipe steps.

You must define the output schema for the code when you use **Ruby snippets by Workato** to execute an action. The output schema builds the output datatree, allowing you to use the data returned from the Ruby function in subsequent recipe actions.

![Output schema](/assets/output-schema.Bri55fhZ.png)_Output schema_

You can configure the output schema by [using sample JSON](#use-sample-json) or by [manually defining output fields](#manually-define-output-fields).

### Manually define output fields

Complete the following steps to manually add fields to your output schema:

1. Go to the **Output schema** section.
   
2. Click **Add fields manually**.
   
   ![Add fields manually](/assets/manual-output-schema.cGqobY-P.png)_Manually define your output schema_
   
3. Enter a **Name** for your field.
   
4. Optional. Add a **Label** to your input.
   
5. Use the **Data type** drop-down menu to select the data type you plan to use, such as string or boolean.
   
6. Use the **Optional** drop-down menu to select whether the field is optional or required.
   
7. Optional. Use the **Nest under** drop-down menu to select where to nest the field.
   
8. Optional. Enter a description or provide additional context to help users in the **Hint** field.
   
9. Click **Add field** to add this field to your output schema.
   
10. Repeat these steps for all fields you plan to pass to your Ruby code.
    

### Use sample JSON

Complete the following steps to configure your output schema with sample JSON:

1. Click the **Use JSON** button to open the schema generation wizard.
   
   ![Sample JSON](/assets/json-sample.B8NLHEKj.png)_Define your output schema with sample JSON_
   
2. Paste the JSON sample you plan to use in the window and click **Next**.
   
3. Review the JSON sample and then click **Generate schema**. The output datatree appears in the **Output** fields.
   

## Code

The **Code** field is where you write the Ruby code that your recipe executes. This code can use the data from the **Input** field and must return a hash that matches the structure defined in the **Output schema** field. The keys in the returned hash must match the field names in the **Output schema**, and the corresponding values contain the data for those fields.

![Code section](/assets/ruby-code-section.BJetHEDE.png)_Add your Ruby code_

## Error stacktrace

Workato displays the relevant error stacktrace to help you debug your code when the **Execute Ruby code** action fails due to an error inside your code.

![Error stacktrace](/assets/ruby-error-stacktrace.BpTQ1ojO.png)_Sample error stacktrace_

## Logging

Workato supports logging intermediate values using `puts` statements to help with development and debugging. Each `puts` statement is displayed as a new line. Workato only displays `puts` statements in the log if a return value exists at the end of the Ruby script.

Refer to the following code example and output:

```ruby
z = 2 + 1
puts "The result of the computation is:"
puts z
{result: z}
```

**Output**

```json
{
    "Output": {
        "result": 3,
        "log": "The result of the computation is: 3."
    }
}
```

![puts](/assets/puts-functionality.Dqr-YMG2.png)_Output of `puts` statements_

---
