---
url: >-
  https://docs.workato.com/en/oem/embedded-environments/migrate-embedded-environments.md
description: >-
  Adopt Embedded Environments by migrating existing customer workspaces into
  isolated Development, Test, and Production environments.
---

# Adopt the Embedded Environments feature

Embedded Environments enhance your organization's agility, reliability, and preparedness for future technological advancements.

## Migration

Contact your Customer Success Manager for more information if you plan to use Environments for your customers.

> **MIGRATION EXPERIENCE**
> 
> When you provision environments for an existing customer, their current workspace assets (recipes, connections, and projects) automatically transition to the **Production** environment without affecting active recipes. The newly provisioned **Development** and **Test** environments are empty. If this automatic setup meets your requirements, you can proceed with the update by following the steps in the [Provision Environments for existing customers](/en/oem/embedded-environments/provision-embedded-environments#provision-environments-for-existing-customers-existing-customers) section.
> 
> If you require a custom approach for asset distribution across environments, we encourage you to contact your Customer Success Manager to explore available migration options that align with your operational requirements.

## Embedded Environments benefits

The Environments feature enhances the customer experience by improving organization and testing processes. Environments also provide a structured approach to manage and test integrations, helping to meet the organizational requirements of customers and partners.

Embedded Environments eliminate confusion and prevent the creation of unnecessary isolated workspaces of the same Embedded Customer (EC).

Other benefits include:

- **CI/CD integration:** Environments streamline CI/CD processes at the EC level with a user-friendly UI that automates project deployments.
  
- **Efficient deployment mechanics:** When deploying updates, recipes in the target environment are updated with the new changes without interrupting their operation. This means that during deployment, changes in the recipe logic are detected. If there are no changes, the recipe does not overwrite the target Environment. When there are changes, the recipe in the target environment overwrites the existing logic with the new logic. Recipes don't stop during this process.
  
- **Connection authentication:** When deploying a connection to another environment, initial authentication suffices. Future deployments of the same connection will not require re-authentication. You can choose to maintain isolated connections across Development, Test, and Production environments. Alternatively, you can use a single connection across all environments based on your preference, offering both isolation and convenience in connection management.
  
- **Clarification:** Increased project organization that reduces confusion and prevents the creation of numerous isolated ECs within a single customer.
  
- **Role based access control (RBAC):** Collaborators can have different permissions for different environments using Workato's RBAC feature. This ensures Environments compatibility with the current processes your customers are using.
  
- **Unified Workspace:** The Environments UI and APIs enable users to access and manage three different isolated workspaces individually.
  
- **Enterprise requirements:** Enterprise-level ECs use staging and live environments to update recipes without overwriting those in production.
  
- **Administrative efficiency:** You can manage all Environments under a single Admin workspace to simplify administrative tasks. This allows you to avoid creating multiple Admin workspaces.
  
- **Backward compatibility:** Environments is implemented as a provisioning flag that ensures all existing workflows remain functional without disruptions, offering a safe upgrade path.
  
- **Isolation and unique identifiers:** Each environment is completely isolated and acts as a different workspace. This isolation extends to the assets within each environment, ensuring that the same recipe has different identifiers in Development, Test, and Production for accurate tracking and management.
  
- **Cost-Effective connection management:** The development (DEV), test (TEST), and production (PROD) environments are fully isolated, enabling you to set up connections within the environment workspaces with different credentials. These connections are billed as instances of the same connection if they share the same path and name. This ensures you are billed only once for a connection, even if the connection operates under different circumstances across environments.
  

## Audit log streaming

Multiple Admin workspace accounts ensure that customer data in specific customer workspaces (distinct from lifecycle stages) streams to the correct destination. This is especially important if you have an Admin workspace account with an audit log streaming configuration inherited by all customers nested under it.

After you migrate the customer to Environments, all events are sent to the Development, Test, and Production environments. The `environment_type` field identifies the environment where the event occurred.
