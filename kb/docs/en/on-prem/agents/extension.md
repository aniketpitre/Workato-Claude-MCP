---
url: 'https://docs.workato.com/en/on-prem/agents/extension.md'
description: >-
  Connect legacy on-prem applications to Workato recipes by registering Java
  extensions as REST endpoints in the on-prem agent.
---

# Extensions

Enterprises often have on-prem applications and databases that are deployed behind a corporate firewall.

Workato’s on-prem extensions allows you to connect to legacy applications using Java. Extensions are registered as Servlets in the Workato on-prem agent, and expose as REST endpoints which can be used from within a recipe.

When to use this:

- Application does not have REST / SOAP APIs.
- Application has a supported Java library.

When not to use this:

- Application has REST / SOAP APIs. Use the [HTTP Connector](/en/developing-connectors/http-v2) or build a custom connection with the [Connector SDK](/en/developing-connectors/sdk).
- You want to execute simple command-line scripts. Use [Command-line scripts](/en/on-prem/agents/connection/profile#command-line-scripts-profile) instead.

### Prerequisites

OPA versions lower than [23.0](/en/on-prem/agents/versions#v23-0) require you to install the [Java 17 SDK](https://adoptium.net) manually. Refer to the [On-prem agent version notes](/en/on-prem/agents/versions#v23-0) for more information.

### Example

To explain Extensions, we'll walkthrough how to create a simple extension that performs a SHA-256 message digest. This extension takes the request body and returns a SHA-256 encrypted version of it. We will then enable it as a REST endpoint so that you can use this extension in a recipe.

#### Build Extension

Download the [repository](https://github.com/workato/opa-extensions) for this extension. This is a Gradle project which will serve as a base template that you can leverage on to write your own extensions.

The source file for the on-prem extension is located in `src/main/java/com/mycompany/onprem/SecurityExtension.java`

Run `./gradlew jar` on the root folder to bootstrap Gradle and build the project. You will find the output in `build/libs/opa-extensions-0.2.jar`

#### Install Extension

To install the OPA extension, create a new directory called `ext` under the Workato agent directory and place `opa-extensions-0.2.jar` in the `ext` folder.

Update `conf/config.yml` with the classpath and newly added extension. This tells the on-prem agent where to find the jar files:

```yaml
server:
  classpath: C:\\Program Files\\Workato Agent\\ext
extensions:
  security:
    controllerClass: com.mycompany.onprem.SecurityExtension
    secret: HA63A3043AMMMM
```

Note that the `classpath` value above should be set to the appropriate location, which may differ in your environment.

If you have multiple extensions, place all jar files in the ext folder and add a new entry under extensions:

```yaml
server:
  classpath: C:\\Program Files\\Workato Agent\\ext
extensions:
  security:
    controllerClass: com.mycompany.onprem.SecurityExtension
    secret: HA63A3043AMMMM
  otherextension:
    controllerClass: com.mycompany.onprem.OtherExtension
```

The **server** parameter configuration property is as follows:

| Property name | Description |
| --- | --- |
| classpath | Specifies the location of user-defined class |

  

The **extensions** parameter configuration properties are as follows:

| Property name | Description |
| --- | --- |
| security | This is the extension profile name that will be used in the SDK. Use a unique name for each extension. |
| controllerClass | A required field to inform the OPA which Java class to map the extension to. |
| secret | Optional environment property that is used in the Java class. Multiple properties can be added. |

> **TROUBLESHOOT 520 CONNECTION FAILED ERRORS**
> 
> The agent logs a **520 Connection Failed** error when it can't start the extension. Refer to the [520 Connection Failed error troubleshooting](/en/on-prem/agents/opa-troubleshooting/troubleshoot-opa-connections#520-connection-failed-error-troubleshooting) guide to learn how to resolve it.

#### Build SDK

In order to use the extension in a recipe, we need a custom connector (SDK) in Workato. Create an custom connector in the [Connectors page](https://www.workato.com/custom_adapters) with the following code:

```ruby
{
  title: 'On-prem security',
  secure_tunnel: true,

  connection: {
    fields: [{ name: 'profile', hint: 'On-prem security connection profile' }],
    authorization: { type: 'none'},
    apply: ->() {
      headers('X-Workato-Connector': 'enforce')
    }
  },

  test: ->(connection) {
    post("http://localhost/ext/#{connection['profile']}/computeDigest", { payload: 'test' })
  },

  actions: {
    sha256_digest: {
      title: 'Create SHA-256 digest',
      description: 'Create <span class="provider">SHA-256</span> digest',

      input_fields: -> { [{ name: 'payload' }] },
      output_fields: -> { [{name: 'signature' }] },

      execute: ->(connection, input) {
        post("http://localhost/ext/#{connection['profile']}/computeDigest", input)
      }
    }
  }
}
```

Take note of the following in the SDK code:

- `secure_tunnel` is set to true which allows you to select an OPA when creating a connection. Make sure to select the OPA that has the extension.
  
- Header `X-Workato-Connector: enforce` is used to inform the OPA that this is a request to communicate with the OPA extension
  
- The path `http://localhost/ext/#{connection['profile']}/computeDigest` is defined in the Java class
  

```java
@RequestMapping(path = "/computeDigest", method = RequestMethod.POST)
```

---
