---
url: 'https://docs.workato.com/en/recipes/performance-copilot.md'
description: >-
  Performance Copilot helps optimize your recipes by providing AI-powered
  evaluations and actionable suggestions across several dimensions, including
  cost, performance, security, and quality.
---

# Performance Copilot

Performance Copilot helps you optimize your recipes by evaluating them across key quality dimensions and providing AI-powered suggestions.

After you build and save a recipe, Performance Copilot generates a health score and highlights areas for improvement. This allows you to make your recipe more efficient, reliable, and production-ready before deploying it or submitting it for review.

![Use Performance Copilot to optimize your recipes](/assets/performance-copilot.NxAHj8q5.gif)_Use Performance Copilot to optimize your recipes_

## Key capabilities

Performance Copilot offers the following key capabilities:

- **Recipe scoring**: Assess the overall health and efficiency of your recipe.
- **AI-powered suggestions**: Receive actionable improvements for your recipe tailored to cost, performance, security, and quality.

## How it works

Performance Copilot evaluates your recipe based on several key dimensions to ensure it is efficient, secure, and production-ready. It uses a set of predefined rules to assess and suggest optimizations.

### Evaluation criteria

Performance Copilot uses the following criteria to identify areas for improvement:

- **Cost**: Can the recipe perform the same work with lower usage?
- **Performance**: Can the recipe complete jobs faster or handle more work?
- **Security**: Does the recipe use deprecated features?
- **Quality**: Can the recipe be made more maintainable or production-ready?

### Optimization rules

Based on its evaluation, Performance Copilot applies a set of predefined rules to detect inefficiencies and recommend specific improvements:

| Rule | Explanation | Suggested fix |
| --- | --- | --- |
| Consecutive variable declaration | Declaring variables in separate steps increases cost unnecessarily. | Consolidate variables into a single step to reduce resource consumption. |
| Unused variable detection | Unused variables add cost and reduce readability without benefits. | Remove the unused variable or incorporate it into the recipe. |
| Inefficient job filtering | Stopping jobs immediately through IF conditions can clutter job history and increase costs. | Use trigger filters to prevent unnecessary processing. |
| Recipe too long | Recipes that exceed 50 steps are harder to maintain and troubleshoot. | Break recipes into smaller, manageable components. |
| Redundant logging | Excessive logging increases costs. | Remove debugging log actions before production or use a logging service for better observability. |
| Empty error handling | Suppressing errors without action makes troubleshooting difficult. | Add notifications or recovery steps within error-handling blocks. |
| Deprecated action used | Deprecated actions may cause instability. | Replace deprecated actions with supported alternatives. |

Additional rules are planned and will be added over time.

## Prerequisites

Before you can use Performance Copilot, you must enable **Copilot** in your workspace. Enabling Copilots requires the [Environment admin](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) role or the legacy [Admin](/en/roles#role-admin) system role. If you aren't assigned one of these roles, contact your workspace administrator. Refer to our [Copilots documentation](/en/ai-features/copilot#set-up-copilots) for setup details.

> **PERMISSIONS**
> 
> Copilots don't have granular permission settings. When enabled, all workspace collaborators can access it regardless of their role.

## Example: Optimize a recipe with Performance Copilot

This example demonstrates how Performance Copilot evaluates a recipe that uses a deprecated [Scheduler by Workato](/en/features/scheduler) action and provides optimization suggestions.

Complete the following steps to optimize your recipe:

1. Save your recipe by clicking **Save**.
   
   > **RECIPE SCANS**
   > 
   > Performance Copilot automatically scans recipes when they are saved. This includes when you refresh schema or test the recipe.
   
2. Click the **Optimize** tab.
   
   ![Click the Optimize tab](/assets/click-optimize.IpXo4z8z.png)_Click the Optimize tab_
   
3. Review the optimization score to gauge your recipe's performance.
   
   ![Review the optimization score](/assets/optimization-score.Bi3CJfNy.png)_Review the optimization score_
   
4. Expand the category or categories where Performance Copilot suggests improvements.
   
   ![Expand categories to view Performance Copilot's suggested improvements](/assets/expand-improvement.hlRa_h7X.png)_Expand categories to view Performance Copilot's suggested improvements_
   
   In this example, Performance Copilot highlights an improvement in the **Performance** category for Step 5, which uses a deprecated action. It labels using deprecated actions as a high-impact issue.
   
5. Click **View suggestion** to see the recommended fix.
   
   ![View the suggestion](/assets/show-suggestion.CtZJmqSa.png)_View the suggestion_
   
   In this example, Performance Copilot suggests replacing the deprecated action with the [Wait for time duration action](/en/features/scheduler/actions/wait-for-time-duration).
   
6. Open the action's configuration settings by clicking the **Step 5** link, the blue sparkle icon, or the step itself.
   
7. Replace the deprecated action with the suggested action.
   
   When you make the change, Performance Copilot detects it and prompts you to save the recipe for re-analysis.
   
   ![Apply the suggested change to your recipe](/assets/apply-suggestion.k9NOvDRN.png)_Apply the suggested change to your recipe_
   
8. Save your recipe again and watch your optimization score improve.
   
   ![Optimized recipe](/assets/optimized-recipe.DJiYkH-A.png)_Optimized recipe_
   

## What's next?

We're continuously improving Performance Copilot with new features, including:

- **LLM-based rules** for smarter, more accurate suggestions.
- **Field-level suggestions** for granular optimizations.
- **Developer API endpoints** to programmatically trigger health scans and retrieve scores. [Learn more](/en/workato-api/recipes).
- **Admin insights** for tracking recipe, project, and workspace-level quality metrics.
- **Aggregated health scores** at the project level when individual scores are unavailable.
- **Custom rule support** so admins can enforce company-specific policies.

These enhancements are subject to change as we refine the experience based on user feedback.

---
