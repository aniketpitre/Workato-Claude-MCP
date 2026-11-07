---
url: 'https://docs.workato.com/en/connectors/dropbox/trigger-new-file-revision.md'
description: >-
  The New file revision trigger in the Dropbox connector fires immediately when
  a monitored file is updated and a new revision is created.
---

# Dropbox - New file revision in Dropbox trigger

This trigger monitors a file in Dropbox, and triggers immediately when the file is updated (and a new file revision created).

If the filename is changed, updates will no longer be picked up. Picks up file revisions from a day ago when recipe is first started.

![New file revision in dropbox trigger](/assets/new-file-revision-trigger.C7oLBZm3.png)_New file revision in Dropbox trigger_

## Input

| Field name | Description |
| --- | --- |
| File / File path | The CSV file to monitor for new changes. |
| Obtain a direct URL to file? | Whether or not to generate a public URL that is valid for 4 hours. |

## Output

| Field name | Description |
| --- | --- |
| Path | File path. |
| Bytes | File size in bytes. |
| Size | File size in string format. |
| Mime type | The Mime type of this file. |
| URL | File's public URL. Can be used to download file using the [Workato file connector](/en/features/handling-binary-files#download-file-content-from-public-url). |
| URL expires | Date/time the file's public URL will expire. |
| Rev | A unique identifier for the current revision of the file. |
| Modified | Date/time the file was last modified. |
| Client modified time | This is the modification time set by the desktop client when the file was added to Dropbox. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not. |

---
