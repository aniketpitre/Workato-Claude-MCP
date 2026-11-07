---
url: 'https://docs.workato.com/en/connectors/mastercard.md'
description: >-
  Connect Mastercard to Workato to automate payment and financial services
  workflows using the Mastercard payment network for secure electronic
  transactions.
---

# Mastercard

[Mastercard](https://mastercard.us) is a financial services company that provides a payment network for electronic transactions. It enables secure transactions and is widely accepted by merchants globally, allowing customers to make payments efficiently.

## Prerequisites

Before using the Mastercard connector on Workato, you must have a Mastercard developers account. Complete the following steps to set up your account:

1. [Obtain a Mastercard developers account](#account-obtain)
2. [Create a new project in the Mastercard developer portal](#new-project)
3. [Configure environment and keys](#configure-environment-and-keys)
4. [Export your signing key](#export-signing-key)

### Obtain a Mastercard Developers account

Complete the following steps to obtain a Mastercard developers account:

1. Go to the [Mastercard Developers account sign up page](https://developer.mastercard.com/account/sign-up).
   
2. Fill out the required fields and click **Create account.**
   
3. Activate your account through the link sent to your registered email address.
   

You can use your Mastercard Developer account to create projects, access APIs, and request production access.

### Create a new project in the Mastercard developer portal

Complete the following steps to create a new project in the Mastercard developer portal:

1. Create a project on your [My Projects](https://developer.mastercard.com/dashboard) page.
   
2. Name your project.
   
3. Indicate whether you are creating a project on behalf of a client.
   
4. Provide the client company name and client company address (if applicable).
   
5. Select the API service you plan to integrate with.
   
6. Provide the **Commercial countries** for the project. This field represents where you are doing business.
   
7. Fill out additional details that the API service requires (if applicable).
   

### Configure your environment and keys.

Complete the following steps to configure your environment and keys:

1. Within your project, select **Credentials**.
   
2. Choose whether you are creating a **Sandbox/Production** key.
   
3. Click **Add project key.**
   
4. Enter your Sandbox key alias and keystore password.
   
5. Click **Create key**.
   

### Export your signing key.

Complete the following steps to export your key to **.pem** format. This is necessary to use the key in Workato.

1. To export your key to a PKCS#1 PEM file (BEGIN RSA PRIVATE KEY), run the following command: `openssl pkcs12 \-in key.p12 \-nodes | openssl rsa \-outform pem \-out pkcs1-key.pem`
   
2. To export your key to a PKCS#8 PEM file (BEGIN PRIVATE KEY), run the following command: `openssl pkcs12 \-in key.p12 \-nodes | openssl pkcs8 \-topk8 \-nocrypt \-out pkcs8-key.pem`
   

## How to connect to Mastercard on Workato

The Mastercard connector supports OAuth 1.0a authentication. Complete the following steps to establish a connection to Mastercard:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Mastercard** as your connection on the New Connection page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your consumer key in the **Consumer key** field.
   
6. Enter your private key in the **Private key** field.
   
7. Choose your environment in the **Environment** drop-down, if applicable.
   
8. Click **Connect**.
   
   ![Mastercard connection](/assets/mastercard-connection.DSeDyZ1I.png)_Mastercard connection_

---

---
url: >-
  https://docs.workato.com/en/connectors/mastercard/enroll-or-unenroll-merchants.md
description: >-
  The Enroll/unenroll merchants action enables you to add or delete merchants in
  Mastercard.
---

# Mastercard - Enroll/unenroll merchants action

The **Enroll/unenroll merchants** action enables you to add or delete merchants in Mastercard.

## Input

| Input fields | Description |
| --- | --- |
| Merchant data | Provide an array of merchant data objects containing the merchant details. |
| Processor name | Provide the name of the service provider or acquirer. For example, `MPGS`. |
| Action | Select the action to be performed, either add or delete. |
| Acquirer BIN | Provide the acquirer reference ID number. |
| Acquirer CID | Provide the acquirer company ID. |
| Acquirer ICA | Provide the acquirer ICA number. |
| Acquirer Name | Enter the acquirer name. |
| Merchant ID | Provide the acquirer Merchant ID. |
| Merchant name | Enter the name of the merchant. |
| Identity Check Express | Select a flag for Identity Check Express. Valid values are `Y` or `N`. |
| Delete reason | Provide a reason for deleting the merchant enrollment. This is only required if the selected action is delete. |

## Output

| Output fields | Description |
| --- | --- |
| Message type | Type of the message. |
| Total records | Total number of records processed. |
| Transaction ID | Unique ID of the transaction. |

---

---
url: >-
  https://docs.workato.com/en/connectors/mastercard/get-status-of-merchant-enrollment-action.md
description: >-
  The Get status of merchant enrollment action enables you to fetch the status
  of enrolled merchants.
---

# Mastercard - Get status of merchant enrollment action

The **Get status of merchant enrollment** action enables you to fetch the status of enrolled merchants.

## Input

| Input fields | Description |
| --- | --- |
| Transaction ID | Provide the transaction ID of the merchant enrolled. |
| Limit | Enter the number of records to fetch. |
| Offset | Determine the offset of the records. |

## Output

| Output fields | Description |
| --- | --- |
| Message type | Type of the message. |
| Total records | Total number of records uploaded. |
| Offset | Offset of the records to be returned. This number must be equal or greater than zero. |
| Limit | Number of records to fetch per request. This number should be less than or equal to the configured quota on the API side, which is `1000`. |
| Transaction ID | Unique ID of the transaction. |
| Processor name | Name of the processor. |
| Report status | Indicates whether the status is completed or failed. |
| Success records | Number of successful records in the current page. |
| Failed records | Number of failed records in the current page. |
| Merchant data | An array of merchant data outbound objects containing the status response details. |
| Acquirer BIN | Acquirer reference ID number. |
| Acquirer CID | Acquirer company ID. |
| Acquirer ICA | Acquirer ICA number. |
| Acquirer name | The acquirer name. |
| Merchant ID | Acquirer merchant ID. |
| Merchant name | Name of the merchant. |
| Identity check express | Flag for Identity Check Express. Valid values are `Y` or `N`. |
| Delete reason | Reason for deleting the merchant enrollment. Only required if the selected action is delete. |
| Status | Status of the record. This is either `Successful` or `Rejected`. |
| Reason | Contains either new record data for successful merchant enrollment or the reason for failure for rejected records. |

---
