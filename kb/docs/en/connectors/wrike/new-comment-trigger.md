---
url: 'https://docs.workato.com/en/connectors/wrike/new-comment-trigger.md'
description: >-
  The New comment trigger in the Wrike connector picks up newly created
  comments, processing each as a separate job and retrieving recent comments.
---

# Wrike - New comment trigger

This trigger picks up comments that are created.

Each comment is processed as a separate job. It checks for new jobs once every poll interval, retrieving up to 7 days of new comments for each poll.

If the last new comment event is older than 7 days, more than 1 poll will be required to retrieve new comments up to current date & time.

![New comment trigger](/assets/new-comment-trigger.C6BFVScJ.png)_New comment trigger_

## Input

| Input field | Description |
| --- | --- |
| When first start, this recipe should pick up events from | Comments created after this time will be processed by the recipe. If left blank, the default date will be set to **one hour** before the recipe is first started. |

## Output

The output of this trigger contains the full set of columns from the selected comment. Here are some commonly used outputs. Since each Wrike comments are uniquely attached to folders or task, either the **Folder ID** or the **Task ID** will be displayed.

| Output field | Description |
| --- | --- |
| Comment ID | The ID of the comment. |
| Author ID | The ID of the author. |
| Text | The text of the comment. |
| Updated data | The date this comment was updated. |
| Created data | The date this comment was created. |
| Folder ID | The ID of the related task. Either `Folder ID` or `Task ID` is displayed. |
| Task ID | The ID of the related folder. Either `Folder ID` or `Task ID` is displayed. |

---
