---
url: 'https://docs.workato.com/en/connectors/message-template-by-workato.md'
description: >-
  Message template by Workato is a utility connector that lets you create
  reusable Mustache templates to generate HTML, text, JSON, and XML messages in
  recipes.
---

# Message template by Workato

The Message template by Workato connector enables you to create and use static [Message templates](/en/features/message-template) for commonly used messages in your recipes. These templates use [Mustache](https://mustache.github.io/mustache.5.html) as the templating language. Message templates can be used to generate HTML, text, JSON, and XML messages. They also allow you to separate the message composition logic (what the message looks like) from the message generation logic (when the message is sent). This separation enables you to change the message format without changing the recipe that sends the message.

> **MESSAGE TEMPLATE ESCAPES HARMFUL ELEMENTS**
> 
> Message template escapes some potentially harmful HTML elements, such as those that could lead to XML injection.

## Create a new template

Templates define a structure for variables and body text that is consistent across runs and recipes.

Complete the following steps to create a new template:

1. Navigate to **Tools > Message templates** and click **\+ New template**.
   
2. Provide the body text of the message in the **Template body** field. Specify variables by wrapping them in double brackets (`{{}}`).  
     
   This field uses Mustache as its templating language. Refer to the [Mustache documentation](https://mustache.github.io/mustache.5.html) or the variables section of the [Message template](/en/features/message-template#variables) page for more information.
   
3. Add your variables in the **Template input**. You can use JSON or manually create your variables. Template variables support both scalar data types (string, integer, date, number, time, and boolean) and complex data types (object and list). You can define values for template variables using the **Create message** action.
   
   ![Completed Template input](/assets/template-with-object-section.p5mp7Clm.png)_Template with defined variables_
   

> **VARIABLES, SECTIONS, COMMENTS, AND PARTIALS**
> 
> Refer to the [Message template](/en/features/message-template) page for more information on using variables, sections, comments, and partials in your templates.

## Create message action

The **Create message** action defines the values to pass to a template's tags and generates a static `Document` string from the `Template body`.

> **REQUIRES AT LEAST ONE TEMPLATE**
> 
> To use the **Create message** action, your workspace must have at least one template saved. Refer to the [create a new message template](#create-a-new-template) section to learn how to create a message template.

### Input

| Input | Description |
| --- | --- |
| Document template | Select the template you plan to use. |
| Template input | Provide datapills or fixed values for your template variables to use within this recipe. |

### Output

| Output | Description |
| --- | --- |
| Document | A static string generated from the `Document template`, with values from the `Template input` field in place of the variables. |

---
