---
url: >-
  https://docs.workato.com/en/connectors/okta/list-applications-assigned-to-user.md
description: >-
  The List applications assigned to user action in the Okta connector returns
  the applications assigned to a user with their metadata.
---

# Okta - List applications assigned to user action

This lists the applications that are assigned under a user with the associated metadata information.

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. |
| Page size | The maximum number of records to return in a single response. Default to 50. |
| Next page token | The token for continuing a previous list request on the next page. Provide the token from a previous response here. |

## Output

The output datatree contains a list of user applications. Each user application contains information like the application ID and application name. Refer to the Okta [Apps API response parameters](https://developer.okta.com/docs/reference/api/apps/#response-parameters-14) documentation for more details on the output fields.

| Field | Description |
| --- | --- |
| ID | The unique ID for the application. |
| Name | The name of the application. |
| Label | The label added to the application. |
| Status | Current status of the user's application. |
| Creation | The timestamp when the application was created. |
| Last updated | The timestamp when the application was last updated. |
| Accessibility | Object containing details such as whether the application is self service or not, the login URL, etc. |
| Visibility | Object containing visibility details about the application. |
| Links | Object containing specific links to users, groups and so on. |
| Credentials | Object containing credential-related details such as whether the password is revealed or not. |
| Embedded | Object containing user details. |
| List size | The number of groups in the list. |
| List index | The index of this group in the list of groups. |
