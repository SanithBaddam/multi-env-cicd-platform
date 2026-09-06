# Multi-Environment CI/CD Platform

A reusable delivery pattern for containerized services promoted through development, staging, and production with immutable image tags and environment gates.

## Design principles

- Build once, promote the same artifact
- Separate CI from deployment concerns
- Use short-lived cloud identity instead of static credentials
- Require production approvals through protected environments
- Keep deployment configuration versioned and reviewable

## Promotion model

```text
PR -> test -> build -> scan -> dev -> stage -> production approval -> prod
```

This repository contains a small Python service only to exercise the platform. The primary engineering focus is the pipeline, container lifecycle, Kubernetes manifests, and promotion controls.
