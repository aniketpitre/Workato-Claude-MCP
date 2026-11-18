---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/get-presentation-info-action.md
description: >-
  The Get presentation info action retrieves metadata about a PowerPoint
  presentation, including its title, slide count, creator, and last modifier.
---

# Microsoft PowerPoint - Get presentation info action

The **Get presentation info** action retrieves metadata about a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor to view the remaining fields.

| Output field | Description |
| --- | --- |
| Title | The title of the presentation. |
| Author | The author of the presentation, from the presentation's own document properties. |
| Last modified by | The display name and the email address of the user who last modified the presentation, from the presentation's own document properties. Blank if the presentation doesn't have this property set. |
| Created at | The date and time the presentation was created. |
| Last modified at | The date and time of the last change to the presentation. |
| Slide count | The number of slides in the presentation. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| Created by | The display name and email address of the user who created the presentation file, from the file storage account. |
