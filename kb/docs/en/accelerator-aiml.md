---
url: 'https://docs.workato.com/en/accelerator-aiml.md'
description: >-
  The AIML accelerator is a framework for training and deploying machine
  learning models in Workato to drive intelligent automation without ML
  expertise.
---

# Accelerator: AIML

![AIML accelerator](/assets/aiml.DHw1VeHt.png)

<dl><dt>What is it?</dt><dd>A framework for training and deploying machine learning models from within Workato. You can leverage predictions to drive intelligent automation.</dd><dt>Why is it valuable?</dt><dd>This framework enables you to collect and validate data for machine learning. It also enables you to train machine learning models without ML expertise.</dd><dt>Who should use it?</dt><dd>Data analysts or citizen data scientists.</dd></dl>

Artificial intelligence (AI) is key to delivering end-to-end automations in any technology-driven organization. Leveraging machine learning while integrating various applications adds value and boosts both the speed and quality of business deliverables.

The [Deloitte Report](https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/services/consulting/2026/state-of-ai-2026.pdf) mentions that many enterprises face challenges when they implement AI/ML automation due to a lack of integration and expertise with artificial intelligence and machine learning. These challenges include:

- Difficulty scaling AI/ML solutions
- Difficulty acquiring quality data for ML model training
- Difficulty leveraging trained models as part of an automated process to derive business value

Additionally, organizations struggle to move, transform, and develop data into a predictive model, and to deploy and integrate predictive models into IT architecture to power new solutions. Each of these tasks requires considerable technical resources. Workato's AIML accelerator aims to change that.

The AIML accelerator provides the framework required to train a machine learning model and use it to make predictions to automate end-to-end business processes. This enables your data scientists and machine learning engineers to focus on building models.

Some ML platforms, like AWS SageMaker, have autoML capabilities, which you can drive from within Workato. The AIML accelerator can easily integrate deployed models into the IT landscape to drive intelligent automation solutions.

The recipes in this accelerator are modular, enabling you to integrate them with any machine-learning platform. This framework enables any citizen developer to deploy a machine learning model and use it in their automations.

This accelerator provides ready-to-use connections and recipes for you to use SageMaker as the machine learning platform and AWS S3 as the storage platform. You can [customize this accelerator](/en/accelerator-aiml-customize) to suit your use case by modifying recipes or connecting alternate applications.

* * *

## Benefits

- Unlock access to data with the ability to connect to thousands of enterprise business systems.
- Transform data and load it into databases, storage systems, and ML platforms.

## Capabilities

- Drive AutoML directly from within Workato.
- Easily plug into deployed models for inference.
- Evaluate ML model output to drive automation.
- Integrate ML output or ML-driven automation back into business systems and processes.

## Features of the AIML accelerator

The AIML accelerator consists of three main features: [train a machine learning (ML) model](#model-train), [stage training data](#training-data), and [get predictions](#prediction-get).

* * *

### Train ML model

This feature enables you to point your data to a location so that Workato can validate the data. Workato uses this data to train and deploy a machine-learning model.

[Learn more about training a machine learning model](/en/accelerator-aiml-design#model-train)

* * *

### Stage training data

This feature enables you to stage CSV-formatted training data in a defined location while validating it against your specified configuration.

[Learn more about staging training data](/en/accelerator-aiml-design#training-data)

* * *

### Get predictions

This feature enables you to pass all data except for the prediction field. Workato validates the data and then passes it to the ML platform. Then, the ML platform returns the prediction data.

[Learn more about get predictions](/en/accelerator-aiml-design#prediction-get)

---
