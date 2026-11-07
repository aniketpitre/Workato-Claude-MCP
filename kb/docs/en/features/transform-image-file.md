---
url: 'https://docs.workato.com/en/features/transform-image-file.md'
description: >-
  Use the Transform image file action from File tools by Workato to convert
  images to PNG or JPG and resize them to a set width and height.
---

# File tools by Workato - Transform image file action

The **Transform image file** action transforms an image file to the required type and size. The maximum file size allowed is 50 MB. This action fails if the file size is larger than 50 MB.

![Transform image file action](/assets/transform-image-file.Basijqw9.png)_Transform image file action_

## Input

| Field | Description |
| --- | --- |
| Input image | Provide the image file content. |
| Convert to | Specify the format to convert the image to. Options include **png** and **jpg**. |
| Resize | Expand and configure the fields in this section to resize the image to the specified width and height. |
| Width | Specify the width to resize the image to (in pixels). |
| Height | Specify the height to resize the image to (in pixels). |
| Strict resize? | Define how the image is resized relative to the specified dimensions. By default, the resized image maintains its aspect ratio and may be smaller than the specified dimensions. Select **Yes** to ensure the image matches the exact dimensions. When enabled, Workato resizes the image so that its larger dimension fits the specified size, then adds white padding to the smaller dimension to fill the remaining space. |

## Output

| Field | Description |
| --- | --- |
| Transformed image | The transformed image file. |

---
