---
url: 'https://docs.workato.com/en/formulas/complex-data-types.md'
description: >-
  Learn how to use formula mode in Workato to map complex data types like
  objects and arrays, including JSON, in recipe input fields.
---

# Complex data types

APIs commonly use complex data structures, such as objects and arrays. These arrays are also referred to as lists. APIs typically organize and transmit these structures in JSON format to represent structured data.

## Mapping complex data in formula mode

Formula mode provides tools for working with complex data types within Workato's input fields.

You can use formula mode to perform the following actions when mapping complex data:

- Create arrays of primitive data types
- Access and manipulate data without needing a detailed schema
- Provide values for specific fields

## Example

The following example demonstrates how to use formula mode with complex data types. In this example, formula mode applies tags to Zendesk tickets based on associated Salesforce campaigns.

1. Enable formula mode within the `Tags` field of the Zendesk **Update ticket** action. Formula mode is required to input complex data structures. According to Zendesk's [API documentation](https://developer.zendesk.com/rest_api/docs/core/tickets#update-ticket), tags must be formatted as a JSON array of strings.
   
2. Enter sample tags in the `Tags` field and click **Test recipe** to verify that the action is set up correctly. Ensure that the tags follow the correct JSON syntax for an array of strings. Invalid values in formula mode raise [design-time formula errors](/en/recipes/design-time-errors/incorrect-formulas#incorrect-formulas).
   
   ![Update ticket tags](/assets/update-ticket-tags.BFypBIsl.png)_Tags field with sample tags_
   
3. Use the [pluck](/en/formulas/array-list-formulas#pluck) formula, which returns an object's sub-field, to retrieve `Name` values from the Salesforce `Campaigns` object and apply them as tags. This method dynamically adds tags to tickets instead of using static values.
   
   ![Dynamic array input](/assets/formula-dynamic-array-input.Dkj2iP3V.png)_Dynamic array input in formula mode_
   
4. Ensure that the correct data is sent to Zendesk by checking the job's **Output** tab.
   
   ![Dynamic tabs output](/assets/formula-array-job-details.BcJ-M4ZT.png)_The Tags array of strings is correctly inserted into the ticket._

---
