---
url: 'https://docs.workato.com/en/connectors/confluence/create-task.md'
description: >-
  The Create task action in the Confluence connector lets you add a new task to
  a specified page, including assignee, status, and due date.
---

# Confluence - Create task action

The **Create task** action allows you to add a new task to a specified page in Confluence.

> **REQUIRES CLOUD CONNECTION**
> 
> You must use a cloud connection for this action. Use a [Custom action](/en/developing-connectors/custom-actions) if you need a feature the Data Center edition doesn't support.

## Input

| Input field | Description |
| --- | --- |
| Space key | Input the key for the space where you plan to create the task. Find this key in the URL of the space's Confluence page. |
| Page title | Specify the title of the page where the task is created. |
| Task status | Set the status of the task as either `incomplete` or `complete`. |
| Task | Describe the task details. |
| Username | Enter the username of the individual responsible for the task. |
| Due date | Select the due date for the task completion. |

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
