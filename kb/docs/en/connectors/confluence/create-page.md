---
url: 'https://docs.workato.com/en/connectors/confluence/create-page.md'
description: >-
  The Create page action in the Confluence connector lets you create a new page
  in a specified space, returning its ID, status, and content details.
---

# Confluence - Create page action

The **Create page** action allows you to create a new page in Confluence.

> **REQUIRES CLOUD CONNECTION**
> 
> You must use a cloud connection for this action. Use a [Custom action](/en/developing-connectors/custom-actions) if you need a feature the Data Center edition doesn't support.

## Input

| Input field | Description |
| --- | --- |
| Space key | Enter the space key found in the Confluence space URL. |
| Title | Choose a title for the new page. |
| Body | Input the content for the new page. |

## Output

| Output field | Description |
| --- | --- |
| Page ID | The unique identifier of the page created in Confluence. |
| Type | The type of content created. |
| Status | The current status of the page. |
| Title | The title of the page. |
| Space | Details of the space that contains the page. |
| History | Historical information about the page. |
| Version | Versioning information of the page. |
| Ancestors | Information about the page's parent pages. |
| Container | Information about the container of the page. |
| Body | The full content of the body of the page. |
| Extensions | Additional features associated with the page. |
| Links | A collection of relevant URLs related to the page. |
| Expandable | Fields that can be expanded to reveal more information. |

---
