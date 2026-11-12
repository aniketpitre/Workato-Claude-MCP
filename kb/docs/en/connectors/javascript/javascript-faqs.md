---
url: 'https://docs.workato.com/en/connectors/javascript/javascript-faqs.md'
description: >-
  Answers to frequent questions about the Workato JavaScript connector,
  including its Node.js runtime, script size quotas, and defining input fields.
---

# JavaScript FAQs

Get answers to frequently asked questions (FAQs) about the JavaScript connector.

## What is the Workato JavaScript connector used for?

View answer

The [Workato JavaScript connector](/en/connectors/javascript#javascript) allows you to write custom JavaScript code as part of your recipes. You can use it for tasks like data transformation and invoking external services.

## What JavaScript runtime does the Workato JavaScript connector use?

View answer

The Workato JavaScript connector runs on [Node.js version 20.11.0](/en/connectors/javascript#javascript-runtime). It includes all JavaScript libraries available in Node.js version 20.11.0, as well as additional libraries such as:

- node\_fetch
- lodash
- gRPC
- Google Protobuf

## Is there a limit to the size of JavaScript scripts in the connector?

View answer

Yes. The JavaScript action limits script size and has the following quotas:

| Description | Quota | Notes |
| --- | --- | --- |
| Memory quota for JavaScript connector actions, including libraries, temporary memory, and inputs | 256 MB | NA |
| Maximum code field size for JavaScript connector actions | 1 MB | NA |
| Timeout for JavaScript connector actions | 30 seconds | NA |
| Read request timeout for JavaScript evaluation in actions | 30 seconds | This quota applies to the following action: **Invoke custom JavaScript code** action |

## How do I define input fields in the Workato JavaScript connector?

View answer

Locate the [Input fields](/en/connectors/javascript#input-fields) section and select **Add field** to define input fields for your JavaScript code. You can map values to these input fields from previous steps in your recipe.

## How are Date input fields passed to the JavaScript code?

View answer

[Date input fields](/en/connectors/javascript#date-input-field) with the Date type are passed as strings to the JavaScript code. We recommend consuming date input by converting it to Date objects within your code.

## How do I define the output schema for the JavaScript code being called?

View answer

To define the [output schema](/en/connectors/javascript#output-fields), you can use one of two methods:

- Use a sample JSON for schema generation.
- Manually define the schema by adding fields, specifying data types, and determining which of these are optional.

## What format should my JavaScript code follow in the exports.main function?

View answer

The JavaScript connector requires your code to be within the [`exports.main` function](/en/connectors/javascript#the-main-function). Your code must follow the CommonJS format and export the main function, which takes in data as input and returns the output.

---
