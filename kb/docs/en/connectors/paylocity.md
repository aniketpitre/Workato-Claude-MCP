---
url: 'https://docs.workato.com/en/connectors/paylocity.md'
description: >-
  Paylocity is a cloud-based HR and payroll platform. This connector helps you
  manage employees, deductions, taxes, and payroll data in Workato.
---

# Paylocity

[Paylocity](https://www.paylocity.com) is a cloud-based human capital management (HCM) and payroll platform that helps organizations manage employee data, payroll, benefits, and workforce processes. This connector enables you to read and manage employee, payroll, and tax records in Paylocity from your Workato recipes.

With this connector, you can:

- Retrieve the details of an employee, earning, deduction, local tax, or direct deposit record by ID
- Search for employees, earnings, deductions, local taxes, pay statement details, pay statement summaries, and company codes
- Create employee, earning, deduction, local tax, and onboarding records
- Update employee, earning, tax, emergency contact, employee benefit setup, and sensitive data records

## Supported objects

This connector supports the following objects:

- Employees
- Earnings
- Deductions
- Local taxes
- Direct deposits
- Primary and non primary state taxes
- Emergency contacts
- Employee benefit setup
- Sensitive data
- Onboarding
- Pay statement details and summaries
- Company codes

## Install Paylocity from the community library

Complete the following steps to install the Paylocity connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The Paylocity connector uses OAuth 2.0 client credentials authentication. Paylocity provides the secure client credentials and sets up the scope for your account.

### Paylocity setup

Complete the following steps to get your API credentials from Paylocity before you create a connection in Workato:

1. Contact Paylocity to request access to the Web Services API and have the `WebLinkAPI` scope configured for your account.
   
2. Obtain your **Client ID** and **Client Secret** from Paylocity. Paylocity provides these values when you sign up.
   
3. Note your Paylocity **Company ID**.
   

Refer to the [Paylocity API](https://developer.paylocity.com/integrations/docs/getting-started) documentation for more information.

### Connect to Paylocity using OAuth 2.0

Complete the following steps to connect to Paylocity in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Paylocity` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Paylocity connection setup](/assets/paylocity-connection-setup.DU1fPqw9.png)_Paylocity connection setup_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Enter your Paylocity **Client ID**.
   
6. Enter your Paylocity **Client Secret**.
   
7. Enter your Paylocity **Company ID**.
   
8. Use the **Environment** drop-down menu to select the environment your connection targets:
   
   - **Production** connects to `api.paylocity.com`.
   - **Sandbox** connects to `apisandbox.paylocity.com`.
9. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/paylocity/get-record-details-by-id-action.md
description: >-
  The Get record details by ID action retrieves the details of a specific record
  in Paylocity.
---

# Paylocity - Get record details by ID action

The **Get record details by ID** action retrieves the details of a record you specify in Paylocity.

## Input

Input fields are dynamically generated based on the object you select. The following field is common to all object types:

| Input field | Description |
| --- | --- |
| Object | Select the type of record to retrieve. Available objects are Employee, Earnings, Local tax, Direct deposit, and Deduction. |

## Output

Output fields are dynamically generated based on the object you select. Refer to the [Paylocity API](https://developer.paylocity.com/integrations/docs/getting-started) documentation for a complete list of output fields.

---
