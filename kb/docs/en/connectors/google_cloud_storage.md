---
url: 'https://docs.workato.com/en/connectors/google_cloud_storage.md'
description: >-
  The Google Cloud Storage connector lets you manage object storage: create and
  list buckets, and upload, download, and delete objects.
---

# Google Cloud Storage

[Google Cloud Storage](https://cloud.google.com/storage) is a RESTful online storage service for securely storing and accessing data on the Google Cloud Platform infrastructure.

> **FEATURE AVAILABILITY**
> 
> The Google Cloud Storage connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

This connector uses the [Cloud Storage JSON API v1](https://cloud.google.com/storage/docs/json_api).

> **ENABLE THE GOOGLE CLOUD STORAGE API**
> 
> Ensure the Google Cloud Storage API is enabled in the Google Cloud Console. If the API isn’t already enabled, refer to the [Google Cloud documentation](https://cloud.google.com/endpoints/docs/openapi/enable-api) for instructions on how to enable it in your project.
> 
> ![Enable Google Cloud Storage API in the Google Cloud Platform](/assets/enable-gcs-api-on-gcp.NSd7M5a6.png)_Enable Google Cloud Storage API in the Google Cloud Platform_

## How to connect to Google Cloud Storage

The Google Cloud Storage connector supports service account authentication.

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

### Create a service account

Complete the following steps to set up a Google service account:

1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
   
2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account.
   
   ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
   
3. Click the **Email** of the service account you intend to use.
   
   ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
   
4. Copy the service account's **Email** and save it to configure your connection later.
   
   ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
   
5. Go to the **KEYS** tab.
   
6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
   
7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
   

Enable the Google Cloud Storage API, then return to Workato to finish setting up your connection.

> **PERMISSIONS**
> 
> Your service account must have one of the following roles:
> 
> - **Storage Admin** (recommended for full access to actions and triggers)
> - Storage Object Admin
> - Storage Object Viewer Connecting without these roles can prevent you from establishing a connection successfully.
> 
> Refer to the [Permissions](#permissions) section for more information.

### Connect to Workato

1. Sign in to Workato and select the project where you plan to create your connection.
   
2. Click **Create > Connection** or press C twice.
   
3. Search for and select `Google Cloud Storage` on the **New connection** page.
   
4. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Google Cloud Storage](/assets/connect.DN7RNrmu.png)_Connect to Google Cloud Storage_
   
5. Use the **Location** drop-down menu to select the project where you plan to store this connection.
   
6. Enter a valid Google Cloud Platform project ID in the **Project identifier** field. You can find the project ID in the [Google Cloud Console](https://console.cloud.google.com) by clicking **Select a project** in the navigation menu.
   
7. Enter the email address of the service account in the **GCS Project service account email** field.
   
8. Provide the private key from the downloaded JSON file in the **Private key** field.
   
   > **PRIVATE KEY**
   > 
   > You must copy the private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----`.
   
9. Optional. Enter a comma-separated list of buckets the connection can access in the **Restrict to bucket** field. For example, `bucket-1,bucket2`.
   
10. Optional. Expand **Advanced settings** and use the **Requested permissions (OAuth scopes)** drop-down menu to select the permissions to request for this connection.
    
11. Click **Sign in with Google**.
    

## Permissions

The recommended service account role for using all actions and triggers is **Storage Admin**.

To limit the available actions for your Google Cloud Storage connection, you can select a role with a narrower scope:

- **Storage Object Admin**: Quotas actions to Google Cloud Storage objects.
- **Storage Object Viewer**: Restricts actions to viewing and downloading Google Cloud Storage objects only.
- **Custom role**: Use [custom roles](https://cloud.google.com/iam/docs/creating-custom-roles) to define specific permissions for your Google Cloud Storage connection.

The following permissions are required to enable all actions and triggers:

- firebase.projects.get
- resourcemanager.projects.get
- resourcemanager.projects.list
- storage.buckets.create
- storage.buckets.createTagBinding
- storage.buckets.delete
- storage.buckets.deleteTagBinding
- storage.buckets.get
- storage.buckets.getIamPolicy
- storage.buckets.list
- storage.buckets.listTagBindings
- storage.buckets.setIamPolicy
- storage.buckets.update
- storage.multipartUploads.abort
- storage.multipartUploads.create
- storage.multipartUploads.list
- storage.multipartUploads.listParts
- storage.objects.create
- storage.objects.delete
- storage.objects.get
- storage.objects.getIamPolicy
- storage.objects.list
- storage.objects.setIamPolicy
- storage.objects.update

However, during connection setup, Workato retrieves all buckets associated with the project. Therefore, the minimum required permission to establish a connection is `storage.buckets.list`.

Refer to [IAM permissions for Cloud Storage](https://cloud.google.com/storage/docs/access-control/iam-permissions) for more information.

> **INSUFFICIENT PRIVILEGES**
> 
> Actions for this connector return an access error if the connection attempts to retrieve or update a resource beyond the access that is provided.

## More resources

- [Create bucket](/en/connectors/google_cloud_storage/create-bucket)
- [Delete bucket](/en/connectors/google_cloud_storage/delete-bucket)
- [Delete object](/en/connectors/google_cloud_storage/delete-object)
- [Download object](/en/connectors/google_cloud_storage/download-object)
- [Get bucket](/en/connectors/google_cloud_storage/get-bucket)
- [List buckets](/en/connectors/google_cloud_storage/list-buckets)
- [List objects](/en/connectors/google_cloud_storage/list-objects)
- [Update bucket](/en/connectors/google_cloud_storage/update-bucket)
- [Update object metadata](/en/connectors/google_cloud_storage/update-object-metadata)
- [Upload object with file streaming](/en/connectors/google_cloud_storage/upload-object-with-file-streaming)

---
