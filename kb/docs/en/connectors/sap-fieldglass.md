---
url: 'https://docs.workato.com/en/connectors/sap-fieldglass.md'
description: >-
  The SAP Fieldglass connector enables you to automate external workforce and
  services procurement workflows in this cloud-based vendor management system.
---

# SAP Fieldglass

[SAP Fieldglass](https://www.sap.com/products/acquired-brands/what-is-fieldglass.html) is a cloud-based vendor management system (VMS) designed to help businesses manage their external workforce and services procurement. It is part of the SAP family of enterprise solutions.

## Prerequisites

Before using the SAP Fieldglass connector in Workato, ensure you have an active SAP Fieldglass account with appropriate permissions to access APIs.

1. [Register an application in SAP Fieldglass](#register-an-application-in-sap-fieldglass)
2. [Generate an API key](#generate-an-api-key)

### Register an application in SAP Fieldglass

Suppliers can register new supplier accounts after the registration email has been received from the buyer company.

Register an application in SAP Fieldglass

1. Copy the temporary registration code in the first email.
   
2. Select the link in the second email to go to the SAP Fieldglass website.
   
3. Paste the temporary registration code into the **Registration Code** field, and select **Next**.
   
4. Enter a **Username** and **Password**, and re-enter the password. Specify user preferences.
   
5. Review all of the fields and update any that aren’t accurate.
   
6. Select **Sign In**. The SAP Fieldglass home page displays.
   

Refer to the [SAP Fieldglass help](https://help.sap.com/docs/SAP_Fieldglass/966d9b18b66c4304b9d585884f7b0931/8d8700fdc42644f89de2d487f2ad10f7.html) page for more information.

### Generate an API key

[Generate an API key](https://www.servicenow.com/docs/bundle/xanadu-integrate-applications/page/administer/integrationhub-store-spokes/task/generate-api-key.html) on the SAP Fieldglass tenant to enable your ServiceNow instance to connect to the SAP Fieldglass tenant.

Generate an API key

1. Sign in to your SAP Fieldglass tenant account.
   
2. Select **Linked Accounts**. ![Linked accounts](/assets/sap-fieldglass-spoke-linked-account.CkVResL3.png)_Linked accounts_
   
3. On the **Self-Service Dashboard**, select the **API Application Keys** card. ![Configuration tools](/assets/sap-fieldglass-spoke-application-keys-card.CDNknj22.png)_Configuration tools_
   
4. Select **New**. ![New button](/assets/sap-fieldglass-spoke-new-button.DuwaMv_H.png)_New button_
   
5. On the **Create Application Key** page, enter the following values:
   
   1. **Application Name**: Provide the name of the application.
      
   2. **Description**: Provide a custom description of the API key.
      
6. Select **Create**. ![API key](/assets/sap-fieldglass-spoke-api-key-details.BnkFOf05.png)_API key_
   
7. The API key and other details are generated. The API key, client ID, and client secret are required to establish a connection to Workato. ![API key](/assets/sap-fieldglass-spoke-api-key-generated.CnuBKtXh.png)_API key_
   

## How to connect to SAP Fieldglass

Connecting to the SAP Fieldglass involves the following steps:

1. [Download the SAP Fieldglass from the community](#community-download)
2. [Complete setup in Workato](#workato-setup)

### Download the SAP Fieldglass from the community

Complete the following steps to install the SAP Fieldglass connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### Complete setup in Workato

Complete the following steps to establish a connection to SAP Fieldglass in Workato:

1. Click **Create > Connection** or press C+C.
   
2. Search for and select `SAP Fieldglass` as your connection on the New connection page.
   
3. Provide a unique name for your connection in the **Connection name** field.
   
4. Enter the **Username** for your SAP Fieldglass.
   
5. Enter the **Password** for your SAP Fieldglass.
   
6. Provide the **API Key** generated on the SAP Fieldglass tenant.
   
7. Provide the **Client ID** generated on the SAP Fieldglass tenant.
   
8. Provide the **Client Secret** generated on the SAP Fieldglass tenant.
   
9. Enter the **Server URL** for your SAP Fieldglass instance.
   
10. Click **Connect**.
    
    ![Connection to SAP Fieldglass](/assets/sap-fieldglass-connection.bmKfeyHS.png)_Connection to SAP Fieldglass_

---

---
url: >-
  https://docs.workato.com/en/connectors/sap-fieldglass/active-worker-delta-single-line-download-action.md
description: >-
  The Active worker delta single line download action enables you to download
  worker data for workers who have had revisions since the last successful
  connector run date.
---

# SAP Fieldglass - Active worker delta single line download action

The **Active worker delta single line download** action enables you to download worker data for workers who have had revisions since the last successful connector run date.

![Active worker delta single line download](/assets/sap-fieldglass-active-worker-delta-download-action.DZQxpIJe.png)_Active worker delta single line download action_

## Input

You can specify the [custom fields](https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION/9cfd5c12ee3046d59453e73974f9c4b7/da87d14e8f5c48ebb7a76aba0afcb25e.html?locale=en-US#custom-fields) that you plan to include in the result and the order that you wish to see in the result.

## Output

| Output fields | Description |
| --- | --- |
| Job seeker ID | SAP Fieldglass job seeker ID. |
| Worker ID | SAP Fieldglass worker ID. |
| Person ID | Unique identifier for the worker as a person. |
| Security ID | This column only appears in the file if the security ID field functionality is activated in SAP Fieldglass for the buyer. If the functionality is not activated, this column isn't in the file. |
| Status | Status of the worker (active, closed, or withdrawn). |
| First name | First name of the worker as defined in SAP Fieldglass. |
| Last name | Last name of the worker as defined in SAP Fieldglass. |
| Worker email | Worker’s e-mail address. |
| Job posting title | Job posting’s title or SOW Name (if an SOW Worker). |
| Work order ID | Work order ID. |
| Work order/work order revision owner | Work order owner’s name. |
| Work order/work order revision owner employee ID | Work order owner employee ID. |
| Business unit code | Business unit code. |
| Business unit name | Business unit name. |
| Vendor number | Fieldglass supplier code. |
| Vendor name | Supplier name. |
| Buyer code | Buyer company code. |
| Remit to address code | Code as assigned to the RTA by the supplier. |
| Cost center name | Cost center name in SAP Fieldglass. This is the primary cost center only. |
| Cost center code | Cost center code in SAP Fieldglass. This is the primary cost center only. |
| Billable per diem | Billable amount. |
| Start date | Work order start date. |
| End date | Work order end date. |
| Currency | Currency designation (USD). |
| Site code | Site code. |
| Site name | Site name. |
| Pay rate | Pay rate |
| Rate category/UOM | Rate category/UOM. |
| Bill rate | The billing rate. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sap-fieldglass/active-worker-download-action.md
description: >-
  The Active worker download action enables you to worker data for currently
  active workers from SAP Fieldglass.
---

# SAP Fieldglass - Active worker download action

The **Active worker download** action enables you to worker data for currently active workers from SAP Fieldglass.

![Active worker download action](/assets/sap-fieldglass-active-worker-download-action.BBO6bBxJ.png)_Active worker download action_

## Input

You can specify the [custom fields](https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION/9cfd5c12ee3046d59453e73974f9c4b7/5cbd340eaa474a5e9c30cd59c56d01be.html?locale=en-US#custom-fields) that you plan to include in the result and the order that you plan to see in the result.

## Output

| Output fields | Description |
| --- | --- |
| Job seeker ID | SAP Fieldglass job seeker ID. |
| Worker ID | SAP Fieldglass worker ID. |
| Person ID | Unique identifier for the worker as a person. |
| Security ID | This column only appears in the file if the security ID field functionality is activated in SAP Fieldglass for the buyer. If the functionality is not activated, this column isn't in the file. |
| Status | Status of the worker (active, closed, or withdrawn). |
| First name | First name of the worker as defined in SAP Fieldglass. |
| Last name | Last name of the worker as defined in SAP Fieldglass. |
| Worker email | The worker’s e-mail address. |
| Job posting title | Job posting’s title or SOW Name (if an SOW Worker). |
| Work order ID | Work order ID. |
| Work order/work order revision owner | Work order owner’s name. |
| Work order/work order revision owner employee ID | Work order owner employee ID. |
| Business unit code | Business unit code. |
| Business unit name | Business unit name. |
| Vendor number | Fieldglass supplier code. |
| Vendor name | Supplier name. |
| Buyer code | Buyer company code. |
| Remit to address code | Code as assigned to the RTA by the supplier. |
| Cost center name | Cost center name in SAP Fieldglass. This is the primary cost center only. |
| Cost center code | Cost center code in SAP Fieldglass. This is the primary cost center only. |
| Billable per diem | Billable amount. |
| Start date | Work order start date. |
| End date | Work order end date. |
| Currency | Currency designation (USD). |
| Site code | Site code. |
| Site name | Site name. |
| Pay rate | Pay rate. |
| Rate category/UOM | Rate category/UOM. |
| Bill rate | The billing rate. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sap-fieldglass/active-worker-single-line-download-action.md
description: >-
  The Active worker single line download action enables you to download active
  worker details in a single-line format from SAP Fieldglass.
---

# SAP Fieldglass - Active worker single line download action

The **Active worker single line download** action enables you to download active worker details in a single-line format from SAP Fieldglass.

![Active worker single line download action](/assets/sap-fieldglass-active-worker-single-action.B1RRAqgX.png)_Active worker single line download action_

## Input

You can specify the [custom fields](https://help.sap.com/docs/SAP_FIELDGLASS_INTEGRATION/9cfd5c12ee3046d59453e73974f9c4b7/9d453f6729274f708def45d1df02b820.html?locale=en-US#custom-fields) that you plan to include in the result and the order that you plan to see in the result.

## Output

| Output fields | Description |
| --- | --- |
| Job seeker ID | SAP Fieldglass job seeker ID. |
| Worker ID | SAP Fieldglass worker ID. |
| Person ID | Unique identifier for the worker as a person. |
| Security ID | This column only appears in the file if the security ID field functionality is activated in SAP Fieldglass for the buyer. If the functionality isn't activated, this column isn't in the file. |
| Status | Status of the worker (Active or closed or withdrawn). |
| First name | First name of the worker as defined in SAP Fieldglass. |
| Last name | Last name of the worker as defined in SAP Fieldglass. |
| Worker email | Worker’s e-mail address. |
| Job posting title | Job posting’s title or SOW Name (if an SOW Worker). |
| Work order ID | Work order ID. |
| Work order/work order revision owner | Work order owner’s name. |
| Work order/work order revision owner employee ID | Work order owner employee ID. |
| Business unit code | Business unit code. |
| Business unit name | Business unit name. |
| Vendor number | Fieldglass supplier code. |
| Vendor name | Supplier name. |
| Buyer code | Buyer company code. |
| Remit to address code | Code as assigned to the RTA by the supplier. |
| Cost center name | Cost center name in SAP Fieldglass. This is the primary cost center only. |
| Cost center code | Cost center code in SAP Fieldglass. This is the primary cost center only. |
| Billable per diem | Billable amount. |
| Start date | Work order start date. |
| End date | Work order end date. |
| Currency | Currency designation (USD). |
| Site code | Site code. |
| Site name | Site name. |
| Pay rate | Pay rate. |
| Rate category/UOM | Rate category/UOM. |
| Bill rate | Bill rate. |

---
