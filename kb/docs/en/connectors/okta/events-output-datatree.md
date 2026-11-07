---
url: 'https://docs.workato.com/en/connectors/okta/events-output-datatree.md'
description: >-
  Reference for the Okta events output datatree, covering actor, client,
  authentication, security, transaction, and target fields for log events.
---

# Okta - Output datatree for events

The output datatree contains basic information about the event like the outcome and timestamp. Additionally, it contains data objects about the following:

- Actor
- Client
- Authentication context
- Security context
- Transaction information
- Targets of the event

| Output field | Description |
| --- | --- |
| Version | A versioning indicator. |
| Actor _The entity that created the event._ | ID | ID of the actor. |
| Type | Type of actor. |
| Alternate ID | Alternative ID of the actor. |
| Display Name | Display name of the actor. |
| Detail | Details about the actor. |
| Client _Where the HTTP request originated from._ | User Agent object | A software acting on behalf of a user. This object includes the User agent, OS, and Browser. |
| Zone | Display name of the actor. |
| Device | The type of device (for example, a computer). |
| ID | ID of the OAuth client or ID of the agent. |
| IP address | The IP address where the request originated. |
| Geographical context object | The physical location where the client made the request. It contains information about city, state, country, postal code as well as geolocation coordinates. |
| Authentication context _This contains metadata about how the actor was authenticated._ | Authentication provider | The system that proves the identity of an actor. |
| Credential provider | A credential provider is a software service that manages identities and their associated credentials. |
| Credential type | The credential type used. |
| Interface | The third party user interface. |
| Authentication step | A zero-based step number in the authentication pipeline. |
| External session ID | A proxy for the actor's session ID. |
| Issuer object | The specific software entity that created and issued the credential. It contains information about The ID and type of the authorization server. |
| Display message | The display message for the event. |
| Event type | The type of event that was retrieved. |
| Outcome _Information about the result of the event._ | Result | Result of the action. |
| Reason | The result of the result. Usually, this describes the error message. |
| Published | The timestamp when the event was published. |
| Security context _Security data of the event._ | As number | Autonomous system number associated with the autonomous system that the event request was sourced to. Refer to the [Autonomous system](https://en.wikipedia.org/wiki/Autonomous_system_\(Internet\)) Wikipedia article for more information. |
| As organization | Organization associated with the autonomous system that the event request was sourced to. |
| ISP | The internet service provider used to send the event request. |
| Domain | The domain name associated with the IP address of the inbound event request. |
| Is proxy | Specifies whether this event's request is from a known proxy. |
| Severity | This indicates how severe the event is. |
| Debug context | Contains additional information about the event. The debug data includes **Request URI, Request ID, and URL**. |
| Legacy event type | Associated events API attribute value. |
| Transaction _Transaction details of the event._ | Type | Describes the kind of transaction. For example, \`Web\` or \`Job\`. |
| ID | The unique identifiers for this transaction. |
| UUID | A unique identifier for this event. |
| Request | Information about the request that triggered this event. If it is sourced from a HTTP request, it will return an IP chain. |
| Target _A list datapill that describes the targets of the event._ | ID | ID of the target. |
| Type | Type of the target |
| Alternate ID | The alternative ID of the target. |
| Display name | The display name of the target. |
| Detail entry | Details about the target. |
| List size | The number of targets in the list. |
| List index | The index of this target in the list of targets. |

Refer to the Okta [log event object](https://developer.okta.com/docs/reference/api/system-log/#request-object) documentation for more information.

---
