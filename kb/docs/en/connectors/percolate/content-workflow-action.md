---
url: 'https://docs.workato.com/en/connectors/percolate/content-workflow-action.md'
description: >-
  The Check content workflow step action in the Percolate connector lets you
  verify whether a content item's current workflow step matches yours.
---

# Percolate - Check content workflow step action

The **Check content workflow step** action allows you to verify if a content item's workflow step matches the specified criteria.

![Check content workflow step in Percolate action](/assets/check-content-workflow-step-action.BWXifTFp.png)_Percolate - Check content workflow step action_

## Input

| Input field | Description |
| --- | --- |
| Team | Enter the team ID or IDs associated with the content you plan to check. Separate team IDs with a comma if you plan to check multiple teams. For example: `license:1234567891098765432, license:098765432112345678` |
| Content ID | Input the ID of the content to check. For example: `post:123345`. |

## Output

| Output field | Description |
| --- | --- |
| Content workflow step matches selected steps? | Indicates if the content's current workflow step matches the steps you've specified. |

---
