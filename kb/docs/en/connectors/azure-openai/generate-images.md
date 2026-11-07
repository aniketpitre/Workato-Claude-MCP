---
url: 'https://docs.workato.com/en/connectors/azure-openai/generate-images.md'
description: >-
  The Generate images action generates high-quality images from text
  descriptions using machine learning models, such as Dall-E.
---

# Azure OpenAI - Generate images action

The **Generate images** action generates high-quality images from text descriptions using machine learning models, such as Dall-E. You can use this action in a variety of use cases, such as:

- **Slide deck generation:** Sales teams can use the generate images API to create high-quality product images for sales presentations and proposals. By inputting a text description of a product, the action generates a photorealistic image that accurately represents the product's features and benefits. You can use this action to generate slide decks based on specific inputs easily.
- **Brand asset generation:** Marketing teams can use this action to obtain a series of preliminary assets for their various campaigns. Within the standard campaign workflows, you can incorporate an additional step to kickstart the campaign assets generation aspect by utilizing this action and the campaign description.

![Generate images action](/assets/azure-openai-generate-images.BYWVhzWj.png)_Generate images action_

## Input

| Input field | Description |
| --- | --- |
| Prompt | Enter a prompt that describes the image to generate. The maximum length is 1000 characters. Workato recommends that you provide a detailed prompt to obtain an image suited for your purposes. |
| Number of images | Select the number of images to generate. The default value is `1` and the maximum is `5`. |
| User | Enter a unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. |
| Image size | Select a resolution for the generated image from the picklist. This influences the level of detail in the image. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the generated image. |
| Created at | The time and date that the image was generated. |
| Expires at | The time and date the image expires. |
| Result | A JSON object containing the following attributes: **Created:** The time and date the image was generated.; **Data:** A nested JSON object within **Result** containing the following attributes: **URL:** The URL of the generated image., **List size:** The total number of tokens used by the prompt and response., **List index:** Value indicating which item in the list is currently being accessed. |
| Status | Indicates whether the image was generated successfully. |

---
