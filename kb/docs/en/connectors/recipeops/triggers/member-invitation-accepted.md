---
url: >-
  https://docs.workato.com/en/connectors/recipeops/triggers/member-invitation-accepted.md
description: >-
  The Member invitation accepted trigger in the RecipeOps connector fires when a
  member invitation is accepted in the workspace.
---

# RecipeOps - Member invitation accepted trigger

This trigger monitors for accepted member invitations in the workspace.

* * *

## Input

| Field | Description |
| --- | --- |
| **Invitations to monitor** | Select invitations to monitor for acceptance. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Invitation ID** | The ID of the invitation. |
| **User ID** | The workspace ID where the invitation was accepted. |
| **Email** | The email of the user who accepted the invitation. |
| **Name** | The name of the user who accepted the invitation. |
| **Role** | The name of the collaborator role assigned to the user who accepted the invitation. |
| **Invitation sent at** | The time the invitation was sent. |
| **Joined at** | The time the user accepted the invitation. |
| **Team** | Details about the team the user joined. This field has some additional sub-fields:
| Field | Description |
| --- | --- |
| **Team ID** | The team's ID. |
| **Team name** | The team's name. |
| **Owner ID** | The ID of the user who owns the team. |

 |

* * *

## Resources

- [RecipeOps overview](/en/connectors/recipeops)
- [RecipeOps actions](/en/connectors/recipeops#actions)
- [RecipeOps triggers](/en/connectors/recipeops#triggers)
