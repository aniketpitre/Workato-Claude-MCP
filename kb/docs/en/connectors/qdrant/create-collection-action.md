---
url: 'https://docs.workato.com/en/connectors/qdrant/create-collection-action.md'
description: Create a Qdrant collection with a vector size and distance metric.
---

# Qdrant - Create collection action

The **Create collection** action creates a collection on your Qdrant cluster. For example, you can use it to provision a collection for each agent or tenant in an onboarding recipe.

## Input

| Input field | Description |
| --- | --- |
| Collection name | Enter the name of the new collection. |
| Vector size | Enter the number of dimensions each vector has. This must match your embedding model's output. |
| Distance | Select the metric used to compare vectors. Options are `Cosine`, `Euclid`, `Dot`, and `Manhattan`. |

## Output

| Output field | Description |
| --- | --- |
| Usage | Resources the request used. Includes hardware usage and inference usage. |
| Time | The time the request took to process, in seconds. |
| Status | The status of the request. Returns `ok` when the request succeeds. |
| Result | Returns `true` if the collection was created. |

---
