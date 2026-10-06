# Frontier UI Forge

**Frontier UI Forge** (`frontier-ui-forge`) is an evidence-driven frontend design and implementation skill for building distinctive, production-minded web interfaces.

It turns visual taste into a repeatable loop:

`brief → competing directions → design contract → implementation → browser evidence → independent review → repair`

The skill is designed for dashboards, SaaS products, app shells, landing pages, components, and existing UI redesigns. It preserves product truth, routes, data, analytics hooks, and existing design systems unless the brief explicitly changes them.

## What it adds

- Three to five genuinely different directions before implementation when the brief is open.
- A design contract for thesis, type, palette, rhythm, material, motion, states, and responsive behavior.
- Product-specific anti-slop checks instead of banning visual techniques blindly.
- Real state coverage: loading, empty, error, success, permission, offline, long content, and mobile transformations where applicable.
- Browser-first verification at relevant viewports with explicit `ready`, `needs repair`, or `blocked` outcomes.
- Separate design judgment from deterministic evidence checks.
- A small warning-only static verifier for HTML, CSS, and JavaScript examples.

## Install

For Claude-compatible skill directories, copy `skill/` into your skills directory. The distributable package is also included:

```bash
unzip frontier-ui-forge.skill -d ~/.claude/skills
```

Then invoke it with `frontier-ui-forge` when asking for a premium, distinctive, responsive, or audited frontend experience.

## Example

Open [`skill/examples/atlas-incident-console/index.html`](skill/examples/atlas-incident-console/index.html) for a complete incident-triage workspace with an evidence timeline, containment action, audit trail, responsive layout, focus styles, reduced-motion support, and a real interaction state.

Open [`skill/examples/atlas-incident-console/directions.html`](skill/examples/atlas-incident-console/directions.html) to see the direction-comparison gate that precedes implementation.

Run the deterministic pass:

```bash
python3 skill/scripts/verify_frontier_ui.py skill/examples/atlas-incident-console
```

## Repository layout

- `skill/SKILL.md` — the core agent instructions.
- `skill/references/` — direction, quality, framework, and example brief guidance.
- `skill/scripts/` — deterministic static checks.
- `skill/examples/` — runnable HTML examples.
- `frontier-ui-forge.skill` — packaged distributable.

## Research basis

The workflow synthesizes publicly documented ideas from Impeccable, better-react-web-ui, Tasteful Frontend, Taste, Design Distinctive UI, Anthropic frontend-design, UI/UX Pro Max, Incline, Hallmark, anti-slop systems, Tastemaker, Design Loop, screenshot-to-design-system, and Agentic Design System. Their ideas are used as design-process references; this repository does not copy their code or claim an independent benchmark.

The “100x” goal is an aspiration, not a measured guarantee. The skill reports what was rendered and checked instead of treating a style prompt or static lint result as proof of quality.
