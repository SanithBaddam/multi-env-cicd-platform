# Promotion Strategy

Every commit produces one immutable image identified by commit SHA. Environment promotion changes only deployment metadata; it does not rebuild the application.

Production should be protected by required reviewers, deployment concurrency controls, and a post-deployment health check. Rollback points to the previously known-good immutable tag.
