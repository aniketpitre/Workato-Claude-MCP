---
url: 'https://docs.workato.com/en/connectors/kissflow.md'
description: >-
  Connect Kissflow to Workato to automate business process management workflows
  and manage processes and datasets through the Kissflow API.
---

# Kissflow

[Kissflow](https://kissflow.com) is a cloud-based business process management platform that helps you streamline, automate, and manage workflows with ease. This connector lets you interact with the Kissflow API to manage processes and datasets efficiently.

## Prerequisites

Before using the Kissflow connector in Workato, ensure you have an active account and a Kissflow instance with permissions to access the Kissflow API.

### Create an access key

Complete the following steps to create an access key in Kissflow:

1. Click your profile picture and navigate to **My settings > API authentication > Access keys**.
   
2. Click **Create Access Key**.
   
3. Enter a name for the access key.
   
4. Set an appropriate expiry period for the key.
   
5. Copy the access key **ID** and **secret** and store them in your preferred location on your computer. Alternatively, you can click **Download credentials** to store them directly as a file.
   
6. Click **Done** after downloading the access key credentials.
   
7. Click **Proceed** to confirm your action after reading the alert message. Your access key has been successfully created.
   

### Retrieve your account ID

The account ID is a unique alphanumeric key that distinguishes your Kissflow account from other accounts. You can copy the Account ID from **My Settings > API Authentication > Account ID** and use it for your API sessions while establishing secured connections.

## How to connect to Kissflow

Complete the following steps to establish a Kissflow connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Kissflow** as your connection on the **New connection** page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
   ![Kissflow connection](/assets/kissflow-connection.VmHU7Zlm.png)_Kissflow connection_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to save your connection.
   
5. Enter the **Account ID** for your Kissflow account.
   
6. Enter the **Region** for your Kissflow account instance. You can locate this value in your Kissflow instance URL. For example, if the URL ends with `.com`, the region is `US`. Otherwise, the region is `EU`.
   
7. Enter the **Access key ID** and the **Access key secret** for your Kissflow account.
   
8. Enter your Kissflow **Account domain** using your instance URL.
   
9. Click **Connect**.

---
