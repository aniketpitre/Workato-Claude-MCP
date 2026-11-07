---
url: >-
  https://docs.workato.com/en/connectors/netsuite/troubleshooting/troubleshoot-netsuite-connection.md
description: >-
  Use this guide to troubleshoot errors that occur when establishing a NetSuite
  connection in Workato.
---

# Troubleshoot NetSuite connection errors

Use this guide to troubleshoot errors that occur when establishing a NetSuite connection in Workato.

## Error establishing connection when Subsidiaries feature isn't enabled

You may receive a connection error if your NetSuite account doesn't have the Subsidiaries feature enabled. This error can occur even if your account has only one legal entity.

To resolve this issue:

- Enable the subsidiaries feature in NetSuite.
- Grant the integration user access to the correct subsidiary if the feature is already enabled.

Ensure the integration user has the following NetSuite permissions:

- SOAP Web Services
- Set Up Company
- User Access Tokens
- Log in using OAuth 2.0 Access Tokens
