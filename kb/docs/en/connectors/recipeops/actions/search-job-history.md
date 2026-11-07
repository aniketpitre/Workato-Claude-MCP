---
url: 'https://docs.workato.com/en/connectors/recipeops/actions/search-job-history.md'
description: >-
  The Search job history action in the RecipeOps connector lists the job history
  for a recipe, with filters for job status and start time.
---

# RecipeOps - Search job history action

This action lists the job history for a specified recipe. Results can be filtered by job status and start time.

* * *

## Limitations

Results are limited to the most recent 1,000 jobs.

* * *

## Input

| Input field | Description |
| --- | --- |
| Recipe | Select the recipe to retrieve job history for. |
| Job status | Select an option to filter jobs by status: **All**, **Completed**, **Pending**, **Failed** |
| Jobs created since | Enter a date and time to filter jobs created on or after this timestamp. |
| Jobs created till | Enter a date and time to filter jobs created on or before this timestamp. |

* * *

## Output

The output will contain the following attributes, along with custom job report data.

| Output field | Description |
| --- | --- |
| Job ID | The job ID. |
| Calling job ID | The ID of the calling job. |
| Root recipe ID | The ID of the original recipe that initiated the workflow. This remains the same for all jobs related to that workflow. |
| Root job ID | The ID of the first job in the workflow triggered by the root recipe. |
| Status | The status of the job. |
| Title | The title of the job. |
| Started at | The time the job started. |
| Completed at | The time the job completed. |
| Recipe ID | The ID of the recipe associated with the job. |
| Error | Details about the error encountered during the job, if applicable. This field contains additional subfields: **Error ID:** The error ID., **Error type:** The type of error., **Error message:** The error message. |
| List size | The total number of jobs in the result set. |
| List index | The index (current position) of the job in the list of results. |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---
