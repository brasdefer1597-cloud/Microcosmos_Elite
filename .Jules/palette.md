## 2025-05-15 - [Terminal Input Accessibility]
**Learning:** Terminal-style "hacker" inputs often remove default focus rings (`outline: none`) for aesthetics, but fail to provide a replacement, making them invisible to keyboard users.
**Action:** Always pair `outline: none` with a visual focus indicator (like a glow or border color change) that fits the theme, and ensure `aria-label` is present when visible labels are "decorative" text.

## 2025-05-16 - [Dynamic Log Accessibility]
**Learning:** Auto-updating logs are invisible to screen readers without `aria-live`. Also, `overflow: hidden` on logs prevents users from reviewing history, which is a critical usability flaw for "terminal" interfaces.
**Action:** Use `role="log"` and `aria-live="polite"` for dynamic feeds. Always enable scrolling (`overflow-y: auto`) and ensure keyboard reachability (`tabindex="0"`) for scrollable containers.
