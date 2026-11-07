---
url: >-
  https://docs.workato.com/en/security/data-protection/secrets-management/google-service-account-setup.md
description: >-
  Learn how to create a Google Cloud service account and generate the JSON key
  file Workato needs to connect to Google Secret Manager.
---

# Set up a Google Cloud service account

This guide explains how to create a Google Cloud service account and generate credentials that allow Workato to access secrets in Google Secret Manager.

## Prerequisites

Ensure you have the following before you begin:

- An active Google Cloud project (GCP project) with billing enabled
  
- The following IAM permissions in your GCP project:
  
  - `serviceusage.services.enable`
  - `iam.serviceAccounts.create`
  - `iam.serviceAccountKeys.create`
  - `resourcemanager.projects.setIamPolicy`

## Enable the Secret Manager API

Complete the following steps to enable the Secret Manager API in your GCP project:

1. Sign in to the [Google Cloud Console](https://console.cloud.google.com/) and select your project.
   
2. Go to **APIs & Services > Library**.
   
3. Search for and select `Secret Manager API`.
   
4. Click **Enable**.
   
   ![Enable the Secret Manager API](/assets/enable-api.DO7pnAp3.png)_Enable the Secret Manager API_
   

## Create a service account

Complete the following steps to create a Google Cloud service account:

1. Go to **IAM & Admin > Service Accounts**.
   
2. Click **Create Service Account**.
   
3. Enter a descriptive **Service account name**. For example, `Workato Secrets Manager`. The **Service account ID** is auto-generated from the name.
   
4. Optionally, enter a **Service account description**. For example, `Service account for Workato to access Secret Manager`.
   
   ![Create the service account](/assets/create-service-account.C5Ci8f7A.png)_Create the service account_
   
5. Click **Create and continue**.
   

## Assign the Secret Manager IAM roles

Complete the following steps to grant the service account permission to access secrets in your project. The service account requires two roles:

- **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`)
- **Secret Manager Viewer** (`roles/secretmanager.viewer`)

1. Click the **Select a role** drop-down menu in the **Permissions** section.
   
2. Search for and select **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`).
   
3. Click **\+ Add another role**.
   
4. Search for and select **Secret Manager Viewer** (`roles/secretmanager.viewer`).
   
   ![Select the Secret Manager Secret Accessor permission](/assets/secret-manager-permission.BvFj_PTq.png)_Select the Secret Manager Secret Accessor permission_
   
5. Click **Continue**.
   
6. Click **Done** to skip the optional **Principals with access** section.
   

## Create and download a service account key

Complete the following steps to generate a JSON key file that Workato uses to authenticate as the service account:

1. Locate the service account you just created on the **Service Accounts** page.
   
2. Click the service account email address to open its details.
   
3. Click the **Keys** tab.
   
4. Click **Add Key > Create new key**.
   
5. Select **JSON** as the key type.
   
6. Click **Create**.
   

The JSON key file downloads automatically. The file contains the credentials Workato needs to authenticate to Google Secret Manager, including `project_id`, `private_key`, and `client_email`. Store the file securely and restrict access.

## Next steps

Refer to the following guides to complete the setup:

- [Set up Google Secret Manager for your workspace](/en/security/data-protection/secrets-management/setting-up-workspace-level-google-secret-manager)
- [Set up Google Secret Manager for a project](/en/security/data-protection/secrets-management/setting-up-project-level-google-secret-manager)

## Further reading

- [Google Cloud Service Accounts documentation](https://cloud.google.com/iam/docs/service-accounts)
- [Secret Manager IAM roles and permissions](https://docs.cloud.google.com/secret-manager/docs/access-control)
- [Best practices for managing service account keys](https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)
