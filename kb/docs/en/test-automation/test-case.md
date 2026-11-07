---
url: 'https://docs.workato.com/en/test-automation/test-case.md'
description: >-
  Learn how Workato test cases use mock data and checks on specific recipe steps
  to verify that a recipe behaves as expected.
---

# Test cases overview

Test cases are available at the recipe level. To view the list of test cases, choose a recipe and navigate to the **Test cases** interface. This interface displays a table containing all test cases created for this recipe.

* * *

## What is a test case?

A test case is a set of mock data and checks for specific steps of a particular recipe.

You can create multiple test cases for any recipe you plan to test.

A test case defines:

- What steps should use mock (simulated) data and the mock data that should be used.
- What step output data must be checked and the expected result of the check.

For each test case, you can add a unique name and provide a description of the purpose of the test case.

![List of test cases](/assets/test-automation.Bwosa57G.png)_List of test cases_

Each test case contains the following data columns:

- Name
  
- The name of the test case. We recommend using a descriptive name that helps you identify the test.
  
- Modified on
  
- The date the test case was most recently modified.
  
- Last run
  
- The status of the most recent run.
  
  - Passed/Failed
    
  - The result of the most recent run.
    
  - Never active
    
  - The test case was never run.
    
- Last run recipe version
  
- The version of the recipe that was used to run the test case.
  
- Last run date
  
- The date of the most recent run.
  
- Case summary
  
- The number of checks and mocked steps.
  
- Description
  
- The description of the test.
  

Additionally, click the **...** (ellipsis) to access the action menu. From here, you can perform the following actions:

- Delete a test case
- Clone (duplicate) a test case

---
