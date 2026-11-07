---
url: 'https://docs.workato.com/en/connectors/sap/connection-setup.md'
description: >-
  Connect the SAP RFC connector to Workato, including RFC destination,
  integration user, OPA configuration, and optional IDoc setup steps.
---

# Connect to SAP RFC

The SAP RFC connector runs in all SAP systems even when a firewall is in use. You can either deploy an on-prem agent within the same subnet domain as SAP to ensure seamless connectivity regardless of firewall configurations or use a SAP Router string in the connection property to route the call through a SAP router in case an on-prem agent is on a different domain subnet.

* * *

## Configuration setup for RFC communication with SAP

Connecting the SAP RFC connector to Workato for IDocs is a multi-step process. To configure the connection, complete these phases in the following order:

1. [Create RFC destination for Workato in SAP](/en/connectors/sap/rfc-destination-create)
2. [Create a Workato integration user in SAP](/en/connectors/sap/integration-user-create)
3. [Configure OPA for SAP](/en/connectors/sap/opa-configure)
4. [Configure the Workato SAP connector](/en/connectors/sap/sap-connector)
5. [Optional: Configure IDocs to/from Workato in SAP](/en/connectors/sap/configure-idoc-sap)

* * *

## Troubleshooting

If you encounter error at any step, review our [troubleshooting guide](/en/connectors/sap/sap-troubleshooting).

---
