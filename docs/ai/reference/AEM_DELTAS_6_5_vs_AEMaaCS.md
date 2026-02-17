# AEM 6.5 / AMS vs AEMaaCS – Delta Tables
**Version:** 1.0.0  
**Last Updated:** 2025-12-29

These tables summarize **practical differences** that routinely impact implementation design.

## Platform Deltas (High-Level)

| Area | AEM 6.5 / AMS (On-Prem / Managed) | AEM as a Cloud Service (AEMaaCS) |
|---|---|---|
| Bootstrap (users/ACLs) | Content packages & manual config are common | RepoInit is the supported approach; Git-delivered |
| Dispatcher | Can be modified per environment | Immutable, Git-driven, Cloud Manager deployed |
| OSGi configuration | Web console used routinely | Git + Cloud Manager pipelines are the norm |
| Index management | Indexes can be edited in repo | Index definitions delivered via SDK / code deployment |
| Filesystem | Often accessible | Not a supported dependency |
| Runtime mutability | High (admins can change many things) | Limited; changes are code/config delivered |
| UI customization | Many legacy overlay patterns still exist | Prefer supported extension points; avoid invasive customization |
| Scaling | Manual planning & ops | Auto scaling characteristics; design for distributed runtime |

## Design Implications (Short Form)

| Concern | 6.5 Approach | AEMaaCS Approach |
|---|---|---|
| “Config drift” | Common without strict governance | Reduced by Git delivery; treat repo as source of truth |
| Long-running jobs | May “work” but risky | Prefer asynchronous processing patterns and jobs |
| Query/index tuning | Direct tuning in environments possible | Tune by code + redeploy; measure/iterate via SDK |
| Admin console hacks | Sometimes tolerated | Avoid; can break during Cloud updates |

