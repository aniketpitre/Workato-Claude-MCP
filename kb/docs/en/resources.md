---
url: 'https://docs.workato.com/en/resources.md'
description: >-
  Learn how Workato resources let you define common files once, including XSD,
  XSLT, and WSDL, and reference them across recipes.
---

# Resources

Resources are assets you can define once and reference across multiple recipes and files. Use resources as a single source of truth for common files, including XSD, XSLT, WSDL, Ruby, JavaScript, Python, and WEL files.

Resources provide the following additional benefits:

- **Version management**: Workato retains the last 100 versions of a resource in the [Versions](/en/resources/resource-management#versioning) tab. You can download and re-upload a previous version to [restore it](/en/resources/resource-management#restore-a-resource-version).
  
- **Security**: Workato parses resources without resolving external references. This protects your environment from potential vulnerabilities. Workato also scans uploaded files for threats and blocks malicious files from view or use.
  
- **Automatic updates**: Recipes automatically update to use the newest version of a resource after it passes security checks.
  

> **RESOURCES ARE LIVE REFERENCES**
> 
> Resource references store static paths to files and resolve the paths at runtime, so changes to a resource's active version or availability immediately affect the assets that consume it.

Refer to the following pages to get started with resources:

- [Recipe integration](/en/resources/recipe-integration): Use a resource as a data source in supported recipe actions.
- [Resource management](/en/resources/resource-management): Upload, view, update, download, delete, move, and version resources using the Workato UI.
- [Resources API](/en/workato-api/static-assets): Manage resources programmatically.

## Role-based access control

You can configure the following resource permissions using collaborator and project roles:

- Full access
  
- Grants all resource permissions.
  
- View
  
- View resources.
  
- Edit
  
- Edit resources.
  
- Create
  
- Create resources.
  
- Delete
  
- Delete resources.
  

Workato's default system roles provide the following permissions:

**Collaborator roles**

| Collaborator role | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Admin | ✔ | ✔ | ✔ | ✔ | ✔ |
| Analyst | ✔ | ✔ | ✔ | ✔ | ✔ |
| Operator | ❌ | ✔ | ❌ | ❌ | ❌ |

**Project roles**

| Project role | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Project Admin | ✔ | ✔ | ✔ | ✔ | ✔ |
| Project Operator | ❌ | ✔ | ❌ | ❌ | ❌ |
| Builder | ✔ | ✔ | ✔ | ✔ | ✔ |
| Advanced Builder | ✔ | ✔ | ✔ | ✔ | ✔ |

## Limitations

Resources enforce the following limits:

| Description | Limit |
| --- | --- |
| Maximum size of a single resource file | 50 MB |
| Maximum combined size of all resources in an environment | 5 GB |
| Maximum number of versions stored per resource | 100 |

---
