---
url: 'https://docs.workato.com/en/accelerator-aiml-assets.md'
description: >-
  Reference for the AIML accelerator asset package, including recipes, lookup
  tables, and connections you install into your Workato workspace.
---

# AIML accelerator assets

This accelerator's assets includes the following file, and its components:

- [aiml-accelerator.zip](#main)

## aiml-accelerator.zip

This is the core asset package that you must install into your Workato workspace:

- 10 recipes
  
  - 4 API recipes (all active)
  - 5 function recipes (4 active, 1 optional)
  - 1 standard recipe (only to load schema, one-time use, optional)
- 2 lookup tables
  
  - AIML | Data Fields
  - AIML | Model Profile
- 4 connections
  
  - AIML | CON-001 - AIML accelerator SDK
  - AIML | CON-002 - SageMaker
  - AIML | CON-003 - Amazon S3
  - AIML | CON-004 - Snowflake
- 2 connector SDKs
  
  - AI/ML Accelerator
  - Amazon SageMaker
- 4 API Endpoints
  
  - train\_ml\_model.api\_endpoint.json
  - get\_prediction.api\_endpoint.json
  - get\_model\_identifiers\_and\_schema.api\_endpoint.json
  - aiml\_call\_001\_stage\_training\_data.api\_endpoint.json
- 2 properties
  
  - aiml.storage
  - aiml.platform

---
