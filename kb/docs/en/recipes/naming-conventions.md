---
url: 'https://docs.workato.com/en/recipes/naming-conventions.md'
description: >-
  Apply consistent naming conventions for Workato projects and integration
  assets so teams understand each project's purpose and structure.
---

# Naming conventions

We recommend using clear and consistent naming conventions for your projects and integration assets to ensure that other users can quickly understand what your project involves, the assets it includes, and how it's structured.

> **AVOID SPECIAL CHARACTERS**
> 
> When naming projects and assets, avoid using the following special characters:
> 
> - Single quotes (`'`)
> - Double quotes (`"`)
> - Emojis
> 
> Additionally, avoid including numbers in project codes.

## Projects

Use the following naming convention for projects:

```text
[DEPARTMENT_CODE] [PROJECT_CODE] PROJECT_NAME
```

Replace the following:

- _`DEPARTMENT_CODE`_: A two-character shortcode for the department or team responsible for the project. For example, `HR`.
- _`PROJECT_CODE`_: A two- to five-letter, uppercase, alphabetical code for the project. This value is typically an acronym made from the words in the project name. Don't use numbers, single quotes (`'`), double quotes (`"`), or emojis. For example, `TM`.
- _`PROJECT_NAME`_: A descriptive name for the project. For example, `Talent Management`.

> **UNIQUE PROJECT CODES**
> 
> Ensure that all project codes within a workspace are unique.

### Example

- `[HR] [TM] Talent Management`

## Folders

Use the following naming convention for folders:

```text
[PROJECT_CODE] FOLDER_NAME
```

Replace the following:

- _`PROJECT_CODE`_: A two- to five-letter, uppercase, alphabetical code for the project. This value is typically an acronym made from the words in the project name. Don't use numbers, single quotes (`'`), double quotes (`"`), or emojis. For example, `TM`.
- _`FOLDER_NAME`_: A descriptive name for the folder. For example, `Resume Screening`.

All folder and subfolder names should include the project code to facilitate searching when creating [manifests](/en/recipe-development-lifecycle/export#export-manifests).

### Example

- `[TM] Resume Screening`

### Folder structure

Create folders and subfolders using the following structures:

Simple projects

```text
|-- [DEPARTMENT_CODE] [PROJECT_CODE] PROJECT_NAME
    |-- [PROJECT_CODE] Functions
    |-- [PROJECT_CODE] Recipes
```

Complex projects with subfunctions

```text
|-- [DEPARTMENT_CODE] [PROJECT_CODE] PROJECT_NAME
    |-- [PROJECT_CODE] SUBFUNCTION_NAME_1
        |-- [PROJECT_CODE] Functions
        |-- [PROJECT_CODE] Recipes
    |-- [PROJECT_CODE] SUBFUNCTION_NAME_2
        |-- [PROJECT_CODE] Functions
        |-- [PROJECT_CODE] Recipes
```

#### Example

```text
|-- [HR] [TM] Talent Management
    |-- [TM] Resume Screening
        |-- [TM] Functions
        |-- [TM] Recipes
    |-- [TM] Interview Scheduling
        |-- [TM] Functions
        |-- [TM] Recipes
    |-- [TM] Offers
        |-- [TM] Functions
        |-- [TM] Recipes
```

## Connections

Use the following naming convention for connections:

```text
APP_NAME (USERNAME)
```

Replace the following:

- _`APP_NAME`_: The name of the app connector. For example, `Greenhouse`.
- _`USERNAME`_: Optional. The account username if the connection uses a specific user account. For example, `hr@example.com`

Connection names should not include the lifecycle state (for example, whether the connection is for a development or production environment) to ensure they can be used across environments.

### Example

- `Greenhouse (hr@example.com)`

## Recipes

Use the following naming convention for recipes:

```text
PROJECT_CODE ASSET_CODE | RECIPE_SEQUENCE_NUMBER RECIPE_NAME
```

Replace the following:

- _`PROJECT_CODE`_: A two- to five-letter, uppercase, alphabetical code for the project. This value is typically an acronym made from the words in the project name. Don't use numbers, single quotes (`'`), double quotes (`"`), or emojis. For example, `TM`.
  
- _`ASSET_CODE`_: An acronym specifying the recipe type. All recipes should have an asset type in the recipe name to confirm that the builder intended the recipe to be of this asset type.
  
- _`RECIPE_SEQUENCE_NUMBER`_: Optional. If your recipes must run sequentially, you can indicate the sequence or order of the recipes. This especially applies to bot recipes but isn't required if your recipes aren't required to run sequentially.
  
- _`RECIPE_NAME`_: A descriptive name that communicates what the recipe is supposed to achieve.
  

Refer to the following table for guidance on labeling the different types of recipes you might have:

| Asset type | Asset code | Description |
| --- | --- | --- |
| Recipe | REC | Core Workato recipe. |
| Global function | GF | Recipe triggered by another recipe. Designed for reuse across automation projects. |
| Local function | LF | Recipe triggered by another recipe. Designed for modular development within the same project. |
| API endpoint | API | Recipe with an API trigger. |

### Example

- `[TM] REC | 1. New application detected in Greenhouse`

---
