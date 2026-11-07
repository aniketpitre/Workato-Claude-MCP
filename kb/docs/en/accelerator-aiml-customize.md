---
url: 'https://docs.workato.com/en/accelerator-aiml-customize.md'
description: >-
  Customize the AIML accelerator to connect to other machine learning and
  storage platforms in place of SageMaker and AWS S3.
---

# Connect to other ML platforms

This accelerator provides ready-to-use connections and recipes for Sagemaker as the machine learning platform and AWS S3 as the storage platform.

These platforms are placeholders. You can change them to different platforms to suit your use case. Contact Customer Success for guidance.

## How to customize the AIML accelerator

The **AWS SageMaker** folder contains recipes that call the Sagemaker SDK. To change this to another platform, make a copy of this folder and replace SageMaker with a platform of your choice.

Similarly, the **AWS S3** folder contains recipes that call AWS S3. To change this to another platform, make a copy of this folder and replace AWS S3 with a platform of your choice.

> **REQUIRED CHANGES**
> 
> Replacing SageMaker or AWS S3 with an alternative platform may require you to make additional changes to the recipes in this accelerator. This may include changing recipe actions, adapting parameters, or adding additional steps to recipes. For example, an alternative platform may require additional recipe steps to parse JSON to extract the model profile from the lookup tables.

---
