---
url: 'https://docs.workato.com/en/test-automation/test-case-run.md'
description: >-
  Run a Workato test case to verify recipe functionality, with details on run
  priority, how mocked steps execute, and how data checks work.
---

# Run test case

After you create a test case, you can use it to test your recipe's functionality.

You can run each test case manually from the list of test cases. To access this list, select a recipe and navigate to the **Test cases** tab.

## Run priority

Test cases run with the same priority as standard recipes. This means that some test cases run sequentially and some run simultaneously to stay within [recipe concurrency](/en/features/batch-processing#maximize-data-throughput-with-batch-processing) quotas.

## How Workato runs mocked steps

- Input
  
- Workato evaluates the input values.
  
- Step execution
  
- Workato does not run the step. For example, for the step **Search for tickets in Zendesk** Workato does not send a request to Zendesk.
  
- Step output
  
- The step output is replaced with the mock output you provide for a specific step.
  

## How Workato handles data checks

### When checks run

- Step input check
  
- This check occurs before the step runs.
  
- Step output check
  
- This check occurs after the step runs.
  
- Step output field check
  
- This check occurs after the step runs.
  

### Check conditions for different data types

Workato evaluates the data type when it performs a check. Depending on what you plan to check, the available set of conditions for a check varies.

- Step input/output object checks
  
- Workato compares JSON objects as objects, not as strings.
  
  - Available condition(s):
  - - Equals
- Output field checks
  
- - Available condition(s):
  - - Equals
    - Contains
    - Starts with
    - Ends with
    - Doesn't equal
    - Doesn't contain
    - Doesn't start with
    - Doesn't end with
    - Is present
    - Is not present

## How Workato handles step failure checks

In general, test cases pass successfully in the following scenarios:

- The test case run job is successful, and all checks are successful.
  
- The test case run job failed, all checks are successful, and all steps with errors have [negative (step failure) checks](/en/test-automation/test-case-set-up#step-failure-checks) set up for them.
  

### Examples

The following example scenarios describe how Workato handles step failure checks under certain conditions:

Example 1

- The test case run job failed on a **STOP** step.
  
- The step inside the **monitor** block that failed **_DOES NOT_** have a negative (**step failure**) check.
  
- The step inside the **monitor** block fails.
  

**Overall result:** The test case fails.

Example 2

- The test case run job failed on a **STOP** step.
  
- The step inside the **monitor** block that failed **_HAS_** a negative (**step failure**) check
  
- The step inside the **monitor** block fails.
  

**Overall result:** The test case passes.

Example 3

- The test case run job failed on a **STOP** step.
  
- The step inside the **monitor** block has a **throw error** mock and **_DOES NOT_** have a negative (**step failure**) check
  
- The step inside the **monitor** block fails.
  

**Overall result:** The test case fails.

Example 4

- The test case run job failed on a **STOP** step.
  
- The step inside the **Monitor** block has a **throw error** and **_HAS_** a negative (**step failure**) check
  
- The step inside the **monitor** block fails.
  

**Overall result:** The test case passes.

## When checks fail

When a check fails, Workato stops the test case run job and does not complete additional recipe steps.

- Recipe error
  
- Because a test case run is a recipe run, it fails if there are problems in the recipe.
  
- Check failed
  
- The test case run fails and the job stops when any check fails.
  
- When checked or mocked steps are deleted from a recipe
  
- The test case run fails immediately. The job report displays the following error message:
  
  > Test case contains an error: Some steps with mocks or checks were deleted from the recipe. Please update the test case or revert the recipe to the version that the test case was built for. Please fix it in the test case editor.
  
  > **EDITING A STEP**
  > 
  > When you edit a recipe step, Workato considers this equivalent to creating a new step and deleting the previous step. Thus, if you make changes to any of the steps in your recipe, Workato treats this as a deleted step and the check fails.
  

> **FURTHER READING**
> 
> - [View test case run results](/en/test-automation/test-case-results)

---
