---
url: 'https://docs.workato.com/en/connectors/openai/business-actions.md'
description: >-
  Use the pre-configured OpenAI business actions in Workato to analyze,
  categorize, parse, translate, summarize text, and draft email without writing
  prompts.
---

# OpenAI - Business actions

We have created common business actions that allow you to get a jump start on using AI in your recipes. These actions are pre-configured, allowing you to immediately start gaining value from OpenAI's models without needing to create or fine-tune the prompts yourself. OpenAI models also enable you to use the [conversations endpoint](/en/connectors/openai/chatgpt-conversation).

You can use the **Model** drop-down menu to select the OpenAI model you plan to use. You can click into the **Model** field and enter the model if it isn't listed. The model defaults to GPT3.5-Turbo if left blank.

Workato supports the following actions:

- Analyze text
- Categorize text
- Draft email
- Parse text
- Translate text
- Summarize text

## Analyze text

![Analyze text action](/assets/analyse-text.uV4qtzXd.png)_Analyze text action_

Use the analyze text action to help you easily understand specific information from a given piece of text. It aims to aid in knowledge retrieval tasks and prioritizing the importance of the provided input. If there is no answer found in the text, the action outputs an empty datapill.

Some common use cases include content summarization and sentiment analysis. A user can quickly generate action items from a meeting transcript, title and hints for documents, and even descriptions/hints for technical briefs.

## Categorize text

![Categorize text action](/assets/categorise-text.Cez4wtTA.png)_Categorize text action_

The categorize text action enables you to classify or organize text data based on predefined categories automatically. For common categories, you can omit the rules, but in general, we recommend configuring a clear rule description to aid with classification.

This action allows you to efficiently sort, group, or route incoming text information to streamline your business processes. Some possible workflows it can augment are customer support ticket routing, content tagging, spam filtering, and product classification.

## Draft email

![Draft email action](/assets/draft-email.CgQ1IY0L.png)_Draft email action_

The draft email action allows you to create personalized emails using a visual interface without writing code. This action simplifies composing and sending customized emails to individuals or groups, automating your communication workflows.

You can use this action in marketing and sales workflows to draft personalized emails. It can help with lead nurturing with different types of emails depending on the sales funnel stage, with the added user-specific context of past emails or other data. This action is also useful for marketing campaigns and event reminders that require minimal but necessary customization across various campaigns/events.

## Parse text

![Parse text action](/assets/parse-text.BSZH-UmE.png)_Parse text action_

The parse text action enables you to extract structured data from unstructured text without requiring any coding skills. It allows you to identify and extract specific information from text documents, emails, or other textual sources. This information can include names, addresses, dates, product details, and more.

You can use this action as a part of your lead generation workflows to extract customer information from incoming text messages, chat conversations, or social media posts to capture and categorize leads.

## Translate text

![Translate text action](/assets/translate-text.52WmbRTs.png)_Translate text action_

The translate text action empowers you to automatically translate text from one language to another, enabling efficient communication across language barriers. With this action, you can automate the translation process and easily incorporate multilingual capabilities into your workflows.

Users can easily translate support tickets or inquiries from different languages into a common language, and generate localized content for websites and documents. It can also help with changing marketing assets across languages with ease.

## Summarize text

![Summarize text action](/assets/summarize-text.CZVL3pM_.png)_Translate text action_

The summarize text action allows you to summarize long textual information easily. This action enables you to obtain summaries from any source and define the length of the output summary.

This action is versatile and can be used to augment multiple workflows across various departments within an organization. For example, you can use this action in sales workflows to summarize call transcripts and long email threads. Customer support teams can also use this action to quickly summarize long support tickets or product release notes into concise bullet points.

---
