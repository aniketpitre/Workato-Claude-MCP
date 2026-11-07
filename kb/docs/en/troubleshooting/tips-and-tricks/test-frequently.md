---
url: 'https://docs.workato.com/en/troubleshooting/tips-and-tricks/test-frequently.md'
description: >-
  Learn how to build and test Workato recipes incrementally using skip steps to
  isolate logic, compare paths, and catch errors early.
---

# Build recipes in small steps

Workato recommends that you build and test recipes incrementally to isolate logic and identify errors early. This approach simplifies development and reduces debugging time.

Troubleshoot with skip steps under 2min

[Video](https://www.youtube.com/embed/MWqMBEJvhxw)

## Use skip step to partially build recipes

You can mark a step as [skipped](/en/recipes/steps/skip-step) to instruct the recipe to bypass that step or block at runtime. Skipped steps don't run, and their datapills are unavailable for use in subsequent steps.

![Skipped step](/assets/skipped-step.CV4gD5SP.png)_A skipped step doesn't run and its datapills are not available_

### When to use skip step

Use skip steps in the following situations:

| Objective | Scenario |
| --- | --- |
| Test a recipe incrementally | Build and test part of a recipe while leaving other steps unconfigured. Skip the incomplete steps to run and validate the logic you finished. |
| Compare logic paths | Try different methods to solve the same problem. Skip one branch of logic to focus on testing the other without deleting any steps. |
| Bypass faulty steps | Skip steps that return design-time errors, such as invalid connections, datapills, or missing configurations, to test the rest of the recipe without interruption. |

---
