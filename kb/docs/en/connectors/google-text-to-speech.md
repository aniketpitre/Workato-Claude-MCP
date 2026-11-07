---
url: 'https://docs.workato.com/en/connectors/google-text-to-speech.md'
description: Learn how to connect to the Google Text to Speech connector in Workato.
---

# Google Text to Speech

[Google Text to Speech](https://cloud.google.com/text-to-speech/) allows you to convert text into natural-sounding speech with 30 voices, available in multiple languages and variants. It applies DeepMind's research in WaveNet and Google’s neural networks to deliver high-fidelity audio.

Workato's Google Text to Speech connector allows you to build powerful automation and connect with other applications in the workflow.

> **FEATURE AVAILABILITY**
> 
> The Google Text to Speech connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The Google Text to Speech connector uses the [Cloud Text to Speech API v1](https://cloud.google.com/text-to-speech/docs/reference/rest/).

## How to connect to Google Text to Speech

The Google Text to Speech connector supports OAuth 2.0 authentication.

Complete the following steps to create a Google Text to Speech connection in Workato:

1. Sign in to Workato.
   
2. Select the project where you plan to store the Google Text to Speech connection.
   
3. Click **Create > Connection** or press C twice.
   
4. Search for the `Google Text to Speech` connector and select it as your app.
   
5. Enter a name for your connection in the **Connection name** field.
   
   ![Connection setup](/assets/connection-setup.jH_GasTY.png)_Google Text to Speech connection setup_
   
6. Select the project or folder where you plan to store the connection from the **Location** drop-down menu.
   
7. Click **Sign in with Google**.
   
8. Click **Allow** when prompted to authorize Workato to access your Google account.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-text-to-speech/action-synthesize-text.md
description: >-
  The Convert text to speech action converts text into synthetic voice audio,
  supporting 30 voices and multiple languages.
---

# Google Text to Speech - Convert text to speech action

The **Convert text to speech** action converts text into synthetic voice audio, supporting 30 voices and multiple languages.

## Input

| Input field | Description |
| --- | --- |
| Text | Input the text you plan to convert into voice audio. This field can accept a datapill or raw text. |
| Voice language | Specify the [language code](https://cloud.google.com/speech-to-text/docs/languages) of the voice. Note that the conversion accuracy differs across languages. Google may not yet have full support for certain languages. |
| Voice gender | Specify the gender of the voice. |
| Audio encoding | Specify the encoding of the output audio file. |

## Output

| Output field | Description |
| --- | --- |
| Audio content | The string content of the converted audio. You can map this datapill to the **File contents** field of an **Upload file** action from any file connector such as Box or Dropbox and create an audio file. |

---
