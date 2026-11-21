---
url: 'https://docs.workato.com/en/ai-gateway/access-keys.md'
description: >-
  Create, edit, refresh, and delete the access keys applications use to
  authenticate with Model Gateway.
---

# Access keys

An access key is the credential an application presents to [Model Gateway](/en/ai-gateway). Issue a separate key for each team, project, or application to attribute usage and revoke or rotate access without touching other clients.

## Create an access key

Each key grants access to one or more routes, which determine the provider and model the key can use.

> **PREREQUISITES**
> 
> You must create at least one [route](/en/ai-gateway/routes#create-a-route) before you create an access key.

Complete the following steps to create an access key:

1. Go to **Model Gateway > Keys**.
   
2. Click **\+ Create key**.
   
3. Enter a descriptive name in the **Name** field.
   
   ![Create key](/assets/create-key.D7zOoMsF.png)_Create key_
   
4. Use the **Location** drop-down menu to select the project where you plan to store this key.
   
5. Optional. Use the **Assigned to** drop-down menu to assign the key to the person who uses it. Leave the field empty for keys that multiple users or services share.
   
   **Workato Identity user**
   
   Select a [Workato Identity](/en/workato-identity) user to link the key to that user. Model Gateway deactivates the key when the user leaves the workspace.
   
   To link the key to a user who isn't listed, click **Add them as an end user**. This opens **Workspace admin > Access control > End users**, where you can [add an end user](/en/workato-identity/add-end-user-manually).
   
   **Email only**
   
   Enter an email address and select it under **Email only** to record who uses the key without linking it. The key stays active when the person leaves.
   
   Click **X** to clear the selection.
   
6. Use the **Route(s)** drop-down menu to select the routes this key can use, then click **OK**. Click **Select all** to select every route. Manage routes in **Model Gateway > Routes**.
   
7. Optional. Use the **Policy** drop-down menu to select a policy for this key. Click **Create policy** to create a policy without leaving the dialog, or manage policies in **Model Gateway > Policies**. Refer to [Create a policy](/en/ai-gateway/policies#create-a-policy) for the field descriptions.
   
   > **SHARED USAGE**
   > 
   > All users who share an access key contribute to the same rate limits and token limits. Issue separate access keys for teams or applications that need independent limits.
   
8. Optional. Enter one or more tags in the **Tags** field. Rules on a rule-based route can match on the tags assigned to a key.
   
9. Optional. Click **Add parameter** to add a key-value pair to this access key, then enter a **Parameter name** and a **Value**. Rules on a rule-based route can match on these parameters to differentiate requests that come from this key. Click **Clear** to remove a parameter.
   
10. Click **Create**.
    
11. Copy the generated key and store it in a safe place. Click **Copy**, then click **Close**.
    
    The **Access key generated** dialog also displays the URL to call and the request body format for the OpenAI-compatible API. Refer to [Test a route](/en/ai-gateway/test-route) for the Anthropic-compatible API. Pass the route ID as the `model` value to select which route serves the request:
    
    ```json
    {
      "model": "<route-id>"
    }
    ```
    
    Refer to [Test a route](/en/ai-gateway/test-route) for a full example request.
    
    > **THE KEY IS DISPLAYED ONCE**
    > 
    > You can't view the generated key again after you close the dialog. Refresh the key to generate a new value if you lose it.
    

The access key displays in the **Keys** list with its routes, policy, creation date, and a masked key value. The assigned email address displays under the key name, with a person icon for a linked Workato Identity user or an envelope icon for an email-only assignment. Use the **Search keys** field to find a key by name.

## Edit an access key

Complete the following steps to edit an access key:

1. Go to **Model Gateway > Keys**.
   
2. Click the **...** (ellipsis) menu for the key you plan to edit, then click **Edit**.
   
   ![Edit key](/assets/edit-key.KOWYOC9J.png)_Edit key_
   
3. Update the **Name**, **Assigned to**, **Route(s)**, **Policy**, **Tags**, or **Parameters** fields, then click **Save**.
   

## Refresh an access key

Refresh an access key to rotate its value. Refreshing generates a new token and revokes access for all current users of the key.

> **CLIENTS MUST BE UPDATED**
> 
> Applications that use the previous token lose access when you refresh a key. You must update each client with the refreshed token to regain access.

Complete the following steps to refresh an access key:

1. Go to **Model Gateway > Keys**.
   
2. Click the **...** (ellipsis) menu for the key you plan to refresh, then click **Refresh**.
   
   ![Refresh key](/assets/refresh-key.u2rPcAr6.png)_Refresh key_
   
3. Click **Refresh token**.
   
4. Copy the refreshed key and store it in a safe place. Click **Copy**, then click **Close**. You can't view the refreshed key again after you close the dialog.
   

## Delete an access key

Complete the following steps to delete an access key:

1. Go to **Model Gateway > Keys**.
   
2. Click the **...** (ellipsis) menu for the key you plan to delete, then click **Delete**.
   
3. Click **Delete** to confirm.
   
   ![Delete key](/assets/delete-key.CY8bdwbZ.png)_Delete key_
   

> **ACCESS IS REVOKED IMMEDIATELY**
> 
> Deleting an access key revokes access for all current users of that key. You can't undo this action.

---
