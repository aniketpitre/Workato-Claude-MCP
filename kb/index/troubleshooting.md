# Troubleshooting

27 pages. Paths are relative to the repository root.


## Troubleshooting

- **Common recipe errors** - `kb/docs/en/recipes/design-runtime-error.md` - Learn the difference between design-time and run-time recipe errors in Workato to troubleshoot and keep recipes running smoothly.
- **Troubleshooting** - `kb/docs/en/troubleshooting.md` - Troubleshoot Workato recipes with guidance on design-time and run-time errors, error codes, timeouts, connection issues, and debugging best practices.
- **General error codes** - `kb/docs/en/troubleshooting/general-errors.md` - Reference for common HTTP error codes returned in Workato recipes, including 400, 401, 403, 404, 422, and 500, with causes and fixes.
- **Troubleshooting - Webhook Rate Limits** - `kb/docs/en/troubleshooting/webhook-gateway-limits.md` - Learn how the Workato webhook gateway enforces rate limits and byte quotas per environment and how leaky bucket rate limiting handles bursts.

## Best practices

- **Security best practices for recipes** - `kb/docs/en/recipes/recipe-security.md` - Follow security best practices for Workato recipes, including storing credentials in connections, using a secrets manager, and data masking.
- **Tips and tricks - Test frequently** - `kb/docs/en/troubleshooting/tips-and-tricks/test-frequently.md` - Learn how to build and test Workato recipes incrementally using skip steps to isolate logic, compare paths, and catch errors early.

## Common recipe errors

- **Design-time errors** - `kb/docs/en/recipes/design-time-errors.md` - Learn how to find and fix design-time errors in Workato recipes that prevent you from testing or starting the recipe.
- **Action and fields errors** - `kb/docs/en/recipes/design-time-errors/empty-actions.md` - Learn how to identify and fix action and field errors in Workato recipes, including empty actions, missing input fields, and invalid datapills.
- **Incorrect formulas and code actions** - `kb/docs/en/recipes/design-time-errors/incorrect-formulas.md` - Learn how to find and fix formula and code action errors in Workato recipes, including syntax mistakes in SQL, Python, Ruby, and JavaScript steps.
- **Unestablished connectivity** - `kb/docs/en/recipes/design-time-errors/unestablished-connectivity.md` - Learn how to resolve unestablished connectivity errors in Workato recipes caused by changed credentials, missing permissions, or wrong configurations.
- **Infinite loops** - `kb/docs/en/recipes/infinite-loops.md` - Learn what infinite loops are in Workato recipes, how to recognize them in bi-directional syncs, and how to prevent recipes from triggering themselves.
- **Memory optimization best practices** - `kb/docs/en/recipes/memory-utilization.md` - Learn how to optimize recipe memory use, avoid temporary job dispatch failures, and handle large batches and files with batch and streaming actions.
- **Rate limiting** - `kb/docs/en/recipes/rate-limiting.md` - Learn how API rate limits cause errors in Workato recipes and how to optimize recipes or raise limits to avoid hitting them.
- **Job errors** - `kb/docs/en/recipes/recipe-job-errors.md` - Learn how to troubleshoot recipe job errors in Workato, including trigger errors, run-time formula errors, missing fields, and timeouts.
- **Run-time errors** - `kb/docs/en/recipes/run-time-errors.md` - Learn how to identify and troubleshoot run-time errors that occur during recipe job execution in Workato.
- **Action and trigger errors** - `kb/docs/en/recipes/run-time-errors/action-internal-errors.md` - Learn how to identify and troubleshoot action errors (caught and uncaught) and trigger errors during recipe job execution in Workato.
- **Troubleshooting APIM/webhook calls at run time** - `kb/docs/en/recipes/run-time-errors/apim-webhooks.md` - Troubleshoot APIM and webhook call errors in Workato by checking network connectivity, access permissions, and HTTP status codes.
- **Internal and upstream/downstream application errors** - `kb/docs/en/recipes/run-time-errors/internal-upstream-errors.md` - Learn how to distinguish and troubleshoot internal Workato errors from upstream and downstream application errors in your recipes.

## General error codes

- **Troubleshooting - 400 Bad request error** - `kb/docs/en/troubleshooting/400-bad-request-error.md` - Learn why the 400 Bad Request error occurs in Workato from malformed requests or invalid input, and how to troubleshoot and resolve it.
- **Troubleshooting - 401 Unauthorized error** - `kb/docs/en/troubleshooting/401-unauthorized-error.md` - Learn why the 401 Unauthorized error occurs in Workato when credentials are rejected, and how to reconnect the app to resolve it.
- **Troubleshooting - 403 Forbidden error** - `kb/docs/en/troubleshooting/403-forbidden-error.md` - Learn why the 403 Forbidden error occurs in Workato when a connection lacks permissions, and how to troubleshoot it in triggers and actions.
- **Troubleshooting - 404 Not found** - `kb/docs/en/troubleshooting/404-not-found.md` - Learn why the 404 Not Found error occurs in Workato when a record or identifier is invalid, and how to troubleshoot and resolve it.
- **Troubleshooting - 422 Unprocessable Entity** - `kb/docs/en/troubleshooting/422-unprocessable-entity.md` - Learn why the 422 Unprocessable Entity error occurs in Workato from invalid or conflicting input data, and how to troubleshoot and fix it.
- **Troubleshooting - 500 internal server error** - `kb/docs/en/troubleshooting/500-internal-server-error.md` - Learn why the 500 Internal Server Error occurs in Workato from a server-side failure in the external service, and what to do next.

## Solution articles

- **Troubleshooting - Column does not exist** - `kb/docs/en/troubleshooting/column-does-not-exist.md` - Learn why the UndefinedColumn SQL error occurs in Workato when a query references a missing column, and how to troubleshoot and resolve it.
- **Troubleshooting - Undefined method for nil:NILClass** - `kb/docs/en/troubleshooting/undefined-method-for-nilclass.md` - Troubleshoot the Undefined method for nil:NilClass error in Workato recipes that occurs when a formula runs on an empty datapill.

## Troubleshooting tools

- **Job debug tracing** - `kb/docs/en/recipes/job-debug-tracing.md` - Learn how to use Workato job debug tracing to view detailed HTTP requests, responses, headers, and payloads for each recipe action line.
