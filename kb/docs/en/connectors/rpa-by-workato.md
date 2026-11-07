---
url: 'https://docs.workato.com/en/connectors/rpa-by-workato.md'
description: >-
  The RPA by Workato connector lets you start automation jobs, get job and
  process details, retrieve job logs, and list departments and processes.
---

# RPA by Workato

Robotic Process Automation (RPA) uses bots to automate repetitive, rules-based tasks. RPA bots can learn to perform tasks such as data entry, web scraping, content tagging, and spreadsheet updates by interacting with a computer screen the same way a human does. By automating these tasks, RPA reduces human errors and boosts efficiency.

RPA by Workato is a complete RPA solution in partnership with [Robotiq.ai](https://robotiq.ai/), an industry-agnostic, enterprise-ready RPA client. You can use the RPA by Workato connector to integrate with applications that don't have APIs, including legacy systems such as older SAP platforms, desktop applications, and browser apps without API support. Contact your Workato Customer Success Representative for more information.

> **RPA BY WORKATO TUTORIALS**
> 
> For detailed tutorials and guides on building RPA automations, visit [rpabyworkato.com](https://rpabyworkato.com/).

## Key features

The RPA by Workato connector offers the following key features:

- UI recorder
  
- Record automation scenarios to generate step-by-step outputs, making them easy to create and manage. This feature allows you to capture your interactions with the user interface, which can then be replayed to automate repetitive tasks.
  
- Script support
  
- Create automations with scripting languages such as Visual Basic. This provides flexibility and control over automation processes, enabling you to script complex tasks that might not be easily handled through a graphical interface.
  
- Low code/No code interface
  
- A cloud-based drag-and-drop interface enables you to automate, monitor, and refine processes. This interface is designed to allow non-technical users to create automation workflows without writing code.
  
- Excel file operations
  
- RPA offers built-in support for operations on Excel files, such as reading, updating, and manipulating data. This capability is essential for automating tasks that involve handling large volumes of spreadsheet data, ensuring accuracy and efficiency in data processing.
  

## How to connect to RPA by Workato

Connecting to RPA by Workato consists of the following steps:

1. [Generate an access token in Robotiq](#access-token)
2. [Complete setup in Workato](#setup)

> **PREREQUISITES**
> 
> You must [create processes in Robotiq](https://docs.robotiq.ai/en/article/processes) before you can start or manage them using the connector.

### Generate an access token

Complete the following steps to generate an access token in Robotiq:

1. Sign in to your Robotiq.ai account.
   
2. Go to the **Applications** page.
   
3. Click **New application** to open the **Register new applications** dialog. ![Click New application](/assets/new-application.C7kRUhwa.png)_Click **New application**._
   
4. Enter a name and description for the access token. ![Register new applications dialog](/assets/register-new-applications.B7J_yqNB.png)_The **Register new applications** dialog_
   
5. Set the **Scope** to **job\_create**, then click **Confirm**.
   
6. Click **Get access token** to view your token's details. ![Click Get access token](/assets/get-access-token.2jfcPNDK.png)_Click **Get access token**._
   
7. Retrieve the following values from your token for later use in configuring RPA by Workato:
   
   - **Client ID**.
     
   - **Client secret**. After 30 minutes, the **Client secret** expires, and Robotiq.ai generates a new secret.
     
   - **Tenant name**. The **Tenant name** can be found in the **POST** URL between `/realms/` and `/protocol/`. The **Tenant name** in the following example is `testName`:
     
   
   ```
   https://auth.robotiq.ai/realms/testName/protocol/openid-connect/token
   ```
   

Return to Workato to finish setting up your connection.

### Complete setup in Workato

Complete the following steps to configure the connection to RPA by Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `RPA by Workato` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![RPA by Workato's connection fields](/assets/rpa-connection-fields.Df-vUE_C.png)_RPA by Workato's connection fields_
   
4. Provide your application's **Tenant name**.
   
5. Provide your application's **Client ID**.
   
6. Provide your application's **Client secret**. This value expires 30 minutes after it is generated in Robotiq.ai.
   
7. Click **Connect** to complete the setup.
   

## Actions

RPA by Workato supports the following actions:

- [Get job detail](/en/connectors/rpa-by-workato/get-job-detail)
- [Get job logs (batch)](/en/connectors/rpa-by-workato/get-job-logs-batch)
- [Get process details](/en/connectors/rpa-by-workato/get-process-details)
- [List departments (batch)](/en/connectors/rpa-by-workato/list-departments-batch)
- [List processes by department (batch)](/en/connectors/rpa-by-workato/list-processes-by-department-batch)
- [Start job](/en/connectors/rpa-by-workato/start-job)

---
