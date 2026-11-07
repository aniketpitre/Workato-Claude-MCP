---
url: 'https://docs.workato.com/en/test-automation/test-case-results.md'
description: >-
  View test case run results in Workato, including pass or fail status, the
  check that failed, and links to the test case run jobs.
---

# View test case run results

When Workato finishes running a test job, you receive a notification with the test case run results.

The test case run results modal contains the following information about each test case that was executed.

- Recipe name
- Test case name
- Test case run result (passed/failed)
- Check that failed (if any)
- Link to a job for a test case run

## If the test case has no checks

The job run result is the same as the test case run result.

## Test case run jobs

In addition to viewing test case run results after a test case run completes, you can access all test case run results at the recipe level on the **Jobs** page.

![Job page](/assets/job-page.w45wwXn8.png)_Select a test case run job from the list_

### Test case job metadata

The Jobs page for each test case run contains the following information.

![View job result](/assets/job-result.z1geUr1P.png)_View test case run results_

- Steps that were mocked
- Steps that had checks
  - For each check
    - Check data
    - Check result
- Test case run result
- Test case name and link
  - If the test case was deleted, Workato only displays the name of the deleted test.

---
