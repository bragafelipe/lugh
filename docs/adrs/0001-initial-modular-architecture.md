# ADR-0001: Initial Modular Architecture

## Status
Accepted

## Context
Lugh must support safe automation now and multi-provider growth over time.

## Decision
Adopt a modular architecture with strict boundaries:
- detection
- policy decisioning
- action execution

## Consequences
- Easier provider extensibility
- Better testing isolation
- Clearer governance for risky action paths
