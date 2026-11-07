---
url: 'https://docs.workato.com/en/accelerator-aiml-recipes.md'
description: >-
  Reference for the AIML accelerator recipes, organized into Functions,
  Bootstrap, AWS SageMaker, AWS S3, and API endpoint folders.
---

# AIML accelerator recipes

The recipes in this accelerator are organized in the following folders:

- [Functions](#function)
- [Bootstrap](#bootstrap)
- [AWS SageMaker](#sagemaker)
- [AWS S3](#aws)
- [API Endpoint recipes](#endpoint)

* * *

## Functions

<dl><dt>AIML | FUNC-005 | CSV Validator</dt><dd>This recipe defines the validation logic. The AIML SDK actions use this logic to validate the data against predefined configurations in the <strong>AIML | Data Fields</strong> lookup table.</dd></dl>

* * *

## Bootstrap

<dl><dt>AIML| REC-009 | Load Model Schema</dt><dd>Use this recipe to automatically load your schema into the <strong>AIML Data Fields</strong> lookup table. Inspect the lookup table after using this recipe to ensure that the recipe loaded the correct datatype and validation rules.</dd><dt>AIML | FUNC-012 | Get Workato Data Type</dt><dd>This recipe works as a support recipe for <strong>AIML | REC-009 | Load Model Schema</strong>. It identifies the schema's data type.</dd></dl>

* * *

## AWS SageMaker

<dl><dt>AIML | FUNC-003 | Get Sagemaker Prediction</dt><dd>Calls the Sagemaker InvokeEndpoint function to generate predictions. See <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html">Sagemaker documentation</a> for more information.</dd><dt>AIML | FUNC-011 | Train ML Model Sagemaker</dt><dd>Calls Sagemaker CreateAutoMLJob endpoint to create a new AutoML training job. See the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html">CreateAutoMLJob documentation </a>for details.</dd></dl>

* * *

## AWS S3

<dl><dt>AIML | FUNC-004 | Stage Training Data in S3</dt><dd>The recipe connects with S3 to get the source and target data.</dd></dl>

* * *

## Endpoint recipes

<dl><dt>AIML | API-001 | Stage Training Data</dt><dd>Stage the training data from the source to a target location while validating it against the rules you define in the <strong>AIML | Data Fields</strong> lookup table.</dd><dt>AIML | API-002 | Get Prediction</dt><dd>Pass new, unseen feature data to the trained model to generate a prediction. The accelerator validates the data against the rules you define in the <strong>AIML | Data Fields</strong> lookup table and then passes it to the ML platform to return the prediction data.</dd><dt>AIML | API-002 | Train ML Model</dt><dd>This recipe trains a new ML model. This recipe takes the ML Model configuration, source, and target training data location from the <strong>AIML | Model Profile</strong> lookup table. It reads the data from the source, validates it, and then passes it to the <strong>ML Model</strong> to train a machine learning model.</dd><dt>AIML | API-008 | Get Model Identifiers and Schema</dt><dd>Reads the <strong>Data Fields</strong> and <strong>Model Identifier</strong> defined in the lookup tables and loads them in the actions.</dd></dl>

* * *

---
