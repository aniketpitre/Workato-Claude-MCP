---
url: 'https://docs.workato.com/en/connectors/typeform/search-records-action.md'
description: >-
  The Search records action searches Typeform for records matching the criteria
  you specify.
---

# Typeform - Search records action

The **Search records** action searches Typeform for records matching the criteria you specify.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of object to search for in Typeform. |

This action dynamically loads additional fields based on your selected **Object**. Use these fields to specify search criteria. The action outputs objects that match all criteria.

## Output

The output of this action varies based on the **Object** you select. For example, the action returns the following when you select the **Forms** object:

| Output field | Description |
| --- | --- |
| ID | The form's unique identifier. |
| Title | The title of the form. |
| Last updated at | The date and time the form was last updated. |
| Self | The API endpoint URL for the form. |
| Theme | The API endpoint URL for the form's theme. |
| Links | Contains links relevant to the form. For example, the display URL where respondents can access the form. |
| Settings | Contains the form's configuration settings. For example, `Is public` and `Is trial`. |
| List size | The total number of forms returned by the search. |
| List index | The position of the current form in the list of results. |

---
