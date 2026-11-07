---
url: 'https://docs.workato.com/en/connectors/sap/sap-error-behavior.md'
description: >-
  Understand how the SAP RFC connector surfaces errors at runtime so you can
  distinguish technical failures, schema mismatches, and business errors.
---

# Error behavior in the SAP RFC connector

This page explains how the SAP RFC connector surfaces errors at runtime. Understanding these behaviors helps you design recipes that correctly distinguish between technical failures and business errors.

The SAP RFC connector supports multiple SAP interaction types, including Business Application Programming Interfaces (BAPIs), standard RFC-enabled function modules, and IDocs. These interaction types use different execution models, but include consistent high-level error behavior patterns that recipes can rely on.

## How SAP RFC errors surface at runtime

SAP RFC errors fall into the following categories at runtime. Each category produces distinct, observable behavior during recipe execution.

- [Technical (step-level errors)](#technical-step-level-errors)
- [Schema or parameter mismatches](#schema-or-parameter-mismatches)
- [Business errors returned in the response](#business-errors-returned-in-the-response)

### Technical (step-level errors)

Technical errors occur when the connector can't complete the RFC request–response cycle. The action step fails during recipe execution, and SAP business logic doesn't execute or return a business payload.

These errors usually indicate issues at the connectivity, transport, or SAP runtime level. Common examples include the following:

- Authentication or authorization failures, such as invalid credentials, missing SAP roles, or SNC misconfiguration
- Connectivity or transport issues, including unreachable SAP servers, RFC destination misconfiguration, network interruptions, or timeouts
- SAP runtime failures, such as missing function modules or low-level RFC/JCo exceptions

The recipe action step fails when a technical error occurs. No SAP business response payload is returned. The error surfaces in the recipe run as a technical exception. Workato translates some well-known exceptions into user-friendly messages to assist with diagnosis, while other exceptions surface as returned by the SAP RFC runtime.

### Schema or parameter mismatches

Schema or parameter mismatches occur when the interface definition expected by the connector doesn't align with what SAP expects or returns. These issues often appear during configuration or after SAP-side changes that aren't reflected in the recipe.

This behavior commonly results from the following:

- Incorrect recipe configuration, such as missing required parameters, invalid field names, or incorrect data types
- SAP-side interface changes, including added, removed, or renamed parameters, modified structures, or IDoc segment changes
- Metadata drift, where a previously working recipe fails after an SAP transport or configuration change

The action step fails when a schema or parameter mismatch occurs. The failure may occur before execution, such as during schema validation or request serialization, or during execution when SAP rejects incorrectly structured input. Errors typically surface as validation, parsing, serialization, or RFC/JCo exceptions.

These failures are considered technical errors because the action step fails and SAP doesn't return a business response payload.

### Business errors returned in the response

Business errors occur when SAP successfully executes the RFC call at a technical level but rejects the request based on application or business rules.

The connector treats these calls as successful and returns data to the recipe. SAP reports these failures through message structures rather than RFC exceptions, following SAP design guidelines, particularly for BAPIs.

SAP typically returns message structures such as `RETURN`, `BAPIRET2`, or `BAPIRETURN` in BAPI-based interactions. SAP sets the message type to `E` (Error) or `A` (Abort) on a business failure. Other RFC-enabled APIs may use different but conceptually equivalent message structures.

The recipe action step succeeds when a business error occurs. The response payload includes business error information. The recipe must implement error handling logic explicitly.

## Differences by SAP interaction type

The same high-level error categories apply across SAP interaction types. The way business errors surface varies by interaction type:

- BAPIs return business errors synchronously in message structures, while technical failures cause the step to error.
- Standard RFC-enabled function modules may return business errors in function-specific output fields, depending on the implementation.
- IDocs operate asynchronously. A successful step indicates SAP accepted the IDoc, not that SAP completed business processing. Business failures typically surface later through IDoc status tracking rather than as step-level errors.

## Recipe design guidance

Handle step-level failures as technical errors using retries, alerts, or error workflows. Manage successful steps that return business error information in the response using conditional logic in the recipe.

Implement follow-up status checks for IDoc-based integrations to detect downstream business failures after SAP accepts the IDoc. Use the [Check IDoc status action](/en/connectors/sap/action-check-idoc#sap-check-idoc-status-action) to retrieve the processing result.

---
