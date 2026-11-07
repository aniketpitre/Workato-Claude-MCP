---
url: 'https://docs.workato.com/en/ai-gateway/providers.md'
description: >-
  Add, edit, and delete the LLM provider connections Model Gateway uses to
  authenticate with Anthropic, OpenAI, OpenAI Compatible, Azure OpenAI, AWS
  Bedrock, AWS Bedrock Mantle, Fireworks, and Gemini.
---

# Providers

A provider is a connection to an LLM service, along with the credentials [Model Gateway](/en/ai-gateway) uses to authenticate with it. Add a provider before you create the [routes](/en/ai-gateway/routes) that use it.

## Add a provider

Providers are stored in a project, and you can reuse the same provider connection in [genies](/en/agentic/agent-studio/ai-model/ai-model#connect-to-your-own-llm).

Model Gateway supports the following LLM providers: Anthropic, OpenAI, OpenAI Compatible, Azure OpenAI, AWS Bedrock, AWS Bedrock Mantle, Fireworks, and Gemini. The fields you configure depend on the provider you select.

Complete the following steps to add a provider:

1. Go to **Model Gateway > Providers**.
   
2. Click **\+ Add provider**.
   
   ![Add provider](/assets/add-provider.CjGYdUIf.png)_Add provider_
   
3. Enter a descriptive name in the **Connection name** field.
   
   ![Create provider](/assets/create-provider.HE8BuOwQ.png)_Create provider_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store this provider.
   
5. Use the **Connection type** drop-down menu to select **Cloud** or an [on-prem group](/en/on-prem/groups). Select an on-prem group if the provider is only reachable from your private network. If you select an on-prem group, any **API URL** or **Endpoint URL** you enter must be reachable from the on-prem agent's network. Private DNS names and IP addresses are allowed.
   
6. Use the **LLM Provider** drop-down menu to select the provider this connection uses. The remaining fields depend on the provider you select:
   
   **Anthropic**
   
   1. Enter the vendor-provided API key for this provider in the **API Key** field.
      
   2. Optional. Enter the API base URL in the **API URL** field. Leave this field blank to use the default, `https://api.anthropic.com/v1`.
      
   
   **OpenAI**
   
   1. Enter the vendor-provided API key for this provider in the **API Key** field.
      
   2. Optional. Enter the API base URL in the **API URL** field. Leave this field blank to use the OpenAI default, `https://api.openai.com/v1`.
      
   3. Optional. Enter the organization ID for OpenAI accounts with multiple organizations in the **Organization ID** field.
      
   4. Optional. Enter the project ID for OpenAI accounts with multiple projects in the **Project ID** field.
      
   
   **OpenAI Compatible**
   
   1. Enter the vendor-provided API key for this provider in the **API Key** field.
      
   2. Optional. Enter the API base URL in the **API URL** field. Leave this field blank to use the OpenAI default, `https://api.openai.com/v1`. Enter a value to override the default when you use a custom OpenAI-compatible API.
      
   3. Optional. Enter the organization ID for OpenAI accounts with multiple organizations in the **Organization ID** field.
      
   4. Optional. Enter the project ID for OpenAI accounts with multiple projects in the **Project ID** field.
      
   
   **Azure OpenAI**
   
   1. Enter the vendor-provided API key for this provider in the **API Key** field.
      
   2. Enter the Azure service endpoint URL in the **Endpoint URL** field, for example `https://your-resource.openai.azure.com`.
      
   3. Optional. Enter the Azure API version in the **API Version** field. Leave this field blank to use the default, `2024-08-01-preview`.
      
   
   **AWS Bedrock**
   
   1. Use the **Authentication type** drop-down menu to select **Access keys** or **Bedrock API key**.
      
   2. Enter the credentials for the authentication type you selected:
      
      - **Access keys**: Enter your access key in the **AWS Access Key ID** field and your secret key in the **AWS Secret Access Key** field. You can also enter a session token for temporary credentials in the **AWS Session Token** field.
      - **Bedrock API key**: Enter a long-term Amazon Bedrock API key in the **API Key** field. Short-term keys expire within 12 hours.
   3. Optional. Use the **AWS Region** drop-down menu to select the region where your Bedrock model is hosted. Defaults to **US East (N. Virginia)**.
      
   
   **AWS Bedrock Mantle**
   
   1. Use the **Authentication type** drop-down menu to select **Access keys** or **Bedrock API key**.
      
   2. Enter the credentials for the authentication type you selected:
      
      - **Access keys**: Enter your access key in the **AWS Access Key ID** field and your secret key in the **AWS Secret Access Key** field. You can also enter a session token for temporary credentials in the **AWS Session Token** field.
      - **Bedrock API key**: Enter a long-term Amazon Bedrock API key in the **API Key** field. Short-term keys expire within 12 hours.
   3. Optional. Use the **AWS Region** drop-down menu to select the region where your Bedrock model is hosted. Defaults to **US East (N. Virginia)**.
      
   4. Optional. Enter your Amazon Bedrock project ID in the **Project ID** field. Leave this field blank to use your default project.
      
   
   **Fireworks**
   
   1. Enter your Fireworks AI API key in the **API Key** field. Create an API key under **Settings > API Keys** in your Fireworks AI account. Refer to [Connect Fireworks AI](/en/ai-gateway/fireworks) for more information.
      
   2. Optional. Enter the API base URL, including the API version, in the **API URL** field. Leave this field blank to use the Fireworks AI default, `https://api.fireworks.ai/inference/v1`.
      
   
   **Gemini**
   
   1. Enter the vendor-provided API key for this provider in the **API Key** field.
      
   2. Optional. Enter the API base URL, including the API version, in the **API URL** field. For example, `https://generativelanguage.googleapis.com/v1beta`. Leave this field blank to use the Google default endpoint.
      
   
   Click **Connect** to complete the setup.
   
   > **PROVIDER UNREACHABLE**
   > 
   > Model Gateway returns `Error 503` and the message `Could not reach provider. The service may be temporarily down or overloaded. Please try again shortly.` when it can't reach the provider. Your entries are preserved. Click **Connect** again to retry.
   

The provider displays in the **Providers** list with a **Connected** status and the date it was added.

## Edit a provider

Complete the following steps to edit a provider:

1. Go to **Model Gateway > Providers**.
   
2. Click the **...** (ellipsis) menu for the provider you plan to edit, then click **Edit**. This opens the **Edit provider** page.
   
3. Update the fields for the provider.
   
4. Click **Save**.
   

## Delete a provider

Complete the following steps to delete a provider:

1. Go to **Model Gateway > Providers**.
   
2. Click the **...** (ellipsis) menu for the provider you plan to delete, then click **Delete**.
   
3. Review the impact summary in the **Delete provider** dialog.
   
4. Select **I understand that this action cannot be undone**.
   
   ![Delete a provider](/assets/delete-provider.JCXHE0q5.png)_Delete a provider_
   
5. Click **Delete**.
   

## Validation messages

Model Gateway returns the following validation messages when you add or edit a provider:

| Field | Message | Condition |
| --- | --- | --- |
| **Connection name** | `Name cannot exceed 100 characters.` | The name is longer than 100 characters. |
| **API URL** | `Please enter a valid URL.` | The value isn't a valid URL. |

---
