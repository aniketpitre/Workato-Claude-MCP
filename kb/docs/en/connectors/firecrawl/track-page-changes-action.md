---
url: 'https://docs.workato.com/en/connectors/firecrawl/track-page-changes-action.md'
description: >-
  Get an early warning when a monitored page changes, with a status of new,
  same, changed, or removed.
---

# Firecrawl - Track page changes action

The **Track page changes** action scrapes a page and returns whether its content changed since the prior scrape in Firecrawl. This action includes markdown in the format it returns and an optional line-level or JSON diff.

## Input

The following input fields are the most commonly used. Refer to the Firecrawl [Change tracking](https://docs.firecrawl.dev/features/change-tracking) documentation for the complete list of input fields.

| Input field | Description |
| --- | --- |
| URL | Enter the absolute URL to track, for example `https://docs.firecrawl.dev`. |
| Diff modes | Optional. Select the diff detail to include. Options are **Git diff** for a line-level diff or **JSON** to compare schema fields. |
| Prompt | Optional. Enter a prompt for JSON diff mode. |
| JSON schema | Optional. Enter a JSON schema for JSON diff mode. The schema is sent to Firecrawl only. Add matching fields in **Custom metadata fields** to get datapills for the extracted data. |
| Only main content | Optional. Select **Yes** or **No** to exclude headers, navigation, and footers from the output. The default is **Yes**. |
| Skip TLS verification | Optional. Select **Yes** or **No** to skip TLS certificate verification. When **Yes**, Firecrawl connects to the target site even if its certificate is invalid, expired, or self-signed. The default is **Yes**. |
| Remove base64 images | Optional. Select **Yes** or **No** to strip base64 images from the markdown output. The default is **Yes**. |
| Block ads | Optional. Select **Yes** or **No** to enable ad and cookie-popup blocking. The default is **Yes**. |
| Store in cache | Optional. Select **Yes** or **No** to store the page in the Firecrawl index. The default is **Yes**. |
| Custom metadata fields | Optional. Add fields to create datapills for additional metadata that the default output doesn't include. |

## Output

| Output field | Description |
| --- | --- |
| Success | A `true` or `false` boolean response that indicates if the scrape completed successfully. |
| Markdown | The page content in markdown. |
| Metadata | The page's metadata, such as its title, description, and status code. |
| Previous scrape at | The date and time of the previous scrape used for comparison. |
| Change status | The page's change status. Options are `new`, `same`, `changed`, or `removed`. |
| Visibility | The page's visibility. Options are `visible` if it's still discoverable through links or a sitemap, or `hidden` if the URL still works but is no longer linked. |
| Diff | The line-level or JSON diff, depending on **Diff modes**. |

---
