## 2025-05-15 - [Terminal Input Accessibility]
**Learning:** Terminal-style "hacker" inputs often remove default focus rings (`outline: none`) for aesthetics, but fail to provide a replacement, making them invisible to keyboard users.
**Action:** Always pair `outline: none` with a visual focus indicator (like a glow or border color change) that fits the theme, and ensure `aria-label` is present when visible labels are "decorative" text.

## 2025-05-22 - [Dynamic Logs Accessibility]
**Learning:** Dynamic content areas like terminal logs are silent to screen readers by default. Using `aria-live="polite"` ensures updates are announced without interrupting the user.
**Action:** Always add `aria-live="polite"` and `role="log"` to real-time feed containers.
