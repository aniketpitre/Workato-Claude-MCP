---
url: 'https://docs.workato.com/en/agentic/agentx-support/ai-agents/localization.md'
description: Translate AI agent content to multiple languages
---

# AgentX Support - Localization

You can export an AI agent's text content for translation into other languages. AgentX Support allows you to export the content to Google Sheets for collaborative editing and sharing.

After your translations are complete and you've defined the target locales for your site, you can import the updated sheet back into AgentX Support.

## Export translations

Complete the following steps to export translations:

1. Select an AI agent.
   
2. Click the icon.
   
3. Select **Export/Import Translations**.
   
4. Select the **Export** operation.
   
5. Optional. Select the **Prefill Auto Translation** checkbox to prefill the sheet with Google Translate values if the translation doesn't exist.
   
   ![Prefill Auto Translation](/assets/prefill-auto-translation.-bAfYZhX.png)_Prefill Auto Translation_
   
6. Click **Submit**.
   
7. Check your email for an invitation to access and edit a Google Sheet that contains the exported translations for your AI agent.
   

## Add translations

Complete the following steps to add translations to the Google Sheet:

1. Add a new column for each target language. For example, add a column labeled `fr` for French, `es` for Spanish, or `de` for German.
   
2. Use the [`GOOGLETRANSLATE` function](https://support.google.com/docs/answer/3093331?hl=en) in the new column.
   
   For example, you can use the formula `=GOOGLETRANSLATE(C2, "en", "fr")`, where:
   
   - `C2` is the cell with the original text
   - `"en"` is the source language (English)
   - `"fr"` is the target language (French)
   
   Drag the formula down the column to apply it to all rows.
   
   ![AI agent translations](/assets/translations.9VEZmM1U.png)_AI agent translations_
   
3. Review and refine the translations for accuracy.
   

## Import translations

Complete the following steps to import translations:

1. Select an AI agent.
   
2. Click the icon.
   
3. Select **Export/Import Translations**.
   
4. Select the **Import** operation.
   
5. Enter the **Sheet Key** and the **Worksheet Title**.
   
   ![Import translations](/assets/import-translations.B7OdVAbL.png)_Import translations_
   
   The sheet key is the long string of characters that appears after `docs.google.com/spreadsheets/d/` and before the next slash in the URL.
   

> **LOCALES AND TRANSLATIONS**
> 
> Locales in the Google Sheet must match the locales you use in your production and deployment environments for the translations to get picked up. If a text doesn't have the corresponding language translation, it defaults to `en_us`.

---
