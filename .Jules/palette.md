## 2025-05-15 - [Terminal Input Accessibility]
**Learning:** Terminal-style "hacker" inputs often remove default focus rings (`outline: none`) for aesthetics, but fail to provide a replacement, making them invisible to keyboard users.
**Action:** Always pair `outline: none` with a visual focus indicator (like a glow or border color change) that fits the theme, and ensure `aria-label` is present when visible labels are "decorative" text.

## 2025-05-16 - [Dynamic Terminal Log Accessibility]
**Learning:** Terminal interfaces often use `overflow: hidden` for aesthetics and dynamic content injection, making them inaccessible to screen readers and keyboard users who cannot scroll back.
**Action:** Use `role="log"` and `aria-live="polite"` for dynamic content containers. Ensure `overflow-y: auto` and `tabindex="0"` are set so keyboard users can access and scroll through the history.
