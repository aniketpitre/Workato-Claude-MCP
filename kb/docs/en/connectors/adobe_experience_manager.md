---
url: 'https://docs.workato.com/en/connectors/adobe_experience_manager.md'
description: >-
  The Adobe Experience Manager connector lets you manage AEM folders and assets,
  search and update assets, and trigger recipes when assets or folders change.
---

# Adobe Experience Manager

[Adobe Experience Manager (AEM)](https://business.adobe.com/products/experience-manager/adobe-experience-manager.html), is a content management solution for building websites, mobile apps and forms. Use the triggers in the Adobe Experience Manager connector to run recipes when an asset or folder is added in AEM or when an asset is updated. Use the actions in this connector to manage folders and assets.

## API version

This connector uses the [Assets HTTP API](https://experienceleague.adobe.com/docs/experience-manager-65/assets/extending/mac-api-assets.html?lang=en#extending).

## How to connect to Adobe Experience Manager on Workato

| Field | Description |
| --- | --- |
| Connection name | Give this connection a unique name so you can reuse it in other recipes. |
| AEM instance address | The address of your Adobe Experience Manager (AEM) instance. For example, if your AEM instance address is `http://wkto.aem.com:8080`, then enter `http://wkto.aem.com` into this field. If your AEM instance is hosted locally in a private network, you will need to deploy an on-prem agent and select the agent in a later step. |
| Port | Enter the port if there is one associated with your AEM instance. For example, if your AEM instance address is `http://wkto.aem.com:8080`, then your port number is `8080`. If you are unsure of whether there is a port associated with your AEM instance, contact your AEM admin. |
| Username | The username of the user provisioned for Workato. |
| Password | The password of the user provisioned for Workato. |
| Is this app in a private network | If you have deployed the on-prem agent, select the on-prem group. |

## Asset properties

The **Search assets** and **Update assets** actions contain fields where you specify the asset properties and the corresponding values. For example, you can enter `jcr:content/jcr:lastModifiedBy` in the **Property** field to filter the search results to assets that were most recently modified by `bgoh`. ![property search](/assets/property_field.D9MrpOE0.png) When you enter a property, use a forward slash to indicate nested Json objects. For the preceding example, the source code would look similar to this:

```
...
	"jcr_content": {
	...
		"jcr_lastModifiedBy":"bgoh",
      ...
```

> **NOTE**
> 
> Underscores (`_`) are converted to colons (`:`) in the Output tab. When searching or updating a property, you should enter the property name with colons instead of underscores. In the example above, `jcr_content` in the job output corresponds to `jcr:content` in the screenshot.

If you define custom asset metadata in Adobe Experience Manager, these properties will not appear in the datatree as we only cater for the standard asset properties. When that occurs, you must manually create the datapill. Use the **Asset output fields** in the triggers or the **Search assets** action to create a datapill.

1. Navigate to **Test jobs > Output** and copy the Json code.
2. Navigate to **Recipe > Asset output fields > Edit schema** and paste the code.
3. This allows us to take one example of an asset in your AEM instance take the properties we find there as datapills.

When you enter an existing property and a value in the **Update assets** action, the action updates the property with the new value you provided. If the property doesn't exist, this action creates the new property.

---
