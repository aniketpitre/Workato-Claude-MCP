---
url: 'https://docs.workato.com/en/recipes/cancel-job.md'
description: >-
  Cancel a running Workato job from the job details page to stop a recipe that
  has a bug or appears stuck in processing.
---

# Cancel Job

You can halt the execution of running jobs. Jobs that are running are in the **Processing** status.

You may need to cancel a running job when:

- you found a bug in the recipe and want to immediately stop the job
- the job seems to be stuck in processing

## How to Cancel a Running Job

You can cancel a job from the job details page. Simply select the **Cancel job** button.

![Cancel a job from job details page](/assets/cancel-job.Z8aks0ER.png)_Cancel a job from job details page_

The job status will be updated from **Processing** to **Canceled**. This job details will indicate that the job was canceled by the a user (`Job canceled by user`).

![Reason for cancel](/assets/reason-for-cancel.BwK5ZOIL.png)_Reason for cancel_

* * *

## Recipe Functions And Callable Recipes

Canceling a parent recipe job generally won't cancel the child recipes. If you are using [Recipe functions](/en/connectors/recipe-functions), the called recipes may continue to run independently to completion.

**Note**: This is also applicable to [Callable recipes (deprecated)](/en/features/callable-recipes).

---
