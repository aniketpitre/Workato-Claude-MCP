---
url: 'https://docs.workato.com/en/accelerator-aiml-connections.md'
description: >-
  Set up the connections for the AIML accelerator, including the API client and
  connections to Amazon SageMaker and Amazon S3.
---

# AIML accelerator connections

Connect your applications.

## AIML connector

To connect with the AIML accelerator, you must set up an API Client. You can create a new API client or configure an existing API client.

1. Sign in to your Workato account.
   
2. Go to **API Platform > Clients** in the navigation sidebar.
   
3. If you do not have an existing API client, click **Add New Client**.
   
   If you already have an API client, you can skip to step 5.
   
4. In the **Add new client** interface, enter a **Name**, **Description**, and **Client logo** (optional).
   
5. Configure the client's access configuration.
   
   ![New access profile](/assets/new-access-profile.DHhIKB78.png)
   
   <dl><dt>Authentication method</dt><dd>Select <strong>Auth Token</strong>.</dd><dt>API collections to include</dt><dd>Add <strong>AIML Accelerator</strong> into <strong>API collections</strong>.</dd><dt>Policy</dt><dd>Set to the maximum. You can skip this step if you want to refrain from enforcing any policies.</dd></dl>
   
6. Click **Next**, then [create a new API key](/en/api-mgmt/api-client-mgmt#create-a-new-application) for the client.
   
7. Enter a descriptive **API key name** and, optionally, restrict access with **Allowed IPs**.
   
8. Click **Next**. The AIML accelerator API key appears.
   
9. Navigate to **Projects > Home > AIML Accelerator > API Endpoints**.
   
10. Start all recipes in this folder.
    
11. Navigate to **API Platform > API Collections > AIML Accelerator**.
    
12. Activate all API endpoints.
    
13. Navigate to **Projects > Home > AIML Accelerator > Connections**.
    
14. To connect your AIML Accelerator SDK, enter your **API key** and **domain** (base URL).
    
    ![Enter your API key and base URL](/assets/connect-sdk.8GSwNyrD.png)_Enter your API token and base URL_
    
15. <dl><dt>API key</dt><dd><ol><li>In Workato, use the sidebar to navigate to <strong>API platform &gt; Clients &gt; [Client Name] &gt; API keys</strong>.</li><li>Copy the <strong>API key</strong>.</li></ol></dd><dt>Domain</dt><dd>The domain consists of two parts you must customize, your team name and API collection path.</dd><dd><dl class="horizontal-dl"><dd><ol><li>To find the domain, navigate to <strong>API Collections &lt; Select Collection Name &lt; Settings &lt; URL Settings</strong> copy <strong>Collection Path Preview</strong>.</li><li>Remove the prefix: <code>https://</code> and suffix: <code>endpoint_path</code>.</li><li>The final result looks like this:<pre><code>apim.workato.com/accelerators-dev/aiml-accelerator-v1/</code></pre></li></ol></dd></dl></dd></dl>
    

## Connect to Sagemaker

Use your AWS credentials to connect to Sagemaker.

1. In Workato, Navigate to **Projects > AIML Accelerator/Connections > AIML|CON-002|SageMaker**.
   
2. Configure the **AIML|CON-002|SageMaker** interface, entering your **Access key ID**, **Access key secret**, **AWS region**.
   
   ![Enter your Sagemaker credentials](/assets/connect-sagemaker.DbfnBqUG.png)_Enter your Sagemaker credentials_
   
   <dl><dt>Access key ID</dt><dd>Enter your access key.</dd><dt>Access key secret</dt><dd>Provide your access key secret.</dd><dt>AWS region</dt><dd>Provide your AWS region, such as <code>us-west</code>.</dd></dl>
   

## Connect to AWS S3

Use your AWS credentials to connect to AWS S3.

1. In Workato, navigate to **Projects > AIML Accelerator/Connections > AIML|CON-003|Amazon S3**.
   
2. Configure the **AIML|CON-003|Amazon S3** interface.
   
   ![Enter your AWS credentials](/assets/connect-aws2.DpAsrbCQ.png)_Enter your credentials_
   
   <dl><dt>Authorization type</dt><dd>Enter your authorization type.</dd><dt>Restrict to bucket</dt><dd>Restrict connection to a specific bucket. Required when a user has only limited <code>s3:ListBucket</code> access</dd><dt>Region</dt><dd>The region is typically provided in the S3 account. If your account URL is <code>https://eu-west-1.console.s3.amazon.com</code>, use <code>eu-west-1</code> as the region.</dd><dt>Download threads</dt><dd>Use to boost download speed. The default is 1, max is 20.</dd></dl>

---
