# Framework adapters

Use the existing project's conventions first. The adapter changes implementation details; it does not relax the workflow or quality gates.

## Plain HTML, CSS, and JavaScript

Keep tokens in a single CSS layer, use semantic elements, and keep interaction state in small functions. Use the bundled static verifier before browser inspection. Prefer native CSS transitions and respect prefers-reduced-motion.

## React and Next

Read package.json and the existing component library before importing anything. Keep server and client boundaries explicit. Put continuous pointer or scroll values in motion values or CSS, not a state update on every frame. Preserve routes, data fetching, and analytics hooks during redesigns.

## Vue, Svelte, and other frameworks

Match the project's component and state patterns. Do not transplant React APIs or invent a second token system. Keep the design contract framework-neutral and map it to the local primitives.

## Component libraries

Use the project's existing primitives when they already express the required semantics. If a library component fights the direction, wrap or theme it before replacing it. Do not mix multiple icon families or multiple radius languages without a documented reason.

## Browser evidence

Use the host browser, Playwright, or DevTools to capture the real route, viewport, theme, and state. A DOM query or successful build is not visual proof. If the host lacks browser access, report UNVERIFIED_RENDER and continue with source checks.
