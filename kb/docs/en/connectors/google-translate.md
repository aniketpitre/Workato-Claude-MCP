---
url: 'https://docs.workato.com/en/connectors/google-translate.md'
description: >-
  Translates an arbitrary text into any supported language using
  state-of-the-art Neural Machine Translation.
---

# Google Translate

[Google Translate](https://cloud.google.com/translate/) enables fast translation of any text into a wide range of supported languages using advanced Neural Machine Translation technology. It also offers language detection for cases where the source language is unknown. The underlying technology is continuously updated with enhancements from Google's research teams, leading to improved translations, as well as the addition of new languages and language pairs.

Workato's Google Translate connector allows you to build powerful automation and connect with other applications in the workflow.

> **FEATURE AVAILABILITY**
> 
> The Google Translate connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The Google Translate connector uses [Google Translation API v2](https://cloud.google.com/translate/docs/reference/rest).

## How to connect to Google Translate on Workato

Google Translate uses OAuth 2.0 for authentication.

Complete the following steps to establish a connection to Google Translate in Workato:

1. Search for and select the Google Translate connector.
   
2. Enter a name for your connection in the **Connection name** field.
   
   ![Connection setup](/assets/connection-setup.BrFBVCGx.png)_Google Translate connection setup_
   
3. Select the project or folder where you plan to store the connection from the **Location** drop-down menu.
   
4. Click **Sign in with Google**.
   
5. Click **Allow** when prompted to authorize Workato to access your Google account.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-translate/action-translate-text.md
description: Allows you to translate any text into another language.
---

# Google Translate - Translate text action

This action allows you to translate any text into another language. You can define the source language or let Google detect the source language automatically.

## Input

| Input field | Description |
| --- | --- |
| Text | Provide the text to translate. This field accepts a text datapill or raw text. |
| Target language | Specify the target language to translate to. |
| Source language | Optionally, specify the source language of the text. If left blank, Google automatically detects the language. |

## Output

| Output field | Description |
| --- | --- |
| Translated text | The text translated to the target language. |
| Detected source language | Source language of the text that Google automatically detected. |

---
