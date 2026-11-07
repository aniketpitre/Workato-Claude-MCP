---
url: 'https://docs.workato.com/en/workflow-apps/pages-customize.md'
description: >-
  Customize Workflow apps pages with the drag-and-drop page editor using the
  canvas, content and background panel, properties panel, and page data.
---

# Customize a page

The Workflow apps page editor features a drag-and-drop page builder. It allows you to determine the look and feel of your app and create dynamic pages that change in response to user input.

The page editor allows you to [duplicate existing components](/en/workflow-apps/page-components-modify#duplicate-components) and reuse them within your page. This saves time during app development by allowing you to quickly reuse and modify components while maintaining design consistency across your page. The page editor also allows you to [undo or redo actions that modify page layout](/en/workflow-apps/page-components-modify#undo).

The page editor consists of the following parts:

- The [Page canvas](#page-canvas): Resize components, determine layout, and more in the central portion of the editor.
- The [Content and Background panel](#content-and-background-panel): Drag and drop components onto your page from the left panel, add custom colors, and more.
- The [Properties panel](#properties-panel): Customize components by deciding how data displays on your page. You can determine whether components are read-only, editable, and more using the right panel.
- [Page data](#page-data): Map in datapills related to the request, application, or page components to create custom and dynamic forms that change in response to user input using the page data modal (similar to the [datatree](/en/workato-concepts#datatree-and-datapills) in the recipe editor).
- The [preview button](/en/workflow-apps/pages-preview): Preview your designs in real-time to design quality user experiences.

![Page editor](/assets/page-editor.FGY4kpOp.png)_Workflow apps page editor_

## Page canvas

Pages have a grid-style canvas where you can drag and drop components from the palette on the left side of the page. The grid is 12 columns wide and a fixed height by default. This enables you to easily align the components without adjusting every pixel.

![Edit components](/assets/page-edit.DQQ-hQt9.png)_Drag and drop components to customize a Page_

## Content and Background panel

The left panel of the editor contains controls that enable you to determine the content and background of your applications. Read our [page components](/en/workflow-apps/page-components) guide to learn how to customize your Workflow app content.

![Content and background panel](/assets/left-panel.KmyWY6Ga.png)_Content and background panel_

## Properties panel

Customize page components using the **Properties** panel, which displays on the right side of the screen. Select an individual component from the canvas to view its properties.

![Properties panel](/assets/properties-panel.C0k6R2uh.png)_The properties panel_

The set of available properties depends on the [page component](/en/workflow-apps/page-components) type you select. However, all components except display components have the mandatory **Label** property for the text displayed on the component.

## Page data

You can map datapills from the workflow request, application, or page components to create pages that change in response to user input, create dynamic URLs, and more.

Similar to the datatree in the recipe editor, page data is available in a modal at the bottom of the page editor. Drag and drop datapills into the properties panel to customize your pages. Additionally, use page data to [configure **IF** conditions](/en/features/conditions) to control whether page components are editable, visible, or required only under conditions you specify.

![Map page data](/assets/page-data.Bf9ee2CN.png)_Map page data_

Learn more about [using datapills in pages](/en/workflow-apps/pages-datapill).

## Preview a page

The **Preview** button at the top of the Page editor switches your view to preview mode. Previewing a Page enables you to:

- Check how the page would look in the **Workflow apps portal**. Preview mode provides both mobile and tablet views.
- Check the data population of the components from the data columns they're linked to.

![Preview button](/assets/preview-button-2.Cg-F4lcn.png)_Click the preview button to view your page outside of the page editor_

Learn more about [previewing a page](/en/workflow-apps/pages-preview).

> **FURTHER READING**
> 
> Learn how to customize [page components](/en/workflow-apps/page-components) using the properties panel.

---
