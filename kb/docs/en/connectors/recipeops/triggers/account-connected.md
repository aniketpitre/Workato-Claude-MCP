---
url: 'https://docs.workato.com/en/connectors/recipeops/triggers/account-connected.md'
description: >-
  The Account connected trigger in the RecipeOps connector monitors selected
  connections and fires when those connections connect successfully.
---

# RecipeOps - Account connected trigger

This trigger monitors selected connections and triggers when the connections are connected successfully.

* * *

## Input

| Field | Description |
| --- | --- |
| **Apps to monitor** | Select app connections to monitor. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Connection ID** | The ID of the connection. |
| **Name** | The display name of the connection. |
| **Application** | The type of the connection. For example: **PostgreSQL** |
| **Authorization error** | If an authorization error occurred, this will contain the error message. |
| **Authorized at** | The time the connection was authorized. |
| **Connected by user** | Details about the user who created the connection. This field has some additional sub-fields:
| Field | Description |
| --- | --- |
| **User ID** | The workspace ID where this connection is located. |
| **User name** | The user's name. |
| **User email** | The user's email address. |

 |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/account-credentials-refresh-failed.md
description: >-
  The Account credentials refresh failed trigger in the RecipeOps connector
  fires when OAuth 2.0 or Multi-digest connections fail to refresh access
  credentials.
---

# RecipeOps - Account credentials refresh failed trigger

The **Account credentials refresh failed** trigger monitors only OAuth 2.0 and Multi-digest connections and creates a job if these connections fail to refresh their access credentials. This trigger doesn't monitor connections that use Basic, API key, or other static API credentials, as these types of connections lack a mechanism for refreshing API credentials.

## Input

This trigger doesn't require any input.

## Output

| Output field | Description |
| --- | --- |
| Connection ID | The ID of the connection that failed to refresh its access credentials. |
| Connection name | The name of the connection that failed to refresh its access credentials. |
| Application | The name of the application. |
| Initial connection time | The initial connection datetime. |
| Connection lost at | The datetime the connection was lost. |
| Connection lost reason | The reason the connection was lost. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/account-disconnected.md
description: >-
  The Account disconnected trigger in the RecipeOps connector monitors selected
  connections and fires when those connections are disconnected.
---

# RecipeOps - Account disconnected trigger

This monitors selected connections and triggers when they are disconnected.

* * *

## Input

| Field | Description |
| --- | --- |
| **Apps to monitor** | Select app connections to monitor for disconnections. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Connection ID** | The ID of the connection. |
| **Name** | The display name of the connection. |
| **Application** | The type of the connection. For example: **PostgreSQL** |
| **Authorization error** | If an authorization error occurred, this will contain the error message. |
| **Authorized at** | The time the connection was last authorized. |
| **Disconnected by user** | Details about the user who disconnected the connection. This field has some additional sub-fields:
| Field | Description |
| --- | --- |
| **User ID** | The workspace ID where this connection was located. |
| **User name** | The user's name. |
| **User email** | The user's email address. |

 |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/deployment-approved.md
description: >-
  The Deployment approved trigger in the RecipeOps connector fires when a
  project deployment is approved by reviewers in real time.
---

# RecipeOps - Deployment approved trigger

The **Deployment approved** trigger monitors project deployments approved by reviewers in real-time.

> **PRIVATE BETA**
> 
> This trigger is in private beta. Private beta features are available in production but only to selected customers. Customers must opt in and be accepted into the beta.
> 
> During the private beta, Workato may update its functionality or change its availability without prior notice.

## Input

This trigger doesn't require any input.

## Output

| Field | Description |
| --- | --- |
| Deployment | An object containing details about the deployment. |
| ID (deployment) | The unique identifier for the deployment. |
| Name (deployment) | The name of the deployment. |
| Description (deployment) | A brief description of the deployment. |
| Author (deployment) | An object containing information about the user who created the deployment. |
| User ID (author) | The workspace ID of the user who created the deployment. |
| User name (author) | The name of the user who created the deployment. |
| User email (author) | The email address of the user who created the deployment. |
| Deployment state (deployment) | The current state of the deployment. For example, `pending_review`. |
| Reviews (deployment) | A list of reviews associated with the deployment. |
| Reviewer (reviews) | An object containing details about the user assigned to review the deployment. |
| User ID (reviewer) | The workspace ID of the user assigned to review the deployment. |
| User name (reviewer) | The name of the user assigned to review the deployment. |
| User email (reviewer) | The email address of the user assigned to review the deployment. |
| Status (reviews) | The status of the review. For example, `pending`, `approved`, or `rejected`. |
| Comment (reviews) | Any comment added to the review. |
| Project build ID (deployment) | The unique identifier for the project build associated with the deployment. |
| Target folder (deployment) | An object containing details about the target folder. |
| ID (target folder) | The unique identifier of the target folder. |
| Name (target folder) | The name of the target folder. |
| Path (target folder) | The workspace path that indicates the location of the target folder. |
| Reviewed at (deployment) | The date and time the deployment was reviewed. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---

---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/deployment-complete.md
description: >-
  The Deployment complete trigger in the RecipeOps connector fires when a
  project deployment is successfully pushed to assigned environments in real
  time.
---

# RecipeOps - Deployment complete trigger

The **Deployment complete** trigger monitors project deployments successfully pushed to assigned environments in real-time.

> **PRIVATE BETA**
> 
> This trigger is in private beta. Private beta features are available in production but only to selected customers. Customers must opt in and be accepted into the beta.
> 
> During the private beta, Workato may update its functionality or change its availability without prior notice.

## Input

This trigger doesn't require any input.

## Output

| Field | Description |
| --- | --- |
| Deployment | An object containing details about the deployment. |
| ID (deployment) | The unique identifier for the deployment. |
| Name (deployment) | The name of the deployment. |
| Description (deployment) | A brief description of the deployment. |
| Author (deployment) | An object containing information about the user who created the deployment. |
| User ID (author) | The workspace ID of the user who created the deployment. |
| User name (author) | The name of the user who created the deployment. |
| User email (author) | The email address of the user who created the deployment. |
| Deployment state (deployment) | The current state of the deployment. For example, `pending_review`. |
| Reviews (deployment) | A list of reviews associated with the deployment. |
| Reviewer (reviews) | An object containing details about the user assigned to review the deployment. |
| User ID (reviewer) | The workspace ID of the user assigned to review the deployment. |
| User name (reviewer) | The name of the user assigned to review the deployment. |
| User email (reviewer) | The email address of the user assigned to review the deployment. |
| Status (reviews) | The status of the review. For example, `pending`, `approved`, or `rejected`. |
| Comment (reviews) | Any comment added to the review. |
| Project build ID (deployment) | The unique identifier for the project build associated with the deployment. |
| Target folder (deployment) | An object containing details about the target folder. |
| ID (target folder) | The unique identifier of the target folder. |
| Name (target folder) | The name of the target folder. |
| Path (target folder) | The workspace path that indicates the location of the target folder. |
| Deployed by | An object containing information about the user who deployed the project. |
| User ID (deployed by) | The workspace ID of the user who deployed the project. |
| User name (deployed by) | The name of the user who deployed the project. |
| User email (deployed by) | The email address of the user who deployed the project. |
| Deployed at | The date and time the project was deployed. |

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)

---
