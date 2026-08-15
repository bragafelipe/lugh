# Lugh — Cloud Resource Utilization Management Platform

Lugh helps teams reduce cloud waste by detecting idle/underutilized resources and taking configurable actions (e.g., stop, schedule, rightsize workflows over time).

## Goals (initial)

- Detect idle/underutilized resources.
- Apply configurable policies to decide actions.
- Execute safe, auditable actions to reduce unnecessary cloud costs.

## Architecture principles

- Clear separation of concerns:
  - **Detection** (collect/analyze utilization signals)
  - **Policy/Decisioning** (rules, thresholds, approvals, safety)
  - **Actions** (stop/schedule/tag/notify)
- Extensible provider model for multi-cloud growth.
- Production-grade engineering: testing, CI/CD, IaC, observability, security.

## Repository structure

- `src/` application source
- `tests/` unit/integration tests
- `infra/` infrastructure-as-code
- `.github/workflows/` CI/CD
- `docs/` architecture, ADRs, runbooks

## Local development

See `docs/developer-setup.md`.
