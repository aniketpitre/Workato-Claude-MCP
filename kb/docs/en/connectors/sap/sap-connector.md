---
url: 'https://docs.workato.com/en/connectors/sap/sap-connector.md'
description: >-
  Configure the SAP RFC connector in Workato by creating a connection, whether
  you use cloud profiles or set up connections manually in each agent.
---

# Configure the Workato SAP connector

To configure the SAP connector you must create a connection in the Workato UI.

There are two ways to create a connection in Workato depending on whether you've chosen to set up connections directly in Workato (Cloud profiles) or Manually in each agent (Legacy)

## If you're creating connections directly in Workato

1. Select the connector **SAP RFC**.
   
2. Select the on-prem group.
   
3. Provide the details of your connection in the connection fields. [Learn more](/en/on-prem/agents/connection/cloud#sap-profile)
   
4. Click **Connect**. If the connection is successful, you can start building recipes in Workato to talk to SAP.
   

## If you're creating connections manually in each agent

1. Select the connector **SAP RFC**.
   
2. Select the on-prem group.
   
3. Input the OPA profile name for SAP you have created in [Create a SAP profile in OPA](/en/on-prem/agents/connection/profile#on-prem-files-profile), in this case `sap_profile_qs4`.
   
4. Click **Connect**. If the connection is successful, you can start building recipes in Workato to talk to SAP.

---
