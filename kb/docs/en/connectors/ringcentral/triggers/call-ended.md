---
url: 'https://docs.workato.com/en/connectors/ringcentral/triggers/call-ended.md'
description: >-
  Use the Call ended trigger to retrieve calls that have ended for the connected
  RingCentral extension.
---

# RingCentral - Call ended trigger

The **Call ended** trigger retrieves calls that have ended on the connected RingCentral extension. The trigger checks for ended calls every five minutes.

Ensure the connected RingCentral extension has **Read Call Log** permissions. These permissions are typically enabled for predefined or default RingCentral roles.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum allowed value is five minutes. |
| When first started, this recipe should pick up events from | Specify the start time to retrieve calls that have ended since this time. Defaults to one hour before the recipe is first started if left blank. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

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
| To | An object containing information about the recipient of the call. |
| Phone number (to) | The recipient's phone number. |
| Name (to) | The recipient's name. |
| Extension number (to) | The recipient's extension number. |
| From | An object containing information about the caller. |
| Phone number (from) | The caller's phone number. |
| Name (from) | The caller's name. |
| Extension number (from) | The caller's extension number. |

---

---
url: >-
  https://docs.workato.com/en/connectors/ringcentral/triggers/new-call-recording.md
description: >-
  Use the New call recording trigger to retrieve calls with recordings made by
  the connected RingCentral extension.
---

# RingCentral - New call recording trigger

The **New call recording** trigger retrieves calls with recordings made by the connected RingCentral extension. The trigger checks for new calls with recordings every five minutes.

Ensure the connected RingCentral extension has **Read Call Log** permissions. These permissions are typically enabled for predefined or default RingCentral roles.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum allowed value is five minutes. |
| When first started, this recipe should pick up events from | Specify the start time to retrieve call recordings created since this time. Defaults to one hour before the recipe is first started if left blank. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Field | Description |
| --- | --- |
| URI | The URI of the call recording. |
| ID | The unique identifier of the call recording. |
| Session ID | The session ID of the call. |
| Start time | The start time of the call. |
| Duration | The duration of the call in seconds. |
| Type | The type of call. |
| Direction | The direction of the call (for example, inbound, outbound). |
| Action | The action taken during the call. |
| Result | The result of the call. |
| To | An object containing information about the recipient of the call. |
| Phone number (to) | The recipient's phone number. |
| Name (to) | The recipient's name. |
| Extension number (to) | The recipient's extension number. |
| From | An object containing information about the caller. |
| Phone number (from) | The caller's phone number. |
| Name (from) | The caller's name. |
| Extension number (from) | The caller's extension number. |
| Recording | An object containing details about the recording. |
| URI (recording) | The URI of the recording. |
| ID (recording) | The ID of the recording. |
| Type (recording) | The type of the recording. |
| Content URI (recording) | The content URI of the recording. |

---
