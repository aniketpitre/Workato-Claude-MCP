---
url: 'https://docs.workato.com/en/workbot-for-teams/adaptive-card-blocks.md'
description: >-
  Build rich Microsoft Teams messages with Workbot Adaptive card blocks that
  combine text, images, buttons, fact sets, and input fields.
---

# Adaptive card blocks for Microsoft Teams

[Adaptive cards](https://adaptivecards.io/) are customizable cards that can contain any combination of text, speech, images, buttons, and input fields.

With Adaptive card blocks, you can build simple or rich messages by customizing the order and appearance of each block, including elements within them.

Blocks can be used in the following Microsoft Teams surfaces:

| Surface | Applicable actions |
| --- | --- |
| Messages | [Post message](/en/workbot-for-teams/workbot-actions#post-message-and-post-simple-message) [Post reply](/en/workbot-for-teams/workbot-actions#post-reply-and-post-simple-reply) |

## Supported blocks

Adaptive card blocks in Workbot for Microsoft Teams support the following block types:

| Blocks | Description |
| --- | --- |
| Text block | Displays Header, Subheader or Body text. To fully customize text styles, choose Custom. Supports markdown. You can also [mention](/en/workbot-for-teams/workbot-actions.html#mentions) users, in that case their names will be displayed in red color like shown below. ![](data:image/png;base64,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)_Example text block_ ![](/assets/text-block-recipe.DLU96SNR.png)_Recipe view_ |
| Image block | Displays an image using a provided public URL. You can control the **Image size** and **Image horizontal alignment**. ![](/assets/image-block-example.B9lg4nVZ.png)_Example image block_ ![](/assets/image-block-recipe.Cl_qVTV9.png)_Recipe view_ |
| Text with thumbnail | Displays text alongside an image thumbnail. Both header text and block text are optional, but at least 1 must be filled. Order can be changed. ![](/assets/text-with-thumbnail-example.CdZgBQAx.png)_Example text with thumbnail block_ ![](/assets/text-with-thumbnail-recipe.BC85yzn2.png)_Recipe view_ |
| Text with button | Displays text alongside a button to the right. A button can either invoke a command or open a URL. Order cannot be changed. ![](/assets/text-with-button-example.BDKH_RuZ.png)_Example text block_ ![](/assets/text-with-button-recipe.BgpWcQq4.png)_Recipe view_ |
| Text with button & thumbnail | Displays a thumbnail, text and button in a single row. Both header text & block text are optional, but at least 1 must be filled. Order cannot be changed. ![](/assets/text-with-button-thumbnail-example.B5Woo8Z6.png)_Example of a Text with button & thumbnail in a repeat block group_ ![](/assets/text-with-button-thumbnail-recipe.DlFBVq16.png)_Recipe view_ |
| Fact set | Displays name-value pairs in 2 columns. ![](/assets/fact-set-example.Bu9yyVic.png)_Example fact set block_ ![](/assets/fact-set-recipe.Dohg7Gwb.png)_Recipe view_ |
| Repeat block group | This special block type is only available only Workato. The repeat block group allows you to define a set of blocks to use as a pattern. By iterating through a list and mapping the list items to the blocks in the pattern, the pattern can be repeated for each item in the list. For example, display a different icon, details, and button for each category your bot can assist with. ![](/assets/repeat-blocks-example.CtX41XlH.png)_Example of a Text with button & thumbnail in a repeat block group_ ![](/assets/repeat-blocks-recipe.C8vOj3qO.png)_Recipe view_ |
| Text input | Displays a single-line or multi-line text area for users to enter text input. On button submit, the text input is passed via the text input parameter. ![](data:image/png;base64,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)_Example text input_ ![](/assets/text-input-recipe.L7nuSaLu.png)_Recipe view_ |
| Choice set | Displays radio button options, or drop-down menu options. ![](/assets/choice-set-example.DXKoKAlt.gif)_Example choice set_ ![](/assets/choice-set-recipe.CSQbTbi3.png)_Recipe view_ |
| Toggle input | Displays a single checkbox that passes `true` or `false` when checked and unchecked respectively. On submission, `true` or `false` is passed via the toggle input parameter. ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXYAAABFCAMAAABpGT3gAAAAllBMVEX5+Pf////GxsXo6OcgHx/Y19b29fXx8O+rqqpIR0dcW1uPjY2HhoZ4dna2tbSjoqGnp6bU09IkJCR9fHxvbm7X1tVTUlLh4N+/vbyamZnLy8piYWFYWFja2dj08/Ls6+vQz8+wrq6kpKM9PDyLi4ppaWhmZmUwLy7BwMC6ubhPTU3m5eSTkpJzcXErKiqDgoFGRkY1NDSPVZZ1AAAEbklEQVR42u3c2XbaSBAG4N9V1fSmlrAEEvsO3u3k/V9uLiRiJ/EkOBmTk3H9VwIkLj6K6m7pSIDmnLm46F1cXFwohLIru0bZlV2j7MquUfa/ip2DiETy5idHOpGrxACA5Zpf3+d6Joe5Ip/GXjAvT2CfzZv0tACAy9nq5Sfm4Ui9GTYPWU+VT2J3AE5gDwwKr5X587E99LKoyG9iv0tXVzuL0e3VriYAWN9KPUF+K5X9wt6kh0EkPzls0NvtrmfyKScRcbiuH9MdsD7cKfLJvZ3Im2XTm9cTc5vb/DMBQGN799VlPflS7Zx2yzRtQN5sHuzddNIw1lMmbzDZN4u4600OjRqf3tsX5I3dTLdC68MSHAgALqv6MTWDcGO7IVUe2KYIkDeXM0MHbnazq8DkDe5FRJJdJ6vGb2sy48QcyA2W4BkBaMKo55K1o+mA2yF1CRzZF5WLm+W+v6COvVoo7i+xxyc7+kwrn9v+IwEw9YRTsgDV8663P7Mj3x8MhxsbA69uJ7jejnrza9zsWY3fxm5m2/GMFv3tp2JGABbjq8F9uqzlNsf37E1dLbDezorAtpL1Yv3pcbpS9t9ZpTbHYVRzLnZ2zLupzgLPzL6srh4HusD/E01Go+zKrlF2Zdcou7JrlF3Zlb2NHWddxnq+/Hzs4/yyS75Ro7OxZ5fPm8eNflmWfQAAT4cKdzb2PuyAXvkKypTxXdnR7yv7H2EfVlU9H8ynQyCjflnWTGW5HdpBWZJqvg87T4fDLYEH3O+DB9y+SxlsNexea95hSCUMKwse8LCy1AfXZZmBMnBdluVWB9p3ajI4sttqUg15OgS17FrpZ2EHVfcYThlZBspgB32l/C+WS8et5+XS1+xcE5CVZZaB6+2Q67Ic6IL2d08ObI4nBzZqeT52jbIru0bZlV2j7MquUXZlV3ZlV3Zl15yXnYMI0fdX6IgAcHzrqTFy//aBiLT3zsevbrR3H+FW1lfYR0fjF8kN6NRrpSb/5o3i1Wsg5A2HVx5IED80OwcJjCghMkAijqJ4Ywsb2xolkWRN9BJBUcTBeAlsor8Jkq4JXKBIkqzJnUjhWnzjJVkSoSO7cyKp7ychwvkbL0JOJDCJ/L/xX20y3hABICIHTtxVe4QZ26Ip2r2iBTnzZDE2FGFjExlmbJ4sTA4icIFIcGRyFGwLe/wP5KYrfhKRZJ0QnDcxNCm2pR6TNd61d8d+vGq3SYRG3LWItslwYQtL4gCYFcCFyYGVIQJG8xFgi1WOZ/aCQS07VmbEx5+UQ7I4Pv7EeQPnDXkK1Hb7mCyJiMQPyZ4bOHL0oto7diA3X6p9DBuZHDhyW+0duwPFl+wci67Lj03X/b9i57APHJONgWNg491H7e3Gy55sans7SFzHzqltuyQSYZIIgfbiTdu3TQ5wSJwkPVe7E8LYdI0lGSfefMsOJ7Gb25AEdiJ+FfkjsX+TH04Z24Z9whzn7RPPj7xcIpEfPrzqVPafPwJL2TXKruwaZVd2jbL/Xez/ALYhQxbLA2JfAAAAAElFTkSuQmCC)_Example toggle input_ ![](/assets/toggle-input-recipe.DY_9C9sV.png)_Recipe view_ |
| Date input | Displays a date picker. On submission, the date picker is passed via a date parameter. You can customize the name of this date parameter. ![](/assets/date-input-example.C-Ard1wN.gif)_Example date input_ ![](/assets/date-input-recipe.6TyzHFkn.png)_Recipe view_ |
| Actions set | A block that can contain bot command buttons, URL buttons, or showcards. At least one bot command button is required if input blocks are present in your message. This is so that these parameters can be passed onto the downstream bot recipe on button submissions. Any bot command button will pass _all_ input parameter values present in its containing message, regardless of the position of the button in the message. ![](/assets/action-set-example.DH_-pSCM.png)_Example action set with button and show card_ ![](/assets/action-set-recipe.CpDfFhiu.png)_Recipe view_ |
| Column set | Built for advanced users who want full customizability of their message. Each column set can hold multiple columns, occupying the entire row in the message. Each column can contain text blocks, image blocks, fact sets, or actions. Columns grow from left to right, based on the order they are in inside the column set. ![](/assets/column-set.Ds4xV1UI.png)_Anatomy of a column set_ ![](/assets/action-set-example.DH_-pSCM.png)_Example column set_ ![](/assets/action-set-recipe.CpDfFhiu.png)_Recipe view_ To see how column sets, columns, and column items can be arranged to form a message, head over to [Microsoft's Adaptive Cards Designer](https://adaptivecards.io/designer/). |

## Best practices

### Use column set and column blocks to fully customize message structure

You have limited control over content styles for the following Workato-only templates:

- Text with thumbnail
- Text with button
- Text with button & thumbnail

To fully customize message structure, use column set and column blocks.

### Fix your columns

You can build columns dynamically. However, this approach can quickly become unmanageable because Workato does not set hard quotas on the number of columns you can include. Microsoft Teams does not reject messages that exceed its rendering frame, but their appearance may be compromised.

We highly recommend an approach where you have a fixed set of columns and then build dynamic (or static) content inside the columns.

### Determine message width

Select the width of your message from the available options. This setting is global and applies to all adaptive card blocks in your message.

Available options include:

- Default
- Full

**Determine message width**

![Determine message width](/assets/message-width.Cmb_Xmaj.png)_Determine message width_

**Default width message**

![Default width](/assets/message-width-default.BkeGEqaT.png)_Default width message in Microsoft Teams_

**Full width message**

![Full width](/assets/message-width-full.CqA7SWud.png)_Full width message in Microsoft teams_

### Require user input

You can mark specific adaptive card block types that capture user input as required. If a user fails to provide input for a required field in these blocks, Workbot sends an error message. This feature supports marking fields as mandatory for the following block types:

- **Text input**
- **Date input**
- **Time input**
- **Toggle input**
- **Choice set**

### Validate user input

Additionally, you can create logic to validate input to ensure it matches the expected format. The following adaptive block type supports user input validation:

- **Text input**

#### How to mark input as required and validate user input

The following example demonstrates how to mark input as required and configure Workbot to validate user input for **Text input**. This is useful when you must collect specific data from your users, such as email addresses, phone numbers, and more.

1. Add a **Post reply** or **Post message** step to your recipe.
   
2. Click **+** (plus) **Add block**, and select **User input** from the **Type** drop-down.
   
3. Fill in the following fields:
   
   - Parameter name
     
   - _Required_. This must be unique and contain no spaces. Define this parameter in the downstream recipe steps to use its value.
     
   - Label
     
   - Provide a label for this input.
     
   - Hint
     
   - Provide a hint for this input.
     
   - Is multiline?
     
   - Select **Yes** to allow multiple lines of input. Defaults to single-line input.
     
   - Placeholder
     
   - Determine a placeholder value. This is not visible if you set an **Initial value**.
     
   - Initial value
     
   - Set an initial value.
     
   - Required
     
   - Select **Yes** to set this input as mandatory.
     
   - Validation pattern
     
   - Regular expression (regex) indicating the required format of this text input. For example, you can use a regex to validate email addresses, phone numbers, and more. [Learn more about configuring regex](https://www.regular-expressions.info/).
     
     - Regex for email addresses:
     
     ```
     ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
     ```
     
     - Regex for phone numbers:
     
     ```
     ^\+?\d{1,3}[\s-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$
     ```
     
   - Error message
     
   - Create an error message. Workbot displays this message to users when required input is missing or invalid.
     
   - Separator
     
   - Add a separator above this input element.
     
   
   ![Validate user input](/assets/workbot-teams-adaptive-blocks-validation.aQ-UsoCO.png)_Validate user input and mark as required_
   

#### Example in Microsoft teams

The following image demonstrates how error messages render in Microsoft Teams for missing or invalid input:

![Error messages in Microsoft teams](/assets/ms-teams-error-messages.qPwwLz37.png)_Example error messages_

## Limitations

### Repeat blocks and input blocks

- Repeat blocks and input blocks are not available inside columns
- Repeat blocks are not available within repeat blocks
- Column sets are not available inside columns

---
