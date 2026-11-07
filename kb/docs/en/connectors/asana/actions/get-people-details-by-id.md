---
url: >-
  https://docs.workato.com/en/connectors/asana/actions/get-people-details-by-id.md
description: The Get people details by ID action retrieves user details by ID in Asana.
---

# Asana - Get people details by ID action

The **Get people details by ID** action retrieves user details by ID in Asana.

## Input

| Input field | Description |
| --- | --- |
| People ID | Enter the user ID. |

## Output

| Output field | Description |
| --- | --- |
| People | Object representing the person. |
| People ID (People) | The unique identifier of the person. |
| Name (People) | The name of the person. |
| Email (People) | The email address of the person. |
| Photo (People) | Photo URLs for the person in various sizes. |
| Image 21x21 (Photo) | 21x21 pixel image URL. |
| Image 27x27 (Photo) | 27x27 pixel image URL. |
| Image 36x36 (Photo) | 36x36 pixel image URL. |
| Image 70x70 (Photo) | 70x70 pixel image URL. |
| Image 128x128 (Photo) | 128x128 pixel image URL. |
| Workspaces (People) | Array of workspaces the person belongs to. |
| Workspace ID (Workspaces) | The unique identifier of each workspace. |
| Name (Workspaces) | The name of each workspace. |
