---
url: 'https://docs.workato.com/en/connectors/google-vision.md'
description: >-
  The Google Vision connector lets you automate image analysis: read and extract
  printed text from images in your recipes.
---

# Google Vision

[Google Vision](https://cloud.google.com/vision) uses machine learning to get insight from your images. It quickly classifies images into thousands of categories, detects individual objects and faces in images, and reads printed words contained in images. You can build metadata on your image catalog, moderate offensive content, or enable new marketing scenarios by using image sentiment analysis.

Workato's Google Vision connector allows you to build powerful automations and connect with other applications.

> **FEATURE AVAILABILITY**
> 
> The Google Vision connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The Google Vision connector uses [Google Cloud Vision API v1](https://cloud.google.com/vision/docs/reference/rest/).

## How to connect to Google Vision on Workato

Google Vision uses OAuth 2.0 for authentication.

Complete the following steps to establish a connection to Google Vision in Workato:

1. Search for and select `Google Vision` as your connection on the **New connection** page.
   
2. Enter a name for your connection in the **Connection name** field.
   
   ![Connection setup](/assets/connection-setup.Dvkd0H4i.png)_Google vision connection setup_
   
3. Select the project or folder where you plan to store the connection from the **Location** drop-down menu.
   
4. Click **Sign in with Google**.
   
5. Click **Allow** when prompted to authorize Workato to access your Google account.

---
