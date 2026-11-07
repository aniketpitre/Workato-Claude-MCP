---
url: 'https://docs.workato.com/en/connectors/openai/generate-images.md'
description: >-
  The Generate images action in the OpenAI connector creates images from text
  prompts, edits images, or makes variations using Dall-E models.
---

# OpenAI - Generate images action

The generate images action feature allows you to generate high-quality images from textual descriptions using machine learning models (Dall-E). This action can be used in a variety of use cases, such as:

- **Slide deck generation:** Sales teams can use the generate images API to create high-quality product images for sales presentations and proposals. By inputting a textual description of a product, the action can generate a photorealistic image that accurately represents the product's features and benefits. This can be used to generate slide decks based on specific inputs easily.
- **Brand asset generation:** Marketing teams can use this action to obtain a series of preliminary assets for their various campaigns. Within the standard campaign workflows, you can incorporate an additional step to kickstart the campaign assets generation aspect by utilizing this action and the campaign description.

This action supports three ways to generate images:

- Create images from prompt
- Edit existing image
- Generate variations of existing images.

![Generate images action](/assets/generate-images.BhrOmnmr.png)_Generate Images Action_

## Input

| Field | Description |
| --- | --- |
| Action | Select the image action you wish to utilize from the picklist. |
| Prompt | Enter the text for which to obtain an image. Maximum length is 1000 characters. We recommend that you provide a detailed prompt to obtain an image suited for your purposes. |
| Number of images | The number of images to generate. It must be between 1 and 10. |
| User | A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. |
| Resolution | Select a resolution that influences the level of detail an image holds. |
| Response format | Select between URL and binary content. |
| Image | The image to edit. It must be a valid PNG file, less than 4MB, and square. If a mask is not provided, the image must have transparency, which will be used as the mask. |
| Mask | An additional image whose fully transparent areas (ex., where alpha is zero) indicate where the image should be edited. This must be a valid PNG file, less than 4MB, and have the same dimensions as the image. |

## Output

| Field | Description |
| --- | --- |
| Data | URL/File Content | Generated image by OpenAI based on the defined parameters. |
| List size | Total number of tokens utilized by the prompt and response. |
| List index | Value indicating which item in the list is currently being accessed. |

---
