---
name: frontier-ui-forge
description: Build, redesign, and audit high-fidelity web interfaces through a brief-first, multi-direction, design-contract, implementation, browser-evidence, and critique loop. Use when the user asks for a premium, distinctive, non-generic, polished, or less AI-looking website, landing page, dashboard, SaaS product, app shell, component, or existing-UI redesign.
---

# Frontier UI Forge

Create a deliberate interface and prove the rendered result. Treat taste as a sequence of decisions, evidence, and repairs rather than a decorative prompt.

## Operating contract

- Preserve repository instructions, routes, data flow, analytics hooks, component ownership, package manager, and existing design system unless the brief explicitly changes them.
- Separate product truth from visual direction. Never invent metrics, customers, testimonials, awards, capabilities, or domain facts to make a page feel finished.
- Make one visual thesis win. Generate alternatives when the brief is open, then commit to one direction and carry it through every surface and state.
- Prefer the smallest reliable tool chain. Use the existing framework and browser, DevTools, or Playwright capability. If a capability is unavailable, report the unverified item instead of claiming a pass.
- Keep a durable evidence trail in .frontier-ui/ when the project allows it: brief.md, directions/, contract.md, states.md, verification.md, and review.md.
- Give every preference a provenance, scope, and confidence: user instruction, repository evidence, rendered observation, or agent inference. Preserve unresolved “depends” decisions instead of turning silence into approval.

## Select a mode

- Build: the surface does not exist. Run the complete workflow.
- Redesign: preserve routes, behavior, content facts, and integration hooks. Scan first, diagnose second, repair in bounded slices.
- Component: define every state and variant the component can enter before polishing its appearance.
- Audit: inspect without editing unless the user asks for fixes. Separate observed defects, inferred risks, and taste decisions.
- Study: extract transferable visual mechanics from a reference; do not pixel-clone it.
- Handoff: produce a design contract and implementation-ready tokens/specs without writing production code.

## The workflow

### 1. Read the product before the pixels

Inspect project instructions, package metadata, routes, existing tokens, shared components, content sources, and the current rendered UI. Write a compact brief:

- surface and visitor mode: persuade, operate, read, or experience;
- audience, primary job, decision or action, and success evidence;
- product facts, brand constraints, accessibility requirements, and technical limits;
- content hierarchy, primary proof, primary action, and states the user can actually enter.

State one sentence of design intent: “Reading this as [surface] for [audience], with [visual language], optimized for [job].”

### 2. Create competing directions

For an open brief, create three to five directions before implementation. Each direction must define:

- composition: split, rail, stack, full-bleed, editorial grid, dense workspace, or another named structure;
- type: display/body pairing, scale, weight, casing, and measure;
- color: surface, text, accent, semantic status colors, and contrast plan;
- material: border, elevation, texture, imagery, illustration, or data treatment;
- motion: one meaningful transition or feedback moment, plus reduced-motion behavior.

Use a direction matrix. Any two directions must differ in at least three of those five axes. If two directions look interchangeable at thumbnail size, discard one. Do not default to purple gradients, generic glass cards, centered hero plus three equal cards, emoji icons, invented dashboard metrics, or decorative motion without a product reason.

When the user can review a preview, create an explicit compare surface with the same content and viewport for every direction. Record the selected direction and the reason. If no human checkpoint is possible, choose the highest-scoring direction and disclose that the selection was agent-made.

### 3. Freeze a design contract

Before broad implementation, write the contract:

- thesis, own-world metaphor, and one memorable moment;
- layout regions and priority order;
- primitive to semantic to component tokens;
- type scale, spacing scale, radius, border, elevation, and motion rules;
- real content shape and prohibited inventions;
- state matrix and responsive transformations;
- stack-specific implementation rules and a short anti-pattern list.

Use semantic tokens in components. A primitive change must flow through semantic tokens before reaching a component. Do not scatter raw color, radius, or timing values through markup.

### 4. Build the real experience

Implement against the existing stack. Start with the primary task and the dominant region, then add supporting content. Preserve working behavior in a redesign. Use real nouns, realistic lengths, and domain-appropriate examples.

For each interactive surface, decide which states apply:

- idle, hover, focus-visible, pressed, disabled;
- loading, empty, filtered-empty, error, success, queued, processing, permission, offline;
- mobile collapse, overflow, text scaling, and keyboard behavior.

Do not add irrelevant states merely to satisfy a checklist. Do not ship only the happy path.

### 5. Verify in a real viewport

Inspect the rendered page at relevant widths. Default probes are 360, 390, 768, 1024, and 1280 pixels; add the product's actual target viewport. Check:

- hierarchy, first viewport, content wrapping, overflow, and visual rhythm;
- focus order, keyboard operation, visible focus, semantic landmarks, labels, and alt text;
- contrast: 4.5:1 for normal text and 3:1 for large text;
- touch targets of at least 44 by 44 CSS pixels where applicable;
- loading, empty, error, success, and permission states;
- reduced motion, image dimensions, lazy loading, layout shift, and expensive effects;
- dark mode or theme variants only when the product requires them.

Batch desktop and mobile inspection before making a repair pass. Capture the actual rendered page, not a DOM-only assertion. If browser inspection is unavailable, mark the result UNVERIFIED_RENDER.

### 6. Run two independent reviews

Keep subjective design judgment separate from mechanical evidence.

Design review scores 0 to 10 for task fit, hierarchy, distinctiveness, coherence, content truth, state quality, responsive behavior, and emotional fit. List two strengths and three to five highest-impact changes.

Evidence review reports concrete findings with viewport, selector or file location, impact, and repair. The bundled static pass checks transition-all, dynamic viewport fallbacks, image alt attributes, raw colors outside token declarations, focus-visible, and reduced motion. Use the project's own lint, accessibility, browser, and content checks for labels, links, fixed widths, touch targets, and product truth.

The final score is not a vanity number. Any score below 8 needs a repair or a written reason. Stop after three repair rounds or when the last round produces no evidence-backed improvement.

Classify the delivery gate in four blocks: **Hard** (product truth, runtime, accessibility, overflow, dead interactions), **Purpose** (every unusual visual choice has a job), **Craft** (type, rhythm, tokens, states, responsive fit), and **Evidence** (rendered screenshots, interaction traces, console/network checks). A failed Hard block means `blocked`; any other failure means `needs repair`; only a clean set of blocks is `ready`. Keep a short evidence manifest with source, route, viewport, state, timestamp, and whether the claim is observed, measured, inferred, or still unverified.

### 7. Deliver and explain

Deliver the working interface plus a short report:

- selected direction and why it won;
- files changed and preserved behavior;
- state and viewport coverage;
- verification evidence and any UNVERIFIED items;
- remaining risks and the next smallest useful improvement.

Do not report “polished” without rendered evidence. Do not report “accessible” without naming the checks performed.

## Framework and tool guidance

Read references/framework-adapters.md when the project uses a named framework or component library. Read references/quality-gates.md when designing the review score or writing verification output. Read references/direction-matrix.md when the brief is open or the first concepts are too similar. Read references/example-brief.md for a complete example.

Use `<skill-root>/scripts/verify_frontier_ui.py` for a deterministic static pass when the deliverable is HTML, CSS, or JS. When working from the skill directory, this is `python3 scripts/verify_frontier_ui.py <path>`. It is a warning system, not a substitute for a real browser or a WCAG audit.

## Failure modes

- If the request is ambiguous but different interpretations would change the whole interface, ask one focused question. Otherwise make a stated assumption and proceed.
- If the repository has no browser or preview path, finish the implementation and report exactly what could not be verified.
- If a reference image, URL, or brand asset is missing, use transferable composition and material mechanics, not a fake reconstruction.
- If another auto-triggered UI Skill is active, use one orchestrator for the run. Do not let multiple Skills overwrite the same direction or review files.
- If a decision repeats across projects, promote the smallest reusable rule to a token, test, or reference; keep one-off taste judgments local to the current brief.
