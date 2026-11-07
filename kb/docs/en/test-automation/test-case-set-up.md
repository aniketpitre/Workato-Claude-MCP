---
url: 'https://docs.workato.com/en/test-automation/test-case-set-up.md'
description: >-
  Set up a Workato test case by mocking the recipe trigger and steps, adding
  data checks, and validating the test before you run it.
---

# Set up a test case

Setting up a test case consists of four basic steps:

1. Step 1: [Mock a trigger](#mock-trigger)
2. Step 2: [Mock steps](#mock-steps)
3. Step 3: [Add checks](#add-steps)
4. Step 4: [Validate the test case](#test-case-validate)

> **LIMITS**
> 
> Workato restricts test case sizes to 10MB, and cannot run test cases that exceed this quota.

* * *

## Step 1: Mock a trigger

You must mock the recipe trigger to successfully run a test case.

To mock a trigger:

1. Click the trigger step of your recipe.
   
2. Decide how you plan to mock the trigger. You can use data from a previous job, or type in your own JSON.
   
3. If you decide to use data from a previous job:
   
   1. Select **Pick data from a prior job**.
      
   2. Select a job from the list of previous jobs displayed in the wizard. ![Select a job](/assets/test-case-mock-trigger.BwWBnJm8.png)_Select a previous job_
      
   3. Click **Preview output**.
      
   4. Click **Copy to mock trigger**. ![Copy to mock trigger](/assets/test-case-preview-output.ZQFn3dDH.png)_Preview output_
      
4. Alternatively, select **Type in your own JSON** to type in your own JSON.
   
   ![Type in your own JSON](/assets/mock-trigger-json.CqMyxwNk.png)_Type in your own JSON_
   

* * *

## Step 2: Mock steps

If you do not want Workato to use your external apps data in your tests, you can use mock data instead. In this situation, you must use mock data to mock all of the steps that involve interaction with third-party applications.

For example, if your recipe involves searching for tickets in Zendesk or updating a ticket in Jira, you can mock these steps to avoid using the data in your Zendesk or Jira instances.

### What types of mocking is available in Test Automation

Test Automation allows you to [mock step data output](#mock-step-data-output) and [mock errors](#mock-to-throw-an-error).

#### Mock step data output

When you mock step data output, the following actions occur:

- Workato evaluates all input fields.
- Workato does NOT hit external app data or send HTTP requests.
- Workato uses the mock data you provide as a step output.

#### Mock to throw an error

When used, the following actions occur:

- Workato evaluates all input fields.
- Workato does NOT hit external app data or send HTTP requests.
- Workato simulates a recipe error with the error name and description you provide.
  - If the recipe you are testing does not have a MONITOR/ON ERROR wrapper for a step, the recipe fails with an error.
  - Otherwise, the following occurs:
    - Recipe execution jumps to the ON ERROR section of the recipe.

### Steps that must be mocked

To use Test Automation, you must mock the following steps.

- Trigger
- Workbot actions
- All long or multistep actions
- Functions

### Steps that can't be mocked

Test Automation does not support mocking the following types of steps.

- Conditions and loops
  - If
  - If else
  - Repeat action
- Stop job
- Monitor and ON ERROR steps
- Return action
- Certain Workato utility connectors
  - All Variables by Workato actions
  - All Lists by Workato actions

### How to mock a step

1. Select a step you plan to mock.
   
2. Decide how to mock the step. Like when you mock a trigger, choose between using a prior job as the source data or entering your own JSON.
   

* * *

## Step 3: Add checks

To add a check:

1. Choose a step.
   
2. Click **Create check**.
   
3. In the **Type** field, select the check you plan to perform on this step from the following options:
   
   - Data check
     
   - Validate if step input or output data works under the conditions you specify.
     
   - Step failure check
     
   - Verify if the step throws an error. If the recipe job fails and all steps with errors pass this check, the test case still passes.
     
4. By default, Test Automation automatically creates a data check with the following default settings:
   
   - Check data: Step output
   - Check condition: Equals
   - Check value: `{}`
   
   ![Create a check](/assets/test-case-name.Cc3qQWKB.png)_Create a check_
   

### Available checks

Test Automation supports two basic types of checks: [data checks](#data-checks) and [step failure checks](#step-failure-checks).

#### Data checks:

Validate if step input and output data work under the conditions you specify.

The following is a list of data checks and their corresponding conditions:

- Step input (JSON object)
  
- - Available condition(s):
  - - Equals
- Step output (JSON object)
  
- - Available condition(s):
  - - Equals
- Step output (fields)
  
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

#### Step failure check:

The step failure check verifies if the step throws an error. If the recipe job fails and all steps with errors pass this check, the test case will still pass. This type of check is useful in scenarios where you plan to test negative scenarios, wherein you deliberately introduce erroneous data or conditions that cause the recipe to stop with failure.

Test Automation also gives you the option to set up your test case to check for specific error details by configuring the following fields:

- Error type
  
- Provide an error type only if you want specific errors to pass the test.
  
- Error message
  
- Provide an error message only if you want specific error messages to pass the test.
  

### Number of checks

You can add as many checks as you need for each step.

### Naming checks

You can name your checks to differentiate them from other checks.

Checks for the same step cannot have duplicate names.

* * *

## Step 4: Validate test case

When you save a test case, Workato validates the test case.

1. To save your changes, click **Save**.
   
   ![Save a test case](/assets/test-case-save.CM-i7DJ9.png)_Save a test case_
   

### Errors

The following errors prevent you from saving a test case.

Step not mocked

![Trigger not mocked error](/assets/trigger-mock-error.BN6iZERW.png)_You must mock the trigger step_

Mock has invalid JSON document

![invalid JSON in mock step](/assets/mock-error.5lFPrsaF.png)_Invalid JSON in mocked step_

Check has invalid JSON document

![invalid JSON in check](/assets/check-error.Brq31KAA.png)_Invalid JSON in step with checks_

Recipe was updated

![Recipe updated](/assets/recipe-updated.dHmOe5cV.png)\_

* * *

> **FURTHER READING**
> 
> - [View a test case](/en/test-automation/test-case-view)

---
