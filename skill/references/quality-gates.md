# Quality gates

Use this file to write a verification report. A gate is pass, fail, or unverified; do not turn missing evidence into a pass.

## Product truth

- [ ] Product facts, prices, metrics, testimonials, and capabilities come from a source or are clearly marked as demo data.
- [ ] The primary user job and primary action are obvious in the first viewport.
- [ ] Content lengths are realistic at every target viewport.

## Visual system

- [ ] A direction contract exists and matches the shipped page.
- [ ] Components use semantic tokens, not scattered raw values.
- [ ] One type scale, spacing rhythm, radius rule, and accent strategy govern the page.
- [ ] The memorable moment has a user or product reason.
- [ ] No generic card wall, decorative glass layer, or gradient is carrying the entire design.

## Interaction and states

- [ ] Hover, focus-visible, pressed, disabled, and loading behavior are defined where relevant.
- [ ] Empty, error, success, validation, permission, and offline states are covered where the product can enter them.
- [ ] Long labels, long numbers, CJK, RTL, zoom, overflow, and reduced-content cases have an intentional result.
- [ ] Errors preserve user input and explain recovery.

## Accessibility

- [ ] Normal text contrast is at least 4.5:1; large text is at least 3:1.
- [ ] Keyboard traversal reaches every action in a sensible order.
- [ ] Focus is visible and never removed without a replacement.
- [ ] Controls have names, labels, roles, and state announcements where needed.
- [ ] Touch targets are at least 44 by 44 CSS pixels where applicable.
- [ ] Reduced motion is respected.

## Responsive and performance

- [ ] Rendered evidence exists at the product target plus 360, 390, 768, 1024, and 1280 when relevant.
- [ ] No horizontal overflow, clipped text, or accidental fixed-height collapse occurs.
- [ ] Images reserve space, use appropriate formats, and load intentionally.
- [ ] Expensive effects are bounded and do not block the primary task.
- [ ] Performance claims are marked unverified unless measured.

## Review output

For every failed or unverified item, record viewport, file or selector, observed evidence, impact, suggested repair, and status after repair. Use P0 blocking, P1 major, P2 minor, and P3 polish. Keep taste preferences separate from objective failures.
