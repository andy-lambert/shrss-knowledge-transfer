# Adobe Experience League Documentation Search Index for AI Agents

Purpose: Provide fast lookup hints that map common Adobe Experience
Manager topics to the most likely AdobeDocs repositories and
directories.

Agents should use this index to reduce search time when locating
canonical Adobe guidance.

## Primary Repositories

-   https://github.com/AdobeDocs/experience-manager-cloud-service.en
-   https://github.com/AdobeDocs/experience-manager-learn.en
-   https://github.com/AdobeDocs/experience-manager-dispatcher.en
-   https://github.com/AdobeDocs/experience-manager-core-components.en
-   https://github.com/AdobeDocs/experience-platform.en

## Topic → Likely Documentation Locations

  --------------------------------------------------------------------------------------------------
  Topic            Repo                                    Typical Path
  ---------------- --------------------------------------- -----------------------------------------
  AEM Architecture experience-manager-cloud-service.en     help/overview/

  Sling Models     experience-manager-cloud-service.en     help/implementing/developing/components

  OSGi             experience-manager-cloud-service.en     help/implementing/deploying
  Configuration                                            

  Dispatcher Setup experience-manager-dispatcher.en        help/using

  Dispatcher       experience-manager-dispatcher.en        help/using/configuring-cache
  Caching                                                  

  Core Components  experience-manager-core-components.en   content

  Content          experience-manager-cloud-service.en     help/assets
  Fragments                                                

  Experience       experience-manager-learn.en             help/cloud-service
  League Tutorials                                         

  Cloud Manager    experience-manager-cloud-service.en     help/implementing/cloud-manager
  Pipelines                                                

  Asset Metadata   experience-manager-cloud-service.en     help/assets

  Headless AEM     experience-manager-cloud-service.en     help/headless

  GraphQL API      experience-manager-cloud-service.en     help/headless/graphql

  Security Best    experience-manager-cloud-service.en     help/security
  Practices                                                

  Performance      experience-manager-cloud-service.en     help/operations
  Tuning                                                   

  Workflow         experience-manager-cloud-service.en     help/operations
  Configuration                                            

  Tagging &        experience-manager-cloud-service.en     help/sites
  Metadata                                                 

  Multi-Site       experience-manager-cloud-service.en     help/sites
  Manager                                                  

  Localization     experience-manager-cloud-service.en     help/sites

  CI/CD Deployment experience-manager-cloud-service.en     help/implementing

  Dispatcher       experience-manager-dispatcher.en        help/security
  Security                                                 
  --------------------------------------------------------------------------------------------------

## Agent Search Strategy

When looking for documentation:

1.  Identify topic keywords.
2.  Locate likely repository using the mapping table.
3.  Search for relevant markdown files under the `help/` directory.
4.  Prefer official documentation over external sources.
5.  Extract patterns and best practices before generating implementation
    guidance.

Agents should treat AdobeDocs repositories as authoritative sources for
architecture, development practices, and operational guidance.
