---
url: 'https://docs.workato.com/en/connectors/ghost/upload-image-action.md'
description: The Upload image action uploads an image to Ghost and returns a hosted URL.
---

# Ghost - Upload image action

The **Upload image** action uploads a single image to Ghost and returns a hosted URL you can use as a post's feature image or inside post HTML.

## Input

| Input field | Description |
| --- | --- |
| File content | Enter the contents of the image file. |
| File name | Enter the file name with extension. For example, `hero.png`. |
| MIME type | Select the MIME type of the image, such as `PNG`, `JPEG`, `WebP`, `GIF`, `SVG`, or `ICO`. |
| Purpose | Select the image's intended use, such as `Image`, `Profile image`, or `Icon`. Defaults to `Image` if left blank. `Profile image` and `Icon` must be square. `Icon` also accepts ICO files. |
| Reference | Optional. Enter the original file name or path. Returned as-is in the response for find-and-replace workflows. |

## Output

| Output field | Description |
| --- | --- |
| URL | Hosted URL of the uploaded image. |
| Reference | Reference value you provided in the input. |

---
