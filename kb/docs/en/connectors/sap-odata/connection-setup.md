---
url: 'https://docs.workato.com/en/connectors/sap-odata/connection-setup.md'
description: >-
  Set up and connect SAP OData in Workato across on-premise and SAP S/4HANA
  Cloud systems, using an on-prem agent or IP allowlisting.
---

# Connect to SAP OData

The SAP OData connector runs in all on-premise SAP systems supporting OData under **SAP Business Suite including, SAP BW and SAP BW/4HANA**, **SAP S/4HANA Cloud, Private Edition** and **SAP S/4HANA Cloud, Public Edition**. You can deploy an on-prem agent within the same subnet domain in cases in which the SAP system is behind a firewall.

> **CONNECT TO SAP ON-PREMISE SYSTEMS**
> 
> Complete the following steps to connect to the on-premise SAP system through an [on-prem agent](/en/on-prem):
> 
> 1. Navigate to the OPA installation file structure that allows you to grant agent access to [HTTP resources](/en/on-prem/agents/connection/profile#http-profile).
>    
> 2. Navigate to the **config** directory and configure your `config.yml` file.
>    
> 
> However, if you want to connect to the on-premise SAP systems without an on-prem agent, then you can allow traffic from Workato by whitelisting these [IP addresses](/en/security/ip-allowlists#traffic-from-workato) for HTTPS port (maintained in `SMICM` transaction code in SAP application or SAP Web dispatcher port if you use it for exposing HTTPS calls) in the inbound rules of the SAP server's firewall.

## Supported authentication

SAP OData connector supports following authentication types:

- [Basic Authentication](/en/connectors/sap-odata/basic-auth): supported by on-premise SAP Business Suite applications, SAP S/4HANA Cloud Private Edition and SAP S/4HANA Cloud Public Edition.
- [Client Certificate Authentication](/en/connectors/sap-odata/client-cert-auth): supported by SAP S/4HANA Cloud, Public Edition.
- [OAuth 2.0 Authentication](/en/connectors/sap-odata/sap-oauth2): Authorization code grant and Client credentials supported by on-premise SAP Business Suite applications and SAP S/4HANA Cloud, Private Edition.
- [OAuth BTP Authentication](/en/connectors/sap-odata/sap-oauth-btp): supported by SAP S/4HANA Cloud, Public Edition.

## Minimum permissions required

The following permissions are required to establish a basic connection:

On-premise SAP Business suite applications and SAP S/4HANA Cloud, Private Edition

The following authorizations are required to establish a basic connection:

| Authorization Object | Activity (ACTVT) |
| --- | --- |
| S\_USER\_GRP | 03 |

| Authorization Object | SRV\_NAME | SRV\_TYPE |
| --- | --- | --- |
| S\_SERVICE | \[Service ID as captured in transaction code `ST01`\] | \[Service Type as captured in transaction code `ST01` \] |

Additional authorization required for OAuth2 connection:

| Authorization Object | Activity (ACTVT) |
| --- | --- |
| /IWFND/ADM | 03 |

| Authorization Object | OA2\_CLIENT | OA2\_SCOPE |
| --- | --- | --- |
| S\_SCOPE | \[OAuth 2.0 Client ID created in transaction code `SOAUTH2`\] | \[OAuth 2.0 Scope ID assigned to the Client ID. For example: `/IWFND/SG_MED_CATALOG_0002`\] |

SAP S/4HANA Cloud, Public Edition

Ensure that you [set up Communication Management](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/2e84a10c430645a88bdbfaaa23ac9ff7.html) in your SAP S/4HANA Public Cloud instance to provide access to specific services to which you plan to connect. Refer to the [SAP S/4HANA official documentation](https://api.sap.com/products/SAPS4HANACloud/apis/ODATA) to check the relevant Communication Scenario to which the OData service is associated.

---
