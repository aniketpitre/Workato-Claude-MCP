---
url: 'https://docs.workato.com/en/connectors/aws-inspector-2/add-tags-action.md'
description: >-
  The Add tags action attaches metadata (tags) to resources, such as findings or
  reports, using key-value pairs.
---

# AWS Inspector2 - Add tags action

The **Add tags** action attaches metadata (tags) to resources, such as findings or reports, using key-value pairs. Tags help organize, categorize, and filter resources for better management and reporting.

## Input

| Input field | Description |
| --- | --- |
| Resource ARN | Enter the Amazon Resource Name (ARN) of the AWS resource to tag. |
| Tags | Enter key-value pairs for the tags to assign to the resource. For example: `Environment: Production` |

## Output

AWS Inspector2 returns an HTTP 200 response with an empty body if the action is successful.

---
