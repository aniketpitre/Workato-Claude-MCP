---
url: 'https://docs.workato.com/en/connectors/zuora.md'
description: >-
  The Zuora connector lets you automate subscription billing workflows: create,
  update, search, and query records across your order-to-revenue processes.
---

# Zuora

[Zuora](https://www.zuora.com/) is a cloud-based SaaS platform that specializes in handling the complexity of Order-to-Revenue processes for subscription based businesses. It has a suite of tools that handle billing and renewal cycles of customers and can also handle payment collection from customers.

## API version

The Zuora connector uses [Zuora REST API](https://www.zuora.com/developer/api-reference/). Support for Zuora Collect APIs and RevPro APIs will be introduced in separate connectors.

## How to connect to Zuora on Workato

The Zuora connector uses OAuth2. This will require you to generate an OAuth client on Zuora.

![Subdomain setup](/assets/connection.Btaat78f.png)_Connection setup_

| Field | Description |
| --- | --- |
| Connection name | Give this Zuora connection a unique name that identifies which Zuora instance it is connected to. |
| Client ID | The client ID of the OAuth app generated in Zuora. Create a client OAuth app by following the instructions over [here.](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) |
| Client secret | The client secret of the OAuth app generated in Zuora. Create a client OAuth app by following the instructions over [here.](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) |
| Environment | This affects the URL of the endpoints in Zuora that Workato will make requests to. Ensure that you pick the proper Environment. More details can be found [here.](https://jp.zuora.com/developer/api-reference/#section/Introduction/Access-to-the-API) |
| Zuora SOAP API version | Pick the latest WSDL version, which can be found [here.](https://knowledgecenter.zuora.com/DC_Developers/G_SOAP_API/Zuora_SOAP_API_Version_History) |

---
