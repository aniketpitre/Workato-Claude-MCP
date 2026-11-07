---
url: 'https://docs.workato.com/en/connectors/javascript.md'
description: >-
  The JavaScript connector is a utility connector that lets you run custom
  JavaScript code in a recipe to transform data or invoke external services.
---

# JavaScript

JavaScript is a popular language for web development. The Workato JavaScript connector enables you to write custom JavaScript code as part of the recipe. You can take advantage of the power of JavaScript language to accomplish things like data transformation or invoke external services.

## JavaScript runtime

The Workato JavaScript connector runs on Node.js version 20.11.0. All JavaScript libraries included in the Node.js version 20.11.0 are available in the JavaScript action. Additionally, the following libraries are included:

- [node\_fetch](https://github.com/node-fetch/node-fetch)
- [lodash](https://lodash.com/)
- [gRPC](https://www.npmjs.com/package/@grpc/grpc-js)
- [Google Protobuf](https://github.com/protocolbuffers/protobuf-javascript)

## Quotas

The JavaScript connector has the following quotas:

| Description | Quota | Notes |
| --- | --- | --- |
| Memory quota for JavaScript connector actions, including libraries, temporary memory, and inputs | 256 MB | NA |
| Maximum code field size for JavaScript connector actions | 1 MB | NA |
| Timeout for JavaScript connector actions | 30 seconds | NA |
| Read request timeout for JavaScript evaluation in actions | 30 seconds | This quota applies to the following action: **Invoke custom JavaScript code** action |

Additionally, user-provided libraries are not supported.

## Working with the JavaScript connector

### Input

The first step in configuring the action is to define the input fields in the action. In the `Input fields` section, select `Add field` to add a new field. Repeat these steps for all the input fields you want to pass to your JavaScript code. Map the values to these input fields from previous steps in the recipe.

![Input fields](/assets/add-input-field.DyRXgbcT.png)_Add input field_

#### Date input field

Input field of type `Date` is passed as `String` to the JavaScript code. It is recommended to consume such date input as follows:

```js
exports.main = ({when}) => {
  const whenDate = new Date(when);
  // use whenDate
};
```

### Output

When working with JavaScript execute action, you must define the output schema for the JavaScript being called. This output schema is used to build the [output datatree](/en/workato-concepts#datatree-and-datapills). This datatree allows you to use the data returned from the JavaScript function in subsequent recipe actions.

To define the output schema, provide a sample response to generate the schema. The schema defines the data type and structure of the output. There are 2 ways to configure the output schema:

- Use a sample JSON
- Manually define schema by adding fields

### Use JSON

![Use JSON](/assets/output-fields-empty.B-wqn0hy.png)_Sample JSON for schema generation_

Let's define the output schema via sample JSON. Click the `Use JSON` button to bring up the schema generation wizard.

![JSON Sample](/assets/json-sample-schema.DW29K7iA.png)_Sample JSON for schema generation_

Paste the JSON sample in the window and click Next. Review the JSON sample and select Generate Schema. You should now see the output datatree in the `Output fields`.

![JSON datatree](/assets/output-fields-datatree.CAIoMTS-.png)_Output datatree generated from sample JSON_

This datatree can be used in subsequent actions to consume the output from your JavaScript code.

### Define schema manually

Alternatively, you can define the schema by adding fields manually. Following data types are supported for the fields:

- String
- Number
- Integer
- Date
- Time
- Boolean

Select `add fields manually` to add a field. Provide the field name, select data type and whether its optional or not then click `Add field`. ![Add output field manually](/assets/add-output-field.CkQXxTqI.png)_Add output field manually_

Repeat the steps to as many fields as returned by the JavaScript code.

### The main function

JavaScript connector requires your code to be in the `exports.main` function. By default, the sample code snippet is displayed in the code editor. ![exports.main](/assets/template-code.DnVJg66I.png)_Template code with exports.main function_

The code must follow the CommonJS format and export the `main` function.

Example code below takes in the `data` as input, transforms the data and returns the output.

```js
const fetch = require('node-fetch');

exports.main = ({data}) => {
  const converter = new DataConverter();
  return converter.convert(data);
};
```

### Error stacktrace

When the "Execute JavaScript code" action fails due to an error inside the `exports.main` function, Workato displays the relevant error stacktrace to help you debug your code.

![Error stacktrace](/assets/js-error-stacktrace.Dc01Rmiy.png)_Sample error stacktrace_

#### Logging

To help with development and debugging, Workato supports logging intermediate values using `console.log` statements. Note that Workato only displays `console.log` statements inside the `exports.main` function. Each `console.log` statement is displayed as a new line.

![console.log](/assets/console-log-functionality.DjfEWo28.png)_Output of console.log statements inside exports.main function_

### Consuming gRPC services

[gRPC](https://grpc.io/) is an open-source RPC framework. gRPC is used as a high-performance framework to implement client and server applications. The Workato JavaScript connector can be used to consume gRPC based services. This section describes the steps to implement the client code in JavaScript to invoke gRPC services. By default, gRPC uses [Protocol Buffers](https://developers.google.com/protocol-buffers/docs/overview), Google’s mature open-source mechanism for serializing structured data.

The architecture for a typical gRPC service and JavaScript client in a Workato recipe looks like as follows.

![Workato recipe and gRPC service](/assets/gRPC-architecture.D_AKg-Vi.png)_Architecture of Workato recipe and gRPC service_

Before we describe the steps to invoke gRPC service, a word about the [_proto_ file](https://grpc.io/docs/what-is-grpc/introduction/):

> **PROTOCOL BUFFERS**
> 
> The first step when working with Protocol Buffers is to define the data structure in a `.proto` file. You can create a `.proto` file by adding the `.proto` extension to a plain text file. In Protocol Buffers, data is organized into messages, which are logical records containing a series of name-value pairs called fields.

#### Tools used

Install the `grpc-tools`, `@grpc/grpc-js`, `google-protobuf` and `browserify` packages.

```shell
npm i -g grpc-tools
```

```shell
npm i @grpc/grpc-js
```

```shell
npm i -g google-protobuf
```

```shell
npm i -g browserify
```

- [grpc-tools](https://github.com/grpc/grpc-node/tree/master/packages/grpc-tools), [npm grpc-tools](https://www.npmjs.com/package/grpc-tools)
- [npm @grpc/grpc-js](https://www.npmjs.com/package/@grpc/grpc-js)
- [npm google-protobuf](https://www.npmjs.com/package/google-protobuf)
- [browserify](https://github.com/browserify/browserify), [npm browserify](https://www.npmjs.com/package/browserify)

Follow the steps outlined below to generate the relevant stub code that must be copied and pasted in the JavaScript connector code editor.

- Get the gRPC interface definition files (proto files) for the service you want to invoke
- Convert the proto file to JavaScript stubs using `grpc-tools`. The example below generates the gRPC stub for the `contacts.proto` service definition.

```shell
grpc_tools_node_protoc --js_out=import_style=commonjs,binary:. --grpc_out=generate_package_definition:. <your proto file.proto>
```

- Package and minify the generated code using `browserify`

```shell
browserify . --external @grpc/grpc-js --external google-protobuf -o <your bundle name.js> --node --im -s <your client code.js>
```

Replace the command with the bundle name and the client code JavaScript file names in the browserify command.

- Copy and paste the minified gRPC stubs to JavaScript action code editor
- JavaScript connector requires your code to be in the `exports.main` function. By default, the sample code snippet is displayed in the code editor.
- Use the generated client stub in your JavaScript code inside the `main` function.

> **WORKAROUND COMPATIBILITY**
> 
> This workaround is guaranteed to work for the specific use case of consuming gRPC services only. While it may appear to function with other libraries that are compatible with Browserify, Workato does not guarantee its effectiveness outside the documented scenario.

---
