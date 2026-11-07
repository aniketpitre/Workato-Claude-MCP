---
url: 'https://docs.workato.com/en/connectors/tavily/map-website-action.md'
description: >-
  The Map website action traverses a website starting from a root URL and
  returns a list of discovered URLs.
---

# Tavily - Map website action

The **Map website** action traverses a website starting from a root URL using Tavily and returns a list of discovered URLs.

## Input

| Input field | Description |
| --- | --- |
| URL | Enter the root URL you plan to map from. |
| Instructions | Enter natural-language guidance for the crawler. |
| Select paths | Enter regex path patterns to include. For example, `/docs/.*`. |
| Select domains | Enter regex domain patterns to include. |
| Exclude paths | Enter regex path patterns to exclude. |
| Exclude domains | Enter regex domain patterns to exclude. |
| Include usage | Select whether to include usage information in the response. |

## Output

| Output field | Description |
| --- | --- |
| Base URL | The root URL the map started from. |
| Results | The list of discovered URLs. |
| Response time | The time Tavily took to process the map, in seconds. |
| Usage | The number of credits the map consumed. |
| Request ID | The unique identifier for this map request. |

---
