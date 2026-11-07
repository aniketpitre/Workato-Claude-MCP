---
url: 'https://docs.workato.com/en/connectors/walmart-seller-center.md'
description: >-
  The Walmart Seller Center connector enables you to automate e-commerce
  workflows, managing product listings, inventory, orders, and fulfillment on
  Walmart.
---

# Walmart Seller Center

[Walmart Seller Center](https://marketplace.walmart.com/about-walmart-marketplace/) is a platform that enables businesses to sell products on Walmart.com. Use this connector to manage product listings, track inventory, process customer orders, and utilize Walmart's fulfillment services.

## Prerequisites

Before using the Walmart Seller Center connector in Workato, ensure you have an active account with appropriate permissions to access APIs. If you don't already have an account, complete the following steps to register for one.

1. [Register for a Walmart Seller Center account](#register-account)
2. [Retrieve an API key](#retrieve-key)

### Register for a Walmart Seller Center account

Complete the following steps to register for a new supplier account in the Walmart Seller Center:

1. Visit the [registration](https://seller.walmart.com/signup?locale=en-US) page.
   
2. Enter details in each field as required.
   
3. Click the checkbox at the bottom of the form to agree to the terms and conditions.
   
4. Click **Create account**.
   

After creating your account, you are redirected to the [Seller Center](https://seller.walmart.com/home) page. Check your email for your portal login credentials.

For more information, refer to the [Walmart Seller help](https://sellerhelp.walmart.com/s/?language=en_US&kb=1) page.

### Retrieve an API key

Complete the following steps to retrieve an API key from the [Developer Portal](https://developer.walmart.com/) of your Walmart Seller Center account:

1. Sign in to your Seller Center account.
   
2. Click the grid on the navigation menu and select **Developer Portal**.
   
   ![Walmart Developer Portal](/assets/walmart-developer-portal.oFu9P1Q7.png)_Walmart Developer Portal_
   
3. In the developer portal, navigate to the taskbar in the top right corner and select **My Account**.
   
4. Select the applicable login type.
   
   ![Walmart Login](/assets/walmart-login.BSDLRIHD.png)_Walmart Login_
   
5. Locate the **My API Key** section and copy the **Client ID** and **Client Secret**. These values are required to establish the connection in Workato.
   
   ![Walmart Credentials](/assets/walmart-credentials.C-nc-baH.png)_Walmart Credentials_
   

## How to connect to Walmart Seller Center

The Walmart Seller Center connector supports client credentials grant authentication. Complete the following steps to connect to the Walmart Seller Center connector in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Walmart Seller Center** as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Walmart Connection Setup](/assets/walmart-connection-setup.GG9Enkxj.png)_Walmart Connection Setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client ID** for your Walmart Seller Center account, which you saved during the previous steps.
   
6. Enter the **Client Secret** for your Walmart Seller Center account, which you saved during the previous steps.
   
7. Optional. Provide your **Walmart Seller/Supplier ID**, which can be retrieved by navigating to **Settings** on the home page of your Walmart account. On the settings page, you can copy the ID present in the top left corner under your name.
   
8. Optional. Provide your **Walmart marketplace**.
   
9. Provide the **Walmart service name**. For example, `Walmart fulfillment service`.
   
10. Click **Connect**.
    

## Actions

The Walmart Seller Center connector supports the following actions:

- [Bulk update inventory](/en/connectors/walmart-seller-center/bulk-update-inventory-action)
- [Get record details by ID](/en/connectors/walmart-seller-center/get-record-details-by-id-action)
- [Search records](/en/connectors/walmart-seller-center/search-records-action)
- [Update record](/en/connectors/walmart-seller-center/update-record-action)

![Walmart Seller Center connector actions](/assets/walmart-actions.yeOBLUP2.png)_Walmart Seller Center connector actions_

---

---
url: >-
  https://docs.workato.com/en/connectors/walmart-seller-center/bulk-update-inventory-action.md
description: >-
  The Bulk update inventory action enables you to update details of multiple
  items existing in an inventory in a single call.
---

# Walmart Seller Center - Bulk update inventory action

The **Bulk update inventory** action enables you to update the details of multiple inventory items in a single call.

## Input

| Input field | Description |
| --- | --- |
| Feed type | Select the feed type that you plan to update. This can be an inventory or a multi-node inventory. |
| File name | Enter the name of the file you plan to upload. |
| MIME-type | Specify the mime type of the file to upload. Must be a JSON extension. |
| File content | Provide the file content of the file to upload in binary raw format. |

## Output

| Output field | Description |
| --- | --- |
| Completed | Returns true if the action ran successfully. Else, returns false. |
| Feed ID | A unique ID used to track the feed file. |
| Feed status | Status of the feed file. Can be one of the following: `RECEIVED`, `INPROGRESS`, `PROCESSED`, or `ERROR`. |
| Feed submission date | Timestamp of when the feed file was submitted. |
| Items succeeded | The number of items in the feed that were processed successfully. |
| Items failed | The number of items in the feed that failed due to a data or system error. |
| Items processing | The number of items in the feed that are still processing. |
| Limit | The number of items returned. The maximum quota is 1000. |
| Offset | The object responds to the starting number, where 0 is the first entity available for request. |
| Mart ID | Mart ID that a user or seller uses for a marketplace. |
| SKU | An arbitrary alphanumeric unique ID, seller-specified, identifies each item. |
| WPID | An alphanumeric product ID that is generated by Walmart. |
| Index | Index of items in the feed. |
| Item ID | Unique ID of the item. |
| Ingestion status | Data ingestion status. Can be one of the following: `DATA_ERROR`, `SYSTEM_ERROR`, `TIMEOUT_ERROR`, or `INPROGRESS`. |
| Product ID type | ID of the product type. |
| Product ID | ID of the product. |

---

---
url: >-
  https://docs.workato.com/en/connectors/walmart-seller-center/get-record-details-by-id-action.md
description: >-
  The Get Record Details by ID action enables you to retrieve details of a
  specific record in the Walmart Seller Center.
---

# Walmart Seller Center - Get record details by ID action

The **Get record details by ID** action enables you to retrieve details of a specific record in the Walmart Seller Center.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object whose details you plan to retrieve. Fields load dynamically based on the object you select. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/walmart-seller-center/search-records-action.md
description: >-
  The Search records action enables you to retrieve a list of records that match
  your search criteria in the Walmart Seller Center.
---

# Walmart Seller Center - Search records action

The **Search records** action enables you to retrieve a list of records that match your search criteria in the Walmart Seller Center.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to search. Fields load dynamically based on the object you select. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

---

---
url: >-
  https://docs.workato.com/en/connectors/walmart-seller-center/update-record-action.md
description: >-
  The Update record action enables you to update the details of a specific
  record in the Walmart Seller Center.
---

# Walmart Seller Center - Update record action

The **Update record** action enables you to update the details of a specific record in the Walmart Seller Center.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object you plan to update. Fields load dynamically based on the object you select. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

---
