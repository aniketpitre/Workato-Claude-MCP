---
url: 'https://docs.workato.com/en/insights/dashboards-styling.md'
description: >-
  Style Insights dashboards using display components such as text, containers,
  dividers, and padding to customize their visual appearance.
---

# Styling dashboards

Use display components such as text, containers, and dividers to customize the visual appearance of your dashboard.

## Containers, dividers, and padding

Use containers to group related charts together. Use dividers and padding to separate components.

Add a container

Complete the following steps to add and customize containers in your dashboard:

1. Drag and drop a **Container** from the components panel onto the dashboard canvas.
   
2. Click and drag the edge of the container to resize it.
   
   ![Customize containers](/assets/container-customize.BIkvy_W8.gif)_Customize containers_
   
3. Add additional containers to the dashboard canvas as necessary.
   

Add a divider

Complete the following steps to add and customize dividers in your dashboard:

1. Drag and drop a **Divider** from the components panel onto your dashboard.
   
   ![Add a divider](/assets/divider-customize.Cn0HfgSh.gif)_Add and customize dividers_
   
2. Use the **Component properties** panel to customize the divider's color.
   

Customize padding

You can customize the padding of chart and container components.

Complete the following steps to customize padding in your dashboard:

1. Select a **Container** on the dashboard canvas.
   
2. Modify the padding using the properties panel. Available options are **Large**, **Medium**, **Small**, and **None**.
   
   ![Customize padding](/assets/padding-customize.PEK0h61H.gif)_Customize padding_
   

## Text

Use text to add context or instructions to your dashboard. Text components support specific [Markdown](https://daringfireball.net/projects/markdown/) syntax.

Customize text

Complete the following steps to add and customize text in your dashboard:

1. Drag and drop a **Text** component from the components panel onto your dashboard.
   
2. Enter your text in the properties panel. Text components support specific markdown syntax.
   
   Supported markdown syntax
   
   | Markdown element | Markdown syntax | Description |
   | --- | --- | --- |
   | H1 | `#` | Use H1 headings for structured hierarchies, such as dashboard titles. |
   | H2 | `##` | Use H2 headings for structured hierarchies, such as container titles. |
   | Bold | `**bold text**` | Use bold text to emphasize important information. |
   | Italic | `*italic text*` or `_italic text_` | Use italic text to emphasize important information. |
   | Hyperlink | `[link text](https://www.example.com)` | Use hyperlinks to add links to external resources or related content. |
   | Ordered list | `1. First item` `1. Second item` `1. Third item` | Use ordered lists to group sequential information into numbered steps. |
   | Unordered list | `- First item` `- Second item` `- Third item` | Use unordered lists to group related information into bulleted lists. |
   
   ![Add a text component](/assets/text-customize.BZ4Bv0zr.gif)_Add and customize text_
   
3. Customize the text alignment. Available options are **Left**, **Center**, and **Right**.
   
4. Customize the text color by choosing from a range of pre-defined options.
   

## Color

Customize colors for containers, text, and charts to improve readability and visual consistency.

Customize colors

Complete the following steps to customize colors in your dashboard:

1. Select a container component on your dashboard.
   
2. Customize the container's background and border color by selecting pre-defined options from the properties panel.
   
   ![Customize container colors](/assets/color-customize-2.DSbgbG6L.gif)_Customize container colors_
   

## Best practices for dashboard design

Follow these best practices to design dashboards that are both functional and easy to read:

- Give your dashboard meaningful titles, headings, and chart labels so your audience immediately understands what they're looking at. For example, label a metric `Number of jobs` instead of the default `Count of Rows`.
- Use color to convey meaning so your dashboard is intuitive. For example, use green for successful jobs and red for failures.
- Group related charts in containers, and use dividers and padding to separate components and reduce visual clutter. For example, group high-level job and recipe metrics in one container and usage data in another.
- Apply [filters](/en/insights/filter-groups) at the dashboard or container level so your audience can focus on a specific project, recipe, or date range.

---
