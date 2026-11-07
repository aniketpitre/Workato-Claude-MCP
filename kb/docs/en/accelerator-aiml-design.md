---
url: 'https://docs.workato.com/en/accelerator-aiml-design.md'
description: >-
  Learn how the AIML accelerator works across its three processes: staging
  training data, training a machine learning model, and getting predictions.
---

# Solution design overview

![Solution design](/assets/aiml-design.CGb2_v-8.png)

The AIML accelerator consists of three main processes: stage training data, train a machine learning (ML) model, and get predictions.

* * *

## Stage training data

Staging training data involves the following steps:

1. Workato queries the source system(s) for relevant training data.
2. The source system(s) respond(s) to the query
3. Workato transforms the source data into a feature representation and validates the data against defined rules.
4. S3 serves as a data staging area for AWS SageMaker.

[Learn how to stage training data](/en/accelerator-aiml-run#data-stage).

* * *

## Train ML model

Training an ML model involves the following steps:

1. Workato queries source system(s) for relevant training data.
2. Source system(s) respond to the query.
3. Workato transforms the source data into a feature representation and validates it against defined rules.
4. Workato calls SageMaker with the S3 location to train and deploy the machine learning model.

[Learn how to train a machine learning model](/en/accelerator-aiml-run#ml-train).

* * *

## Get predictions

Getting predictions involves the following steps:

1. Workato triggers based on a relevant event and captures previously unseen data.
2. Workato constructs a feature string and makes a prediction request against a model endpoint.
3. SageMaker responds with an ML model prediction.
4. Workato handles the response as required by the specific use case. For example, you can configure Workato to send the output to a target system. You can also configure Workato to evaluate the response and drive an automated process.

[Learn how to get predictions](/en/accelerator-aiml-run#prediction).

* * *

---
