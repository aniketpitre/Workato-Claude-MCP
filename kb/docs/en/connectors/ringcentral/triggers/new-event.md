---
url: 'https://docs.workato.com/en/connectors/ringcentral/triggers/new-event.md'
description: >-
  Use the New event trigger to monitor new events in your RingCentral account in
  real-time.
---

# RingCentral - New event trigger (real-time)

The **New event** trigger monitors new events in your RingCentral account in real-time.

## Input

| Field | Description |
| --- | --- |
| Event | Select the [event types](#event-types) to monitor in real-time. |

### Event types

You can select the following event types to monitor:

- Account presence event
- Account telephony sessions event
- Company directory event
- Contact center phone number event
- Detailed extension presence event
- Detailed extension presence with SIP event
- Emergency address event
- Extension favorites event
- Extension grant list event
- Extension info event
- Extension list event
- Extension presence event
- Extension presence line event
- Extension telephony sessions event
- Inbound fax event
- Instant message event
- Message event
- Voicemail message event

## Output

| Field | Description |
| --- | --- |
| UUID | The unique identifier of the event. |
| Timestamp | The timestamp of the event. |
| Event | The type of event. |
| Subscription ID | The subscription ID associated with the event. |
| Owner ID | The owner ID of the event. |
| Body | An object containing additional information about the event. The structure of this object changes based on your selected event type. |

---
