## 2025-05-15 - [Terminal Input Accessibility]
**Learning:** Terminal-style "hacker" inputs often remove default focus rings (`outline: none`) for aesthetics, but fail to provide a replacement, making them invisible to keyboard users.
**Action:** Always pair `outline: none` with a visual focus indicator (like a glow or border color change) that fits the theme, and ensure `aria-label` is present when visible labels are "decorative" text.

## 2025-05-24 - [Scrollable Live Regions]
**Learning:** Auto-updating "terminal" divs (`overflow-y: hidden`) are inaccessible to screen reader users (who miss updates) and keyboard users (who can't scroll back).
**Action:** Use `role="log"` and `aria-live="polite"` for announcements, and add `tabindex="0"` plus `overflow-y: auto` to make the history navigable by keyboard.
