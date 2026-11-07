---
url: 'https://docs.workato.com/en/connectors/wrike/search-projects-action.md'
description: >-
  The Search projects action in the Wrike connector retrieves up to 100 projects
  that match your search criteria from your Wrike instance.
---

# Wrike - Search projects action

Projects are one of the main ways to organize, manage, and report on work within Wrike. In essence, Wrike projects are folders with additional properties.

This action retrieves a list of projects that matches your search criteria. Only records in your Wrike instance that match all the criteria will be returned. A maximum of 100 projects can be retrieved per job.

![Search projects action](/assets/search-projects-action.CreW7imA.png)_Search projects action_

## Input

| Input field | Description |
| --- | --- |
| Custom field list | Select a custom field to open the corresponding input fields. This will be blank by default. |
| Metadata | The metadata details to use in your search. You can define metadata with a metadata source list or manually input the `Key`/`Value` pair information. |
| Permalink | The link to open the project in a web workspace. This is only accessible if the user has the appropriate access. |
| Descendants | Select `Yes` to add all descendant projects to search scope, otherwise select `No`. |
| Retrieve deleted projects only | Select `True` to return deleted projects only, otherwise select `False`. |
| Updated date | Retrieve projects created after this date. |

## Output

| Output field | Description |
| --- | --- |
| Project ID | The ID of the project. |
| Account ID | The ID of the account. |
| Title | The title of the project. |
| Updated date | The date this project was updated. |
| Created date | The date this project was created. |
| Description | The description of the project. Will be blank if not specified. |
| Users who share the project | The list of users who share the project.
<table><tbody><tr><td>User ID</td><td>The ID of the user who shares this project.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of users retrieved.</td></tr></tbody></table>

 |
| Parent project | The list of parent projects of this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the parent project.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of parent projects retrieved.</td></tr></tbody></table>

 |
| Child project | The list of child projects to this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the child project.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of child projects retrieved.</td></tr></tbody></table>

 |
| Super parent project | The list of super parent project to this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the super parent project.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of super parent projects retrieved.</td></tr></tbody></table>

 |
| Scope | The scope of the project. |
| Has attachments | Indicates if the project has attachments. |
| Permalink | The link to open the project in a web workspace. This is only accessible if the user has the appropriate access. |
| Workflow ID | The ID of the project workflow. |
| Metadata | The metadata of this project. The metadata list size corresponds to the number of metadata entries retrieved. |
| Project | The project properties of this project.

<table><tbody><tr><td>Author</td><td>The author who created the project.</td></tr><tr><td>Owner ID</td><td>The list of IDs of project owners.<table><tbody><tr><td>User ID</td><td>The user ID of the project owner.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of project owners retrieved.</td></tr></tbody></table></td></tr><tr><td>Status</td><td>The status of the project.</td></tr><tr><td>Start date</td><td>The date this project was started.</td></tr><tr><td>End date</td><td>The date this project was ended.</td></tr><tr><td>Created date</td><td>The date this project was created.</td></tr><tr><td>Completed date</td><td>The date this project was completed.</td></tr></tbody></table>

 |
| Custom fields | Includes data from custom fields. |
| List size | The size of the list, corresponding to the number of projects retrieved. |

---
