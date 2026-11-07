---
url: 'https://docs.workato.com/en/features/project-properties-faq.md'
description: >-
  Answers to common questions about project properties in Workato, including
  name conflicts and how moving recipes between projects affects values.
---

# Project properties FAQ

## What happens when environment and project properties share the same name?

Environment properties and project properties can have the same name. In this situation, you must make sure to select the appropriate property from the datatree yourself.

Workato does not facilitate automatic transfers of properties between environmental and project levels, whether it's from environmental to project or vice versa.

## What if project properties have the same name? How does Workato solve for this conflict?

Workato does not allow you to have multiple project properties with identical names within the same project. However, you can have multiple recipes that have project properties with identical names if they belong to separate projects.

Because the scope of each recipe is isolated by the project, there is no conflict between the project properties; the recipes simply use the project properties within their own projects and are unaffected by properties outside their parent project.

However, consider a scenario where you move a recipe from one project to another, and the new project contains a project property with an identical name to one already utilized by the recipe. In this situation, the recipe uses the value of the property from the new project automatically.

---
