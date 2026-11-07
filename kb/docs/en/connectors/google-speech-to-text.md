---
url: 'https://docs.workato.com/en/connectors/google-speech-to-text.md'
description: >-
  Google Speech to Text allows converting audio to text by applying neural
  network models.
---

# Google Speech to Text

[Google Speech to Text](https://cloud.google.com/speech-to-text/) leverages advanced neural network models to convert audio into text, supporting over 120 languages and variants. It enables features like voice command-and-control, transcription of call center audio, and more.

Workato's Google Speech to Text connector allows you to build powerful automations and integrate with other applications in your workflow.

> **FEATURE AVAILABILITY**
> 
> The Google Speech to Text connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

## API version

The Google Speech to Text connector uses [Cloud Speech to Text API v1](https://cloud.google.com/speech-to-text/docs/reference/rest).

## How to connect to Google Speech to Text on Workato

Google Speech to Text uses OAuth 2.0 for authentication.

Complete the following steps to create a Google Speech to Text connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select the Google Speech to Text connector.
   
3. Provide a **Connection name** to identify the Google Speech to Text instance Workato connects to.
   
   ![Connection setup](/assets/connection-setup.D04yhPn-.png)_Google Speech to Text connection setup_
   
4. Select the project or folder where you plan to store the connection from the **Location** drop-down menu.
   
5. Click **Sign in with Google**.
   
6. Click **Allow** when prompted to authorize Workato to access your Google Speech to Text account.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-speech-to-text/action-short-speech.md
description: Converts a short audio file into a text transcript.
---

# Google Speech to Text - Convert short speech to text action

This action allows you to convert a short audio file (less than 1 minute) into a text transcript.

![Google Convert short speech to text action](/assets/convert-short-speech-to-text-action.EmUW7H7D.png) _Convert short speech to text action_

## Input

| Input field | Description |
| --- | --- |
| Audio content | Accepts a content datapill, or audio content as a string. Workato automatically converts the provided audio content into base-64 format. |
| Language | Specify the language code of the audio file. Refer to [Google Speech to Text documentation](https://cloud.google.com/speech-to-text/docs/languages) for more information. |
| Encoding | Specify the encoding of the audio file. Google doesn't support MP3 input. MP3 files must be converted to a [supported encoding format](https://cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig#AudioEncoding) before use in this action. |
| Sample rate in Hertz | Specify the audio file's sample rate. A valid value ranges between 8000-48000 Hz. The usual optimal rate is 16,000, but this can vary across encodings and settings. Refer to [Google Speech to Text documentation](https://cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig#audioencoding) for information on the recommended sample rate for your file. |
| Enable word time offsets | If true, the output includes a list of words, the start and end time offsets (timestamps) for those words. |

## Output

| Output field | Description |
| --- | --- |
| Transcript | The extracted text transcript from the audio. |
| Confidence score | The confidence level for the entire transcription, with 0.0 as the lowest and 1.0 as the highest. |
| Words | List of words extracted from the audio. This list contains the start time, end time, and words extracted from the file. |

---
