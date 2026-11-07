---
url: >-
  https://docs.workato.com/en/features/decision-models/decision-models-by-workato.md
description: >-
  Use the Make a decision action in the Decision Models by Workato connector to
  call a decision model from a recipe and return its results.
---

# Decision Models by Workato connector - Make a decision action

The **Decision Models by Workato** connector allows you to use the **Make a decision** action to call an existing [decision model](/en/recipes/decision-models) from a recipe, including skill recipes used by genies and MCP servers. This behavior is similar to the [Recipe functions](/en/connectors/recipe-functions) connector, which calls an existing recipe. The decision model uses business logic to process the **Input values** you provide and returns the results for use in downstream recipe steps.

### Input

| Input field | Description |
| --- | --- |
| Model name | Select the model to call. |
| Input values | Provide values for the model's input fields. Refer to [Create an input field](/en/features/decision-models/model-builder#create-an-input-field) to configure a model's input schema. |

### Output

| Output field | Description |
| --- | --- |
| Model outputs | Contains fields defined in the model's output schema. The business logic of the model determines the values in these fields. Refer to [Configure output fields](/en/features/decision-models/model-builder#configure-output-fields) to configure a model's output schema. |
| Decision path | Contains the following information about each decision table or conditional node that was processed: **ID**: The unique identifier for the node., **Input**: Contains the fields that were passed to the node and their values., **Name**: The name of the node., **Output**: Contains the fields that were output by the node and their values., **List size**: The total number of nodes visited., **List index**: The position of the current node in the list. |
