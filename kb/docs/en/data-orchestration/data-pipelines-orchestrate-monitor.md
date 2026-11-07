---
url: >-
  https://docs.workato.com/en/data-orchestration/data-pipelines-orchestrate-monitor.md
description: >-
  Orchestrate and monitor data pipelines in Workato to design, automate, and
  manage data workflows and track pipeline health.
---

# Orchestrate and monitor data pipelines

Workato offers robust tools that enable you to orchestrate data pipelines and monitor pipeline health. These tools facilitate the seamless data flow between various systems, applications, and databases. These tools allow you to design, automate, and manage complex data workflows.

## Data pipeline orchestration tools

- Designing and managing data flows
  
- Workato provides a visual workflow ([recipe](/en/workato-concepts#recipes)) builder that allows you to design data pipelines using a drag-and-drop interface. You can create workflow sequences by connecting different [actions](/en/workato-concepts#steps-and-actions), [triggers](/en/workato-concepts#triggers), and transformations using visual elements.
  
- Conditional execution
  
- Workato's data pipeline orchestration tools support conditional logic and branching, allowing you to create dynamic workflows that adapt to different scenarios and conditions. You can define rules and conditions to route data based on specific criteria, ensuring that it is processed and handled appropriately.
  
- Custom error handling
  
- Workato enables you to design custom [error handling logic](/en/recipes/steps#handle-errors-step) within your recipes. This can include conditional actions based on the type of error, such as retrying a failed step, sending notification messages, or executing alternative workflows to manage the exception.
  

## Monitoring tools and dashboards

Workato provides robust monitoring tools and dashboards to facilitate efficient data orchestration processes. These tools are essential for tracking data flows, identifying issues, and ensuring smooth operations.

- Real-time monitoring of data pipelines
  
- Workato offers real-time monitoring capabilities that automatically [detect errors](/en/recipes/best-practices-error-handling) that occur at any step of the workflow. This includes HTTP errors from web services, data validation errors, and system-specific errors from integrated applications. When errors are detected, Workato can halt the recipe's execution or trigger predefined error handling procedures. This ensures that any issues or bottlenecks are identified promptly, minimizing potential disruptions.
  
- Dashboard
  
- The Workato [Dashboard](/en/features/admin-dashboard) offers a comprehensive view of trends, outliers, and recipe issues, allowing users to efficiently address problems as they occur. It includes sections like Jobs graph, Recipe details table, Plan usage, and App connection overview. The dashboard also provides operational metrics for a 360° view of the recipes in a workspace.
  
- Notifications and alerts
  
- Workato enables the configuration of [automatic notifications and alerts](/en/recipes/error-notifications#trigger-errors) in response to errors. This ensures that the right team members are informed about issues promptly. Notifications are sent to recipients you specify through email.
  

## Auditing and logging

Observability is a key aspect of Workato's data orchestration solution. You can leverage our [logging service](/en/features/logging-service) and [job report](/en/recipes/jobs) to gain insights into the performance and status of your data orchestration pipelines. This ensures transparency and facilitates proactive monitoring and issue resolution.

- Job history and debugging
  
- Workato provides a comprehensive [job history](/en/recipes/jobs#viewing-job-reports) for each recipe execution, including successful runs and errors. This detailed execution log helps you [debug](/en/recipes/job-debug-tracing) your recipes by offering insights into the data and conditions present at the time of the error.
  
- Audit trails
  
- Workato logs user activities in the [Activity audit log](/en/features/activity-audit-log#activity-audit-log), providing an audit trail that administrators can review to track changes, monitor usage, and ensure compliance with security policies.
  
- Audit log streaming
  
- Workato provides tools for [streaming Activity audit logs](/en/features/activity-audit-log-streaming) into centralized monitoring tools like Datadog, Splunk, and more. You can configure this feature for real-time monitoring. This is useful if you are working with centralized operations, especially as the number of automations grows.
