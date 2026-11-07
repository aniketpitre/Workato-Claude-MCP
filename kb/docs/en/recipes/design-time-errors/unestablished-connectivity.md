---
url: >-
  https://docs.workato.com/en/recipes/design-time-errors/unestablished-connectivity.md
description: >-
  Learn how to resolve unestablished connectivity errors in Workato recipes
  caused by changed credentials, missing permissions, or wrong configurations.
---

# Unestablished connectivity

Unestablished connectivity errors occur when your recipe cannot establish or maintain a valid connection with external apps or services. These errors prevent the recipe from starting and can occur due to incorrect credentials, permissions, or configurations.

## Common causes of app connection errors

Common reasons for app connection invalidation include:

- App credentials were changed, but you did not update the connection in Workato.
- You lack the appropriate permissions to read/write records.
- Your permissions were modified to a reduced scope.

In these cases, reconnect the app or verify that you have the necessary permissions to resolve the issue.

## Troubleshooting steps

If you experience connection issues, ensure all connections associated with the recipe are correctly established:

1. Select the correct connection from the drop-down menu.
   
2. Assign a unique **Connection name** for easy reference in future recipes.
   
3. Choose the correct **Authentication type**, such as OAuth 2.0, if required.
   

![Establish your connection](/assets/establish-connection.DOJ0k_L-.png)_Establish your connection_

Even if the connection appears established, an invalid connection can prevent the recipe from starting. Review the user account to ensure that it has the required permissions and privileges.

![Review your account](/assets/review-account.BIk9jY1v.png)_Review your account_
