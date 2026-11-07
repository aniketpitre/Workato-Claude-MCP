---
url: 'https://docs.workato.com/en/connectors/creatomate/search-records-action.md'
description: >-
  The Search records action enables you to search templates in your Creatomate
  project.
---

# Creatomate - Search records action

The **Search records** action searches templates in your Creatomate project. Results are display with the newest-updated listed first.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to search. **Template** is the only available object. |
| Tags | Enter comma-separated tags for the object. For example, `Product,Marketing`. Returns templates that carry any of these tags. |

## Output

| Output field | Description |
| --- | --- |
| Records | List of templates matching the search, including the following properties. |
| ID (Records) | Unique identifier of the template. |
| Name (Records) | Name of the template. |
| Tags (Records) | List of tags applied to the template. |
| Created at (Records) | Date and time when the template was created. |
| Updated at (Records) | Date and time when the template was last updated. |
| Warnings (Records) | List of warnings about the template's RenderScript source. |

Search results don't include the template's RenderScript source. Use the [Get record action](/en/connectors/creatomate/get-record-action) to retrieve a specific template's source.

---
