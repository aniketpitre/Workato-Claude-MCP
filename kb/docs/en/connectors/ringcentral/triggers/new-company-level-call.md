---
url: >-
  https://docs.workato.com/en/connectors/ringcentral/triggers/new-company-level-call.md
description: >-
  Use the New company level call trigger to retrieve new company level calls
  made by the connected RingCentral account.
---

# RingCentral - New company level call trigger

The **New company level call** trigger retrieves new company level calls made by the connected RingCentral account. The trigger checks for new company level calls every five minutes.

Ensure the connected RingCentral account has **Read Call Log** permissions. These permissions are typically enabled for predefined or default RingCentral roles.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum allowed value is five minutes. |
| When first started, this recipe should pick up events from | Specify the start time to retrieve calls received since this time. Defaults to one hour before the recipe is first started if left blank. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Field | Description |
| --- | --- |
| URI | The URI of the call. |
| ID | The unique identifier of the call. |
| Session ID | The session ID of the call. |
| Start time | The start time of the call. |
| Duration | The duration of the call in seconds. |
| Type | The type of call. |
| Direction | The direction of the call (for example, inbound, outbound). |
| Action | The action taken during the call. |
| Result | The result of the call. |
| Telephony session ID | The telephony session ID of the call. |
| To | An object containing information about the recipient of the call. |
| Phone number (to) | The recipient's phone number. |
| Name (to) | The recipient's name. |
| From | An object containing information about the caller. |
| Phone number (from) | The caller's phone number. |
| Name (from) | The caller's name. |
| Recording | An object containing details about the recording. |
| URI (recording) | The URI of the recording. |
| ID (recording) | The ID of the recording. |
| Type (recording) | The type of the recording. |
| Content URI (recording) | The content URI of the recording. |
| Extension | An object containing details about the extension. |
| URI (extension) | The URI of the extension. |
| ID (extension) | The ID of the extension. |
