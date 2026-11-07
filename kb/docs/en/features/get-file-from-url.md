---
url: 'https://docs.workato.com/en/features/get-file-from-url.md'
description: >-
  Use the Get file from URL action to retrieve text or binary file contents from
  a public URL in Workato recipes, with file streaming support.
---

# File tools by Workato - Get file from URL action

The **Get file from URL** action retrieves file contents from a specified URL. It supports both text and binary files. Use [file streaming](/en/features/file-streaming) for files larger than 1024 MB.

> **SEE AN EXAMPLE**
> 
> Refer to the [PlanGrid and Microsoft SharePoint use case](/en/getting-started/use-cases/plangrid-sharepoint) for an example of how this action is used in a recipe.

![Get file from URL action](/assets/get-file-from-url.1Y4ahanN.png)_Get file from URL action_

## Input

| Field | Description |
| --- | --- |
| URL | Specify the URL where the file is located. The URL must be publicly accessible. |
| Base64 encoding | Select **Yes** when the downstream action expects a Base64 encoded value. |
| Include line breaks? | Select **No** to remove line breaks from the file content. Defaults to **Yes** if left blank. |
| Enable file streaming? | Select **Yes** when the file you plan to download is larger than 200 MB. |
| Encoding of the file content | Specify the encoding of the file to set it explicitly. Defaults to **UTF-8** if left blank. |

## Output

| Field | Description |
| --- | --- |
| File contents | The contents of the file. |
| Size | The size of the file in bytes. |

## Limitations and compatibility

The **Get file from URL** action behaves differently based on the file size and whether file streaming is enabled. Understanding these differences helps you choose the right configuration for your source system.

### How the action handles files

The **Get file from URL** action retrieves the entire file in memory before uploading the file to Workato when streaming is disabled. The disabled streaming mode supports a maximum 200 MB file size and is a recommended option when the source URL responds with a complete file in one response.

The **Get file from URL** action downloads the file in chunks to reduce memory usage when streaming is enabled. The streaming enabled mode is designed for large files and supports a maximum file size of approximately 2 GB. The source system must support HTTP range requests or chunked transfer encoding. The download may fail, repeat, or return incomplete data if the source doesn't support HTTP range requests or chunked transfer encoding methods.

### Compatibility with different sources

Not all file servers or APIs support streaming. For example, some endpoints return the full file in one response and reject range or chunked requests.

The **Get file from URL** action fails when connecting to non-streaming sources if you enable **Enable file streaming?**.

Disable **Enable file streaming?** in the action settings if your file source doesn't support streaming. Alternatively, use the HTTP connector to make a standard GET request and handle the file in your recipe.

### File size quotas

The following quotas apply to the **Get file from URL** action:

- **Maximum 200 MB**: Supported in non-streaming mode.
- **Maximum 2 GB**: Supported in streaming mode if the source supports range or chunked requests.

---
