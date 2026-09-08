---
id: WISH-002
title: An agent that drops wishes from sourced intent
status: planned
source: human
beads:
  - FACTORY-022
---

# WISH-002: An agent that drops wishes from sourced intent

Human wish (2026-09-08): we need an agent that can create wishes for me.

The ready queue stays empty unless someone writes a wish file. The human
should not have to hand-author YAML. An agent transcribes sourced intent
(a chat message, a playtest note) into `docs/work-graph/wishes/WISH-NNN.md`
as `open`.

It does **not** invent wishes with no source, convert them into beads, or
start workers. Empty or missing intent means stop.
