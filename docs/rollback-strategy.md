# Deployment Rollback Strategy

Production rollback should be fast, deterministic, and based on immutable artifacts.

## Trigger conditions

Rollback can be initiated when:
- health checks fail after deployment
- error rate or latency breaches release thresholds
- critical smoke tests fail
- a severe regression is confirmed

## Approach

1. Identify the previously known-good image digest or immutable tag.
2. Revert deployment metadata only; do not rebuild.
3. Monitor readiness, error rate, latency, and saturation.
4. Confirm recovery before closing the incident.
5. Preserve failed release artifacts for investigation.

Avoid "fix forward" during a severe production incident unless rollback is riskier than the defect.
