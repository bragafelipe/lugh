# Architecture — Lugh

## High-level components

- `detectors/`: resource utilization collectors and analyzers
- `policy/`: policy rules, thresholds, exceptions
- `actions/`: cloud action executors (stop/schedule/etc.)
- `orchestrator/`: workflow coordination and safety gates
- `audit/`: event logs and action trail
- `api/`: control plane API (future)

## Core separation

1. Detection produces normalized findings.
2. Policy evaluates findings and emits decisions.
3. Actions execute decisions with safeguards.

## Extensibility

Provider adapters implement interfaces for detection and actions.
