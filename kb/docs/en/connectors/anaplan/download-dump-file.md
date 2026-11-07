---
url: 'https://docs.workato.com/en/connectors/anaplan/download-dump-file.md'
description: >-
  The Download dump file action in the Anaplan connector lets you download the
  dump file from the latest task of a process and return its contents.
---

# Anaplan - Download dump file action

The **Download dump file** action enables you to download a dump file from Anaplan. Dump files are only available for the latest task of a process in Anaplan.

![Download dump file in Anaplan action](/assets/download-dump-file-action.Deu3C6Nc.png)_Anaplan - Download dump file action_

## Input

| Input field | Description |
| --- | --- |
| Workspace | Select the workspace where your model is located. |
| Model | Select the model you plan to interact with. |
| Process | Select the process you plan to run. |
| Task ID | Input the ID of the process you plan to run. You can find this ID in the output of a **Run process** action. |
| Object ID | Enter the dump file object ID. You can find this ID in the output of a **Run process** action. |

## Output

| Output field | Description |
| --- | --- |
| File contents | The contents of the downloaded dump file from Anaplan. |

---
