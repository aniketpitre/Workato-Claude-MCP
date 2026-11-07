---
url: >-
  https://docs.workato.com/en/connectors/google-workspace-custom/create-records-action.md
description: >-
  The Create records action enables you to create multiple records in Google
  Workspace.
---

# Google Workspace (Custom) - Create records action

The **Create records** action enables you to create multiple records in Google Workspace.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create records for. Fields load dynamically based on the object you select. |

For example, the following input fields correspond to the **Users** object.

| Input field | Description |
| --- | --- |
| Users | Provide the details for the users you plan to create. |
| Primary email | Provide the user's primary email address. |
| Password | Provide the user's password. |
| Suspended | Indicates if the user is suspended. |
| Change password at next login | If true, the user must change their password at the next login. |
| IP whitelisted | Indicates if the IP is whitelisted. |
| Name | Provide objects containing the user's name information. |
| Emails | Provide values for the user's email addresses object. |
| External ids | Provide values for the user's external IDs object. |
| Relations | Provide values for the user's relations object. |
| Aliases | Provide values for the object of email aliases for the user. |
| Addresses | Provide details for the user's addresses. |
| Organizations | Provide values for the user's organization object. |
| Last login time | Provide the last login timestamp. |
| Phones | Provide values for the user's phone numbers object. |
| Suspension reason | Provide a reason for suspension. |
| Thumbnail photo URL | Provide the URL of the user's thumbnail photo. |
| Languages | Provide values for the languages users speak. |
| POSIX accounts | Provide values for POSIX (Portable Operating System Interface) accounts. |
| SSH public keys | Provide values for the user's SSH public keys object. |
| Notes | Provide details for the user’s notes object. |
| Websites | Provide values for the user's website object. |
| Locations | Provide users' locations. |
| Include in global address list | Specify if the user is in the global address list. |
| Keywords | Provide values for the user's keywords object. |
| Deletion time | Provide the time when the user was deleted. |
| Gender | Provide values for the user's gender object. |
| Thumbnail photo ETag | Provide the eTag of the thumbnail photo. |
| Instant messenger accounts | Provide instant messaging accounts. |
| Recovery email | Provide a recovery email address. |
| Recovery phone | Provide recovery phone number. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, the following output fields correspond to the **Users** object.

| Output field | Description |
| --- | --- |
| Users | An array of User objects. |
| Primary email | The user's primary email address. |
| Suspended | Indicates if the user is suspended. |
| Change password at next login | If true, the user must change their password at the next login. |
| IP whitelisted | Indicates if the IP is whitelisted. |
| Name | Object containing the user's name information. |
| Kind | Type of the resource. |
| Etag | ETag of the resource. |
| Emails | Users' email addresses. |
| External ids | Object for the user's external IDs. |
| Relations | Object containing the user's relations. |
| Aliases | Object of email aliases for the user. |
| Addresses | An object that contains the user's addresses. |
| Organizations | Object containing the user's organizations. |
| Last login time | Last login timestamp. |
| Phones | Users' phone numbers. |
| Suspension reason | Reason for suspension. |
| Thumbnail photo URL | URL of the user's thumbnail photo. |
| Languages | Languages the user speaks. |
| POSIX accounts | POSIX (Portable Operating System Interface) accounts information. |
| SSH public keys | Object for the user's SSH public keys. |
| Notes | Object that contains user notes details. |
| Websites | Object containing the user's website information. |
| Locations | User's locations object. |
| Include in global address list | Indicates if the user is in the global address list. |
| Keywords | User's keywords. |
| Deletion time | Time when the user was deleted. |
| Gender | User's gender. |
| Thumbnail photo ETag | ETag of the thumbnail photo. |
| Ims | Instant messaging accounts object. |
| Org unit path | Path to organizational unit. |
| Recovery email | Recovery email address. |
| Recovery phone | Recovery phone number. |
