---
url: 'https://docs.workato.com/en/features/handling-soap.md'
description: >-
  Learn how to parse and create SOAP messages in Workato recipes. SOAP tools by
  Workato is deprecated; migrate to Message Templates and XML tools.
---

# Handling SOAP

Simple Object Access Protocol (SOAP) is a messaging protocol for communication over the internet. SOAP messages follow a standardized protocol on how it structures the body message. This allows SOAP to develop security, authorization, and error-handling standards that work across web systems.

SOAP acts as a specification on how XML messages are structured and is therefore encoded in XML. Similar to [handling raw XML content](/en/features/handling-xml), convert SOAP content into usable datapills with the built-in parser.

> **SOAP TOOLS BY WORKATO DEPRECATION NOTICE**
> 
> Workato is deprecating SOAP tools by Workato. Although we continue to provide runtime support for active recipes using this connector, creating new recipes with it is no longer possible. Additionally, we will no longer fix bugs or enhance this connector in the future. We recommend transitioning recipes that use this connector to Message Templates and XML Tools by Workato for enhanced XML communication and processing. You can use Message Templates to create diverse message formats with [Mustache](https://mustache.github.io/mustache.5.html) and leverage XML Tools to directly process and handle your XML data. This transition may require updating your workflows. For guidance and support, refer to our [Message Templates](/en/features/message-template) and [XML Tools](/en/features/handling-xml) by Workato documentation.

## SOAP tools by Workato

**SOAP tools by Workato** is a native application that does not require any connection setup.

Select **App** > **SOAP tools by Workato** to get started.

![Parse SOAP message](/assets/parse-soap-message.BCn_30u9.png)_Parse SOAP message_

| Input field | Description |
| --- | --- |
| Sample document | A sample SOAP/XML that has the same format as the SOAP document to be parsed. |
| Document | The input SOAP content to be parsed. |

Datapills are generated according to the **sample document** provided in the input. It includes all SOAP tags and all attributes associated with each tag.

![Datatree output for parse SOAP message](/assets/parse-soap-message-datatree.DaLNI4Zw.png)_Datatree output for parse SOAP message_

## Create SOAP message

**SOAP tools by Workato** also allows you to create SOAP messages. Use the **Create SOAP message** action to return a SOAP message. It will take in datapills as `tags` and generate a SOAP document.

For example, we can create a SOAP/XML document that contains a list of employee names, roles, and department details.

![Create SOAP message](/assets/create-soap-message.BYlK6Uvy.png)_Create SOAP message_

| Input field | Description |
| --- | --- |
| Message template | Select a message template. To learn how to set up a new SOAP message template, see [below](#setup-message-template). |
| Template input | The inputs required as defined in the message. |

### Output

The output of this action is a file data object, encoded in SOAP/XML. You can upload this directly to your target web system.

### Setup message template

To effectively draft a SOAP/XML message, you first have to set up the SOAP/XML schema in Message templates. Refer to [Message templates](/en/features/message-template) for more information.

Set up a message template for your use case. Define the schema of the output SOAP document and use `{tags}` to indicate where datapills are being used.

![SOAP message template for employee list](/assets/soap-message-template.m2fgN34P.png)_SOAP message template for employee list_

---
