---
url: 'https://docs.workato.com/en/recipes/data-pills-and-mapping.md'
description: >-
  Learn how datapills work in Workato recipes as variables that map trigger and
  action output data between app fields.
---

# Datapills

Datapills are output data from a trigger or action step. They serve as variables that enable you to map business logic into recipe steps. For example, when you create a [Zendesk](/en/connectors/zendesk) organization from a [Salesforce](/en/connectors/salesforce) account, you can map datapills from the new Salesforce account trigger to fields in the Zendesk organization within your recipe actions.

Datapills appear in the **Recipe data** menu. At any specific recipe step, the **Recipe data** section holds the output from the trigger and all preceding actions.

![Recipe data menu within a recipe step](/assets/datatree-example.KH_Q7xXx.png)_Recipe data menu within a recipe step_

You can expand the **Recipe data** menu in the recipe editor.

![Expand the Recipe data menu](/assets/datatree-expanded.Bti7zQhL.png)_Expand the Recipe data menu_

## Default datapills

Every job contains a default set of datapills. You can access them by expanding the **Properties** data menu.

![Default datapills](/assets/default-datapills.DCVSQj_Z.png)_Default datapills for all Recipes_

| Datapill | Description |
| --- | --- |
| User ID | The unique identifier for the user. In a [workspace](/en/workspace), this corresponds to the [workspace ID](/en/workspace#workspace). |
| User name | The name of the workspace or workspace owner. In the **Development** environment, this corresponds to the workspace name or workspace owner's name. In the **Test** and **Production** environments, this name is `Environment Test` or `Environment Production`, respectively. |
| User email | The email address of the user. In a [workspace](/en/workspace), this corresponds to the [workspace email](/en/workspace#workspace). |
| Recipe ID | The unique identifier for the recipe. |
| Root recipe ID | The originating recipe ID that first triggered the job, if applicable. The Root recipe ID represents the earliest non-function recipe in the call chain if you use nested function calls. |
| Recipe URL | A URL link to the recipe. |
| Recipe name | The name of the recipe. |
| Recipe path | The directory path where the recipe is stored. |
| Job ID | The unique identifier for the job. |
| Root job ID | The originating job ID that first triggered the job, if applicable. The Root job ID represents the earliest non-function recipe job in the call chain if you use nested function calls. |
| Job URL | A URL link to the job report. |
| Job created at | The date and time when the job was created. |
| Master job ID | The initial job ID if the job is repeated. This is the current job ID for first-time jobs. |
| Calling recipe ID | The ID of the recipe that triggered this job, if applicable. |
| Calling job ID | The ID of the job that triggered this job, if applicable. |
| Is repeat | Indicates whether the job is a repeated job. |
| Is test | Indicates whether the job is a test job. |
| Repeat count | The number of times the job has been repeated. |
| Repeated job? _deprecated_ | **This field is deprecated**. Use **Is repeat** instead. Indicates whether the job is repeated. |
| Parent job ID _deprecated_ | **This field is deprecated**. Use **Master job ID** instead. The initial job ID if the job is repeated. |

## On error datapills

When you add a [handle errors step](/en/recipes/steps#handle-errors-step) to your recipe, Workato generates the following error-related datapills if an error occurs. This enables you to configure your recipe to handle recipe errors differently depending on the error type, message, source (recipe step, action, or app), and more.

Learn more about [error handling best practices](/en/recipes/best-practices-error-handling#error-handling-best-practices).

> **ON ERROR DATAPILL API NAME VARIATIONS**
> 
> On error datapill API names can vary by app and service. It's important to inspect the actual error payload to determine the cause of the datapill error.

| Datapill | Description | API names |
| --- | --- | --- |
| Error type | The type of error that occurred. | `error[type]`, `error[error_type]` |
| Error message | A message describing the error. | `error[message]`, `error[error_message]`, `error[msg]` |
| Retry count | The number of times Workato tried to rerun the actions in the **handle errors** block. | `error[retry_count]`, `error[retries]` |
| Error UUID | The Universally Unique Identifier (UUID) of the error. This is a 128-bit label used to identify the error. This key is optional and only displays a value if you provide the key. | `error[uuid]`, `error[error_id]` |
| Errored step number | The step on which the error occurred. | `error[line_number]`, `error[step_number]`, `error[step]` |
| Errored app | The app that caused the error. | `error[adapter]`, `error[app]`, `error[application]` |
| Errored action | The action on which the error occurred. | `error[action]`, `error[action_name]`, `error[operation]` |
| Inner message | Unprocessed error message that may include a response from the third-party service or details returned directly from the client. The format and content may change without notice. | `error[inner_message]` |

## Data types

Video guide: Data tree, data mapping, and data types

[Video](https://www.youtube.com/embed/OXv-qVdGKl0)

Datapills can be of the following data types:

- String
- Integer or number
- Date or datetime
- List
- Object
- Boolean

When mapping datapills, ensure they are type-compatible to avoid issues. Workato performs default type conversions when possible, provided there is no ambiguity or loss of information.

You can also transform data by opening the recipe steps in [formula mode](/en/formulas/formula-mode). This enables you to perform more advanced data manipulation.

### Root-level datapills

Root-level datapills are available for all triggers and actions. You can access them after selecting formula mode in a recipe step input field.

![Expand data menu](/assets/trigger-output-pill.C-aQLwrT.png)_Trigger output datapill_

These datapills provide the complete output schema of a trigger or action. You can use them with formulas such as [`.to_json`](/en/formulas/array-list-formulas#to-json) for formatting or with [`.pluck`](/en/formulas/array-list-formulas#pluck) to extract specific data or keys.

### Type conversions

You can convert specific data types using [formulas](/en/formulas). For example, you can convert a text string of numbers into an integer for arithmetic operations or transform a datetime expressed as a string into a proper datetime type.

Commonly used type conversion formulas include the following:

- [`to_currency`](/en/formulas/number-formulas#to-currency)
- [`to_date`](/en/formulas/date-formulas#to-date)
- [`to_f`](/en/formulas/number-formulas#to-f)
- [`to_i`](/en/formulas/number-formulas#to-i)
- [`to_s`](/en/formulas/number-formulas#to-s)
- [`to_time`](/en/formulas/date-formulas#to-time)

Use the formula editor to explore the other type conversions.

![Finding type conversions in formula mode](/assets/type-conversions-in-formula.BaJjJVF6.png)_Finding type conversions in formula mode_

## Preview data

Workato displays sample data retrieved from your account alongside datapills to help you better understand the data in your app.

Sample data appears in _italic type_ next to the datapills:

![Output data menu](/assets/output-datatree.HB1YHzMj.png)_Output data menu for New Salesforce account trigger_

## Fields mapping

Fields mapping is the assignment of datapills (variables) or absolute values (constants) into action or trigger input fields. This controls the flow of data between apps.

By mapping fields from a Salesforce account (from a trigger) to a Zendesk [Create organization action](/en/connectors/zendesk/create-organization-action), you can ensure that the Zendesk organization and Salesforce account have the same data.

In each recipe step, you can access datapills from all previous steps to configure the input fields of the current step.

### Example

In the following example, we map the Account Name datapill from the Salesforce [New account trigger](/en/connectors/salesforce/real-time-triggers#new-new-updated-object-real-time) into the **Message** input field in the [Send email action](/en/connectors/email-by-workato#send-email-action).

![Mapping the account name datapill into the message input field](/assets/mapping.Defz-tdt.png)_Mapping the Account name datapill into the message input field_

## Mapping constants versus mapping variables

Workato input fields accept variables (datapills) or constants (fixed values).

### Mapping variables

In this example, the variable Account Name (Step 1) is mapped to the **Name** input field. This means that for each new Salesforce account created, the account name is used as the organization name in Zendesk. For example, if a new Salesforce account named `Sattei Winery` is created, the recipe creates a Zendesk organization with the same name.

![Input field with variable mapping](/assets/input-field-with-variable.BnHcfkM1.png)_Input field with variable mapping_

### Mapping constants

In this example, the **Notes** input field has a constant value mapped to it: `Synced over from Salesforce`. This means that every Zendesk organization created through Workato has this text in its **Notes** field.

![Input field with constant mapping](/assets/input-field-with-constant.CJ84o0fR.png)_Input field with constant mapping_

The result is a new Zendesk organization created using both variable and constant mapping:

![Newly created Zendesk organization](/assets/zendesk-organization.CAvxEpwK.png)_Newly created Zendesk organization Sattei Winery_

### Mapping both constants and variables

You can also combine constants and variables in input fields to customize the data as needed.

#### Example

This example recipe sends a welcome email to each Salesforce lead who has signed up for a mailing list.

![Recipe will send a welcome email to each new Salesforce lead](/assets/salesforce-lead-welcome-email-recipe.DFxpR-Ep.png)_Recipe that sends a welcome email to new Salesforce leads. [Example recipe](https://www.workato.com/recipes/504766)_

In the [Send email action](/en/connectors/email-by-workato#send-email-action), datapills from the **New Salesforce lead** action **Recipe data** menu are mapped into the input fields.

![Datapill mapping](/assets/datapills-example.BZh4dR5Q.png)_Example of datapills being mapped into an action step_

Because datapills are variables, their value depends on a specific trigger event or action. In this example, the value assigned in the **To** input field depends on the value of `Email` in each new lead.

The recipe reads the `First name` (`Betty`) and `Email` (`betty@example.com`) from the new lead and sends the following email:

```text
To: betty@example.com

Hi Betty,

Thanks for joining our mailing list! We're excited to have you!
```

## Mapping fields not defined as datapills in step output

Some scenarios can require you to access a field that isn't directly available as a datapill in the step's output.

### Example

Consider a recipe using the [Webhooks connector](/en/connectors/workato-webhooks), triggered by an HTTP webhook that accepts **Query params** `A` and `B`.

In this recipe, a [Logger by Workato](/en/features/logging-service#logger-by-workato) action logs a message. You plan to map parameter `C` to the **Message** field, but `C` doesn't appear as a datapill in the **Recipe data** menu. This happens when a parameter is included in the step output payload but isn't defined in the webhook schema.

![Mapping hidden datapills](/assets/mapping-hidden-datapills.gIaW7m2x.png)_Mapping hidden datapills_

Follow these steps to access fields from the step output payload that aren't shown in the **Recipe data** menu:

1. Identify the field you plan to map that isn't shown in the **Recipe data** menu. For example, parameter `C`.
   
2. Map the parent object datapill to the input field where you plan to map the parameter. For example: Params (Step 2).
   
3. Append the specific field name in [square brackets](/en/formulas/other-formulas#square-brackets) to the parent object datapill. For example, use Params (Step 2)`['C']` to access parameter `C`.
   
   ![Append the specific field name in brackets](/assets/append-field-name-brackets.CYHbHXGj.png)_Append the specific field name in brackets_
   

## Data transformation

Sometimes the data fields from one app don't directly map into a data field for a different app. For example:

- Your sales app stores names in a single field **Full name**, but your marketing app uses two fields **First name** and **Last name**
- Your e-commerce app stores addresses as the individual fields **Address line 1**, **Address line 2**, **City**, **State**, but your accounting app only accepts a single **Billing address** field
- The priority levels in your ticketing app are stored as **Low**, **Medium**, and **High**, but in your sales system they are **Low**, **Normal**, and **Urgent**

In such cases, you can take advantage of Workato's data transformation capabilities by using [formulas](/en/formulas).

## Common issues when mapping fields

Common errors you can encounter during fields mapping include the following:

### Required fields that have no values at run-time

At design-time (when building the recipe), you must map all required fields. If a required field is left empty, the recipe does not start and throws an error.

However, even if an input field is mapped at design-time, it might not have a value at run-time (when a trigger event occurs and a job is processed). If a required field does not have a value at run-time, the job throws an error and fails.

You must decide on an appropriate response to handle such scenarios. If the missing value represents a business logic error that requires resolution, you might let the job fail and flag the issue for further action. For example, if a recipe attempts to move a new lead from a sales app but finds that the **Email address** is empty, the recipe should address this according to your business logic.

### Datapills from the wrong data menu

When mapping input fields using datapills, you can encounter datapills with identical names in the **Recipe data** menu, for example, Email in Salesforce and Email in Zendesk. Verify that you are mapping the correct datapills from the relevant steps to avoid confusion and ensure accurate data handling.

### Datapills from the wrong part of the recipe

If your recipe includes conditional steps, each job can have unprocessed steps. Consequently, the values in the **Recipe data** menu for these steps are likely blank.

When using datapills from these steps, be aware that they can be null.

---
