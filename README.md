# Multi-Environment CI/CD Platform

Reusable delivery pattern for containerized services promoted through development, staging, and production using immutable image tags and environment gates.

## Principles
- Build once and promote the same artifact
- Separate CI from deployment concerns
- Prefer short-lived cloud identity over static credentials
- Require production approvals through protected environments
- Keep deployment configuration versioned and reviewable

```text
PR -> test -> build -> scan -> dev -> stage -> production approval -> prod
```

The sample Python service exists to exercise the platform; the primary focus is pipeline design, container lifecycle, Kubernetes deployment, and promotion controls.
