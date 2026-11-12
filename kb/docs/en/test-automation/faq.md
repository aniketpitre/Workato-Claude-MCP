---
url: 'https://docs.workato.com/en/test-automation/faq.md'
description: >-
  Answers to common questions about Workato test automation, including
  versioning, loops, RLCM packages, and cloning behavior.
---

# Test automation FAQs

Get answers to frequently asked questions (FAQs) about test automation.

## Is there versioning for test cases?

View answer

No. Workato does not store the history of changes made to test cases or create new test case versions when a test case is saved.

## How does Test Automation handle loops?

View answer

If there is a check in the loop, Workato performs the check during every loop cycle. Workato recommends you avoid including checks inside loops.

## Are test cases a part of the Recipe Lifecycle Management (RLCM) package?

View answer

By default, Workato does not include test cases in RLCM packages. However, you can add test cases to your manifests manually.

Additionally, if your account has the Environments feature enabled, you can customize your deployments to include test cases in your Recipe Design Lifecycle (RDLC) packages.

## Are test cases cloned when the parent recipe is cloned?

View answer

No, test cases are not cloned.

## What happens when my test cases' parent recipe is deleted?

View answer

The test cases are deleted permanently.

## Does Workato send error notification emails when a test case fails?

View answer

No, Workato does not send error notification emails when a test case fails, regardless of the reason for the failure. This is different from regular jobs where Workato sends [email notifications](/en/recipes/error-notifications#error-notifications) to recipients you specify when a job fails.

---
