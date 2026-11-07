---
url: 'https://docs.workato.com/en/recipes/rate-limiting.md'
description: >-
  Learn how API rate limits cause errors in Workato recipes and how to optimize
  recipes or raise limits to avoid hitting them.
---

# Rate limiting

Most APIs have a cap on the number of API calls you can make within a certain period. These limits usually differ by app.

In cases whereby the rate limits may have been reached, the particular trigger or action will throw an error in Workato when made. In such cases, the error is typically explicit about being a rate limit error.

To remedy such errors, you might want to look into optimizing your recipes to make minimal calls (by reducing the number of actions done with that particular app). If it occurs frequently, you might want to increase your API rate limits for that app.

---
