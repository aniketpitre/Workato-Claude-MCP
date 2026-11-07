---
url: 'https://docs.workato.com/en/connectors/azure-openai.md'
description: >-
  Azure OpenAI is a collaboration between Microsoft Azure and OpenAI, an
  artificial intelligence research organization. Azure OpenAI is a cloud-based
  platform that enables users to build and deploy AI models.
---

# Azure OpenAI

[Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) is a collaboration between Microsoft Azure and [OpenAI](https://openai.com/), an artificial intelligence research organization. Azure OpenAI is a cloud-based platform that enables users to build and deploy AI models. These models allow you to edit text, generate images, and perform classification. You can fine-tune and create models that are exposed internally using Azure OpenAI.

## API version

The Azure OpenAI connector uses the [Azure OpenAI Service REST API](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference).

## How to connect to Azure OpenAI

Workato supports the following types of connections to Azure OpenAI:

- [OAuth 2.0 authentication](#oauth2)
- [API key authentication](#api-key-authentication)

> **MICROSOFT MFA ENFORCEMENT**
> 
> Microsoft is rolling out mandatory multifactor authentication (MFA) gradually to different applications and accounts in phases. This enforcement continues throughout 2025 and beyond. Refer to the Microsoft [Mandatory multifactor authentication for Azure and admin portals](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication?tabs=dotnet) documentation for more information.
> 
> We strongly recommend enabling MFA now for all Microsoft accounts used with Workato to avoid service disruptions from short-notice enforcement changes.
> 
> Complete the following steps to maintain uninterrupted service:
> 
> 1. Enable MFA for your Microsoft organization following the Microsoft MFA setup guide. Refer to [Set up multifactor authentication for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365-worldwide) for more information.
>    
> 2. Reconnect your Microsoft connection in Workato.
>    
> 3. Complete the OAuth flow with MFA when prompted.
>    
> 4. Test your recipes to ensure they work with the updated connection.
>    

### OAuth 2.0 authentication

OAuth 2.0 authentication consists of the following steps:

- [Complete the prerequisites](#client-credentials)
- [Complete setup in Workato](#setup-oauth2)

#### Prerequisites

You must complete the following prerequisites to establish an OAuth 2.0 connection to Azure OpenAI:

- Refer to the Azure [OAuth 2.0 authorization](https://learn.microsoft.com/en-us/azure/api-management/api-management-authenticate-authorize-ai-apis#oauth-20-authorization-by-using-identity-provider) documentation to generate a client ID and secret using an identity provider, such as Microsoft Entra ID.
- Refer to the Azure [Delegate an Azure DNS subdomain](https://learn.microsoft.com/en-us/azure/dns/delegate-subdomain) documentation to delegate a subdomain in the Azure portal.

#### Complete setup in Workato

Complete the following steps to establish an OAuth 2.0 connection to Azure OpenAI:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Azure OpenAI` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Azure OpenAI OAuth 2.0 connection](/assets/azure-openai-connect-oauth2.DSPUPSpV.png)_Azure OpenAI OAuth 2.0 connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select `OAuth 2.0`.
   
6. Enter the **Client ID** and **Client secret** for your Azure application.
   
7. Enter your organization's **Sub domain**.
   
8. Click **Connect**.
   

### API key authentication

API key authentication consists of the following steps:

1. [Complete the prerequisites](#api-key)
2. [Complete setup in Workato](#setup)

#### Prerequisites

You must complete the following prerequisites to establish an API key connection to Azure OpenAI:

- Refer to the Azure OpenAI [Authentication](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#authentication) documentation to generate an API key. Workato recommends that you store the API key safely, as it's only displayed once.
- Refer to the Azure [Delegate an Azure DNS subdomain](https://learn.microsoft.com/en-us/azure/dns/delegate-subdomain) documentation to delegate a subdomain in the Azure portal.

#### Complete setup in Workato

Complete the following steps to establish an API key connection to Azure OpenAI:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Azure OpenAI` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Azure OpenAI API key connection](/assets/azure-openai-connect.Db5jU4AO.png)_Azure OpenAI API key connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select `API key`.
   
6. Enter the **API key**.
   
7. Enter your organization's **Sub domain**.
   
8. Click **Connect**.
   

## Supported actions

Azure OpenAI supports the following actions:

- [Complete text prompt](/en/connectors/azure-openai/complete-text-prompt)
- [Generate images](/en/connectors/azure-openai/generate-images)
- [Generate text embedding](/en/connectors/azure-openai/generate-text-embedding)
- [Send messages to ChatGPT](/en/connectors/azure-openai/chatgpt-conversations)

---
