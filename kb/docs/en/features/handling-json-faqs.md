---
url: 'https://docs.workato.com/en/features/handling-json-faqs.md'
description: >-
  Answers to common questions about handling JSON data in Workato recipes,
  including what JSON is and how Workato exposes it.
---

# Handling JSON FAQs

Get answers to frequently asked questions (FAQs) about handling JSON.

## What is JSON, and why is it important in the context of Workato?

View answer

[JSON (JavaScript Object Notation)](/en/features/handling-json#handling-json) is a data syntax used for storing and exchanging data. It is a popular and widely used format in the world of APIs. JSON is based on name/value pairs and arrays, making it highly readable and easily transmitted. In Workato, JSON is essential for handling data within recipes.

## How does Workato typically handle JSON data?

View answer

Workato exposes [JSON data](/en/features/handling-json#json-parser-by-workato) as input fields and output datapills in recipes, making JSON mostly transparent to regular users. However, you may occasionally handle raw JSON data in specific workflow automation.

## What is an example of JSON data?

View answer

The following [JSON data example](/en/connectors/json-by-workato/parse-json-action#example-usage) represents an array of contacts:

```json
[
  {
    "Name" : {
      "first_name" : "Sally",
      "last_name" : "Jones"
    },
    "Address": {
      "street" : "20450 Stevens Creek Blvd #150",
      "city" : "Cupertino",
      "st" : "CA",
      "postal": "95014"
    },
    "phone" : "4105554119"
  },
  {
    "Name" : {
      "first_name" : "Bob",
      "last_name" : "Towner"
    },
    "Address": {
      "street" : "1 Hacker Way",
      "city" : "Menlo Park",
      "st" : "CA",
      "postal": "94025"
    },
    "phone" : "8552982507"
  }
]
```

## How can I parse JSON data in Workato?

View answer

Use the [Parse JSON document action](/en/connectors/json-by-workato/parse-json-action) from JSON tools by Workato. This action extracts values from raw JSON based on a sample structure you provide.

## What are the input fields for the JSON parser in Workato?

View answer

The [Parse JSON document action input fields](/en/connectors/json-by-workato/parse-json-action#input) include the following:

- **Sample document**: A sample JSON structure that defines the expected format.
- **Document**: The actual JSON content to parse at runtime.
- **Encoding of the file content**: Set the character encoding.
- **Edit schema**: Refine or override the generated output schema.

## What can I expect as the output of the JSON parser in Workato?

View answer

Datapills are generated using the JSON format in the **Sample document** field. For example, if your JSON contains an array with objects such as `Name` and `Address`, the [output includes datapills that correspond to these objects and their properties](/en/connectors/json-by-workato/parse-json-action#output).

## Are there alternatives to the built-in JSON parser for handling JSON data?

View answer

Yes. If you frequently work with raw JSON data, we recommend that you consider more permanent solutions, such as custom connectors. [Workato offers two primary options](/en/features/handling-json#developing-custom-connectors):

- **HTTP connector:** This is a convenient way to handle raw data from APIs. You can build HTTP triggers and actions to manage JSON data.
  
- **Workato Connector SDK:** This extension of the Workato framework supports various authentication procedures and allows developers to build, maintain, and distribute connectors to integration-seekers.

---
