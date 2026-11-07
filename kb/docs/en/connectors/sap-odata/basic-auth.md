---
url: 'https://docs.workato.com/en/connectors/sap-odata/basic-auth.md'
description: >-
  Set up and connect on-premise SAP instances to Workato, including activating
  OData services for SAP S/4HANA and legacy ECC systems.
---

# How to connect to on-premise SAP instances on Workato

Complete the following steps to set up OData services for your on-premise SAP system. Most legacy SAP systems as well as new SAP S/4HANA instances use the same or similar steps. However, legacy SAP systems such as ECC, do not have standard OData services available. Refer to this [blogpost](https://blogs.sap.com/2021/05/06/a-step-by-step-process-to-create-odata-services-in-sap-sap-hana-system/) to create a custom OData service on your SAP Gateway.

If you're using SAP S/4HANA on-premise or [SAP S/4HANA Cloud, private edition](https://www.sap.com/products/erp/s4hana-private-edition.html), the following steps illustrate how to set up an example service for exposing OData v2 service.

For exposing OData v4 service, please refer to the section [Publish Service Group](https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_752/68bf513362174d54b58cddec28794093/97abd231f89a40169aaaad017439531e.html#publish-service-group) in the official SAP help documentation.

1. Go to transaction code `/n/iwfnd/maint_service`
   
   ![Activate and Maintain service](/assets/activate-maintain-service.m1cQLHcl.png)_Activate the service_
   
2. Click **Add Service**, maintain `LOCAL` in the **System Alias** field, and press Enter.
   
   ![Add service](/assets/add-service.CahMm1Di.png)_Add a service_
   
3. Select service and click on Add Selected Services. In this example, we are adding `API_BANKACCOUNT_SRV` - a standard SAP API.
   
   ![Add selected service](/assets/add-selected-service.DSjlT5SS.png)_Add your selected service_
   
4. Name the technical service. In our example, its `ZAPI_BANKACCOUNT_SRV`. Click on Local Object to Save in Local Package and continue.
   
   ![Save in local package](/assets/save-local-package.Bd6r5GG4.png)_Save the local package_
   
   ![Confirmation](data:image/png;base64,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)_Confirmation message_
   
5. Test your new OData service by going to the **Service Catalog**, search for `Technical Service Name`, and then click **Call Browser** to hit the OData Endpoint URL on the Browser and SAP Gateway Client. You can test different options, such as operations, methods, headers, payload , and more on the Gateway Client.
   
   ![search for technical service](/assets/search-for-service.Kt2R0pAY.png)_Search for the technical service_
   
   ![test in call browser](/assets/test-in-call-browser.bF8tXDau.png)_Test in-call browser_
   

Return to Workato to fill in the [connection fields](/en/connectors/sap-odata/client-cert-auth#connection-fields) with the same details displayed in the SAP Gateway Client. Refer to the [minimum permissions](/en/connectors/sap-odata/connection-setup#sap-permissions) section to review the minimum permissions required to establish a connection.

## How to connect to SAP S/4HANA Cloud via Basic Authentication on Workato

Complete the following steps to set up OData services for your SAP S/4HANA Cloud instance.

1. Find the OData API for your automation requirements in the [SAP API Business Hub explorer](https://api.sap.com/package/SAPS4HANACloud?section=Artifacts).
   
   ![SAP API explorer](/assets/api_explorer.BOhdewup.png)_SAP API explorer_
   
2. Click to open the API you plan to use and locate the communication scenario ID. Store this ID for use later on.
   
   ![API communication scenario](/assets/details_communication_scenario.DoubNr09.png)_API details communication_
   
3. Follow the steps in [Setting up Communication Management](https://blogs.sap.com/2017/11/09/setting-up-communication-management-in-sap-s4hana-cloud/). This process includes the following required tasks:
   
   - **Create a Communication User**: the integration user assigned to Workato. Ensure that you **use basic authentication**.
   - **Create a Communication System**: tied to the communication User.
   - **Create a Communication Arrangement**: ties the communication system and user to the communication scenario.
4. Return to Workato to fill in the [connection fields](/en/connectors/sap-odata/client-cert-auth#connection-fields).

---
