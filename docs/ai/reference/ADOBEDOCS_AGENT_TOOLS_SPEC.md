# AdobeDocs Agent Tool Specification

Purpose: Define tools that AI agents should use when interacting with
Adobe Experience League documentation repositories.

These tools allow orchestrator agents and specialist agents to
systematically search and retrieve authoritative documentation.

## Tool: adobedocs-search

Search AdobeDocs repositories for documentation topics.

Input: - keywords - repository (optional)

Example:

adobedocs-search("dispatcher caching")

Expected behavior:

-   Search GitHub repository contents
-   Return file paths and titles
-   Rank by relevance

## Tool: adobedocs-open-file

Retrieve the content of a documentation markdown file.

Input:

-   repository
-   file_path

Example:

adobedocs-open-file( repository="experience-manager-cloud-service.en",
file_path="help/implementing/developing/components/sling-models.md" )

Output:

-   Markdown content
-   Metadata headers
-   Section headings

## Tool: adobedocs-find-topic

Locate documentation pages related to a concept.

Input:

-   concept

Example:

adobedocs-find-topic("AEM dispatcher cache invalidation")

Expected behavior:

1.  Identify relevant repositories
2.  Locate candidate markdown documents
3.  Return ranked matches

## Agent Usage Workflow

Agents should:

1.  Identify the topic or technical problem
2.  Search AdobeDocs repositories
3.  Read relevant documentation files
4.  Extract architecture patterns and best practices
5.  Apply these patterns when generating implementation guidance

This ensures AI-generated solutions align with official Adobe
recommendations.
