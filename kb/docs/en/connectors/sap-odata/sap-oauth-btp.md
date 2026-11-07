---
url: 'https://docs.workato.com/en/connectors/sap-odata/sap-oauth-btp.md'
description: >-
  Connect SAP OData to Workato using OAuth 2.0 SAML Bearer Assertion through SAP
  BTP destination authentication for SAP S/4HANA Cloud, Public Edition.
---

# OAuth Business Technology Platform (BTP) Authentication

Workato supports OAuth 2.0 (Open Authorization 2.0) through SAP BTP Destination Authentication Method using OAuth2SAMLBearerAssertion. OAuth 2.0 SAML Bearer Assertion is a way of using Security Assertion Markup Language (SAML) assertions as authorization grants in OAuth 2.0. This flow allows systems that rely on SAML for authentication to leverage OAuth 2.0 for accessing OAuth-protected resources, combining the strengths of both protocols. This authentication is applicable for SAP S/4HANA Cloud, Public Edition.

## Configuration prerequisites for OAuth BTP

- Access to SAP S/4HANA Cloud with the catalogs `SAP_CORE_BC_EXT` and `SAP_CORE_BC_COM` assigned to the business user.
- Access to SAP Business Technology Platform.
- Admin access to a SAP Cloud Identity provider such as SAP Cloud Identity Services.

### Establish trust and federation

Complete the steps to [manually establish trust and federation between SAP Authorization and Trust Management Service and Identity Authentication](https://help.sap.com/docs/authorization-and-trust-management-service/authorization-and-trust-management/manually-establish-trust-and-federation-between-uaa-and-identity-authentication) and do the following:

- **Establish Trust with an SAML 2.0 Identity Provider in a Subaccount**: You must use a SAML 2.0 identity provider, for example, SAP Cloud Identity Services - Identity Authentication. The identity provider authenticates business users for SAP BTP.
- **Register SAP BTP Subaccount in the SAML 2.0 Identity Provider**: To establish trust between an identity provider and a Subaccount, you must register your subaccount by providing the SAML metadata to the identity provider. The identity provider is SAP Cloud Identity Services - Identity Authentication.

### Create signing certificate from SAP BTP

The SAML assertion sent to SAP S/4HANA Cloud is signed using the private key of the local service provider. To enable SAP S/4HANA Cloud to verify this signature, the relevant certificate is required.

1. Log in to SAP BTP Cockpit.
   
2. Create a Signing Certificate from the SAP BTP Account by navigating to **Destinations** under Connectivity and clicking **Download Trust**. ![OAuth BTP Trust](/assets/oauth-btp-trust.DyscsEoF.png)
   

## Implementation steps in the SAP S/4HANA Cloud System

Complete the steps to [allow inbound communication to the SAP S/4HANA tenant](https://help.sap.com/docs/SAP_EXTENSIBILITY_EXPLORER/8ce29283d61a4bca96e9e7d87c95baa3/a53d6d9c482f47a1b9e65712db544d70.html) and do the following:

1. Create Communication System and User.
2. Create Communication Arrangement.
3. Maintain Business User in the SAP S/4HANA Cloud System.

## Implementation steps on SAP Business Technology Platform

1. Complete these steps to [create and configure a destination in SAP BTP](https://help.sap.com/docs/SAP_EXTENSIBILITY_EXPLORER/8ce29283d61a4bca96e9e7d87c95baa3/4673c0fb402c45a78ff78b4baef8f73e.html).  
     
   Maintain the values of the properties as suggested in the following sample table:
   
   | Property | Value |
   | --- | --- |
   | Name | Provide a unique name identifier, for example `OAuth2Destination`. |
   | Type | HTTP |
   | Description | Provide a description for the destination describing the purpose. |
   | URL | Provide a service URL, for example: `https://www.myS4HanaSystem.com/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV`. |
   | Proxy Type | Internet |
   | Authentication | OAuth2SAMLBearerAssertion |
   | Audience | Provide the base URL to your SAP S/4HANA Cloud system, for example `https://myXXXXXX.s4hana.ondemand.com`. |
   | AuthnContextClassRef | `urn:oasis:names:tc:SAML:2.0:ac:classes:X509` |
   | Client Key | Enter the communication user name. |
   | Token Service URL Type | Dedicated |
   | Token Service URL | Provide a token URL, for example: `https://www.myS4HanaSystem.com/sap/bc/sec/oauth2/token`. |
   | Token Service User | Enter the communication user name. |
   | Token Service Password | Enter the communication user password. |
   
   | Additional properties | Value |
   | --- | --- |
   | nameIdFormat | `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` |
   | scope | Provide scope ID, for example: `API_PURCHASEORDER_PROCESS_SRV_0001`. |
   | SystemUser | The email ID of the business user. |
   
   > **CLIENT KEY, TOKEN SERVICE USER, AND TOKEN SERVICE URL VALUES**
   > 
   > Navigate to the **Communication Arrangements** application and search for the arrangement that you created. Go to **Inbound Communication** and choose **OAuth2.0 Details**. The value of the **Client Key** and **Token Service User** are the same as the User Name. You can also obtain the **Token Service URL** from this interface. ![OAuth BTP Token](/assets/oauth-btp-token.dHGI9Q-3.png)
   
2. Navigate to **Instances and Subscriptions** under **Services** and click **Create** to create a service instance. ![OAuth Service Instance](/assets/oauth-btp-service-instance.CtZWQLu2.png)
   
3. Select **Destination Service** in Service, **lite** in Plan, **Other** in Runtime Environment and a description name in the Instance Name. ![OAuth Service Instance creation](/assets/oauth-btp-service-binding.D2wzfC0m.png)
   
4. Once instance is created, click on it to proceed ahead for creation of Service Binding.
   
5. Click **Create** and provide a descriptive Binding Name. ![OAuth Service binding](/assets/oauth-btp-service-binding1.DsfPOECe.png)
   
6. Click **View** or **Download** to retrieve the Service Credentials after creating **Service Binding**.
   

## Connection fields

Complete the following fields in Workato to finish establishing your connection:

> **ODATA VERSIONS**
> 
> We recommend that you create dedicated connections for V2 and V4 APIs.

| Field | Description |
| --- | --- |
| Connection name | Provide the connection with a descriptive name so you can reuse it in other recipes. |
| Connection type | Select `Cloud`. |
| Authentication type | Select `OAuth BTP`. |
| OData version | Select OData version for the API used in this connection - `v2` or `v4`. |
| Client ID | Enter the value as per the parameter `clientid` in Service Binding downloaded from SAP BTP. |
| Client Secret | Enter the value as per the parameter `clientsecret` in Service Binding downloaded from SAP BTP. |
| Authentication URL | Provide the authentication URL. This is the value of the `url` parameter in your Service Binding. For example: `https://s-4hana-cloud.authentication.eu10.hana.ondemand.com`. |
| Destination URL | Provide URL of the destination service. This is the value of the `uri` parameter in your Service Binding. For example: `https://destination-configuration.cfapps.eu10.hana.ondemand.com`. |
| Destination Name | Provide the unique name identifier of the destination as defined in SAP BTP cockpit under **Connectivity > Destinations**. |
| Host | Provide the host name of the SAP Application Server. For example: If `https://www.myS4HanaSystem.com/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV` is the service URL, your host is `https://www.myS4HanaSystem.com/sap/opu/odata/sap/`. |
| Service | Provide the service configured in the SAP system. For example: If `https://www.myS4HanaSystem.com/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV` is the service URL, your service is `API_PURCHASEORDER_PROCESS_SRV`. |
| SAP client | Leave it blank. |

---
