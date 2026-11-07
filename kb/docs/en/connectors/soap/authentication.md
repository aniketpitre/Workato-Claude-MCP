---
url: 'https://docs.workato.com/en/connectors/soap/authentication.md'
description: >-
  Configure SOAP connector authentication in Workato, including basic auth,
  WS-Security, API key, NTLM, custom headers, and dedicated login operations.
---

# SOAP authentication

Workato's SOAP connector supports a variety of web service [authentication types](#authentication-types), in addition to a [dedicated login operation](#login-operation). You configure authentication when you [set up the connection](/en/connectors/soap#connection-setup).

## Authentication types

| Authentication type | Description |
| --- | --- |
| None | The web service doesn't require authentication. |
| Basic authentication | The web service requires a username and password. |
| WS-Security user credentials | The web service requires a UsernameToken and password. **Send password as digest:** Select **Yes** if the web service requires the password to be sent as a digest (hash of password and timestamp). |
| Message parameters | The web service's authentication structure depends on validating authorization parameters. **Parameter name:** Case-sensitive path of the parameter in the input message. Note that root-level parts of a SOAP input message are typically objects with sub-parameters that should be concatenated with a dot, such as `parameters.username` or `parameters.password`; **Parameter value:** Value of the input parameter, such as `user1` or `password123` |
| API key | The web service requires an API key. **API key:** The value of the API key.; **Location of the API key:** Where the API key is located: in the header, cookie, or query parameters.; **Name of the API key:** The custom API key name. Default: `X-API-Key` for header, `X-API-KEY` for cookie, and `api_key` for query parameters. |
| NTLM | The web service requires authentication through NT LAN Manager. **Username:** The NTLM username without the domain to authenticate with. For example, enter `user`, not `domain\user`.; **Password:** The NTLM password.; **NTLM domain:** The domain to authenticate within.; **NTLM workstation:** The workstation the authentication request is originating from. Essentially, the computer name for this machine. |
| Custom HTTP headers | The web service requires additional headers outside of the usual username and password or API key. |

## Dedicated login operation

![Require a dedicated login operation](/assets/soap-require-dedicated-login-operation.CoCeTVop.png)_Require a dedicated login operation_

When you configure the SOAP connection, you can specify whether a dedicated login operation is required. A login operation validates credentials and obtains an authentication token or session identifier for subsequent interactions with the service. For most SOAP connections, it is not necessary.

To require a dedicated login, set the **Require dedicated login operation** field to **Yes**, and configure the following fields:

| Field | Description |
| --- | --- |
| Login binding | Name of the SOAP binding for the login operation. To find the binding name, identify the binding that has the login operation in the WSDL file. For example, in `<wsdl:binding name="MyServiceBinding">`, the binding name is `MyServiceBinding`. Note that the name is case-sensitive. |
| Login operation | Name of the operation to obtain an authentication token or session identifier for subsequent interactions with the service. To find the operation name, identify the login operation defined in the binding in the WSDL file. For example, in `<wsdl:operation name="login">`, the operation name is `login`. Note that the name is case-sensitive. |
| How to handle login results | Specify how to use the results of the login operation for subsequent operations. Typically, fields mapping is required. Select one of the following options: **Map fields to subsequent operations:** Use the authentication token or session identifier you get from this operation as input for later operations. You must "map" the fields by specifying which output field corresponds to which input field., **Process HTTP cookies:** Request a session cookie that will be sent along with later operations. |

> **FURTHER READING**
> 
> - [Connection setup](/en/connectors/soap#connection-setup)
> - [Execute operation action](/en/connectors/soap/execute-operation-action)

---
