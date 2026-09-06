# Delivery Architecture

```mermaid
flowchart LR
    Dev[Developer] --> PR[Pull Request]
    PR --> CI[Test / Lint / Scan]
    CI --> Registry[Immutable Container Image]
    Registry --> DevEnv[Dev]
    DevEnv --> Stage[Stage]
    Stage --> Gate[Production Approval]
    Gate --> Prod[Production]
```

## Key controls

The same immutable image is promoted across environments. Production should be protected by required reviewers, deployment concurrency, environment-scoped credentials, and post-deployment health checks.

GitHub Actions is the primary implementation, while Azure DevOps and Jenkins examples demonstrate portability across common enterprise CI/CD systems.
