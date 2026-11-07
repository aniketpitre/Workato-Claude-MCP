---
url: 'https://docs.workato.com/en/connectors/sap/opa-configure.md'
description: >-
  Configure a Workato on-prem agent for SAP, including installing the OPA,
  downloading SAP JCo libraries, and creating an SAP profile.
---

# Configure OPA for SAP

You must complete the following steps to configure a Workato on-prem agent (OPA) for an SAP server:

1. [Install the Workato OPA](#opa-download)
2. [Download the SAP JCO libraries](#library-download)
3. [Create SAP profile in OPA](#sap-profile-create)
4. [Run the OPA](#opa-run)

## Install the Workato OPA

You must install a Workato on-prem agent either on your SAP server or on a separate virtual machine (VM) that can access your SAP server to allow Workato to connect to your SAP environment.

The VM server and your SAP server must be in the same domain, not outside of a firewall, and able to access each other. Ping each server from the other to test the VM server and the SAP's server's ability to communicate with each other.

Alternatively, if there are restrictions on downloading the on-prem agent on the same system or domain as SAP, you can use [SAP router](https://support.sap.com/en/tools/connectivity-tools/saprouter.html) to regulate access to your SAP system. This approach helps ensure compliance with internal policies and regulatory requirements.

Refer to the [Create group](/en/on-prem/groups/create-group) guide to download and set up a Workato on-prem group and create an on-prem agent.

> **CONNECTION SETUP RECOMMENDATION**
> 
> We recommend that you select **Directly in Workato** as the connection type for easier configuration management.

## Download the SAP JCO libraries

If you do not already have a license to use SAP JCo libraries, contact your SAP provider for a license.

> **SAP JCO, OPA COMPATIBILITY AND WORKATO SUPPORT**
> 
> | SAP JCo Version | OPA Version | Workato Support |
> | --- | --- | --- |
> | 3.0.x and 3.1.x | v27 and above | Limited support for SAP JCo 3.0.x (contact your customer support manager for more information). |
> | 3.1.7 and above | v25 - v26 | Yes (dropped support of SAP JCo 3.0) |
> | 3.1.6 and lower patches of release 3.1 | v24.3 and lower | Yes |
> | 3.0.x and 3.1.x | v24. v24.1, v24.2, v24.3 | Limited support for SAP JCo 3.0.x (contact your customer support manager for more information). |
> | 3.1.3 and above (recommended 3.1.7 and above) | v2.16.0 | Yes (dropped support of SAP JCo 3.0) |

Visit [SAP JCO Libraries](https://support.sap.com/en/product/connectors/jco.html) to download the following items:

- SAP JCO connector libraries
  - Direct connections (**version 3.1.7** and above)
  - Message server connections (**version 3.1.7** and above)

> **OPERATING SYSTEM COMPATIBILITY**
> 
> Select the correct version of the library for your operating system.
> 
> Additionally, refer to [SAP Note 2786882 - SAP JCo 3.1 release and support strategy](https://launchpad.support.sap.com/#/notes/2786882) to make sure your operating system fulfills all prerequisites.

After you download the libraries, place them in the `lib_ext/` directory of all on-prem agents in your created group.

<dl><dt>Windows users:</dt><dd>Ensure that you import all relevant files into the <code>lib_ext</code> folder. You should have imported a total of three files: <code>sapjco3.dll</code>, <code>sapjco3.jar</code>, and <code>sapidoc3.jar</code> into your <code>lib_ext</code> folder. A file named <code>sap-connector-impl-X.X.X.jar</code> should already be inside the folder.</dd><dt>Mac users:</dt><dd>Ensure that you import all relevant files into the <code>lib_ext</code> folder. You should have imported a total of three files: <code>libsapjco3.dylib</code>, <code>sapjco3.jar</code>, and <code>sapidoc3.jar</code> into your <code>lib_ext</code> folder. A file named <code>sap-connector-impl-X.X.X.jar</code> should already be inside the folder.</dd><dt>Linux users:</dt><dd>Ensure that you import all relevant files into the <code>lib_ext</code> folder. You should have imported a total of three files: <code>libsapjco3.so</code>, <code>sapjco3.jar</code>, and <code>sapidoc3.jar</code> into your <code>lib_ext</code> folder. A file named <code>sap-connector-impl-X.X.X.jar</code> should already be inside the folder.</dd></dl>

## Run the OPA

Refer to the [Run an on-prem agent](/en/on-prem/agents/run) guide to run the on-prem agent. After it successfully runs, you can move on to configure the SAP connector in Workato.

> **REFLECT SAP SCHEMA CHANGES**
> 
> You must click **Refresh** in the recipe editor when a change occurs in the BAPI, RFC, or IDoc schema for OPA versions v25 and later. For example, when new custom fields are added, changes are made to the data type, or changes are made in the field length. You must have SAP JCo 3.1.7 or above to use this feature. For OPA versions earlier than v25, you must restart OPA to reflect changes in Workato. ![Refresh SAP schema](/assets/refresh-schema.TvQLyaZL.png)_Refresh SAP schema_

## Create a SAP profile

Refer to one of the following guides based on your OPA connection type to create a SAP connection within Workato:

- `Directly in Workato` - Refer to the [SAP Cloud Profile](/en/on-prem/agents/connection/cloud#sap-profile) guide.
- `Manually in each agent` - Refer to the [SAP Profile](/en/on-prem/agents/connection/profile#sap-profile) guide. Restart the on-prem agent to enforce the changes after you configure the `config.yml` file. You must update the `config.yml` file for each agent in your group individually.

> **FURTHER READING**
> 
> To complete your connection to SAP RFC, read the following guides:
> 
> 1. [Configure the Workato SAP connector](/en/connectors/sap/sap-connector).
> 2. [Optional: Configure IDocs to/from Workato in SAP](/en/connectors/sap/configure-idoc-sap).

---
