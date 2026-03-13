# Technical Knowledge Transfer Agenda

**NOTE:** All topics will be contextual to current SHRSS implementation

**Presenters:**

- Andy Lambert -- Principal technical architect, Adobe

  - AEMaaCS application and cloud service paradigms, DevOps instructions, best practices

- Vinay S A -- AEM technical architect, Adobe

  - SHRSS implementation details, backend code, configurations, AEM authoring components

- Deepkamal Narang -- Senior technical consultant, Adobe

  - Frontend code, UX implementation, AEM authoring components

**Overview (Andy)**

- Cloud services ecosystem (Admin console -\> Cloud Manager)

- AEMaaCS architecture

- AEMaaCS cloud manager paradigms

**AEM Application Development**

- Development tooling/IDEs (**Andy/Vinay**)

- Code structure (**Andy/Vinay**)

  - Overview of Maven/POM configuration/dependency management

  - Main modules (core, ui.apps, ui.content, ui.config, etc.)

  - Other configs (CDN, maintenance tasks, log forwarding)

- AEM authoring components (**Andy -\> Vinay**)

  - Core components

    - Extending

      - Example: hrccard

  - Dialogs

  - Clientlibs

  - Sling models

    - Use-API

  - Extending

  - Debugging/troubleshooting

  - Best practices

    - File/folder structure

    - Clientlibs definition/categories

- Backend (**Andy -\> Vinay**)

  - Run modes, environment variables and secrets

  - Repo initialization

  - OSGi component implementations (servlet, Sling models, services, listeners, etc. as applicable based on what\'s been implemented to date)

  - OSGi configurations

  - Debugging/troubleshooting

  - Best practices

- Frontend (**Deep**)

  - Client libraries (clientlibs)

  - Webpack, NPM, etc.

  - Debugging/troubleshooting

  - Best practices

- External Integrations (**Vinay**)

- Dispatcher/CDN (**Andy -\> Vinay**)
- General AEM Troubleshooting/Debugging (**Andy/Vinay**)

  - Cache issues

    - Check distribution queues and logs via AEM distribution console

  - Unhandled exceptions/500 errors

    - Analyze AEM logs
- Developer Console (https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console)
- Development considerations for AEMaaCS (**Andy**)

  - Idempotency

  - Distributed, Mongo based repository

  - Best practices

**Change and Release Management (Andy)**

- Source Control Management

  - Aligning code changes to Jira

  - Git branching strategy

  - Cutting a release and production deployment

**DevOps (Andy)**

- User/Group/Permission Management (Admin Console (IAM) -\> native AEM groups)

  - Walk-through

    - Create IAM group in admin console

    - Add user with DEV author profile to IAM group

    - Have user log into DEV author

    - Add IAM group to native AEM group

    - View user and IAM group memberships in console
- Cloud Manager

  - Environments

    - Dev, QA, Integration, Stage, Prod

    - Rapid Development Environments (RDE)

    - Preview

  - Run modes, environment variables and secrets

  - Repositories

  - Build pipelines

  - Environment whitelists

  - Content restore

  - Bulk content copy
