---
url: 'https://docs.workato.com/en/connectors/veza.md'
description: >-
  Connect Veza to Workato to automate identity and access governance workflows,
  enforcing least-privilege access and securing sensitive cloud data.
---

# Veza

[Veza](https://veza.com/) is a data security platform that helps organizations manage and secure access to sensitive data across cloud and hybrid environments. Veza provides identity and access governance by integrating with identity providers, cloud services, and data systems. You can use Veza to enforce least-privilege access, maintain compliance, and reduce security risks.

## Prerequisites

Ensure you have the following items before you set up the Veza connector in Workato:

- An API key for your Veza user account

### Generate an API key in Veza

1. Sign in to your Veza account.
   
2. Go to **Administration > API Keys > Add New API Key**.
   
3. Enter a descriptive name for the API key and then click **Save**.
   
4. Copy the API key and store it in a secure location. The API key can't be viewed again.
   

## How to connect to Veza

Complete the following steps to set up a connection between Workato and Veza:

1. Sign in to your Workato account and go to the project where you plan to add your Veza connection.
   
2. Click **Create > Connection** or press C twice.
   
3. Search for and select **Veza** as your connection.
   
4. Provide a unique name for the connection in the **Connection name** field.
   
   ![Veza Connection](/assets/connection.CxeNQA1_.png)_Veza Connection_
   
5. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
6. Provide your API token in the **API Token** field.
   
7. Provide the base URL for your Veza API in the **Sub-domain** field. For example: `https://<your-tenant>.veza.com`

---
